---
id: "02-data-preprocessing/encoding-categoricals"
topic: "Encoding Categorical Variables"
parent: "02-data-preprocessing"
level: beginner
built_from: ["pandas", "one-hot-encoding"]
interview_frequency: very-high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Encoding Categorical Variables"
minutes: 10
category: data-preparation
---

# Encoding Categorical Variables
> Turning categories into numbers models can use — one-hot for nominal, ordinal for ordered, and
> target/mean encoding for high-cardinality features — without inventing fake order or leaking the target.

**Why it matters:** a staple interview topic. You should know one-hot vs ordinal vs label encoding and
when each is appropriate, why label-encoding a nominal feature misleads linear models, the curse of
high-cardinality (one-hot blowup) and how target encoding addresses it, and the **leakage trap** in target
encoding (must be fit inside cross-validation / with smoothing).

**Start here — suggested path:**

1. **Ordinal versus nominal** — read [sklearn: Encoding categorical features](https://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features). *`OrdinalEncoder` asserts an order; `OneHotEncoder` refuses to. Picking wrongly is the most common quiet error on this topic.*
2. **One-hot done right** — read [Google ML Crash Course — Categorical data](https://developers.google.com/machine-learning/crash-course/categorical-data). *Dummy variables, sparsity, and what to do with a category the model has never seen.*
3. **High cardinality** — read [Target encoding done the right way](https://maxhalford.github.io/blog/target-encoding/). *Mean encoding with smoothing + how to avoid leakage.*
4. **Reference the API** — read [sklearn: Encoding categorical features](https://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features). *OneHotEncoder/OrdinalEncoder/TargetEncoder, with handle_unknown.*
5. **Apply in a pipeline** — see [sklearn TargetEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html). *Built-in cross-fitted target encoding that prevents leakage.*

## Courses (free)
- [Google ML Crash Course — Categorical data](https://developers.google.com/machine-learning/crash-course/categorical-data) — **Google** — free, clear treatment of vocabulary, one-hot, and embeddings.
- [Kaggle Learn — Feature Engineering (Categorical Encodings)](https://www.kaggle.com/learn/feature-engineering) — **Kaggle** — hands-on count/target encoding on real data.

## Videos
- [probabl (scikit-learn maintainers' channel)](https://www.youtube.com/@probabl_ai) — **probabl / scikit-learn core developers** — sessions on encoders and `ColumnTransformer` from the people who wrote `TargetEncoder`.
- [Machine Learning Fundamentals: Cross Validation](https://www.youtube.com/watch?v=fSytzGwwBVw) — **StatQuest with Josh Starmer** — the loop target encoding must be fitted inside; the whole leakage trap in six minutes.
- [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) — **Andrej Karpathy** — the same problem one level up: turning unbounded discrete symbols into integers a model can consume.

## Key Papers
- [Similarity Encoding for Learning with Dirty Categorical Variables](https://arxiv.org/abs/1806.00979) — **Cerda, Varoquaux & Kégl (2018)** — handling high-cardinality and noisy categories beyond one-hot; free on arXiv.
- [Entity Embeddings of Categorical Variables](https://arxiv.org/abs/1604.06737) — **Guo & Berkhahn (2016)** — learning dense embeddings for categories (the neural alternative to one-hot).

## Articles / Blogs (free, no paywall)
- [Target encoding done the right way](https://maxhalford.github.io/blog/target-encoding/) — **Max Halford** — smoothing + leakage-safe target encoding, with math and code.
- [Encoding categorical features — user guide](https://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features) — **scikit-learn** — the authoritative API reference for all encoders.
- [category_encoders documentation](https://contrib.scikit-learn.org/category_encoders/) — **scikit-learn-contrib** — a whole library of encoders (target, James-Stein, CatBoost, hashing) with explanations.

## Books (free, with chapters)
- [Feature Engineering and Selection — **Ch. 5 "Encoding Categorical Predictors"**](http://www.feat.engineering/) — **Kuhn & Johnson** — one-hot, effect, and likelihood/target encodings; free online.
- [Python Data Science Handbook — **§5.4 "Feature Engineering" (Categorical Features)**](https://jakevdp.github.io/PythonDataScienceHandbook/05.04-feature-engineering.html) — **Jake VanderPlas** — practical one-hot with DictVectorizer.

## In this platform
- Concept depth (the *why*): [ai-ml-intuitions 1.01 One-Hot Encoding](/ai-ml/ai-ml-intuitions/representation/discrete-representations/one-hot-encoding-intuition) · [1.02 Dense Embeddings](/ai-ml/ai-ml-intuitions/representation/embedding-spaces/dense-embeddings-intuition)
- Next concepts: [06 Feature Engineering](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/feature-engineering/feature-engineering) · [11 Data Leakage](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/data-leakage/data-leakage)
- Related domain: [01. Foundations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme)
