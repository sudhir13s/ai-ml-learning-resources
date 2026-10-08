---
id: "09-llms/decoding-and-sampling/decoding-in-production"
topic: "Decoding: In Production"
parent: "09-llms"
chapter_of: "09-llms/decoding-and-sampling"
chapter: 5
level: intermediate
built_from: ["09-llms/decoding-and-sampling"]
interview_frequency: very-high
template: concept-chapter
updated: 2026-10-08
tier: flagship
est_minutes: 14
core_idea: "In production the decoder is a product decision: the request parameters choose behaviour per task, the serving stack makes any choice fast without changing it, and most bad output traces back to one misset knob."
title: "Decoding in Production"
minutes: 14
category: inference-and-serving
---

# Decoding in production: defaults, code and failure modes

This page carries the course into a serving stack: the defaults that ship, the same knobs in code, and how to diagnose bad output.

## The playbook: which decoder for which task

The task's shape dictates the strategy. One row per task you will actually ship:

| Task | Goal | Recommended decoding | Why |
|---|---|---|---|
| **Factual QA, extraction** | one correct answer | greedy, or $T\approx0.1$ with top-p $\approx0.9$ | the most probable answer is the one you want |
| **Code generation** | correct and parseable | $T\approx0.2$, top-p $\approx0.95$, plus grammar or JSON constraints | a small valid space; determinism and structure matter |
| **Machine translation** | faithful and complete | beam search, $b$ = 4–8, with length normalization | closed-ended; the likeliest complete output wins BLEU |
| **Summarization** | faithful and fluent | beam $b$ = 4, length normalization, `no_repeat_ngram_size=3` | closed-ended; block repeated phrases |
| **Chat, assistants, retrieval-augmented generation (RAG) answers** | helpful, varied, grounded | nucleus top-p $\approx0.9$ with $T\approx0.7$, repetition penalty $\approx1.1$ | cut the tail tightly, keep a little variety |
| **Stories, brainstorming, dialogue** | creative and human-like | nucleus top-p $\approx0.92$–$0.95$ with $T\approx0.9$–$1.0$ | a wider nucleus for range; it still stays coherent |
| **Evals and unit tests** | deterministic | greedy (`do_sample=False`, $T = 0$) | same input, same output, no seed |
| **Structured output for tools** | valid JSON or enum | constrained decoding with a low temperature | the grammar guarantees the output parses |
| **Open-ended output that loops** | stop the repeat | keep nucleus sampling, add a repetition penalty of 1.1–1.2 | treats the symptom once the decoder itself is right |

The two-line summary that fits in your head:

- **Closed-ended, faithfulness-first** tasks use **search** (greedy or beam); **open-ended, creativity-first** tasks use **sampling** (temperature plus top-p).
- Turn temperature **down** toward the factual end and **up** toward the creative end, and reach for [constraints](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/constrained-and-guided-decoding) whenever structure must be guaranteed.

> [!WARNING]
> "Lower temperature is always safer" is wrong for open-ended tasks.
> - Push $T$ too low there and you slide straight back into greedy's repetition.
> - There is no globally safe setting; the safe setting is the one matched to the task's place on the quality–diversity curve.

---

## In production

A few realities of how this is deployed:

- **Defaults that ship.** Most chat APIs default to **nucleus sampling around $p=0.9$–$1.0$ with $T=0.7$–$1.0$**.
  - OpenAI, Anthropic, and open-source serving stacks (vLLM, Text Generation Inference (TGI)) all expose `temperature` + `top_p` as request parameters.
  - Often they also expose `top_k`, `min_p`, and frequency/presence penalties.
- **Decoders compose with serving optimizations.** [Speculative decoding](/ai-ml/ai-ml-learning-resources/inference-and-serving/speculative-decoding/speculative-decoding) accelerates *whatever* decoder you chose.
  - Its rejection-sampling correction makes the sped-up output **distributionally identical** to plain sampling from your chosen strategy.
  - The two are orthogonal: this page picks the strategy, the serving stack makes it fast.
