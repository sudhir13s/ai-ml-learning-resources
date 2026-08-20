---
id: "03-supervised-learning"
topic: "Supervised Learning"
level: intermediate
built_from: ["foundations", "data-preprocessing"]
updated: 2026-06-27
---

# Supervised Learning
> Learning from labeled data — regression, classification, trees, SVMs, and gradient boosting
> (still the king of tabular data).

## 📑 Concept Index
Every chapter is a self-contained folder (`NN-Concept/NN-Concept.md`) with its page and a curated
`.references.md` resource card (free, open courses · videos · papers · articles · books · cross-links).
> **✅ ready.** New to the field? Start with the field overview below, then work top to bottom.

### Linear models
1. ✅ [Linear Regression](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/regression/linear-regression/linear-regression)
2. ✅ [Logistic Regression](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/classification/logistic-regression/logistic-regression)
3. ✅ [Regularization for Linear Models (Ridge · Lasso · Elastic-Net)](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/regression/regularization-linear-models/regularization-linear-models)

### Instance-based & probabilistic
4. ✅ [k-Nearest Neighbors (k-NN)](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/classification/k-nearest-neighbors/k-nearest-neighbors)
5. ✅ [Naive Bayes](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/classification/naive-bayes/naive-bayes)

### Margin & tree models
6. ✅ [Support Vector Machines (SVM)](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/classification/support-vector-machines/support-vector-machines)
7. ✅ [Decision Trees](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/trees-and-ensembles/decision-trees/decision-trees)

### Ensembles
8. ✅ [Bagging](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/trees-and-ensembles/bagging/bagging)
9. ✅ [Random Forests](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/trees-and-ensembles/random-forests/random-forests)
10. ✅ [Gradient Boosting (XGBoost · LightGBM · CatBoost)](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/trees-and-ensembles/gradient-boosting-xgboost/gradient-boosting-xgboost)
11. ✅ [Stacking & Blending](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/trees-and-ensembles/stacking-and-blending/stacking-and-blending)

### Theory & evaluation
12. ✅ [Bias–Variance Tradeoff](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/bias-variance-tradeoff/bias-variance-tradeoff)
13. ✅ [Cross-Validation](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/cross-validation/cross-validation)
14. ✅ [Classification Metrics (precision · recall · F1 · ROC-AUC · PR-AUC)](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/classification/classification-metrics/classification-metrics)
15. ✅ [Regression Metrics (RMSE · MAE · R²)](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/regression/regression-metrics/regression-metrics)

### Related concepts (covered in another section)
> These topics are used across many areas, so they're kept in one place to avoid repetition.
- **Math & optimization** — Gradient Descent · Maximum Likelihood · Convexity · Linear Algebra → [01. Foundations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme)
- **Neural networks** — MLPs · Backpropagation · Activation functions · Regularization (dropout/BN) → [05. Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/readme)
- **Clustering & dimensionality reduction** — k-Means · PCA · t-SNE · GMMs → [04. Unsupervised Learning](/ai-ml/ai-ml-learning-resources/core-machine-learning/unsupervised-learning/readme)
- **Feature engineering & data prep** — scaling · encoding · imputation · leakage → [02. Data Preprocessing](/ai-ml/ai-ml-learning-resources/foundations/data-preparation/readme)

## 🎓 Courses (free)
- [Machine Learning Specialization (Courses 1–2)](https://www.coursera.org/specializations/machine-learning-introduction) — **Andrew Ng** — regression → classification, the canonical intro.
- [Kaggle Learn: Intro + Intermediate ML](https://www.kaggle.com/learn) — **Kaggle** — trees → random forests → XGBoost, hands-on.

## 🎥 Videos
- [StatQuest ML playlist](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) — **Josh Starmer** — linear/logistic regression, trees, SVMs, boosting — each clearly explained.

## 📄 Key Papers
- [Random Forests](https://link.springer.com/article/10.1023/A:1010933404324) — **Breiman (2001)** — the bagging classic.
- [XGBoost: A Scalable Tree Boosting System](https://arxiv.org/abs/1603.02754) — **Chen & Guestrin (2016)** — the tabular-ML workhorse.

## 📚 Books (free)
- [An Introduction to Statistical Learning (ISLP)](https://www.statlearning.com/) — **James, Witten, Hastie & Tibshirani** — free; the best applied-ML textbook, with Python labs.
- [The Elements of Statistical Learning](https://hastie.su.domains/ElemStatLearn/) — **Hastie et al.** — free; the rigorous reference.

## 🔗 In this platform
- Losses & metrics: [ai-ml-intuitions Module 3](../../../ai-ml-intuitions/objectives-and-evaluation/) · Practice: [problemsets](../../../AI-ML-problemsets/)
