---
id: "02-data-preprocessing/imbalanced-data"
topic: "Imbalanced Data (resampling · SMOTE · class weights)"
parent: "02-data-preprocessing"
level: intermediate
built_from: ["classification-metrics", "train-test-split"]
interview_frequency: very-high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Imbalanced Data (resampling · SMOTE · class weights)"
minutes: 10
category: data-preparation
---

# Imbalanced Data
> When one class vastly outnumbers another (fraud, disease, churn) — handled via resampling
> (under/oversampling, SMOTE), class weights, or threshold tuning — and evaluated with metrics that
> don't reward predicting the majority class.

**Why it matters:** with 99% negatives, a model that predicts "negative" always scores 99% accuracy and is
useless — so this topic tests whether you know to use precision/recall/F1/PR-AUC instead, and the three
families of fixes: **resampling** (SMOTE, random under/over), **algorithmic** (class_weight='balanced',
scale_pos_weight), and **threshold tuning**. The classic trap: SMOTE must be applied **inside CV, on
training folds only** — never before the split.

**Start here — suggested path:**

1. **Frame the problem** — watch [The Confusion Matrix](https://www.youtube.com/watch?v=Kdsp6soqA7o) — **StatQuest**. *Why 99% accuracy on a 1% positive class is worthless, stated in counts rather than slogans.*
2. **Resampling in practice** — read the [imbalanced-learn user guide](https://imbalanced-learn.org/stable/user_guide.html). *Under- and over-sampling with a pipeline-safe API that resamples training folds only.*
3. **SMOTE** — read the [SMOTE paper](https://arxiv.org/abs/1106.1813) — **Chawla et al.**, then [imbalanced-learn: over-sampling](https://imbalanced-learn.org/stable/over_sampling.html). *How synthetic minority points are interpolated, and where Borderline-SMOTE and ADASYN differ.*
4. **Weights instead of resampling** — read [Google ML Crash Course — Imbalanced data](https://developers.google.com/machine-learning/crash-course/overfitting/imbalanced-datasets). *Downsampling with upweighting, and why `class_weight="balanced"` is often the simpler, better first move.*
5. **Use the right metrics** — read [ROC vs PR curves (sklearn)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html). *Why PR-AUC beats ROC-AUC under heavy imbalance.*

## Courses (free)
- [imbalanced-learn — User Guide](https://imbalanced-learn.org/stable/user_guide.html) — **imbalanced-learn** — the canonical library's guide to every resampling method.
- [Google ML Crash Course — Imbalanced data](https://developers.google.com/machine-learning/crash-course/overfitting/imbalanced-datasets) — **Google** — downsampling + upweighting, applied.

## Videos
- [ROC and AUC, Clearly Explained!](https://www.youtube.com/watch?v=4jRBRDbJemM) — **StatQuest with Josh Starmer** — the curve everyone quotes under imbalance, and exactly what it does and does not measure when the negative class dominates.
- [Machine Learning Fundamentals: The Confusion Matrix](https://www.youtube.com/watch?v=Kdsp6soqA7o) — **StatQuest with Josh Starmer** — precision, recall and specificity from the counts, which is where "accuracy lies" becomes concrete.
- [Machine Learning Fundamentals: Cross Validation](https://www.youtube.com/watch?v=fSytzGwwBVw) — **StatQuest with Josh Starmer** — the loop resampling must live inside; oversampling before the split is the classic silent leak.

## Key Papers
- [SMOTE: Synthetic Minority Over-sampling Technique](https://arxiv.org/abs/1106.1813) — **Chawla et al. (2002)** — the original SMOTE paper (JAIR), free on arXiv; the method every interview references.
- [Learning from Imbalanced Data](https://www.jair.org/index.php/jair/article/view/10302) — **He & Garcia (2009)** — the definitive survey of imbalance methods and metrics; free in JAIR.

## Articles / Blogs (free, no paywall)
- [imbalanced-learn — Over-sampling](https://imbalanced-learn.org/stable/over_sampling.html) — **imbalanced-learn** — SMOTE variants (Borderline, ADASYN) with API + intuition.
- [Precision-Recall (sklearn example)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html) — **scikit-learn** — the right evaluation curve under imbalance.
- [imbalanced-learn — Combining over- and under-sampling](https://imbalanced-learn.org/stable/combine.html) — **imbalanced-learn** — SMOTEENN/SMOTETomek and pipeline-safe usage.

## Books (free, with chapters)
- [Feature Engineering and Selection — **Ch. 3 "Review of Key Concepts" (class imbalance, metrics)**](http://www.feat.engineering/) — **Kuhn & Johnson** — imbalance + metric pitfalls in context; free online.
- [An Introduction to Statistical Learning (Python) — **Ch. 4 "Classification"**](https://www.statlearning.com/) — **James et al.** — thresholds, confusion matrices, and why accuracy misleads; free PDF.

## In this platform
- Concept depth (the *why*): [ai-ml-intuitions 3.05 Precision, Recall, F1](/ai-ml/ai-ml-intuitions/objectives-and-evaluation/predictive-evaluation/classification-metrics-intuition) · [3.06 ROC/AUC & PR Curves](/ai-ml/ai-ml-intuitions/objectives-and-evaluation/predictive-evaluation/roc-and-pr-curves-intuition)
- Next concepts: [10 Train/Validation/Test Splits](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/train-validation-test-splits/train-validation-test-splits) · [11 Data Leakage](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/data-leakage/data-leakage)
- Related domain: [03. Supervised Learning](/ai-ml/ai-ml-learning-resources/classical-machine-learning/supervised-learning/readme)
