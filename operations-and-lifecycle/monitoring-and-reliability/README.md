---
id: "operations-and-lifecycle/monitoring-and-reliability"
topic: "Monitoring and Reliability"
level: advanced
built_from: ["packaging-and-serving", "release-and-deployment"]
updated: 2026-09-07
---

# Monitoring and Reliability

> Machine-learning systems fail quietly. Nothing throws, no alert fires, and the predictions
> simply get worse because the world moved. These three pages cover what to watch (operational
> health, data quality, model quality), how to detect the specific failure the world causes, and
> what to do when it happens — including the incident classes that never page anyone.

**Start here:** [Model Monitoring and Observability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability) — the three layers of signal, and the difference between knowing *that* it failed and being able to ask *why*.

## Concept index

Each page is a self-contained resource card: a plain-words definition, why it matters in 2026, a
five-step start-here path, and verified courses, videos, papers, articles and books.

### What to watch

1. [Model Monitoring and Observability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability) — latency, errors and throughput; schema and range checks on inputs; accuracy when labels arrive and proxies when they do not.

### The failure the world causes

2. [Data and Concept Drift Detection](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/data-and-concept-drift-detection/data-and-concept-drift-detection) — P(X) shifting versus P(Y|X) shifting, the statistical tests for each, and the signal that says retrain now.

### When it happens anyway

3. [AI Incident Response and Postmortems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/ai-incident-response-and-postmortems/ai-incident-response-and-postmortems) — detect, declare, command, mitigate, then write blamelessly; plus the ML-specific classes such as silent quality degradation and upstream data outages.

## Courses (free)

