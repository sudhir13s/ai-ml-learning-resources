---
title: "Run Supervised Fine-Tuning"
id: lr-scm-run-supervised-fine-tuning
minutes: 20
core_idea: "One thirty-line adapter turns the base model into something three separate toolkits can train, which is the difference between composing a pipeline and writing a fourth copy of everything in it."
builds_on: [lr-scm-build-the-instruction-data]
leads_to: [lr-scm-align-on-preferences]
related: [lr-fine-tuning-build-the-supervised-fine-tuning-baseline]
section: "ai-ml-learning-resources"
workflow: "build-a-small-chat-model"
chapter: 4
status: complete
template: workflow
category: model-adaptation
---

# Run Supervised Fine-Tuning

The training loop for this stage is not written here. It exists, it is tested, and it belongs to
[fine-tuning-toolkit](/python/python-production-examples/fine-tuning-toolkit/readme).

What stands between "it exists" and "we can call it" is a **calling-convention mismatch** — and how
you resolve that is the difference between composing a pipeline and forking one.

---

## The mismatch, stated exactly

The base model's forward is the plain PyTorch shape:

```python
logits, loss = model(idx, targets)          # a tuple
```

All three toolkits speak the other common dialect, the one the Hugging Face causal-language-model
classes established:

```python
output = model(input_ids=..., attention_mask=..., labels=...)
output.loss                                  # an object with named fields
output.logits
```

Three ways out, and only one is right:

| Option | Cost |
|---|---|
| Change the base model's forward | breaks `small-language-model`, whose own tests and pipeline use it |
| Fork each toolkit | three forks to keep in step forever |
| **Write an adapter** | **about thirty lines, in one place** |

---

## The adapter

```python
class CausalLMAdapter(nn.Module):
    """Presents a ``TransformerLM`` through the causal-language-model calling convention."""

    def __init__(self, model: TransformerLM) -> None:
        super().__init__()
        self.model = model

    def forward(
        self,
        input_ids: Tensor,
        attention_mask: Tensor | None = None,
        labels: Tensor | None = None,
    ) -> CausalLMOutput:
        """Run the base model and, when labels are supplied, compute the shifted causal loss."""
        logits, _ = self.model(input_ids)
        if labels is None:
            return CausalLMOutput(logits=logits)
        shifted_logits = logits[:, :-1, :].reshape(-1, logits.size(-1))
        shifted_labels = labels[:, 1:].reshape(-1)
        loss = F.cross_entropy(shifted_logits, shifted_labels, ignore_index=IGNORE_INDEX)
        return CausalLMOutput(logits=logits, loss=loss)
```

That is the whole seam, and it serves all three toolkits:

- `ftkit.training.loop.train` calls `model(**batch).loss`
- `rlhfkit.modeling.logprob.batch_sequence_logprob` calls `model(...).logits`
- `mckit.compression.quantize.dynamic_quantize` takes any `nn.Module`, so it needs nothing

---

## The shift is the detail that decides correctness

```python
shifted_logits = logits[:, :-1, :]
shifted_labels = labels[:, 1:]
```

**The toolkits pass labels aligned with `input_ids`** — label position *i* is the target *at* position
*i* — and expect the model to shift internally, exactly as the Hugging Face classes do.

Get this off by one and the model trains, the loss falls, and it predicts the wrong token at every
position. There is no error and no warning; the generations are simply wrong in a way that looks like
undertraining. So it is asserted:

```python
def test_the_loss_shift_matches_next_token_prediction(model: CausalLMAdapter) -> None:
    """Position i's logits are graded against label i+1 — off by one and everything still runs."""
    output = model(input_ids=input_ids, labels=labels)
    expected = torch.nn.functional.cross_entropy(
        output.logits[:, :-1, :].reshape(-1, model.vocab_size),
        labels[:, 1:].reshape(-1),
        ignore_index=IGNORE_INDEX,
    )
    assert torch.allclose(output.loss, expected)
```

---

## Why `attention_mask` is accepted and ignored

The parameter is in the signature because the toolkits pass it. It is not used, and the reason is a
property of this specific combination rather than laziness:

- **The base model attends causally.** A token can only see positions before it.
- **The toolkits right-pad.** Every pad sits *after* the real tokens.

A real token therefore never attends to a pad, because causal masking already excludes everything
later in the sequence. Pad positions in the labels are already `-100`, so they contribute nothing to
the loss either.

**Left-padding would break that argument entirely** — pads would sit before real tokens, inside the
causal window. The adapter's docstring says "right-padding" for exactly this reason, rather than
leaving the next reader to discover the constraint.

---

## Freeze most of the model

