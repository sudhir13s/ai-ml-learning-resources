---
id: "llms-applications-and-agents/reasoning-evaluation-and-alignment/test-time-computation-and-scaling"
topic: "Test-Time Computation and Scaling"
level: advanced
built_from: ["chain-of-thought-and-reasoning", "decoding-and-sampling"]
leads_to: ["09-llms/llm-evaluation-and-benchmarks", "llms-applications-and-agents/training-and-adaptation/reinforcement-learning-for-reasoning-grpo-and-rlvr"]
interview_frequency: very-high
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Test-Time Computation and Scaling"
minutes: 16
category: reasoning-evaluation-and-alignment
---

# Test-Time Computation and Scaling

> Accuracy is not fixed at training time. Let a model **think longer** (more reasoning tokens),
> **think more often** (sample N answers and pick), or **think with search** (expand and prune a tree
> of partial solutions), and it gets measurably better on hard problems. Inference compute became a
> tunable axis alongside parameters and training tokens.

**Why it matters:** it changes the economics of deployment — you now choose an accuracy/latency/cost
point per request — and it is the single most-asked reasoning question of 2025–2026.

- **What is probed:** the difference between **sampling** (best-of-N, self-consistency) and **search** (beam search, tree search) over reasoning steps; what a **verifier** does and why a process reward model (PRM) beats an outcome one for guiding search; the *compute-optimal* result — for easy problems, more test-time compute beats a bigger model; for the hardest ones, it does not.
- **The bound you must state:** pass@N (does *any* sample succeed) rises far faster than accuracy with a *selector*. Without a good verifier, most of the coverage a sampler generates is unusable. This is the whole reason verifiers matter.
- **The cheapest useful trick:** **budget forcing** (s1) — append "Wait" to suppress the end-of-thinking token and force more reasoning, or truncate to force less. A 1,000-example fine-tune plus this control reproduces much of the effect.

**Start here — suggested path:**

1. **Get the map** — read [Why We Think](https://lilianweng.github.io/posts/2025-05-01-thinking/) — **Lilian Weng (2025)**. *The most complete free survey: parallel sampling, sequential revision, search, RL, and what "thinking" costs.*
2. **Read the compute-optimal result** — read [Scaling LLM Test-Time Compute Optimally](https://arxiv.org/abs/2408.03314) — **Snell et al. (2024)**. *Allocating inference compute by problem difficulty beats a 14× larger model on easy and medium problems — and loses on the hardest.*
3. **See the ceiling and the gap** — read [Large Language Monkeys](https://arxiv.org/abs/2407.21787) — **Brown et al. (2024)**. *Coverage scales like a power law in samples; without a verifier you cannot cash it in.*
4. **Learn what a verifier is** — read [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) — **Lightman et al. (2023)**. *Process supervision beats outcome supervision, and gives search something to score.*
5. **Do it on open models** — work through [Scaling Test-Time Compute with Open Models](https://huggingface.co/spaces/HuggingFaceH4/blogpost-scaling-test-time-compute) — **Hugging Face** and its [cookbook recipe](https://huggingface.co/learn/cookbook/en/search_and_learn). *Best-of-N, beam search and diverse verifier tree search, with runnable code.*

## Courses (free)

- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Stanford** — the inference, scaling-law and alignment lectures put test-time compute in the same frame as train-time compute; free slides and assignments.
- [Search and Learn](https://github.com/huggingface/search-and-learn) — **Hugging Face** — the toolkit behind the blog post: best-of-N, beam search and diverse verifier tree search over vLLM, ready to run.
- [Reasoning with o1](https://www.deeplearning.ai/short-courses/reasoning-with-o1/) — **DeepLearning.AI × OpenAI** — free short course on prompting and budgeting a reasoning model in practice.

## Videos

- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — the "thinking models" segment: why extra tokens are extra serial computation, not decoration.
- [Build a Reasoning Model From Scratch — Motivation and Code Setup](https://www.youtube.com/watch?v=Kh9mqTzjuEQ) — **Sebastian Raschka** — opens the from-scratch series that implements inference-time scaling before any reinforcement learning.

## Key Papers

- [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314) — **Snell et al. (2024)** — the compute-optimal test-time scaling result and the difficulty-dependent strategy.
- [Large Language Monkeys: Scaling Inference Compute with Repeated Sampling](https://arxiv.org/abs/2407.21787) — **Brown et al. (2024)** — coverage as a power law in N, and the verifier bottleneck.
- [s1: Simple Test-Time Scaling](https://arxiv.org/abs/2501.19393) — **Muennighoff et al. (2025)** — 1,000 curated examples plus budget forcing; the minimal recipe that works.
- [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) — **Lightman et al. (2023)** — process reward models, and why step-level supervision is the better search signal.
- [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465) — **Zelikman et al. (2022)** — the loop that turns successful samples back into training data; the bridge from test-time to train-time.
- [DeepSeek-R1](https://arxiv.org/abs/2501.12948) — **DeepSeek-AI (2025)** — read the response-length curve: the model learns to spend more test-time compute on its own.

## Articles / Blogs (free, no paywall)

- [Why We Think](https://lilianweng.github.io/posts/2025-05-01-thinking/) — **Lilian Weng** — the definitive free survey of test-time thinking, including chain faithfulness and the "thinking tokens as latent computation" view.
- [Learning to Reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/) — **OpenAI** — the o1 post: accuracy improving smoothly with both train-time RL and test-time thinking.
- [Scaling Test-Time Compute with Open Models](https://huggingface.co/spaces/HuggingFaceH4/blogpost-scaling-test-time-compute) — **Hugging Face** — a 3B model beating a 70B on hard maths, with every search strategy ablated.
- [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) — **Sebastian Raschka** — where inference-time scaling sits among the four ways reasoning gets built.
- [OpenAI o1 System Card](https://cdn.openai.com/o1-system-card-20241205.pdf) — **OpenAI** — the primary document on what more thinking time changed, including the safety-relevant behaviours.

## Books (free, with chapters)

- [*Reinforcement Learning from Human Feedback* — "Reasoning and Inference-Time Scaling"](https://rlhfbook.com/c/14-reasoning.html) — **Nathan Lambert** — free online book; the written reference that ties inference-time scaling to the training methods that produce it.

## In this platform

- Canonical home of chain-of-thought, self-consistency and tree-of-thoughts (this page does not repeat them): [Chain-of-Thought and Reasoning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/chain-of-thought-and-reasoning/chain-of-thought-and-reasoning)
- How the ability is trained in the first place: [Reinforcement Learning for Reasoning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/reinforcement-learning-for-reasoning-grpo-and-rlvr/reinforcement-learning-for-reasoning-grpo-and-rlvr) · [Preference and Alignment Training](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/preference-and-alignment-training/preference-and-alignment-training)
- What makes the samples diverge: [Decoding and Sampling](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/decoding-and-sampling/decoding-and-sampling)
- What thinking costs to serve: [Inference Optimization](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/inference-optimization/inference-optimization) · [Continuous Batching and Scheduling](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/continuous-batching-and-scheduling/continuous-batching-and-scheduling) · [Caching and Cost Optimization](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/caching-and-cost-optimization/caching-and-cost-optimization)
- Measuring it honestly: [LLM Evaluation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/llm-evaluation/llm-evaluation) · [Hallucination and Grounding](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/hallucination-and-grounding/hallucination-and-grounding)
- Search over steps is also how agents plan: [Planning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/planning/planning) · [Reflection](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/reflection/reflection)
- Intuition track: [Test-Time Computation](/ai-ml/ai-ml-intuitions/reasoning-and-agency/reasoning/test-time-computation-intuition)
