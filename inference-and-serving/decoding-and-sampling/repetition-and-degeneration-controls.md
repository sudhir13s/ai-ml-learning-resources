---
id: "09-llms/decoding-and-sampling/repetition-and-degeneration-controls"
topic: "Decoding: Repetition and Degeneration Controls"
parent: "09-llms"
chapter_of: "09-llms/decoding-and-sampling"
chapter: 3
level: intermediate
built_from: ["09-llms/decoding-and-sampling"]
interview_frequency: very-high
template: concept-chapter
updated: 2026-10-08
tier: flagship
est_minutes: 8
leads_to: ["09-llms/decoding-and-sampling/constrained-and-guided-decoding"]
core_idea: "A repetition penalty pushes down tokens already emitted to break a loop, but it treats the symptom: it cannot tell a needed repeat from a stuck one, so the first fix for looping text is to turn sampling on."
title: "Repetition and Degeneration Controls"
minutes: 8
category: inference-and-serving
---

# Repetition and degeneration controls: breaking the loop

Even a well-chosen sampler can drift into repeats; this page covers the controls that push back on them, and where they stop helping.

## Repetition penalty: a loop breaker, not a cure

[Greedy and low-temperature decoding](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/greedy-and-beam-search) loop because a phrase already in the context makes itself likelier. The **repetition penalty** $\rho \ge 1$ pushes back on exactly the tokens already emitted:

$$z'_i = \begin{cases} z_i / \rho & \text{if } i \text{ was generated and } z_i > 0 \\ z_i \cdot \rho & \text{if } i \text{ was generated and } z_i \le 0 \\ z_i & \text{otherwise} \end{cases}$$

> [!NOTE]
> **Source:** the penalized sampling rule is introduced in [Keskar et al., *CTRL: A Conditional Transformer Language Model for Controllable Generation* (2019)](https://arxiv.org/abs/1909.05858). The sign branch for negative logits is how [Hugging Face `transformers`](https://huggingface.co/docs/transformers/en/generation_strategies) implements `repetition_penalty`.

What each part of the rule does, and where it stops helping:

- **Two branches, one direction.** Dividing a negative logit by $\rho$ would move it *toward zero* and make the token likelier; multiplying it pushes it further down instead.
- **A presence test, not a count.** A token said once and a token said ten times get the same penalty.
  - OpenAI-style `presence_penalty` and `frequency_penalty` are the subtractive cousins (below).
  - The frequency form does scale with the count.
- **The safe band is $\rho \approx 1.1$–$1.2$.** On the flat toy distribution, $\rho = 1.2$ after emitting `the`, `the`, `on` drops both tokens out of the top four and greedy switches to `cat` — the demo prints it below.
- **Past about 1.3 it garbles text.** A sentence genuinely needs "the" and "a"; code needs `}` and `;` again and again.

> [!NOTE]
> The penalty treats the symptom. If output still loops at $\rho = 1.2$, the cause is almost always greedy decoding or a temperature set too low — switch on sampling before raising the penalty.

---

## The other repetition controls

The repetition penalty is one of four direct controls; each edits the logits or the search before a token is picked:

- **Frequency and presence penalties** (the OpenAI API knobs) are additive adjustments to the logits, tuned independently.
  - **Frequency penalty** subtracts an amount proportional to how many times a token has already appeared, escalating against overused words.
  - **Presence penalty** subtracts a flat amount once a token has appeared at all, nudging toward new topics.
- **No-repeat n-gram blocking** (`no_repeat_ngram_size = n`) is a hard constraint: no n-gram that has already occurred may be emitted.
  - With $n = 3$ the model can never repeat a trigram — blunt but effective.
  - The risk is blocking phrases that legitimately recur, such as names and technical terms.
- **Contrastive search** is a *deterministic* decoder that attacks repetition at the representation level.
  - Each candidate's score is its model probability **minus** a degeneration penalty: its highest cosine similarity to the hidden states of tokens already generated.
  - With $k = 4$–$8$ candidates and penalty weight $\alpha \approx 0.6$ it gives coherent, non-repeating text, often the best quality without sampling.
  - **Source:** [Su et al., *A Contrastive Framework for Neural Text Generation* (2022)](https://arxiv.org/abs/2202.06417).

> [!TIP]
> These controls stack with the sampling knobs, so stack them lightly.
> - A robust chat default is `temperature ≈ 0.7, top_p ≈ 0.9, repetition_penalty ≈ 1.1` — sample for variety, discourage exact repeats a little.
> - Each control removes probability mass; all of them at full strength gives stilted, word-avoiding text.

---

## Loops broken, and greedy set against sampling

The [sampling page's script](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/sampling-temperature-top-k-top-p) — its `VOCAB`, `FLAT` and `top_p_filter` — gains two more blocks: the repetition penalty, and five draws from one distribution, greedy against sampled. Both run on the **flat** toy distribution, where no token dominates:

```step
///FILE decoding_sampling_loops.py
def repetition_penalty(logits, generated_ids, penalty):
    penalized = logits.clone()                                   # never mutate the caller's logits
    seen = torch.tensor(sorted(set(generated_ids)), dtype=torch.long)
    seen_logits = penalized[seen]
    penalized[seen] = torch.where(seen_logits > 0, seen_logits / penalty, seen_logits * penalty)
    return penalized

already = [VOCAB.index("the"), VOCAB.index("the"), VOCAB.index("on")]
after = F.softmax(repetition_penalty(FLAT, already, 1.2), dim=-1)

gen = torch.Generator(device="cpu").manual_seed(0)
shaped = top_p_filter(FLAT, 0.9) / 0.8                           # truncate first, then temperature
greedy  = [VOCAB[int(torch.argmax(FLAT))] for _ in range(5)]
sampled = [VOCAB[int(torch.multinomial(F.softmax(shaped, -1), 1, generator=gen))] for _ in range(5)]
```

Output (CPU, from the full script, top four tokens shown):

```text
[repetition] penalty=1.2 after emitting 'the','the','on' (FLAT dist):
   before  the:0.129  on:0.117  cat:0.111  dog:0.106
   after   cat:0.120  dog:0.115  sat:0.109  fast:0.104

[greedy vs sampled] FLAT dist, 5 draws (top-p=0.9, then T=0.8):
   greedy   ['the', 'the', 'the', 'the', 'the']
   sampled  ['sky', 'cat', 'sat', 'on', 'cat']
```

What the two blocks show:

- **The penalty re-ranks plausible tokens; it does not judge them.** `the` and `on` leave the top four and `cat` leads at 0.120 — useful against a loop, blind to whether `the` was needed.
- **Greedy says the same thing every time the step looks the same.** Five identical `the`s is the repetition trap in miniature.
- **Sampling from the same distribution gives four different tokens in five draws.** `sky` is a legitimate pick: the flat nucleus keeps 9 of the 10 tokens, dropping only `ran`.

---

## References

Shared with the topic's companion file — see [Decoding & Sampling — references](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/decoding-and-sampling#references-further-reading).
