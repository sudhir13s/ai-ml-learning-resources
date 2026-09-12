---
title: "Evaluate and Generate"
id: lr-slm-evaluate-and-generate
minutes: 20
core_idea: "Perplexity is the exponential of the mean next-token cross-entropy, it is only comparable within one tokenizer, and it says nothing about whether the model is useful — which is why the samples are printed beside it."
builds_on: [lr-slm-read-the-training-curves]
leads_to: [lr-slm-capabilities-and-limitations]
related: [pw-inference-and-decoding]
section: "ai-ml-learning-resources"
workflow: "build-a-small-language-model"
chapter: 8
status: complete
template: workflow
category: model-building
---

# Evaluate and Generate

Two questions, and they need different instruments.

**How surprised is the model by text it has never seen?** That is perplexity, and it is a number.

**Does it write anything?** That is generation, and it is a judgement — so the samples get printed
beside the number rather than replaced by it.

---

## Perplexity, exactly

```python
mean_loss = total_loss / total_tokens
perplexity = math.exp(mean_loss)
```

The exponential of the mean next-token cross-entropy. What makes it readable is that it comes out in
the units of a guess:

> A perplexity of 82 means the model is, on average, as uncertain as if it were choosing uniformly
> among 82 tokens.

Some anchors for this build's 4,096-token vocabulary:

| Perplexity | What it corresponds to |
|---|---|
| 4,096 | uniform guessing — a model that has learned nothing |
| 202 | the `toy` preset: 139,584 parameters, 200 steps |
| **82** | the `scale` preset: 12.2M parameters, 1,250 steps |
| 1 | perfect prediction, which on held-out text means a leak |

From 4,096 to 82 is a factor of fifty. That is real learning, and it is also a long way from a
production model on general English.

---

## Score every held-out token exactly once

```python
def sequential_batches(self, max_batches: int | None = None) -> list[...]:
    """Non-overlapping windows in order — how a held-out split is scored exactly once."""
    usable = (len(self._tokens) - 1) // self._block_size
```

Training samples windows at random, with replacement, because it wants variety. **Evaluation must
not.** Overlapping windows count some tokens twice, random windows count some zero times, and either
makes the number depend on the draw rather than on the model.

Non-overlapping, in order, once each:

```text
held-out test: loss 4.4055, perplexity 81.8962 over 17,152 tokens
```

Seventeen thousand one hundred and fifty-two — the test split, to the token.

---

## Two properties of perplexity that are easy to get wrong

**It is tokenizer-relative.** The measure is per token, so two models with different vocabularies are
not being asked the same question. A tokenizer that compresses better produces fewer, harder
predictions and a *higher* perplexity on identical text and identical quality. Comparing this
project's 81.9 to a published number from a different vocabulary is meaningless, and it is done
constantly.

**It rewards fluency, not usefulness.** Perplexity measures how well the model predicts the next
token of a corpus. That is exactly the right question for a base model, which is what this course
trains. It is the wrong question for a chat model, which is scored on whether it followed the
instruction — and that is why the next course changes the instrument rather than the threshold.

---

## Decoding: three controls, applied in order

```python
if temperature <= 0.0:
    return logits.argmax(dim=-1, keepdim=True)
scaled = logits / temperature
if top_k > 0:
    scaled = _mask_below_top_k(scaled, top_k)
probabilities = torch.softmax(scaled, dim=-1)
if 0.0 < top_p < 1.0:
    probabilities = _mask_outside_nucleus(probabilities, top_p)
```

Each narrows what the one before it left.

- **Temperature** rescales the logits. Below one it sharpens toward the argmax; above one it
  flattens. At zero this switches to greedy decoding rather than dividing by zero.
- **Top-k** keeps the k highest-scoring tokens. Blunt: the same k whether the model is confident or
  not.
- **Top-p (nucleus)** keeps the smallest set whose probability sums past p. It *adapts* — wide where
  the model is unsure, narrow where it is confident — which is why it is the default in most serving
  stacks.

The nucleus mask has one detail worth stating, because getting it wrong empties the row:

```python
remove = cumulative - sorted_probs > top_p
```

The shift keeps the first token *above* the threshold inside the nucleus. Without it, a single token
carrying more than `top_p` of the mass would be excluded and there would be nothing left to sample.

