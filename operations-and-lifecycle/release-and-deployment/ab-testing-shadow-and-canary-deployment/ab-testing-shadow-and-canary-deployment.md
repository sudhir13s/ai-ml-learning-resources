---
id: "18-mlops/ab-testing-shadow-and-canary-deployment"
topic: "A/B Testing · Shadow & Canary Deployment"
parent: "18-mlops-and-deployment"
level: advanced
built_from: ["model-serving", "model-registry-and-governance"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "A/B Testing · Shadow & Canary Deployment"
minutes: 10
category: release-and-deployment
---

# A/B Testing · Shadow & Canary Deployment
> Strategies for releasing a new model safely, because **offline metrics don't guarantee online wins**.
> **Shadow**: run the new model in parallel, serve nothing — measure risk-free. **Canary**: route a small
> % of live traffic to it, ramp up if healthy. **A/B test**: split traffic and measure the business metric
> that decides the winner. Test in production, without betting the whole house.

**Why it matters:** the "your offline AUC went up — how do you know it's actually better in prod, and how
do you roll it out without risk?" question. Interviewers want the shadow → canary → full-rollout ladder,
when to use each, and the A/B basics (split, primary metric, why offline ≠ online). The deployment
counterpart to monitoring. (The *statistics* of A/B tests live in 01. Foundations — link below.)

**Start here — suggested path:**

1. **Get the ladder** — read [CD4ML: progressive delivery section](https://martinfowler.com/articles/cd4ml.html) for how models are rolled out gradually. *Frames shadow/canary/A-B as one safety continuum.*
2. **Shadow first** — read [SageMaker Shadow Tests](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html). *Mirror live traffic to the challenger, serve none of it — test under real load with zero user risk.*
3. **Then canary** — read [Canary Release](https://martinfowler.com/bliki/CanaryRelease.html), then [Canarying Releases](https://sre.google/workbook/canarying-releases/) in the Google SRE Workbook. *The 1% → 20% → 100% ramp, the metrics that gate each step, and how to size the canary so the signal is statistically real.*
4. **See it automated** — watch [Progressive Delivery Made Easy With Argo Rollouts](https://www.youtube.com/watch?v=C34TJFDsq-s). *Analysis templates that promote or abort a rollout from live metrics, no human in the loop.*
5. **Get the stats right** — for hypothesis tests, power, and CUPED, go to [01. Foundations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme). *MLOps owns the deployment mechanics; Foundations owns the experiment statistics.*

## Courses (free)
- [Made With ML — MLOps Course (deployment strategies)](https://madewithml.com/courses/mlops/) — **Goku Mohandas** — safe rollout within the production workflow.
- [Google — Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml) — **Google** — "measure the metric that matters" and launch discipline.

## Videos
- [Progressive Delivery Made Easy With Argo Rollouts](https://www.youtube.com/watch?v=C34TJFDsq-s) — **CNCF (Kevin Dubois, Red Hat)** — canary and blue/green as a Kubernetes controller, with automated metric analysis deciding promote-or-abort.
- [Testing & Deployment — course overview](https://www.youtube.com/watch?v=Dk-95mt0MLA) — **The Full Stack** — why offline tests never settle the question, and what shipping behind a traffic split buys you.

## Key Papers
- [Challenges in Deploying ML: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes et al. (2020)** — why offline metrics mislead and rollout safety matters.
- [The ML Test Score](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/) — **Breck et al. (Google, 2017)** — "test in production" as part of production readiness.

## Articles / Blogs (free, no paywall)
- [Canary Release](https://martinfowler.com/bliki/CanaryRelease.html) — **Martin Fowler** — the canonical definition of progressive rollout.
- [Continuous Delivery for ML (CD4ML)](https://martinfowler.com/articles/cd4ml.html) — **martinfowler.com** — model rollout inside the CD pipeline.
- [Shadow Tests (SageMaker)](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html) — **AWS** — production shadow-testing mechanics and metrics.
- [Canarying Releases](https://sre.google/workbook/canarying-releases/) — **Google SRE Workbook** — free book chapter on sizing a canary, choosing the evaluation window, and the failure modes of "it looked fine at 1%".
- [Argo Rollouts — Documentation](https://argo-rollouts.readthedocs.io/en/stable/) — **Argo project (CNCF)** — canary/blue-green as a Kubernetes resource, with analysis runs as the promotion gate.

## Books (free, with chapters)
- [Designing Machine Learning Systems — **Ch. 9 "Continual Learning & Test in Production"** (shadow, canary, A/B)](https://huyenchip.com/mlops/) — **Chip Huyen** — the canonical chapter on test-in-prod (author notes free).
- [Machine Learning Engineering — **Ch. 8 "Model Deployment"** (deployment strategies)](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — read-first chapters free.

## In this platform
- Builds on: [09 Model Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-serving/model-serving) · [13 Model Registry & Governance](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/model-registry-and-governance/model-registry-and-governance)
- Next concepts: [12 Data & Concept Drift Detection](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/data-and-concept-drift-detection/data-and-concept-drift-detection) · [07 CI/CD for ML & CT](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/cicd-for-ml-and-continuous-training/cicd-for-ml-and-continuous-training)
- When the canary fails: [Rollback & Recovery for ML Systems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/rollback-and-recovery-for-ml-systems/rollback-and-recovery-for-ml-systems)
- Related concept (covered elsewhere): A/B-test statistics (hypothesis tests, power, CUPED) → [01. Foundations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme)
