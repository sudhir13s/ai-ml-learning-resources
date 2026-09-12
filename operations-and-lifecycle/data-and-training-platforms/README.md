---
id: "operations-and-lifecycle/data-and-training-platforms"
topic: "Data and Training Platforms"
level: advanced
built_from: ["lifecycle-and-reproducibility", "data-preparation"]
updated: 2026-09-07
---

# Data and Training Platforms

> The data plane models are trained from: the system that guarantees a feature means the same
> thing offline and online, and the orchestrator that turns a notebook into a retryable directed
> acyclic graph (DAG). The compute plane — accelerators, parallelism, checkpoints, schedulers,
> cost — is its own sub-area, [Training Infrastructure](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/readme).

**Start here:** [Feature Stores](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/feature-stores/feature-stores) — the problem it solves (train/serve skew) is the reason the rest of the data platform exists.

## Concept index

Each page is a self-contained resource card: a plain-words definition, why it matters in 2026, a
five-step start-here path, and verified courses, videos, papers, articles and books.

1. [Feature Stores](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/feature-stores/feature-stores) — one feature definition serving both point-in-time-correct training data and low-latency online lookups; the cure for train/serve skew.
2. [ML Pipelines and Orchestration](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/ml-pipelines-and-orchestration/ml-pipelines-and-orchestration) — ingest → validate → transform → train → evaluate → deploy as a scheduled, retried, monitored DAG in Airflow or Kubeflow.

## Courses (free)

- [Made With ML — Feature Store](https://madewithml.com/courses/mlops/feature-store/) — **Goku Mohandas** — feature stores inside a complete production workflow rather than in isolation.
- [Made With ML — Orchestration](https://madewithml.com/courses/mlops/orchestration/) — **Goku Mohandas** — the same workflow turned into scheduled, retryable pipeline runs.

## Videos

- [Intro to Kubeflow Pipelines](https://www.youtube.com/watch?v=_AY8mmbR1o4) — **Google Cloud Tech** — ML-native pipelines, reusable components and metadata tracking.

## Key Papers

- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (Google, 2015)** — the pipeline-jungle and data-dependency debt that feature stores and orchestrators exist to cut.

## Articles / Blogs (free, no paywall)

- [Feature Stores — A Hierarchy of Needs](https://eugeneyan.com/writing/feature-stores/) — **Eugene Yan** — the clearest free explainer of what problem a feature store solves before which one to buy.
- [Feast documentation — Concepts](https://docs.feast.dev/getting-started/concepts) — **Feast maintainers** — entities, feature views, point-in-time joins and the offline/online split, defined by the people who built the reference implementation.

## Books (free, with chapters)

- [*Designing Machine Learning Systems* — Ch. 5 "Feature Engineering"](https://huyenchip.com/mlops/) — **Chip Huyen** — feature engineering, train/serve skew and stores; author notes free.

## In this platform

- Section index: [Operations and Lifecycle](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/readme)
- The compute plane: [Training Infrastructure](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/readme)
- Sibling sub-areas: [Lifecycle and Reproducibility](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/readme) · [Packaging and Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/readme) · [Release and Deployment](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/readme) · [Monitoring and Reliability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/readme) · [Governance and Economics](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/readme)
- Upstream of the features: [Data Preparation](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/readme)
- Doing it rather than reading it: [Data Preparation workflow](/ai-ml/practitioner-workflows/workflow-library/data-and-inputs/data-preparation)
