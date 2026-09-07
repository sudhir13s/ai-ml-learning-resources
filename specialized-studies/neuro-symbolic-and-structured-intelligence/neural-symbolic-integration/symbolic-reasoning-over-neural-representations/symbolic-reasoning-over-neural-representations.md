---
id: "specialized-studies/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/symbolic-reasoning-over-neural-representations"
topic: "Symbolic Reasoning over Neural Representations"
level: advanced
built_from: ["specialized-studies/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai", "specialized-studies/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neural-models-with-symbolic-constraints"]
leads_to: ["specialized-studies/neuro-symbolic-and-structured-intelligence/modern-applications/program-synthesis-and-code-reasoning", "what-is-mechanistic-interpretability"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 18
title: "Symbolic Reasoning over Neural Representations"
minutes: 18
category: neural-symbolic-integration
---

# Symbolic Reasoning over Neural Representations
> The direction of travel reverses. Instead of pushing symbols into a network, this page is about
> **pulling symbols out of one** and reasoning over them: naming the concepts a layer encodes,
> inducing programs that reproduce a learned behaviour, having a language model translate a problem
> into first-order logic or Python for a solver to answer, and treating sparse-autoencoder features
> as a discrete vocabulary the model itself uses. The one sentence: **the network is the perceptual
> front end; the symbols are read off it and reasoned about elsewhere.**

**Why it matters:** this is where interpretability and neuro-symbolic AI met in 2025. Anthropic's
attribution graphs trace a specific answer back through named features, Gemma Scope put hundreds of
sparse autoencoders (SAEs) in the open, and solver-backed pipelines such as Logic-LM and
program-aided models now beat chain-of-thought on constraint-heavy tasks. Interviewers probe the
honest limit, and it is the one people underrate: **an extracted symbol is a hypothesis about the
network, not a proof** — features can be an artefact of the dictionary you trained, and a faithful
sounding trace can still be post-hoc.

**Start here — suggested path:**

1. **See features get names** — read [Towards Monosemanticity: Decomposing Language Models With Dictionary Learning](https://transformer-circuits.pub/2023/monosemantic-features/index.html) — **Bricken, Templeton, Batson et al. (Anthropic)**. *Sparse dictionary learning turns polysemantic neurons into features you can label.*
2. **See it at frontier scale** — skim [Scaling Monosemanticity](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html) — **Templeton, Conerly, Marcus et al. (Anthropic)**. *Millions of features from a production model, with steering experiments that test whether the labels mean anything.*
3. **Reason over the extracted structure** — read [Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) — **Ameisen, Lindsey, Pearce et al. (Anthropic, 2025)**. *Attribution graphs: features become nodes and the answer becomes a path you can intervene on.*
4. **Let the model emit formal language** — read [Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning](https://arxiv.org/abs/2305.12295) — **Pan, Albalak, Wang & Wang (2023)**. *The model parses; the solver decides; solver errors are the repair signal.*
5. **Induce the program, not the answer** — watch [DreamCoder: Bootstrapping Inductive Program Synthesis with Wake-Sleep Library Learning](https://www.youtube.com/watch?v=NYIeP1hns6A) — **Kevin Ellis (Simons Institute)**. *A learned library of abstractions is a symbolic theory the network grew for itself.*

## Courses (free)
- [Introduction to Program Synthesis](https://people.csail.mit.edu/asolar/SynthesisCourse/) — **Armando Solar-Lezama (MIT)** — the canonical free course on searching program spaces; the formal half of program induction.
- [Neuro-Symbolic AI Summer School 2025](https://www.youtube.com/playlist?list=PLqk1rh3Hd4UoHA-RkG41JuLOiM-p5dqkG) — **Centaur AI Institute and the Neuro-Symbolic AI Community** — 2025 sessions on extracting and verifying structure from learned models.

## Videos
- [Neel Nanda — Mechanistic Interpretability: A Whirlwind Tour](https://www.youtube.com/watch?v=veT2VI4vHyU) — **FAR AI (Alignment Workshop)** — features, circuits, and superposition in one sitting, from the person leading the Google DeepMind team.
- [Neel Nanda — Our Pivot to Pragmatic Interpretability](https://www.youtube.com/watch?v=k93o4R145Os) — **FAR AI (Alignment Workshop, 2025)** — the 2025 course correction: what reading structure out of models did and did not deliver.
- [DreamCoder: Bootstrapping Inductive Program Synthesis with Wake-Sleep Library Learning](https://www.youtube.com/watch?v=NYIeP1hns6A) — **Simons Institute for the Theory of Computing (Kevin Ellis)** — how a system invents its own symbolic abstractions and a neural policy to search them.

## Key Papers
- [Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors (TCAV)](https://arxiv.org/abs/1711.11279) — **Kim, Wattenberg, Gilmer et al. (2017)** — test whether a human-named concept is actually used by a layer, with a significance test attached.
- [Concept Bottleneck Models](https://arxiv.org/abs/2007.04612) — **Koh, Nguyen, Tang, Mussmann, Pierson, Kim & Liang (2020)** — force the network to predict named concepts first, then the label from those concepts alone.
- [The Neuro-Symbolic Concept Learner](https://arxiv.org/abs/1904.12584) — **Mao, Gan, Kohli, Tenenbaum & Wu (2019)** — perception produces symbols, a program executes over them, and both are learned from language supervision.
- [DreamCoder: Growing Generalizable, Interpretable Knowledge with Wake-Sleep Bayesian Program Learning](https://arxiv.org/abs/2006.08381) — **Ellis, Wong, Nye, Sablé-Meyer, Cary, Morales, Hewitt, Solar-Lezama & Tenenbaum (2020)** — the library-learning loop that grows an interpretable domain language.
- [LILO: Learning Interpretable Libraries by Compressing and Documenting Code](https://arxiv.org/abs/2310.19791) — **Grand, Wong, Bowers et al. (2023)** — the same idea with a language model doing the compression and the documentation.
- [PAL: Program-aided Language Models](https://arxiv.org/abs/2211.10435) — **Gao, Madaan, Zhou, Alon, Liu, Yang, Callan & Neubig (2022)** — reasoning emitted as Python, executed by an interpreter; the arithmetic is never the model's job.
- [LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers](https://arxiv.org/abs/2310.15164) — **Olausson, Gu, Lipkin, Zhang, Solar-Lezama, Tenenbaum & Levy (2023)** — the model as semantic parser into first-order logic, with a prover as the decider, and a careful failure-mode analysis.
- [Gemma Scope: Open Sparse Autoencoders Everywhere All At Once on Gemma 2](https://arxiv.org/abs/2408.05147) — **Lieberum, Rajamanoharan, Conmy et al. (Google DeepMind, 2024)** — over 400 open SAEs; the reason this line of work is reproducible outside a frontier lab.

## Articles / Blogs (free, no paywall)
- [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) — **Anthropic (2025)** — attribution graphs applied to real behaviours: planning, multi-step inference, and refusals, with interventions that confirm or refute each story.
- [Neuronpedia](https://www.neuronpedia.org/) — **Neuronpedia (Johnny Lin, Joseph Bloom et al.)** — browse and search extracted features across open models; the fastest way to see what a "symbol" from an SAE looks like.

## Books (free, with chapters)
- [*Interpretable Machine Learning*](https://christophm.github.io/interpretable-ml-book/) — **Christoph Molnar** — free online; concept-based and example-based explanation methods with their assumptions stated.

## In this platform
- Prerequisites: [Neuro-Symbolic AI](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai/neuro-symbolic-ai) · [Neural Models with Symbolic Constraints](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neural-models-with-symbolic-constraints/neural-models-with-symbolic-constraints)
- The interpretability half, in depth: [What Is Mechanistic Interpretability](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/what-is-mechanistic-interpretability/what-is-mechanistic-interpretability) · [Superposition and Sparse Autoencoders](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/superposition-and-sparse-autoencoders/superposition-and-sparse-autoencoders) · [Transformer Circuits, Induction Heads and Attention Patterns](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/transformer-circuits-induction-heads-and-attention-patterns/transformer-circuits-induction-heads-and-attention-patterns) · [Probing, Attribution and Feature Visualization](/ai-ml/ai-ml-learning-resources/deep-learning/interpretability-and-analysis/probing-attribution-and-feature-visualization/probing-attribution-and-feature-visualization)
- Where it goes next: [Program Synthesis and Code Reasoning](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/modern-applications/program-synthesis-and-code-reasoning/program-synthesis-and-code-reasoning) · [Neural Theorem Proving](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/differentiable-reasoning/neural-theorem-proving/neural-theorem-proving)
- Applied: [Code Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/coding-and-computer-use-agents/code-agents) · [Tool Use and Function Calling](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/tool-use/tool-use)
