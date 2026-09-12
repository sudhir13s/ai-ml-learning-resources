---
id: "02-data-preprocessing/eda"
topic: "Exploratory Data Analysis (EDA)"
parent: "02-data-preprocessing"
level: beginner
built_from: ["python", "pandas", "descriptive-statistics"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Exploratory Data Analysis (EDA)"
minutes: 10
category: data-preparation
---

# Exploratory Data Analysis (EDA)
> Looking at your data before you model it — distributions, missingness, outliers, correlations, and
> relationships — so every cleaning and feature decision that follows is grounded in what's actually there.

**Why it matters:** EDA is where you catch the problems that silently break models — skew, leakage hints,
data-entry errors, class imbalance, suspicious correlations. Interviewers ask "how would you approach a
new dataset?"; a structured EDA answer (univariate → bivariate → multivariate, plus quality checks) signals
real applied experience.

**Start here — suggested path:**

1. **See the workflow** — watch [Exploratory Data Analysis with Pandas](https://www.youtube.com/watch?v=xi0vhXFPegw) — **Rob Mulla**. *A full first pass on a real dataset: shape, types, missingness, one variable at a time, then relationships.*
2. **Read one plot properly** — watch [StatQuest: Histograms, Clearly Explained](https://www.youtube.com/watch?v=qBigTkBLU6g). *Bin width changes the story a distribution tells; knowing that keeps the first pass honest.*
3. **Get the mindset** — read [R4DS — Exploratory Data Analysis](https://r4ds.had.co.nz/exploratory-data-analysis.html). *The canonical "ask questions about your data" framework (language-agnostic).*
4. **Practice on real data** — do [Kaggle: Pandas](https://www.kaggle.com/learn/pandas). *Builds the muscle memory of slicing/grouping/aggregating you need for EDA.*
5. **Make plots speak** — skim the [Seaborn tutorial](https://seaborn.pydata.org/tutorial.html). *Distribution, relational, and categorical plots that reveal structure fast.*

## Courses (free)
- [Kaggle Learn — Pandas](https://www.kaggle.com/learn/pandas) — **Kaggle** — short, hands-on; the data-wrangling skills EDA is built on.
- [Kaggle Learn — Data Visualization](https://www.kaggle.com/learn/data-visualization) — **Kaggle** — short, hands-on lessons on the plots an exploratory pass actually produces.
- [scikit-learn MOOC — the predictive modelling pipeline](https://inria.github.io/scikit-learn-mooc/) — **INRIA / scikit-learn core developers** — starts where exploration ends: what you learned about the data, encoded into a pipeline.

## Videos
- [Exploratory Data Analysis with Pandas](https://www.youtube.com/watch?v=xi0vhXFPegw) — **Rob Mulla** — a Kaggle Grandmaster's full first pass on a real dataset: shape, dtypes, missingness, distributions, then relationships.
- [StatQuest: Histograms, Clearly Explained](https://www.youtube.com/watch?v=qBigTkBLU6g) — **StatQuest with Josh Starmer** — how bin width decides what a distribution appears to say; the most misread plot in every first EDA.
- [Pandas Tutorials (full playlist)](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) — **Corey Schafer** — the slicing, grouping and aggregation that every exploratory pass is made of.

## Key Papers
- [The Future of Data Analysis](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-33/issue-1/The-Future-of-Data-Analysis/10.1214/aoms/1177704711.full) — **John W. Tukey (1962)** — the manifesto that launched EDA as a discipline; free full text on Project Euclid.
- [Tidy Data](https://vita.had.co.nz/papers/tidy-data.pdf) — **Hadley Wickham (2014)** — why a consistent data layout makes EDA and modeling dramatically easier.

## Articles / Blogs (free, no paywall)
- [R for Data Science — Exploratory Data Analysis](https://r4ds.had.co.nz/exploratory-data-analysis.html) — **Wickham & Grolemund** — the definitive "questions-first" EDA framework, fully open.
- [NIST/SEMATECH e-Handbook — EDA](https://www.itl.nist.gov/div898/handbook/eda/eda.htm) — **NIST** — rigorous, free reference on EDA techniques and assumptions.
- [Seaborn tutorial](https://seaborn.pydata.org/tutorial.html) — **Seaborn docs** — the visualization grammar (distribution/relational/categorical) for EDA.
- [pandas — Getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html) — **pandas docs** — official, free, task-oriented intro to exploring data.

## Books (free, with chapters)
- [Python Data Science Handbook — **Ch. 3 (Pandas) & Ch. 4 (Matplotlib)**](https://jakevdp.github.io/PythonDataScienceHandbook/) — **Jake VanderPlas** — the free, runnable NumPy/Pandas/visualization reference.
- [R for Data Science — **Ch. 7 "Exploratory Data Analysis"**](https://r4ds.had.co.nz/exploratory-data-analysis.html) — **Wickham & Grolemund** — concepts transfer directly to Python.

## In this platform
- Concept depth (the *why*): [ai-ml-intuitions 0.02 Distributions & the Gaussian](/ai-ml/ai-ml-intuitions/foundational-mental-models/probability-and-belief/distributions-and-gaussians-intuition) · [0.03 Expectation, Variance, Covariance](/ai-ml/ai-ml-intuitions/foundational-mental-models/probability-and-belief/expectation-variance-and-covariance-intuition)
- Next concepts: [02 Feature Scaling & Normalization](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/feature-scaling-and-normalization/feature-scaling-and-normalization) · [05 Outlier Detection & Treatment](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/outlier-detection-and-treatment/outlier-detection-and-treatment)
- Related domain: [04. Unsupervised Learning](/ai-ml/ai-ml-learning-resources/classical-machine-learning/unsupervised-learning/readme)
