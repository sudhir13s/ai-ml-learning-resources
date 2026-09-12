---
title: "Quantize and Serve the Chat Loop"
id: lr-scm-quantize-and-serve-the-chat-loop
minutes: 20
core_idea: "The chat loop closes the circle between training and serving: it renders history in exactly the trained format, stops on the marker the loss graded, and drops whole turns rather than half of one."
builds_on: [lr-scm-evaluate-behaviour-and-regression]
related: [pw-model-compression, pw-model-serving]
section: "ai-ml-learning-resources"
workflow: "build-a-small-chat-model"
chapter: 7
status: complete
template: workflow
category: model-adaptation
---

# Quantize and Serve the Chat Loop

Two stages left, and they answer different questions. Quantization asks *how small can this get*.
The chat loop asks *does the format the model was taught actually work at inference*.

---

## Quantization: `mckit`'s job, and one honest omission

```python
def quantize_for_serving(model: CausalLMAdapter) -> tuple[CausalLMAdapter, CompressionReport]:
    """Quantize the linear layers to int8 and report the size on both sides."""
    before = disk_bytes(model)
    quantized = dynamic_quantize(model, dtype=QuantDtype.INT8)
    return quantized, CompressionReport(
        engine=select_quant_engine(),
        parameters=param_count(model),
        bytes_before=before,
        bytes_after=disk_bytes(quantized),
    )
```

[model-compression](/python/python-production-examples/model-compression/readme) owns quantization
here, including engine selection and the guarded four-bit path. This module calls it and measures the
result.

**Dynamic int8** stores weights as eight-bit integers and computes activations in floating point.
Three properties make it the right choice for a processor:

- **No calibration data.** Static quantization needs a representative sample to set activation
  ranges; dynamic computes them per batch.
- **No call site changes.** The quantized model has the same interface.
- **It targets the linear layers**, which is where a transformer keeps almost all of its parameters.

```text
quantized (qnnpack): 48,796,775 -> 18,663,339 bytes (61.8% smaller)
```

Not the naive four times, because embeddings and normalisation gains stay in floating point and only
`nn.Linear` is converted. **61.8% is the real number for this architecture**, and quoting the
theoretical one would be quoting a different model.

### What is not reused, and why that is worth saying

`model-compression` also ships `load_predictor`, and this build does not use it. That loader rebuilds
a **fixed classifier architecture** from a state dictionary — right for the model it was written for,
wrong for a language model whose architecture comes from a checkpoint.

Composition means using what fits and **saying plainly what does not**. A silent omission reads as an
oversight; a stated one is a decision.

---

## The chat loop: three rules, each closing a loop with training

### The prompt must match the training format exactly

```python
prompt = render_prompt(turns)
prompt_ids = tokenizer.encode(prompt)[-model.block_size + max_new_tokens :]
```

`render_prompt` is the same function chapter one defined and chapter two masked against. The model
sees at inference exactly the string shape it saw in training, ending in the assistant opener.

This is the failure that produces "the fine-tune did nothing", and the defence is structural: **one
renderer, used by both paths.**

### Stopping is a decoded-text match, one token at a time

```python
for _ in range(max_new_tokens):
    idx = generate(model.model, idx, max_new_tokens=1, temperature=temperature,
                   top_k=top_k, generator=generator)
    decoded = tokenizer.decode(idx[0].tolist()[len(prompt_ids):])
    marker = decoded.find(stop_text)
    if marker != -1:
        return Reply(text=decoded[:marker].strip(), stopped_cleanly=True,
                     tokens_generated=idx.shape[1] - len(prompt_ids))
```

The end marker is **several tokens** in a byte-level vocabulary, so there is no single stop id to hand
the sampler. Generating one token at a time and checking the decoded tail is what makes an early stop
possible at all.

Generating to the budget and trimming afterwards would produce the same *text* — and would make
`tokens_generated` the same number for every model, which is one of the two things the previous
chapter measures. **The measurement is why the loop is shaped this way.**

At sixty-four tokens on a twelve-million-parameter model this costs nothing: the model has no
key-value cache, so it recomputes the context every token regardless.

### History is re-rendered every turn, and trimmed by whole turns

