---
title: "Mask the Loss Across Turns"
id: lr-scm-mask-the-loss-across-turns
minutes: 22
core_idea: "Grade every assistant turn and mask everything else — and build the spans separately rather than hunting for markers in the token stream, because a byte-level vocabulary can merge a marker's last byte into the text that follows it."
builds_on: [lr-scm-design-the-conversation-template]
leads_to: [lr-scm-build-the-instruction-data]
related: [lr-fine-tuning-prepare-instruction-data]
section: "ai-ml-learning-resources"
workflow: "build-a-small-chat-model"
chapter: 2
status: complete
template: workflow
category: model-adaptation
---

# Mask the Loss Across Turns

This is the chapter that decides whether fine-tuning teaches the right thing. Everything else in the
build is machinery around one question: **which positions does the loss grade?**

```text
<|user|>\nWhat is a soliloquy?\n            ← masked   (the question)
<|assistant|>\n                             ← masked   (the cue)
A speech the player makes alone.<|end|>\n   ← GRADED   (the answer, and the stop)
<|user|>\nAnd how does it differ?\n          ← masked
<|assistant|>\n                             ← masked
The aside is short and stolen.<|end|>\n     ← GRADED
```

Two rules, and each prevents a specific, well-known failure:

- **Mask the user turns**, or the model learns to write the human's half of the conversation too.
  Ask it a question and it answers, then invents your follow-up, then answers that.
- **Grade the end marker**, or the model never learns to stop and generates until the token budget
  runs out.

---

## Multi-turn is where this build differs from the toolkit

`ftkit` renders an instruction example into a prompt and a response, and **the response is the final
assistant turn**. Everything before it — including earlier assistant answers — is prompt, and prompt
is masked.

For single-turn instruction data that is exactly right. For a dialogue it throws away half the
supervision:

| | `ftkit` | here |
|---|---|---|
| Single-turn example | 1 graded span | 1 graded span |
| Four-turn dialogue | **1** graded span | **2** graded spans |
| Six-turn dialogue | **1** | **3** |

Across this build's twenty-four conversations, grading every assistant turn puts **54.6% of tokens**
in the loss. Grading only the last would put far fewer, and the eight multi-turn dialogues would each
contribute one answer instead of two or three.

---

## Build the spans separately — do not search for markers

Here is the implementation detail that separates a correct multi-turn masker from one that looks
correct:

```python
for turn in conversation.turns:
    if turn.role is Role.USER:
        masked = encode(f"{USER_MARKER}{turn.content}\n")
        input_ids.extend(masked)
        labels.extend([IGNORE_INDEX] * len(masked))
        continue
    opener = encode(ASSISTANT_MARKER)
    graded = encode(f"{turn.content}{END_MARKER}")
    input_ids.extend(opener)
    labels.extend([IGNORE_INDEX] * len(opener))
    input_ids.extend(graded)
    labels.extend(graded)
```

Each span is **encoded on its own** and its labels are decided as it is appended.

The obvious alternative — encode the whole dialogue, then find the marker positions in the token
stream and mask between them — is wrong in a way that is very hard to see:

> **A byte-level vocabulary can merge a marker's last byte with the first byte of the text that
> follows it.** The boundary the mask needs may not exist as a token boundary at all.

When that happens, one token straddles the boundary. Mask it and you lose the first token of the
answer; grade it and you train the model to emit part of the marker. Either way the run completes,
the loss falls, and the model is subtly wrong.

Encoding span by span makes the boundary exact **by construction**, so there is nothing to get right
at runtime.

---

## What the labels actually are

`IGNORE_INDEX` is `-100`, the value PyTorch's cross-entropy skips:

```python
loss = F.cross_entropy(shifted_logits, shifted_labels, ignore_index=IGNORE_INDEX)
```

On graded positions the label **is** the input token — the model is being taught to produce exactly
what is there. The project asserts that, because a masker that produces the right *shape* and the
wrong *values* is otherwise invisible:

