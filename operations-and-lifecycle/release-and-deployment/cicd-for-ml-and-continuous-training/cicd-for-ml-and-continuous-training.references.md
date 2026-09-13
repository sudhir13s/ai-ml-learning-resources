---
id: "18-mlops/cicd-for-ml-and-continuous-training/references"
topic: "CI/CD for ML & Continuous Training (CT) — References"
parent: "18-mlops/cicd-for-ml-and-continuous-training"
type: references
updated: 2026-09-13
---

# CI/CD for ML and Continuous Training — references

> Companion link library for **[CI/CD for ML and Continuous Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/cicd-for-ml-and-continuous-training/cicd-for-ml-and-continuous-training)** (the teaching page). Internal links and external sources, grouped by type and alphabetical within each group.

**Start here — suggested path**:

1. **See why ML CI is different** — watch [MLOps Tutorial #1: Intro to Continuous Integration for ML](https://www.youtube.com/watch?v=9BgIDqAzfuA). *Data and model checks, not just unit tests.*
2. **Get the vocabulary** — read [Continuous Delivery for Machine Learning (CD4ML)](https://martinfowler.com/articles/cd4ml.html). *The canonical article interviewers borrow their terms from.*
3. **Learn the gate** — read [CI/CD for ML and Continuous Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/cicd-for-ml-and-continuous-training/cicd-for-ml-and-continuous-training) and run its gate. *Floor, no regression and latency, with the verdict CI keys off.*
4. **See a model gate in a pull request** — watch [MLOps Tutorial #3: Track ML Models with Git & GitHub Actions](https://www.youtube.com/watch?v=xPncjKH6SPk). *Model metrics compared across branches before merge.*
5. **Build the whole pipeline** — work [Made With ML — CI/CD](https://madewithml.com/courses/mlops/cicd/). *A complete GitHub Actions flow for testing, training and deploying.*

**In this platform**:
- [A/B Testing, Shadow and Canary Deployment](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/ab-testing-shadow-and-canary-deployment/ab-testing-shadow-and-canary-deployment) — where a model goes once the gate lets it through.
- [Continuous Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/continuous-training/continuous-training) — the retraining loop whose candidates enter this pipeline.
- [Data and Concept Drift Detection](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/data-and-concept-drift-detection/data-and-concept-drift-detection) — the signal that fires a retrain.
- [Experiment Tracking](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/experiment-tracking/experiment-tracking) — the record of which run produced the metrics the gate reads.
- [ML Lifecycle and MLOps Maturity](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/ml-lifecycle-and-mlops-maturity/ml-lifecycle-and-mlops-maturity) — where automated CI/CD/CT sits on the maturity ladder.
- [ML Pipelines and Orchestration](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/ml-pipelines-and-orchestration/ml-pipelines-and-orchestration) — the step graph that produces each candidate.
- [ml-platform](/python/python-production-examples/ml-platform/readme) — the runnable service with a gated promotion state machine.
- [Model Evaluation and Benchmarks](/ai-ml/ai-ml-learning-resources/evaluation/model-evaluation-and-benchmarks/model-evaluation-and-benchmarks) — how the evaluation report is produced.
- [Model Packaging and Containerization](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-packaging-and-containerization/model-packaging-and-containerization) — the artifact and image the build stage produces.
- [Rollback and Recovery for ML Systems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/rollback-and-recovery-for-ml-systems/rollback-and-recovery-for-ml-systems) — the undo for a release that got past every gate.

**Videos**:
- [Full Stack Deep Learning 2022 lecture series](https://www.youtube.com/playlist?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur) — **The Full Stack (Charles Frye, Sergey Karayev, Josh Tobin)** — the deployment and testing lectures cover the train, validate, ship path end to end.
- [MLOps Tutorial #1: Intro to Continuous Integration for ML](https://www.youtube.com/watch?v=9BgIDqAzfuA) — **DVCorg** — why ML CI needs data and model checks, not just unit tests.
- [MLOps Tutorial #3: Track ML Models with Git & GitHub Actions](https://www.youtube.com/watch?v=xPncjKH6SPk) — **DVCorg** — comparing model metrics across branches in a pull request: a model quality gate.
- [MLOps Tutorial #4: GitHub Actions with Your Own GPUs](https://www.youtube.com/watch?v=rVq-SCNyxVc) — **DVCorg** — self-hosted GPU runners for continuous training.

**Courses**:
- [Full Stack Deep Learning — the course](https://fullstackdeeplearning.com/course/) — **The Full Stack** — the testing-and-deployment lectures: what a model quality gate looks like in a real pipeline.
- [Machine Learning in Production (MLOps Specialization)](https://www.deeplearning.ai/courses/machine-learning-engineering-for-production-mlops/) — **Andrew Ng, Robert Crowe and Laurence Moroney (DeepLearning.AI)** — deployment pipelines and model validation as a structured course.
- [Made With ML](https://madewithml.com/) — **Goku Mohandas** — the course hub; the CI/CD lesson sits on its testing, versioning and orchestration lessons.
- [Made With ML — CI/CD](https://madewithml.com/courses/mlops/cicd/) — **Goku Mohandas** — a complete GitHub Actions pipeline for testing, training and deploying.

**Articles**:
- [CML — Continuous Machine Learning](https://cml.dev/) — **Iterative** — CI/CD patterns purpose-built for ML.
- [Continuous Delivery for Machine Learning (CD4ML)](https://martinfowler.com/articles/cd4ml.html) — **Sato, Wider & Windheuser (martinfowler.com)** — the definitive CD4ML reference and the vocabulary interviewers use.
- [MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — **Google Cloud** — defines CI/CD/CT and the level-2 architecture.
- [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml) — **Google** — testing and launch discipline for production ML.

**Papers**:
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (2015)** — why untested glue code and configuration are the dominant production risk.
- [Machine Learning Operations (MLOps): Overview, Definition, and Architecture](https://arxiv.org/abs/2205.02302) — **Kreuzberger, Kühl & Hirschl (2022)** — the reference architecture that places CI/CD and CT in one system.

**Documentation**:
- [Argo Rollouts — kubectl plugin](https://argo-rollouts.readthedocs.io/en/stable/features/kubectl-plugin/) — **Argo Project (CNCF)** — the `set image` command the pipeline's last step uses to start a canary.
- [CML — Documentation](https://cml.dev/doc) — **Iterative** — continuous ML in CI runners: reports, metrics, cloud GPUs.
- [GitHub Actions documentation](https://docs.github.com/en/actions) — **GitHub** — workflow syntax and the fail-fast step semantics the gate relies on.

**Books**:
- [*Designing Machine Learning Systems* — Ch. 9 "Continual Learning & Test in Production"](https://huyenchip.com/mlops/) — **Chip Huyen** — continuous training, retraining cadence and testing in production.
- [*Machine Learning Engineering* — Ch. 8 "Model Deployment"](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — CI/CD and retraining; read-first chapters online.
