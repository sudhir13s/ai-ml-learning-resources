---
id: "operations-and-lifecycle/release-and-deployment"
topic: "Release and Deployment"
level: advanced
built_from: ["packaging-and-serving", "lifecycle-and-reproducibility"]
updated: 2026-09-07
---

# Release and Deployment

> Offline metrics do not guarantee an online win, so releasing a model is a controlled experiment
> rather than a deploy. These three pages cover the automation that builds and validates a
> candidate, the rollout strategies that let you learn from production traffic without betting
> the whole service, and the recovery path — which for machine learning means restoring a tuple,
> not a binary.

**Start here:** [CI/CD for ML and Continuous Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/cicd-for-ml-and-continuous-training/cicd-for-ml-and-continuous-training) — the automation has to exist before shadow, canary or rollback are anything but manual heroics.

## Concept index

Each page is a self-contained resource card: a plain-words definition, why it matters in 2026, a
five-step start-here path, and verified courses, videos, papers, articles and books.

### Building the candidate

1. [CI/CD for ML and Continuous Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/cicd-for-ml-and-continuous-training/cicd-for-ml-and-continuous-training) — DevOps continuous integration and delivery plus the third loop unique to ML: retrain, validate and redeploy as data arrives.

### Releasing it safely

2. [A/B Testing, Shadow and Canary Deployment](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/ab-testing-shadow-and-canary-deployment/ab-testing-shadow-and-canary-deployment) — mirror traffic and serve nothing, ramp a small percentage, or split and measure the business metric.

### Undoing it

3. [Rollback and Recovery for ML Systems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/rollback-and-recovery-for-ml-systems/rollback-and-recovery-for-ml-systems) — weights plus feature transformations plus schema plus preprocessing plus prompt plus config; miss one and you have rolled back into an untested combination.

## Courses (free)

- [Made With ML — CI/CD](https://madewithml.com/courses/mlops/cicd/) — **Goku Mohandas** — a complete GitHub Actions pipeline that tests, trains and deploys, in a real repository.
- [Full Stack Deep Learning 2022 — Deployment](https://fullstackdeeplearning.com/course/2022/lecture-5-deployment/) — **Charles Frye, Sergey Karayev and Josh Tobin** — free lecture with video on deployment shapes and rollout strategy.
- [CML documentation](https://cml.dev/doc) — **Iterative** — continuous machine learning inside ordinary CI runners: metric reports on pull requests, cloud GPU runners.
- [MLOps principles](https://ml-ops.org/content/mlops-principles) — **INNOQ (Visengeriyeva, Kammer, Bär, Kniesz and Plöd)** — the open vendor-neutral reference on versioning code, data and model as one release.

## Videos

- [Full Stack Deep Learning 2022 lecture series](https://www.youtube.com/playlist?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur) — **The Full Stack** — the deployment, testing and troubleshooting lectures, from practitioners who shipped these systems.
- [MLOps Tutorial #1: Intro to Continuous Integration for ML](https://www.youtube.com/watch?v=9BgIDqAzfuA) — **DVC (Iterative)** — CI adapted for the data-and-model half of the release.
- [MLOps Tutorial #3: Track ML Models with Git and GitHub Actions](https://www.youtube.com/watch?v=xPncjKH6SPk) — **DVC (Iterative)** — automated model comparison and quality gates on a pull request.
- [Postmortem Culture at Google](https://www.youtube.com/watch?v=qgHWzQ2zcqQ) — **Ramon Medrano Llamas (Google)** — how the rollback decision is actually made under time pressure.

## Key Papers

- [The ML Test Score: A Rubric for ML Production Readiness](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/) — **Breck et al. (Google, 2017)** — 28 concrete tests; "test in production" as an explicit readiness criterion.
- [MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) — **Google Cloud** — defines continuous integration, delivery and training, and the level-2 architecture that makes automated rollback possible.
- [Challenges in Deploying Machine Learning: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes, Urma and Lawrence (2020)** — why offline metrics mislead, documented across real deployments.
- [Machine Learning Operations (MLOps): Overview, Definition, and Architecture](https://arxiv.org/abs/2205.02302) — **Kreuzberger, Kühl and Hirschl (2022)** — the reference architecture that names the versioned artifacts a rollback has to restore together.

## Articles / Blogs (free, no paywall)

- [Continuous Delivery for Machine Learning](https://martinfowler.com/articles/cd4ml.html) — **Sato, Wider and Windheuser (martinfowler.com)** — code, model and data versioned as one reversible release; the canonical write-up.
- [Canary Release](https://martinfowler.com/bliki/CanaryRelease.html) — **Martin Fowler** — the definition progressive rollout is measured against.
- [Shadow tests](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html) — **AWS** — the mechanics of mirroring production traffic and which metrics to compare.
- [Release Engineering](https://sre.google/sre-book/release-engineering/) — **Google SRE book** — free chapter; hermetic builds, gradual rollout and the discipline the ML release inherits.
- [MLflow Model Registry](https://mlflow.org/docs/latest/model-registry.html) — **MLflow maintainers** — versions, aliases and stage transitions: the mechanism that makes "promote the previous version" a one-line operation.

## Books (free, with chapters)

- [*Designing Machine Learning Systems* — Ch. 9 "Continual Learning and Test in Production"](https://huyenchip.com/mlops/) — **Chip Huyen** — the canonical chapter on shadow, canary and A/B for models; author notes free.
- [*Machine Learning Engineering* — Ch. 8 "Model Deployment"](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — deployment strategies compared; read-first chapters free.
- [*Site Reliability Engineering* — Ch. 8 "Release Engineering" and Ch. 14 "Managing Incidents"](https://sre.google/books/) — **Google** — free online; the source of most rollback discipline in the industry.

## In this platform

- Section index: [Operations and Lifecycle](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/readme)
- Sibling sub-areas: [Lifecycle and Reproducibility](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/readme) · [Data and Training Platforms](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/readme) · [Packaging and Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/readme) · [Monitoring and Reliability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/readme) · [Governance and Economics](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/readme)
- What the rollout is measured with: [Model Monitoring and Observability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability) · [AI Incident Response and Postmortems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/ai-incident-response-and-postmortems/ai-incident-response-and-postmortems)
- What is being restored on rollback: [Data and Model Versioning](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/data-and-model-versioning/data-and-model-versioning) · [Feature Stores](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/feature-stores/feature-stores) · [Model Registry and Governance](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/model-registry-and-governance/model-registry-and-governance)
- Offline evidence that a candidate is worth releasing: [Error Analysis and Model Debugging](/ai-ml/ai-ml-learning-resources/classical-machine-learning/model-selection-and-evaluation/error-analysis-and-model-debugging/error-analysis-and-model-debugging)
- Doing it rather than reading it: [Continuous Training workflow](/ai-ml/practitioner-workflows/operations-and-lifecycle/continuous-training) · [MLOps and Deployment workflow](/ai-ml/practitioner-workflows/operations-and-lifecycle/mlops-and-deployment)
