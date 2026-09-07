---
id: "core-machine-learning/model-selection-and-evaluation"
topic: "Model Selection and Evaluation"
level: intermediate
built_from: ["ai-ml-orientation", "supervised-learning"]
updated: 2026-09-07
---

# Model Selection and Evaluation

> The half of machine learning that decides whether the other half was worth anything. This
> sub-area covers where error comes from, how to estimate generalization honestly, how to search
> for a configuration without fooling yourself, whether a predicted probability means what it
> says, how to quantify what the model does not know, and how to read the mistakes rather than
> the average. It is the most interviewed material in classical ML.

**Start here:** [Bias-Variance Tradeoff](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/bias-variance-tradeoff/bias-variance-tradeoff) for where error comes from, then [Cross-Validation](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/cross-validation/cross-validation) for how to measure it without leaking the answer.

## Concept index

Each page is a self-contained resource card: a plain-words definition, why it matters in 2026, a
five-step start-here path, and verified courses, videos, papers, articles and books.

### Where error comes from, and how to measure it

1. [Bias-Variance Tradeoff](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/bias-variance-tradeoff/bias-variance-tradeoff) — the decomposition of expected error into bias, variance and irreducible noise, and the U-curve it produces.
2. [Cross-Validation](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/cross-validation/cross-validation) — k-fold, stratified, grouped and time-series splits; why the final test set stays untouched.
3. [Hyperparameter Search — a bridge](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/hyperparameter-search-a-bridge/hyperparameter-search-a-bridge) — the loop that runs cross-validation over many configurations, in the classical-ML setting.

### Is the number believable?

4. [Calibration and Reliability Diagrams](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/calibration-and-reliability-diagrams/calibration-and-reliability-diagrams) — whether a score of 0.8 really means 80%; reliability diagrams, expected calibration error (ECE), temperature scaling.
5. [Uncertainty Estimation and Conformal Prediction](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/uncertainty-estimation-and-conformal-prediction/uncertainty-estimation-and-conformal-prediction) — aleatoric versus epistemic uncertainty, deep ensembles, and prediction sets with a finite-sample coverage guarantee.

### Reading the failures

6. [Error Analysis and Model Debugging](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/error-analysis-and-model-debugging/error-analysis-and-model-debugging) — sample the mistakes, tag them, count the tags; plus the systematic search for why training itself misbehaves.

## Courses (free)