```python
def test_every_graded_label_equals_its_input_token(tokenizer: Tokenizer) -> None:
    record = build_masked_record(_multi(), tokenizer, max_seq_len=256)

    assert all(
        label == token
        for token, label in zip(record.input_ids, record.labels, strict=True)
        if label != IGNORE_INDEX
    )
```

---

## Truncation cuts from the left

```python
def _truncate_keeping_the_tail(input_ids, labels, max_seq_len):
    """Cut from the left when a conversation overruns the window."""
    if len(input_ids) <= max_seq_len:
        return input_ids, labels
    return input_ids[-max_seq_len:], labels[-max_seq_len:]
```

The most recent turns are what the model needs to answer, and the **last assistant span is the graded
one**. Cutting from the right removes the supervision and leaves a row with nothing to learn from —
undefined loss, and it poisons the batch it lands in rather than merely shortening it.

The stage that builds records drops any row that survives truncation with nothing graded:

```python
return [record for record in records if record.graded_tokens > 0]
```

Cheaper than discovering it as a run that will not converge.

---

## The one number that tells you it worked

```python
@property
def graded_fraction(self) -> float:
    """Share of positions the loss actually grades — the number a masking bug moves."""
    if not self.input_ids:
        return 0.0
    return self.graded_tokens / len(self.input_ids)
```

```bash
PYTHONPATH=$COMPOSED python -m chatkit.cli template
```

```text
templated: 24 records (8 multi-turn), 54.6% of tokens graded
```

**Read that number every time.** It is the single cheapest check on the whole stage:

| Graded fraction | What it usually means |
|---|---|
| ~0% | the mask is inverted, or nothing matched — the run will not learn |
| 30–70% | healthy for conversational data |
| ~100% | nothing is masked — the model will learn to write both halves |

Fifty-four per cent is right for short questions and comparable-length answers. Long questions with
short answers land lower; the number is corpus-shaped, and its *stability* across a data change is
what to watch.

---

## Verifying it yourself

```python
from chatkit.template import Conversation, Role, Turn, build_masked_record
from chatkit.adapter import IGNORE_INDEX
from slmkit.tokenizer.bpe import BPETokenizer

tok = BPETokenizer.load("../small-language-model/runs/scale/tokenizer.json")
conversation = Conversation(turns=(
    Turn(Role.USER, "What is an act?"),
    Turn(Role.ASSISTANT, "A division of a play."),
))
record = build_masked_record(conversation, tok, max_seq_len=256)

print(f"{record.graded_fraction:.1%} graded")
print(tok.decode([i for i, lab in zip(record.input_ids, record.labels)
                  if lab != IGNORE_INDEX]))
```

The second print is the check that matters: **decode only the graded positions and read them.** They
should be the assistant's answer and its end marker, and nothing else. If the question appears there,
the mask is wrong, and you have found it in a second rather than after a training run.

## Pitfalls

- **Grading the user turns.** The model learns to write both halves of the conversation.
- **Masking the end marker.** The model never learns to stop.
- **Searching for markers in the token stream.** A merged boundary token silently corrupts the mask.
- **Truncating from the right.** The graded span is at the end.
- **Keeping a fully masked row.** Its loss is undefined and it poisons its batch.
- **Not looking at the graded fraction.** It is the cheapest possible check and it catches the worst
  bug.

## Key takeaways

- **Grade every assistant turn, mask everything else.** A four-turn dialogue has two graded spans,
  not one.
- **The end marker is inside the graded span**, or the model never stops.
- **Encode span by span**, so the mask boundary exists by construction.
- **Truncate from the left**, and drop rows with nothing left to grade.
- **Read the graded fraction every run.** Near 0% or near 100% are both broken.
- **Decode the graded positions and read them.** One second, catches the worst class of bug.

## References

- The implementation: `chatkit/template.py` in
  [small-chat-model](/python/python-production-examples/small-chat-model/readme)
- The single-turn version this extends: `ftkit/formatting/dataset.py` in
  [fine-tuning-toolkit](/python/python-production-examples/fine-tuning-toolkit/readme)
- Deeper on the reusable mechanism:
  [Prepare Instruction Data (workflow)](/ai-ml/ai-ml-learning-resources/model-adaptation/fine-tuning/prepare-instruction-data)
