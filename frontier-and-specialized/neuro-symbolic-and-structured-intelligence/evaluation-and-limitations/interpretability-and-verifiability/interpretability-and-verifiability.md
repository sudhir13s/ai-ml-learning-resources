---
id: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/interpretability-and-verifiability"
topic: "Interpretability and Verifiability"
level: advanced
built_from: ["frontier-and-specialized/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/evaluating-symbolic-correctness", "what-is-mechanistic-interpretability"]
leads_to: ["frontier-and-specialized/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/scalability-limitations", "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/open-problems"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Interpretability and Verifiability"
minutes: 16
category: evaluation-and-limitations
---

# Interpretability and Verifiability
> A symbolic trace looks like an explanation, and often is not one. **Verifiable by construction**
> means the output was produced by a process whose validity you can check — a proof, a program, a
> constraint-satisfying layer. **Post-hoc explanation** means a story generated after the fact,
> including the model's own chain of thought. The one sentence: **a trace tells you what the system
> said it did, and only a checker tells you what it actually did.**

**Why it matters:** the 2025 evidence is blunt. Anthropic's alignment team found that reasoning
models mentioned a hint they had demonstrably used in roughly **25% of cases for Claude 3.7 Sonnet
and 39% for DeepSeek R1** — so monitoring the chain of thought cannot be relied on to catch rare
bad behaviour. That result is the strongest practical argument for the neuro-symbolic position:
if the reasoning artefact is a Lean proof or an executed program, faithfulness is not a research
question. What interviewers probe: **can you distinguish faithfulness, plausibility, and
legibility**, and say which of them your system's trace actually delivers.

**Start here — suggested path:**

1. **Read the headline result** — read [Reasoning models don't always say what they think](https://www.anthropic.com/research/reasoning-models-dont-say-think) — **Anthropic Alignment Science Team**. *The hint experiment, stated plainly, with the numbers and the safety implication.*
2. **Read the paper behind it** — read [Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410) — **Chen, Benton, Radhakrishnan et al., Anthropic (2025)**. *Method, models, and the outcome-based reinforcement-learning experiments that did not fix faithfulness.*
3. **See the earlier demonstration** — read [Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting](https://arxiv.org/abs/2305.04388) — **Turpin, Michael, Perez & Bowman (2023)**. *Bias the input invisibly, and the stated reasoning changes to justify the biased answer.*
4. **Watch what a real internal trace looks like** — watch [Tracing the thoughts of a large language model](https://www.youtube.com/watch?v=Bj9BD2D3DzA) — **Anthropic**. *Attribution graphs over features: the mechanistic picture that a verbal trace is being compared against.*
5. **Take the design lesson** — read [Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead](https://arxiv.org/abs/1811.10154) — **Cynthia Rudin (2019)**. *The case for building the constraint in rather than explaining afterwards; the position the whole sub-area rests on.*

## Courses (free)
- [ARENA: Alignment Research Engineer Accelerator](https://www.arena.education/) — **ARENA** — free curriculum with the interpretability chapters (transformer internals, sparse autoencoders) as runnable exercises.
- [Mechanistic Interpretability — getting started](https://www.neelnanda.io/mechanistic-interpretability/getting-started) — **Neel Nanda (Google DeepMind)** — the standard self-study path, sequenced by someone who teaches it full time.

## Videos
- [Tracing the thoughts of a large language model](https://www.youtube.com/watch?v=Bj9BD2D3DzA) — **Anthropic** — circuit tracing explained by the team that built it, with worked examples of planning and multi-step inference.
- [Mechanistic Interpretability](https://www.youtube.com/watch?v=yG3TxLPO_Uc) — **Neel Nanda (HAAISS 2024)** — what the field can and cannot currently establish about a model's internal computation.

## Key Papers
- [Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410) — **Chen, Benton, Radhakrishnan et al., Anthropic (2025)** — the 2025 faithfulness measurement that reset expectations for chain-of-thought monitoring.
- [Language Models Don't Always Say What They Think](https://arxiv.org/abs/2305.04388) — **Turpin, Michael, Perez & Bowman (2023)** — unfaithful explanations produced by invisible biasing features.
- [Measuring Faithfulness in Chain-of-Thought Reasoning](https://arxiv.org/abs/2307.13702) — **Lanham, Chen, Radhakrishnan et al., Anthropic (2023)** — perturb the chain and see whether the answer moves; the operational definition of faithfulness.
- [Chain-of-Thought Reasoning In The Wild Is Not Always Faithful](https://arxiv.org/abs/2503.08679) — **Arcuschin, Janiak, Krzyzanowski, Rajamanoharan, Nanda & Conmy (2025)** — unfaithfulness without artificial prompts, on ordinary tasks.
- [Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety](https://arxiv.org/abs/2507.11473) — **Korbak, Balesni, Barnes et al. (2025)** — the cross-lab position paper: monitorability is a property that training decisions can destroy.
- [Towards A Rigorous Science of Interpretable Machine Learning](https://arxiv.org/abs/1702.08608) — **Doshi-Velez & Kim (2017)** — the taxonomy that separates "explanation" claims from evaluation claims.
- [Stop Explaining Black Box Machine Learning Models for High Stakes Decisions](https://arxiv.org/abs/1811.10154) — **Rudin (2019)** — interpretable-by-construction as an engineering requirement, not a preference.
- [Interpretable Machine Learning: Fundamental Principles and 10 Grand Challenges](https://arxiv.org/abs/2103.11251) — **Rudin, Chen, Chen, Huang, Semenova & Zhong (2021)** — the open problems, including sparse logical models and constrained scoring systems.
- [Mechanistic Interpretability for AI Safety — A Review](https://arxiv.org/abs/2404.14082) — **Bereska & Gavves (2024)** — the survey of what internal analysis can currently establish, with its limits stated.

## Articles / Blogs (free, no paywall)
- [Reasoning models don't always say what they think](https://www.anthropic.com/research/reasoning-models-dont-say-think) — **Anthropic** — the readable version of the 2025 result; the source to quote in a discussion.
- [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) — **Anthropic (Transformer Circuits)** — attribution graphs applied to planning, arithmetic, and multilingual features; a mechanistic trace with no verbal claim attached.
- [Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) — **Anthropic (Transformer Circuits)** — the method paper; read it before trusting any attribution-graph figure.
- [Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/) — **Olah, Cammarata, Schubert et al. (Distill)** — the founding claim that features and circuits are the right unit of explanation.

## Books (free, with chapters)
- [*Interpretable Machine Learning* — Ch. "Interpretable Models", Ch. "Model-Agnostic Methods"](https://christophm.github.io/interpretable-ml-book/) — **Christoph Molnar** — free online; the systematic separation of intrinsically interpretable models from post-hoc explanation.

## In this platform
- Previous in this section: [Evaluating Symbolic Correctness](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/evaluating-symbolic-correctness/evaluating-symbolic-correctness)
- Next in this section: [Scalability Limitations](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/scalability-limitations/scalability-limitations)
- The mechanism owner (canonical home): [What Is Mechanistic Interpretability](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/what-is-mechanistic-interpretability/what-is-mechanistic-interpretability) · [Transformer Circuits, Induction Heads and Attention Patterns](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/transformer-circuits-induction-heads-and-attention-patterns/transformer-circuits-induction-heads-and-attention-patterns) · [Superposition and Sparse Autoencoders](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/superposition-and-sparse-autoencoders/superposition-and-sparse-autoencoders)
- Related: [Chain-of-Thought and Reasoning](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/chain-of-thought-and-reasoning/chain-of-thought-and-reasoning) · [Safety and Alignment](/ai-ml/ai-ml-learning-resources/evaluation/alignment-and-safety-evaluation/alignment-and-safety-evaluation) · [Probing, Attribution and Feature Visualization](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/probing-attribution-and-feature-visualization/probing-attribution-and-feature-visualization)
