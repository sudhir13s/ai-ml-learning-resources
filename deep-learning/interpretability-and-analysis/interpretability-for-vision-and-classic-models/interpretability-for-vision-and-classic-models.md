---
id: "deep-learning/interpretability-and-analysis/interpretability-for-vision-and-classic-models"
topic: "Interpretability for Vision and Classic Models"
level: intermediate
built_from: ["cnns-and-convolution", "probing-attribution-and-feature-visualization"]
leads_to: []
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Interpretability for Vision and Classic Models"
minutes: 14
category: interpretability-and-analysis
---

# Interpretability for Vision and Classic Models

> Before circuits there was **explainability**: for a convolutional network, class activation
> mapping (CAM) and Grad-CAM produce a heatmap of which spatial regions drove a prediction; for a
> tabular model, **LIME** fits a local linear surrogate and **SHAP** assigns each feature its
> Shapley value from cooperative game theory. These are the methods a hiring manager expects you
> to know cold, and the ones you will actually be asked for in a model review.

**Why it matters:** they are the working interpretability of production machine learning —
gradient-boosted trees plus SHAP is still the standard explanation stack in credit, insurance and
healthcare, largely because SHAP has axioms and a fast exact algorithm for trees. The distinction
worth carrying: these methods explain a **prediction** (which input mattered), while mechanistic
interpretability explains a **mechanism** (which weights compute what). Knowing that saliency
methods can fail randomisation sanity checks, and that Shapley values assume feature independence
unless you handle correlation explicitly, is what separates a careful answer from a recited one.

**Start here — suggested path:**

