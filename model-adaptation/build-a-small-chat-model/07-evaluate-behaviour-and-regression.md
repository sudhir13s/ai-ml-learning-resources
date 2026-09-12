---
title: "Evaluate Behaviour and Regression"
id: lr-scm-evaluate-behaviour-and-regression
minutes: 20
core_idea: "Measure what the fine-tune bought and what it cost in the same breath — a chat evaluation that never looks back at the base capability cannot see the trade it just made."
builds_on: [lr-scm-align-on-preferences]
leads_to: [lr-scm-quantize-and-serve-the-chat-loop]
related: [lr-fine-tuning-evaluate-capability-and-regression]
section: "ai-ml-learning-resources"
workflow: "build-a-small-chat-model"
chapter: 6
status: complete
template: workflow
category: model-adaptation
---

# Evaluate Behaviour and Regression

Perplexity was the right instrument for a base model. It is the wrong one here: a chat model is
scored on whether it did what it was asked, and perplexity cannot see that.

So this stage asks two questions, and reports both on the same line of output.

---

## Question one: did it learn the behaviour?

At twelve million parameters and twenty-four conversations, the honest measurable behaviour is
**format adherence**: given a held-out prompt in the chat format, does the model answer and then stop
at the end marker?

```python
return ModelScores(
    name=name,
    stopped_cleanly=sum(1 for reply in replies if reply.stopped_cleanly),
    prompts=len(replies),
    mean_reply_tokens=round(
        sum(reply.tokens_generated for reply in replies) / max(1, len(replies)), 1
    ),
    perplexity=report.perplexity,
)
```

It is crude, and it is the right crudeness. **Claiming to measure helpfulness would be claiming more
than the run supports** — a model this size trained on this much data learns a format, not a skill,
and an evaluation that pretends otherwise is the dishonest part of most small fine-tuning write-ups.

The base model gives a clean baseline for free: it has never seen the end marker, so it cannot
produce one, so its format adherence is exactly zero.

```text
format adherence: base 0% -> chat 100% over 6 held-out prompts
reply length: base 64.0 -> chat 19.8 tokens
```

**Those two lines are the same fact measured twice.** The base model runs to the token budget on
every prompt because nothing tells it to stop. The chat model stops on its own after about twenty
tokens.

Reply length is the more useful of the two in practice, because it is continuous. Adherence is six
prompts and therefore only ever takes seven values; length moves smoothly and shows partial progress
during a run that has not finished learning.

---

## Question two: what did it cost?

```python
@property
def perplexity_regression(self) -> float:
    """How much held-out language modelling it cost. Positive means the base got worse."""
    return self.chat.perplexity - self.base.perplexity
```

The same held-out **pretraining** test split, scored before and after:

```text
regression check (pretraining perplexity): base 81.89 -> chat 243.84
```

**Three times worse.** Twenty-four conversations moved three and a half million parameters, and
general language modelling paid for it.

That is a large regression and the project says so rather than burying it. It is also entirely
expected, and the previous chapters named the three reasons in advance:

- **29% of the model was trainable.** A layer freeze is a much blunter instrument than LoRA.
- **Twenty-four examples is a tiny, narrow distribution.** Everything the model sees for 120 steps is
  question-and-answer about stagecraft.
- **No pretraining text was mixed into the fine-tuning data.** The standard mitigation, and this
  build does not use it, so the effect is visible at full strength.

---

## Why both numbers have to be on the same line

This is the point of the chapter.

An evaluation that reports only *"format adherence 0% → 100%"* is true, and it is the kind of true
that gets a model shipped. The reader learns that fine-tuning worked and nothing about what it did to
everything else.

**Catastrophic forgetting is not exotic.** It is the default outcome of fine-tuning a small model on
a small, narrow set, and it is invisible unless something specifically looks for it. The only
reliable way to see it is to keep the base capability's own evaluation and re-run it afterwards.

```python
@dataclass(frozen=True, slots=True)
class ComparisonReport:
    """Base against chat, plus the verdict a caller can act on."""

    base: ModelScores
    chat: ModelScores
```

Both models, both metrics, one object. There is no way to print the win without the cost.

---

## Reading the four numbers together

| | Base | Chat | Reading |
|---|---|---|---|
| Format adherence | 0% | 100% | the behaviour was learned |
| Mean reply tokens | 64.0 | 19.8 | it learned to stop |
| Pretraining perplexity | 81.89 | 243.84 | it cost three times the general ability |
| Preference accuracy | — | 1.00 | separable pairs; mechanism works |

**Is this trade acceptable?** It depends entirely on what the model is for, and that is the honest
answer rather than a hedge:

- **A narrow assistant in one domain** — probably yes. General fluency outside that domain is not
  what it is for.
- **A general assistant** — certainly not. A three-times regression means it has become worse at
  everything it is not being asked about.

Naming the trade is what lets someone else decide. Hiding it decides for them.

---

## Reducing the regression

In descending order of effect, and none of these is applied in this build — each is a change a reader
can make:

- **Mix pretraining text into the fine-tuning set.** The standard mitigation: a few per cent of raw
  corpus keeps the base distribution in the loss.
- **Train fewer parameters.** LoRA at a fraction of a per cent instead of a layer freeze at 29%.
  `ftkit` owns it.
- **More instruction data.** Twenty-four examples is a very narrow window onto the behaviour.
- **Fewer steps, or a lower learning rate.** Less movement, less forgetting, and less of the
  behaviour.

Each is a lever, and the regression number is how you find out whether pulling it worked.

---

## What is deliberately not measured

- **Helpfulness.** No model-judged or human-judged quality score, because the replies do not mean
  anything and scoring them would be theatre.
- **Safety.** No refusal training was done, so there is nothing to evaluate.
- **Multi-turn coherence.** The chat loop in the next chapter shows it; nothing scores it.

All three are real stages of real post-training. Leaving them out and saying so is different from
leaving them out.

## Pitfalls

- **Reporting only the win.** The regression is invisible unless something looks for it.
- **Using perplexity to score a chat model.** It measures fluency, not instruction following.
- **Evaluating on training prompts.** Six held-out prompts is few; zero is fatal.
- **Adherence without length.** Length is continuous and shows partial progress.
- **Fine-tuning without keeping the base evaluation.** You then cannot answer the second question at
  all.

## Key takeaways

- **Format adherence is the honest behaviour measure at this scale**, and reply length is the same
  fact in a more useful form.
- **A regression check is not optional.** Three times worse pretraining perplexity is the price this
  run paid.
- **Report the win and the cost in the same output.** Anything else decides for the reader.
- **The trade is acceptable or not depending on what the model is for** — name it and let someone
  choose.
- **Mixing pretraining text into the fine-tuning set is the standard mitigation**, and this build
  deliberately omits it so the effect is visible.

## References

- The implementation: `chatkit/evaluation.py` in
  [small-chat-model](/python/python-production-examples/small-chat-model/readme)
- Deeper on the reusable mechanism:
  [Evaluate Capability and Regression (workflow)](/ai-ml/ai-ml-learning-resources/model-adaptation/fine-tuning/evaluate-capability-and-regression)
- Kirkpatrick et al., *Overcoming catastrophic forgetting in neural networks*:
  <https://arxiv.org/abs/1612.00796>
