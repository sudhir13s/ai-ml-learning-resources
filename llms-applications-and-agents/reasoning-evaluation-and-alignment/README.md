---
id: "llms-applications-and-agents/reasoning-evaluation-and-alignment"
topic: "Reasoning, Evaluation and Alignment"
level: advanced
built_from: ["large-language-model-foundations", "training-and-adaptation"]
updated: 2026-09-07
---

# Reasoning, Evaluation and Alignment

> How you get behaviour out of a trained model, how you know whether you got it, and how you stop
> the failure modes that matter. The sub-area moves from steering at inference time (prompting,
> chains of thought, spending more compute per question) to measurement (benchmarks, judges,
> calibration) to the two things that break deployments — ungrounded answers and unsafe ones.

**Start here:** [Prompting and In-Context Learning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/prompting-and-in-context-learning/prompting-and-in-context-learning) — the one lever that changes nothing about the weights, so it is the right place to separate "the model cannot" from "the model was not asked properly".

## Concept index

Each page is a self-contained resource card with a curated `.references.md` companion where one
exists: a plain-words definition, why it matters in 2026, a five-step start-here path, and
verified courses, videos, papers, articles and books.

### Steering at inference time

1. [Prompting and In-Context Learning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/prompting-and-in-context-learning/prompting-and-in-context-learning) — what few-shot examples actually do, and where prompting stops and training has to start.
2. [Chain-of-Thought Reasoning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/chain-of-thought-and-reasoning/chain-of-thought-and-reasoning) — intermediate steps, self-consistency, least-to-most, tree of thoughts, and the unfaithfulness problem.
3. [Test-Time Computation and Scaling](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/test-time-computation-and-scaling/test-time-computation-and-scaling) — think longer, sample more, or search; inference compute as a tunable axis alongside parameters and tokens.

### Knowing whether it worked

4. [Hallucination and Grounding](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/hallucination-and-grounding/hallucination-and-grounding) — input and output rails, grounded abstention, and the false-refuse versus false-allow trade-off measured rather than asserted.
5. [LLM Evaluation and Benchmarks](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/llm-evaluation/llm-evaluation) — the portfolio view: perplexity, capability benchmarks, LLM-as-judge and human preference, calibration and safety.

### Keeping it safe

6. [Hallucination and Alignment Basics](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/safety-and-alignment/safety-and-alignment) — why an ungrounded sampler hallucinates by default, and the two families of fix: move probability mass onto truth, or refuse the low-confidence tail.

## Courses (free)

- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Stanford** — how reasoning behaviour is elicited and then trained in, inside the full LLM stack.
- [Stanford CS324 — Large Language Models](https://stanford-cs324.github.io/winter2022/) — **Stanford** — the evaluation and harms lectures: how LMs are measured and where benchmarks mislead.
- [Red Teaming LLM Applications](https://www.deeplearning.ai/short-courses/red-teaming-llm-applications/) — **DeepLearning.AI with Giskard** — how to probe an application for injection, jailbreak and leakage; the attacks guardrails exist to stop.
- [Search and Learn](https://github.com/huggingface/search-and-learn) — **Hugging Face** — the open toolkit for best-of-N, beam search and verifier-guided tree search over reasoning traces.

## Videos

- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — why intermediate thinking tokens help, placed inside the full training and inference picture.
- [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) — **Andrej Karpathy** — the deliberate-reasoning framing that motivates chain of thought and reasoning models.
- [Tree of Thoughts — Deliberate Problem Solving with LLMs](https://www.youtube.com/watch?v=ut5kp56wW_4) — **Yannic Kilcher** — a paper walkthrough of search over reasoning steps, the branching generalization of chain of thought.
- [Reinforcement Learning from Human Feedback (RLHF), Clearly Explained](https://www.youtube.com/watch?v=qPN_XZcJf_s) — **StatQuest with Josh Starmer** — the preference model that both alignment and pairwise judge evaluation rest on.

## Key Papers

- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) — **Wei et al. (2022)** — the founding result, and the source of the GSM8K numbers everyone quotes.
- [Self-Consistency Improves Chain-of-Thought Reasoning](https://arxiv.org/abs/2203.11171) — **Wang et al. (2022)** — sample diverse chains and majority-vote; the cheapest reliable gain in the whole sub-area.
- [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Parameters](https://arxiv.org/abs/2408.03314) — **Snell et al. (2024)** — when spending inference compute beats training a bigger model.
- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) — **Yao et al. (2023)** — search with backtracking over a tree of partial reasoning states.
- [Language Models Don't Always Say What They Think](https://arxiv.org/abs/2305.04388) — **Turpin et al. (2023)** — chain-of-thought explanations can be systematically unfaithful to the computation that produced the answer.
- [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599) — **Guo, Pleiss, Sun and Weinberger (2017)** — the expected-calibration-error estimator and reliability diagrams the evaluation page uses.

## Articles / Blogs (free, no paywall)

- [Learning to Reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/) — **OpenAI** — the lab's own statement of long internal chains trained by reinforcement learning, and the test-time-compute paradigm.
- [Prompt Engineering Guide](https://www.promptingguide.ai/) — **DAIR.AI** — chain of thought, zero-shot chain of thought, self-consistency and tree of thoughts compared, with runnable examples.
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) — **Lilian Weng** — chain of thought and ReAct as the planning core, and the failure modes that follow.
- [Prompt injection series](https://simonwillison.net/series/prompt-injection/) — **Simon Willison** — the continuously updated public record of injection and exfiltration incidents, and why the naive defences do not work.

## Books (free, with chapters)

- [*Speech and Language Processing*, 3rd ed. — Ch. 12 "Model Alignment, Prompting and In-Context Learning"](https://web.stanford.edu/~jurafsky/slp3/) — **Jurafsky and Martin** — free draft; the textbook treatment of the prompting and alignment material.
- [*Speech and Language Processing*, 3rd ed. — Ch. 10 "Large Language Models"](https://web.stanford.edu/~jurafsky/slp3/10.pdf) — **Jurafsky and Martin** — free draft; intrinsic versus extrinsic evaluation and where perplexity stops being informative.
- [*Reinforcement Learning from Human Feedback* — "Reasoning and Inference-Time Scaling"](https://rlhfbook.com/c/14-reasoning.html) — **Nathan Lambert** — free online; ties inference-time scaling back to the training recipe that produced it.
- [*A Survey of Large Language Models* — §6.2 Chain-of-Thought Reasoning](https://arxiv.org/abs/2303.18223) — **Zhao et al. (2023)** — book-length free reference with the citation trail for every technique here.

## In this platform

- Section index: [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme)
- Sibling sub-areas: [Large Language Model Foundations](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/readme) · [LLM Model Architectures](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/readme) · [Training and Adaptation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/readme) · [Inference and Runtime](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/readme)
- Where reasoning is trained rather than prompted: [Reinforcement Learning for Reasoning — GRPO and Verifiable Rewards](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/reinforcement-learning-for-reasoning-grpo-and-rlvr/reinforcement-learning-for-reasoning-grpo-and-rlvr) · [RLHF and DPO](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/preference-and-alignment-training/preference-and-alignment-training)
- Grounding as a system rather than a prompt: [RAG Foundations](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/rag-foundations/rag-foundations) · [Citations and Attribution](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/citations-and-attribution/citations-and-attribution) · [RAG Evaluation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/rag-evaluation/rag-evaluation)
- The agent-facing half: [Agent Evaluation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-evaluation/agent-evaluation) · [Prompt Injection and Agent Guardrails](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/prompt-injection-and-agent-guardrails/prompt-injection-and-agent-guardrails)
- The classical evaluation footing: [Calibration and Reliability Diagrams](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/calibration-and-reliability-diagrams/calibration-and-reliability-diagrams) · [Error Analysis and Model Debugging](/ai-ml/ai-ml-learning-resources/core-machine-learning/model-selection-and-evaluation/error-analysis-and-model-debugging/error-analysis-and-model-debugging)
- The mental models: [In-Context Learning and Prompting](/ai-ml/ai-ml-intuitions/reasoning-and-agency/in-context-behavior/in-context-learning-and-prompting-intuition) · [Test-Time Computation](/ai-ml/ai-ml-intuitions/reasoning-and-agency/reasoning/test-time-computation-intuition) · [Guardrails and Prompt Injection](/ai-ml/ai-ml-intuitions/reasoning-and-agency/safety-boundaries/guardrails-and-prompt-injection-intuition)
- Doing it rather than reading it: [Prompt Engineering workflow](/ai-ml/practitioner-workflows/llm-application-workflows/prompt-engineering) · [Evaluation and Benchmarking workflow](/ai-ml/practitioner-workflows/evaluation-safety-and-reliability/evaluation-and-benchmarking) · [Safety and Guardrails workflow](/ai-ml/practitioner-workflows/evaluation-safety-and-reliability/safety-and-guardrails)
