---
title: "Align on Preferences"
id: lr-scm-align-on-preferences
minutes: 20
core_idea: "Direct preference optimization cancels the reward model by substituting the policy's own implicit reward into the preference loss, leaving one supervised-style objective and a frozen reference that acts as the leash."
builds_on: [lr-scm-run-supervised-fine-tuning]
leads_to: [lr-scm-evaluate-behaviour-and-regression]
related: [pw-preference-alignment]
section: "ai-ml-learning-resources"
workflow: "build-a-small-chat-model"
chapter: 5
status: complete
template: workflow
category: model-adaptation
---

# Align on Preferences

Supervised fine-tuning can say *"produce this answer"*. It cannot say *"prefer this answer to that
one"*, and most of what separates a usable assistant from a merely trained one is exactly that
preference — length, tone, register, when to stop, when to decline.

This stage is owned by [rlhf-alignment](/python/python-production-examples/rlhf-alignment/readme).
This chapter explains what it does and what this build has to get right to call it correctly.

---

## What direct preference optimization is

The classical path is reinforcement learning from human feedback: train a reward model on preference
pairs, then optimise the policy against it with reinforcement learning. Three moving parts, a reward
model that can be gamed, and a training loop that is famously fiddly.

**Direct preference optimization removes the middle part** with one observation: the reward is
*implicit in the policy*.

```text
r(x, y) = beta * (log pi_theta(y|x) - log pi_ref(y|x))
```

Substitute that into the Bradley-Terry preference loss and the reward model cancels. What is left is
a single supervised-style objective over the policy and a frozen reference:

```python
def dpo_loss(policy_chosen_logp, policy_rejected_logp,
             reference_chosen_logp, reference_rejected_logp, *, beta):
    """The DPO loss and the two implicit rewards, for a batch of (chosen, rejected) log-prob pairs."""
    reward_chosen = beta * (policy_chosen_logp - reference_chosen_logp)
    reward_rejected = beta * (policy_rejected_logp - reference_rejected_logp)
    loss = -F.logsigmoid(reward_chosen - reward_rejected).mean()
    return loss, reward_chosen.detach(), reward_rejected.detach()
```

Every step does one thing: **raise the policy's probability of the chosen answer and lower it for the
rejected one, relative to the reference.**

The reference is the leash. Without it the policy could satisfy every preference by collapsing onto a
single output; `beta` is how tightly it is held.

---

## The reference is the fine-tuned model, not the base

```python
def run_preference_alignment(policy, rows, config, *, device, pad_id) -> TrainReport:
    """Snapshot the fine-tuned model as the reference, then hand both to `rlhfkit`."""
    reference = policy.clone_frozen()
    return train_dpo(policy, reference, rows, config, device=device, pad_id=pad_id)
```

This is a decision, not a default. **The reference is a frozen copy of the policy as it is now** —
after supervised fine-tuning.

Using the pretrained base as the reference would let the policy drift back across everything
fine-tuning taught it, because the leash would be pulling toward a model that does not know the chat
format at all. Preference optimization is meant to *nudge an already-usable model*, and the reference
encodes where "already usable" is.

The copy also has to be a real copy:

```python
def clone_frozen(self) -> CausalLMAdapter:
    """A detached, frozen copy — the reference policy direct preference optimization needs."""
    reference = copy.deepcopy(self)
    for parameter in reference.parameters():
        parameter.requires_grad_(False)
    reference.eval()
    return reference
```

Without `deepcopy` the policy and the reference are the same object, every margin is exactly zero,
and the loss is constant. That failure is silent: the run completes and changes nothing.

---

## The boundary that decides whether the numbers mean anything

Preference optimization scores **the answer tokens only**. The prompt is the condition, not part of
what is being compared, so `prompt_len` has to be the exact token index where the answer begins.

```python
prompt_text = render_prompt(pair.prompt_turns)
prompt_ids = tokenizer.encode(prompt_text)
chosen_ids = prompt_ids + tokenizer.encode(f"{pair.chosen}{END_MARKER}")
rejected_ids = prompt_ids + tokenizer.encode(f"{pair.rejected}{END_MARKER}")
```

The prompt is encoded **once** and both sides are built on it. Its length is then exact by
construction, rather than found by searching a token stream — the same argument as the masking
chapter, for the same reason.

