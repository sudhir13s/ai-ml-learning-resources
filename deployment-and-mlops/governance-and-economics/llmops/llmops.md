---
id: "18-mlops/llmops"
topic: "LLMOps (eval · guardrails · prompt versioning · cost/latency)"
parent: "18-mlops-and-deployment"
level: advanced
built_from: ["model-serving", "model-monitoring-and-observability", "llms"]
interview_frequency: very-high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "LLMOps (eval · guardrails · prompt versioning · cost/latency)"
minutes: 10
category: governance-and-economics
---

# LLMOps — Eval · Guardrails · Prompt Versioning · Cost/Latency
> MLOps adapted to LLM applications, where the "model" is often a frozen API and the system you operate is
> prompts + retrieval + tools. What changes: evaluation is open-ended (LLM-as-judge, rubrics, no single
> accuracy number), **prompts are versioned artifacts**, guardrails defend inputs/outputs (prompt injection,
> PII, toxicity, hallucination), and cost/latency per token become first-class operational metrics.

**Why it matters:** the fastest-growing interview area. Expect "how is LLMOps different from MLOps?" —
the answers: evaluation without ground truth (offline evals + LLM-as-judge + online feedback), prompt
versioning and regression testing, guardrails as the production safety layer, and managing token cost +
latency. Builds on LLM internals (covered in LLMs, Applications and Agents) but focuses on *operating* LLM systems.

**What changed in 2025–26** — the operational surface moved from "one prompt, one call" to agents:

- **Tracing is the primary telemetry.** A request is a *trace* of model calls, tool calls, and retrievals;
  the **OpenTelemetry GenAI semantic conventions** are the emerging vendor-neutral schema, and
  Langfuse / Arize Phoenix / W&B Weave / MLflow all emit and read it.
- **Evals run in production, not just in CI.** Online LLM-as-judge scoring on sampled traffic, with
  human review queues feeding a regression dataset.
- **Prompts and agent configs are versioned artifacts** in a registry, promoted like models.
- **Cost is accounted per token, per trace, per user** — an agent loop can burn 50× a single call,
  so cost-per-successful-task replaced cost-per-request as the metric that matters.

**Start here — suggested path:**