- **Beam search is fading for chat, alive for MT.** As models got better at open-ended generation, beam search's blandness made it a poor fit for assistants.
  - It remains standard in **machine-translation and speech** systems where a single best sequence is the goal.
- **Reproducibility in evals.** Benchmarks usually decode **greedily** (or at $T=0$) precisely so results are deterministic and comparable; sampling-based metrics report a seed.

**The same knobs in code.** In Hugging Face `transformers` they are arguments to `.generate(...)`, with the key-value cache on by default. This snippet downloads a 7B model and wants a GPU, so it is shown for its shape and was not run for this page:

```step
///FILE generate_with_transformers.py
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.3"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(MODEL_ID, device_map="auto")
messages = [{"role": "user", "content": "Explain nucleus sampling in one sentence."}]
inputs = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True).to(model.device)

output_ids = model.generate(
    inputs,
    max_new_tokens=128,
    do_sample=True,          # False -> greedy
    temperature=0.7,         # reshape the distribution
    top_k=50,                # hard cap on candidates
    top_p=0.9,               # adaptive nucleus inside that cap
    repetition_penalty=1.1,  # loop breaker, inside the safe band
)
print(tokenizer.decode(output_ids[0], skip_special_tokens=True))
```

When one `.generate()` loop is not enough, the same knobs become vLLM `SamplingParams`, and the engine adds PagedAttention and continuous batching ([Inference Optimization & Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization)). Also shown, not run — it needs a GPU:

```step
///FILE serve_with_vllm.py
from vllm import LLM, SamplingParams

llm = LLM(model="mistralai/Mistral-7B-Instruct-v0.3")
params = SamplingParams(temperature=0.7, top_p=0.9, repetition_penalty=1.1, max_tokens=128)
for request_output in llm.generate(["Summarize: ...", "Translate: ...", "Q: ..."], params):
    print(request_output.outputs[0].text)
```

---

## Mapping the knobs to real APIs

The same concepts carry slightly different names across stacks:

