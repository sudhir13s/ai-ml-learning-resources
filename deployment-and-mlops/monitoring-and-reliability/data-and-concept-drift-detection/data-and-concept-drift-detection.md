---
id: "18-mlops/data-and-concept-drift-detection"
topic: "Data & Concept Drift Detection"
parent: "18-mlops-and-deployment"
level: advanced
built_from: ["model-monitoring-and-observability", "statistics"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Data & Concept Drift Detection"
minutes: 10
category: monitoring-and-reliability
---

# Data & Concept Drift Detection
> Detecting when the world has moved away from the training distribution. **Data drift**: P(X) changes
> (inputs shift). **Concept drift**: P(Y|X) changes (the input→output relationship shifts). Both quietly
> erode accuracy — drift detection tells you *when to retrain* before users notice.

**Why it matters:** the deep-dive that follows monitoring, and a strong differentiator. Interviewers
want a crisp **data drift vs concept drift** distinction, detection methods (KS test, PSI, Chi-square,
Jensen–Shannon / Wasserstein distance), the **delayed-/no-label problem** (use prediction drift + input
drift as proxies), and the response (alert → root-cause → retrain). The trigger for continuous training.
For large language model (LLM) inputs the same question is asked over **embeddings** — you cannot run a
Kolmogorov–Smirnov (KS) test on free text, so you track drift in the vector space instead.

**Start here — suggested path:**

1. **Nail the definitions** — read [Evidently: What is Data Drift](https://www.evidentlyai.com/ml-in-production/data-drift) and [What is Concept Drift](https://www.evidentlyai.com/ml-in-production/concept-drift). *P(X) vs P(Y|X) — get this distinction exactly right.*
2. **Learn the tests** — read [Evidently: Data Drift Detection Deep Dive](https://learn.evidentlyai.com/ml-observability-course/module-2-ml-monitoring-metrics/data-drift-deep-dive). *KS, population stability index (PSI), Chi-square, Jensen–Shannon/Wasserstein — which test for which data type.*
3. **Detect it in code** — watch [Evidently in Jupyter: data & prediction drift](https://www.youtube.com/watch?v=g0Z2e-IqmmU) and skim [the Evidently metric catalog](https://docs.evidentlyai.com/metrics/all_metrics). *Running the tests and reading the reports.*
4. **Read the theory** — skim [A Survey on Concept Drift Adaptation](https://eprints.bournemouth.ac.uk/22491/). *Drift types (sudden/gradual/recurring) and adaptation strategies — the rigorous backbone.*
5. **Close the loop** — connect drift to retraining via [07 CI/CD for ML & CT](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/release-and-deployment/cicd-for-ml-and-continuous-training/cicd-for-ml-and-continuous-training). *Drift detected → continuous-training pipeline fires.*

## Courses (free)
- [Evidently — ML Observability Course (Module 2: Drift)](https://learn.evidentlyai.com/ml-observability-course/module-2-ml-monitoring-metrics/data-drift-deep-dive) — **Evidently AI** — the statistical drift tests, hands-on.
- [Made With ML — Monitoring](https://madewithml.com/courses/mlops/monitoring/) — **Goku Mohandas** — drift detection as part of production monitoring.

## Videos
- [Use Evidently in Jupyter to Evaluate Data & Prediction Drift](https://www.youtube.com/watch?v=g0Z2e-IqmmU) — **Evidently AI** — running the drift report and interpreting it, by the library's authors.
- [Data Drift & Early Monitoring for ML Models](https://www.youtube.com/watch?v=N12uMO-fj40) — **Datafold (Emeli Dral, Evidently AI)** — drift detection methods and their pitfalls.
- [Deep Dive Into Univariate Drift Detection Methods](https://www.youtube.com/watch?v=ZGQny5KlCbo) — **NannyML** — the statistical tests compared head to head, including when each one cries wolf.
- [Concept Drift Detection with NannyML](https://www.youtube.com/watch?v=kBTty6JTW9Q) — **NannyML** — detecting P(Y|X) change *without labels* via confidence-based performance estimation.

## Key Papers
- [A Survey on Concept Drift Adaptation](https://eprints.bournemouth.ac.uk/22491/) — **Gama et al. (2014)** — the canonical taxonomy of drift types and adaptation methods.
- [Learning under Concept Drift: A Review](https://arxiv.org/abs/1010.4784) — **Žliobaitė (2010)** — foundational survey of drift detection and handling.
- [Challenges in Deploying ML: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes et al. (2020)** — drift-driven degradation in real deployments.

## Articles / Blogs (free, no paywall)
- [What is Data Drift in ML](https://www.evidentlyai.com/ml-in-production/data-drift) — **Evidently AI** — P(X) shift, detection tests, and handling.
- [What is Concept Drift in ML](https://www.evidentlyai.com/ml-in-production/concept-drift) — **Evidently AI** — P(Y|X) shift and how to detect it without fresh labels.
- [Data Drift Detection Deep Dive](https://learn.evidentlyai.com/ml-observability-course/module-2-ml-monitoring-metrics/data-drift-deep-dive) — **Evidently AI** — the statistical tests, compared.
- [Embedding drift detection](https://www.evidentlyai.com/blog/embedding-drift-detection) — **Evidently AI** — the LLM-era method: measure drift in embedding space (model-based, distance, or domain-classifier) when the input is text or images.
- [NannyML Documentation](https://nannyml.readthedocs.io/en/stable/) — **NannyML** — confidence-based performance estimation: estimate the metric that actually matters while labels are still missing.

## Books (free, with chapters)
- [Designing Machine Learning Systems — **Ch. 8 "Data Distribution Shifts & Monitoring"**](https://huyenchip.com/mlops/) — **Chip Huyen** — covariate/label/concept shift and detection (author notes free).
- [Machine Learning Engineering — **Ch. 9 "Monitoring & Maintenance"** (distribution shift)](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — read-first chapters free.

## In this platform
- Builds on: [11 Model Monitoring & Observability](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability)
- Next concepts: [07 CI/CD for ML & CT](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/release-and-deployment/cicd-for-ml-and-continuous-training/cicd-for-ml-and-continuous-training) · [14 A/B Testing · Shadow & Canary](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/release-and-deployment/ab-testing-shadow-and-canary-deployment/ab-testing-shadow-and-canary-deployment)
- Related concept (covered elsewhere): distribution-shift theory & generalization → [01. Foundations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme)