1. **See the vision heatmap** — read [Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization](https://arxiv.org/abs/1610.02391) — **Selvaraju et al. (2016)**. *Weight each feature map by its gradient; works on any convolutional architecture without retraining.*
2. **See the tabular surrogate** — read ["Why Should I Trust You?": Explaining the Predictions of Any Classifier](https://arxiv.org/abs/1602.04938) — **Ribeiro, Singh & Guestrin (2016)**, with [the author's blog post](https://homes.cs.washington.edu/~marcotcr/blog/lime/). *LIME: perturb, weight by proximity, fit a sparse linear model.*
3. **See the axiomatic answer** — read [A Unified Approach to Interpreting Model Predictions](https://arxiv.org/abs/1705.07874) — **Lundberg & Lee (2017)**. *SHAP unifies LIME, DeepLIFT and Shapley values, and gives tree models an exact polynomial-time algorithm.*
4. **Learn where they break** — read [Sanity Checks for Saliency Maps](https://arxiv.org/abs/1810.03292) — **Adebayo et al. (2018)**. *Several popular methods produce the same map after the weights are randomised.*
5. **Get the reference text** — read [*Interpretable Machine Learning*](https://christophm.github.io/interpretable-ml-book/) — **Christoph Molnar**. *Free, complete, and the best single treatment of partial dependence, LIME, SHAP, counterfactuals and their assumptions.*

## Which method for which model

- **Convolutional network, spatial explanation** — Grad-CAM (any architecture) or CAM (needs global average pooling).
- **Any differentiable model, input attribution** — integrated gradients; always run the sanity checks.
- **Tree ensembles** — TreeSHAP; exact and fast, and the reason SHAP dominates tabular practice.
- **Any model, local explanation** — LIME; cheap and model-agnostic, but the surrogate is unstable under resampling.
- **The honest caveat** — all of these are *post hoc*; they explain a prediction, and none of them proves the model reasons the way the picture suggests.

## Courses (free)

- [Captum: Model Interpretability for PyTorch](https://captum.ai/) — **PyTorch team** — tutorials for Grad-CAM, integrated gradients, occlusion and layer attribution on real models.
- [SHAP documentation](https://shap.readthedocs.io/en/latest/) — **Scott Lundberg and contributors** — the API doubles as a course, with notebooks per model family.
- [ARENA Chapter 1: Transformer Interpretability](https://www.arena.education/chapter1) — **ARENA** — for the contrast: what mechanistic methods do that post-hoc attribution cannot.

## Videos

- [The Dark Matter of AI (Mechanistic Interpretability)](https://www.youtube.com/watch?v=UGO_Ehywuxc) — **Welch Labs** — frames why heatmaps were not enough and what replaced them.
- [Stanford CS224W Lecture 1.1 — Why Graphs](https://www.youtube.com/watch?v=JAB_plj2rbA) — **Stanford Online (Jure Leskovec)** — background for explaining structured, non-image models.

## Key Papers

- [Learning Deep Features for Discriminative Localization (CAM)](https://arxiv.org/abs/1512.04150) — **Zhou, Khosla, Lapedriza, Oliva & Torralba (2015)** — the original class activation map.
- [Grad-CAM](https://arxiv.org/abs/1610.02391) — **Selvaraju et al. (2016)** — the architecture-agnostic generalisation everyone uses.
- [Deep Inside Convolutional Networks](https://arxiv.org/abs/1312.6034) — **Simonyan, Vedaldi & Zisserman (2013)** — gradient saliency, the ancestor of all of this.
- ["Why Should I Trust You?" (LIME)](https://arxiv.org/abs/1602.04938) — **Ribeiro, Singh & Guestrin (2016)** — local surrogate explanations.
- [A Unified Approach to Interpreting Model Predictions (SHAP)](https://arxiv.org/abs/1705.07874) — **Lundberg & Lee (2017)** — the axiomatic framework and TreeSHAP.
- [Sanity Checks for Saliency Maps](https://arxiv.org/abs/1810.03292) — **Adebayo et al. (2018)** — the negative result every practitioner should know.
- [Axiomatic Attribution for Deep Networks](https://arxiv.org/abs/1703.01365) — **Sundararajan, Taly & Yan (2017)** — integrated gradients, the bridge between the two worlds.

## Articles / Blogs (free, no paywall)

- [The Building Blocks of Interpretability](https://distill.pub/2018/building-blocks/) — **Olah et al. (Distill, 2018)** — composes feature visualisation and attribution into interactive interfaces; still the high-water mark for the genre.
- [Feature Visualization](https://distill.pub/2017/feature-visualization/) — **Distill** — what a convolutional feature actually looks like.
- [Local Interpretable Model-Agnostic Explanations (LIME): An Introduction](https://homes.cs.washington.edu/~marcotcr/blog/lime/) — **Marco Tulio Ribeiro** — the author's own walkthrough.
- [pytorch-grad-cam](https://github.com/jacobgil/pytorch-grad-cam) — **Jacob Gildenblat** — maintained implementations of every CAM variant, with metrics for comparing them.
- [lime](https://github.com/marcotcr/lime) — **Marco Tulio Ribeiro** — the reference implementation.

## Books (free, with chapters)

- [*Interpretable Machine Learning* — Ch. 9 "Local Model-Agnostic Methods"](https://christophm.github.io/interpretable-ml-book/) — **Christoph Molnar** — free online; the reference treatment of LIME, SHAP and counterfactuals.

## In this platform

- Prerequisites: [CNNs & Convolution](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/cnns-and-convolution/cnns-and-convolution) · [Probing, Attribution and Feature Visualization](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/probing-attribution-and-feature-visualization/probing-attribution-and-feature-visualization)
- The classic models these methods explain: [Gradient Boosting & XGBoost](/ai-ml/ai-ml-learning-resources/classical-machine-learning/supervised-learning/trees-and-ensembles/gradient-boosting-xgboost/gradient-boosting-xgboost) · [Random Forests](/ai-ml/ai-ml-learning-resources/classical-machine-learning/supervised-learning/trees-and-ensembles/random-forests/random-forests) · [Decision Trees](/ai-ml/ai-ml-learning-resources/classical-machine-learning/supervised-learning/trees-and-ensembles/decision-trees/decision-trees)
- The mechanistic alternative: [What Is Mechanistic Interpretability](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/what-is-mechanistic-interpretability/what-is-mechanistic-interpretability)
