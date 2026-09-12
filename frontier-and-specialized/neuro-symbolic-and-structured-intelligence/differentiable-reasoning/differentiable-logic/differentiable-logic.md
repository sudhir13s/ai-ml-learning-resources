---
id: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/differentiable-reasoning/differentiable-logic"
topic: "Differentiable Logic"
level: advanced
built_from: ["frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/logic-and-inference", "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai"]
leads_to: ["frontier-and-specialized/neuro-symbolic-and-structured-intelligence/differentiable-reasoning/neural-theorem-proving", "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/differentiable-reasoning/differentiable-programming"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 18
title: "Differentiable Logic"
minutes: 18
category: differentiable-reasoning
---

# Differentiable Logic
> Logic is discrete: a formula is true or false, and there is no gradient in that. Differentiable
> logic **relaxes** it so a network can be trained through it. Two relaxations dominate. **Fuzzy**
> logic replaces conjunction with a t-norm and truth with a number in [0, 1]. **Probabilistic**
> logic keeps the semantics exact and computes the probability a formula holds by weighted model
> counting. The one sentence: **fuzzy is cheap and approximate; probabilistic is faithful and
> expensive — and every relaxation charges a price somewhere.**

**Why it matters:** this is the machinery under every "logic as a loss" claim, and knowing which
relaxation a system used tells you what it actually guarantees. In 2025–26 the field's own reviews
are sharper about the costs — vanishing or misdirected gradients from badly chosen operators,
exponential blow-up when a probabilistic program is grounded, and reasoning shortcuts where the
network satisfies the constraint for the wrong reason. Interviewers probe exactly this: **what did
you give up to get a gradient?**

**Start here — suggested path:**

1. **Find out which operators survive training** — read [Analyzing Differentiable Fuzzy Logic Operators](https://arxiv.org/abs/2002.06100) — **van Krieken, Acar & van Harmelen (2020)**. *A systematic study showing that most textbook t-norms are unusable as losses, and why.*
2. **See the exact alternative** — read [DeepProbLog: Neural Probabilistic Logic Programming](https://arxiv.org/abs/1805.10872) — **Manhaeve, Dumančić, Kimmig, Demeester & De Raedt (2018)**. *Neural predicates inside a probabilistic logic program, with gradients through exact inference.*
3. **Differentiate a solver** — read [SATNet: Bridging Deep Learning and Logical Reasoning Using a Differentiable Satisfiability Solver](https://arxiv.org/abs/1905.12149) — **Wang, Donti, Wilder & Kolter (2019)**. *A smoothed maximum-satisfiability layer; Sudoku learned from examples, no rules supplied.*
4. **Differentiate a proof** — read [End-to-End Differentiable Proving](https://arxiv.org/abs/1705.11040) — **Rocktäschel & Riedel (2017)**. *Backward chaining with unification replaced by a kernel over embeddings; interpretable rules fall out.*
5. **Learn the bill** — read [On the Independence Assumption in Neurosymbolic Learning](https://arxiv.org/abs/2404.08458) — **van Krieken, Minervini, Ponti & Vergari (2024)**. *The convenient independence assumption produces overconfident, disjunction-averse models; the analysis is the honest counterweight to the field's demos.*

## Courses (free)
- [Neuro-Symbolic AI Summer School 2025](https://www.youtube.com/playlist?list=PLqk1rh3Hd4UoHA-RkG41JuLOiM-p5dqkG) — **Centaur AI Institute and the Neuro-Symbolic AI Community** — free and current; the probabilistic-logic and tractable-inference sessions map directly onto this page.
- [Scallop tutorials](https://www.scallop-lang.org/) — **University of Pennsylvania** — differentiable Datalog with provenance semirings; you choose the relaxation and see what it costs at runtime.

## Videos
- [From Probabilistic Logics to Neuro-Symbolic Artificial Intelligence](https://www.youtube.com/watch?v=IT9KDheuS1o) — **RWTH Center for Artificial Intelligence (Luc De Raedt)** — the ProbLog-to-DeepProbLog line told by the person who built both.
- [AI Spotlight Seminar: Symbolic Reasoning for Large Language Models](https://www.youtube.com/watch?v=wApPzSqLVhY) — **Guy Van den Broeck (UCLA)** — weighted model counting and circuits as the exact route, contrasted with fuzzy penalties.
- [Neuro-Symbolic AI Summer School 2025 — Day 1](https://www.youtube.com/live/zVJ59vIden0) — **Centaur AI Institute** — foundations day: semantics, relaxations, and the frameworks that implement them.

## Key Papers
- [Analyzing Differentiable Fuzzy Logic Operators](https://arxiv.org/abs/2002.06100) — **van Krieken, Acar & van Harmelen (2020)** — the reference study of t-norms, t-conorms, and implications as differentiable operators.
- [DeepProbLog: Neural Probabilistic Logic Programming](https://arxiv.org/abs/1805.10872) — **Manhaeve et al. (2018)** — exact probabilistic semantics with neural predicates; the benchmark for tight integration.
- [Logic Tensor Networks](https://arxiv.org/abs/2012.13635) — **Badreddine, d'Avila Garcez, Serafini & Spranger (2020)** — real-valued first-order logic where satisfiability itself is the objective.
- [A Semantic Loss Function for Deep Learning with Symbolic Knowledge](https://arxiv.org/abs/1711.11157) — **Xu, Zhang, Friedman, Liang & Van den Broeck (2017)** — the weighted-model-counting derivation that makes a constraint a differentiable penalty.
- [SATNet: Bridging Deep Learning and Logical Reasoning Using a Differentiable Satisfiability Solver](https://arxiv.org/abs/1905.12149) — **Wang, Donti, Wilder & Kolter (2019)** — a semidefinite relaxation of MAXSAT as a trainable layer.
- [End-to-End Differentiable Proving](https://arxiv.org/abs/1705.11040) — **Rocktäschel & Riedel (2017)** — neural theorem proving over a knowledge base, with rules induced rather than written.
- [Learning Reasoning Strategies in End-to-End Differentiable Proving](https://arxiv.org/abs/2007.06477) — **Minervini, Riedel, Stenetorp, Grefenstette & Rocktäschel (2020)** — conditional theorem provers; how the intractable proof search of the original was tamed.
- [Scallop: A Language for Neurosymbolic Programming](https://arxiv.org/abs/2304.04812) — **Li, Huang & Naik (2023)** — provenance semirings as a dial between exactness and speed, implemented and benchmarked.
- [ULLER: A Unified Language for Learning and Reasoning](https://arxiv.org/abs/2405.00532) — **van Krieken, Badreddine, Manhaeve & Giunchiglia (2024)** — one syntax with classical, fuzzy, and probabilistic semantics, which makes the trade-offs comparable at last.
- [On Scaling Neurosymbolic Programming through Guided Logical Inference](https://arxiv.org/abs/2501.18202) — **Valentin, Werner, Genevès & Layaïda (2025)** — the scalability problem attacked directly: guided inference instead of full model counting.

## Articles / Blogs (free, no paywall)
- [ProbLog](https://dtai.cs.kuleuven.be/problog/) — **DTAI, KU Leuven** — the probabilistic logic programming language DeepProbLog extends, with an in-browser editor and tutorials.
- [SATNet](https://github.com/locuslab/SATNet) — **Locus Lab (Carnegie Mellon University)** — the differentiable MAXSAT layer as an installable PyTorch module; run the Sudoku experiment yourself.

## Books (free, with chapters)
- [*The Elements of Differentiable Programming*](https://diffprog.github.io/) — **Blondel & Roulet (Google DeepMind)** — free; smoothing, relaxation, and differentiating through discrete operations, stated properly.
- [*Probabilistic Machine Learning: Advanced Topics*](https://probml.github.io/pml-book/book2.html) — **Kevin Murphy** — free PDF; inference, model counting, and structured distributions, the background probabilistic logic assumes.

## In this platform
- Prerequisites: [Logic and Inference](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/logic-and-inference/logic-and-inference) · [Neuro-Symbolic AI](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai/neuro-symbolic-ai)
- Next in this sub-area: [Neural Theorem Proving](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/differentiable-reasoning/neural-theorem-proving/neural-theorem-proving) · [Differentiable Programming](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/differentiable-reasoning/differentiable-programming/differentiable-programming)
- The constraint view of the same relaxations: [Neural Models with Symbolic Constraints](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neural-models-with-symbolic-constraints/neural-models-with-symbolic-constraints) · [Rules, Constraints and Ontologies](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/rules-constraints-and-ontologies/rules-constraints-and-ontologies)
- Related elsewhere: [Probabilistic Reasoning and Graphical Models](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/probabilistic-reasoning-and-graphical-models/probabilistic-reasoning-and-graphical-models) · [Causal and Relational Reasoning](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/structured-reasoning/causal-and-relational-reasoning/causal-and-relational-reasoning)
