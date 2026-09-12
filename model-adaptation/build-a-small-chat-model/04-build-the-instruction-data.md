---
title: "Build the Instruction Data"
id: lr-scm-build-the-instruction-data
minutes: 18
core_idea: "Instruction data has to sit inside the base model's distribution, or fine-tuning spends its budget on domain transfer instead of behaviour — which is the failure that presents as we fine-tuned and it got worse."
builds_on: [lr-scm-mask-the-loss-across-turns]
leads_to: [lr-scm-run-supervised-fine-tuning]
related: [lr-fine-tuning-prepare-instruction-data]
section: "ai-ml-learning-resources"
workflow: "build-a-small-chat-model"
chapter: 3
status: complete
template: workflow
category: model-adaptation
---

# Build the Instruction Data

The base model was pretrained on Elizabethan dramatic verse. Now it needs to learn a behaviour, and
there are two ways to write the data that teaches it.

**The wrong one** is modern technical prose. It is what everyone reaches for, and it asks the model
to learn a new *language* and a new *behaviour* simultaneously, from twenty-four examples. It learns
neither, the perplexity collapses, and the conclusion drawn is usually that fine-tuning does not
work at this scale.

**The right one** is question and answer in the register the model already speaks:

```python
_exchange(
    "What is a soliloquy?",
    "A speech the player makes alone, that we may hear the thought and not the "
    "answer of another.",
),
```

The vocabulary is already in the model's distribution. **The only thing left to learn is the
format**, which is the behaviour this build is trying to teach — and a twelve-million-parameter model
has enough capacity for that and nothing more.

---

## The rule, stated generally

> **Instruction data must sit inside the base model's distribution.**
>
> Everything it asks the model to learn that is *not* the target behaviour is budget spent on domain
> transfer.

This scales all the way up. Fine-tuning a general English model on legal drafting works because legal
English is inside its distribution. Fine-tuning it on a language it never saw does not, and the
symptom is identical to the one here: fluency drops, the behaviour does not appear, and the loss
curve looks fine throughout.

**The check to run before writing a single example:** generate from the base model and read it. If
your intended instruction data does not look like something the base model could plausibly have
produced, you are asking for domain transfer.

---

## What the set contains

Twenty-four conversations, and the mix is deliberate:

| | Count | Purpose |
|---|---|---|
| Single exchanges | 16 | the basic shape: question in, answer out, stop |
| Multi-turn dialogues | 8 | that the previous answer is context, not something to repeat |
| Held-out prompts | 6 | evaluation — none appears in training |

The multi-turn ones are what make the previous chapter's masking matter. A two-exchange dialogue
contributes two graded spans; a three-exchange one contributes three.

```python
_dialogue(
    (
        (
            "What is blank verse?",
            "Five beats to the line, unrhymed, and near to true speech.",
        ),
        (
            "Who speaks it?",
            "The noble and the passionate; the plain and the comic keep to prose.",
        ),
        (
            "And when a king speaks prose?",
            "Then mark him well, for he is feigning, or he is falling.",
        ),
    )
),
```

Read the third turn. *"And when a king speaks prose?"* only makes sense given the second answer —
that is the property multi-turn data exists to teach, and it cannot be taught by a set of independent
question-answer pairs.

---

## Answers demonstrate the behaviour, including its length

Every answer here is one or two sentences. That is not a style preference; **the answers are the
specification**, and the model will reproduce whatever they demonstrate:

- **Length.** Two-sentence answers produce a model that answers in two sentences.
- **Register.** Period vocabulary produces period vocabulary.
- **Stopping.** Every answer ends and is followed by the end marker, so the model learns that
  answers end.
- **Refusing to pad.** No answer says "great question" or restates the question. If they did, so
  would the model.

Twenty-four examples is very few. It is enough here only because the behaviour is narrow and the
register is already known. A real instruction set is thousands of examples covering many task types,
and the Workflow Library's
[Prepare Instruction Data](/ai-ml/ai-ml-learning-resources/model-adaptation/fine-tuning/prepare-instruction-data)
chapter is where that is treated properly.