And an over-long pair is dropped rather than trimmed:

```python
if len(chosen_ids) > max_seq_len or len(rejected_ids) > max_seq_len:
    # Truncating a preference row would move the answer boundary and silently change what
    # is being compared, so an over-long pair is dropped rather than trimmed.
    continue
```

Truncation moves the boundary. A row whose boundary has moved is comparing something other than what
you wrote, and it is indistinguishable from a correct row in every log.

---

## The learning rate is small on purpose

```python
dpo_learning_rate: float = 5e-5      # against 3e-4 for supervised fine-tuning
```

Six times smaller. This stage nudges a model that already works; a large step here undoes
fine-tuning to satisfy eight preference pairs, which is the classic way an aligned model gets worse
at everything it was previously good at.

`beta` at 0.1 is the field default and it is the other half of the same control: higher holds the
policy closer to the reference, lower lets it move further.

---

## Running it

```bash
PYTHONPATH=$COMPOSED python -m chatkit.cli align
```

```text
aligned: 40 steps; preference accuracy 1.00; reward margin 8.6404
```

Two numbers, and both need reading carefully.

**Preference accuracy 1.00** — the policy assigns higher implicit reward to the chosen answer on
every pair. On eight pairs whose chosen and rejected answers differ in length, vocabulary and
subject, that is **separable data rather than an aligned model**. It shows the mechanism runs and the
direction is right.

**Reward margin 8.6404** — `beta * ((policy_chosen - ref_chosen) - (policy_rejected - ref_rejected))`.
A positive and growing margin is the signal that the objective is being optimised. Its magnitude is
not meaningful on eight pairs.

The project's own test asserts only what the numbers support:

```python
def test_preference_alignment_separates_chosen_from_rejected(...) -> None:
    report = run_preference_alignment(...)
    assert report.steps == 8
    assert report.final_reward_margin > 0.0
```

---

## What real alignment adds

This build shows the mechanism at the smallest honest scale. A production alignment stage adds:

- **Thousands of pairs**, where the difference is a matter of judgement rather than obvious.
- **A win rate against a held-out set**, judged by humans or a model, rather than training-set
  accuracy.
- **A regression suite**, because alignment routinely costs capability elsewhere — the next chapter
  measures exactly that for the fine-tuning stage.
- **Reward-hacking checks.** Length bias is the classic one: preferring longer answers because
  judges do, until the model pads everything.

`rlhf-alignment` also implements **group-relative policy optimization** over a Bradley-Terry reward
model, which is the online counterpart to this offline method, and its own README is where that
comparison belongs.

## Pitfalls

- **Using the base model as the reference.** The policy drifts back across the fine-tune.
- **A reference that is not a deep copy.** Margins are zero and the run silently does nothing.
- **Truncating a preference row.** The answer boundary moves and the comparison changes.
- **A supervised-sized learning rate.** It undoes fine-tuning to satisfy a handful of pairs.
- **Reporting training-set preference accuracy as alignment.** On separable data it is 1.00.
- **Ignoring length bias.** Preferring longer answers is the easiest reward to hack.

## Key takeaways

- **Direct preference optimization cancels the reward model** by substituting the policy's implicit
  reward into the preference loss.
- **The frozen reference is the leash**, and it should be the fine-tuned model, not the base.
- **Score the answer tokens only** — encode the prompt once, and drop rather than truncate.
- **Use a small learning rate.** This stage nudges; it does not teach.
- **1.00 accuracy on eight separable pairs means the machinery works**, not that the model is
  aligned.

## References

- The implementation this build calls: `rlhfkit/training/dpo.py` in
  [rlhf-alignment](/python/python-production-examples/rlhf-alignment/readme)
- The composition: `chatkit/stages/align.py` in
  [small-chat-model](/python/python-production-examples/small-chat-model/readme)
- Rafailov et al., *Direct Preference Optimization: Your Language Model is Secretly a Reward Model*:
  <https://arxiv.org/abs/2305.18290>
- Deeper on the reusable mechanism:
  [RLHF and Alignment (workflow)](/ai-ml/practitioner-workflows/training-and-adaptation/preference-alignment/rlhf-and-alignment)