- **Hugging Face `transformers`** (`model.generate`):
  - `do_sample` (False is greedy or beam, True is sampling), `num_beams`, `temperature`, `top_k`, `top_p`.
  - `repetition_penalty`, `no_repeat_ngram_size`, `length_penalty` (the $\alpha$ of beam's length normalization), `penalty_alpha` with `top_k` (contrastive search), `min_new_tokens`.
- **OpenAI and Anthropic chat APIs**:
  - `temperature`, `top_p`, plus `frequency_penalty` and `presence_penalty` where offered; `logit_bias` for token-level steering; a structured-output or JSON mode for constrained decoding.
  - No beam search is exposed — these endpoints sample. Conventionally you tune **either** `temperature` **or** `top_p`, not both.
- **vLLM and Text Generation Inference** (serving):
  - The full sampling set (`temperature`, `top_p`, `top_k`, `min_p`, the penalties) as per-request `SamplingParams`, plus guided-decoding back ends for grammars, JSON and regular expressions.
  - Speculative decoding is configured on the engine, invisible to the request.

The vocabulary differs; the operation is identical everywhere: reshape the logits, optionally truncate the tail, then sample or take the argmax.

---

## How decoding interacts with alignment and evaluation

Two connections tie the decoder into the wider large-language-model (LLM) picture.

**Alignment changes the distribution the decoder samples from.**

- A base model's next-token distribution often has a heavy, ragged tail, so it leans hard on truncation to stay coherent.
- [Instruction tuning and reinforcement learning from human feedback (RLHF)](/ai-ml/ai-ml-learning-resources/model-adaptation/preference-and-alignment-training/preference-and-alignment-training) **sharpen** that distribution toward helpful continuations, so aligned chat models are far more forgiving of decoding settings.
- Over-optimized RLHF can make a model **too** peaked: even nucleus sampling then gives near-identical, mode-collapsed answers.
- When a chat model feels robotic and same-y, the cause may be the **training**, not the decoder — no temperature recovers diversity the model no longer has.

**The decoder changes your evaluation numbers.** It is part of the system under test, so it must match the [metric](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/nlp-evaluation-metrics/nlp-evaluation-metrics):

- **Reference-overlap metrics** (BLEU for translation, ROUGE for summarization) reward matching one reference, so they favour **beam search**; BLEU from a high-temperature sample understates a system.
- **Diversity and human-likeness metrics** (distinct-n, MAUVE, the perplexity of human text) reward variety, so they favour **nucleus sampling**; reported from greedy output, a good model looks degenerate.
- **Reproducibility**: a benchmark meant to be deterministic must fix the decoder — greedy, or a fixed seed — or the same model scores differently run to run.

> [!WARNING]
> Comparing two models under *different* decoders — one with beam, one with sampling — and crediting the gap to the models is a classic evaluation mistake.
> - The decoder is a confound: hold it fixed, or report both.

---

## Recap and rapid-fire

**If you remember nothing else:** the model emits a *distribution*; the **decoder** turns it into text, and that choice — not the weights — controls coherence, diversity, and repetition.

- **Greedy/beam** maximize likelihood: great for closed-ended tasks, degenerate and repetitive for open-ended.
- **Temperature** reshapes the softmax: low = sharp/focused, high = flat/diverse.
- **Top-k** keeps a *fixed* number of tokens.
- **Top-p (nucleus)** keeps the smallest set covering mass $p$ — an *adaptive* cutoff that's narrow when the model is confident and wide when it's not, which is why it's the open-ended default.

**Quick-fire — say these out loud:**

- *What does the model actually output?* A probability distribution over the whole vocabulary, every step — not text.
- *Why does greedy repeat?* Locally-optimal tokens reinforce themselves; maximizing per-token likelihood maximizes the wrong objective for a sentence.
- *Temperature formula and the two limits?* $p_i = \text{softmax}(z_i/T)$; $T\to0$ is greedy (argmax), $T\to\infty$ is uniform.
- *Top-k vs top-p in one sentence?* Top-k keeps a fixed *count*; top-p keeps a fixed *mass*, so its count adapts to the distribution's shape.
- *Why is top-p usually better than top-k?* Its cutoff widens when the model is uncertain and tightens when it's confident — top-k can't.
- *What is neural text degeneration?* Likelihood-maximizing decoders (greedy/beam) produce repetitive loops; pure sampling produces incoherence; nucleus sampling is the sweet spot (Holtzman 2019).
- *Which decoder for translation? for chat?* Beam search for translation (closed-ended); nucleus sampling for chat (open-ended).
- *Is speculative decoding a decoding strategy?* No — it's a *speed* technique whose output is distributionally identical to your chosen strategy; it changes *how fast*, not *which token*.
- *Most common nucleus bug?* The off-by-one that drops the threshold-crossing token and can empty the nucleus → keep the crossing token, always keep top-1, use $\ge p$.

---

## Production implementation

Runnable services in this estate that put these decoding knobs behind a real serving path:

- **[inference-orchestrator](/python/python-production-examples/inference-orchestrator/readme)** — a continuous-batching scheduler with key-value and prefix-cache-aware routing behind an OpenAI-compatible API, where sampling parameters arrive per request.
- **[llm-serving-bench](/python/cross-service-workflows/llm-serving-bench)** — throughput and tail-latency measurement, so a decoder change shows up as a number.

---

## Pitfalls: symptoms, causes and fixes

Decoding is where many "the model is broken" tickets start. Start from what you see in the generated text — five symptoms cover most complaints:

| Symptom in the text | Likely cause | First fix |
|---|---|---|
| **Loops** — "the the the", repeated phrases | greedy decoding, or temperature too low | turn on sampling ($T\approx0.7$, top-p 0.9); only then add a repetition penalty of 1.1–1.2 |
| **Gibberish** — off-topic or invented words | temperature too high with no tail cut | lower $T$, and add top-p 0.9 to truncate the tail |
| **Bland** — the same safe answer every time | greedy, or $T$ near 0 | raise $T$ toward 0.8 and set top-p to 0.95 |
| **Too short** — truncated translations or summaries | beam search without length normalization, or an early end-of-sequence token | add length normalization ($\alpha\approx0.6$); for sampling set `min_new_tokens` |
| **Invalid structure** — JSON that won't parse, an invented enum value | unconstrained decoding | constrain the decoder with a grammar or schema; never regex-repair the output afterwards |

The mechanisms behind those symptoms, and the bugs that bite implementers:

- **Greedy / beam repetition on open-ended text.**
  - Mechanism: locally-optimal tokens reinforce themselves into a loop; maximizing likelihood maximizes the wrong thing (Holtzman 2019).
  - Fix: switch to nucleus sampling for open-ended generation; reserve greedy/beam for closed-ended tasks (translation, extraction, math).
- **Temperature too high → gibberish.**
  - At $T=2$+ the distribution flattens so far that nonsense tokens become probable (entropy 2.2 of a max 3.32 bits, in the [sampling page's demo](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/sampling-temperature-top-k-top-p)).
  - Fix: keep $T \le 1$ for factual work; if you want creativity, raise $T$ *and* tighten top-p so the flattened tail is still truncated.
- **Temperature too low → repetition.**
  - As $T \to 0$ you converge to greedy and inherit its loops.
  - Fix: don't set $T$ below ~0.3 for open-ended text; if you need determinism use greedy *and* a repetition penalty.
- **Top-k's fixed size is wrong on both ends.**
  - Too small when the model is uncertain (chops good tokens), too large when it's confident (admits junk).
  - Fix: prefer top-p, which adapts; or combine `top_k` and `top_p` (most libraries apply both — top-k as a hard cap, top-p as the adaptive cutoff).
- **The nucleus off-by-one / empty-nucleus crash.**
  - Covered on the [sampling page](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/sampling-temperature-top-k-top-p) — shift the mask, always keep the top-1 token, and check kept mass $\ge p$, not $> p$.
- **Repetition penalty side effects.**
  - Penalizing *all* previously-seen tokens suppresses legitimately-frequent words ("the", "is", "a") and can degrade fluency.
  - In code generation it can break syntax (you *need* to repeat `}` and `;`).
  - Fix: stay in the 1.1–1.2 band, scope the penalty to a recent window, exempt high-frequency function tokens, or prefer presence/frequency penalties tuned conservatively.
  - Treat it as a band-aid: if loops persist at 1.2, fix the decoder (sampling on, temperature up) before pushing the penalty past ~1.3.
- **Forgetting the seed → irreproducible bugs.**
  - Sampling is stochastic; without a fixed random number generator (RNG) seed the same prompt yields different outputs, and a bug you saw once won't reproduce.
  - Fix: seed the generator (the [repetition page's demo](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/repetition-and-degeneration-controls) passes an explicit `torch.Generator`), and log it. Greedy and beam are deterministic and need no seed.
- **"Temperature does nothing."**
  - With `do_sample=False`, temperature and top-p are **ignored**: greedy takes the argmax regardless.
  - Fix: temperature only matters when you are sampling — turn sampling on, or stop tuning a knob that is switched off.
- **Settings that don't transfer between models.**
  - A top-p tuned on a base model can be wrong for an aligned one, whose distribution is sharper, and the reverse.
  - Fix: re-tune per model; never copy magic numbers across checkpoints.
- **`float16` softmax overflow at extreme logits.**
  - Very large logits (or very low temperature, which *multiplies* them) can overflow in half precision before the softmax's max-subtraction kicks in.
  - Fix: compute the softmax in `float32`, or rely on a numerically-stable `log_softmax` — the same max-subtraction trick covered in [Loss Functions (softmax & cross-entropy stability)](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/loss-functions/loss-functions).

> [!TIP]
> When debugging generation, change **one** knob at a time and read a few samples.
> - Decoding bugs masquerade as model bugs, and the fix is usually a single parameter.
> - That only works if each symptom can be traced to the knob that caused it.

---

## References

Shared with the topic's companion file — see [Decoding & Sampling — references](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/decoding-and-sampling#references-further-reading).
