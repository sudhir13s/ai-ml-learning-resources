---
id: "15-rag-and-llm-apps/guardrails-hallucination-mitigation/references"
topic: "Guardrails & Hallucination Mitigation — References"
parent: "15-rag-and-llm-apps/guardrails-hallucination-mitigation"
type: references
updated: 2026-09-14
---

# Guardrails & Hallucination Mitigation — references

> Companion link library for **[Guardrails & Hallucination Mitigation](/ai-ml/ai-ml-learning-resources/evaluation/hallucination-and-grounding/hallucination-and-grounding)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Get the concept** — watch [What are guardrails for LLMs?](https://www.youtube.com/watch?v=FLOXGvqdwbM) (**Red Hat**). *Input/output rails and why you wrap the model with checks.*
2. **See the categories** — read [What Are AI Guardrails?](https://www.ibm.com/think/topics/ai-guardrails) (**IBM**). *The taxonomy (safety, topic, fact-check, PII) and where each rail sits.*
3. **Know the attack** — skim [Indirect Prompt Injection (Greshake et al. 2023)](https://arxiv.org/abs/2302.12173). *Why a retrieved document can hijack your LLM — the threat input rails defend against.*
4. **Build output rails** — watch [How to implement LLM guardrails for RAG applications](https://www.youtube.com/watch?v=l5K4r_TJz_8) (**IBM Developer**). *Fact-checking retrieved context + blocking unsafe outputs in a RAG pipeline.*
5. **Read the sources** — skim [NeMo Guardrails (Rebedea et al. 2023)](https://arxiv.org/abs/2310.10501) and [Llama Guard (Inan et al. 2023)](https://arxiv.org/abs/2312.06674). *Programmable rails, and the trained input/output safety classifier.*

**In this platform**:
- [01 RAG Fundamentals](/ai-ml/practitioner-workflows/llm-applications/rag-foundations/rag-foundations) — a foundation this builds on.
- [05 Hybrid Search (the DenseRetriever)](/ai-ml/practitioner-workflows/llm-applications/hybrid-search/hybrid-search) — machinery reused here.
- [08 Advanced RAG (Self-RAG support check)](/ai-ml/practitioner-workflows/llm-applications/advanced-rag/advanced-rag) — a foundation this builds on.
- [11 RAG Evaluation (the faithfulness/grounding proxy)](/ai-ml/practitioner-workflows/llm-applications/rag-evaluation/rag-evaluation) — machinery reused here.
- [13 Citations & Attribution (the grounding cosine + cosine≠entailment caveat)](/ai-ml/practitioner-workflows/llm-applications/citations-and-attribution/citations-and-attribution) — machinery reused here.
- [15 LLM App Orchestration](/ai-ml/practitioner-workflows/agentic-systems/llm-app-orchestration/llm-app-orchestration) — a related page.
- [8.01 In-Context Learning & Prompting](/ai-ml/ai-ml-intuitions/reasoning-and-agency/in-context-behavior/in-context-learning-and-prompting-intuition) — concept depth (the *why*).
- [ai-ml-intuitions 8.02 Retrieval-Augmented Generation](/ai-ml/ai-ml-intuitions/memory-retrieval-and-context/retrieval-augmented-generation/rag-intuition) — concept depth (the *why*).
- [Guardrails & Hallucination Mitigation](/ai-ml/ai-ml-learning-resources/evaluation/hallucination-and-grounding/hallucination-and-grounding) — the concept page (full explanation).
- [LLMs — Hallucination & Alignment Basics](/ai-ml/ai-ml-learning-resources/evaluation/alignment-and-safety-evaluation/alignment-and-safety-evaluation) — related domain.
- [Prompt Injection and Agent Guardrails](/ai-ml/practitioner-workflows/agentic-systems/prompt-injection-and-agent-guardrails/prompt-injection-and-agent-guardrails) — the injection attack surface and architectural defenses in depth.

**Videos**:
- [How to implement LLM guardrails for RAG applications](https://www.youtube.com/watch?v=l5K4r_TJz_8) — **IBM Developer** — fact-checking and output moderation inside a RAG pipeline.
- [How We Build Effective Agents](https://www.youtube.com/watch?v=D7_ipDqhtwk) — **Barry Zhang (Anthropic), AI Engineer** — where checks belong inside a production loop, and why a validator that only inspects the final answer catches the failure far too late.
- [What are guardrails for LLMs?](https://www.youtube.com/watch?v=FLOXGvqdwbM) — **Red Hat** — a clear conceptual overview of input/output rails and why they exist.

**Courses**:
- [Building & Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) — **DeepLearning.AI × TruLens** — groundedness checks are the core hallucination guardrail; this teaches measuring them.
- [Red Teaming LLM Applications](https://www.deeplearning.ai/short-courses/red-teaming-llm-applications/) — **DeepLearning.AI × Giskard** — how to probe an app for injection/jailbreak/leakage — the attacks guardrails must stop.

**Interactive**:
- [Adversarial Prompting / Risks](https://www.promptingguide.ai/risks/adversarial) — **DAIR.AI** — a catalogue of prompt injection & jailbreak techniques that input rails must defend against.
- [Azure AI Content Safety — Prompt Shields quickstart](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-jailbreak) — **Microsoft** — detect direct and indirect prompt-injection attacks against your app, hands-on.
- [Guardrails AI — docs & quickstart](https://www.guardrailsai.com/docs) — **Guardrails AI** — a runnable, free walkthrough of `Guard` objects and input/output validators.

**Articles**:
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) — **OWASP GenAI Security Project** — the checklist form of this page: each risk with its recognized mitigations, useful for structuring a design-review answer.
- [Prompt injection — the ongoing series](https://simonwillison.net/series/prompt-injection/) — **Simon Willison** — the running record of attacks that defeat instruction-level rails; read it before believing any guardrail that lives only in a system prompt.
- [What Are AI Guardrails?](https://www.ibm.com/think/topics/ai-guardrails) — **IBM** — the categories of guardrails and how they reduce risk, clearly organized.

**Papers**:
- [Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations](https://arxiv.org/abs/2312.06674) — **Inan et al. (2023)** — the trained input/output safety classifier over a risk taxonomy; the generalizing answer to regex bypass.
- [NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails](https://arxiv.org/abs/2310.10501) — **Rebedea et al. (2023, EMNLP demo)** — the five programmable rail categories (input/dialog/retrieval/execution/output) and the Colang language.
- [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) — **Greshake et al. (2023)** — the threat model the input rail defends against: instructions planted in retrieved content that the LLM then follows.
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — **Lewis et al. (2020)** — the RAG pipeline these guardrails wrap.
- [Selective Classification for Deep Neural Networks](https://arxiv.org/abs/1705.08500) — **Geifman & El-Yaniv (2017, NeurIPS)** — the reject-option / risk-coverage framework behind grounding-based abstention and the false-refuse/false-allow tradeoff.
- [SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models](https://arxiv.org/abs/2303.08896) — **Manakul, Liusie & Gales (2023, EMNLP)** — a sampling-based output rail that flags non-self-consistent (likely hallucinated) claims with no gold context.
- [Survey of Hallucination in Natural Language Generation](https://arxiv.org/abs/2202.03629) — **Ji et al. (2022)** — the reference taxonomy of hallucination types and mitigations the output rail targets.

**Documentation**:
- [Groundedness detection (Azure AI Content Safety)](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/groundedness) — **Microsoft** — the production output rail: detect (and correct) ungrounded generations against provided sources.
- [Prompt Shields in Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection) — **Microsoft** — how the production input rail detects direct + indirect injection, with the API.

**Books**:
- [Speech and Language Processing, 3rd ed. — Ch. 14 "Question Answering & Information Retrieval"](https://web.stanford.edu/~jurafsky/slp3/14.pdf) — **Jurafsky & Martin** — grounding and answer-faithfulness/abstention foundations behind output guardrails, free PDF.

**Resources**:
- [guardrails-ai/guardrails (GitHub)](https://github.com/guardrails-ai/guardrails) — **Guardrails AI** — validators for structure, PII, toxicity, and hallucination, open source.
- [NVIDIA NeMo-Guardrails (GitHub)](https://github.com/NVIDIA-NeMo/Guardrails) — **NVIDIA** — the open-source toolkit with runnable examples of input/dialog/output rails.
