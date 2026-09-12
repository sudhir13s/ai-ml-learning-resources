---
title: "Prove the Gradient Path"
id: lr-slm-prove-the-gradient-path
minutes: 12
core_idea: "Train on one batch until the loss collapses: it takes seconds, it fails loudly, and it separates every bug that makes learning impossible from every hyperparameter that only makes it slow."
builds_on: [lr-slm-build-the-transformer]
leads_to: [lr-slm-run-the-pretraining]
section: "ai-ml-learning-resources"
workflow: "build-a-small-language-model"
chapter: 5
status: complete
template: workflow
category: model-building
---

# Prove the Gradient Path

Before spending twelve minutes on a training run, spend twelve seconds on this one.

Take a single batch. Train on only that batch, over and over. A correct model **memorises** it — the
loss has to fall to near zero, because nothing prevents a network with millions of parameters from
storing a few thousand tokens verbatim.

If it does not, the bug is upstream of every hyperparameter you were about to tune.

---

## What a failure here actually means

The loss failing to collapse on one batch is not a signal that training is hard. It is a signal that
**learning is impossible**, and there are only a handful of causes:

| The loss sits at the uniform-guess value | The loss falls slowly, or plateaus high |
|---|---|
| A tensor was detached from the graph | The learning rate is orders of magnitude off |
| Parameters are frozen that should not be | The optimizer never sees some parameters |
| Labels are shifted the wrong way | The loss masks almost everything |
| The output layer is disconnected | The batch is too large to memorise quickly |

Every one of those is invisible in a real training run, where a slowly falling loss looks like
progress. On one batch there is nowhere to hide.

---

## The threshold has to be a real number

"Near zero" is not checkable. The threshold here is expressed **relative to the loss of a uniform
guess** over the vocabulary, which is the number a model that has learned nothing produces:

```python
def uniform_loss(vocab_size: int) -> float:
    """Cross-entropy of a model that assigns every token equal probability."""
    return math.log(vocab_size)
```

For a 4,096-token vocabulary that is `ln(4096) = 8.3178`. The proof asks the model to reach **a tenth
of it**:

```python
threshold = threshold_fraction * uniform_loss(model.config.vocab_size)   # 0.1 × 8.3178 = 0.8318
```

Memorisation clears that comfortably. A broken gradient path sits at 8.3 and cannot move.

---

## The whole implementation

```python
def overfit_one_batch(
    model: TransformerLM,
    inputs: torch.Tensor,
    targets: torch.Tensor,
    *,
    steps: int = 200,
    learning_rate: float = 1e-3,
    threshold_fraction: float = 0.1,
) -> OverfitReport:
    """Train on a single batch and report whether the loss collapsed as it must."""
    threshold = threshold_fraction * uniform_loss(model.config.vocab_size)
    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)
    model.train()

    initial_loss = float("nan")
    final_loss = float("nan")
    for step in range(steps):
        optimizer.zero_grad(set_to_none=True)
        _, loss = model(inputs, targets)
        loss.backward()
        optimizer.step()
        final_loss = float(loss.detach())
        if step == 0:
            initial_loss = final_loss

    return OverfitReport(
        steps=steps,
        initial_loss=round(initial_loss, 4),
        final_loss=round(final_loss, 4),
        threshold=round(threshold, 4),
    )
```

Four sentences worth noticing:

- **A fresh model, not the one about to train.** The probe memorises a batch; starting the real run
  from that model would begin it already overfitted to four sequences.
- **A small batch, the same size for both presets.** Memorising four sequences is the cheapest
  observation that answers the question; a bigger batch only makes the same check slower.
- **A higher learning rate than training uses.** The job is to memorise fast, not to generalise.
- **`loss.detach()` before converting to a float.** Reading a tensor that still carries a gradient
  works and warns; detaching says what is meant.

---

## Where it sits in the pipeline, and why

```python
result.corpus = _run_corpus_stage(settings)
tokenizer, result.tokenizer = _run_tokenizer_stage(settings)
model = TransformerLM(settings.to_model_config(tokenizer.vocab_size)).to(device)
result.overfit = _run_overfit_stage(settings, ...)      # <- here
result.training = _run_training_stage(settings, model, train_batcher, device)
```

**Third of six.** After the tokenizer, because the probe needs real token ids at the real vocabulary
size — a proof on random integers would not catch a vocabulary mismatch. Before training, because
everything after it is expensive.

---

## What it prints

```bash
PYTHONPATH=. python -m slmkit.cli overfit --preset scale
```

```text
overfit-one-batch: 8.3961 -> 0.0057 in 200 steps (threshold 0.8318) [PASS]
```

Read it left to right. The model starts at **8.3961**, which is `ln(4096)` to two decimal places —
exactly the uniform guess, confirming the initialisation is sane. It ends at **0.0057**, which is
memorisation. The threshold it had to beat was **0.8318**.

The toy preset tells the same story at its own scale:

```text
overfit-one-batch: 6.2507 -> 0.065 in 200 steps (threshold 0.6238) [PASS]
```

`ln(512) = 6.238`, and the model starts at 6.2507.

**A failing proof exits non-zero**, so it can gate a pipeline rather than being read by a human:

```python
def _succeeded(result: PipelineResult) -> bool:
    """The run failed only when the overfit proof ran and did not clear its threshold."""
    return result.overfit is None or result.overfit.passed
```

---

## Two diagnostics that come free

The initial loss is a second check hiding inside the first. **It must equal the natural logarithm of
the vocabulary size.**

- **Much higher** — the output layer is badly initialised, or the logits are being scaled somewhere
  they should not be.
- **Much lower** — the model is already predicting something, which at step zero means a leak: the
  targets are visible in the inputs.

And the shape of the fall matters. A loss that drops instantly to zero on a *real* batch is usually
a leak too. Memorising a few thousand tokens should take tens of steps, not one.

## Pitfalls

- **Running the proof after training** — the run has already been paid for.
- **Reusing the probe model for the real run.** It has memorised four sequences.
- **Skipping it because the code "obviously" works.** The failures it catches are exactly the ones
  that look like working code.
- **A pass threshold of "near zero".** Anchor it to the uniform-guess loss so it is checkable.
- **Ignoring the initial loss.** It is a free initialisation and leakage check.

## Key takeaways

- **A correct model memorises one batch.** If it cannot, no hyperparameter will save the run.
- **Anchor the threshold to `ln(vocab_size)`** — the loss of a model that has learned nothing.
- **Run it third**: after the tokenizer, before training.
- **The initial loss should equal the uniform guess.** Higher means bad initialisation, lower means a
  leak.
- **Make it exit non-zero**, so it gates rather than informs.

## References

- The implementation: `slmkit/training/overfit.py` in
  [small-language-model](/python/python-production-examples/small-language-model/readme)
- Andrej Karpathy, *A Recipe for Training Neural Networks* — where "overfit one batch" is argued for
  at length, and free to read: <https://karpathy.github.io/2019/04/25/recipe/>
