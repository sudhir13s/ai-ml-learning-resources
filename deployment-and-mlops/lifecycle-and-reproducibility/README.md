---
id: "deployment-and-mlops/lifecycle-and-reproducibility"
topic: "Lifecycle and Reproducibility"
level: advanced
built_from: ["ai-ml-orientation", "tools-and-frameworks"]
updated: 2026-09-07
---

# Lifecycle and Reproducibility

> The foundation everything else in MLOps stands on. Before you can automate a pipeline, serve a
> model or roll one back, a run has to be a deterministic function of versioned inputs — pinned
> code, pinned data, pinned environment, recorded randomness — and every experiment has to be
> findable afterwards. These four pages establish that floor.

**Start here:** [ML Lifecycle and MLOps Maturity](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/lifecycle-and-reproducibility/ml-lifecycle-and-mlops-maturity/ml-lifecycle-and-mlops-maturity) — the maturity ladder is the map every other page in this section hangs off.

## Concept index

Each page is a self-contained resource card: a plain-words definition, why it matters in 2026, a
five-step start-here path, and verified courses, videos, papers, articles and books.

### The map

1. [ML Lifecycle and MLOps Maturity](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/lifecycle-and-reproducibility/ml-lifecycle-and-mlops-maturity/ml-lifecycle-and-mlops-maturity) — scope → data → train → evaluate → deploy → monitor as a loop, and the manual/pipeline/CI-CD-CT maturity levels.

### Making a run repeatable

2. [Reproducibility](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/lifecycle-and-reproducibility/reproducibility/reproducibility) — seeds, environments and lineage; the difference between bitwise determinism and scientific reproducibility.

### Making a run findable

3. [Experiment Tracking](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/lifecycle-and-reproducibility/experiment-tracking/experiment-tracking) — logging parameters, metrics, code version and artifacts to a central store with MLflow or Weights & Biases.
4. [Data and Model Versioning](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/lifecycle-and-reproducibility/data-and-model-versioning/data-and-model-versioning) — content-addressed data and model artifacts with DVC or lakeFS; the half of reproducibility Git cannot do.

## Courses (free)

- [Made With ML — MLOps Course](https://madewithml.com/courses/mlops/) — **Goku Mohandas** — the best free end-to-end MLOps course; the versioning and experiment-tracking lessons map one-to-one onto pages 2 to 4.
- [Machine Learning in Production (MLOps Specialization)](https://www.deeplearning.ai/courses/machine-learning-engineering-for-production-mlops/) — **Andrew Ng, Robert Crowe and Laurence Moroney (DeepLearning.AI)** — free to audit; Course 1 is the canonical lifecycle treatment.
- [Full Stack Deep Learning — Course 2022](https://fullstackdeeplearning.com/course/2022/) — **Charles Frye, Sergey Karayev and Josh Tobin** — free lectures on experiment management and reproducible training as part of shipping a product.
- [DVC — Get Started](https://dvc.org/doc/start) — **Iterative** — guided, hands-on introduction to versioning data and models alongside code.

## Videos

- [MLOps Zoomcamp 1.1 — Introduction](https://www.youtube.com/watch?v=s0uaFZSzwfI) — **DataTalks.Club** — frames the maturity ladder and where versioning sits, at the start of a free project-based course.
- [Versioning Data with DVC](https://www.youtube.com/watch?v=kLKBcPonMYw) — **DVC (Iterative)** — the maintainers' own walkthrough of `dvc add`, `push` and `checkout`.
- [Track Your PyTorch Experiments with Weights & Biases](https://www.youtube.com/watch?v=KESSYZExK44) — **Weights & Biases** — instrumenting a training loop in minutes, from the tool's own team.
- [MLOps Zoomcamp — Experiment Tracking with Weights & Biases](https://www.youtube.com/watch?v=yNyqFMwEyL4) — **DataTalks.Club** — tracking, sweeps and artifacts inside a real project.

## Key Papers

- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (Google, 2015)** — "data dependencies cost more than code dependencies"; the argument for everything on these four pages.
- [MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — **Google Cloud** — the whitepaper that defined the maturity levels this sub-area teaches.
- [Improving Reproducibility in Machine Learning Research](https://arxiv.org/abs/2003.12206) — **Pineau et al. (2020)** — the reproducibility checklist and what it found; why pinning is a scientific requirement, not hygiene.
- [Challenges in Deploying Machine Learning: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes, Urma and Lawrence (2020)** — real deployment failures organized by lifecycle stage.

## Articles / Blogs (free, no paywall)

- [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml) — **Martin Zinkevich (Google)** — 43 practices structured by lifecycle phase; the most quoted document in production ML.
- [MLOps Principles](https://ml-ops.org/content/mlops-principles) — **INNOQ (ml-ops.org)** — a vendor-neutral definition of the lifecycle, automation levels and maturity.
- [MLflow Tracking](https://mlflow.org/docs/latest/tracking/) — **MLflow maintainers** — runs, experiments, autologging and backends, from the canonical reference.
- [DVC — Data Management](https://dvc.org/doc/user-guide/data-management) — **Iterative** — how content-addressed storage and remotes actually work under the pointer files.

## Books (free, with chapters)

- [*Designing Machine Learning Systems* — Ch. 6 "Model Development and Offline Evaluation"](https://huyenchip.com/mlops/) — **Chip Huyen** — versioning and lineage in the definitive modern text; the book is paid, the author's notes and companion code are free.
- [*Machine Learning Engineering* — Ch. 3 "Data Collection and Preparation"](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — data versioning treated as engineering; read-first chapters free.
- [*Site Reliability Engineering* and *The SRE Workbook*](https://sre.google/books/) — **Google** — free online; the release-engineering discipline the ML lifecycle inherits.

## In this platform

- Section index: [MLOps and Deployment](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/readme)
- Next in this section: [Data and Training Platforms](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/data-and-training-platforms/readme) · [Packaging and Serving](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/packaging-and-serving/readme) · [Release and Deployment](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/release-and-deployment/readme) · [Monitoring and Reliability](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/readme) · [Governance and Economics](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/governance-and-economics/readme)
- Where the lifecycle was first described: [The ML Workflow and Lifecycle](/ai-ml/ai-ml-learning-resources/foundations/ai-ml-orientation/the-ml-workflow-and-lifecycle/the-ml-workflow-and-lifecycle)
- The environment discipline this assumes: [Environments and Package Management](/ai-ml/ai-ml-learning-resources/foundations/programming-and-data-foundations/environments-and-package-management/environments-and-package-management)
- What tracking is used to decide: [Cross-Validation](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/cross-validation/cross-validation) · [Error Analysis and Model Debugging](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/error-analysis-and-model-debugging/error-analysis-and-model-debugging)
- Doing it rather than reading it: [Experiment Tracking workflow](/ai-ml/practitioner-workflows/workflow-library/training-and-adaptation/experiment-tracking) · [MLOps and Deployment workflow](/ai-ml/practitioner-workflows/workflow-library/production-lifecycle/mlops-and-deployment)
