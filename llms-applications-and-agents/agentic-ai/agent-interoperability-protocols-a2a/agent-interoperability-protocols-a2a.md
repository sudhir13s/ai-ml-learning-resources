---
id: "llms-applications-and-agents/agentic-ai/agent-interoperability-protocols-a2a"
topic: "Agent Interoperability Protocols — A2A and the Landscape"
level: advanced
built_from: ["model-context-protocol", "multi-agent-systems"]
leads_to: ["agent-frameworks", "prompt-injection-and-agent-guardrails"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Agent Interoperability Protocols — A2A and the Landscape"
minutes: 14
category: agentic-ai
---

# Agent Interoperability Protocols — A2A and the Landscape

> The Model Context Protocol (MCP) connects one agent to its **tools**. **Agent2Agent (A2A)**
> connects agents to *each other*: a remote agent publishes an **Agent Card** describing its skills
> and endpoint, a client agent discovers it, sends a **Task**, and streams status back — without
> either side exposing its internal state, memory or prompts. One is vertical, the other horizontal.

**Why it matters:** the moment an organisation has agents from more than one team or vendor, this is
the integration question — and interviewers use it to separate protocol understanding from vendor
recall.

- **What is probed:** the MCP-versus-A2A distinction in one sentence (tools versus peers), and the fact that they compose rather than compete; the A2A objects — Agent Card, Task, Message, Artifact — and the transport (HTTP with JSON-RPC 2.0, plus server-sent events for streaming and push notifications for long jobs).
- **The design property that matters:** **opacity**. A2A deliberately does not require agents to share memory, tools or reasoning traces, so a remote agent stays a black box with a contract — the whole point for cross-vendor use.
- **The governance fact:** A2A was announced by Google in April 2025 and donated to the Linux Foundation, which is why it is now discussed as a neutral standard rather than a vendor protocol.
- **The honest caveat:** the space is unsettled. ACP, ANP and the AGNTCY collective all exist; a good answer maps the landscape and names the adoption order rather than declaring a winner.

**Start here — suggested path:**

1. **Get the one-paragraph distinction** — read [What is A2A?](https://a2a-protocol.org/latest/topics/what-is-a2a/) — **A2A Project (Linux Foundation)**. *Peer delegation versus tool access, stated by the specification itself.*
2. **Read the launch rationale** — read [A2A: a new era of agent interoperability](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) — **Google**. *Why an opaque, capability-discovered protocol, and the design principles behind it.*
3. **Read the objects** — read the [A2A Specification](https://a2a-protocol.org/latest/specification/) — **A2A Project**. *Agent Card, Task lifecycle, Message and Artifact, streaming and push notifications.*
4. **Place it in the landscape** — read [A Survey of Agent Interoperability Protocols](https://arxiv.org/abs/2505.02279) — **Ehtesham et al. (2025)**. *MCP, ACP, A2A and ANP compared, with a phased adoption roadmap.*
5. **Build one** — do the [Agent2Agent codelab](https://codelabs.developers.google.com/intro-a2a-purchasing-concierge) — **Google Codelabs**. *A concierge agent delegating to a remote seller agent; the abstractions become concrete in an hour.*

## Courses (free)

- [Agent2Agent codelab: purchasing concierge and remote seller agents](https://codelabs.developers.google.com/intro-a2a-purchasing-concierge) — **Google Codelabs** — free, hands-on: publish an Agent Card, discover a peer, delegate a task.
- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit1/introduction) — **Hugging Face** — free; the single-agent loop and tool layer that these protocols sit above.
- [OpenAI Agents SDK — Handoffs](https://openai.github.io/openai-agents-python/handoffs/) — **OpenAI** — the in-process alternative: delegation between agents inside one runtime, with documented tradeoffs against a network protocol.

## Videos

- [Introduction to Agent2Agent (A2A) Protocol](https://www.youtube.com/watch?v=Fbr_Solax1w) — **Google Cloud Tech** — the clearest short walk-through of Agent Cards, tasks and the client/remote split, from the team that authored it.
- [How We Build Effective Agents](https://www.youtube.com/watch?v=D7_ipDqhtwk) — **Barry Zhang, Anthropic (AI Engineer)** — the prerequisite judgement: when a multi-agent boundary is worth its coordination cost at all.

## Key Papers / Specs

- [A2A Protocol Specification](https://a2a-protocol.org/latest/specification/) — **A2A Project / Linux Foundation** — the normative document: transport, Agent Card, Task states, streaming.
- [Model Context Protocol Specification](https://modelcontextprotocol.io/specification/latest) — **Anthropic / MCP** — the tool-and-resource layer A2A composes with; the canonical home for MCP is the page linked below.
- [A Survey of Agent Interoperability Protocols: MCP, ACP, A2A and ANP](https://arxiv.org/abs/2505.02279) — **Ehtesham, Singh et al. (2025)** — the comparative map, including identity, discovery and security per protocol.

## Articles / Blogs (free, no paywall)

- [A2A: A new era of agent interoperability](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) — **Google Developers** — the launch post and the five design principles.
- [Linux Foundation launches the Agent2Agent protocol project](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents) — **Linux Foundation** — the governance move, and the list of contributing vendors.
- [Agent Development Kit, Agent Engine and A2A enhancements](https://developers.googleblog.com/en/agents-adk-agent-engine-a2a-enhancements-google-io/) — **Google Developers** — how A2A fits an actual deployment stack rather than a diagram.
- [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) — **Anthropic** — the other half of the story; read it before arguing about which protocol does what.
- [AGNTCY](https://agntcy.org/) — **AGNTCY (Linux Foundation collective)** — the open "internet of agents" effort: identity, directory and observability layers beyond message passing.

## Books (free, with chapters)

- [*Artificial Intelligence: A Modern Approach* — Ch. 2 "Intelligent Agents"](https://aima.cs.berkeley.edu/) — **Russell & Norvig** — free chapter material; the agent–environment interface these protocols are a modern, networked instance of.

## In this platform

- Canonical home of MCP (this page does not re-teach it): [Model Context Protocol](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/model-context-protocol/model-context-protocol)
- What is being delegated, and to whom: [Multi-Agent Systems](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/multi-agent-systems/multi-agent-systems) · [Tool Use and Function Calling](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/tool-use/tool-use) · [Agent Frameworks](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-frameworks/agent-frameworks)
- The context a remote agent must be given: [Context Engineering](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/context-engineering/context-engineering)
- Every new endpoint is new attack surface: [Prompt Injection and Agent Guardrails](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/prompt-injection-and-agent-guardrails/prompt-injection-and-agent-guardrails) · [Safety, Guardrails and Human-in-the-Loop](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-safety/agent-safety)
- How you would test a federation: [Agent Evaluation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-evaluation/agent-evaluation)
- Intuition track: [Multi-Agent Coordination](/ai-ml/ai-ml-intuitions/reasoning-and-agency/multi-agent-systems/multi-agent-coordination-intuition)
- Build it as a workflow: [A2A](/ai-ml/practitioner-workflows/workflow-library/agentic-systems/a2a) · [MCP](/ai-ml/practitioner-workflows/workflow-library/agentic-systems/mcp)
