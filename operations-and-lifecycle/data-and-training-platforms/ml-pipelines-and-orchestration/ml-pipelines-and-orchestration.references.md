---
id: "18-mlops/ml-pipelines-and-orchestration/references"
topic: "ML Pipelines & Orchestration (Airflow · Kubeflow) — References"
parent: "18-mlops/ml-pipelines-and-orchestration"
type: references
updated: 2026-09-13
---

# ML Pipelines and Orchestration — references

> Companion link library for **[ML Pipelines and Orchestration](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/ml-pipelines-and-orchestration/ml-pipelines-and-orchestration)** (the teaching page). Internal links and external sources, grouped by type and alphabetical within each group.

**Start here — suggested path**:

1. **See an ML-native pipeline** — watch [Intro to Kubeflow Pipelines](https://www.youtube.com/watch?v=_AY8mmbR1o4). *Containerized, reusable components with metadata tracked per step.*
2. **Get the levels** — read [Three Levels of ML Software](https://ml-ops.org/content/three-levels-of-ml-software). *Why pipelines, not scripts, are what automation means in MLOps.*
3. **Learn the DAG model** — read [Apache Airflow — Core concepts](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/overview.html), then run the runner in [ML Pipelines and Orchestration](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/ml-pipelines-and-orchestration/ml-pipelines-and-orchestration). *Order, retries and caching, from the project and from scratch.*
4. **Build a real pipeline** — work [Made With ML — Orchestration](https://madewithml.com/courses/mlops/orchestration/). *Data, training and evaluation wired into a scheduled DAG.*
5. **Compare tools on their own docs** — skim [Dagster](https://docs.dagster.io/), [Prefect](https://docs.prefect.io/) and [Metaflow](https://docs.metaflow.org/). *Asset-first versus flow-first versus Python-native.*

**In this platform**:
- [CI/CD for ML and Continuous Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/cicd-for-ml-and-continuous-training/cicd-for-ml-and-continuous-training) — the gated release pipeline a registered candidate enters next.
- [Cluster Scheduling and Training Orchestration](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/cluster-scheduling-and-training-orchestration/cluster-scheduling-and-training-orchestration) — how the train step gets its GPUs.
- [Continuous Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/continuous-training/continuous-training) — this DAG fired by a schedule or a drift trigger.
- [Feature Stores](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/feature-stores/feature-stores) — where the ingest step usually reads features.
- [ML Lifecycle and MLOps Maturity](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/ml-lifecycle-and-mlops-maturity/ml-lifecycle-and-mlops-maturity) — why pipelines mark the step from manual to automated.
- [ml-platform](/python/python-production-examples/ml-platform/readme) — the runnable service with an idempotent DAG runner and gate-driven skip propagation.
- [Reproducibility](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/reproducibility/reproducibility) — pinning the inputs that make a cached step safe to reuse.

**Videos**:
- [Intro to Kubeflow Pipelines](https://www.youtube.com/watch?v=_AY8mmbR1o4) — **Google Cloud Tech** — ML-native pipelines, reusable components, metadata tracking.
- [Introducing Apache Airflow 3](https://www.youtube.com/watch?v=2La0OfXE_TY) — **Databricks (with Astronomer)** — DAG versioning, the task-execution API, event-driven scheduling.
- [Machine Learning Pipelines with DVC (Hands-On)](https://www.youtube.com/watch?v=71IGzyH95UY) — **DVCorg** — lightweight, reproducible pipelines with DAG stages and caching.

**Courses**:
- [Full Stack Deep Learning — the course](https://fullstackdeeplearning.com/course/) — **The Full Stack** — where pipelines sit in a shipped ML product.
- [Made With ML — Orchestration](https://madewithml.com/courses/mlops/orchestration/) — **Goku Mohandas** — wires data, training and evaluation into a runnable, scheduled DAG.

**Articles**:
- [MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — **Google Cloud** — defines ML pipeline automation as MLOps level 1.
- [Three Levels of ML Software](https://ml-ops.org/content/three-levels-of-ml-software) — **ml-ops.org** — data, model and code pipelines and how they automate the lifecycle.

**Papers**:
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (2015)** — "pipeline jungles" and glue code that orchestration is meant to tame.

**Documentation**:
- [Apache Airflow — Core concepts](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/overview.html) — **Apache Airflow** — DAGs, tasks, scheduling and retries from the project itself.
- [Apache Airflow — Documentation](https://airflow.apache.org/docs/apache-airflow/stable/index.html) — **Apache Airflow** — operators, executors and the authoring tutorial.
- [Dagster Documentation](https://docs.dagster.io/) — **Dagster Labs** — asset-first orchestration: declare the data assets and the graph is derived.
- [graphlib — topological sorting](https://docs.python.org/3/library/graphlib.html) — **Python Software Foundation** — the standard-library sorter and cycle detection the runnable example uses.
- [Kubeflow Pipelines — Overview](https://www.kubeflow.org/docs/components/pipelines/overview/) — **Kubeflow** — containerized, reusable ML components on Kubernetes.
- [Metaflow Documentation](https://docs.metaflow.org/) — **Netflix / Outerbounds** — the data-scientist-facing flow API with built-in versioning.
- [Prefect Documentation](https://docs.prefect.io/) — **Prefect** — Python-native flows with dynamic, runtime-defined graphs.

**Books**:
- [*Designing Machine Learning Systems* — Ch. 10 "Infrastructure & Tooling for MLOps"](https://huyenchip.com/mlops/) — **Chip Huyen** — schedulers versus orchestrators and the workflow-management landscape.
- [*Machine Learning Engineering* — Ch. 7–8](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — model deployment and pipelines; read-first chapters online.
