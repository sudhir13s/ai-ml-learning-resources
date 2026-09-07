---
id: "deep-learning/interpretability-and-analysis/what-is-mechanistic-interpretability"
topic: "What Is Mechanistic Interpretability"
level: intermediate
built_from: ["transformer-architecture", "backpropagation-and-computational-graphs"]
leads_to: ["transformer-circuits-induction-heads-and-attention-patterns", "superposition-and-sparse-autoencoders"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 14
title: "What Is Mechanistic Interpretability"
minutes: 14
category: interpretability-and-analysis
---

# What Is Mechanistic Interpretability

> Mechanistic interpretability tries to **reverse-engineer a trained network into human-readable
> algorithms** — not "which input pixels mattered", but "which circuit of weights implements this
> behaviour, and what does each direction in activation space mean". Two objects carry the whole
> field: a **feature** (a direction in activation space that represents something) and a
> **circuit** (a subgraph of features and weights that computes something).

**Why it matters:** a model's weights are the only complete description of what it will do, and
we cannot read them. That gap — sometimes called the *dark matter* of these systems — is the
reason interpretability sits under safety, debugging, and evaluation at once. In 2026 this is no
longer purely academic: Anthropic's attribution graphs trace multi-step reasoning inside a
production model, and sparse-autoencoder features are used to steer behaviour. The framing to
carry into any discussion is that interpretability is **descriptive, not yet reliable**: features
found by current methods are real but incomplete, and the field is openly arguing about how much
they explain.

**Start here — suggested path:**

1. **See the problem before the machinery** — watch [The Dark Matter of AI (Mechanistic Interpretability)](https://www.youtube.com/watch?v=UGO_Ehywuxc) — **Welch Labs**. *A visual, honest introduction to why a trained network is opaque and what "finding a feature" actually looks like.*
2. **Get the two core objects** — read [Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/) — **Olah, Cammarata, Schubert, Goh, Petrov & Carter (Distill, 2020)**. *Features, circuits and universality, stated as three testable claims about neural networks.*
3. **Learn the vocabulary** — read [A Comprehensive Mechanistic Interpretability Explainer and Glossary](https://www.neelnanda.io/mechanistic-interpretability/glossary) — **Neel Nanda**. *The reference for every term the papers assume you already know.*
4. **Watch the field's own lectures** — [Mechanistic Interpretability](https://www.youtube.com/@mechanisticinterpretabilit5092) — **Neel Nanda's channel**, starting with the [Transformer Circuits playlist](https://www.youtube.com/playlist?list=PLoyGOS2WIonajhAVqKUgEMNmeq3nEeM51). *Rough, unpolished, and much closer to how the research is actually done than a produced course.*
5. **Do the exercises** — work through [ARENA Chapter 1: Transformer Interpretability](https://www.arena.education/chapter1) — **Callum McDougall et al.** *The standard hands-on curriculum: build a transformer, then find induction heads in it with TransformerLens.*

## The claims the field is testing

- **Features** — networks represent human-meaningful concepts as directions in activation space.
- **Circuits** — those features are connected by weights into subgraphs that implement algorithms.
- **Universality** — analogous features and circuits recur across models trained on similar data.
- **The open question** — whether the features current tools recover are the model's *actual* units of computation or a convenient basis imposed by the method.

## Courses (free)

- [ARENA Chapter 1: Transformer Interpretability](https://www.arena.education/chapter1) — **ARENA (Callum McDougall)** — the compulsory-plus-bonus curriculum used to train new interpretability researchers; all notebooks are free.
- [Getting Started in Mechanistic Interpretability](https://www.neelnanda.io/mechanistic-interpretability/getting-started) — **Neel Nanda** — a curated study path with prerequisites, papers and exercises in order.
- [TransformerLens documentation](https://transformerlensorg.github.io/TransformerLens/) — **TransformerLens maintainers** — the library tutorials double as a course on activation-level analysis.

## Videos

- [The Dark Matter of AI (Mechanistic Interpretability)](https://www.youtube.com/watch?v=UGO_Ehywuxc) — **Welch Labs** — the best visual introduction currently available.
- [Mechanistic Interpretability](https://www.youtube.com/@mechanisticinterpretabilit5092) — **Neel Nanda** — the researcher's own channel of walkthroughs and paper readings.
- [1L Attention — Theory](https://www.youtube.com/watch?v=7crsHGsh3p8) — **Mechanistic Interpretability (Neel Nanda)** — a one-layer attention-only model worked through by hand; the exact exercise the field starts from.

## Key Papers

- [Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/) — **Olah et al. (Distill, 2020)** — the manifesto that named features, circuits and universality.
- [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html) — **Elhage et al. (Anthropic, 2021)** — the algebraic decomposition every later result uses.
- [Mechanistic Interpretability for AI Safety — A Review](https://arxiv.org/abs/2404.14082) — **Bereska & Gavves (2024)** — the best single survey of methods, results and open problems.
- [An Extremely Opinionated Annotated List of My Favourite Mechanistic Interpretability Papers](https://www.neelnanda.io/mechanistic-interpretability/favourite-papers) — **Neel Nanda** — a reading list with the reason each paper matters, maintained by a practitioner.

## Articles / Blogs (free, no paywall)

- [Transformer Circuits Thread](https://transformer-circuits.pub/) — **Chris Olah and the Anthropic interpretability team** — the primary venue; almost every foundational result appears here first.
- [Mapping the Mind of a Large Language Model](https://www.anthropic.com/news/mapping-mind-language-model) — **Anthropic (2024)** — the accessible announcement of features found in a production model.
- [A Comprehensive Mechanistic Interpretability Explainer and Glossary](https://www.neelnanda.io/mechanistic-interpretability/glossary) — **Neel Nanda** — the field's dictionary.
- [Distill Circuits thread](https://distill.pub/2020/circuits/) — **Distill** — the original vision-model circuits series, still the clearest worked examples.

## In this platform

- Prerequisites: [Transformer Architecture](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/transformer-architecture/transformer-architecture) · [Attention Mechanism](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/attention-mechanism/attention-mechanism)
- Next in this sub-area: [Transformer Circuits, Induction Heads and Attention Patterns](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/transformer-circuits-induction-heads-and-attention-patterns/transformer-circuits-induction-heads-and-attention-patterns) · [Superposition and Sparse Autoencoders](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/superposition-and-sparse-autoencoders/superposition-and-sparse-autoencoders)
- The classic-model bridge: [Interpretability for Vision and Classic Models](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/interpretability-for-vision-and-classic-models/interpretability-for-vision-and-classic-models)