1. **Get the landscape** — read [Building LLM Applications for Production](https://huyenchip.com/2023/04/11/llm-engineering.html) and watch [the companion talk](https://www.youtube.com/watch?v=spamOhG7BOA). *The canonical map of what LLMOps must handle.*
2. **See the 2026 architecture** — read [Building a Generative AI Platform](https://huyenchip.com/2024/07/25/genai-platform.html). *Context construction, guardrails, routing, caching, observability — the reference block diagram teams converged on.*
3. **Evaluate LLMs** — browse [OpenAI Evals](https://github.com/openai/evals) and read [LLM patterns](https://eugeneyan.com/writing/llm-patterns/). *Eval harnesses, LLM-as-judge, regression testing for prompts.*
4. **Add guardrails** — watch [Combining Guardrails and LLM Evaluations](https://www.youtube.com/watch?v=gXdBwgVZ_Ho). *Input/output filters: prompt injection, personally identifiable information (PII), toxicity, format checks.*
5. **Trace & monitor in prod** — read the [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) and watch the [Langfuse walkthrough](https://www.youtube.com/watch?v=2E8iTvGo9Hs). *Tracing, online evals, and feedback loops on a portable schema.*

## Courses (free)
- [What is LLMOps? (LLM Operations Guide)](https://www.databricks.com/glossary/llmops) — **Databricks** — the discipline, components, and how it differs from MLOps.
- [LangSmith — Documentation](https://docs.smith.langchain.com/) — **LangChain** — tracing, evaluation, and monitoring for LLM apps.
- [Langfuse — Documentation](https://langfuse.com/docs) — **Langfuse** — the open-source stack end to end: traces, prompt management with versioned deployments, datasets, and online evaluation.

## Videos
- [Building LLM Applications for Production // Chip Huyen](https://www.youtube.com/watch?v=spamOhG7BOA) — **AAIF Live (Chip Huyen)** — the foundational LLMOps talk: eval, cost, latency, reliability.
- [New Course with Google Cloud: LLMOps](https://www.youtube.com/watch?v=tabmG21y290) — **DeepLearningAI** — the LLMOps lifecycle and tooling overview.
- [AI with Assurance: Combining Guardrails and LLM Evaluations](https://www.youtube.com/watch?v=gXdBwgVZ_Ho) — **Arize AI** — guardrails + evals as the production safety layer.
- [LLM Evals & Guardrails in Production](https://www.youtube.com/watch?v=041gk0N8gPA) — **Toronto Machine Learning Society (TMLS)** — practitioners on evaluating and guarding LLMs live.
- [10-minute walkthrough of Langfuse](https://www.youtube.com/watch?v=2E8iTvGo9Hs) — **Langfuse** — what an LLM observability tool actually shows you: traces, scores, prompt versions, datasets.
- [OpenTelemetry for GenAI and the OpenLLMetry project](https://www.youtube.com/watch?v=JnQXEMHh3aw) — **OpenObservability Talks** — why LLM telemetry is converging on OpenTelemetry rather than per-vendor SDKs.

## Key Papers
- [Challenges in Deploying ML: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes et al. (2020)** — deployment challenges that compound for LLM systems.
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (2015)** — the debt patterns that prompts/chains reintroduce at scale.

## Articles / Blogs (free, no paywall)
- [Building LLM Applications for Production](https://huyenchip.com/2023/04/11/llm-engineering.html) — **Chip Huyen** — the definitive free LLMOps overview (eval, prompt versioning, cost/latency).
- [Building a Generative AI Platform](https://huyenchip.com/2024/07/25/genai-platform.html) — **Chip Huyen** — the reference architecture: context, guardrails, routing, caching, observability, in build order.
- [Patterns for Building LLM-based Systems & Products](https://eugeneyan.com/writing/llm-patterns/) — **Eugene Yan** — evals, retrieval, caching, guardrails, defensive UX — the practitioner's pattern catalog.
- [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) — **OpenTelemetry** — the vendor-neutral span/attribute schema for model, tool, and agent calls; the reason 2026 traces are portable between tools.
- [Arize Phoenix — Documentation](https://arize.com/docs/phoenix) — **Arize AI** — open-source tracing plus evaluation, notable for embedding/response drift analysis on live traffic.
- [MLflow Prompt Registry](https://mlflow.org/docs/latest/genai/prompt-registry/) — **MLflow** — prompts as first-class versioned artifacts with aliases, so a prompt change ships like a model change.
- [W&B Weave](https://docs.wandb.ai/weave) — **Weights & Biases** — trace capture and scorer-based evaluation for LLM and agent apps.
- [What is LLMOps?](https://www.databricks.com/glossary/llmops) — **Databricks** — clear definition and component breakdown.
- [OpenAI Evals](https://github.com/openai/evals) — **OpenAI** — open framework for evaluating LLM behavior and regressions.

## Books (free, with chapters)
- [Designing Machine Learning Systems — **Ch. 8–9** (monitoring, distribution shift, test-in-prod) applied to LLM apps](https://huyenchip.com/mlops/) — **Chip Huyen** — author notes/talks free.
- [Machine Learning Engineering — **Ch. 9 "Monitoring & Maintenance"** (operating models in prod)](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — read-first chapters free.

## In this platform
- Builds on: [09 Model Serving](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/packaging-and-serving/model-serving/model-serving) · [11 Model Monitoring & Observability](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/model-monitoring-and-observability/model-monitoring-and-observability)
- Next concepts: [16 Cost Optimization](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/governance-and-economics/cost-optimization/cost-optimization)
- When an LLM system misbehaves in production: [AI Incident Response & Postmortems](/ai-ml/ai-ml-learning-resources/deployment-and-mlops/monitoring-and-reliability/ai-incident-response-and-postmortems/ai-incident-response-and-postmortems)
- Related concepts (covered elsewhere): LLM evaluation & benchmarks → [LLMs — LLM Evaluation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/llm-evaluation/llm-evaluation) · prompting & in-context learning → [LLMs — Prompting](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/prompting-and-in-context-learning/prompting-and-in-context-learning) · LLM inference cost/latency internals → [LLMs — Inference Optimization & Serving](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/inference-optimization/inference-optimization)
