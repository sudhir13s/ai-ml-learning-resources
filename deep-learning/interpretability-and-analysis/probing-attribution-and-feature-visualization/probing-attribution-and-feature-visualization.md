---
id: "deep-learning/interpretability-and-analysis/probing-attribution-and-feature-visualization"
topic: "Probing, Attribution and Feature Visualization"
level: advanced
built_from: ["what-is-mechanistic-interpretability", "transformer-circuits-induction-heads-and-attention-patterns"]
leads_to: ["deep-learning/interpretability-and-analysis/interpretability-for-vision-and-classic-models"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Probing, Attribution and Feature Visualization"
minutes: 15
category: interpretability-and-analysis
---

# Probing, Attribution and Feature Visualization

> Three families of tools sit under circuit analysis. **Probing** trains a small classifier on
> frozen activations to ask *is this information present?* **Attribution** assigns credit for an
> output back to inputs or components — integrated gradients, activation patching, attribution
> patching. **Feature visualization** synthesises the input that maximally excites a unit, to ask
> *what does this direction represent?*

**Why it matters:** these are the everyday instruments, and each has a well-known way of lying.
A probe that reads a concept proves the information is *present*, not that the model *uses* it —
which is exactly what control tasks and selectivity were invented to measure. Gradient-based
saliency can pass a visual sanity check while being independent of the model's weights. Only
**interventional** methods — patch a clean activation into a corrupted run and see whether the
output flips — establish a causal claim, which is why activation patching became the default
evidence standard in circuit papers.

**Start here — suggested path:**

1. **See the causal method first** — read [How to use and interpret activation patching](https://arxiv.org/abs/2404.15255) — **Heimersheim & Nanda (2024)**. *A short, practical guide to the technique everything else is validated against, including the ways it misleads.*
2. **Learn the scalable approximation** — read [Attribution Patching](https://www.neelnanda.io/mechanistic-interpretability/attribution-patching) — **Neel Nanda**. *A linear approximation that makes patching feasible over every component at once.*
3. **Get probing right** — read [Designing and Interpreting Probes with Control Tasks](https://arxiv.org/abs/1909.03368) — **Hewitt & Liang (2019)**. *Selectivity: the discipline that separates "the representation encodes it" from "my probe memorised it".*
4. **Understand gradient attribution** — read [Axiomatic Attribution for Deep Networks](https://arxiv.org/abs/1703.01365) — **Sundararajan, Taly & Yan (2017)**. *Integrated gradients derived from two axioms rather than proposed by analogy.*
5. **See what a feature looks like** — read [Feature Visualization](https://distill.pub/2017/feature-visualization/) — **Olah, Mordvintsev & Schubert (Distill, 2017)**. *Optimisation-based visualisation, and the regularisation needed to keep the results meaningful.*

## Which tool answers which question

- **Is the information there?** — a linear probe; report selectivity against a control task, never raw accuracy alone.
- **Does the model use it?** — activation patching or ablation; a causal intervention, not a correlation.
- **Which input tokens or pixels mattered?** — integrated gradients or SHAP-style attribution; check it against the sanity checks before trusting it.
- **What does this direction mean?** — feature visualisation, dataset examples of maximal activation, or a sparse-autoencoder dashboard.

## Courses (free)

- [ARENA Chapter 1: Transformer Interpretability](https://www.arena.education/chapter1) — **ARENA (Callum McDougall)** — the patching and probing exercises, with solutions.
- [TransformerLens documentation](https://transformerlensorg.github.io/TransformerLens/) — **TransformerLens maintainers** — hooks, caching and patching are the library's core API; the docs teach the method.
- [Captum: Model Interpretability for PyTorch](https://captum.ai/) — **PyTorch team** — reference implementations and tutorials for every gradient-attribution method named here.

## Videos

- [A Walkthrough of A Mathematical Framework for Transformer Circuits](https://www.youtube.com/watch?v=KV5gbOmHbjU) — **Neel Nanda** — shows patching used as the evidence for each claim.
- [The Dark Matter of AI](https://www.youtube.com/watch?v=UGO_Ehywuxc) — **Welch Labs** — includes a visual account of attribution and feature dashboards.
- [Mechanistic Interpretability](https://www.youtube.com/@mechanisticinterpretabilit5092) — **Neel Nanda** — research walkthroughs where these tools are applied live.

## Key Papers

- [Understanding intermediate layers using linear classifier probes](https://arxiv.org/abs/1610.01644) — **Alain & Bengio (2016)** — the paper that introduced probing.
- [Designing and Interpreting Probes with Control Tasks](https://arxiv.org/abs/1909.03368) — **Hewitt & Liang (2019)** — selectivity, and why an accurate probe can mean nothing.
- [Axiomatic Attribution for Deep Networks](https://arxiv.org/abs/1703.01365) — **Sundararajan, Taly & Yan (2017)** — integrated gradients.
- [Sanity Checks for Saliency Maps](https://arxiv.org/abs/1810.03292) — **Adebayo et al. (2018)** — the randomisation tests several popular saliency methods fail.
- [How to use and interpret activation patching](https://arxiv.org/abs/2404.15255) — **Heimersheim & Nanda (2024)** — the practical standard for causal interventions.
- [Interpretability in the Wild](https://arxiv.org/abs/2211.00593) — **Wang et al. (2022)** — patching used end to end to establish a circuit.
- [Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps](https://arxiv.org/abs/1312.6034) — **Simonyan, Vedaldi & Zisserman (2013)** — the origin of both gradient saliency and activation maximisation.

## Articles / Blogs (free, no paywall)

- [Feature Visualization](https://distill.pub/2017/feature-visualization/) — **Distill (Olah, Mordvintsev & Schubert)** — the definitive treatment, with interactive examples.
- [Attribution Patching](https://www.neelnanda.io/mechanistic-interpretability/attribution-patching) — **Neel Nanda** — the scalable gradient approximation to patching.
- [SAELens documentation](https://decoderesearch.github.io/SAELens/) — **SAELens maintainers** — feature dashboards as the modern replacement for single-neuron visualisation.
- [Neuronpedia](https://www.neuronpedia.org/) — **Neuronpedia** — browse maximal-activating examples and attribution graphs without writing code.

## In this platform

- Prerequisites: [What Is Mechanistic Interpretability](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/what-is-mechanistic-interpretability/what-is-mechanistic-interpretability) · [Transformer Circuits, Induction Heads and Attention Patterns](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/transformer-circuits-induction-heads-and-attention-patterns/transformer-circuits-induction-heads-and-attention-patterns)
- Next: [Interpretability for Vision and Classic Models](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/interpretability-for-vision-and-classic-models/interpretability-for-vision-and-classic-models)
- Related: [Superposition and Sparse Autoencoders](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/superposition-and-sparse-autoencoders/superposition-and-sparse-autoencoders) · [Backpropagation & Computational Graphs](/ai-ml/ai-ml-learning-resources/deep-learning/neural-network-foundations/backpropagation-and-computational-graphs/backpropagation-and-computational-graphs)
