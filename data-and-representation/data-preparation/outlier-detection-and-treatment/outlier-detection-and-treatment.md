---
id: "02-data-preprocessing/outliers"
topic: "Outlier Detection & Treatment"
parent: "02-data-preprocessing"
level: beginner
built_from: ["mean-std", "quartiles-iqr", "gaussian"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Outlier Detection & Treatment"
minutes: 10
category: data-preparation
---

# Outlier Detection & Treatment
> Finding the points that don't fit — via Z-score, IQR, or percentiles — then deciding whether to keep,
> cap (winsorize), transform, or drop them, depending on whether they're errors or genuine extremes.

**Why it matters:** outliers wreck mean-based statistics, distort scaling, and skew linear models — but
blindly deleting them throws away signal (fraud, anomalies, the very thing you may want to detect). Expect
to compare Z-score vs IQR vs percentile rules, explain why median/IQR are robust while mean/std aren't, and
justify capping vs removal vs a log transform — and to do detection **using training-set statistics only**.

**Start here — suggested path:**

1. **See one before naming it** — watch [Boxplots are Awesome](https://www.youtube.com/watch?v=fHLhBnmwUM0) — **StatQuest**. *The fence, the whiskers, and what a point outside them actually claims.*
2. **The parametric rule and its assumption** — read [NIST — Detection of Outliers](https://www.itl.nist.gov/div898/handbook/prc/section1/prc16.htm). *The ±3σ and Grubbs tests, together with the normality they quietly require.*
3. **The robust alternative** — read [Google ML Crash Course — Numerical data](https://developers.google.com/machine-learning/crash-course/numerical-data). *Clipping, log scaling and bucketing: treating the extreme value instead of deleting the row.*
4. **Multivariate outliers** — read [sklearn: Novelty and outlier detection](https://scikit-learn.org/stable/modules/outlier_detection.html). *A row can be unremarkable in every column and still be an outlier jointly; Isolation Forest and Local Outlier Factor are what find it.*
5. **Reference detectors** — read [sklearn: Novelty & outlier detection](https://scikit-learn.org/stable/modules/outlier_detection.html). *Isolation Forest, LOF, Elliptic Envelope for multivariate outliers.*

## Courses (free)
- [Kaggle Learn — Data Cleaning](https://www.kaggle.com/learn/data-cleaning) — **Kaggle** — practical lessons touching outliers and inconsistent values.
- [Google ML Crash Course — Numerical data](https://developers.google.com/machine-learning/crash-course/numerical-data) — **Google** — handling outliers via clipping, log scaling, and bucketing.

## Videos
- [Boxplots are Awesome](https://www.youtube.com/watch?v=fHLhBnmwUM0) — **StatQuest with Josh Starmer** — where the 1.5×IQR fence comes from and what the points beyond it do and do not mean.
- [StatQuest: Histograms, Clearly Explained](https://www.youtube.com/watch?v=qBigTkBLU6g) — **StatQuest with Josh Starmer** — seeing a heavy tail before you decide it is an error to remove.
- [Exploratory Data Analysis with Pandas](https://www.youtube.com/watch?v=xi0vhXFPegw) — **Rob Mulla** — outliers found the way practitioners find them: sorting, describing, and plotting the columns.

## Key Papers
- [Isolation Forest](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf) — **Liu, Ting & Zhou (2008)** — isolates anomalies via random partitioning; the standard scalable outlier detector.
- [Deep Learning for Anomaly Detection: A Review](https://arxiv.org/abs/2007.02500) — **Pang et al. (2020)** — survey of modern outlier/anomaly methods; free on arXiv.

## Articles / Blogs (free, no paywall)
- [Novelty and Outlier Detection — user guide](https://scikit-learn.org/stable/modules/outlier_detection.html) — **scikit-learn** — Isolation Forest, Local Outlier Factor, and Elliptic Envelope explained.
- [NIST/SEMATECH e-Handbook — Detection of Outliers](https://www.itl.nist.gov/div898/handbook/prc/section1/prc16.htm) — **NIST** — Grubbs', Tietjen-Moore, and boxplot rules, free and rigorous.
- [Forecasting: Principles and Practice — Missing values & outliers](https://otexts.com/fpp3/missing-outliers.html) — **Hyndman & Athanasopoulos** — outlier handling in a time-series context.

## Books (free, with chapters)
- [Feature Engineering and Selection — **Ch. 6 "Engineering Numeric Predictors" (transformations)**](http://www.feat.engineering/) — **Kuhn & Johnson** — transforms that tame skew and extremes; free online.
- [Python Data Science Handbook — **Ch. 3 (Pandas: detecting/filtering)**](https://jakevdp.github.io/PythonDataScienceHandbook/) — **Jake VanderPlas** — boolean masking and aggregation to find/remove outliers.

## In this platform
- Concept depth (the *why*): [ai-ml-intuitions 0.02 Distributions & the Gaussian](/ai-ml/ai-ml-intuitions/foundational-mental-models/probability-and-belief/distributions-and-gaussians-intuition) · [1.10 Mahalanobis Distance](/ai-ml/ai-ml-intuitions/representation/similarity-and-distance/mahalanobis-distance-intuition)
- Next concepts: [02 Feature Scaling & Normalization](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/feature-scaling-and-normalization/feature-scaling-and-normalization) · [06 Feature Engineering](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/feature-engineering/feature-engineering)
- Related domain: [04. Unsupervised Learning](/ai-ml/ai-ml-learning-resources/classical-machine-learning/unsupervised-learning/readme)