- [Evidently — ML Observability Course](https://learn.evidentlyai.com/ml-observability-course/module-1-introduction/ml-monitoring-observability) — **Evidently AI** — a free end-to-end open course on monitoring and observability, with a [drift deep dive](https://learn.evidentlyai.com/ml-observability-course/module-2-ml-monitoring-metrics/data-drift-deep-dive) that is the best free treatment of the statistical tests.
- [Made With ML — Monitoring](https://madewithml.com/courses/mlops/monitoring/) — **Goku Mohandas** — builds the detection half inside a real project: the alerts a runbook responds to.
- [PagerDuty Incident Response](https://response.pagerduty.com/) — **PagerDuty** — a complete, openly licensed on-call curriculum: before, during and after an incident, with severity definitions you can adopt as written.
- [SREcon proceedings and recordings](https://www.usenix.org/srecon) — **USENIX** — the practitioner conference for incident response; talks and papers are free and increasingly cover ML and LLM serving.

## Videos

- [Data Drift and Early Monitoring for ML Models](https://www.youtube.com/watch?v=N12uMO-fj40) — **Emeli Dral (Evidently AI)** — drift detection methods and the pitfalls, from someone who implemented them.
- [Drift Monitoring and Evaluation for LLM Apps](https://www.youtube.com/watch?v=eQ6cGzDUtMU) — **Evidently AI** — extending drift detection to embeddings and generated text, where there is no accuracy to fall back on.
- [Postmortem Culture at Google](https://www.youtube.com/watch?v=qgHWzQ2zcqQ) — **Ramon Medrano Llamas (Google)** — how blameless postmortems are actually run and reviewed inside Google.
- [Full Stack Deep Learning 2022 lecture series](https://www.youtube.com/playlist?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur) — **The Full Stack** — the troubleshooting, testing and monitoring lectures: the ML-specific complement to standard site reliability engineering.

## Key Papers

- [A Survey on Concept Drift Adaptation](https://eprints.bournemouth.ac.uk/22491/) — **Gama, Žliobaitė, Bifet, Pechenizkiy and Bouchachia (2014)** — the canonical taxonomy of drift types and adaptation methods.
- [Learning under Concept Drift: A Review](https://arxiv.org/abs/1010.4784) — **Indrė Žliobaitė (2010)** — the foundational survey of drift detection, still the clearest statement of the problem.
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (Google, 2015)** — feedback loops and undeclared consumers: the mechanisms behind the incidents these pages describe.
- [Challenges in Deploying Machine Learning: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes, Urma and Lawrence (2020)** — a catalogue of real post-deployment failures, usable directly as an incident-class list.
- [Machine Learning Operations (MLOps): Overview, Definition, and Architecture](https://arxiv.org/abs/2205.02302) — **Kreuzberger, Kühl and Hirschl (2022)** — where monitoring, alerting and the human roles sit in a reference architecture.

## Articles / Blogs (free, no paywall)

- [Data Distribution Shifts and Monitoring](https://huyenchip.com/2022/02/07/data-distribution-shifts-and-monitoring.html) — **Chip Huyen** — a chapter-length free article; the clearest map of shift types and what to monitor for each.
- [Managing Incidents](https://sre.google/sre-book/managing-incidents/) — **Google SRE book** — free chapter; incident command, roles and handoffs, with [Emergency Response](https://sre.google/sre-book/emergency-response/) alongside.
- [A postmortem of three recent issues](https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues) — **Anthropic (2025)** — a rare public, technical postmortem of LLM-serving bugs; read it as a worked example of the artifact page 3 asks you to produce.
- [AI Incident Database](https://incidentdatabase.ai/) — **Responsible AI Collaborative** — thousands of indexed real-world AI harms and failures; the reference corpus for building an incident-class taxonomy.
- [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — **NIST** — the Govern/Map/Measure/Manage frame that most organizational reliability requirements now cite.

## Books (free, with chapters)

- [*Designing Machine Learning Systems* — Ch. 8 "Data Distribution Shifts and Monitoring"](https://huyenchip.com/mlops/) — **Chip Huyen** — the ML failure taxonomy your severity ladder should encode; author notes free.
- [*Site Reliability Engineering* — Ch. 14 "Managing Incidents" and Ch. 15 "Postmortem Culture"](https://sre.google/books/) — **Google** — free online; the foundational text, with *The SRE Workbook* adding templates.
- [*Machine Learning Engineering* — Ch. 9 "Monitoring and Maintenance"](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — distribution shift treated as an operational concern; read-first chapters free.

## In this platform

- Section index: [Operations and Lifecycle](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/readme)
- Sibling sub-areas: [Lifecycle and Reproducibility](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/readme) · [Data and Training Platforms](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/readme) · [Packaging and Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/readme) · [Release and Deployment](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/readme) · [Governance and Economics](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/readme)
- What drift is measured against: [Cross-Validation](/ai-ml/ai-ml-learning-resources/classical-machine-learning/model-selection-and-evaluation/cross-validation/cross-validation) · [Calibration and Reliability Diagrams](/ai-ml/ai-ml-learning-resources/classical-machine-learning/model-selection-and-evaluation/calibration-and-reliability-diagrams/calibration-and-reliability-diagrams) · [Uncertainty Estimation and Conformal Prediction](/ai-ml/ai-ml-learning-resources/classical-machine-learning/model-selection-and-evaluation/uncertainty-estimation-and-conformal-prediction/uncertainty-estimation-and-conformal-prediction)
- The response to a detected problem: [Rollback and Recovery for ML Systems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/rollback-and-recovery-for-ml-systems/rollback-and-recovery-for-ml-systems) · [CI/CD for ML and Continuous Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/cicd-for-ml-and-continuous-training/cicd-for-ml-and-continuous-training)
- The LLM-shaped version of these problems: [LLMOps](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/llmops/llmops) · [Agent Safety](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-safety/agent-safety)
- Doing it rather than reading it: [Monitoring and Observability workflow](/ai-ml/practitioner-workflows/evaluation-and-safety/monitoring-and-observability) · [Continuous Training workflow](/ai-ml/practitioner-workflows/operations-and-lifecycle/continuous-training)
