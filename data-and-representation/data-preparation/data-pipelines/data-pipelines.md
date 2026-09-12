---
id: "02-data-preprocessing/data-pipelines"
topic: "Data Pipelines (sklearn Pipeline · ColumnTransformer)"
parent: "02-data-preprocessing"
level: intermediate
built_from: ["scaling", "encoding", "imputation", "cross-validation"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Data Pipelines (sklearn Pipeline · ColumnTransformer)"
minutes: 10
category: data-preparation
---

# Data Pipelines (sklearn Pipeline · ColumnTransformer)
> Chaining every preprocessing step + the model into one fit/transform object — so the exact same
> transforms (fit on train) apply to validation, test, and production, and nothing leaks across the split.

**Why it matters:** pipelines are how you make preprocessing **correct and reproducible**. Fitting a scaler
or imputer on the whole dataset is the #1 cause of leakage; a `Pipeline` + `ColumnTransformer` fits all
transforms on training folds only, applies them consistently everywhere, and serializes cleanly for
deployment. Interviewers love this because it ties together scaling, encoding, imputation, CV, and leakage
into one production-grade pattern.

**Start here — suggested path:**

1. **Why pipelines** — watch [Understanding Pipeline in scikit-learn](https://www.youtube.com/watch?v=jzKSAeJpC6s). *What problem they solve, and how `fit` and `predict` flow through the steps.*
2. **Different columns, different transforms** — read the [ColumnTransformer mixed-types example](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html). *Numeric columns scaled, categorical columns encoded, in one estimator.*
3. **Build one end to end** — work [Kaggle Learn — Pipelines](https://www.kaggle.com/code/alexisbcook/pipelines). *Preprocessing, model and cross-validation assembled into a single object you can tune.*
4. **Read the reference** — read [sklearn: Pipelines & composite estimators](https://scikit-learn.org/stable/modules/compose.html). *Pipeline, ColumnTransformer, FeatureUnion, get_feature_names_out.*
5. **Lock in leakage-safety** — read [sklearn: Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html). *Why pipelines + CV are the structural fix for leakage.*

## Courses (free)
- [Kaggle Learn — Intermediate ML (Pipelines)](https://www.kaggle.com/code/alexisbcook/pipelines) — **Kaggle** — the best free hands-on pipelines lesson.
- [Kaggle Learn — Feature Engineering](https://www.kaggle.com/learn/feature-engineering) — **Kaggle** — where pipelines tie preprocessing + features together.

## Videos
- [probabl (scikit-learn maintainers' channel)](https://www.youtube.com/@probabl_ai) — **probabl / scikit-learn core developers** — `Pipeline`, `ColumnTransformer` and `set_output` demonstrated by the people who maintain them.
- [Understanding Pipeline in scikit-learn](https://www.youtube.com/watch?v=jzKSAeJpC6s) — **Dr. Data Science** — fit and transform semantics, and why a pipeline is what actually prevents leakage.
- [Machine Learning Fundamentals: Cross Validation](https://www.youtube.com/watch?v=fSytzGwwBVw) — **StatQuest with Josh Starmer** — the other half of the pattern: the pipeline is only leakage-safe because cross-validation refits it per fold.

## Key Papers
- [Scikit-learn: Machine Learning in Python](https://www.jmlr.org/papers/volume12/pedregosa11a/pedregosa11a.pdf) — **Pedregosa et al. (2011)** — the JMLR paper introducing the fit/transform/Pipeline API design; free.
- [API design for machine learning software: experiences from the scikit-learn project](https://arxiv.org/abs/1309.0238) — **Buitinck et al. (2013)** — the design philosophy behind estimators, transformers, and pipelines; free on arXiv.

## Articles / Blogs (free, no paywall)
- [Pipelines and composite estimators — user guide](https://scikit-learn.org/stable/modules/compose.html) — **scikit-learn** — the authoritative reference for Pipeline + ColumnTransformer.
- [ColumnTransformer for heterogeneous data](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html) — **scikit-learn** — a complete mixed numeric/categorical example.
- [Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html) — **scikit-learn** — why pipelines + CV are the leakage-safe pattern.

## Books (free, with chapters)
- [Python Data Science Handbook — **§5.4 "Feature Engineering" (Pipelines)**](https://jakevdp.github.io/PythonDataScienceHandbook/05.04-feature-engineering.html) — **Jake VanderPlas** — building processing pipelines with sklearn.
- [Tidy Modeling with R — **Ch. 8 "Feature Engineering with recipes"**](https://www.tmwr.org/) — **Kuhn & Silge** — the recipes/workflow pattern (the R analogue of Pipeline); concepts transfer; free.

## In this platform
- Builds on: [02 Feature Scaling](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/feature-scaling-and-normalization/feature-scaling-and-normalization) · [03 Encoding Categoricals](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/encoding-categorical-variables/encoding-categorical-variables) · [04 Missing Data Imputation](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/missing-data-imputation/missing-data-imputation)
- Prevents: [11 Data Leakage](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/data-leakage/data-leakage) — pipelines are the structural fix.
- Related domain: [12. Deployment & MLOps](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/readme) — where pipelines become serving-time feature transforms.
