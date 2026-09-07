---
id: "02-data-preprocessing/datetime-cyclical"
topic: "Handling Date/Time & Cyclical Features"
parent: "02-data-preprocessing"
level: intermediate
built_from: ["pandas", "feature-engineering", "trigonometry"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Handling Date/Time & Cyclical Features"
minutes: 10
category: data-preparation
---

# Handling Date/Time & Cyclical Features
> Turning timestamps into useful signals — extracting hour/day/month/weekday, computing elapsed time and
> lags, and encoding periodic features with sine/cosine so "23:00" and "00:00" are correctly *close*.

**Why it matters:** raw datetimes are useless to most models, and naively encoding hour as 0–23 tells the
model that hour 23 and hour 0 are maximally far apart — wrong. Expect to explain datetime decomposition,
the **sine/cosine cyclical encoding** trick for periodic features (hour, month, day-of-week), lag/rolling
features for time series, and the time-aware leakage trap (never use future rows; split chronologically).

**Start here — suggested path:**

1. **Decompose datetimes** — read [pandas — time series functionality](https://pandas.pydata.org/docs/user_guide/timeseries.html). *Parsing, the `.dt` accessor, offsets and resampling: the components every temporal feature is built from.*
2. **See it in a workflow** — watch [Extract Hour, Day, Month from Pandas DateTime](https://www.youtube.com/watch?v=ZjMTZIxgkYo) — **Mısra Turp**. *The practical accessor workflow on a real frame.*
3. **Cyclical encoding** — read the [scikit-learn time-related feature engineering example](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html). *Why hour 23 and hour 0 must be adjacent, and how sine/cosine and splines each achieve it.*
4. **See it done right** — read [sklearn: Cyclical feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html). *Trigonometric vs spline encodings on a real bike-share dataset.*
5. **Time-series predictors** — read [FPP3: Useful predictors](https://otexts.com/fpp3/useful-predictors.html). *Trend, seasonal dummies, and Fourier terms for forecasting.*

## Courses (free)
- [Kaggle Learn — Time Series](https://www.kaggle.com/learn/time-series) — **Kaggle** — trend, seasonality, lags, and time-based features, hands-on.
- [Kaggle Learn — Feature Engineering](https://www.kaggle.com/learn/feature-engineering) — **Kaggle** — where date/time features fit in a broader pipeline.

## Videos
- [Feature Engineering for Time-Series Forecasting](https://www.youtube.com/watch?v=9QtL7m3YS9I) — **PyData (Kishan Manani)** — calendar, lag and window features built correctly and leakage-safely; the most complete talk on this topic.
- [Extract Hour, Day, Month from Pandas DateTime](https://www.youtube.com/watch?v=ZjMTZIxgkYo) — **Mısra Turp** — the practical `.dt` accessor workflow.
- [Pandas Tutorials (full playlist)](https://www.youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) — **Corey Schafer** — includes the datetime and time-series episodes: parsing, indexing, resampling and `shift`.

## Key Papers
- [Distributed and parallel time series feature extraction (FRESH / tsfresh)](https://arxiv.org/abs/1610.07717) — **Christ, Kempa-Liehr & Feindt (2017)** — systematic extraction + selection of temporal features; free on arXiv.
- [A Few Useful Things to Know about Machine Learning](https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf) — **Pedro Domingos (2012)** — why thoughtful feature construction (incl. temporal) drives results.

## Articles / Blogs (free, no paywall)
- [Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html) — **scikit-learn** — the canonical cyclical (sine/cosine) vs spline encoding example.
- [feature-engine — Datetime features](https://feature-engine.trainindata.com/en/latest/user_guide/datetime/index.html) — **Train in Data** — transformers that extract and cyclically encode datetime features.
- [pandas — Time series / date functionality](https://pandas.pydata.org/docs/user_guide/timeseries.html) — **pandas docs** — the authoritative reference for datetime handling, resampling, and offsets.

## Books (free, with chapters)
- [Forecasting: Principles and Practice (3rd ed.) — **Ch. 7 "Time series regression"** (trend, seasonal dummies, Fourier)](https://otexts.com/fpp3/useful-predictors.html) — **Hyndman & Athanasopoulos** — free, the standard forecasting text.
- [Feature Engineering and Selection — **Ch. 6 (transformations) & Ch. 9 (profile/temporal data)**](http://www.feat.engineering/) — **Kuhn & Johnson** — engineering features from structured/temporal data; free online.

## In this platform
- Concept depth (the *why*): [ai-ml-intuitions 1.03 Positional Encoding](/ai-ml/ai-ml-intuitions/representation/embedding-spaces/positional-representations-intuition) — the same sine/cosine idea that encodes sequence position.
- Next concepts: [06 Feature Engineering](/ai-ml/ai-ml-learning-resources/foundations/data-preparation/feature-engineering/feature-engineering) · [11 Data Leakage](/ai-ml/ai-ml-learning-resources/foundations/data-preparation/data-leakage/data-leakage)
- Related domain: [03. Supervised Learning](/ai-ml/ai-ml-learning-resources/core-machine-learning/supervised-learning/readme)
