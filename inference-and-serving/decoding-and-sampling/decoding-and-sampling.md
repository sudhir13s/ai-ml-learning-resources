---
id: "09-llms/decoding-and-sampling"
topic: "Decoding & Sampling (greedy · beam · temperature · top-k · top-p)"
parent: "09-llms"
level: intermediate
built_from: ["09-llms/language-modeling-objectives", "softmax", "09-llms/decoder-only-architecture"]
interview_frequency: very-high
template: concept-deep
updated: 2026-10-08
tier: flagship
est_minutes: 15
leads_to: ["09-llms/decoding-and-sampling/greedy-and-beam-search", "09-llms/llm-evaluation-and-benchmarks"]
chapters:
  - "greedy-and-beam-search.md"
  - "sampling-temperature-top-k-top-p.md"
  - "repetition-and-degeneration-controls.md"
  - "constrained-and-guided-decoding.md"
  - "decoding-in-production.md"
core_idea: "Same weights, different text: coherence, diversity and repetition are set by how each next-token distribution is turned into a choice, and the robust choice cuts the unreliable tail adaptively before it samples."
title: "Decoding & Sampling (greedy · beam · temperature · top-k · top-p)"
minutes: 15
category: inference-and-serving
---

# Decoding & Sampling: turning the next-token distribution into text

A trained language model does **not** output text. At every step it outputs a *probability distribution over the whole vocabulary*.

- That is fifty thousand numbers that sum to 1, one per possible next token.
- "The capital of France is ___" produces a distribution where `Paris` might hold 0.92, `the` 0.01, `a` 0.008, and so on down a long tail.
- **Decoding** is the separate, deliberate algorithm that turns that distribution into one actual token, and then the next, and the next.
- The model proposes; the *decoder* disposes.

This is the most under-appreciated lever in all of large language model (LLM) usage. The *exact same model*, with the *exact same weights*, can produce very different text.

- It can give a crisp factual answer, a repetitive broken loop, or fluent creative prose.
- The only thing that changed was **how you picked tokens from its distributions**.
- Pick the single most-likely token every time and a powerful model collapses into "*I think that I think that I think that…*".
- Pick purely at random from the raw distribution and it dissolves into word salad.

The art is the narrow corridor between these two failures. Each setting in that corridor has a name: **greedy**, **beam search**, **temperature**, **top-k**, and **top-p (nucleus)**.

By the end of this course you'll be able to:

- explain **why** the choice of decoder changes coherence, diversity, and repetition so dramatically;
- derive how **temperature** reshapes the softmax, and predict the effect of $T=0.5$ vs $T=2.0$;
- explain the precise difference between **top-k** (fixed count) and **top-p** (adaptive mass), and *why top-p is usually better*;
- explain **neural text degeneration** (Holtzman 2019) — why likelihood-maximizing decoders loop, and why nucleus sampling fixes it;
- pick the right decoder for a task — **closed-ended** (translation, extraction) vs **open-ended** (chat, story);
- prove every one of these claims in runnable from-scratch code.

> [!NOTE]
> This page is about *which* token, not *how fast*.
> - [Speculative decoding](/ai-ml/ai-ml-learning-resources/inference-and-serving/speculative-decoding/speculative-decoding) is a pure speed trick: its output is provably **distributionally identical** to plain sampling.
> - Decoding *strategy*, the subject here, is the choice that **changes what text you get**. Speculation makes a strategy faster; it never changes which one you chose.

**The strategies at a glance.** Every decoder in this course reads the same logits; they differ in what they keep and how they pick. The axis that decides between them is **closed-ended vs open-ended**:

| Strategy | What it does | Output feel | Task shape it fits |
|---|---|---|---|
| **[Greedy](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/greedy-and-beam-search)** (argmax) | always the single most likely token | deterministic; loops on long text | closed-ended and short: extraction, arithmetic, a label |
| **[Beam search](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/greedy-and-beam-search)** | keeps the $b$ most probable *sequences* | high-likelihood, low-diversity, slower | closed-ended with one best sequence: translation, summarization |
| **[Temperature](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/sampling-temperature-top-k-top-p)** | rescales the logits before the softmax | the dial from focused to adventurous | both; it is combined with every sampling decoder |
| **[Top-k](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/sampling-temperature-top-k-top-p)** | keeps a fixed $k$ best tokens, then samples | bounded randomness, blind to confidence | open-ended, when a hard cap on candidates is enough |
| **[Top-p (nucleus)](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/sampling-temperature-top-k-top-p)** | keeps the smallest set covering mass $p$ | adaptive: tight when sure, wide when unsure | the open-ended default: chat, dialogue, stories |

