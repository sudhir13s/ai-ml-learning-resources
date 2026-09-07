---
id: "deployment-and-mlops/release-and-deployment/rollback-and-recovery-for-ml-systems"
topic: "Rollback & Recovery for ML Systems"
level: advanced
built_from: ["cicd-for-ml-and-continuous-training", "ab-testing-shadow-and-canary-deployment"]
leads_to: ["deployment-and-mlops/monitoring-and-reliability/ai-incident-response-and-postmortems"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Rollback & Recovery for ML Systems"
minutes: 15
category: release-and-deployment
---

# Rollback & Recovery for ML Systems
> Rolling back a service means redeploying the previous binary. Rolling back a **model** means
> restoring a *tuple*: model weights **plus** the feature transformations, the feature-store schema,
> the preprocessing code, the prompt or system message, and the configuration that selects among
> them. Miss one element and you have "rolled back" into a combination that was never tested.
> The design goal is a **reversible release**: every artifact immutably versioned, the previous
> version still warm, and one switch that moves traffic back.

**Why it matters:** the mean time to recovery, not the failure rate, is what users experience —
and ML gives you failure modes a web service does not. Interviewers push on the ones that bite:
**training/serving skew** reintroduced by rolling back the model but not the transformation code;
a **feature-store schema migration** that the old model cannot read; a fine-tune that must be
rolled back to a base model whose serving stack has already been upgraded; **cache and state**
(a key-value cache or an embedding index) built by the new version and invalid under the old.
The strong answer names the artifact set, the immutability rule, the traffic switch, and the
**pre-agreed rollback trigger** — a metric and a threshold decided before the rollout, not during it.

**Start here — suggested path:**

1. **Start from software practice** — read [Release Engineering](https://sre.google/sre-book/release-engineering/) — **Google SRE book (Dick, Ashish & Hallowell)**. *Hermetic builds, immutable artifacts and "self-service with a big red button" — the preconditions for any rollback.*
2. **Get the ML-specific pipeline** — read [Continuous Delivery for Machine Learning](https://martinfowler.com/articles/cd4ml.html) — **Danilo Sato, Arif Wider & Christoph Windheuser (martinfowler.com)**. *The three axes — code, model, data — that must all be versioned for a release to be reversible.*
3. **Learn the mechanism** — read [BlueGreenDeployment](https://martinfowler.com/bliki/BlueGreenDeployment.html) — **Martin Fowler**, and the Kubernetes [Deployment rollback documentation](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/). *Two live environments and one switch; the `kubectl rollout undo` primitive underneath most model rollbacks.*
4. **Automate the trigger** — read [Argo Rollouts](https://argo-rollouts.readthedocs.io/en/stable/) — **Argo Project (CNCF)**, and [KServe canary rollout](https://kserve.github.io/website/latest/modelserving/v1beta1/rollout/canary/) — **KServe maintainers**. *Analysis templates that abort and revert automatically on a metric breach, applied to model servers.*
5. **Measure whether it works** — read [DORA's four key metrics](https://dora.dev/guides/dora-metrics-four-keys/) — **DORA / Google Cloud**. *Change failure rate and failed-deployment recovery time are the two numbers a rollback story is judged by.*

## Courses (free)

- [Made With ML](https://madewithml.com/) — **Goku Mohandas** — the deployment and continual-learning modules build versioned artifacts and a revertible release path in a real project.
- [Full Stack Deep Learning 2022 — Deployment](https://fullstackdeeplearning.com/course/2022/lecture-5-deployment/) — **Charles Frye, Sergey Karayev & Josh Tobin** — free lecture with video; deployment shapes, rollout strategies and how each one fails.
- [MLOps principles](https://ml-ops.org/content/mlops-principles) — **INNOQ (Visengeriyeva, Kammer, Bär, Kniesz, Plöd)** — an open, vendor-neutral reference on versioning code, model and data as one release unit.

## Videos

- [Full Stack Deep Learning 2022 lecture series](https://www.youtube.com/playlist?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur) — **The Full Stack** — the deployment and monitoring lectures cover staged rollout, rollback triggers and what to watch during a release.
- [Postmortem Culture at Google](https://www.youtube.com/watch?v=qgHWzQ2zcqQ) — **Ramon Medrano Llamas, Google (Conf42)** — how the rollback decision is made under time pressure and what gets recorded afterwards.

## Key Papers

- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (2015, Google)** — entanglement, undeclared consumers and feedback loops: precisely why an ML rollback is not a binary rollback.
- [Challenges in Deploying Machine Learning: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes, Urma & Lawrence (2020)** — documented deployment and recovery failures across industries, stage by stage.
- [Machine Learning Operations (MLOps): Overview, Definition, and Architecture](https://arxiv.org/abs/2205.02302) — **Kreuzberger, Kühl & Hirschl (2022)** — the reference architecture that names the versioned artifacts a rollback has to restore.

## Articles / Blogs (free, no paywall)

- [Continuous Delivery for Machine Learning (CD4ML)](https://martinfowler.com/articles/cd4ml.html) — **Sato, Wider & Windheuser** — the canonical article on making an ML release reproducible and therefore reversible.
- [Release Engineering](https://sre.google/sre-book/release-engineering/) and [Emergency Response](https://sre.google/sre-book/emergency-response/) — **Google SRE book** — free chapters: hermetic builds, and what "roll back first, diagnose second" means in practice.
- [MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — **Google Cloud** — the MLOps level 0/1/2 model; level 2 is where automated rollback becomes possible.
- [MLflow Model Registry](https://mlflow.org/docs/latest/model-registry.html) — **MLflow maintainers** — versions, aliases and stage transitions: the mechanism that makes "promote the previous version" a one-line operation.
- [Feast documentation](https://docs.feast.dev/) — **Feast maintainers** — feature views and schema evolution; the half of the rollback that teams forget until it breaks.
- [Argo Rollouts](https://argo-rollouts.readthedocs.io/en/stable/) — **Argo Project (CNCF)** — progressive delivery with automated analysis and abort; the standard open-source implementation of an automatic revert.

## Books (free, with chapters)

- [*Site Reliability Engineering* — Ch. 8 "Release Engineering" and Ch. 14 "Managing Incidents"](https://sre.google/books/) — **Google** — the full books are free to read online; the source of most rollback discipline in the industry.
- [*Designing Machine Learning Systems* — Ch. 9 "Continual Learning and Test in Production"](https://huyenchip.com/mlops/) — **Chip Huyen** — rollout and rollback of models as a continual-learning problem (author notes free).

## In this platform

- Builds on: [CI/CD for ML & Continuous Training](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/release-and-deployment/cicd-for-ml-and-continuous-training/cicd-for-ml-and-continuous-training) — the pipeline that produced the artifact you are reverting
- Canary, shadow and A/B rollout are owned elsewhere: [A/B Testing, Shadow & Canary Deployment](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/release-and-deployment/ab-testing-shadow-and-canary-deployment/ab-testing-shadow-and-canary-deployment) — this page starts where the canary fails
- The artifact store that makes a revert one command: [Model Registry & Governance](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/governance-and-economics/model-registry-and-governance/model-registry-and-governance) · [Data & Model Versioning](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/lifecycle-and-reproducibility/data-and-model-versioning/data-and-model-versioning) · [Reproducibility](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/lifecycle-and-reproducibility/reproducibility/reproducibility)
- What tells you to roll back: [Model Monitoring & Observability](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability) · [Data & Concept Drift Detection](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/data-and-concept-drift-detection/data-and-concept-drift-detection)
- What happens around the rollback: [AI Incident Response & Postmortems](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/ai-incident-response-and-postmortems/ai-incident-response-and-postmortems)
