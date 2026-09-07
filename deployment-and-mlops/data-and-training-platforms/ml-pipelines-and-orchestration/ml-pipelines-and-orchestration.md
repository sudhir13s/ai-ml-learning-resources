---
id: "18-mlops/ml-pipelines-and-orchestration"
topic: "ML Pipelines & Orchestration (Airflow · Kubeflow)"
parent: "18-mlops-and-deployment"
level: advanced
built_from: ["ml-lifecycle", "reproducibility"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "ML Pipelines & Orchestration (Airflow · Kubeflow)"
minutes: 10
category: data-and-training-platforms
---

# ML Pipelines & Orchestration — Airflow · Kubeflow
> Turning an ad-hoc notebook into a reliable DAG of steps (ingest → validate → transform → train →
> evaluate → deploy) that an orchestrator schedules, retries, and monitors. The automation backbone of
> MLOps maturity level 1 — pipelines, not people, run the workflow.

**Why it matters:** the "how do you automate retraining / move from a notebook to a production pipeline?"
question. Expect the DAG model, idempotency and retries, why data pipelines differ from generic workflows
(data validation, lineage, caching), and the tool landscape: **Airflow 3** (general workflow scheduler,
now with a task-execution API and DAG versioning) vs **Kubeflow Pipelines 2** (Kubernetes-native,
ML-specific) vs asset/flow-first options (Dagster, Prefect, Metaflow).

**Start here — suggested path:**

1. **Get the levels** — read [ml-ops.org: Three Levels of ML Software](https://ml-ops.org/content/three-levels-of-ml-software). *Why pipelines (not scripts) are what "automation" means in MLOps.*
2. **Learn the DAG model** — read [Airflow: core concepts overview](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/overview.html). *DAGs, tasks, scheduling, retries — the orchestration vocabulary, from the project itself.*
3. **See the ML-native option** — read [Kubeflow Pipelines Overview](https://www.kubeflow.org/docs/components/pipelines/overview/) and watch [Intro to Kubeflow Pipelines](https://www.youtube.com/watch?v=_AY8mmbR1o4). *Containerized, reusable ML components on Kubernetes.*
4. **Build a real pipeline** — work [Made With ML: Orchestration](https://madewithml.com/courses/mlops/orchestration/). *Wires data → train → evaluate into a runnable, scheduled DAG.*
5. **Compare tools on their own docs** — skim [Dagster](https://docs.dagster.io/), [Prefect](https://docs.prefect.io/) and [Metaflow](https://docs.metaflow.org/). *Asset-first vs flow-first vs Python-native — the decision criteria interviewers expect you to weigh.*

## Courses (free)
- [Made With ML — Orchestration](https://madewithml.com/courses/mlops/orchestration/) — **Goku Mohandas** — build and schedule a real ML DAG.
- [Apache Airflow — Fundamentals Tutorial](https://airflow.apache.org/docs/apache-airflow/stable/index.html) — **Apache Airflow** — official docs + tutorial for authoring DAGs.
- [Full Stack Deep Learning — the course](https://fullstackdeeplearning.com/course/) — **The Full Stack** — where pipelines sit in a shipped ML product, lectures and notes free.

## Videos
- [Intro to Kubeflow Pipelines](https://www.youtube.com/watch?v=_AY8mmbR1o4) — **Google Cloud Tech** — ML-native pipelines, reusable components, metadata tracking.
- [Introducing Apache Airflow 3](https://www.youtube.com/watch?v=2La0OfXE_TY) — **Databricks (with Astronomer)** — what Airflow 3 changed: DAG versioning, the task-execution API, event-driven scheduling.
- [Machine Learning Pipelines with DVC (Hands-On)](https://www.youtube.com/watch?v=71IGzyH95UY) — **DVCorg** — lightweight, reproducible pipelines with DAG stages and caching.

## Key Papers
- [MLOps: Continuous delivery and automation pipelines in ML](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — **Google Cloud** — the whitepaper defining ML pipeline automation (level 1).
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (2015)** — "pipeline jungles" and glue code that orchestration is meant to tame.

## Articles / Blogs (free, no paywall)
- [Three Levels of ML Software](https://ml-ops.org/content/three-levels-of-ml-software) — **ml-ops.org** — data/model/code pipelines and how they automate the lifecycle.
- [Kubeflow Pipelines — Overview](https://www.kubeflow.org/docs/components/pipelines/overview/) — **Kubeflow** — the ML-pipeline component model on Kubernetes.
- [Apache Airflow — Documentation](https://airflow.apache.org/docs/apache-airflow/stable/index.html) — **Apache** — DAGs, operators, scheduling, and executors.
- [Dagster Documentation](https://docs.dagster.io/) — **Dagster Labs** — the asset-first alternative: you declare the *data assets*, the graph is derived — a natural fit for ML lineage.
- [Prefect Documentation](https://docs.prefect.io/) — **Prefect** — Python-native flows with dynamic, runtime-defined DAGs.
- [Metaflow Documentation](https://docs.metaflow.org/) — **Netflix / Outerbounds** — the data-scientist-facing flow API with built-in versioning and cloud scale-out.

## Books (free, with chapters)
- [Designing Machine Learning Systems — **Ch. 6 "Model Development"** & **Ch. 10 "Infrastructure & Tooling"** (orchestration)](https://huyenchip.com/mlops/) — **Chip Huyen** — author notes/talks free.
- [Machine Learning Engineering — **Ch. 7–8** (model deployment & pipelines)](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — read-first chapters free.

## In this platform
- Builds on: [01 ML Lifecycle & MLOps Maturity](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/lifecycle-and-reproducibility/ml-lifecycle-and-mlops-maturity/ml-lifecycle-and-mlops-maturity) · [05 Feature Stores](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/data-and-training-platforms/feature-stores/feature-stores)
- Next concepts: [07 CI/CD for ML & CT](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/release-and-deployment/cicd-for-ml-and-continuous-training/cicd-for-ml-and-continuous-training) · [10 Scaling Inference](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/packaging-and-serving/scaling-inference/scaling-inference)