---

## The problem: a distribution is not a sentence

Here is the felt problem. Run a model forward one step and you get a vector of logits $z \in \mathbb{R}^{|V|}$.

- The softmax turns it into a probability $p_i$ for each of the $|V|$ vocabulary tokens.
- You must emit exactly one token, then feed it back in and repeat.
- **What rule do you use to choose?**

Two obvious rules both fail, and feeling *why* they fail is the whole motivation.

**Naïve rule 1 — always take the most likely token (greedy).** Surely the highest-probability token is the "best"? On open-ended text it is not.

- Greedy decoding falls into **repetition loops**: once the model emits "*the United States and the United States*", the most-likely continuation is *again* "*and the United States*", because that phrase is now in the context reinforcing itself.
- The locally-optimal choice is globally catastrophic, and this is not a small-model artefact: **GPT-2-large does it too** (Holtzman et al. 2019).
- Greedy is *myopic*: it optimizes the next token, never the sentence.

**Naïve rule 2 — sample straight from the raw distribution.** If greedy is too rigid, just draw a token at random with probability $p_i$? The problem is the **long tail**.

- A 50,000-token vocabulary puts a *tiny* probability on each of thousands of irrelevant tokens.
- There are *so many* of them that their **combined** mass is large, and you'll regularly draw one.
- One absurd token ("*The capital of France is **bicycle**…*") derails the rest of the generation, because the model now has to continue from nonsense.
- Pure sampling is *too loose*.

```mermaid
---
title: Decoding sits between the model's distribution and the emitted token
---
graph LR
    L(["model logits z<br/>(|V| numbers)"]) --> SM["softmax<br/>p_i = e^{z_i} / Σ e^{z_j}"]
    SM --> DIST[("next-token distribution<br/>p over the vocab")]
    DIST --> G["DECODER<br/>which token to pick?"]
    G --> BAD1(["greedy → repetition loops"])
    G --> BAD2(["pure sampling → incoherence"])
    G --> GOOD(["truncated sampling → fluent + diverse"])

    class G focus
    class BAD1,BAD2 failure
```

*The two naïve rules fail at opposite extremes (the red nodes name the failures: loops and incoherence). Every good decoder lives in between: keep the plausible tokens, discard the tail, sample with controlled randomness.*

So we need a rule that is **random enough to be diverse and non-repetitive, but constrained enough to never wander into the nonsense tail.** That single sentence is the design brief for the rest of the course.

---

## Intuition first: the dinner-party menu

Before any math, the mental model I actually use.

Think of the model's distribution as a **menu the chef hands you each round**, with a recommendation score next to every dish.

- You order one dish and eat it.
- The chef then writes the *next* menu based on what you just ate.
- How do you order?

The five strategies, as ordering rules:

- **Greedy** = *always order the single top-scored dish.*
  - Decisive, but you eat the same "safe" dish forever.
  - Each choice shapes the next menu, so ordering "fries" once makes "fries" top-scored again and you spiral into fries-fries-fries. (Repetition.)
- **Pure sampling** = *roll a weighted die over the entire menu, including the dish the chef scored 0.0001.*
  - Occasionally you order the kitchen-sink special and the evening goes off the rails. (Incoherence.)
- **Temperature** = *how much you trust the scores.*
  - Low temperature ($T<1$): you trust the chef, so you almost always pick near the top — conservative, focused.
  - High temperature ($T>1$): you treat the scores as mere suggestions and spread your orders around — adventurous, wilder.
- **Top-k** = *"only let me order from the top 5 dishes."* A fixed-size shortlist, and a blunt instrument.
  - If there are really only 2 good dishes tonight you're still forced to consider 5.
  - If there are 30 equally-good dishes you're cruelly limited to 5.
- **Top-p (nucleus)** = *"give me the shortest shortlist that covers 90% of the recommendation score, and let me order from that."*
  - When one dish is clearly best, the shortlist is just that one dish.
  - When ten dishes are all plausible, the shortlist grows to include them all.
  - **The shortlist resizes itself to the chef's confidence.** That self-resizing is the entire reason nucleus sampling beats fixed top-k.

Hold a follow-up question to this analogy — *"what if two dishes tie at the 90% boundary?"* — and it still works.

