---
id: "deep-learning/interpretability-and-analysis/superposition-and-sparse-autoencoders"
topic: "Superposition and Sparse Autoencoders"
level: advanced
built_from: ["what-is-mechanistic-interpretability", "autoencoders"]
leads_to: ["deep-learning/interpretability-and-analysis/probing-attribution-and-feature-visualization"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Superposition and Sparse Autoencoders"
minutes: 15
category: interpretability-and-analysis
---

# Superposition and Sparse Autoencoders

> Networks represent far more features than they have neurons by packing them as **almost
> orthogonal directions** in activation space — *superposition*. That is why individual neurons
> are polysemantic and why reading them off one at a time fails. A **sparse autoencoder (SAE)** is
> the proposed fix: train a wide, sparsely activating autoencoder on a layer's activations, and
> its dictionary elements are candidate monosemantic features.

**Why it matters:** superposition explains a decade of confusing neuron-level results in one idea,
and sparse autoencoders turned it into a scalable method — Anthropic extracted millions of
features from a production model, and Google DeepMind released Gemma Scope, open SAEs for every
layer of Gemma 2. The 2025 correction matters just as much: controlled evaluations found SAEs did
**not** beat simple baselines on probing or steering, DeepMind's interpretability team publicly
deprioritised fundamental SAE research, and the current position is that SAEs are a tool for
*discovering unknown concepts*, not the canonical decomposition of a model.

**Start here — suggested path:**

1. **Understand the phenomenon** — read [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html) — **Elhage et al. (Anthropic, 2022)**. *A tiny model, fully solvable, where you can watch features get packed into fewer dimensions than they need.*
2. **See the proposed decoder** — read [Towards Monosemanticity: Decomposing Language Models With Dictionary Learning](https://transformer-circuits.pub/2023/monosemantic-features/index.html) — **Bricken et al. (Anthropic, 2023)**. *The sparse autoencoder recipe, plus the evaluation criteria for calling a feature interpretable.*
3. **See it at production scale** — read [Scaling Monosemanticity](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html) — **Templeton et al. (Anthropic, 2024)**. *Millions of features from Claude 3 Sonnet, including the steering demonstrations.*
4. **Read the strongest critique** — read [Are Sparse Autoencoders Useful? A Case Study in Sparse Probing](https://arxiv.org/abs/2502.16681) — **Kantamneni et al. (2025)**. *Careful head-to-head evaluation where SAEs lose to simple baselines; the paper that changed the field's posture.*
5. **Use them yourself** — browse [Neuronpedia](https://www.neuronpedia.org/) and the [SAELens documentation](https://decoderesearch.github.io/SAELens/) — **Neuronpedia / Joseph Bloom, Curt Tigges, David Chanin et al.** *Open SAEs you can load in a notebook and inspect feature by feature.*

## Why superposition happens

- **More features than neurons** — a model tracks many more concepts than its width allows if each gets its own direction.
- **Sparsity makes it cheap** — if only a few features are active at once, near-orthogonal directions interfere rarely; the model trades a little noise for a lot of capacity.
- **Consequence** — neurons are polysemantic, so neuron-level interpretation is looking at the wrong basis.
- **The SAE bet** — an overcomplete dictionary with an $L_1$ or top-$k$ sparsity penalty recovers the original basis; the open question is whether the recovered basis is the model's or the method's.

## Courses (free)

- [ARENA Chapter 1: Transformer Interpretability](https://www.arena.education/chapter1) — **ARENA (Callum McDougall)** — includes superposition and SAE training exercises with solutions.
- [SAELens documentation and tutorials](https://decoderesearch.github.io/SAELens/) — **SAELens maintainers** — the practical course: load a pretrained SAE, train your own, generate feature dashboards.
- [Getting Started in Mechanistic Interpretability](https://www.neelnanda.io/mechanistic-interpretability/getting-started) — **Neel Nanda** — the ordered path into this literature.

## Videos

- [The Dark Matter of AI (Mechanistic Interpretability)](https://www.youtube.com/watch?v=UGO_Ehywuxc) — **Welch Labs** — the clearest visual explanation of superposition and dictionary learning available.
- [Mechanistic Interpretability](https://www.youtube.com/@mechanisticinterpretabilit5092) — **Neel Nanda** — walkthroughs of the SAE literature as it developed.

## Key Papers

- [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html) — **Elhage et al. (Anthropic, 2022)** — the phenomenon, in a model small enough to fully understand.
- [Towards Monosemanticity](https://transformer-circuits.pub/2023/monosemantic-features/index.html) — **Bricken et al. (Anthropic, 2023)** — sparse dictionary learning on a one-layer transformer.
- [Sparse Autoencoders Find Highly Interpretable Features in Language Models](https://arxiv.org/abs/2309.08600) — **Cunningham, Ewart, Riggs, Huben & Sharkey (2023)** — the independent result that arrived at the same method.
- [Scaling Monosemanticity](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html) — **Templeton et al. (Anthropic, 2024)** — features and steering in a deployed model.
- [Scaling and evaluating sparse autoencoders](https://arxiv.org/abs/2406.04093) — **Gao et al. (OpenAI, 2024)** — top-$k$ SAEs and the scaling laws for dictionary size.
- [Gemma Scope: Open Sparse Autoencoders Everywhere All At Once on Gemma 2](https://arxiv.org/abs/2408.05147) — **Lieberum et al. (Google DeepMind, 2024)** — the open SAE suite that made this research reproducible outside frontier labs.
- [Are Sparse Autoencoders Useful? A Case Study in Sparse Probing](https://arxiv.org/abs/2502.16681) — **Kantamneni et al. (2025)** — the negative result.
- [Position: Use Sparse Autoencoders to Discover Unknown Concepts, Not to Act on Known Concepts](https://arxiv.org/abs/2506.23845) — **Movva et al. (2025)** — the reconciliation the field currently works from.

## Articles / Blogs (free, no paywall)

- [Transformer Circuits Thread](https://transformer-circuits.pub/) — **Anthropic interpretability team** — where each of these results was published first.
- [Progress update from the Google DeepMind mechanistic interpretability team](https://www.alignmentforum.org/posts/HpAr8k74mW4ivCvCu/summary-progress-update-1-from-the-gdm-mech-interp-team) — **Google DeepMind (Neel Nanda's team)** — replications, small investigations and the negative results that reset expectations.
- [Neuronpedia](https://www.neuronpedia.org/) — **Neuronpedia** — an interactive index of open SAE features; the fastest way to see what a "feature" is.
- [Mapping the Mind of a Large Language Model](https://www.anthropic.com/news/mapping-mind-language-model) — **Anthropic (2024)** — the accessible version of Scaling Monosemanticity.

## In this platform

- Prerequisites: [What Is Mechanistic Interpretability](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/what-is-mechanistic-interpretability/what-is-mechanistic-interpretability) · [Autoencoders](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/autoencoders/autoencoders)
- Related: [Transformer Circuits, Induction Heads and Attention Patterns](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/transformer-circuits-induction-heads-and-attention-patterns/transformer-circuits-induction-heads-and-attention-patterns) · [Probing, Attribution and Feature Visualization](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/probing-attribution-and-feature-visualization/probing-attribution-and-feature-visualization)
- The sparsity machinery elsewhere: [Regularization](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/regularization/regularization)
