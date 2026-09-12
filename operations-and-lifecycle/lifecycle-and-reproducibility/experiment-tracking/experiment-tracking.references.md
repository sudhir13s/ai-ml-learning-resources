---
id: "18-mlops/experiment-tracking/references"
topic: "Experiment Tracking (MLflow · Weights & Biases) — References"
parent: "18-mlops/experiment-tracking"
type: references
updated: 2026-09-13
---

# Experiment Tracking (MLflow · Weights & Biases) — references and further reading

> Companion link library for **[Experiment Tracking (MLflow · Weights & Biases)](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/experiment-tracking/experiment-tracking)** (the teaching page). External sources and internal links, grouped by type, best-first; every entry is from a primary author or a recognized deep explainer, and everything here is free or open-access.

**Start here — suggested path:**

1. **Get the mental model** — read [MLflow Tracking docs](https://mlflow.org/docs/latest/tracking/). *Runs / experiments / params / metrics / artifacts — the vocabulary everything else uses.*
2. **Do it end-to-end** — follow [Made With ML: Experiment Tracking](https://madewithml.com/courses/mlops/experiment-tracking/). *Logs a real training loop and compares runs — the fastest path to fluency.*
3. **See a second tool** — watch [MLOps Zoomcamp: W&B Experiment Tracking](https://www.youtube.com/watch?v=yNyqFMwEyL4). *W&B shows the hosted/collaborative flavor; comparing tools sharpens the "why."*
4. **Wire into your workflow** — add tracking to a PyTorch loop with [W&B + PyTorch](https://www.youtube.com/watch?v=KESSYZExK44). *Making logging a one-liner is what makes the habit stick.*
5. **See the 2026 shape** — watch [MLflow 3.0: AI and MLOps](https://www.youtube.com/watch?v=UezTglxJC88) and skim [MLflow GenAI docs](https://mlflow.org/docs/latest/genai/). *Tracking extended to prompts, traces, and LLM-as-judge evaluation runs.*

**Videos**:
- [MLOps Zoomcamp — Experiment Tracking with Weights & Biases](https://www.youtube.com/watch?v=yNyqFMwEyL4) — **DataTalksClub** — hands-on tracking, sweeps, and artifacts with W&B.
- [Track Your PyTorch Experiments with Weights & Biases](https://www.youtube.com/watch?v=KESSYZExK44) — **Weights & Biases** — instrument a training loop in minutes.
- [Using W&B beyond experiment tracking](https://www.youtube.com/watch?v=_2DNYGv3jiM) — **Weights & Biases** — sweeps, artifacts, and reports built on the tracking core.
- [MLflow 3.0: AI and MLOps](https://www.youtube.com/watch?v=UezTglxJC88) — **Databricks** — what MLflow 3 changed: unified tracking for classic runs, prompts, traces, and evaluations.
- [Versioning Data with DVC — Hands-On Tutorial](https://www.youtube.com/watch?v=kLKBcPonMYw) — **DVC (Iterative)** — the data-pointer half of a reproducible run, from the maintainers.

**Courses (free)**:
- [Made With ML — Experiment Tracking](https://madewithml.com/courses/mlops/experiment-tracking/) — **Goku Mohandas** — log, organize, and compare runs in a real project.
- [Made With ML — MLOps Course](https://madewithml.com/courses/mlops/) — **Goku Mohandas** — situates tracking inside the full develop→deploy loop.
- [MLOps Zoomcamp (module 2: experiment tracking)](https://github.com/DataTalksClub/mlops-zoomcamp) — **DataTalksClub** — free cohort course; module 2 builds an MLflow tracking server end to end.

**Articles / blogs (free, no paywall)**:
- [MLflow Tracking](https://mlflow.org/docs/latest/tracking/) — **MLflow** — the canonical reference: runs, experiments, autologging, backends.
- [W&B Experiment Tracking](https://wandb.ai/site/experiment-tracking/) — **Weights & Biases** — the hosted-tracking model with collaboration and sweeps.
- [MLflow Quickstart / Getting Started](https://mlflow.org/docs/latest/index.html) — **MLflow** — the four components (Tracking, Projects, Models, Registry) in one page.
- [W&B Weave](https://docs.wandb.ai/weave) — **Weights & Biases** — the same logging habit applied to LLM apps: traces, evaluations, and prompt versions instead of loss curves.
- [Optuna — define-by-run hyperparameter optimization](https://optuna.readthedocs.io/en/stable/) — **Optuna maintainers** — the TPE/Bayesian sweep library behind the convergence chart.
- [TensorBoard — Get started](https://www.tensorflow.org/tensorboard/get_started) — **TensorFlow** — the lightweight metrics visualizer in the tracker comparison.
- [Weights & Biases — Experiment Tracking docs](https://docs.wandb.ai/guides/track) — **Weights & Biases** — the hosted tracker's API: init, config, log, artifacts.
- [PyTorch — Reproducibility notes](https://pytorch.org/docs/stable/notes/randomness.html) — **PyTorch maintainers** — what a seed does and does not fix.

**Key papers**:
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (2015)** — why ad-hoc experimentation accrues debt; motivates systematic tracking.
- [Improving Reproducibility in ML Research](https://arxiv.org/abs/2003.12206) — **Pineau et al. (2020)** — what to log so a result is reproducible (params, seeds, env).
- [Random Search for Hyper-Parameter Optimization](https://www.jmlr.org/papers/v13/bergstra12a.html) — **Bergstra & Bengio (2012)** — why random beats grid: only a few hyperparameters matter, and random covers them densely.
- [Algorithms for Hyper-Parameter Optimization](https://papers.nips.cc/paper/2011/hash/86e8f7ab32cfd12577bc2619bc635690-Abstract.html) — **Bergstra et al. (2011)** — the Tree-structured Parzen Estimator behind Optuna's Bayesian search.

**Books (free chapters)**:
- [Designing Machine Learning Systems — **Ch. 6 "Model Development & Offline Evaluation"**](https://huyenchip.com/mlops/) — **Chip Huyen** — experiment tracking and versioning in context (author notes free).
- [Machine Learning Engineering — **Ch. 5 "Supervised Model Training"** (experiment management)](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — read-first chapters free.

**In this platform**:
- Teaching page (full explanation): [Experiment Tracking (MLflow · Weights & Biases)](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/experiment-tracking/experiment-tracking)
- Builds on: [01 ML Lifecycle & MLOps Maturity](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/ml-lifecycle-and-mlops-maturity/ml-lifecycle-and-mlops-maturity) · [02 Reproducibility](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/reproducibility/reproducibility)
- Next concepts: [04 Data & Model Versioning](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/data-and-model-versioning/data-and-model-versioning) · [13 Model Registry & Governance](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/model-registry-and-governance/model-registry-and-governance)
- The other half of the discipline: [Reproducibility](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/reproducibility/reproducibility) · [Data and Model Versioning](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/data-and-model-versioning/data-and-model-versioning) · [Model Registry and Governance](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/model-registry-and-governance/model-registry-and-governance)
- The knobs a sweep tunes: [AdamW — decoupled weight decay](/ai-ml/ai-ml-intuitions/learning-and-optimization/adaptive-optimization/adamw-intuition) · [Learning rate schedules](/ai-ml/ai-ml-intuitions/learning-and-optimization/adaptive-optimization/learning-rate-schedules-intuition) · [L1 and L2 regularization](/ai-ml/ai-ml-intuitions/learning-and-optimization/objective-shaping/l1-and-l2-regularization-intuition)
- Why the sweep optimizes a held-out metric: [Bias-variance and generalization](/ai-ml/ai-ml-intuitions/objectives-and-evaluation/generalization/bias-variance-tradeoff-intuition)
- Doing it in an application stack: [Evaluation and Benchmarking workflow](/ai-ml/practitioner-workflows/evaluation-and-safety/evaluation-and-benchmarking/evaluation-and-benchmarking) · [Data Preparation workflow](/ai-ml/practitioner-workflows/data-and-inputs/data-preparation)
