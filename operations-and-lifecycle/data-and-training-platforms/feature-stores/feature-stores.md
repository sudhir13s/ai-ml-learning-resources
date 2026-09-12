---
id: "18-mlops/feature-stores"
topic: "Feature Stores (Feast)"
parent: "18-mlops-and-deployment"
level: advanced
built_from: ["data-and-model-versioning", "feature-engineering"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Feature Stores (Feast)"
minutes: 10
category: data-and-training-platforms
---

# Feature Stores — Feast
> A central system that computes, stores, and serves ML features for both training (offline, historical,
> point-in-time correct) and inference (online, low-latency) — guaranteeing the **same** feature logic
> in both. The fix for train/serve skew and duplicated feature pipelines across teams.

**Why it matters:** the "how do you stop training and serving from computing features differently?"
question. Interviewers want the offline vs online split, **point-in-time correctness** (no future
leakage in training labels), feature reuse/discovery across teams, and where a feature store sits in
the architecture. Feast is the canonical open-source example; by 2026 most teams meet the pattern
inside a managed platform (Databricks, Vertex AI, Tecton) where the warehouse doubles as the offline
store — so know the *pattern*, and be able to say when a feature store is overkill.

**Start here — suggested path:**

1. **Understand the problem** — read [Feature Stores for ML](https://eugeneyan.com/writing/feature-stores/). *Train/serve skew and the offline/online duality — the "why" before any tool.*
2. **See the canonical design** — read [Feast: Architecture](https://docs.feast.dev/getting-started/architecture). *Offline store, online store, registry, materialization — the four pieces every feature store has.*
3. **Build one** — follow [Feast Quickstart](https://docs.feast.dev/getting-started/quickstart). *Define features, materialize to the online store, and fetch for inference — point-in-time joins click here.*
4. **Put it in a pipeline** — work [Made With ML: Feature Store](https://madewithml.com/courses/mlops/feature-store/). *Connects the store to training + serving in a real MLOps flow.*
5. **Survey the landscape** — browse [featurestore.org](https://www.featurestore.org/). *Where managed/open options differ, and when a feature store is overkill.*

## Courses (free)
- [Made With ML — Feature Store](https://madewithml.com/courses/mlops/feature-store/) — **Goku Mohandas** — feature stores in a full production ML workflow.
- [Feast — Getting Started](https://docs.feast.dev/getting-started/quickstart) — **Feast** — guided, hands-on intro to defining and serving features.

## Videos
- [Rethinking Feature Stores with Feast and Tecton (apply() Conference)](https://www.youtube.com/watch?v=qh7bh4YVI2E) — **Tecton (Mike Del Balso & Willem Pienaar, Feast tech lead)** — the people who built Feast on what a feature store is and is not.
- [Feast: feature store for Machine Learning](https://www.youtube.com/watch?v=DaNv-Wf1MBA) — **Hasgeek TV** — conference talk: concepts plus a live demo of offline/online serving.

## Key Papers
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (2015)** — "data dependencies" and pipeline-jungle debt that feature stores exist to cut.
- [MLOps: Continuous delivery and automation pipelines in ML](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — **Google Cloud** — where feature engineering/serving fits the automated lifecycle.

## Articles / Blogs (free, no paywall)
- [Feature Stores — A Hierarchy of Needs](https://eugeneyan.com/writing/feature-stores/) — **Eugene Yan** — the clearest free explainer of the problem and the design.
- [Feast Documentation](https://docs.feast.dev/) — **Feast** — concepts, architecture, and the offline/online split in depth.
- [Feature Store for ML (featurestore.org)](https://www.featurestore.org/) — **community** — vendor-neutral landscape, definitions, and patterns.
- [Databricks Feature Store / Feature Engineering docs](https://docs.databricks.com/aws/en/machine-learning/feature-store/) — **Databricks** — how a managed store handles point-in-time lookups and online publishing; useful contrast to self-hosted Feast.
- [Vertex AI Feature Store overview](https://cloud.google.com/vertex-ai/docs/featurestore/latest/overview) — **Google Cloud** — the 2025 BigQuery-backed redesign, where the offline store *is* the warehouse.

## Books (free, with chapters)
- [Designing Machine Learning Systems — **Ch. 5 "Feature Engineering"** & feature-store discussion](https://huyenchip.com/mlops/) — **Chip Huyen** — feature engineering, train/serve skew, and stores (author notes free).
- [Machine Learning Engineering — **Ch. 4 "Feature Engineering"**](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — feature lifecycle and serving; read-first chapters free.

## In this platform
- Builds on: [04 Data & Model Versioning](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/data-and-model-versioning/data-and-model-versioning)
- Next concepts: [06 ML Pipelines & Orchestration](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/ml-pipelines-and-orchestration/ml-pipelines-and-orchestration) · [11 Model Monitoring & Observability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability)
- Related concept (covered elsewhere): feature engineering theory → [02. Data_Preprocessing](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/readme)
