---
id: "16-agentic-ai/mcp"
topic: "Model Context Protocol (MCP)"
parent: "16-agentic-ai"
level: advanced
built_from: ["tool-use-function-calling"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Model Context Protocol (MCP)"
minutes: 10
category: agentic-ai
---

# Model Context Protocol (MCP)
> An **open standard** for connecting LLM apps to tools and data. Instead of bespoke integrations per
> app, an MCP **client** (the agent host) talks to MCP **servers** that expose **tools**,
> **resources**, and **prompts** over a common protocol — the "USB-C port for AI."

**Why it matters:** MCP is the fast-rising answer to "how do agents integrate with the world without
N×M custom glue?" Be ready to explain the **client/server/host** architecture, the three primitives
(tools / resources / prompts), how it differs from raw function calling (a *standard transport &
discovery layer*, not a replacement for the model deciding what to call), and the security surface
(servers run code; prompt injection via resources).

**Start here — suggested path:**

1. **Get the why** — read [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol). *The motivation and the USB-C-for-AI framing in two minutes.*
2. **See the architecture** — read [MCP — Getting Started / Intro](https://modelcontextprotocol.io/docs/getting-started/intro). *Client/server/host and the tools/resources/prompts primitives, from the spec.*
3. **Build one, guided** — watch [Building Agents with Model Context Protocol — full workshop](https://www.youtube.com/watch?v=kQmXtrmQ5Zg) (**Mahesh Murag, Anthropic**). *The protocol's own team, from first principles to a working server; the single best MCP resource.*
4. **Read the current spec revision** — read the [2025-06-18 specification](https://modelcontextprotocol.io/specification/2025-06-18). *Where the protocol actually is now: streamable HTTP transport, structured tool output, elicitation, and OAuth resource-server authorization.*
5. **Place it vs function calling** — re-read [Tool Use overview](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview). *MCP standardizes **how tools are served**; the model still chooses calls via tool use.*

## Courses (free)
- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit1/introduction) — **Hugging Face** — tools and integrations, the layer MCP standardizes.
- [MCP — Getting Started](https://modelcontextprotocol.io/docs/getting-started/intro) — **MCP / Anthropic** — official walkthrough: build a client and a server.

## Videos
- [Building Agents with Model Context Protocol — full workshop](https://www.youtube.com/watch?v=kQmXtrmQ5Zg) — **Mahesh Murag (Anthropic), AI Engineer** — the protocol's own maintainer: primitives, transports, and a server built live. Start here.
- [The Model Context Protocol (MCP)](https://www.youtube.com/watch?v=CQywdSdi5iA) — **Anthropic** — design and goals from the team that built it.
- [How We Build Effective Agents](https://www.youtube.com/watch?v=D7_ipDqhtwk) — **Barry Zhang (Anthropic), AI Engineer** — where a protocol like MCP fits among agent patterns, and why tool *interfaces* matter more than tool count.

## Key Papers / Specs
- [Model Context Protocol — Specification](https://modelcontextprotocol.io/) — **Anthropic / MCP** — the protocol itself (transport, primitives, lifecycle).
- [MCP specification, revision 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18) — **MCP maintainers** — the revision most 2026 hosts implement: the SSE transport is replaced by **streamable HTTP**, tools may return **structured output**, servers may **elicit** input from the user mid-call, and authorization is defined as OAuth 2.1 with the server as a resource server. Know these four when asked "what changed in MCP."
- [Tool Use overview](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview) — **Anthropic** — the function-calling layer MCP servers plug into.
- [Toolformer](https://arxiv.org/abs/2302.04761) — **Schick et al. (2023)** — background on models learning to call external tools.

## Articles / Blogs (free, no paywall)
- [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) — **Anthropic** — the launch post and rationale.
- [MCP — Getting Started / Intro](https://modelcontextprotocol.io/docs/getting-started/intro) — **MCP** — architecture and primitives, free and open.
- [Writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) — **Anthropic (2025)** — the practical half of MCP: what makes a *good* tool definition (naming, granularity, error messages, token budget) as opposed to a merely valid one. This is where most MCP servers actually fail.
- [Agent2Agent (A2A) protocol](https://a2a-protocol.org/latest/) — **A2A maintainers (Linux Foundation)** — the complementary standard: MCP connects an agent to *tools*, A2A connects an agent to *other agents*. Interviewers increasingly ask for the distinction.

## Books (free, with chapters)
- [Artificial Intelligence: A Modern Approach — **Ch. 2 "Intelligent Agents"** (agent–environment interface)](https://aima.cs.berkeley.edu/) — **Russell & Norvig** — MCP is a modern standard for the sensor/actuator interface between agent and environment.

## In this platform
- Concept depth (the *why*): [ai-ml-intuitions 8.03 Agents & Tool Use](/ai-ml/ai-ml-intuitions/reasoning-and-agency/agents-and-tools/agent-loop-and-tool-use-intuition)
- Prev / next: [Tool Use & Function Calling](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/tool-use/tool-use) · [Agent Frameworks](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-frameworks/agent-frameworks)
- The agent-to-agent counterpart: [Agent Interoperability Protocols (A2A)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-interoperability-protocols-a2a/agent-interoperability-protocols-a2a)
- What to do with everything a server exposes: [Context Engineering](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/context-engineering/context-engineering)
- The security surface this opens: [Prompt Injection and Agent Guardrails](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/prompt-injection-and-agent-guardrails/prompt-injection-and-agent-guardrails)
- Related (canonical home): [Prompting & In-Context Learning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/prompting-and-in-context-learning/prompting-and-in-context-learning)
