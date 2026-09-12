---
id: "18-mlops/reproducibility/references"
topic: "Reproducibility (seeds, environments, lineage) — References"
parent: "18-mlops/reproducibility"
type: references
updated: 2026-09-13
---

# Reproducibility (seeds, environments, lineage) — references and further reading

> Companion link library for **[Reproducibility (seeds, environments, lineage)](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/reproducibility/reproducibility)** (the teaching page). External sources and internal links, grouped by type, best-first; every entry is from a primary author or a recognized deep explainer, and everything here is free or open-access.

**Start here — suggested path:**

1. **See the problem** — watch [Joelle Pineau: Reproducible, Reusable, Robust ML](https://www.youtube.com/watch?v=wVkViYY_fwA). *The reproducibility crisis framing that motivates every practice below.*
2. **Get the checklist** — read [CMU ML Blog: Reproducibility](https://blog.ml.cmu.edu/2020/08/31/5-reproducibility/) and the [ML Reproducibility Checklist (paper)](https://arxiv.org/abs/2003.12206). *Concrete things to pin: code, data, environment, seeds, compute.*
3. **Separate the layers** — read [The Gradient: Independently Reproducible ML](https://thegradient.pub/independently-reproducible-machine-learning/). *Distinguishes "re-run my code" from "someone reproduces my result" — interviewers love this distinction.*
4. **Pin the environment** — read [Made With ML: Versioning](https://madewithml.com/courses/mlops/versioning/) and pin deps + data + model. *Turns the principles into code + DVC + a reproducible run.*
5. **Containerize it** — make the run a deterministic function of a pinned image; see [08 Model Packaging & Containerization](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-packaging-and-containerization/model-packaging-and-containerization). *Environment parity is the last reproducibility gap.*

**Videos**:
- [Reproducible, Reusable, and Robust Reinforcement Learning](https://www.youtube.com/watch?v=wVkViYY_fwA) — **Institute for Advanced Study (Joelle Pineau)** — the keynote that defined the ML reproducibility agenda.
- [2022 Toronto Workshop on Reproducibility — Joelle Pineau](https://www.youtube.com/watch?v=e9CujtFbmmQ) — **Rohan Alexander (workshop host)** — practical guidelines: checklists, code release, variance reporting.
- [MLOps Zoomcamp 1.1 — Introduction](https://www.youtube.com/watch?v=s0uaFZSzwfI) — **DataTalksClub** — frames why reproducibility + tracking + versioning are the MLOps foundation.
- [Versioning Data with DVC (Hands-On)](https://www.youtube.com/watch?v=kLKBcPonMYw) — **DVCorg** — pinning data + models to a Git commit, the practical core of lineage.

**Courses (free)**:
- [Made With ML — Versioning & Reproducibility](https://madewithml.com/courses/mlops/versioning/) — **Goku Mohandas** — pin code, data, and models so a run is reproducible end-to-end.
- [Full Stack Deep Learning — Course 2022](https://fullstackdeeplearning.com/course/2022/) — **The Full Stack** — experiment management and reproducible training as part of shipping ML.

**Articles / blogs (free, no paywall)**:
- [5 — Reproducibility](https://blog.ml.cmu.edu/2020/08/31/5-reproducibility/) — **CMU ML Blog** — clear breakdown of method/data/code reproducibility and how to achieve each.
- [Independently Reproducible Machine Learning](https://thegradient.pub/independently-reproducible-machine-learning/) — **The Gradient** — the spectrum from "re-runs" to "independently reproducible."
- [The reproducibility crisis in ML-based science (Princeton)](https://reproducible.cs.princeton.edu/) — **Kapoor & Narayanan** — leakage and pitfalls that silently break reproducibility.
- [PyTorch — Reproducibility notes](https://pytorch.org/docs/stable/notes/randomness.html) — **PyTorch maintainers** — what is and isn't deterministic: seeds, CUDA kernels, data-loader workers, `use_deterministic_algorithms`.
- [Hydra — configuration management](https://hydra.cc/docs/intro/) — **Hydra maintainers (Meta)** — composable, overridable configs; the one-source-of-truth pattern with command-line overrides.

**Key papers**:
- [Improving Reproducibility in ML Research (NeurIPS 2019 Reproducibility Program)](https://arxiv.org/abs/2003.12206) — **Pineau et al. (2020)** — the reproducibility checklist and what conferences now require.
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (2015)** — config debt and undeclared consumers — direct enemies of reproducibility.
- [Challenges in Deploying ML: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes et al. (2020)** — real failures where lost lineage broke production systems.

**Books (free chapters)**:
- [Designing Machine Learning Systems — **Ch. 6 "Model Development & Offline Evaluation"** (experiment tracking, versioning, reproducibility)](https://huyenchip.com/mlops/) — **Chip Huyen** — author's notes/talks free.
- [Machine Learning Engineering — **Ch. 5–6** (experiment management & reproducible training)](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — read-first chapters free online.

**In this platform**:
- Teaching page (full explanation): [Reproducibility (seeds, environments, lineage)](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/reproducibility/reproducibility)
- Builds on: [01 ML Lifecycle & MLOps Maturity](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/ml-lifecycle-and-mlops-maturity/ml-lifecycle-and-mlops-maturity)
- Next concepts: [03 Experiment Tracking](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/experiment-tracking/experiment-tracking) · [04 Data & Model Versioning](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/data-and-model-versioning/data-and-model-versioning) · [08 Model Packaging & Containerization](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-packaging-and-containerization/model-packaging-and-containerization)
- The knobs the config pins: [AdamW — decoupled weight decay](/ai-ml/ai-ml-intuitions/learning-and-optimization/adaptive-optimization/adamw-intuition) · [Learning rate schedules](/ai-ml/ai-ml-intuitions/learning-and-optimization/adaptive-optimization/learning-rate-schedules-intuition)
- Why a single seed is not a result: [Bias-variance and generalization](/ai-ml/ai-ml-intuitions/objectives-and-evaluation/generalization/bias-variance-tradeoff-intuition)
