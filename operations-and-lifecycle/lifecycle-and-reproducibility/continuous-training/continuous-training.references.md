---
id: "18-mlops/continuous-training/references"
topic: "Continuous Training — References"
parent: "18-mlops/continuous-training"
type: references
updated: 2026-09-13
---

# Continuous Training — references

> Companion link library for **[Continuous Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/continuous-training/continuous-training)**. External sources and internal links, grouped by type, alphabetical within each group; everything here is free or open-access.

**Videos**:
- [CI/CD and Continuous Training in ML](https://www.youtube.com/watch?v=DIwtPQN9cus) — **MLOps Community (Coffee Sessions)** — practitioners on what actually triggers a retrain and what they automate versus gate by hand.
- [Machine Learning Model Drift — Concept Drift and Data Drift Explained](https://www.youtube.com/watch?v=QJTRNxUxmuc) — **1littlecoder** — the two drifts told apart in ten minutes, which is the distinction the trigger logic rests on.
- [MLOps Zoomcamp — Introduction](https://www.youtube.com/watch?v=s0uaFZSzwfI) — **DataTalks.Club** — frames the maturity ladder this loop sits at the top of.

**Courses**:
- [Machine Learning in Production (MLOps Specialization)](https://www.deeplearning.ai/courses/machine-learning-engineering-for-production-mlops/) — **Andrew Ng, Robert Crowe and Laurence Moroney (DeepLearning.AI)** — free to audit; the concept-drift and continual-learning lessons are the closest course treatment of this page.
- [Made With ML — MLOps Course](https://madewithml.com/courses/mlops/) — **Goku Mohandas** — the retraining and monitoring lessons, with the pipeline code alongside.

**Articles**:
- [MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — **Google Cloud** — defines the CI/CD/CT maturity levels; level 2 is this page's automated loop.
- [Population Stability Index (PSI) explained](https://mwburke.github.io/data%20science/2018/04/29/population-stability-index.html) — **Matthew Burke** — the derivation and the 0.1/0.2 bands the drift trigger uses.

**Papers**:
- [A Survey on Concept Drift Adaptation](https://dl.acm.org/doi/10.1145/2523813) — **Gama et al. (2014)** — the taxonomy behind "which drift did I just detect, and does it need a retrain."
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (Google, 2015)** — why an unattended model becomes a liability; the argument for automating this loop at all.

**Books**:
- [*Designing Machine Learning Systems* — Ch. 8–9](https://huyenchip.com/books/) — **Chip Huyen** — distribution shifts, monitoring and continual learning; the closest book treatment of the flywheel.
- [*Machine Learning Engineering*](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — read-first chapters free; model maintenance as an engineering discipline.

**In this platform**:
- What a retrain must reproduce: [Reproducibility](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/reproducibility/reproducibility) · [Data and Model Versioning](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/data-and-model-versioning/data-and-model-versioning)
- Where each retrain is recorded and compared: [Experiment Tracking](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/experiment-tracking/experiment-tracking)
- The signal that fires the trigger: [Data and Concept Drift Detection](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/data-and-concept-drift-detection/data-and-concept-drift-detection) · [Model Monitoring and Observability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability)
- The plumbing that runs the loop: [CI/CD for ML and Continuous Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/cicd-for-ml-and-continuous-training/cicd-for-ml-and-continuous-training)
- How a candidate reaches production: [A/B Testing, Shadow and Canary Deployment](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/ab-testing-shadow-and-canary-deployment/ab-testing-shadow-and-canary-deployment) · [Model Registry and Governance](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/model-registry-and-governance/model-registry-and-governance)
- The training recipe each retrain re-runs: [The Training Loop](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining-the-training-loop)
- The runnable service: [ml-platform](/python/python-production-examples/ml-platform/readme)
