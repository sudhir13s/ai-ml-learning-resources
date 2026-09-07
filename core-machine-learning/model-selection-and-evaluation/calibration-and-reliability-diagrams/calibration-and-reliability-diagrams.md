---
id: "core-machine-learning/model-selection-and-evaluation/calibration-and-reliability-diagrams"
topic: "Calibration & Reliability Diagrams"
level: intermediate
built_from: ["classification-metrics", "cross-validation", "bias-variance-tradeoff"]
leads_to: ["uncertainty-estimation-and-conformal-prediction", "error-analysis-and-model-debugging"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Calibration & Reliability Diagrams"
minutes: 14
category: model-selection-and-evaluation
---

# Calibration & Reliability Diagrams
> A model is **calibrated** when its confidence means what it says: of all the cases it scores
> 0.8, about 80% should actually be positive. Accuracy asks *was the argmax right*; calibration
> asks *was the number right* — and the two come apart badly in modern networks.
> The tools are the **reliability diagram** (a plot of confidence against observed accuracy) and
> **expected calibration error (ECE)** (the gap, averaged over bins).

**Why it matters:** every decision made *from a score* — a fraud threshold, a triage queue, a
router that escalates low-confidence cases to a human, an abstention policy on a large language
model (LLM) — is only as good as the score's meaning. Guo et al. showed that modern deep networks
are far **more overconfident** than the shallow models of the 1990s, and that a single-parameter
fix (**temperature scaling**) removes most of it. Interviews probe three things: why ECE is a
*binned, biased* estimator that can be gamed, why calibration must be fitted on a **held-out**
split and never on training data, and why a perfectly calibrated model can still be useless
(predicting the base rate for everyone is perfectly calibrated and has zero discrimination).

**Start here — suggested path:**

1. **See the failure** — read [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599) — **Guo, Pleiss, Sun & Weinberger (2017)**. *The reliability diagrams that started the modern literature, and temperature scaling as the one-parameter cure.*
2. **Get the vocabulary straight** — watch [Classifier Calibration Tutorial, Part 1: Calibration — What and Why](https://www.youtube.com/watch?v=4kwEMHZJx5A) — **Peter Flach & Miquel Perello Nieto (SAFE-AI channel)**. *Confidence, class-wise and canonical calibration defined precisely before any method.*
3. **Learn the metrics** — watch [Part 2: Evaluation metrics and proper scoring rules](https://www.youtube.com/watch?v=wO6waBBoT6k) — **Peter Flach & Miquel Perello Nieto (SAFE-AI channel)**. *Brier score and log loss decompose into calibration + refinement — this is why a proper scoring rule beats ECE alone.*
4. **Fit one yourself** — work through [Probability calibration](https://scikit-learn.org/stable/modules/calibration.html) — **scikit-learn**, then the [calibration-curve example](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html). *Platt scaling versus isotonic regression, on a held-out fold, in twenty lines.*
5. **Take it to 2026** — read [Uncertainty Quantification and Confidence Calibration in LLMs: A Survey](https://arxiv.org/abs/2503.15850) — **Shorinwa et al. (2025)**. *Where calibration goes when the output is a sequence, not a class: token probabilities, verbalized confidence, semantic consistency.*

## Courses (free)

- [Classifier Calibration Tutorial (ECML-PKDD 2020)](https://classifier-calibration.github.io/) — **Peter Flach & Miquel Perello Nieto, University of Bristol** — the only full course-length treatment of calibration; slides, notebooks and all five video parts, by the authors of the standard survey.
- [Google Machine Learning Crash Course — Thresholding and prediction bias](https://developers.google.com/machine-learning/crash-course/classification/thresholding) — **Google** — the shortest correct explanation of why a score is not a decision, and how thresholds interact with calibration.

## Videos

- [Classifier Calibration Tutorial, Part 1: Calibration — What and Why](https://www.youtube.com/watch?v=4kwEMHZJx5A) — **Peter Flach & Miquel Perello Nieto (SAFE-AI channel)** — the definitions (confidence, class-wise, canonical calibration) that most blog posts blur together.
- [Part 2: Evaluation metrics and proper scoring rules](https://www.youtube.com/watch?v=wO6waBBoT6k) — **Peter Flach & Miquel Perello Nieto (SAFE-AI channel)** — the calibration/refinement decomposition of the Brier score; why proper scoring rules are the honest measure.
- [Part 5: Advanced topics and conclusion](https://www.youtube.com/watch?v=xbMZHfToN7E) — **Peter Flach & Miquel Perello Nieto (SAFE-AI channel)** — multiclass calibration, calibration under dataset shift, and the open problems.

## Key Papers

- [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599) — **Guo, Pleiss, Sun & Weinberger (2017)** — the paper the whole field cites: depth and weight decay make networks overconfident; temperature scaling fixes most of it with one scalar.
- [Transforming Classifier Scores into Accurate Multiclass Probability Estimates](https://cseweb.ucsd.edu/~elkan/calibrated.pdf) — **Zadrozny & Elkan (2002)** — the origin of isotonic (non-parametric) calibration and of binning-based reliability estimates.
- [Verified Uncertainty Calibration](https://arxiv.org/abs/1909.10155) — **Kumar, Liang & Ma (2019)** — proves that the usual binned ECE *underestimates* true calibration error, and gives the scaling-binning estimator that does not.
- [Measuring Calibration in Deep Learning](https://arxiv.org/abs/1904.01685) — **Nixon et al. (2019)** — how binning scheme, bin count and norm change ECE by more than the method being compared; read before trusting any ECE table.
- [Revisiting the Calibration of Modern Neural Networks](https://arxiv.org/abs/2106.07998) — **Minderer et al. (2021, Google Brain)** — the 2017 verdict partly reversed: recent architectures (vision transformers, MLP-Mixer) are better calibrated *and* more accurate.
- [Classifier Calibration: A Survey on How to Assess and Improve Predicted Class Probabilities](https://arxiv.org/abs/2112.10327) — **Silva Filho, Song, Perello-Nieto, Santos-Rodriguez, Kull & Flach (2021)** — the reference survey: taxonomy, metrics, and every post-hoc method in one place.
- [Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221) — **Kadavath et al. (2022, Anthropic)** — LLM self-evaluation is surprisingly well calibrated on multiple-choice, and degrades on open-ended generation.
- [Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey](https://arxiv.org/abs/2503.15850) — **Shorinwa, Mei, Lidard, Ren & Majumdar (2025)** — the current map of LLM calibration: token-level, verbalized, and consistency-based confidence.

## Articles / Blogs (free, no paywall)

- [Probability calibration — scikit-learn user guide](https://scikit-learn.org/stable/modules/calibration.html) — **scikit-learn maintainers** — sigmoid (Platt) versus isotonic, `CalibratedClassifierCV`, and the cross-validated fitting protocol that avoids leaking.
- [Comparison of calibration of classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html) — **scikit-learn maintainers** — runnable reliability diagrams for logistic regression, naive Bayes, random forest and a linear support-vector classifier side by side.
- [Temperature scaling reference implementation](https://github.com/gpleiss/temperature_scaling) — **Geoff Pleiss (paper co-author)** — sixty lines of PyTorch that wrap a trained network and learn one temperature on the validation set.
- [Calibration in Deep Learning: A Survey of the State-of-the-Art](https://arxiv.org/abs/2308.01222) — **Wang (2023)** — free survey covering train-time (label smoothing, focal loss) versus post-hoc calibration, and calibration under distribution shift.

## Books (free, with chapters)

- [*Probabilistic Machine Learning: An Introduction* — Ch. 5 "Decision theory"](https://probml.github.io/pml-book/book1.html) — **Kevin Murphy** — free PDF; proper scoring rules and why the Brier score and log loss are the principled objectives behind calibration.

## In this platform

- Prerequisites: [Classification Metrics](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/classification/classification-metrics/classification-metrics) (a calibrated score still needs a threshold) · [Cross-Validation](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/cross-validation/cross-validation) (calibration is fitted on held-out folds, never on training data)
- Next: [Uncertainty Estimation & Conformal Prediction](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/uncertainty-estimation-and-conformal-prediction/uncertainty-estimation-and-conformal-prediction) — when a calibrated point score is not enough and you want a guaranteed set
- Downstream: [Error Analysis & Model Debugging](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/error-analysis-and-model-debugging/error-analysis-and-model-debugging) · [LLM Evaluation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/llm-evaluation/llm-evaluation) · [Hallucination & Grounding](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/hallucination-and-grounding/hallucination-and-grounding)
- In production, miscalibration shows up as drift: [Model Monitoring & Observability](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability)
