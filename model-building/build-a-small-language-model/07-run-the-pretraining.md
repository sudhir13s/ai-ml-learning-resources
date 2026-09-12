---
title: "Run the Pretraining"
id: lr-slm-run-the-pretraining
minutes: 26
core_idea: "The training loop is five decisions — what to decay, how the learning rate moves, how big the batch really is, what bounds a bad step, and which checkpoint you keep — and the last one is the only artifact that survives."
builds_on: [lr-slm-prove-the-gradient-path]
leads_to: [lr-slm-read-the-training-curves]
related: [pw-model-training]
section: "ai-ml-learning-resources"
workflow: "build-a-small-language-model"
chapter: 6
status: complete
template: workflow
category: model-building
---

# Run the Pretraining

The objective is one line, and it has not changed since 2018: **predict the next token**. Everything
interesting is in the five decisions around it.

```python
loss = F.cross_entropy(
    logits.view(-1, logits.size(-1)), targets.reshape(-1), ignore_index=-100
)
```

Targets are the inputs shifted one position left, so every position in the sequence is a training
example. A 256-token window is 256 predictions, not one.

```python
def next_batch(self) -> tuple[torch.Tensor, torch.Tensor]:
    """Draw one batch of windows uniformly at random from the stream."""
    starts = self._rng.integers(0, len(self._tokens) - self._block_size - 1, size=self._batch_size)
    inputs = np.stack([self._window(start, 0) for start in starts])
    targets = np.stack([self._window(start, 1) for start in starts])
```

Windows are sampled at random from one flat stream, packed end to end — **no padding, ever**. Every
token of every step does work. Documents are separated by the end-of-text id, which is what teaches
the model that a document ends.

---

## Decision one: decay matrices, not gains

```python
def build_optimizer(model: TransformerLM, config: TrainConfig) -> torch.optim.AdamW:
    """AdamW with decay applied to matrices only."""
    decayed = [p for p in model.parameters() if p.requires_grad and p.dim() >= 2]
    undecayed = [p for p in model.parameters() if p.requires_grad and p.dim() < 2]
    return torch.optim.AdamW(
        [
            {"params": decayed, "weight_decay": config.weight_decay},
            {"params": undecayed, "weight_decay": 0.0},
        ],
        lr=config.learning_rate,
        betas=(config.beta1, config.beta2),
    )
```

Weight decay pulls parameters toward zero. On a weight matrix that is regularisation. On a
**normalisation gain** it is something else: pulling a gain toward zero changes the function the
network computes, because that gain is the layer's output scale.

The dimension test is the cheap way to tell them apart — matrices are two-dimensional, gains and
biases are not.

`beta2 = 0.95` rather than the 0.999 default. Language-model gradients are noisier than the default
was tuned for, and a shorter second-moment window adapts faster.

---

## Decision two: warm up, then decay on a cosine

```python
def learning_rate_at(step: int, config: TrainConfig) -> float:
    """Linear warmup to the peak, then cosine decay to the floor, then flat at the floor."""
    if step < config.warmup_steps:
        return config.learning_rate * (step + 1) / max(1, config.warmup_steps)
    decay_steps = max(1, config.steps - config.warmup_steps)
    progress = min(1.0, (step - config.warmup_steps) / decay_steps)
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return config.min_learning_rate + cosine * (config.learning_rate - config.min_learning_rate)
```

**Warmup exists because Adam starts cold.** Its moment estimates are near zero for the first steps,
so the effective step size is enormous and a full learning rate there is where runs diverge. Two
hundred steps of ramp costs nothing.

**Cosine decay lands on a floor, not on zero.** A schedule that reaches zero stops learning before
the run ends; a floor of one tenth the peak keeps the last steps useful.

The shape, from the real run:

```text
step 0      lr 0.000001     (warmup, step 1 of 200)
step 300    lr 0.000299     (just past the peak)
step 600    lr 0.000287
step 900    lr 0.000260
step 1200   lr 0.000224
```

---

## Decision three: the batch is bigger than the batch

```python
optimizer.zero_grad(set_to_none=True)
step_loss = 0.0
for _ in range(config.accumulation_steps):
    inputs, targets = train_batcher.next_batch()
    _, loss = model(inputs, targets)
    (loss / config.accumulation_steps).backward()
    step_loss += float(loss.detach()) / config.accumulation_steps
    tokens_seen += train_batcher.tokens_per_batch
```

Gradients accumulate across micro-batches; the optimizer steps once. **The effective batch is
`batch_size × accumulation_steps`**, and memory only ever holds one micro-batch.

That is how a large-batch recipe runs on a small machine. The division by
`accumulation_steps` matters: without it the gradient is a *sum* rather than a *mean*, and the
effective learning rate scales with the accumulation count.

---

## Decision four: bound the damage of one bad batch

```python
torch.nn.utils.clip_grad_norm_(model.parameters(), config.grad_clip)
optimizer.step()
```

