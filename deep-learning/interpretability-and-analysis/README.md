---
id: "deep-learning/interpretability-and-analysis"
topic: "Interpretability and Analysis"
level: advanced
built_from: ["transformer-architecture", "cnns-and-convolution"]
updated: 2026-09-07
---

# Interpretability and Analysis

> Opening the model. Two traditions meet here: **post-hoc explainability** (Grad-CAM, LIME, SHAP)
> answers "which input drove this prediction", and **mechanistic interpretability** (circuits,
> superposition, sparse autoencoders) answers "which weights implement this behaviour". This
> sub-area curates the best free resources for both, best-first.

**Start here:** watch [The Dark Matter of AI (Mechanistic Interpretability)](https://www.youtube.com/watch?v=UGO_Ehywuxc) — **Welch Labs** — then read [Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/) — **Chris Olah et al. (Distill)**.

## Concept Index

1. [What Is Mechanistic Interpretability](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/what-is-mechanistic-interpretability/what-is-mechanistic-interpretability)
2. [Transformer Circuits, Induction Heads and Attention Patterns](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/transformer-circuits-induction-heads-and-attention-patterns/transformer-circuits-induction-heads-and-attention-patterns)
3. [Superposition and Sparse Autoencoders](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/superposition-and-sparse-autoencoders/superposition-and-sparse-autoencoders)
4. [Probing, Attribution and Feature Visualization](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/probing-attribution-and-feature-visualization/probing-attribution-and-feature-visualization)
5. [Interpretability for Vision and Classic Models](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/interpretability-for-vision-and-classic-models/interpretability-for-vision-and-classic-models)

## Courses (free)

- [ARENA Chapter 1: Transformer Interpretability](https://www.arena.education/chapter1) — **ARENA (Callum McDougall)** — the standard hands-on curriculum, notebooks and solutions free.
- [Getting Started in Mechanistic Interpretability](https://www.neelnanda.io/mechanistic-interpretability/getting-started) — **Neel Nanda** — an ordered study path with prerequisites and exercises.
- [Captum: Model Interpretability for PyTorch](https://captum.ai/) — **PyTorch team** — the attribution toolkit, with tutorials per method.

## Videos

- [The Dark Matter of AI (Mechanistic Interpretability)](https://www.youtube.com/watch?v=UGO_Ehywuxc) — **Welch Labs** — the best visual introduction to features and superposition.
- [A Walkthrough of A Mathematical Framework for Transformer Circuits](https://www.youtube.com/watch?v=KV5gbOmHbjU) — **Neel Nanda** — the foundational paper, re-derived on screen.
- [Mechanistic Interpretability](https://www.youtube.com/@mechanisticinterpretabilit5092) — **Neel Nanda** — the researcher's own channel of rough, honest walkthroughs.

## Key Papers

- [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html) — **Elhage et al. (Anthropic, 2021)** — the decomposition the field runs on.
- [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html) — **Elhage et al. (Anthropic, 2022)** — why neurons are polysemantic.
- [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) — **Anthropic (2025)** — attribution graphs applied to a production model.
- [Grad-CAM](https://arxiv.org/abs/1610.02391) — **Selvaraju et al. (2016)** — the vision method still in daily use.
- [A Unified Approach to Interpreting Model Predictions (SHAP)](https://arxiv.org/abs/1705.07874) — **Lundberg & Lee (2017)** — the tabular standard.

## Articles / Blogs

- [Transformer Circuits Thread](https://transformer-circuits.pub/) — **Anthropic interpretability team** — the primary venue for mechanistic results.
- [Distill Circuits thread](https://distill.pub/2020/circuits/) — **Distill** — the original, still-unmatched worked examples.
- [Neuronpedia](https://www.neuronpedia.org/) — **Neuronpedia** — browse real features and attribution graphs interactively.

## Books (free, with chapters)

- [*Interpretable Machine Learning*](https://christophm.github.io/interpretable-ml-book/) — **Christoph Molnar** — free and complete; the reference for post-hoc methods and their assumptions.

## In this platform

- Upstream: [Transformer Architecture](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/transformer-architecture/transformer-architecture) · [CNNs & Convolution](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/cnns-and-convolution/cnns-and-convolution) · [Autoencoders](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/autoencoders/autoencoders)
- Applied to classic models: [Gradient Boosting & XGBoost](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/trees-and-ensembles/gradient-boosting-xgboost/gradient-boosting-xgboost) · [Random Forests](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/trees-and-ensembles/random-forests/random-forests)
