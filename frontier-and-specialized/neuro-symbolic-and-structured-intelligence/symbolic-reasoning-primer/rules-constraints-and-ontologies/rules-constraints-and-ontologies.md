---
id: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/rules-constraints-and-ontologies"
topic: "Rules, Constraints and Ontologies"
level: intermediate
built_from: ["frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-representation", "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/logic-and-inference"]
leads_to: ["frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-graphs", "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 17
title: "Rules, Constraints and Ontologies"
minutes: 17
category: symbolic-reasoning-primer
---

# Rules, Constraints and Ontologies
> The three shapes symbolic knowledge actually takes in working systems. **Production rules**
> ("if these facts hold, do this") fire forward through a working memory. **Constraints** say what
> a solution must satisfy and let a search engine — constraint satisfaction problem (CSP),
> satisfiability (SAT), or satisfiability modulo theories (SMT) — find one. **Ontologies** define
> the vocabulary itself, so a reasoner can derive that a *cardiologist* is a *doctor*. The one
> sentence: **rules act, constraints restrict, ontologies define.**

**Why it matters:** every solver-backed 2025–26 system runs on one of these three. A language model
that emits a **Z3** or **MiniZinc** model and lets the solver answer (Logic-LM, SatLM) is buying
exactly the guarantee a decoder cannot give. Interviewers probe whether you can pick the right
formalism — and the failure mode people underrate is **expressiveness bought at the price of
tractability**: a richer description logic, or a constraint model with a bad encoding, does not
return a slower answer, it returns no answer at all.

**Start here — suggested path:**

1. **Watch constraint propagation run** — watch [8. Constraints: Search, Domain Reduction](https://www.youtube.com/watch?v=dARl_gGrS4o) — **MIT OpenCourseWare (Patrick Winston)**. *Map colouring by hand until "propagate, then backtrack" is muscle memory.*
2. **Read the standard chapter** — read [*Artificial Intelligence: A Modern Approach* — Ch. 6 "Constraint Satisfaction Problems"](https://aima.cs.berkeley.edu/) — **Russell & Norvig**. *Arc consistency, backtracking search, and variable-ordering heuristics with pseudocode.*
3. **Drive a real solver** — work through the [Z3 Guide](https://microsoft.github.io/z3guide/) — **Microsoft Research (Nikolaj Bjørner, Leonardo de Moura et al.)**. *An in-browser SMT tutorial; you write constraints and get models or `unsat` back immediately.*
4. **Model, don't program** — skim the [MiniZinc Handbook](https://docs.minizinc.dev/en/stable/) — **MiniZinc team (Monash University and Data61)**. *A modelling language that separates "what must hold" from "which solver searches", which is the whole point of declarative constraints.*
5. **Write an ontology** — read [A Description Logic Primer](https://arxiv.org/abs/1201.4089) — **Krötzsch, Simančík & Horrocks (2012)**, then build one in [Protégé](https://github.com/protegeproject/protege) — **Stanford**. *Classes, properties, and the inferences a description-logic reasoner draws for free.*

## Courses (free)
- [MIT 6.034 Artificial Intelligence (Fall 2010)](https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/) — **MIT OpenCourseWare (Patrick Winston)** — rule-based expert systems and constraint propagation taught as executing machinery, with full lecture videos.
- [Stanford CS221: Artificial Intelligence — Principles and Techniques](https://stanford-cs221.github.io/autumn2024/) — **Stanford (Percy Liang, Dorsa Sadigh)** — free notes and assignments; the constraint-satisfaction unit covers factor graphs, backtracking, and beam search.
- [Programming Z3](https://theory.stanford.edu/~nikolaj/programmingz3.html) — **Nikolaj Bjørner, Leonardo de Moura, Lev Nachmanson & Christoph Wintersteiger** — the solver's own authors teaching its API, theories, and tactics; the reference tutorial for SMT in practice.

## Videos
- [8. Constraints: Search, Domain Reduction](https://www.youtube.com/watch?v=dARl_gGrS4o) — **MIT OpenCourseWare (Patrick Winston)** — domain reduction derived at the board; the clearest 50 minutes on why propagation beats naive search.
- [WORKSHOP: SAT/SMT Solvers](https://www.youtube.com/watch?v=DX3G4IoTNF0) — **Microsoft Research** — how modern SAT and SMT engines work and what they are used for, from the lab that builds Z3.
- [Knowledge Graphs (lecture)](https://www.youtube.com/playlist?list=PLar5iR7mhb4dJHDSjmeo6W7HomHBSZf9t) — **Knowledge-Based Systems, TU Dresden (Markus Krötzsch)** — a full university course; the Datalog, rules, and ontology lectures are the rigorous version of this page.

## Key Papers
- [Rete: A Fast Algorithm for the Many Pattern/Many Object Pattern Match Problem](https://www.sciencedirect.com/science/article/pii/0004370282900200) — **Charles Forgy (1982)** — the network that made production-rule systems fast enough to ship; still the core of every business-rule engine.
- [A Description Logic Primer](https://arxiv.org/abs/1201.4089) — **Krötzsch, Simančík & Horrocks (2012)** — the semantics under OWL written as a tutorial, by three of the people who standardised it.
- [Z3: An Efficient SMT Solver](https://doi.org/10.1007/978-3-540-78800-3_24) — **Leonardo de Moura & Nikolaj Bjørner (2008)** — the solver behind most program verification and, now, most solver-augmented language-model pipelines.
- [The Third AI Summer: AAAI Robert S. Engelmore Memorial Lecture](https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/19122) — **Henry Kautz (2022)** — a satisfiability researcher's account of what rule and constraint systems did and did not deliver.
- [Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning](https://arxiv.org/abs/2305.12295) — **Pan, Albalak, Wang & Wang (2023)** — the model writes the constraint program, the solver answers, and solver errors drive self-refinement.
- [SatLM: Satisfiability-Aided Language Models Using Declarative Prompting](https://arxiv.org/abs/2305.09656) — **Ye, Chen, Dillig & Durrett (2023)** — declarative specifications beat imperative programs whenever the task is really search, not arithmetic.

## Articles / Blogs (free, no paywall)
- [OWL 2 Profiles: An Introduction to Lightweight Ontology Languages](https://iccl.inf.tu-dresden.de/web/Inproceedings4014/en) — **Markus Krötzsch (Reasoning Web Summer School lecture notes)** — EL, QL, and RL: three deliberately weakened logics with tractable reasoning, the clearest statement of the expressiveness-tractability bargain.
- [Protégé](https://github.com/protegeproject/protege) — **Stanford Center for Biomedical Informatics Research** — the free ontology editor with pluggable reasoners; build a small ontology and watch inferred classes appear.
- [Drools](https://www.drools.org/) — **Red Hat / Drools community** — a production Rete-based rule engine with open documentation; what "business rules" means in real systems.
- [Potassco: the Potsdam Answer Set Solving Collection](https://potassco.org/) — **University of Potsdam** — answer set programming: rules plus constraints, grounded then solved, the flavour most used inside hybrid systems.

## Books (free, with chapters)
- [*Artificial Intelligence: A Modern Approach* — Ch. 6 "Constraint Satisfaction Problems", Ch. 12 "Knowledge Representation"](https://aima.cs.berkeley.edu/) — **Russell & Norvig** — free sample chapters; CSP algorithms and ontological engineering in one place.
- [*SAT/SMT by Example*](https://sat-smt.codes/) — **Dennis Yurichev** — a free, enormous book of worked encodings; the fastest way to learn how to turn a problem into constraints.

## In this platform
- Before this: [Knowledge Representation](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-representation/knowledge-representation) · [Logic and Inference](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/logic-and-inference/logic-and-inference)
- Next in this sub-area: [Knowledge Graphs](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-graphs/knowledge-graphs) · then [Neuro-Symbolic AI](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai/neuro-symbolic-ai)
- Where constraints meet networks: [Neural Models with Symbolic Constraints](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neural-models-with-symbolic-constraints/neural-models-with-symbolic-constraints) · [Differentiable Logic](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/differentiable-reasoning/differentiable-logic/differentiable-logic)
- Applied: [Tool Use and Function Calling](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/tool-use/tool-use) · [Graph RAG](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/graph-rag/graph-rag)
- Orientation: [Symbolic AI and Good Old-Fashioned AI](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/symbolic-ai-and-good-old-fashioned-ai/symbolic-ai-and-good-old-fashioned-ai)
