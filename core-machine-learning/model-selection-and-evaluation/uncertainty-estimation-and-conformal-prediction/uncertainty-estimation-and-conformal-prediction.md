---
id: "core-machine-learning/model-selection-and-evaluation/uncertainty-estimation-and-conformal-prediction"
topic: "Uncertainty Estimation & Conformal Prediction"
level: advanced
built_from: ["calibration-and-reliability-diagrams", "cross-validation", "bagging"]
leads_to: ["core-machine-learning/model-selection-and-evaluation/error-analysis-and-model-debugging"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Uncertainty Estimation & Conformal Prediction"
minutes: 16
category: model-selection-and-evaluation
---

# Uncertainty Estimation & Conformal Prediction
> Calibration makes a single number honest; **uncertainty estimation** asks the harder question —
> *how much of this error is irreducible noise in the data, and how much is the model not knowing?*
> Those are **aleatoric** and **epistemic** uncertainty. **Conformal prediction** then converts any
> model's scores into **prediction sets with a finite-sample coverage guarantee** — "the true label
> is in this set 90% of the time" — assuming only that the data are exchangeable.

**Why it matters:** the deployable form of "I don't know". Aleatoric uncertainty does not shrink
with more data (two identical inputs with different labels); epistemic uncertainty does, which is
why it drives **active learning** and **out-of-distribution (OOD) detection**. Conformal prediction
is the part interviewers increasingly probe because it is **distribution-free, model-agnostic and
cheap** — one calibration split, one quantile — and because it is the standard way to give an LLM
or a medical classifier a defensible **abstention** policy. The traps: exchangeability breaks under
distribution shift and under time series; **marginal** coverage is not **conditional** coverage
(90% overall can be 60% for a minority slice); and a wide set is a *correct* answer, not a bug.

**Start here — suggested path:**

1. **Separate the two uncertainties** — read [What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision?](https://arxiv.org/abs/1703.04977) — **Kendall & Gal (2017)**. *The clearest statement of aleatoric versus epistemic, with a loss that learns both.*
2. **Get the cheap, strong baseline** — read [Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles](https://arxiv.org/abs/1612.01474) — **Lakshminarayanan, Pritzel & Blundell (2017, DeepMind)**. *Five independently seeded models beat most Bayesian machinery; this is the bar any new method must clear.*
3. **Learn conformal prediction properly** — read [A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification](https://arxiv.org/abs/2107.07511) — **Angelopoulos & Bates (2021)**. *Split conformal in one page of math, then extensions to classification, regression, segmentation and risk control.*
4. **Watch the author explain it** — watch [Rising Stars #9 — Conformal Prediction](https://www.youtube.com/watch?v=BU4t1HPcOCg) — **Anastasios Angelopoulos, UC Berkeley (Alaa Lab channel)**. *The intuition for why one held-out quantile buys a distribution-free guarantee.*
5. **Run it on your own model** — work through [aangelopoulos/conformal-prediction](https://github.com/aangelopoulos/conformal-prediction) — **Anastasios Angelopoulos**. *Notebooks that wrap real ImageNet and regression models; the fastest path from theory to a prediction set.*

## Courses (free)

- [Conformal prediction notebooks and worked examples](https://github.com/aangelopoulos/conformal-prediction) — **Anastasios Angelopoulos (UC Berkeley)** — the companion "course" to the Gentle Introduction: split conformal, adaptive prediction sets, conformalized quantile regression, outlier detection, each as a runnable notebook.
- [Bayesian Deep Learning 101](https://www.cs.ox.ac.uk/people/yarin.gal/website/bdl101/) — **Yarin Gal (Oxford)** — the author's own teaching page for dropout-as-approximate-inference: slides, demos and the reading order.
- [MAPIE — Model Agnostic Prediction Interval Estimator](https://mapie.readthedocs.io/en/stable/) — **MAPIE maintainers (scikit-learn ecosystem)** — documentation that doubles as a tutorial: conformal regression, classification and time-series with scikit-learn-style estimators.

## Videos

- [Rising Stars #9 — Special Series on Conformal Prediction](https://www.youtube.com/watch?v=BU4t1HPcOCg) — **Anastasios Angelopoulos (Alaa Lab channel)** — the primary author walking through coverage, the calibration quantile, and where the guarantee stops holding.
- [Human-in-the-loop Bayesian Deep Learning (UNSURE 2020 keynote)](https://www.youtube.com/watch?v=GL6ZL1Aj9yw) — **Yarin Gal (UNSURE Workshop channel)** — epistemic uncertainty as the signal that decides what a human should look at next.

## Key Papers

- [A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification](https://arxiv.org/abs/2107.07511) — **Angelopoulos & Bates (2021)** — the canonical modern reference; split conformal, conformal risk control, and dozens of worked applications.
- [Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles](https://arxiv.org/abs/1612.01474) — **Lakshminarayanan, Pritzel & Blundell (2017)** — deep ensembles: the strongest simple baseline for both calibration and OOD detection.
- [Dropout as a Bayesian Approximation (MC dropout)](https://arxiv.org/abs/1506.02142) — **Gal & Ghahramani (2016)** — keeping dropout on at test time approximates a deep Gaussian process; the cheapest epistemic estimate available.
- [What Uncertainties Do We Need in Bayesian Deep Learning for Computer Vision?](https://arxiv.org/abs/1703.04977) — **Kendall & Gal (2017)** — the aleatoric/epistemic split made operational, with heteroscedastic loss functions.
- [Selective Classification for Deep Neural Networks](https://arxiv.org/abs/1705.08500) — **Geifman & El-Yaniv (2017)** — the risk–coverage curve: how to trade abstention rate against error rate with a guarantee.
- [Detecting hallucinations in large language models using semantic entropy](https://www.nature.com/articles/s41586-024-07421-0) — **Farquhar, Kossen, Kuhn & Gal (2024, Nature)** — clusters samples by meaning rather than tokens; the leading epistemic-uncertainty signal for LLMs.
- [Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation](https://arxiv.org/abs/2302.09664) — **Kuhn, Gal & Farquhar (2023)** — the ICLR paper the Nature result builds on; why token-level entropy is the wrong unit for text.
- [Conformal Language Modeling](https://arxiv.org/abs/2306.10193) — **Quach et al. (2023)** — conformal guarantees over *sets of generated sequences*; the bridge from classification-era conformal to LLMs.
- [Teaching Models to Express Their Uncertainty in Words](https://arxiv.org/abs/2205.14334) — **Lin, Hilton & Evans (2022)** — verbalized confidence, the format most production LLM systems actually use.

## Articles / Blogs (free, no paywall)

- [Uncertainty in Deep Learning (PhD thesis)](https://www.cs.ox.ac.uk/people/yarin.gal/website/blog_2248.html) — **Yarin Gal (Cambridge / Oxford)** — the thesis landing page with the free full text; the reference treatment of approximate Bayesian deep learning.
- [What My Deep Model Doesn't Know](https://www.cs.ox.ac.uk/people/yarin.gal/website/blog_3d801aa532c1ce.html) — **Yarin Gal** — the intuition post with interactive demos: where a network is confidently wrong and why.
- [awesome-conformal-prediction](https://github.com/valeman/awesome-conformal-prediction) — **Valeriy Manokhin** — the maintained index of conformal papers, libraries, tutorials and theses; use it to find the variant for your data type.

## Books (free, with chapters)

- [*Probabilistic Machine Learning: An Introduction* — Ch. 4 "Statistics" and Ch. 5 "Decision theory"](https://probml.github.io/pml-book/book1.html) — **Kevin Murphy** — free PDF; the frequentist and Bayesian scaffolding behind every method on this page.
- [*Uncertainty in Deep Learning*](https://www.cs.ox.ac.uk/people/yarin.gal/website/thesis/thesis.pdf) — **Yarin Gal (2016)** — free PDF thesis; Ch. 3 derives MC dropout from first principles.

## In this platform

- Prerequisites: [Calibration & Reliability Diagrams](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/calibration-and-reliability-diagrams/calibration-and-reliability-diagrams) · [Cross-Validation](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/cross-validation/cross-validation) (the exchangeable split conformal depends on) · [Bagging](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/trees-and-ensembles/bagging/bagging) (ensembles, the classical ancestor of deep ensembles)
- Next: [Error Analysis & Model Debugging](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/error-analysis-and-model-debugging/error-analysis-and-model-debugging) — what to do with the cases the model abstains on
- Applied to language models: [Hallucination & Grounding](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/hallucination-and-grounding/hallucination-and-grounding) · [LLM Evaluation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/llm-evaluation/llm-evaluation) · [Safety & Alignment](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/safety-and-alignment/safety-and-alignment)
- In production, rising epistemic uncertainty is an early drift alarm: [Data & Concept Drift Detection](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/data-and-concept-drift-detection/data-and-concept-drift-detection)
