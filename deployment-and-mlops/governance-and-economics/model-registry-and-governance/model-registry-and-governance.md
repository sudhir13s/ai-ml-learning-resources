---
id: "18-mlops/model-registry-and-governance"
topic: "Model Registry & Governance"
parent: "18-mlops-and-deployment"
level: advanced
built_from: ["experiment-tracking", "ml-lifecycle"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Model Registry & Governance"
minutes: 10
category: governance-and-economics
---

# Model Registry & Governance
> A central, versioned store for trained models with stage transitions (staging → production → archived),
> lineage, approvals, and metadata. Governance adds the controls around it: who can promote a model, what
> documentation it carries (model cards), audit trails, and compliance. The control plane between "trained"
> and "deployed."

**Why it matters:** "how do you manage which model version is in production, and roll back?" Interviewers
want the registry's role (single source of truth, stage transitions, lineage back to the run + data),
how it gates deployment (approvals, quality checks), and governance/responsible-AI concerns (model cards,
auditability, access control). Since 2025 the compliance half is no longer optional in Europe: the
**EU AI Act** phases in obligations for general-purpose and high-risk AI systems through 2026–27
(technical documentation, logging, human oversight), and the **NIST AI Risk Management Framework (AI RMF)**
is the voluntary US counterpart most enterprises map to. Sits between experiment tracking and serving.

**Start here — suggested path:**

1. **Get the registry concept** — read [MLflow Model Registry](https://mlflow.org/docs/latest/ml/model-registry/). *Registered models, versions, aliases/stages, lineage — the core data model.*
2. **See the workflow** — watch [MLflow 3.0: AI and MLOps](https://www.youtube.com/watch?v=UezTglxJC88). *How promotion, aliases, and evaluation results hang together in the current version.*
3. **See the other registry you already use** — read [Models on the Hub](https://huggingface.co/docs/hub/models-the-hub) and [gated models](https://huggingface.co/docs/hub/models-gated). *Revisions, access requests, and audit trails — a registry with governance built into distribution.*
4. **Add governance** — read [Model Cards (paper)](https://arxiv.org/abs/1810.03993) and the [Hugging Face model card spec](https://huggingface.co/docs/hub/model-cards). *Documentation, intended use, and limitations — the governance layer, in the format the ecosystem actually publishes.*
5. **Meet the rulebook** — skim the [NIST AI RMF 1.0](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf) (Govern/Map/Measure/Manage) and the [EU AI Act framework page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai). *What an auditor will ask your registry to prove.*

## Courses (free)
- [MLflow — Model Registry docs](https://mlflow.org/docs/latest/ml/model-registry/) — **MLflow** — registry concepts, stages, and APIs.
- [Made With ML — MLOps Course](https://madewithml.com/courses/mlops/) — **Goku Mohandas** — model management within the production lifecycle.

## Videos
- [MLflow 3.0: AI and MLOps](https://www.youtube.com/watch?v=UezTglxJC88) — **Databricks** — the current registry: versions, aliases, linked evaluation runs, and deployment gates.
- [Evaluation-Driven Development with MLflow 3.0](https://www.youtube.com/watch?v=7Q2Z9CYvdRc) — **AAIF Live** — promotion decided by recorded evaluations rather than a human clicking "production".

## Key Papers
- [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993) — **Mitchell et al. (2019)** — the standard for documenting a model's intended use, performance, and limitations.
- [The ML Test Score: A Rubric for Production Readiness](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/) — **Breck et al. (Google, 2017)** — what to verify before promoting a model.
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (2015)** — undeclared consumers and versioning debt that governance addresses.

## Articles / Blogs (free, no paywall)
- [MLflow Model Registry](https://mlflow.org/docs/latest/model-registry/) — **MLflow** — the canonical reference for registry workflows.
- [Model Cards on the Hugging Face Hub](https://huggingface.co/docs/hub/model-cards) — **Hugging Face** — the model-card spec the open ecosystem publishes against, metadata fields included.
- [Gated models](https://huggingface.co/docs/hub/models-gated) — **Hugging Face** — access requests, licence acceptance, and audit logs as a distribution-level governance control.
- [NIST AI Risk Management Framework 1.0](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf) — **NIST** — the Govern/Map/Measure/Manage structure most enterprise AI governance programmes are written against.
- [EU regulatory framework for AI](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) — **European Commission** — the primary source on risk tiers and the 2025–27 obligation timeline for the AI Act.
- [Best Practices for ML on Google Cloud](https://cloud.google.com/architecture/ml-on-gcp-best-practices) — **Google Cloud** — model management, lineage, and governance practices.

## Books (free, with chapters)
- [Designing Machine Learning Systems — **Ch. 6 "Model Development"** & **Ch. 11 "The Human Side of ML"** (governance/responsible AI)](https://huyenchip.com/mlops/) — **Chip Huyen** — author notes/talks free.
- [Machine Learning Engineering — **Ch. 8–9** (deployment, versioning & maintenance)](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — read-first chapters free.

## In this platform
- Builds on: [03 Experiment Tracking](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/lifecycle-and-reproducibility/experiment-tracking/experiment-tracking) · [04 Data & Model Versioning](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/lifecycle-and-reproducibility/data-and-model-versioning/data-and-model-versioning)
- The registry is what makes an undo possible: [Rollback & Recovery for ML Systems](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/release-and-deployment/rollback-and-recovery-for-ml-systems/rollback-and-recovery-for-ml-systems)
- Next concepts: [14 A/B Testing · Shadow & Canary](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/release-and-deployment/ab-testing-shadow-and-canary-deployment/ab-testing-shadow-and-canary-deployment) · [11 Model Monitoring & Observability](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability)
