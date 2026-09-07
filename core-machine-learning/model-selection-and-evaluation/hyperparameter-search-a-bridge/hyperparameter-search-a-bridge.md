---
id: "core-machine-learning/model-selection-and-evaluation/hyperparameter-search-a-bridge"
topic: "Hyperparameter Search — a bridge"
level: beginner
built_from: ["cross-validation", "bias-variance-tradeoff"]
leads_to: ["calibration-and-reliability-diagrams"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Hyperparameter Search — a bridge"
minutes: 10
category: model-selection-and-evaluation
---

# Hyperparameter Search — a bridge
> Cross-validation tells you how good *one* configuration is; hyperparameter search is the loop
> that runs it over *many* and picks a winner. This is a short bridge for the classical-ML setting
> — the full derivation lives on the owner page linked below, and this page does not repeat it.

**Why it matters:** for scikit-learn-scale models the choice is usually cheap and mechanical, and
the interview question is narrow — *why is random search better than grid search?* Answer: only a
few hyperparameters matter, and for a fixed budget random search samples many distinct values of
the important one while grid search samples only a few. **Everything else on this topic — the
budget math, Bayesian optimization, Hyperband, the leak-free protocol — is taught in full on the
deep-learning page linked below.**

**The four families, one line each:**

- **Grid search** — every combination on a fixed lattice; interpretable, exponential in the knobs.
- **Random search** — sample from per-parameter distributions (log-uniform for scale parameters like `C`, `alpha`, `learning_rate`); strictly better than grid at equal budget.
- **Bayesian optimization** — fit a surrogate to past trials and probe where expected improvement is highest; worth it once one trial costs minutes.
- **Hyperband / successive halving** — start many configurations cheaply, kill the losers early, reinvest in survivors; the default when a trial can be stopped part-way.

**Two rules that decide whether the result is real:** search **inside** the cross-validation loop (a
scaler fitted on the full data leaks the folds), and report the winner on data the search never
touched — nested cross-validation, or a test set opened exactly once.

**Start here — suggested path:**

1. **Read the argument** — [Random Search for Hyper-Parameter Optimization](https://jmlr.org/papers/v13/bergstra12a.html) — **Bergstra & Bengio (2012)**. *The source of the grid-versus-random answer.*
2. **Wire it up** — [Tuning the hyper-parameters of an estimator](https://scikit-learn.org/stable/modules/grid_search.html) — **scikit-learn maintainers**. *Leak-free pipelines and successive halving in practice.*
3. **Go deep** — the platform's owner page below. *Budget math, Bayesian optimization, Hyperband and population-based training, derived in full.*

## Key Papers

- [Random Search for Hyper-Parameter Optimization](https://jmlr.org/papers/v13/bergstra12a.html) — **Bergstra & Bengio (2012, JMLR)** — the canonical grid-versus-random result and the interview answer's source.
- [Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization](https://arxiv.org/abs/1603.06560) — **Li, Jamieson, DeSalvo, Rostamizadeh & Talwalkar (2017)** — early stopping as a budget-allocation problem.

## Articles / Blogs (free, no paywall)

- [Tuning the hyper-parameters of an estimator](https://scikit-learn.org/stable/modules/grid_search.html) — **scikit-learn maintainers** — `GridSearchCV`, `RandomizedSearchCV`, `HalvingRandomSearchCV` and the pipeline pattern that prevents leakage.
- [Optuna documentation](https://optuna.readthedocs.io/en/stable/) — **Optuna maintainers (Preferred Networks)** — define-by-run search spaces, the tree-structured Parzen estimator sampler and pruning, for anything past a laptop-sized sweep.

## In this platform

- **Owner page (read this for the full treatment):** [Hyperparameter Tuning](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/hyperparameter-tuning/hyperparameter-tuning) — the budget math, Bayesian optimization, Hyperband, BOHB, population-based training and the leak-free protocol, derived in full.
- Prerequisites: [Cross-Validation](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/cross-validation/cross-validation) (the estimator every search optimizes) · [Bias–Variance Tradeoff](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/bias-variance-tradeoff/bias-variance-tradeoff) (what the knobs are trading).
- After you pick a winner: [Calibration & Reliability Diagrams](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/calibration-and-reliability-diagrams/calibration-and-reliability-diagrams).
