---
id: "16-agentic-ai"
topic: "Agentic AI & Tool Use"
level: advanced
built_from: ["llms"]
updated: 2026-06-27
---

# Agentic AI & Tool Use
> LLMs that *act* — reasoning loops, tool/function calling, memory, planning, and multi-agent
> systems. The fastest-moving area in applied AI.

**Start here:** [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) — **Anthropic** — the clearest, least-hyped guide to when (and when not) to build agents.

## Concept Index
Each topic below is a self-contained page — a short guided learning path plus the best **free,
open** course, video, paper, article, or book for that topic. New here? Read the field framing
above, then work top to bottom.

### Foundations
1. [LLM Agents — Overview & the Agent Loop](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-foundations/agent-foundations)
2. [ReAct — Reason + Act](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/reason-and-act/reason-and-act)
3. [Tool Use & Function Calling](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/tool-use/tool-use)

### Reasoning, planning & memory
4. [Planning — Task Decomposition & Plan-and-Execute](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/planning/planning)
5. [Reflection & Self-Critique](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/reflection/reflection)
6. [Memory for Agents (short- & long-term)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/memory/memory)

### Systems, protocols & frameworks
7. [Multi-Agent Systems & Orchestration](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/multi-agent-systems/multi-agent-systems)
8. [Model Context Protocol (MCP)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/model-context-protocol/model-context-protocol)
9. [Agent Frameworks (LangGraph, etc., conceptual)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-frameworks/agent-frameworks)

### Applied agents
10. [Code Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/coding-and-computer-use-agents/code-agents)
11. [Computer-Use & GUI Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/coding-and-computer-use-agents/computer-use-and-gui-agents)

### Evaluation & safety
12. [Agent Evaluation & Benchmarks (AgentBench · SWE-bench)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-evaluation/agent-evaluation)
13. [Safety, Guardrails & Human-in-the-Loop](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-safety/agent-safety)

### Related concepts (canonical home is another section)
> These topics are foundations or applications of agents, but their canonical home is another section —
> linked here to avoid repetition.
- **Prompting & In-Context Learning · Chain-of-Thought · Fine-tuning / SFT · RLHF** → [LLMs](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme) ([Prompting](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/prompting-and-in-context-learning/prompting-and-in-context-learning) · [Chain-of-Thought](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/chain-of-thought-and-reasoning/chain-of-thought-and-reasoning) · [SFT](/ai-ml/ai-ml-learning-resources/model-adaptation/supervised-fine-tuning/supervised-fine-tuning) · [RLHF & DPO](/ai-ml/ai-ml-learning-resources/model-adaptation/preference-and-alignment-training/preference-and-alignment-training))
- **Retrieval-Augmented Generation (RAG) & retrieval** → [RAG & LLM Applications](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/overview)
- **RL foundations (MDPs · policies · reward)** → [Reinforcement Learning](/ai-ml/ai-ml-learning-resources/reinforcement-learning/readme)

## Courses (free)
- [AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) — **DeepLearning.AI × LangChain** — free short course on agent loops.
- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course) — **Hugging Face** — free, build agents with tools and memory.

## Videos
- [Intro to LLMs + agents](https://www.youtube.com/watch?v=zjkBMFhNj_g) — **Andrej Karpathy** — the "LLM OS" framing.
- [How we build effective agents](https://www.youtube.com/watch?v=D7_ipDqhtwk) — **Anthropic** — workflows vs agents, in practice.

## Key Papers / Specs
- [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629) — **Yao et al. (2022)** — the reason→act→observe loop.
- [Toolformer](https://arxiv.org/abs/2302.04761) — **Schick et al. (2023)** — models learning to call tools.
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) — **Anthropic** — the emerging tool-interface standard.

## Articles
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) — **Lilian Weng** — the canonical survey (planning, memory, tools).

## In this platform
- Math/mechanism: [ai-ml-intuitions 8.03 Agents & Tool Use](/ai-ml/ai-ml-intuitions/reasoning-agency/agent-loop-and-tool-use-intuition)
