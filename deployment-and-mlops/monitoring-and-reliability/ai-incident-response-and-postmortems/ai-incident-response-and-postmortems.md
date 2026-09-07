---
id: "deployment-and-mlops/monitoring-and-reliability/ai-incident-response-and-postmortems"
topic: "AI Incident Response & Postmortems"
level: advanced
built_from: ["model-monitoring-and-observability", "data-and-concept-drift-detection", "rollback-and-recovery-for-ml-systems"]
leads_to: ["18-mlops/llmops"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "AI Incident Response & Postmortems"
minutes: 16
category: monitoring-and-reliability
---

# AI Incident Response & Postmortems
> Site reliability engineering (SRE) gives you the shape of an incident: detect, declare, assign a
> commander, mitigate, then write a **blameless postmortem** whose output is action items, not
> blame. Machine-learning systems add incident classes that never page anyone: **silent quality
> degradation** (nothing errors, the predictions just get worse), an **upstream data outage** that
> quietly turns a feature into nulls, a **prompt-injection or tool-abuse incident**, and a
> **cost blow-up** from a retry loop or a runaway agent.

**Why it matters:** the on-call question for ML and large-language-model (LLM) systems. Availability
alarms do not fire on a model that has gone stupid, so the runbook has to name **quality** signals
(drift, calibration, refusal rate, tool-error rate, evaluation scores on a held-out canary set)
alongside latency and errors, and to define what "mitigate" means when the fix is not a code
revert. Interviewers look for: the severity ladder and who declares, **mitigate before diagnose**
(roll back, disable the feature flag, fall back to the previous model or a rules baseline), the
delayed-label problem that makes ML detection slow, and a postmortem culture that produces tracked
actions. In 2026 the LLM-specific half is expected too — injection, jailbreak and data-exfiltration
incidents, plus the governance frames (NIST AI Risk Management Framework, MITRE ATLAS) that
regulators and enterprise customers now ask about.

**Start here — suggested path:**

1. **Learn the incident frame** — read [Managing Incidents](https://sre.google/sre-book/managing-incidents/) — **Google SRE book (Andrew Stribblehill)**. *Roles, handoff, and why an unstructured response is the failure mode, not the outage.*
2. **Learn the postmortem** — read [Postmortem Culture: Learning from Failure](https://sre.google/sre-book/postmortem-culture/) — **Google SRE book (John Lunney & Sue Lueder)**, plus the [workbook chapter](https://sre.google/workbook/postmortem-culture/) with a real template. *Blameless, action-item-producing, and reviewed — the three properties that make it worth the hours.*
3. **Get a runnable on-call process** — read [PagerDuty Incident Response documentation](https://response.pagerduty.com/) — **PagerDuty** — *open-sourced internal training: severity levels, the incident-commander role, and the during-incident checklist you can adopt verbatim.*
4. **Add the ML failure classes** — read [Data Distribution Shifts and Monitoring](https://huyenchip.com/2022/02/07/data-distribution-shifts-and-monitoring.html) — **Chip Huyen**. *Why ML degradation is silent, and which signals detect it before the labels arrive.*
5. **Add the LLM failure classes** — read the [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — **OWASP** — and **Simon Willison's** [prompt-injection series](https://simonwillison.net/series/prompt-injection/). *The taxonomy your LLM runbook needs, and the running record of real-world exploits.*

## Courses (free)

- [PagerDuty Incident Response](https://response.pagerduty.com/) — **PagerDuty** — a complete, open-licensed on-call curriculum: before, during and after an incident, with severity definitions and role scripts.
- [SREcon proceedings and recordings](https://www.usenix.org/srecon) — **USENIX** — the practitioner conference for incident response; talks and papers are free and cover ML and LLM operations from 2024 onward.
- [Made With ML — Monitoring](https://madewithml.com/courses/mlops/monitoring/) — **Goku Mohandas** — builds the detection half: the alerts that a runbook responds to.

## Videos

- [Postmortem Culture at Google](https://www.youtube.com/watch?v=qgHWzQ2zcqQ) — **Ramon Medrano Llamas, Google (Conf42)** — how blameless postmortems are actually run and reviewed inside Google, by an SRE who does it.
- [Full Stack Deep Learning 2022 lecture series](https://www.youtube.com/playlist?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur) — **The Full Stack** — the troubleshooting/testing and monitoring lectures are the ML-specific complement to SRE practice.

## Key Papers

- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (2015, Google)** — feedback loops and undeclared consumers: the mechanisms behind the incidents that are hardest to attribute.
- [Challenges in Deploying Machine Learning: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes, Urma & Lawrence (2020)** — a catalogue of real post-deployment failures; useful as an incident-class checklist.
- [Machine Learning Operations (MLOps): Overview, Definition, and Architecture](https://arxiv.org/abs/2205.02302) — **Kreuzberger, Kühl & Hirschl (2022)** — where monitoring, alerting and the human roles sit in a reference MLOps architecture.

## Articles / Blogs (free, no paywall)

- [Managing Incidents](https://sre.google/sre-book/managing-incidents/) and [Emergency Response](https://sre.google/sre-book/emergency-response/) — **Google SRE book** — free chapters; the vocabulary (incident commander, communications lead, operations lead) everyone else borrows.
- [A postmortem of three recent issues](https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues) — **Anthropic (2025)** — a rare public, technical postmortem of LLM-serving bugs (routing, token generation, precision) and how they evaded standard quality monitoring.
- [Incident Response](https://sre.google/workbook/incident-response/) — **Google SRE workbook** — the practical follow-up: paging, escalation policies and running the process at smaller companies.
- [AI Incident Database](https://incidentdatabase.ai/) — **Responsible AI Collaborative** — 3,000+ indexed real-world AI harms and failures; the reference corpus for "has this failure happened before?"
- [MITRE ATLAS](https://atlas.mitre.org/) — **MITRE** — the adversarial tactics-and-techniques matrix for AI systems; the threat-model half of an LLM incident taxonomy.
- [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — **NIST** — the Govern/Map/Measure/Manage frame, with the [AI RMF Playbook](https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook) giving concrete incident-response and documentation actions.
- [Prompt injection series](https://simonwillison.net/series/prompt-injection/) — **Simon Willison** — the continuously updated public record of injection and exfiltration incidents, and why no filter has solved them.
- [AI Incidents Monitor](https://oecd.ai/en/incidents) — **OECD** — cross-jurisdiction incident tracking; useful context for reporting obligations.
- [Status page](https://status.anthropic.com/) — **Anthropic** — a working example of the public-communication artifact an incident process has to produce, alongside the internal postmortem.

## Books (free, with chapters)

- [*Site Reliability Engineering* — Ch. 14 "Managing Incidents" and Ch. 15 "Postmortem Culture"](https://sre.google/books/) — **Google** — free to read online; the foundational text, and the *SRE Workbook* companion adds templates.
- [*Designing Machine Learning Systems* — Ch. 8 "Data Distribution Shifts and Monitoring"](https://huyenchip.com/mlops/) — **Chip Huyen** — the ML failure taxonomy your severity ladder should encode (author notes free).

## In this platform

- Detection comes first: [Model Monitoring & Observability](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability) · [Data & Concept Drift Detection](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/data-and-concept-drift-detection/data-and-concept-drift-detection)
- The usual mitigation: [Rollback & Recovery for ML Systems](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/release-and-deployment/rollback-and-recovery-for-ml-systems/rollback-and-recovery-for-ml-systems) · [A/B Testing, Shadow & Canary Deployment](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/release-and-deployment/ab-testing-shadow-and-canary-deployment/ab-testing-shadow-and-canary-deployment)
- LLM-specific operations and guardrails: [LLMOps](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/governance-and-economics/llmops/llmops) · [Safety & Alignment](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/safety-and-alignment/safety-and-alignment) · [Hallucination & Grounding](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/hallucination-and-grounding/hallucination-and-grounding)
- Cost incidents have their own owner: [Cost Optimization for ML Systems](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/governance-and-economics/cost-optimization/cost-optimization)
- The offline analogue of a postmortem: [Error Analysis & Model Debugging](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/error-analysis-and-model-debugging/error-analysis-and-model-debugging)