- You include the tying dish: the boundary is "at least 90%", so the crossing dish stays on the list.
- We'll see that exact rule in the math.
- The analogy maps cleanly: **menu = distribution, score = probability, shortlist = the truncation set, how-much-you-trust-scores = temperature.**

```svg
<svg viewBox="0 0 760 376" xmlns="http://www.w3.org/2000/svg" font-family="ui-sans-serif, system-ui, sans-serif" data-legend="focus: the dishes this ordering rule lets you order">
<title>The dinner-party menu: greedy, top-k, top-p and temperature on one distribution</title>
<desc>A menu card lists the ten dishes of the page's PEAKED next-token distribution with the chef's score as a bar. Five scenes step through the ordering rules: the full menu, greedy keeping only cat, top-k keeping three, top-p keeping the one dish that already covers 90%, and temperature 2 flattening every score.</desc>
<rect x="24" y="24" width="712" height="328" rx="12" fill="none" stroke-width="1" style="stroke:var(--diagram-muted, #475569)"/>
<text x="48" y="56" font-size="14" font-weight="700" fill="currentColor" opacity="1">The menu: every dish with the chef's score<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;0;0;0;0"/></text>
<text x="48" y="56" font-size="14" font-weight="700" fill="currentColor" opacity="0">Greedy: always order the top dish<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;1;0;0;0"/></text>
<text x="48" y="56" font-size="14" font-weight="700" fill="currentColor" opacity="0">Top-k, k = 3: shortlist the three best<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;1;0;0"/></text>
<text x="48" y="56" font-size="14" font-weight="700" fill="currentColor" opacity="0">Top-p, p = 0.9: the shortest list covering 90%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;1;0"/></text>
<text x="48" y="56" font-size="14" font-weight="700" fill="currentColor" opacity="0">Temperature T = 2: trust the scores less<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;1"/></text>
<text x="56" y="84" font-size="11" style="fill:var(--diagram-muted, #475569)">dish (token)</text>
<text x="168" y="84" font-size="11" style="fill:var(--diagram-muted, #475569)">chef's score (probability)</text>
<g opacity="1"><animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;1;1;1;1"/>
<rect x="40" y="92" width="680" height="22" rx="4" fill-opacity="0" style="fill:var(--diagram-teal, #075e6b)"><animate attributeName="fill-opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0.16;0.16;0.16;0"/></rect>
<text x="56" y="108" font-size="13" font-weight="600" fill="currentColor" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace">cat</text>
<rect x="168" y="97" width="401.6" height="12" rx="2" fill="currentColor" fill-opacity="0.35"><animate attributeName="width" dur="15s" repeatCount="indefinite" keyTimes="0;0.8;0.84;1" values="401.6;401.6;251.1;251.1"/></rect>
<text x="704" y="108" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="1">91.3%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;1;1;1;0"/></text>
<text x="704" y="108" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="0">57.1%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;1"/></text>
</g>
<g opacity="1"><animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;0.3;1;0.3;1"/>
<rect x="40" y="114" width="680" height="22" rx="4" fill-opacity="0" style="fill:var(--diagram-teal, #075e6b)"><animate attributeName="fill-opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0.16;0;0"/></rect>
<text x="56" y="130" font-size="13" font-weight="600" fill="currentColor" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace">the</text>
<rect x="168" y="119" width="20.0" height="12" rx="2" fill="currentColor" fill-opacity="0.35"><animate attributeName="width" dur="15s" repeatCount="indefinite" keyTimes="0;0.8;0.84;1" values="20.0;20.0;56.0;56.0"/></rect>
<text x="704" y="130" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="1">4.5%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;1;1;1;0"/></text>
<text x="704" y="130" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="0">12.7%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;1"/></text>
</g>
<g opacity="1"><animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;0.3;1;0.3;1"/>
<rect x="40" y="136" width="680" height="22" rx="4" fill-opacity="0" style="fill:var(--diagram-teal, #075e6b)"><animate attributeName="fill-opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0.16;0;0"/></rect>
<text x="56" y="152" font-size="13" font-weight="600" fill="currentColor" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace">sat</text>
<rect x="168" y="141" width="7.4" height="12" rx="2" fill="currentColor" fill-opacity="0.35"><animate attributeName="width" dur="15s" repeatCount="indefinite" keyTimes="0;0.8;0.84;1" values="7.4;7.4;34.0;34.0"/></rect>
<text x="704" y="152" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="1">1.7%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;1;1;1;0"/></text>
<text x="704" y="152" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="0">7.7%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;1"/></text>
</g>
<g opacity="1"><animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;0.3;0.3;0.3;1"/>
<rect x="40" y="158" width="680" height="22" rx="4" fill-opacity="0" style="fill:var(--diagram-teal, #075e6b)"><animate attributeName="fill-opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;0"/></rect>
<text x="56" y="174" font-size="13" font-weight="600" fill="currentColor" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace">on</text>
<rect x="168" y="163" width="4.5" height="12" rx="2" fill="currentColor" fill-opacity="0.35"><animate attributeName="width" dur="15s" repeatCount="indefinite" keyTimes="0;0.8;0.84;1" values="4.5;4.5;26.5;26.5"/></rect>
<text x="704" y="174" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="1">1.0%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;1;1;1;0"/></text>
<text x="704" y="174" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="0">6.0%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;1"/></text>
</g>
<g opacity="1"><animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;0.3;0.3;0.3;1"/>
<rect x="40" y="180" width="680" height="22" rx="4" fill-opacity="0" style="fill:var(--diagram-teal, #075e6b)"><animate attributeName="fill-opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;0"/></rect>
<text x="56" y="196" font-size="13" font-weight="600" fill="currentColor" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace">mat</text>
<rect x="168" y="185" width="2.7" height="12" rx="2" fill="currentColor" fill-opacity="0.35"><animate attributeName="width" dur="15s" repeatCount="indefinite" keyTimes="0;0.8;0.84;1" values="2.7;2.7;20.6;20.6"/></rect>
<text x="704" y="196" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="1">0.6%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;1;1;1;0"/></text>
<text x="704" y="196" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="0">4.7%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;1"/></text>
</g>
<g opacity="1"><animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;0.3;0.3;0.3;1"/>
<rect x="40" y="202" width="680" height="22" rx="4" fill-opacity="0" style="fill:var(--diagram-teal, #075e6b)"><animate attributeName="fill-opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;0"/></rect>
<text x="56" y="218" font-size="13" font-weight="600" fill="currentColor" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace">dog</text>
<rect x="168" y="207" width="1.6" height="12" rx="2" fill="currentColor" fill-opacity="0.35"><animate attributeName="width" dur="15s" repeatCount="indefinite" keyTimes="0;0.8;0.84;1" values="1.6;1.6;16.1;16.1"/></rect>
<text x="704" y="218" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="1">0.4%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;1;1;1;0"/></text>
<text x="704" y="218" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="0">3.6%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;1"/></text>
</g>
<g opacity="1"><animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;0.3;0.3;0.3;1"/>
<rect x="40" y="224" width="680" height="22" rx="4" fill-opacity="0" style="fill:var(--diagram-teal, #075e6b)"><animate attributeName="fill-opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;0"/></rect>
<text x="56" y="240" font-size="13" font-weight="600" fill="currentColor" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace">ran</text>
<rect x="168" y="229" width="1.0" height="12" rx="2" fill="currentColor" fill-opacity="0.35"><animate attributeName="width" dur="15s" repeatCount="indefinite" keyTimes="0;0.8;0.84;1" values="1.0;1.0;12.5;12.5"/></rect>
<text x="704" y="240" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="1">0.2%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;1;1;1;0"/></text>
<text x="704" y="240" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="0">2.8%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;1"/></text>
</g>
<g opacity="1"><animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;0.3;0.3;0.3;1"/>
<rect x="40" y="246" width="680" height="22" rx="4" fill-opacity="0" style="fill:var(--diagram-teal, #075e6b)"><animate attributeName="fill-opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;0"/></rect>
<text x="56" y="262" font-size="13" font-weight="600" fill="currentColor" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace">fast</text>
<rect x="168" y="251" width="0.6" height="12" rx="2" fill="currentColor" fill-opacity="0.35"><animate attributeName="width" dur="15s" repeatCount="indefinite" keyTimes="0;0.8;0.84;1" values="0.6;0.6;9.7;9.7"/></rect>
<text x="704" y="262" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="1">0.1%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;1;1;1;0"/></text>
<text x="704" y="262" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="0">2.2%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;1"/></text>
</g>
<g opacity="1"><animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;0.3;0.3;0.3;1"/>
<rect x="40" y="268" width="680" height="22" rx="4" fill-opacity="0" style="fill:var(--diagram-teal, #075e6b)"><animate attributeName="fill-opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;0"/></rect>
<text x="56" y="284" font-size="13" font-weight="600" fill="currentColor" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace">blue</text>
<rect x="168" y="273" width="0.4" height="12" rx="2" fill="currentColor" fill-opacity="0.35"><animate attributeName="width" dur="15s" repeatCount="indefinite" keyTimes="0;0.8;0.84;1" values="0.4;0.4;7.6;7.6"/></rect>
<text x="704" y="284" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="1">0.1%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;1;1;1;0"/></text>
<text x="704" y="284" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="0">1.7%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;1"/></text>
</g>
<g opacity="1"><animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;0.3;0.3;0.3;1"/>
<rect x="40" y="290" width="680" height="22" rx="4" fill-opacity="0" style="fill:var(--diagram-teal, #075e6b)"><animate attributeName="fill-opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;0"/></rect>
<text x="56" y="306" font-size="13" font-weight="600" fill="currentColor" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace">sky</text>
<rect x="168" y="295" width="0.2" height="12" rx="2" fill="currentColor" fill-opacity="0.35"><animate attributeName="width" dur="15s" repeatCount="indefinite" keyTimes="0;0.8;0.84;1" values="0.2;0.2;5.9;5.9"/></rect>
<text x="704" y="306" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="1">0.1%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;1;1;1;0"/></text>
<text x="704" y="306" text-anchor="end" font-size="12" font-weight="500" fill="currentColor" opacity="0">1.3%<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;1"/></text>
</g>
<text x="48" y="340" font-size="12" font-weight="500" style="fill:var(--diagram-muted, #475569)" opacity="1">The page's PEAKED next-token distribution at temperature 1, most to least likely.<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="1;0;0;0;0"/></text>
<text x="48" y="340" font-size="12" font-weight="500" style="fill:var(--diagram-muted, #475569)" opacity="0">Greedy orders cat every time — 91.3% of the score, and no other dish is ever tried.<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;1;0;0;0"/></text>
<text x="48" y="340" font-size="12" font-weight="500" style="fill:var(--diagram-muted, #475569)" opacity="0">k = 3 keeps cat, the and sat; renormalized they become 93.6%, 4.7% and 1.7%.<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;1;0;0"/></text>
<text x="48" y="340" font-size="12" font-weight="500" style="fill:var(--diagram-muted, #475569)" opacity="0">cat alone already covers 91.3% ≥ 90%, so the shortlist is a single dish.<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;1;0"/></text>
<text x="48" y="340" font-size="12" font-weight="500" style="fill:var(--diagram-muted, #475569)" opacity="0">At T = 2 cat falls to 57.1%; the same p = 0.9 shortlist would now hold 6 dishes.<animate attributeName="opacity" dur="15s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;0.2;0.4;0.6;0.8" values="0;0;0;0;1"/></text>
</svg>
```

