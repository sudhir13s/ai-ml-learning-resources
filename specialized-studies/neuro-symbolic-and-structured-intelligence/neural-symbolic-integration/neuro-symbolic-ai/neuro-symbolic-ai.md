---
id: "specialized-studies/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai"
topic: "Neuro-Symbolic AI"
level: advanced
built_from: ["neuro-symbolic-ai-overview", "logic-and-inference"]
leads_to: ["differentiable-programming", "neural-theorem-proving", "program-synthesis-and-code-reasoning"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 18
title: "Neuro-Symbolic AI"
minutes: 18
category: neural-symbolic-integration
---

# Neuro-Symbolic AI
> The depth page on integration: given a neural component and a symbolic one, **how are they wired
> together?** The design space runs from loose coupling (a model calls a solver as a tool) through
> symbolic knowledge injected as a differentiable loss, to fully hybrid systems where logic programs
> carry neural predicates and the whole thing is trained end to end.

**Why it matters:** the wiring decides everything — whether symbolic constraints are *guaranteed*
or merely *encouraged*, whether gradients can flow, and whether inference stays tractable. Kautz's
six categories exist precisely because "neuro-symbolic" otherwise describes systems with nothing in
common. Being able to place a system in that taxonomy, and say what its interface costs, is the
senior-level answer.

**Start here — suggested path:**

1. **Place any system in the taxonomy** — read [The 6 Types of Neuro-Symbolic Systems](https://harshakokel.com/posts/neurosymbolic-systems/) — **Harsha Kokel**, then the source: [The Third AI Summer](https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/19122) — **Henry Kautz (AI Magazine, 2022)**. *One example per category makes the distinctions stick.*
2. **Read the field's agenda** — [Neurosymbolic AI: The 3rd Wave](https://arxiv.org/abs/2012.05876) — **Garcez & Lamb (2020)**. *What integration is supposed to buy: learning, reasoning, and explanation together.*
3. **Study the tightest coupling** — [DeepProbLog: Neural Probabilistic Logic Programming](https://arxiv.org/abs/1805.10872) — **Manhaeve, Dumančić, Kimmig, Demeester & De Raedt (2018)**. *Neural predicates inside a probabilistic logic program, trained by backpropagating through inference.*
4. **Study the softer coupling** — [Logic Tensor Networks](https://arxiv.org/abs/2012.13635) — **Badreddine, d'Avila Garcez, Serafini & Spranger (2020)** and [A Semantic Loss Function for Deep Learning with Symbolic Knowledge](https://arxiv.org/abs/1711.11157) — **Xu, Zhang, Friedman, Liang & Van den Broeck (2017)**. *Logic relaxed into a differentiable penalty — cheaper, but only a soft guarantee.*
5. **Build something** — follow the [Scallop](https://www.scallop-lang.org/) tutorials — **University of Pennsylvania**. *A neurosymbolic programming language with PyTorch bindings; the abstraction becomes code you run.*

## Courses (free)
- [Neuro-Symbolic AI Summer School 2025 — Day 1](https://www.youtube.com/live/zVJ59vIden0) — **Centaur AI Institute and the Neuro-Symbolic AI Community** — the field's own 2025 school, free and complete; foundations and integration methods.
- [Stanford CS221: Artificial Intelligence — Principles and Techniques](https://stanford-cs221.github.io/autumn2024/) — **Stanford (Percy Liang, Dorsa Sadigh)** — the prerequisite half: logic, constraint satisfaction, and search taught alongside learning.

## Videos
- [AI Spotlight Seminar: Symbolic Reasoning for Large Language Models](https://www.youtube.com/watch?v=wApPzSqLVhY) — **Guy Van den Broeck (UCLA)** — probabilistic circuits and logical constraints as guarantees on top of neural predictions.
- [Neuro-Symbolic AI Summer School 2025 — Day 2](https://www.youtube.com/live/-uEx0IICBxg) — **Centaur AI Institute** — applications and current systems, from the researchers building them.

## Key Papers
- [Neurosymbolic AI: The 3rd Wave](https://arxiv.org/abs/2012.05876) — **Garcez & Lamb (2020)** — the survey that named the modern wave.
- [Defining neurosymbolic AI](https://arxiv.org/abs/2507.11127) — **De Smet & De Raedt (2025)** — a formal criterion for what counts, and why most "hybrid" systems do not.
- [DeepProbLog: Neural Probabilistic Logic Programming](https://arxiv.org/abs/1805.10872) — **Manhaeve et al. (2018)** — the reference point for tight, differentiable integration of logic and networks.
- [Logic Tensor Networks](https://arxiv.org/abs/2012.13635) — **Badreddine, d'Avila Garcez, Serafini & Spranger (2020)** — first-order logic grounded in real-valued tensors, learnable by gradient descent.
- [A Semantic Loss Function for Deep Learning with Symbolic Knowledge](https://arxiv.org/abs/1711.11157) — **Xu, Zhang, Friedman, Liang & Van den Broeck (2017)** — turning a logical constraint into a loss term, with the probabilistic derivation.
- [The Neuro-Symbolic Concept Learner](https://arxiv.org/abs/1904.12584) — **Mao, Gan, Kohli, Tenenbaum & Wu (2019)** — neural perception, symbolic program execution, learned jointly from language supervision.
- [Towards Cognitive AI Systems: a Survey and Prospective on Neuro-Symbolic AI](https://arxiv.org/abs/2401.01040) — **Wan et al. (2024)** — the systems and efficiency view: what these architectures cost to run.

## Articles / Blogs (free, no paywall)
- [Scallop: a language for neurosymbolic programming](https://www.scallop-lang.org/) — **University of Pennsylvania** — installable, documented, and the clearest way to see the ideas as code.
- [Neurosymbolic Artificial Intelligence (journal)](https://neurosymbolic-ai-journal.com/) — **IOS Press, open review** — every submission and its reviews are public; a live view of what the field argues about.
- [Neuro-symbolic AI at Arizona State University](https://neurosymbolic.asu.edu/) — **ASU (Paulo Shakarian et al.)** — course material, tutorials, and a maintained reading list.
- [AlphaGeometry: an Olympiad-level AI system for geometry](https://deepmind.google/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/) — **Google DeepMind** — the neural-proposer plus symbolic-deducer loop, explained by its authors.

## Books (free, with chapters)
- [*Artificial Intelligence: A Modern Approach* — Ch. 8-9 "First-Order Logic" and "Inference"](https://aima.cs.berkeley.edu/) — **Russell & Norvig** — the symbolic half these systems embed; free sample chapters.

## In this platform
- Orientation: [Neuro-Symbolic AI Overview](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/neuro-symbolic-ai-overview/neuro-symbolic-ai-overview) · [Symbolic AI and Good Old-Fashioned AI](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/symbolic-ai-and-good-old-fashioned-ai/symbolic-ai-and-good-old-fashioned-ai)
- Prerequisites: [Knowledge Representation](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-representation/knowledge-representation) · [Logic and Inference](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/logic-and-inference/logic-and-inference) · [Knowledge Graphs](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-graphs/knowledge-graphs)
- Where it goes next: [Differentiable Programming](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/differentiable-reasoning/differentiable-programming/differentiable-programming) · [Neural Theorem Proving](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/differentiable-reasoning/neural-theorem-proving/neural-theorem-proving) · [Program Synthesis and Code Reasoning](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/modern-applications/program-synthesis-and-code-reasoning/program-synthesis-and-code-reasoning)
- Applied: [Tool Use and Function Calling](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/tool-use/tool-use) · [Hallucination and Grounding](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/hallucination-and-grounding/hallucination-and-grounding)