---

## Reproducibility is a design decision, not a side effect

```python
drawn = torch.multinomial(probabilities.float().cpu(), num_samples=1, generator=generator)
return drawn.to(logits.device)
```

The draw happens on the processor's generator whatever device the model is on. A generator is bound
to one device and the accelerator streams do not reproduce each other, so **drawing here is what
makes a seeded sample identical on processor, Metal and CUDA.**

That is what lets a README quote generated text as a result rather than as a screenshot — and it is
how this course knows the Metal and processor runs produced the same output.

The context is also cropped to the window before every step:

```python
window = idx[:, -model.config.block_size :]
```

Positions beyond the trained window have never been seen by the rotary tables. Feeding them produces
confident nonsense rather than an error, which is worse.

---

## What it writes

```bash
PYTHONPATH=. python -m slmkit.cli run --preset scale --device cpu
```

```text
--- prompt: 'KING RICHARD' ---
w with her. The:
I will have any man so soon have I:
That I did do this; and what I come,
Your noble father's love would have heard.

--- prompt: 'First Citizen:' ---

I will see't
the we might have made a gentleman to tell you,
you he give him well a wife as his son:
So, as you have you done this?
```

Look at what is present and what is absent.

**Present.** The speaker-colon-speech format. Line breaks near the length of a verse line. Subject
and verb agreeing. Period vocabulary and syntax — *"I will see't"*, *"Your noble father's love"*.
Punctuation used the way the corpus uses it.

**Absent.** Meaning. *"the we might have made a gentleman to tell you"* has the cadence of the
corpus and says nothing. There is no thread across sentences, no fact, no argument.

That gap is the honest description of a twelve-million-parameter model trained on a million
characters: **it learned the shape of the language and none of its content.** Compare the toy
preset, which learned neither:

```text
--- prompt: 'KING RICHARD' ---
 herela Aoryt then
Bn
Lingnd t thef deing a mul: ofsay
```

Two models, the same pipeline, and the difference between them is capacity and steps.

---

## Evaluating without a reference

At this scale there is no ground-truth answer to compare against, so three cheap checks carry most
of the signal:

- **Read ten samples.** Format, grammar and vocabulary are visible immediately, and they are what
  changed between the two presets above.
- **Vary the temperature.** At 0.2 the model should be repetitive; at 1.2 it should degrade. A model
  that looks the same at both is not modelling a distribution.
- **Check the perplexity moved.** From `ln(vocab)` toward something much lower, on text held out
  correctly.

Anything more demanding — helpfulness, factuality, instruction following — needs a model that has
been taught a task. That is the next course.

## Pitfalls

- **Comparing perplexity across tokenizers.** Different vocabulary, different question.
- **Evaluating on overlapping or random windows.** The number then depends on the draw.
- **Reporting perplexity without samples.** It cannot tell you the model writes nothing readable.
- **Sampling with the accelerator's generator.** The seed stops reproducing across devices.
- **Feeding a prompt longer than the trained window.** Confident nonsense, no error.
- **Reading a perplexity near 1 as excellence.** On held-out text it is a leak.

## Key takeaways

- **Perplexity is the exponential of the mean next-token cross-entropy** — an effective branching
  factor, 4,096 down to 82 here.
- **Score each held-out token exactly once**, in order, non-overlapping.
- **It is tokenizer-relative and fluency-shaped** — right for a base model, wrong for a chat model.
- **Temperature, then top-k, then nucleus** — each narrows what the last one left.
- **Draw on the processor's generator** so a seeded sample is reproducible across devices.
- **The samples show what the number cannot:** this model learned the shape of the language and
  none of its content.

## References

- The implementation: `slmkit/evaluation/perplexity.py` and `slmkit/model/sampling.py` in
  [small-language-model](/python/python-production-examples/small-language-model/readme)
- Holtzman et al., *The Curious Case of Neural Text Degeneration* — where nucleus sampling comes
  from: <https://arxiv.org/abs/1904.09751>
- Deeper on the reusable mechanism:
  [Inference and Decoding (workflow)](/ai-ml/practitioner-workflows/inference-and-serving/inference-and-decoding/inference-and-decoding)