Clipping rescales the whole gradient when its global norm exceeds a threshold — **the direction is
preserved, only the length changes**. One outlier batch can otherwise take an enormous step and undo
an hour of progress in one update.

The order is not negotiable: clip after `backward()`, before `step()`.

---

## Decision five: which checkpoint you keep

This is the one that decides what you actually ship.

```python
def _maybe_evaluate(...) -> tuple[bool | None, float]:
    """Score the held-out split on the interval, keeping the checkpoint when it improved."""
    due = (step + 1) % config.eval_interval == 0 or step + 1 == config.steps
    if validation_batcher is None or not due:
        return None, best_validation
    validation_loss = estimate_loss(model, validation_batcher, config.eval_batches)
    if validation_loss >= best_validation:
        return False, best_validation
    save_checkpoint(checkpoint_path, model=model, optimizer=optimizer,
                    step=step + 1, best_validation_loss=validation_loss)
    return True, validation_loss
```

**The checkpoint kept is the best by held-out loss, not the last one.** The last step of a run is not
reliably its best, and a run that has begun to overfit should not overwrite the point where it
stopped generalising. The next chapter shows exactly that happening.

Beside it, early stopping:

```python
evaluations_without_improvement = 0 if improved else evaluations_without_improvement + 1
if evaluations_without_improvement >= config.patience:
    break
```

Three evaluations with no improvement ends the run. That is not a tuning nicety here — it is what
turned 3,000 requested steps into 1,250 actual ones and saved more than half the compute.

---

## Resume is part of the checkpoint, not an extra

```python
payload: dict[str, Any] = {
    "version": _FORMAT_VERSION,
    "config": asdict(model.config),
    "model": model.state_dict(),
    "optimizer": optimizer.state_dict(),
    "step": step,
    "best_validation_loss": best_validation_loss,
}
```

A checkpoint holding only weights **cannot resume a run**. Dropping the optimizer state restarts
Adam's moment estimates from zero; dropping the step restarts the learning-rate schedule from
warmup. Both are silent, and both cost more than the interruption did.

Two more properties worth copying:

- **The architecture travels with the weights**, and a mismatch is refused rather than loaded into
  the wrong shape.
- **`weights_only=True` on load.** A checkpoint is a pickle; unpickling one executes whatever it
  contains. Restricting the loader to tensors and plain containers is the difference between reading
  a file and running it.

```bash
PYTHONPATH=. python -m slmkit.cli train --preset scale --resume
```

---

## The run

```bash
PYTHONPATH=. python -m slmkit.cli run --preset scale --device cpu
```

```text
overfit-one-batch: 8.3961 -> 0.0066 in 200 steps (threshold 0.8318) [PASS]
training: 12,194,688 parameters (10,621,824 non-embedding); 1250 steps over 7,680,000 tokens in 737.69s
loss: 8.4187 -> 1.1681 train, 4.3772 best validation
```

Twelve minutes on a processor. On Apple's Metal the same command takes 7 min 16 s and produces the
**same text** and a held-out perplexity of 81.8950 against the processor's 81.8962 — the difference
is floating-point accumulation order, not a different model.

Seven and a half million tokens seen, over a training split of 294,181 — about twenty-six passes
through the corpus. Which is the subject of the next chapter.

## Pitfalls

- **Decaying normalisation gains.** It changes the function rather than regularising it.
- **No warmup.** Adam's cold start plus a full learning rate is the classic divergence.
- **Forgetting to divide by the accumulation count.** The effective learning rate silently scales.
- **Clipping in the wrong place.** After `backward()`, before `step()`.
- **Keeping the last checkpoint.** It is rarely the best one, and after overfitting starts it is
  reliably worse.
- **Saving weights without the optimizer state and step.** Resume then restarts cold, from warmup.
- **`torch.load` without `weights_only=True`.** A checkpoint is executable.

## Key takeaways

- **Next-token prediction over packed windows** — every position is an example, and no step is spent
  on padding.
- **Decay matrices only**; a gain is not a weight.
- **Warm up because Adam starts cold**, decay to a floor rather than to zero.
- **Accumulation makes the effective batch bigger than memory allows.**
- **Clip the global norm** to bound one bad batch.
- **Keep the best checkpoint by held-out loss, and stop when it stops improving** — 3,000 steps
  became 1,250.
- **A checkpoint that cannot resume is not a checkpoint.**

## References

- The implementation: `slmkit/training/loop.py` and `slmkit/training/checkpoint.py` in
  [small-language-model](/python/python-production-examples/small-language-model/readme)
- Loshchilov and Hutter, *Decoupled Weight Decay Regularization* — why AdamW exists:
  <https://arxiv.org/abs/1711.05101>
- Loshchilov and Hutter, *SGDR: Stochastic Gradient Descent with Warm Restarts* — the cosine
  schedule: <https://arxiv.org/abs/1608.03983>
- Deeper on the reusable mechanism:
  [Training (workflow)](/ai-ml/practitioner-workflows/training-and-adaptation/model-training/training)
