---
id: "operations-and-lifecycle/release-and-deployment/rollback-and-recovery-for-ml-systems/references"
topic: "Rollback & Recovery for ML Systems — References"
parent: "operations-and-lifecycle/release-and-deployment/rollback-and-recovery-for-ml-systems"
type: references
updated: 2026-09-13
---

# Rollback and Recovery for ML Systems — references

> Companion link library for **[Rollback and Recovery for ML Systems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/rollback-and-recovery-for-ml-systems/rollback-and-recovery-for-ml-systems)** (the teaching page). Internal links and external sources, grouped by type and alphabetical within each group.

**Start here — suggested path**:

1. **See how rollouts fail** — watch [Full Stack Deep Learning 2022 — Deployment](https://fullstackdeeplearning.com/course/2022/lecture-5-deployment/). *Rollout strategies and what each one does when it goes wrong.*
2. **Start from software practice** — read [Release Engineering](https://sre.google/sre-book/release-engineering/). *Hermetic builds and immutable artifacts, the preconditions for any rollback.*
3. **Get the ML-specific release unit** — read [Continuous Delivery for Machine Learning (CD4ML)](https://martinfowler.com/articles/cd4ml.html). *Code, model and data versioned together so a release is reversible.*
4. **Run the loop** — read [Rollback and Recovery for ML Systems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/rollback-and-recovery-for-ml-systems/rollback-and-recovery-for-ml-systems) and run its replay. *The tuple to restore and the clock an automated trigger beats.*
5. **Automate and measure** — read [Argo Rollouts](https://argo-rollouts.readthedocs.io/en/stable/), then [DORA's four key metrics](https://dora.dev/guides/dora-metrics-four-keys/). *Automatic abort on a metric breach, and the recovery numbers it is judged by.*

**In this platform**:
- [A/B Testing, Shadow and Canary Deployment](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/ab-testing-shadow-and-canary-deployment/ab-testing-shadow-and-canary-deployment) — the rollout this page starts from when it fails.
- [AI Incident Response and Postmortems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/ai-incident-response-and-postmortems/ai-incident-response-and-postmortems) — what happens around the rollback.
- [CI/CD for ML and Continuous Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/cicd-for-ml-and-continuous-training/cicd-for-ml-and-continuous-training) — the pipeline that produced the artifact being reverted.
- [Data and Concept Drift Detection](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/data-and-concept-drift-detection/data-and-concept-drift-detection) — slow degradation that no rollback trigger will catch.
- [Data and Model Versioning](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/data-and-model-versioning/data-and-model-versioning) — immutable versions of every artifact in the tuple.
- [ml-platform](/python/python-production-examples/ml-platform/readme) — the runnable registry and rollout service.
- [Model Monitoring and Observability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability) — the signals a rollback trigger reads.
- [Model Registry and Governance](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/model-registry-and-governance/model-registry-and-governance) — the alias flip that makes a revert a pointer move.
- [Reproducibility](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/reproducibility/reproducibility) — pinning the environment and infrastructure the old version needs.

**Videos**:
- [Full Stack Deep Learning 2022 lecture series](https://www.youtube.com/playlist?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur) — **The Full Stack** — the deployment and monitoring lectures cover staged rollout, rollback triggers and what to watch during a release.
- [Postmortem Culture at Google](https://www.youtube.com/watch?v=qgHWzQ2zcqQ) — **Ramon Medrano Llamas, Google (Conf42)** — how the rollback decision is made under time pressure and what gets recorded afterwards.

**Courses**:
- [Full Stack Deep Learning 2022 — Deployment](https://fullstackdeeplearning.com/course/2022/lecture-5-deployment/) — **Charles Frye, Sergey Karayev & Josh Tobin** — deployment shapes, rollout strategies and how each one fails.
- [Made With ML](https://madewithml.com/) — **Goku Mohandas** — the deployment and continual-learning modules build versioned artifacts and a revertible release path.
- [MLOps principles](https://ml-ops.org/content/mlops-principles) — **INNOQ (Visengeriyeva, Kammer, Bär, Kniesz, Plöd)** — a vendor-neutral reference on versioning code, model and data as one release unit.

**Articles**:
- [BlueGreenDeployment](https://martinfowler.com/bliki/BlueGreenDeployment.html) — **Martin Fowler** — two live environments and one switch.
- [Continuous Delivery for Machine Learning (CD4ML)](https://martinfowler.com/articles/cd4ml.html) — **Sato, Wider & Windheuser (martinfowler.com)** — code, model and data versioned together so a release is reversible.
- [DORA's four key metrics](https://dora.dev/guides/dora-metrics-four-keys/) — **DORA / Google Cloud** — change failure rate and failed-deployment recovery time.
- [MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — **Google Cloud** — the automation level at which automated rollback becomes possible.

**Papers**:
- [Challenges in Deploying Machine Learning: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes, Urma & Lawrence (2020)** — documented deployment and recovery failures, stage by stage.
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (2015, Google)** — entanglement and undeclared consumers: why an ML rollback is not a binary rollback.
- [Machine Learning Operations (MLOps): Overview, Definition, and Architecture](https://arxiv.org/abs/2205.02302) — **Kreuzberger, Kühl & Hirschl (2022)** — the reference architecture naming the versioned artifacts a rollback restores.

**Documentation**:
- [Argo Rollouts](https://argo-rollouts.readthedocs.io/en/stable/) — **Argo Project (CNCF)** — progressive delivery with automated analysis and abort.
- [Feast documentation](https://docs.feast.dev/) — **Feast maintainers** — feature views and schema evolution, the half of a rollback teams forget.
- [KServe — canary rollout](https://kserve.github.io/website/latest/modelserving/v1beta1/rollout/canary/) — **KServe maintainers** — canary and automatic revert applied to model servers.
- [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) — **Kubernetes** — rolling updates and the `kubectl rollout undo` primitive.
- [MLflow Model Registry](https://mlflow.org/docs/latest/model-registry.html) — **MLflow maintainers** — versions and aliases: promoting the previous version as a one-line operation.

**Books**:
- [*Designing Machine Learning Systems* — Ch. 9 "Continual Learning and Test in Production"](https://huyenchip.com/mlops/) — **Chip Huyen** — rollout and rollback of models as a continual-learning problem.
- [*Site Reliability Engineering* — "Emergency Response"](https://sre.google/sre-book/emergency-response/) — **Google SRE** — "roll back first, diagnose second" in practice.
- [*Site Reliability Engineering* — "Release Engineering"](https://sre.google/sre-book/release-engineering/) — **Google SRE** — hermetic builds and immutable artifacts, the preconditions for any rollback.
