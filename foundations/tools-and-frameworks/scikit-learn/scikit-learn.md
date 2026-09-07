---
id: "17-tools-and-frameworks/scikit-learn"
topic: "scikit-learn (classical ML, pipelines, model selection)"
parent: "17-tools-and-frameworks"
level: beginner
built_from: ["python", "numpy", "pandas"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "scikit-learn (classical ML, pipelines, model selection)"
minutes: 10
category: tools-and-frameworks
---

# scikit-learn — Classical ML · Pipelines · Model Selection
> The standard library for classical machine learning in Python: a consistent
> `fit`/`predict`/`transform` API across dozens of algorithms, plus preprocessing, `Pipeline`s,
> cross-validation, and hyperparameter search. The fastest path from a DataFrame to a trained,
> evaluated model.

**Why it matters:** before reaching for deep learning, most real problems are solved with
scikit-learn — and interviews lean on its concepts: train/test splits and leakage, cross-validation,
the estimator API, building leak-proof `Pipeline`s, and `GridSearchCV`/`RandomizedSearchCV`. It is
also where you internalize the *workflow* of supervised learning.

**Start here — suggested path:**

1. **See the API shape** — read [Getting Started](https://scikit-learn.org/stable/getting_started.html). *The unified `fit`/`predict`/`transform` API is the whole library in one idea.*
2. **Do a guided course** — start the [scikit-learn MOOC](https://inria.github.io/scikit-learn-mooc/) (INRIA, the maintainers). *The best free, hands-on course on the predictive-modeling workflow.*
3. **Watch the workflow live** — work through the [ISLP Python labs](https://www.youtube.com/playlist?list=PLoROMvodv4rNHU1-iPeDRH-J0cL-CrIda) — **Stanford Online**. *Each lab pairs a method with the scikit-learn code that fits and evaluates it.*
4. **Avoid leakage with Pipelines** — study the [User Guide](https://scikit-learn.org/stable/user_guide.html) on Pipelines, preprocessing, and cross-validation. *Pipelines + proper CV are the #1 thing interviews and real projects get wrong.*
5. **Adapt from examples** — browse the [example gallery](https://scikit-learn.org/stable/auto_examples/index.html). *Finding a worked example near your problem is the real practitioner workflow.*

## Courses (free)
- [scikit-learn MOOC](https://inria.github.io/scikit-learn-mooc/) — **INRIA / scikit-learn core devs** — the definitive free course on the predictive-modeling workflow with the library.
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) — **scikit-learn team** — a complete, topic-by-topic course on every estimator family and workflow.

## Videos
- [Statistical Learning — ISLP Python labs](https://www.youtube.com/playlist?list=PLoROMvodv4rNHU1-iPeDRH-J0cL-CrIda) — **Stanford Online (Hastie, Tibshirani and co-authors)** — the *Introduction to Statistical Learning* labs worked in Python; the method and the scikit-learn code, taught by the people who wrote the book.
- [probabl (scikit-learn maintainers' channel)](https://www.youtube.com/@probabl_ai) — **probabl / scikit-learn core developers** — live sessions and feature deep-dives from the people who maintain the library.
- [Machine Learning Fundamentals: Cross Validation](https://www.youtube.com/watch?v=fSytzGwwBVw) — **StatQuest with Josh Starmer** — the idea behind `cross_val_score` in six minutes; watch before trusting a single train/test split.
- [Machine Learning Fundamentals: Bias and Variance](https://www.youtube.com/watch?v=EuBBz3bI-aA) — **StatQuest with Josh Starmer** — what model selection is trading off when you tune with `GridSearchCV`.

## Key Papers
- [Scikit-learn: Machine Learning in Python](https://www.jmlr.org/papers/v12/pedregosa11a.html) — **Pedregosa et al. (2011), *JMLR*** — the foundational open-access paper.
- [API design for machine learning software](https://arxiv.org/abs/1309.0238) — **Buitinck et al. (2013)** — explains the estimator/transformer/pipeline API decisions (free on arXiv).

## Articles / Blogs (free, no paywall)
- [Getting Started](https://scikit-learn.org/stable/getting_started.html) — **scikit-learn team** — the unified API and a first end-to-end example.
- [Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html) — **scikit-learn team** — data leakage, randomness, and how to do CV correctly.
- [Python Data Science Handbook — **Ch. 5 "Machine Learning"**](https://jakevdp.github.io/PythonDataScienceHandbook/05.00-machine-learning.html) — **Jake VanderPlas** — full chapter, scikit-learn-based, free online.
- [calmcode](https://calmcode.io/) — **Vincent Warmerdam (probabl)** — very short, precise screencasts on scikit-learn internals and habits: pipelines, custom transformers, metrics, and the mistakes they prevent.
- [An Introduction to Statistical Learning (ISLP)](https://www.statlearning.com/) — **James, Witten, Hastie, Tibshirani & Taylor** — free PDF plus Python labs; the theory behind the estimators you are calling.

## Books (free, with chapters)
- [scikit-learn MOOC (full curriculum)](https://inria.github.io/scikit-learn-mooc/) — **INRIA** — a book-length, free, structured course with runnable notebooks.
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) — **Jake VanderPlas** — entire book free; Ch. 5 is a thorough scikit-learn treatment.

## In this platform
- Related domain: [03. Supervised Learning](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/readme) · [04. Unsupervised Learning](/ai-ml/ai-ml-learning-resources/core-machine-learning/unsupervised-learning/readme)
- Pairs with: [02 Pandas](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/pandas/pandas) · [12 Weights & Biases](/ai-ml/ai-ml-learning-resources/foundations/tools-and-frameworks/weights-and-biases/weights-and-biases)
- Deeper concept (the *why*): model selection & metrics → [Deployment & MLOps](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/readme)
