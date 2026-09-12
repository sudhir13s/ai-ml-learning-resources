---
id: "16-agentic-ai/evaluation"
topic: "Agent Evaluation & Benchmarks"
parent: "16-agentic-ai"
level: advanced
built_from: ["llm-agents-overview", "code-agents"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Agent Evaluation & Benchmarks"
minutes: 10
category: agentic-ai
---

# Agent Evaluation & Benchmarks
> Agents are **stochastic, multi-step, and tool-using**, so "did it get the right answer?" isn't
> enough — you measure **task success** in a real environment, plus efficiency (steps, tokens, cost)
> and trajectory quality. Benchmarks like **AgentBench**, **SWE-bench**, **WebArena**, and **OSWorld**
> standardize this.

**Why it matters:** evaluation is what separates a demo from a product, and Andrew Ng calls eval-driven
development the biggest predictor of agent success. Interviews probe *why agent eval is hard*
(non-determinism, partial credit, multi-step error compounding, environment setup), the difference
between **outcome** and **process/trajectory** metrics, **execution-based** evaluation, and which
benchmark fits which capability (coding → SWE-bench, web → WebArena, OS → OSWorld, broad → AgentBench).

**Start here — suggested path:**

1. **See a broad benchmark** — read [AgentBench](https://arxiv.org/abs/2308.03688). *Evaluates LLMs as agents across 8 environments — the "what do we even measure" overview.*
2. **Study execution-based eval** — read [SWE-bench](https://arxiv.org/abs/2310.06770). *Success = tests pass; the gold standard for objective, execution-based scoring.*
3. **Add the web/OS environments** — skim [WebArena](https://arxiv.org/abs/2307.13854) + [OSWorld](https://arxiv.org/abs/2404.07972). *Realistic, reproducible environments with task-completion checks.*
4. **Get the practitioner mindset** — watch [Learn to Build Effective Agentic AI Systems](https://www.youtube.com/watch?v=w7vqXL4PWEE). *Error analysis and eval-driven development, the core skill.*
5. **Tie it to design** — read [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents). *Why you measure with real ground truth at each step.*

## Courses (free)
- [HF Agents Course — Evaluation](https://huggingface.co/learn/agents-course/unit3/agentic-rag/introduction) — **Hugging Face** — evaluating agent behavior in a project, free.
- [AI Agents in LangGraph](https://learn.deeplearning.ai/courses/ai-agents-in-langgraph) — **DeepLearning.AI × LangChain** — building loops you then need to evaluate.

## Videos
- [Learn to Build Effective Agentic AI Systems](https://www.youtube.com/watch?v=w7vqXL4PWEE) — **Andrew Ng (DeepLearning.AI)** — eval-driven development and error analysis.
- [How We Build Effective Agents](https://www.youtube.com/watch?v=D7_ipDqhtwk) — **Barry Zhang (Anthropic)** — measuring with ground truth and evaluator loops.
- [Tips for Building AI Agents](https://www.youtube.com/watch?v=LP5OCa20Zpg) — **Anthropic** — what to measure and common eval pitfalls.
- [Andrew Ng on AI Agentic Workflows](https://www.youtube.com/watch?v=q1XFm21I-VQ) — **Andrew Ng** — why iterative agentic systems need their own evaluation.

## Key Papers
- [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688) — **Liu et al. (2023)** — multi-environment agent benchmark.
- [SWE-bench: Can LMs Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) — **Jimenez et al. (2023)** — execution-based coding-agent eval.
- [WebArena: A Realistic Web Environment](https://arxiv.org/abs/2307.13854) — **Zhou et al. (2023)** — task-completion eval on realistic websites.
- [OSWorld: Benchmarking Multimodal Agents](https://arxiv.org/abs/2404.07972) — **Xie et al. (2024)** — real-computer task benchmark.
- [τ-bench: Benchmarking AI Agents for Real-World Tool-Agent-User Interaction](https://arxiv.org/abs/2406.12045) — **Yao et al. (2024, Sierra)** — the eval that exposed *reliability*, not capability, as the bottleneck: agents must follow domain policy while talking to a simulated user, and `pass^k` measures whether they succeed on the same task **k times in a row**. Frontier agents that pass once often fail that consistency test.
- [Humanity's Last Exam](https://arxiv.org/abs/2501.14249) — **Phan et al. (2025)** — the 2025 answer to benchmark saturation: expert-written questions across 100+ subjects, designed to stay hard as models improve. Useful as the counter-example when an interviewer quotes a saturated benchmark.

## Articles / Blogs (free, no paywall)
- [SWE-bench leaderboard & docs](https://www.swebench.com/) — **SWE-bench team** — tasks, harness, and current standings.
- [AgentBench (GitHub)](https://github.com/THUDM/AgentBench) — **THUDM** — code, environments, and how scoring works.
- [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) — **Anthropic** — measuring against ground truth at each step.
- [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) — **Hamel Husain** — the practitioner's method behind every number above: error-analyse real traces, write assertions for the failures you find, and validate any LLM judge against human labels before trusting it.
- [SWE-bench Verified — the dataset](https://huggingface.co/datasets/princeton-nlp/SWE-bench_Verified) — **Princeton NLP / OpenAI (2024)** — the human-validated 500-task subset that replaced the original split as the quotable number, after annotation showed many original tasks were unsolvable as written.
- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) — **Anthropic (2025)** — a candid account of evaluating a non-deterministic multi-agent system: small eval sets used early, LLM judges with an explicit rubric, and human review kept in the loop for the failure modes judges miss.

## Books (free, with chapters)
- [Artificial Intelligence: A Modern Approach — **Ch. 2 "Intelligent Agents"** (performance measures & rationality)](https://aima.cs.berkeley.edu/) — **Russell & Norvig** — defining a performance measure is the classical root of agent evaluation.

## In this platform
- Concept depth (the *why*): [ai-ml-intuitions 8.03 Agents & Tool Use](/ai-ml/ai-ml-intuitions/reasoning-and-agency/agents-and-tools/agent-loop-and-tool-use-intuition)
- Prev / next: [10 Code Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/coding-and-computer-use-agents/code-agents) · [11 Computer-Use & GUI Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/coding-and-computer-use-agents/computer-use-and-gui-agents) · [13 Safety, Guardrails & HITL](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-safety/agent-safety)
- Related (canonical home): [LLM Evaluation & Benchmarks](/ai-ml/ai-ml-learning-resources/evaluation/model-evaluation-and-benchmarks/model-evaluation-and-benchmarks)
