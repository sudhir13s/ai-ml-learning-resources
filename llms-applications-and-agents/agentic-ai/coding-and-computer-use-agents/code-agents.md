---
id: "16-agentic-ai/code-agents"
topic: "Code Agents"
parent: "16-agentic-ai"
level: advanced
built_from: ["llm-agents-overview", "tool-use-function-calling", "planning"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Code Agents"
minutes: 10
category: agentic-ai
---

# Code Agents
> Agents that **read, write, run, and debug code** in a real repo — locating the right files, editing
> them, running tests, and iterating on failures. They turn an LLM into something that can resolve a
> GitHub issue end-to-end. Measured by benchmarks like **SWE-bench**.

**Why it matters:** the highest-value, most-evaluated agent application (and the one powering coding
assistants). Interviews probe the loop (localize → edit → run tests → reflect → repeat), why
**execution feedback** (test results, stack traces) makes code agents far more reliable than
open-ended tasks, the design of the agent–computer interface (file/edit/shell tools), and why
SWE-bench scores are the field's headline metric.

**Start here — suggested path:**

1. **See the task & benchmark** — read [SWE-bench](https://arxiv.org/abs/2310.06770). *Defines the "resolve a real GitHub issue" task that frames the whole area.*
2. **Study a concrete agent** — read [SWE-agent](https://arxiv.org/abs/2405.15793). *The agent–computer interface (file viewer, editor, shell) that drives strong SWE-bench results.*
3. **See production framing** — read [Raising the bar on SWE-bench Verified](https://www.anthropic.com/engineering/swe-bench-sonnet). *What a simple, well-designed scaffold + good tools achieves.*
4. **Learn how they are actually driven** — read [Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices). *What a team that ships a coding agent has learned about repo context, permissions, test loops, and long-horizon runs.*
5. **Build one** — do [Building Code Agents with smolagents](https://www.deeplearning.ai/courses/building-code-agents-with-hugging-face-smolagents). *Agents that write code as their action space.*

## Courses (free)
- [Building Code Agents with Hugging Face smolagents](https://www.deeplearning.ai/courses/building-code-agents-with-hugging-face-smolagents) — **DeepLearning.AI × Hugging Face** — code-writing agents, free.
- [HF Agents Course — Code Agents](https://huggingface.co/learn/agents-course/unit2/smolagents/code_agents) — **Hugging Face** — agents whose actions are executable code.

## Videos
- [How We Build Effective Agents](https://www.youtube.com/watch?v=D7_ipDqhtwk) — **Barry Zhang (Anthropic), AI Engineer** — tool/loop design that underlies coding agents.
- [Tips for Building AI Agents](https://www.youtube.com/watch?v=LP5OCa20Zpg) — **Anthropic** — designing agent–environment interfaces (incl. shell/file tools).
- [Learn to Build Effective Agentic AI Systems](https://www.youtube.com/watch?v=w7vqXL4PWEE) — **Andrew Ng (DeepLearning.AI)** — evaluation-driven agent development.

## Key Papers
- [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) — **Jimenez et al. (2023)** — the canonical code-agent benchmark.
- [SWE-agent: Agent–Computer Interfaces Enable Software Engineering](https://arxiv.org/abs/2405.15793) — **Yang et al. (2024)** — tool design that drives strong issue-resolution.
- [Voyager: An Open-Ended Embodied Agent with LLMs](https://arxiv.org/abs/2305.16291) — **Wang et al. (2023)** — writing & reusing code as a growing skill library.

## Articles / Blogs (free, no paywall)
- [SWE-bench leaderboard & docs](https://www.swebench.com/) — **SWE-bench team** — the benchmark, tasks, and current standings.
- [Raising the bar on SWE-bench Verified](https://www.anthropic.com/engineering/swe-bench-sonnet) — **Anthropic** — scaffold and tool design for code agents.
- [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) — **Anthropic** — agentic patterns that coding agents instantiate.
- [Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices) — **Anthropic (2025)** — how a production coding agent is actually operated: repo-level context files, permission boundaries, test-driven loops, and multi-hour sessions. The closest thing to a manual for the 2025-26 generation of these tools.
- [Writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) — **Anthropic (2025)** — why the *agent–computer interface* (tool granularity, error messages, output size) dominates coding-agent success, which is exactly the SWE-agent finding restated for practitioners.
- [SWE-bench Verified — the dataset](https://huggingface.co/datasets/princeton-nlp/SWE-bench_Verified) — **Princeton NLP / OpenAI (2024)** — the human-validated 500-task subset that removed SWE-bench's unsolvable and under-specified instances; the split whose numbers are quoted in 2026, not the original.

**Where this stands in 2026:** SWE-bench Verified went from single-digit resolve rates in 2023 to the majority of tasks being solved by frontier scaffolds — so the interesting questions moved from "can it patch a file" to **long-horizon reliability**: keeping a coherent plan over hours, managing context across hundreds of tool calls (see [Context Engineering](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/context-engineering/context-engineering)), and constraining what an agent may execute (see [Prompt Injection and Agent Guardrails](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/prompt-injection-and-agent-guardrails/prompt-injection-and-agent-guardrails)). Expect an interviewer to push on the second and third, not the first.

## Books (free, with chapters)
- [Artificial Intelligence: A Modern Approach — **Ch. 2 "Intelligent Agents"**](https://aima.cs.berkeley.edu/) — **Russell & Norvig** — the percept→action loop; a code agent's environment is the repo + shell.

## In this platform
- Concept depth (the *why*): [ai-ml-intuitions 8.03 Agents & Tool Use](/ai-ml/ai-ml-intuitions/reasoning-and-agency/agents-and-tools/agent-loop-and-tool-use-intuition)
- Prev / next: [09 Agent Frameworks](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-frameworks/agent-frameworks) · [11 Computer-Use & GUI Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/coding-and-computer-use-agents/computer-use-and-gui-agents) · [12 Agent Evaluation & Benchmarks](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-evaluation/agent-evaluation)
- Related (canonical home): [Prompting & In-Context Learning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/prompting-and-in-context-learning/prompting-and-in-context-learning)
