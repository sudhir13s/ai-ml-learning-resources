---
title: "Design the Conversation Template"
id: lr-scm-design-the-conversation-template
minutes: 18
core_idea: "The template is the model's social contract, and the prompt at inference must match the training render character for character — a mismatch of one newline is the most common reason a fine-tuned model appears to have ignored its training."
builds_on: [lr-scm-from-base-model-to-assistant]
leads_to: [lr-scm-mask-the-loss-across-turns]
related: [lr-slm-train-a-tokenizer]
section: "ai-ml-learning-resources"
workflow: "build-a-small-chat-model"
chapter: 1
status: complete
template: workflow
category: model-adaptation
---

# Design the Conversation Template

A conversation has to become one string, because that is all a language model reads. The template is
the function that does it, and it is the model's **social contract**: it is how the model knows who
is speaking, when to start, and when to stop.

```text
<|user|>
What is a soliloquy?
<|assistant|>
A speech the player makes alone, that we may hear the thought.<|end|>
<|user|>
And how does it differ from an aside?
<|assistant|>
The aside is short and stolen while others stand by; the soliloquy is long.<|end|>
```

Three markers, and each one does a job:

- **`<|user|>`** opens a turn the model conditions on and is never graded for.
- **`<|assistant|>`** opens a turn the model *is* graded for. At inference this is the last thing in
  the prompt — the cue that says "your turn".
- **`<|end|>`** closes an assistant turn. It is the stop signal, and the next chapter shows why it
  must sit *inside* the graded span.

---

## Why the markers are plain text and not new token ids

Production chat models usually reserve token ids for these markers. This build does not, and the
reason is a constraint worth understanding because it recurs whenever you adapt a model you did not
train.

**Adding a token id resizes the embedding table.** The base model's embedding matrix has exactly
`vocab_size` rows; a new id needs a new row, and a new row means a modified checkpoint — which is
the artifact this build is required to start from unchanged.

**A byte-level tokenizer makes the alternative free.** Every byte sequence is already representable,
so `<|user|>\n` encodes exactly and decodes exactly with no vocabulary change at all:

```python
USER_MARKER = "<|user|>\n"
ASSISTANT_MARKER = "<|assistant|>\n"
END_MARKER = "<|end|>\n"
```

**The trade you accept.** A reserved id is one token; `<|assistant|>\n` is several. That costs a few
tokens of context per turn and removes the possibility of the model emitting a *partial* marker,
which is a real failure mode — a reserved id cannot be half-produced, and a text marker can.

The chat loop in chapter eight handles that by matching the decoded text rather than a single id.

---

## Rendering, twice, from one definition

There are two renders and they must agree exactly.

```python
def render_conversation(conversation: Conversation) -> str:
    """The full dialogue as the model sees it during training."""
    return "".join(_render_turn(turn) for turn in conversation.turns)


def render_prompt(turns: tuple[Turn, ...]) -> str:
    """The conditioning text for generation: the dialogue so far, plus the assistant opener."""
    return "".join(_render_turn(turn) for turn in turns) + ASSISTANT_MARKER


def _render_turn(turn: Turn) -> str:
    """One turn, with the marker that opens it and (for the assistant) the marker that ends it."""
    if turn.role is Role.USER:
        return f"{USER_MARKER}{turn.content}\n"
    return f"{ASSISTANT_MARKER}{turn.content}{END_MARKER}"
```

**Training** renders the complete dialogue. **Inference** renders the dialogue so far and then the
assistant opener, stopping there — that trailing marker is the cue.

Both call `_render_turn`. That is not tidiness; it is the only defence against the failure below.

---

## The failure this chapter exists to prevent

> **A prompt that differs from the training format by one character is a format the model has never
> seen.**

An extra newline. A renamed marker. A space after the colon. The model was trained to respond to one
exact string and is being shown a different one, so it falls back on what it learned in pretraining
— which is continuation.

The symptom is the worst kind: **the model appears to have ignored its fine-tuning entirely.** No
error, no warning, and the natural next move is to train longer, which cannot help.

The project asserts the invariant directly:

```python
def test_the_prompt_prefix_matches_the_training_render_exactly() -> None:
    """The single most common cause of a fine-tune that appears to have been ignored."""
    conversation = _single()
    training = render_conversation(conversation)
    inference = render_prompt(conversation.turns[:1])

    assert training.startswith(inference)
```

The inference prompt must be a **prefix** of the training render. If that holds, the two cannot drift
apart.

---

## Structural rules, enforced at construction

```python
def __post_init__(self) -> None:
    if not self.turns:
        raise ValueError("a conversation needs at least one turn")
    if self.turns[0].role is not Role.USER:
        raise ValueError("a conversation must open with a user turn")
    if self.turns[-1].role is not Role.ASSISTANT:
        raise ValueError("a conversation must close with an assistant turn")
```

A conversation opens with a user turn and closes with an assistant turn. Both are checked when the
object is built rather than when the batch fails.

- **A leading assistant turn** would train the model to speak unprompted.
- **A trailing user turn** contributes a row with nothing graded — which is undefined loss, and it
  poisons the batch it lands in rather than merely wasting a slot.

---

## Comparing with the templates you will meet

| Template | Shape | Where you see it |
|---|---|---|
| **ChatML** | `<\|im_start\|>role\ncontent<\|im_end\|>` | OpenAI-lineage models, and the shape this one follows |
| **Mistral instruct** | `<s>[INST] instruction [/INST] answer</s>` | Mistral and its derivatives |
| **Llama 3** | header-token blocks with `<\|eot_id\|>` | Llama 3 family |
| **This build** | `<\|user\|>` / `<\|assistant\|>` / `<\|end\|>` | plain text, no vocabulary change |

They differ in surface and agree completely on structure: **mark the role, mark the end, condition on
everything before the answer.** A model trained on one and prompted with another produces the failure
above, which is why every released chat model ships its template alongside its weights.

## Pitfalls

- **Two renderers, one for training and one for inference.** They drift, and the drift is silent.
- **Adding special token ids to an existing model's vocabulary.** It resizes the embedding and
  invalidates the checkpoint.
- **Omitting the assistant opener from the inference prompt.** The model has no cue that it is its
  turn.
- **Allowing a conversation to end on a user turn.** Nothing is graded in that row.
- **Assuming a downloaded model's template.** Read the one it shipped with; guessing produces
  exactly this failure.

## Key takeaways

- **The template is the contract**: role markers, an end marker, and a cue that it is the model's
  turn.
- **Plain-text markers avoid a vocabulary change**, which is what keeps the base checkpoint valid —
  possible because the tokenizer is byte-level.
- **The inference prompt must be a prefix of the training render.** Assert it.
- **One `_render_turn`, two renders.** Anything else drifts.
- **Structural rules belong at construction time**, not at the batch that fails.

## References

- The implementation: `chatkit/template.py` in
  [small-chat-model](/python/python-production-examples/small-chat-model/readme)
- Hugging Face, *Chat Templates* — how released models publish theirs, and why:
  <https://huggingface.co/docs/transformers/chat_templating>
