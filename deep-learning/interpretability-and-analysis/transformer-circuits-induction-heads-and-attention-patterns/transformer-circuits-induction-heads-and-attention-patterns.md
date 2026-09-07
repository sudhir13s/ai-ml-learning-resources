---
id: "deep-learning/interpretability-and-analysis/transformer-circuits-induction-heads-and-attention-patterns"
topic: "Transformer Circuits, Induction Heads and Attention Patterns"
level: advanced
built_from: ["what-is-mechanistic-interpretability", "transformer-architecture"]
leads_to: ["deep-learning/interpretability-and-analysis/superposition-and-sparse-autoencoders", "deep-learning/interpretability-and-analysis/probing-attribution-and-feature-visualization"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Transformer Circuits, Induction Heads and Attention Patterns"
minutes: 15
category: interpretability-and-analysis
---

# Transformer Circuits, Induction Heads and Attention Patterns

> Rewrite a transformer as a **residual stream** that every layer reads from and writes to, and
> attention becomes two independent bilinear forms: $W_{QK}$ decides *where* to look and $W_{OV}$
> decides *what* to move. Under that decomposition a two-layer model contains a discoverable
> algorithm — the **induction head**: a previous-token head writes "the token before me was X",
> and a second head matches on that to complete `... X Y ... X → Y`.

**Why it matters:** induction heads are the clearest evidence that trained transformers contain
real algorithms, and their formation coincides with a visible bump in the loss curve and with the
onset of in-context learning. The 2025 successor is **attribution graphs** — replacing dense
multilayer-perceptron activations with interpretable transcoder features so a *specific prompt's*
computation can be traced end to end, which is how Anthropic showed a model planning a rhyme and
doing two-hop reasoning. The caveat worth stating in an interview: these are local, partial
explanations, validated by intervention rather than proven.

**Start here — suggested path:**

1. **Learn the decomposition** — read [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html) — **Elhage et al. (Anthropic, 2021)**. *Residual stream, QK and OV circuits, and the composition rules; every later result speaks this language.*
2. **Have it walked through** — watch [A Walkthrough of A Mathematical Framework for Transformer Circuits](https://www.youtube.com/watch?v=KV5gbOmHbjU) — **Neel Nanda**. *Three hours of someone re-deriving the paper on screen; far easier than reading it cold.*
3. **See the algorithm found in the wild** — read [In-context Learning and Induction Heads](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html) — **Olsson et al. (Anthropic, 2022)**. *Six independent arguments connecting induction heads to in-context learning.*
4. **See a full circuit in a real model** — read [Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 Small](https://arxiv.org/abs/2211.00593) — **Wang, Variengien, Conmy, Shlegeris & Steinhardt (2022)**. *26 heads, named by role, validated by ablation; the template for circuit discovery papers.*
5. **See the 2025 method** — read [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) — **Anthropic (2025)**, with the companion [Circuit Tracing methods paper](https://transformer-circuits.pub/2025/attribution-graphs/methods.html). *Attribution graphs applied to planning, arithmetic and multilingual features in a deployed model.*

## The vocabulary that unlocks the papers

- **Residual stream** — a shared communication channel; layers add to it, never overwrite it.
- **QK circuit** — $W_Q^\top W_K$ as one bilinear form on the stream; determines the attention pattern.
- **OV circuit** — $W_O W_V$; determines what is copied once a position is attended to.
- **Composition** — Q-, K- and V-composition, the three ways a later head can use an earlier head's output; induction heads are K-composition.
- **Attribution graph** — a per-prompt linearised graph over transcoder features; the 2025 replacement for hand-traced circuits.

## Courses (free)

- [ARENA Chapter 1: Transformer Interpretability](https://www.arena.education/chapter1) — **ARENA (Callum McDougall)** — the exercises walk you from a two-layer model to locating induction heads yourself.
- [TransformerLens documentation](https://transformerlensorg.github.io/TransformerLens/) — **TransformerLens maintainers** — the library the exercises use, with a "getting started in mech interp" guide.
- [Getting Started in Mechanistic Interpretability](https://www.neelnanda.io/mechanistic-interpretability/getting-started) — **Neel Nanda** — the ordered reading path through these papers.

## Videos

- [A Walkthrough of A Mathematical Framework for Transformer Circuits](https://www.youtube.com/watch?v=KV5gbOmHbjU) — **Neel Nanda** — the single most useful video for this page.
- [1L Attention — Theory](https://www.youtube.com/watch?v=7crsHGsh3p8) — **Mechanistic Interpretability (Neel Nanda)** — the one-layer case done by hand before the two-layer result.
- [The Dark Matter of AI](https://www.youtube.com/watch?v=UGO_Ehywuxc) — **Welch Labs** — includes an accessible visual account of circuit tracing.

## Key Papers

- [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html) — **Elhage et al. (Anthropic, 2021)** — the foundational decomposition.
- [In-context Learning and Induction Heads](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html) — **Olsson et al. (Anthropic, 2022)** — the mechanism behind in-context learning.
- [Interpretability in the Wild](https://arxiv.org/abs/2211.00593) — **Wang et al. (2022)** — the indirect-object-identification circuit in GPT-2 small.
- [Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) — **Anthropic (2025)** — cross-layer transcoders and attribution graphs.
- [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) — **Anthropic (2025)** — the case studies: planning, multi-hop reasoning, refusals, hallucination.
- [What Does BERT Look At? An Analysis of BERT's Attention](https://arxiv.org/abs/1906.04341) — **Clark, Khandelwal, Levy & Manning (2019)** — the earlier attention-pattern literature, and a useful warning that patterns alone are not explanations.

## Articles / Blogs (free, no paywall)

- [Tracing the Thoughts of a Large Language Model](https://www.anthropic.com/research/tracing-thoughts-language-model) — **Anthropic (2025)** — the readable summary of the attribution-graph results.
- [Transformer Circuits Thread](https://transformer-circuits.pub/) — **Anthropic interpretability team** — the running publication venue for this line of work.
- [Neuronpedia](https://www.neuronpedia.org/) — **Neuronpedia** — browse features, circuits and attribution graphs interactively rather than reading about them.
- [Open Problems in Mechanistic Interpretability](https://www.anthropic.com/research/engineering-challenges-interpretability) — **Anthropic** — what circuit analysis still cannot do.

## In this platform

- Prerequisites: [What Is Mechanistic Interpretability](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/what-is-mechanistic-interpretability/what-is-mechanistic-interpretability) · [Transformer Architecture](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/transformer-architecture/transformer-architecture)
- Next: [Superposition and Sparse Autoencoders](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/superposition-and-sparse-autoencoders/superposition-and-sparse-autoencoders) · [Probing, Attribution and Feature Visualization](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/probing-attribution-and-feature-visualization/probing-attribution-and-feature-visualization)
- Related: [Positional Encoding](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/positional-encoding/positional-encoding) · [Residual / Skip Connections](/ai-ml/ai-ml-learning-resources/deep-learning/stabilization-and-architectural-blocks/residual-skip-connections/residual-skip-connections)
