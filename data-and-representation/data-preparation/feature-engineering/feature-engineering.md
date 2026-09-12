---
id: "02-data-preprocessing/feature-engineering"
topic: "Feature Engineering"
parent: "02-data-preprocessing"
level: intermediate
built_from: ["pandas", "domain-knowledge", "transformations"]
interview_frequency: very-high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Feature Engineering"
minutes: 10
category: data-preparation
---

# Feature Engineering
> Creating better inputs from raw data — combining columns, splitting fields, binning, log/power
> transforms, and interaction terms — so a model can learn relationships it otherwise couldn't.

**Why it matters:** "better data beats fancier algorithms" — feature engineering is where most real-world
accuracy gains come from, and the classic interview line is *"feature engineering is the part of ML that
domain knowledge buys you."* Be ready to walk through constructing a feature, why log/Box-Cox fixes skew,
when binning helps tree-free models, and how to engineer **without leaking** future or target information.

**Start here — suggested path:**

1. **Construct features** — work [Kaggle Learn — Feature Engineering](https://www.kaggle.com/learn/feature-engineering). *Combining and decomposing columns, mutual information, and interaction terms on real data.*
2. **Fix skew** — read [sklearn: non-linear transformations](https://scikit-learn.org/stable/modules/preprocessing.html) (`FunctionTransformer`, `QuantileTransformer`). *Log and square-root transforms, and when a rank-based transform is the safer choice.*
3. **Power transforms** — read the `PowerTransformer` section of the same guide. *Box-Cox and Yeo-Johnson: data-driven variance stabilization, and why Yeo-Johnson tolerates zeros and negatives.*
4. **Discretize** — read the `KBinsDiscretizer` section and the [cyclical feature example](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html). *Buckets, quantile bins, and spline features, with a worked demand-forecasting case.*
5. **Internalize the principle** — read [A Few Useful Things to Know about ML](https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf). *Domingos on why feature engineering is the key to applied ML.*

## Courses (free)
- [Kaggle Learn — Feature Engineering](https://www.kaggle.com/learn/feature-engineering) — **Kaggle** — the best free hands-on course: mutual info, interactions, target encoding, clustering features.
- [Google ML Crash Course — Numerical & Categorical data](https://developers.google.com/machine-learning/crash-course/numerical-data) — **Google** — feature transforms, bucketing, and crosses, applied.

## Videos
- [Exploratory Data Analysis with Pandas](https://www.youtube.com/watch?v=xi0vhXFPegw) — **Rob Mulla** — where features come from: looking at the columns until the useful combination is obvious.
- [StatQuest: Histograms, Clearly Explained](https://www.youtube.com/watch?v=qBigTkBLU6g) — **StatQuest with Josh Starmer** — reading skew off a distribution, which is what triggers a log or power transform in the first place.
- [probabl (scikit-learn maintainers' channel)](https://www.youtube.com/@probabl_ai) — **probabl / scikit-learn core developers** — transformers, `ColumnTransformer` and custom feature code, from the maintainers.

## Key Papers
- [A Few Useful Things to Know about Machine Learning](https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf) — **Pedro Domingos (2012)** — the famous "feature engineering is the key" essay; free PDF.
- [Wide & Deep Learning for Recommender Systems](https://arxiv.org/abs/1606.07792) — **Cheng et al. (2016)** — how hand-crafted cross-features and learned embeddings combine in practice.

## Articles / Blogs (free, no paywall)
- [Preprocessing data — user guide](https://scikit-learn.org/stable/modules/preprocessing.html) — **scikit-learn** — PolynomialFeatures, KBinsDiscretizer, PowerTransformer, FunctionTransformer.
- [feature-engine documentation](https://feature-engine.trainindata.com/en/latest/) — **Train in Data** — a transformer library purpose-built for feature engineering, with clear docs.
- [Tidy Data](https://vita.had.co.nz/papers/tidy-data.pdf) — **Hadley Wickham** — the data layout that makes feature engineering clean and repeatable.

## Books (free, with chapters)
- [Feature Engineering and Selection — **Ch. 6 (numeric) & Ch. 5 (categorical)**](http://www.feat.engineering/) — **Kuhn & Johnson** — the canonical free FE text.
- [Python Data Science Handbook — **§5.4 "Feature Engineering"**](https://jakevdp.github.io/PythonDataScienceHandbook/05.04-feature-engineering.html) — **Jake VanderPlas** — derived features, polynomial features, and pipelines.

## In this platform
- Concept depth (the *why*): [ai-ml-intuitions 1.01 One-Hot Encoding](/ai-ml/ai-ml-intuitions/representation/discrete-representations/one-hot-encoding-intuition) · [1.17 BoW & TF-IDF](/ai-ml/ai-ml-intuitions/representation/discrete-representations/bag-of-words-and-tf-idf-intuition)
- Next concepts: [07 Feature Selection](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/feature-selection/feature-selection) · [08 Date/Time & Cyclical Features](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/date-time-and-cyclical-features/date-time-and-cyclical-features)
- Related domain: [03. Supervised Learning](/ai-ml/ai-ml-learning-resources/classical-machine-learning/supervised-learning/readme)