---

## Preference pairs: the same prompts, one better answer and one worse

Alignment needs a different shape — a prompt with two candidate answers and a stated preference.

```python
PreferencePair(
    prompt_turns=(Turn(Role.USER, "What is a soliloquy?"),),
    chosen="A speech the player makes alone, that we may hear the thought.",
    rejected=(
        "A soliloquy is a monologue delivered by a character who is alone on stage, "
        "typically used to reveal inner thoughts to the audience in a dramatic work."
    ),
),
```

**Both answers are correct.** The rejected one is a perfectly good dictionary definition. It is
rejected because it is out of register — modern encyclopedic English where the model should be
answering in the voice its training establishes.

That is what preference data is for: **choosing between acceptable answers**, where supervised
fine-tuning can only say "produce this one". The eight pairs here break the format in the three ways
this build can actually measure:

| Failure demonstrated | Example |
|---|---|
| **Out of register** | the dictionary definition above |
| **Rambling past the end** | an answer that starts well and keeps going for four more clauses |
| **Answering a different question** | *"What is a tragedy?"* answered with the definition of comedy |

Each is observable in a generation, which is what makes the pairs honest. A preference for something
you cannot detect afterwards is a preference you cannot verify you taught.

---

## What a small preference set can and cannot show

The run reports:

```text
aligned: 40 steps; preference accuracy 1.00; reward margin 8.6404
```

**Preference accuracy of 1.00 on eight pairs is separable data, not an aligned model.** The chosen
and rejected answers differ so obviously — different length, different vocabulary, different subject
— that the mechanism separates them immediately.

That is the right expectation to set. What the number shows is that **the machinery runs and the
margin moves in the right direction**. Real alignment needs thousands of pairs where the difference
is a matter of judgement, and its evaluation is a win rate against a held-out set rather than
training-set accuracy.

---

## Writing your own

Whatever domain you are in, the sequence is the same:

1. **Generate from the base model and read it.** That tells you its register.
2. **Write answers in that register**, demonstrating the exact behaviour you want — length, format,
   stopping.
3. **Hold some prompts out.** Six is not many; zero is fatal.
4. **Write preference pairs where both answers are acceptable** and the difference is something you
   can observe in a generation.
5. **Check the graded fraction** after templating. It is the previous chapter's cheapest check and
   it catches a data-shape problem before training starts.

## Pitfalls

- **Instruction data outside the base model's distribution.** Fine-tuning becomes domain transfer and
  fails at both jobs.
- **Answers that demonstrate a behaviour you do not want** — padding, restating the question, running
  long. The model copies them.
- **No held-out prompts.** There is then nothing to measure.
- **Preference pairs where the rejected answer is simply wrong.** That is supervised data with extra
  steps; preference data is for choosing between acceptable answers.
- **Reading training-set preference accuracy as alignment.** On separable data it is 1.00 and means
  very little.

## Key takeaways

- **Instruction data has to sit inside the base model's distribution** — otherwise the budget goes
  to domain transfer.
- **The answers are the specification.** Length, register, and stopping are all taught by example.
- **Multi-turn examples teach that context is context**, and they only pay off if the mask grades
  every turn.
- **Preference pairs choose between acceptable answers**, and the difference has to be observable.
- **Generate from the base model first.** It tells you what register to write in.

## References

- The data: `chatkit/data.py` in
  [small-chat-model](/python/python-production-examples/small-chat-model/readme)
- Deeper on the reusable mechanism:
  [Prepare Instruction Data (workflow)](/ai-ml/ai-ml-learning-resources/model-adaptation/fine-tuning/prepare-instruction-data)
- Zhou et al., *LIMA: Less Is More for Alignment* — the argument that a small, carefully written
  instruction set can be enough: <https://arxiv.org/abs/2305.11206>