```python
def _trim_to_window(self) -> None:
    """Drop whole turns from the front until the rendered prompt fits the context window."""
    budget = self._model.block_size - self._max_new_tokens
    while len(self._turns) > 1:
        rendered = render_prompt(tuple(self._turns))
        if len(self._tokenizer.encode(rendered)) <= budget:
            return
        del self._turns[:2]
```

**The model has no memory between calls.** The conversation exists only as text in the prompt, so it
is re-rendered from scratch every turn.

That text grows, and eventually exceeds the window. The loop drops a **user-and-assistant pair** —
never half of one. A dangling assistant turn with no question in front of it is a format the model was
never trained on, and it produces exactly the confusion the format was designed to prevent.

---

## Running it

```bash
PYTHONPATH=$COMPOSED python -m chatkit.cli run
```

```text
quantized (qnnpack): 48,796,775 -> 18,663,339 bytes (61.8% smaller)

user: What is a soliloquy?
assistant: A
A play, made good to the city, and hear away.

user: And how does it differ from an aside?
assistant: A play, and beg, andBUC
To have some hand in, may tell a king his fathers.
```

Or type your own turns:

```bash
PYTHONPATH=$COMPOSED python -m chatkit.cli interactive
```

---

## Reading that transcript honestly

**What worked.** The model answered rather than continuing the question. It stopped on its own — the
`<|end|>` marker it was graded on. It stayed in register: *"To have some hand in, may tell a king his
fathers"* is Elizabethan-flavoured English. The second turn was conditioned on the first without
repeating it. And all of that came out of a model that is 61.8% smaller than the one that was
trained.

**What did not.** The answers do not mean anything. *"A play, made good to the city, and hear away"*
is grammatical, in register, and empty. `BUC` is a fragment of a speaker name the base model
memorised.

**Why that is the expected outcome, not a failure of the build.** Twelve million parameters, twenty
four conversations, a million characters of pretraining. The model learned a **format**, and a format
is what this scale can learn. Meaning needs orders of magnitude more of everything.

That distinction is the one to carry out of this course. **The pipeline is correct and the model is
small**, and those are separate facts. Everything here — the template, the mask, the composition, the
regression check, the loop — is the same at a thousand times the scale. What changes is the number of
parameters and the amount of text, and neither is a design decision.

---

## What a real serving path adds

- **A key-value cache**, so generation is linear rather than quadratic in the reply length. That is
  [KV Cache](/ai-ml/ai-buzzwords/inference-serving-and-efficiency/kv-cache), and it belongs to a
  serving project.
- **Batching**, so one model serves many conversations at once.
- **A token budget and a timeout** per request.
- **Streaming**, so the first token reaches the reader immediately.
- **Input and output filtering**, which this build has none of.

[inference-orchestrator](/python/python-production-examples/inference-orchestrator/readme) and
[Model Serving](/ai-ml/practitioner-workflows/inference-and-serving/model-serving)
are where those live.

## Pitfalls

- **A different renderer at inference.** The format breaks and the model appears untrained.
- **Trimming the history mid-turn.** A dangling assistant turn is a format never trained on.
- **Assuming a single stop id.** A text marker is several tokens in a byte-level vocabulary.
- **Generating to the budget and trimming after.** The text is right and the length measurement is
  destroyed.
- **Quoting the theoretical compression ratio.** Only the linear layers are converted; measure the
  real one.
- **Reading a small model's fluency as understanding.** Format and meaning are different learnings.

## Key takeaways

- **Dynamic int8 needs no calibration and changes no call site** — 61.8% smaller here, measured
  rather than assumed.
- **The chat loop closes three loops with training**: the same renderer, the marker the loss graded,
  and turn-aligned trimming.
- **Stop on decoded text, token by token**, because the marker is multi-token and the length is a
  measurement.
- **The model has no memory** — the conversation is text in the prompt, re-rendered every turn.
- **A correct pipeline and a small model are separate facts.** Everything here holds at scale; only
  the numbers change.

## References

- The implementation: `chatkit/chat.py` and `chatkit/stages/compress.py` in
  [small-chat-model](/python/python-production-examples/small-chat-model/readme)
- The quantizer it calls:
  [model-compression](/python/python-production-examples/model-compression/readme)
- Deeper on the reusable mechanisms:
  [Model Compression (workflow)](/ai-ml/practitioner-workflows/inference-and-serving/model-compression/model-compression)
  and
  [Model Serving (workflow)](/ai-ml/practitioner-workflows/inference-and-serving/model-serving)
