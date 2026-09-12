---
id: "operations-and-lifecycle/governance-and-economics"
topic: "Governance and Economics"
level: advanced
built_from: ["release-and-deployment", "monitoring-and-reliability"]
updated: 2026-09-07
---

# Governance and Economics

> The control plane and the bill. Governance answers who may promote a model, what documentation
> it carries and what the audit trail looks like; LLMOps answers what changes when the "model" is
> a frozen application programming interface and the system you actually operate is prompts,
> retrieval and tools; cost optimization answers the question a finance team will eventually ask
> about the largest line item an ML organization controls.

**Start here:** [Model Registry and Governance](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/model-registry-and-governance/model-registry-and-governance) — the registry is the object every promotion, rollback and audit conversation refers to.

## Concept index

Each page is a self-contained resource card: a plain-words definition, why it matters in 2026, a
five-step start-here path, and verified courses, videos, papers, articles and books.

### The control plane

1. [Model Registry and Governance](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/model-registry-and-governance/model-registry-and-governance) — versioned models with stage transitions, lineage, approvals, model cards and audit trails; the gate between trained and deployed.

### Operating LLM applications

2. [LLMOps](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/llmops/llmops) — open-ended evaluation, prompts as versioned artifacts, input and output guardrails, and per-token cost and latency as first-class operational metrics.

### Paying for it

3. [Cost Optimization for ML Systems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/cost-optimization/cost-optimization) — right-sizing and sharing accelerators, batching, autoscaling to zero, spot capacity for training, caching and quantization for inference.

## Courses (free)

- [Made With ML — MLOps Course](https://madewithml.com/courses/mlops/) — **Goku Mohandas** — efficiency and governance decisions taken inside a real project rather than as abstractions.
- [MLflow Model Registry documentation](https://mlflow.org/docs/latest/ml/model-registry/) — **MLflow maintainers** — registry concepts, stages, aliases and the promotion application programming interface, from the reference implementation.
- [LangSmith documentation](https://docs.smith.langchain.com/) — **LangChain** — tracing, evaluation and monitoring for LLM applications; the concrete shape most LLMOps stacks take.
- [Ray Serve documentation](https://docs.ray.io/en/latest/serve/index.html) — **Anyscale** — the autoscaling and batching levers that dominate serving cost.

## Videos

- [Building LLM Applications for Production](https://www.youtube.com/watch?v=spamOhG7BOA) — **Chip Huyen** — the foundational LLMOps talk: evaluation, cost, latency and reliability, stated before the tooling existed.
- [Enabling Cost-Efficient LLM Serving with Ray Serve](https://www.youtube.com/watch?v=TJ5K1CO9Wbs) — **Anyscale** — batching, autoscaling and hardware choice as measured cost levers.
- [Accelerated LLM Inference with Anyscale](https://www.youtube.com/watch?v=_sDMsg0STqs) — **Anyscale (Ray Summit 2024)** — throughput-per-dollar improvements traced to specific changes.
- [New Course with Google Cloud: LLMOps](https://www.youtube.com/watch?v=tabmG21y290) — **DeepLearning.AI** — the LLMOps lifecycle and tooling overview in short form.

## Key Papers

- [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993) — **Mitchell et al. (2019)** — the standard for documenting intended use, disaggregated performance and limitations; the governance artifact everyone cites.
- [The ML Test Score: A Rubric for ML Production Readiness](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/) — **Breck et al. (Google, 2017)** — what to verify before a model may be promoted.
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf) — **Sculley et al. (Google, 2015)** — the infrastructure debt that quietly inflates the bill nobody attributed to a model.
- [Challenges in Deploying Machine Learning: A Survey of Case Studies](https://arxiv.org/abs/2011.09926) — **Paleyes, Urma and Lawrence (2020)** — resource and cost constraints as a recurring, documented deployment blocker.

## Articles / Blogs (free, no paywall)

- [Building LLM Applications for Production](https://huyenchip.com/2023/04/11/llm-engineering.html) — **Chip Huyen** — the LLM cost and latency economics, written out: caching, model size, token accounting.
- [Model Card Toolkit](https://modelcards.withgoogle.com/about) — **Google** — practical model-card templates you can adopt rather than design.
- [MLflow Model Registry](https://mlflow.org/docs/latest/model-registry.html) — **MLflow maintainers** — the canonical reference for registry workflows and stage transitions.
- [Cost-Effective Machine Learning with Ray](https://www.anyscale.com/blog/cost-effective-machine-learning-with-ray) — **Anyscale** — utilization, spot capacity and autoscaling as the three levers that move the number.
- [OpenAI Evals](https://github.com/openai/evals) — **OpenAI** — the open framework for behavioural evaluation and regression testing of LLM systems.

## Books (free, with chapters)

- [*Designing Machine Learning Systems* — Ch. 10 "Infrastructure and Tooling"](https://huyenchip.com/mlops/) — **Chip Huyen** — cost, efficiency and the build-versus-buy decisions; author notes and companion code free.
- [*Machine Learning Engineering* — Ch. 8 "Model Deployment"](http://www.mlebook.com/wiki/doku.php) — **Andriy Burkov** — efficiency and resource trade-offs treated concretely; read-first chapters free.
- [*Site Reliability Engineering* and *The SRE Workbook*](https://sre.google/books/) — **Google** — free online; the capacity-planning and efficiency chapters transfer directly to inference fleets.

## In this platform

- Section index: [Operations and Lifecycle](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/readme)
- Sibling sub-areas: [Lifecycle and Reproducibility](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/readme) · [Data and Training Platforms](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/readme) · [Packaging and Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/readme) · [Release and Deployment](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/release-and-deployment/readme) · [Monitoring and Reliability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/readme)
- The technical levers behind the cost page: [Caching and Cost Optimization for LLM Apps](/ai-ml/ai-ml-learning-resources/inference-and-serving/caching-and-cost-optimization/caching-and-cost-optimization) · [Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization) · [Small and On-Device Language Models](/ai-ml/ai-ml-learning-resources/inference-and-serving/small-and-on-device-language-models/small-and-on-device-language-models)
- What LLMOps evaluates and guards: [LLM Evaluation and Benchmarks](/ai-ml/ai-ml-learning-resources/evaluation/model-evaluation-and-benchmarks/model-evaluation-and-benchmarks) · [Agent Evaluation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-evaluation/agent-evaluation) · [Prompt Injection and Agent Guardrails](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/prompt-injection-and-agent-guardrails/prompt-injection-and-agent-guardrails)
- What the registry stores: [Data and Model Versioning](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/data-and-model-versioning/data-and-model-versioning) · [Experiment Tracking](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/experiment-tracking/experiment-tracking)
- Doing it rather than reading it: [Inference Cost Optimization workflow](/ai-ml/practitioner-workflows/workflow-library/inference-and-serving/inference-cost-optimization) · [MLOps and Deployment workflow](/ai-ml/practitioner-workflows/workflow-library/production-lifecycle/mlops-and-deployment) · [Evaluation and Benchmarking workflow](/ai-ml/practitioner-workflows/workflow-library/evaluation-safety-and-reliability/evaluation-and-benchmarking)