```python
def freeze_all_but_last_layers(model: CausalLMAdapter, layers: int) -> int:
    """Freeze everything except the final ``layers`` transformer blocks and the output norm."""
    total_blocks = len(model.model.blocks)
    keep_from = max(0, total_blocks - layers)
    for parameter in model.parameters():
        parameter.requires_grad_(False)
    for index in range(keep_from, total_blocks):
        for parameter in model.model.blocks[index].parameters():
            parameter.requires_grad_(True)
    for parameter in model.model.final_norm.parameters():
        parameter.requires_grad_(True)
    return trainable_parameter_count(model)
```

Full fine-tuning a twelve-million-parameter model on twenty-four conversations **overwrites the
language it learned in pretraining**. Freezing the bottom of the stack is the cheapest defence that
needs no adapter implementation:

```text
fine-tuned: 3,540,864 of 12,194,688 parameters trainable (29.0% of the model)
```

Two blocks out of six, plus the final normalisation. The intuition is the standard one: **early
layers carry general language, later layers carry task-shaped behaviour**, so freezing the early ones
protects what pretraining bought.

The better answer at real scale is LoRA — a fraction of a per cent trainable rather than 29% — and
`ftkit` owns it. This build uses the layer freeze because it needs no adapter injection into a
custom architecture, and because it makes the next chapter's regression number honest: **29% is a
lot, and the regression will show it.**

---

## The call

```python
def run_supervised_fine_tuning(...) -> TrainReport:
    """Freeze all but the top blocks, then hand the rows to `ftkit`'s training loop."""
    freeze_all_but_last_layers(model, trainable_layers)
    return train(
        model,
        [to_ftkit_record(record) for record in records],
        config,
        device=device,
        pad_id=pad_id,
    )
```

Five lines. Everything about the optimizer, the schedule, the sampling and the accumulation is the
toolkit's, tested in its own project.

The row translation is three fields:

```python
return TokenizedRecord(
    input_ids=record.input_ids,
    labels=record.labels,
    n_prompt_tokens=len(record.input_ids) - record.graded_tokens,
    n_response_tokens=record.graded_tokens,
)
```

Reporting the graded count as the response length keeps `graded_fraction` honest for a multi-turn
row, where the graded tokens are several separate spans rather than one tail.

---

## Running it

```bash
PYTHONPATH=$COMPOSED python -m chatkit.cli finetune
```

```text
templated: 24 records (8 multi-turn), 54.6% of tokens graded
fine-tuned: 3,540,864 of 12,194,688 parameters trainable (29.0% of the model); 120 steps; final loss 0.8180
```

Eleven seconds on a processor. The final loss of 0.8180 is on the **graded spans only** — it is the
model's cross-entropy on assistant answers, not on the whole sequence, so it is not comparable to the
pretraining loss from the previous build.

---

## Composition, as a habit

The general shape of this chapter is worth taking away independent of language models:

> When an existing implementation is right but its interface is wrong, **adapt the interface**. Do
> not fork the implementation, and do not change the thing it was written for.

The adapter is testable on its own, it lives in one file, and its constraints are written down. Three
forks would have been none of those things, and the fourth copy of a training loop is where the bugs
that survive live.

## Pitfalls

- **Shifting labels the wrong way, or twice.** Everything still runs; the model is simply wrong.
- **Left-padding into a causal model without a mask.** The pads are then inside the visible window.
- **Full fine-tuning on a small set.** It overwrites pretraining, and the regression check will say
  so.
- **Forking the toolkit to fit your model.** Three forks, forever.
- **Comparing the fine-tuning loss to the pretraining loss.** Different denominators — one is graded
  spans, the other is every token.

## Key takeaways

- **An adapter is the right answer to a calling-convention mismatch** — thirty lines, one file,
  three consumers.
- **The label shift decides correctness and fails silently.** Assert it.
- **`attention_mask` is safe to ignore here because causal plus right-padding already excludes the
  pads** — and that is a property to state, not to assume.
- **Freeze most of the model on a small set.** LoRA is better and the toolkit owns it.
- **Five lines call a tested loop.** That is the whole point of composing.

## References

- The implementation: `chatkit/adapter.py` and `chatkit/stages/finetune.py` in
  [small-chat-model](/python/python-production-examples/small-chat-model/readme)
- The loop it calls: `ftkit/training/loop.py` in
  [fine-tuning-toolkit](/python/python-production-examples/fine-tuning-toolkit/readme)
- Deeper on the reusable mechanism:
  [Build the Supervised Fine-Tuning Baseline (workflow)](/ai-ml/ai-ml-learning-resources/model-adaptation/fine-tuning/build-the-supervised-fine-tuning-baseline)
