---
id: "02-data-preprocessing/missing-data"
topic: "Missing Data Imputation"
parent: "02-data-preprocessing"
level: beginner
built_from: ["pandas", "mean-median-mode", "knn"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Missing Data Imputation"
minutes: 10
category: data-preparation
---

# Missing Data Imputation
> Filling in (or flagging) missing values — mean/median/mode, KNN, or model-based MICE — while
> respecting *why* the data is missing (MCAR/MAR/MNAR) and never leaking statistics from test into train.

**Why it matters:** real datasets are full of holes, and how you fill them changes results. Interviewers
probe the missingness mechanisms (MCAR vs MAR vs MNAR), why median beats mean under skew, when a
**missing-indicator** column is worth adding, why KNN/MICE can beat simple imputation, and the cardinal
rule: **fit the imputer on training data only** (compute fill values from train, apply to test).

**Start here — suggested path:**

1. **Name the mechanism first** — read [Flexible Imputation of Missing Data, Ch. 1–2](https://stefvanbuuren.name/fimd/) — **Stef van Buuren**. *MCAR, MAR and MNAR decide which methods are even valid; every later choice follows from this.*
2. **Simple imputation, done safely** — read [sklearn: Imputation of missing values](https://scikit-learn.org/stable/modules/impute.html) and use `SimpleImputer` inside a `Pipeline`. *Mean and median fills, plus the train-only fit rule the pipeline enforces for you.*
3. **Multivariate imputation** — watch [StatQuest: K-nearest neighbors](https://www.youtube.com/watch?v=HVXime0nQeI), then use `KNNImputer`. *Filling from similar rows, once you know what "similar" means.*
4. **Model-based** — read the [MICE paper](https://www.jstatsoft.org/article/view/v045i03) — **van Buuren & Groothuis-Oudshoorn**, and use `IterativeImputer`. *Chained-equations imputation, the reference method for MAR data.*
5. **Reference the API** — read [sklearn: Imputation of missing values](https://scikit-learn.org/stable/modules/impute.html). *SimpleImputer, KNNImputer, IterativeImputer, MissingIndicator.*

## Courses (free)
- [Kaggle Learn — Data Cleaning (Handling Missing Values)](https://www.kaggle.com/learn/data-cleaning) — **Kaggle** — short, hands-on lesson dedicated to missing data.
- [Google ML Crash Course — Numerical data](https://developers.google.com/machine-learning/crash-course/numerical-data) — **Google** — covers handling missing/anomalous numeric values.

## Videos
- [StatQuest: K-nearest neighbors, Clearly Explained](https://www.youtube.com/watch?v=HVXime0nQeI) — **StatQuest with Josh Starmer** — the mechanism `KNNImputer` runs on: which rows count as "similar", and what the choice of *k* does.
- [Exploratory Data Analysis with Pandas](https://www.youtube.com/watch?v=xi0vhXFPegw) — **Rob Mulla** — finding and characterising the missingness before you decide how to fill it; imputation starts as a diagnosis.
- [Machine Learning Fundamentals: Cross Validation](https://www.youtube.com/watch?v=fSytzGwwBVw) — **StatQuest with Josh Starmer** — why the imputer must be fitted inside the cross-validation loop, not before it.

## Key Papers
- [mice: Multivariate Imputation by Chained Equations in R](https://www.jstatsoft.org/article/view/v045i03) — **van Buuren & Groothuis-Oudshoorn (2011)** — the standard reference for MICE; free in JSS.
- [Missing-data imputation using machine learning: A review](https://arxiv.org/abs/2106.04619) — **survey** — modern overview of imputation methods and when each wins; free on arXiv.

## Articles / Blogs (free, no paywall)
- [Imputation of missing values — user guide](https://scikit-learn.org/stable/modules/impute.html) — **scikit-learn** — authoritative reference for SimpleImputer/KNNImputer/IterativeImputer.
- [Flexible Imputation of Missing Data (online book)](https://stefvanbuuren.name/fimd/) — **Stef van Buuren** — the definitive open text on missing-data theory + MICE.
- [pandas — Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html) — **pandas docs** — detection (`isna`), dropping, and filling at the dataframe level.

## Books (free, with chapters)
- [Flexible Imputation of Missing Data — **Ch. 1–4 (mechanisms, simple & multiple imputation)**](https://stefvanbuuren.name/fimd/) — **Stef van Buuren** — MCAR/MAR/MNAR and MICE, free online.
- [Feature Engineering and Selection — **Ch. 8 "Handling Missing Data"**](http://www.feat.engineering/) — **Kuhn & Johnson** — applied imputation in a modeling workflow; free online.

## In this platform
- Concept depth (the *why*): [ai-ml-intuitions 0.01 Probability & Bayes](/ai-ml/ai-ml-intuitions/foundational-mental-models/probability-and-belief/probability-and-bayes-intuition) · [0.03 Expectation, Variance, Covariance](/ai-ml/ai-ml-intuitions/foundational-mental-models/probability-and-belief/expectation-variance-and-covariance-intuition)
- Next concepts: [05 Outlier Detection & Treatment](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/outlier-detection-and-treatment/outlier-detection-and-treatment) · [13 Data Pipelines](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/data-pipelines/data-pipelines)
- Related domain: [03. Supervised Learning](/ai-ml/ai-ml-learning-resources/classical-machine-learning/supervised-learning/readme)
