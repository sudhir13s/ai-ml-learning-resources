---
id: "18-mlops/data-and-model-versioning/references"
topic: "Data & Model Versioning (DVC · lakeFS) — References"
parent: "18-mlops/data-and-model-versioning"
type: references
updated: 2026-09-13
---

# Data & Model Versioning (DVC · lakeFS) — references

> Companion link library for **[Data & Model Versioning (DVC · lakeFS)](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/data-and-model-versioning/data-and-model-versioning)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group; every entry is from a primary author or a recognized deep explainer, and everything here is free or open-access.

**Videos**:
- [Versioning Data with DVC (Hands-On Tutorial!)](https://www.youtube.com/watch?v=kLKBcPonMYw) — **DVCorg** — the maintainers' own walkthrough of `dvc add/push/checkout`.
- [Machine Learning Pipelines with DVC (Hands-On Tutorial!)](https://www.youtube.com/watch?v=71IGzyH95UY) — **DVCorg** — versioned stages with caching, where data versioning turns into a reproducible pipeline.
- [MLOps Zoomcamp 1.1 — Introduction](https://www.youtube.com/watch?v=s0uaFZSzwfI) — **DataTalksClub** — frames versioning within the MLOps foundation.

**Courses**:
- [Made With ML — Versioning](https://madewithml.com/courses/mlops/versioning/) — **Goku Mohandas** — version code, data, and models together in a project.
- [DVC — Get Started (interactive docs)](https://dvc.org/doc/start) — **Iterative** — guided, hands-on intro to data + model versioning.

**Articles**:
- [DVC — Data Management](https://dvc.org/doc/user-guide/data-management) — **Iterative** — how content-addressed storage + remotes actually work.
- [DVC — Versioning Data & Models](https://dvc.org/doc/use-cases/versioning-data-and-models) — **Iterative** — the data-and-model lineage use case end to end.
- [lakeFS — Data Version Control](https://lakefs.io/data-version-control/) — **lakeFS** — git-like branch/commit/merge for data lakes at scale.
- [lakeFS Documentation](https://docs.lakefs.io/) — **lakeFS (Treeverse)** — the maintainers' reference: zero-copy branching, commits, and merges over S3-class storage.
- [Models on the Hugging Face Hub](https://huggingface.co/docs/hub/models-the-hub) — **Hugging Face** — the de-facto 2026 model store: Git-LFS-backed repos, revisions/tags, and safetensors weights as the versioned artifact.
- [DVC — Get Started: Data Versioning](https://dvc.org/doc/start/data-management/data-versioning) — **Iterative** — the pointer-file workflow: `dvc add`, `push`, `checkout`, `pull`.

**Papers**:
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (2015)** — "data dependencies cost more than code dependencies" — the case for data versioning.
- [Improving Reproducibility in ML Research](https://arxiv.org/abs/2003.12206) — **Pineau et al. (2020)** — pinning data versions as a reproducibility requirement.

**Books**:
- [Designing Machine Learning Systems — **Ch. 6 "Model Development & Offline Evaluation"** (versioning & lineage)](https://huyenchip.com/mlops/) — **Chip Huyen** — author notes/talks free.
- [Machine Learning Engineering — **Ch. 3 "Data Collection & Preparation"** (data versioning)](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — read-first chapters free.

**In this platform**:
- Teaching page (full explanation): [Data & Model Versioning (DVC · lakeFS)](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/data-and-model-versioning/data-and-model-versioning)
- Builds on: [02 Reproducibility](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/reproducibility/reproducibility) · [03 Experiment Tracking](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/experiment-tracking/experiment-tracking)
- Next concepts: [05 Feature Stores](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/feature-stores/feature-stores) · [13 Model Registry & Governance](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/model-registry-and-governance/model-registry-and-governance)
- Related concept (covered elsewhere): data preprocessing & feature engineering → [02. Data_Preprocessing](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/readme)
- The rest of the discipline: [Reproducibility](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/reproducibility/reproducibility) · [Experiment Tracking](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/experiment-tracking/experiment-tracking)