The menu, played on this course's own `PEAKED` distribution: greedy, top-k, top-p, then temperature. The same picture with every knob in your hands is the [Autoregressive Generation and Sampling Controls intuition](/ai-ml/ai-ml-intuitions/generation/autoregressive-generation/autoregressive-generation-and-sampling-controls-intuition).

![Animated — the temperature dial, swept. The same peaked next-token distribution reshapes as T moves: at T<1 nearly all mass collapses onto the single top token (low entropy — almost greedy); at T=1 it is the model's own distribution; at T>1 the mass spreads toward uniform (entropy climbs) and the bars turn amber. Temperature is the dial between "trust the top" and "spread it around." Hand-authored animated SVG (loops).](images/dec_temperature_softmax.svg)

---

## Where it matters: choosing the decoder is choosing the behaviour

The crux for practitioners: **the decoder is a product decision, not just a hyperparameter.** Match it to the task.

This is why API providers expose `temperature`, `top_p`, `top_k`, `frequency_penalty`, and `presence_penalty` as first-class parameters — they *are* the behaviour controls.

- A coding assistant runs near-greedy ($T\approx0.2$) for correctness.
- A brainstorming tool runs $T\approx1.0$ with $p\approx0.95$ for range.
- **Same model, different decoder, completely different product.**

The per-task settings — which decoder and which knob values for extraction, code, translation, summarization, chat, stories, evals and tool calls — are the playbook in [Decoding in Production](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/decoding-in-production).

---

## References

The curated link library for this topic — videos, courses, articles, papers, books, and internal cross-links — lives in a companion file so it can be reused as a standalone reference list:

**→ [Decoding & Sampling — references](/ai-ml/ai-ml-learning-resources/inference-and-serving/decoding-and-sampling/decoding-and-sampling#references-further-reading)**
