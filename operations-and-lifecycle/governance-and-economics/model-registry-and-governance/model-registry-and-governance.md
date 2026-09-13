---
id: "18-mlops/model-registry-and-governance"
topic: "Model Registry & Governance"
parent: "18-mlops-and-deployment"
level: advanced
built_from: ["experiment-tracking", "ml-lifecycle"]
interview_frequency: medium
template: concept-deep
updated: 2026-09-13
tier: standard
est_minutes: 25
core_idea: "In production a model is a name, a version and a stage — with lineage back to the run that produced it and an approval gate in front of every promotion."
title: "Model Registry & Governance"
minutes: 25
category: governance-and-economics
---

# Model Registry and Governance: a model is a name, a version and a stage
> A central, versioned store for trained models, with stage transitions, lineage, approvals
> and metadata. Governance adds the controls around it: who may promote, what documentation
> travels with the model, and what gets audited.

**Why it matters:** "how do you manage which model version is in production, and roll back?"

- **What gets probed:** the registry as single source of truth, stage transitions, lineage back to the run and data, and how it gates deployment.
- **The governance half:** model cards, audit trails and access control.
- **Why it is no longer optional:** the **EU AI Act** phases in documentation, logging and human-oversight obligations through 2026–27.
  - The **NIST AI Risk Management Framework (AI RMF)** is the voluntary US counterpart most enterprises map to.

A [hyperparameter sweep](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/experiment-tracking/experiment-tracking#hyperparameter-sweeps-why-random-beats-grid) produces a winner. The registry is how you **find it again next month**.

- Each entry has a **name**, a **version number**, the **run** that produced it, and a lifecycle **stage**.
- Typical stages: `Staging`, `Production`, `Archived`.

```mermaid
graph LR
    SWEEP(["sweep winner<br/>val_loss=0.63"]):::run --> REG[("model registry")]:::reg
    REG --> V1(["support-bot v1<br/>Archived"]):::archived
    REG --> V2(["support-bot v2<br/>Production"]):::prod
    REG --> V3(["support-bot v3<br/>Staging"]):::staging
    V2 -.->|"links back to"| RUN(["run + config + data version<br/>that produced it"]):::traceln

    classDef run fill:#7A6528,stroke:#6A5518,color:#fff
    classDef reg fill:#3A6B96,stroke:#2A5B86,color:#fff
    classDef archived fill:#4A5B6E,stroke:#3A4B5E,color:#fff
    classDef prod fill:#2E7A5A,stroke:#1E6A4A,color:#fff
    classDef staging fill:#7D5A2C,stroke:#6D4A1C,color:#fff
    classDef traceln fill:#5D4A8A,stroke:#4D3A7A,color:#fff
```

The diagram carries two ideas:

- **One name, many immutable versions,** each tagged with a stage.
- **The dashed arrow** is what a folder of files cannot give you: every version traces back to the exact run, config and data.

### Why a registry, not a folder of `.pt` files

The registry solves three problems that `model_final_v2_REALLY_final.pt` cannot:

- **Traceability.** Every registered version links back to the **run** that created it — its config, metrics, seed and data version. "What produced production v2?" is one click.
- **Lifecycle.** Promoting from `Staging` to `Production` is an explicit, auditable transition — not a copy of a file with a new name. Rollback is "promote the previous version", not "find the right backup".
- **A clean serving contract.** The inference service loads `support-bot@Production` by name, not by a hardcoded path.

This is where the registry hands off to **[Packaging and Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/readme)**: serving pulls the production version by name.

- Our sweep winner stops being `support-bot.pt` on a laptop and becomes `support-bot v3 @Staging`.
- The day it is promoted, serving picks it up by name, with no path change.
- MLflow Model Registry and W&B Model Registry both implement this: **a model is identified by name + version + stage, and each version is immutable and traceable.**

> **Tip:** Never let a model reach production without a registry entry that links back to its run. If you cannot answer "what config, seed and data version produced production?" in one click, you cannot safely roll it back or debug a regression.

> **Note:** The registry is the bridge between research and production. The moment a model has a name and a version, it stops being a file on someone's laptop and becomes an asset the team can reason about, roll back and audit.

## Promotion and rollback are pointer moves

The registry tracks two different things, and conflating them is a classic mistake.

- **Version** — an immutable identity, such as `iris-classifier` version 7, tied to a commit, a data snapshot and an evaluation report. Versions are only ever added.
- **Alias or stage** — a **mutable pointer** saying which version fills a role. Promotion re-points the label; nothing is re-uploaded.

That indirection is what makes rollback **a metadata change, not a rebuild**. For `iris-classifier`, typical figures:

| Way back to v6 | What happens | Typical time |
|---|---|---|
| Rebuild, push and roll out the old version | new image build, registry push, cluster rollout | **~8–12 minutes** |
| Re-point the `production` alias from 7 to 6 | one registry API call | **~2–5 seconds** |

Two orders of magnitude is the reason the registry is a separate layer from deployment: during an incident you want the five-second move. How the rest of the recovery works is in [Rollback and Recovery for ML Systems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/rollback-and-recovery-for-ml-systems/rollback-and-recovery-for-ml-systems).

The MLflow calls, as reference (they need a tracking server):

```python
# REFERENCE: register a packaged model and move the production pointer (MLflow 3).
import mlflow
from mlflow import MlflowClient

# Log the model as a new immutable version under a registered name.
mlflow.sklearn.log_model(model, name="model", registered_model_name="iris-classifier")

client = MlflowClient()
# Promotion re-points an alias to a version. Nothing is re-uploaded.
client.set_registered_model_alias("iris-classifier", alias="production", version="7")

# Serving resolves the alias, never a path.
live_model = mlflow.pyfunc.load_model("models:/iris-classifier@production")

# Rollback is the same call, pointed at the previous version.
client.set_registered_model_alias("iris-classifier", alias="production", version="6")
```

> **Note:**
> - MLflow deprecated the fixed `Staging`/`Production` stages in version 2.9 in favour of **aliases** like `production` or `champion`.
> - A process that already loaded version 7 keeps it in memory; the flip takes effect when serving reloads the alias.

The same pointer also answers the audit question regulated teams eventually get: "prove which model, trained on which data, by which commit, made this decision on this date."

---

## References

The curated link library for this topic — videos, courses, articles, papers, and internal cross-links — lives in a companion file so it can be reused as a standalone reference list:

**→ [Model Registry and Governance — references](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/model-registry-and-governance/model-registry-and-governance#references-further-reading)**