- [CS229: Machine Learning — lecture notes](https://cs229.stanford.edu/main_notes.pdf) — **Stanford (Andrew Ng)** — the rigorous treatment of bias, variance, model selection and generalization, free as a PDF.
- [Introduction to Data-Centric AI](https://dcai.csail.mit.edu/) — **MIT CSAIL (Northcutt, Mueller, Athalye)** — the only university course dedicated to fixing the dataset rather than the model; label noise, outliers, slice discovery.
- [Classifier Calibration Tutorial](https://classifier-calibration.github.io/) — **Peter Flach and Miquel Perello Nieto, University of Bristol** — the one course-length treatment of calibration, with slides and recorded parts.
- [Conformal prediction notebooks and worked examples](https://github.com/aangelopoulos/conformal-prediction) — **Anastasios Angelopoulos (UC Berkeley)** — split conformal, conformal risk control and coverage, all runnable, from a primary author.

## Videos

- [Classifier Calibration Tutorial, Part 1: Calibration — What and Why](https://www.youtube.com/watch?v=4kwEMHZJx5A) — **Peter Flach and Miquel Perello Nieto** — the definitions (confidence, class-wise, canonical calibration) stated precisely before any method.
- [MIT Data-Centric AI, Lecture 1: Data-Centric AI vs. Model-Centric AI](https://www.youtube.com/watch?v=ayzOzZGHZy4) — **MIT (Introduction to Data-Centric AI)** — why the measurement problem is usually a data problem.
- [Rising Stars #9 — Special Series on Conformal Prediction](https://www.youtube.com/watch?v=BU4t1HPcOCg) — **Anastasios Angelopoulos** — the primary author walking through coverage and the calibration/test split.
- [Human-in-the-loop Bayesian Deep Learning](https://www.youtube.com/watch?v=GL6ZL1Aj9yw) — **Yarin Gal (UNSURE keynote)** — epistemic uncertainty framed as the signal that decides what a human should look at.

## Key Papers

- [Random Search for Hyper-Parameter Optimization](https://jmlr.org/papers/v13/bergstra12a.html) — **Bergstra and Bengio (JMLR, 2012)** — the canonical grid-versus-random result, and the source of the standard interview answer.
- [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599) — **Guo, Pleiss, Sun and Weinberger (2017)** — the paper the whole field cites: modern networks are accurate and badly overconfident, and one temperature fixes most of it.
- [A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification](https://arxiv.org/abs/2107.07511) — **Angelopoulos and Bates (2021)** — the modern reference for distribution-free prediction sets.
- [Beyond Accuracy: Behavioral Testing of NLP Models with CheckList](https://arxiv.org/abs/2005.14118) — **Ribeiro, Wu, Guestrin and Singh (ACL 2020, best paper)** — minimum-functionality, invariance and directional tests; error analysis made into a test suite.
- [No Subclass Left Behind](https://arxiv.org/abs/2011.12945) — **Sohoni, Dunnmon, Angus, Gu and Ré (2020)** — hidden stratification: why a strong aggregate score can hide a catastrophic slice.

## Articles / Blogs (free, no paywall)

- [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/) — **Andrej Karpathy** — the most useful debugging document in deep learning; the discipline behind page 6.
- [MLU-Explain](https://mlu-explain.github.io/) — **Amazon Machine Learning University (Jared Wilber and colleagues)** — interactive visual essays on cross-validation, bias-variance and the ROC curve.
- [Probability calibration](https://scikit-learn.org/stable/modules/calibration.html) — **scikit-learn maintainers** — Platt scaling versus isotonic regression, `CalibratedClassifierCV`, and the cross-validation trap inside it.
- [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml) — **Martin Zinkevich (Google)** — 43 rules; 14 to 29 read as a checklist for diagnosing a model that underperforms in production.

## Books (free, with chapters)

- [*The Elements of Statistical Learning* — §7.3 "The Bias-Variance Decomposition"](https://hastie.su.domains/ElemStatLearn/) — **Hastie, Tibshirani and Friedman** — free PDF; the rigorous derivation and the whole model-assessment chapter.
- [*An Introduction to Statistical Learning* — Ch. 5 "Resampling Methods"](https://www.statlearning.com/) — **James, Witten, Hastie and Tibshirani** — free PDF; cross-validation and the bootstrap at an applied level, with labs.
- [*Machine Learning Yearning*](https://info.deeplearning.ai/machine-learning-yearning-book) — **Andrew Ng** — free book; Ch. 13 to 19 remain the definitive short treatment of error analysis and eyeball versus blackbox dev sets.
- [*Probabilistic Machine Learning: An Introduction* — Ch. 5 "Decision theory"](https://probml.github.io/pml-book/book1.html) — **Kevin Murphy** — free PDF; proper scoring rules, and why Brier score and log loss are the principled objectives.

## In this platform

- Section index: [Core Machine Learning](/ai-ml/ai-ml-learning-resources/core-machine-learning/readme)
- What is being evaluated: [Supervised Learning](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/readme) · [Unsupervised Learning](/ai-ml/ai-ml-learning-resources/core-machine-learning/unsupervised-learning/readme) · [Reinforcement Learning](/ai-ml/ai-ml-learning-resources/core-machine-learning/reinforcement-learning/readme)
- The first statement of these ideas: [Overfitting and Underfitting](/ai-ml/ai-ml-learning-resources/foundations/ai-ml-orientation/overfitting-and-underfitting/overfitting-and-underfitting)
- Where evaluation continues in the deep-learning and LLM eras: [Hyperparameter Tuning](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/hyperparameter-tuning/hyperparameter-tuning) · [LLM Evaluation and Benchmarks](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/llm-evaluation/llm-evaluation)
- What happens to these metrics after deployment: [Model Monitoring and Observability](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability) · [Data and Concept Drift Detection](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/data-and-concept-drift-detection/data-and-concept-drift-detection)
- The mental models: [Bias-Variance Tradeoff](/ai-ml/ai-ml-intuitions/objectives-and-evaluation/generalization/bias-variance-tradeoff-intuition) · [ROC and PR Curves](/ai-ml/ai-ml-intuitions/objectives-and-evaluation/predictive-evaluation/roc-and-pr-curves-intuition) · [Classification Metrics](/ai-ml/ai-ml-intuitions/objectives-and-evaluation/predictive-evaluation/classification-metrics-intuition)
- Doing it rather than reading it: [Evaluation and Benchmarking workflow](/ai-ml/practitioner-workflows/evaluation-safety-and-reliability/evaluation-and-benchmarking)
