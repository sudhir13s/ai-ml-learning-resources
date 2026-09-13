---
id: "evaluation"
topic: "Evaluation"
level: advanced
built_from: ["large-language-models", "model-selection-and-evaluation"]
updated: 2026-09-13
---

# Evaluation

> How you know whether a model is any good, and whether it is safe: the benchmark portfolio,
> judges and human preference, calibration, the two failure modes that break deployments —
> ungrounded answers and unsafe ones — and how each is measured rather than asserted. This is
> evaluation of the *model*; evaluating an application built on one is a Practitioner Workflows
> job, and the classical footing (bias-variance, cross-validation, calibration) lives in
> [Model Selection and Evaluation](/ai-ml/ai-ml-learning-resources/classical-machine-learning/model-selection-and-evaluation/readme).

**Start here:** [Model Evaluation and Benchmarks](/ai-ml/ai-ml-learning-resources/evaluation/model-evaluation-and-benchmarks/model-evaluation-and-benchmarks) — the portfolio view, so that no single number gets to stand for a model.

## Topics

1. [Model Evaluation and Benchmarks](/ai-ml/ai-ml-learning-resources/evaluation/model-evaluation-and-benchmarks/model-evaluation-and-benchmarks) — perplexity, capability benchmarks, LLM-as-judge and human preference, calibration, contamination and saturation.
2. [Hallucination and Grounding](/ai-ml/ai-ml-learning-resources/evaluation/hallucination-and-grounding/hallucination-and-grounding) — input and output rails, grounded abstention, and the false-refuse versus false-allow trade-off measured rather than asserted.
3. [Alignment and Safety Evaluation](/ai-ml/ai-ml-learning-resources/evaluation/alignment-and-safety-evaluation/alignment-and-safety-evaluation) — why an ungrounded sampler hallucinates by default, and the two families of fix: move probability mass onto truth, or refuse the low-confidence tail.

## References

**In this platform**:
- [Agent Evaluation](/ai-ml/practitioner-workflows/agentic-systems/agent-evaluation/agent-evaluation) — the agent-facing half.
- [Calibration and Reliability Diagrams](/ai-ml/ai-ml-learning-resources/classical-machine-learning/model-selection-and-evaluation/calibration-and-reliability-diagrams/calibration-and-reliability-diagrams) — the classical footing.
- [Citations and Attribution](/ai-ml/practitioner-workflows/llm-applications/citations-and-attribution/citations-and-attribution) — grounding as a system rather than a prompt.
- [Error Analysis and Model Debugging](/ai-ml/ai-ml-learning-resources/classical-machine-learning/model-selection-and-evaluation/error-analysis-and-model-debugging/error-analysis-and-model-debugging) — the classical footing.
- [Evaluation and Benchmarking workflow](/ai-ml/practitioner-workflows/evaluation-and-safety/evaluation-and-benchmarking) — doing it rather than reading it.
- [Guardrails and Prompt Injection](/ai-ml/ai-ml-intuitions/reasoning-and-agency/safety-boundaries/guardrails-and-prompt-injection-intuition) — the mental models.
- [Large Language Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/readme) — before this section.
- [Model Adaptation](/ai-ml/ai-ml-learning-resources/model-adaptation/readme) — before this section: what is being judged.
- [Monitoring and Reliability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/readme) — after this section.
- [Operations and Lifecycle](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/readme) — after this section: where evaluation continues after deployment.
- [Prompt Injection and Agent Guardrails](/ai-ml/practitioner-workflows/agentic-systems/prompt-injection-and-agent-guardrails/prompt-injection-and-agent-guardrails) — the agent-facing half.
- [RAG Evaluation](/ai-ml/practitioner-workflows/llm-applications/rag-evaluation/rag-evaluation) — grounding as a system rather than a prompt.
- [RAG Foundations](/ai-ml/practitioner-workflows/llm-applications/rag-foundations/rag-foundations) — grounding as a system rather than a prompt.
- [Safety and Guardrails workflow](/ai-ml/practitioner-workflows/evaluation-and-safety/safety-and-guardrails) — doing it rather than reading it.

**Videos**:
- [Reinforcement Learning from Human Feedback (RLHF), Clearly Explained](https://www.youtube.com/watch?v=qPN_XZcJf_s) — **StatQuest with Josh Starmer** — the preference model that both alignment and pairwise judge evaluation rest on.

**Courses**:
- [Red Teaming LLM Applications](https://www.deeplearning.ai/short-courses/red-teaming-llm-applications/) — **DeepLearning.AI with Giskard** — how to probe a model for injection, jailbreak and leakage; the attacks safety evaluation exists to find.
- [Stanford CS324 — Large Language Models](https://stanford-cs324.github.io/winter2022/) — **Stanford** — the evaluation and harms lectures: how LMs are measured and where benchmarks mislead.

**Articles**:
- [Prompt injection series](https://simonwillison.net/series/prompt-injection/) — **Simon Willison** — the continuously updated public record of injection and exfiltration incidents, and why the naive defences do not work.

**Papers**:
- [Language Models Don't Always Say What They Think](https://arxiv.org/abs/2305.04388) — **Turpin et al. (2023)** — chain-of-thought explanations can be systematically unfaithful to the computation that produced the answer.
- [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599) — **Guo, Pleiss, Sun and Weinberger (2017)** — the expected-calibration-error estimator and reliability diagrams the evaluation page uses.

**Books**:
- [*A Survey of Large Language Models*](https://arxiv.org/abs/2303.18223) — **Zhao et al. (2023)** — book-length free reference with the citation trail for the evaluation landscape.
- [*Speech and Language Processing*, 3rd ed. — Ch. 10 "Large Language Models"](https://web.stanford.edu/~jurafsky/slp3/10.pdf) — **Jurafsky and Martin** — free draft; intrinsic versus extrinsic evaluation and where perplexity stops being informative.
