---
id: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/logic-and-inference"
topic: "Logic and Inference"
level: intermediate
built_from: ["knowledge-representation"]
leads_to: ["frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-graphs", "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai"]
interview_frequency: low
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Logic and Inference"
minutes: 16
category: symbolic-reasoning-primer
---

# Logic and Inference
> The machinery that turns stored knowledge into new conclusions: a **syntax** for writing
> sentences, a **semantics** that says when they are true, and **inference rules** that derive
> further sentences. The two properties you are always trading are **soundness** (never derive a
> falsehood) and **completeness** (derive everything that follows) — against how long the search
> takes.

**Why it matters:** inference is the guarantee a neural network cannot give. When a 2026 agent
calls a satisfiability (SAT) or satisfiability-modulo-theories (SMT) solver, type-checks generated
code, or has a proof assistant confirm a step, it is buying soundness from a logic engine. Knowing
propositional versus first-order logic, forward versus backward chaining, and why first-order
validity is only semi-decidable is the difference between "the model said so" and "the system
proved it".

**Start here — suggested path:**

1. **Watch inference run** — [Stanford CS221: Artificial Intelligence (Autumn 2021)](https://www.youtube.com/playlist?list=PLoROMvodv4rOca_Ovz1DvdtWuz8BfSWL2) — **Stanford Online**, the logic block. *Propositional syntax, models, modus ponens, and resolution, in order.*
2. **Read the standard chapters** — [*Artificial Intelligence: A Modern Approach* Ch. 7-9](https://aima.cs.berkeley.edu/) — **Russell & Norvig**. *Logical agents, first-order logic, and inference algorithms with pseudocode you can implement.*
3. **Do proofs yourself** — work through [*Logic and Proof*](https://avigad.github.io/logic_and_proof/) — **Jeremy Avigad, Robert Lewis & Floris van Doorn (Carnegie Mellon University)**. *A free book where every exercise is checked by the Lean proof assistant, so "sound" stops being a word.*
4. **Program in logic** — [*Learn Prolog Now!*](https://lpn.swi-prolog.org/) — **Blackburn, Bos & Striegnitz**. *Backward chaining and unification become obvious once you have written twenty lines of Prolog.*
5. **See the modern solver view** — [Potassco: the Potsdam Answer Set Solving Collection](https://potassco.org/) — **University of Potsdam**. *Answer set programming: declarative constraints solved by a grounder plus a SAT-style search, the flavour of logic most used in current hybrid systems.*

## Courses (free)
- [Stanford CS221: Artificial Intelligence — Principles and Techniques](https://stanford-cs221.github.io/autumn2024/) — **Stanford (Percy Liang, Dorsa Sadigh)** — free notes and assignments; the logic unit is short, formal, and modern.
- [MIT 6.034 Artificial Intelligence (Fall 2010)](https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/) — **MIT OpenCourseWare (Patrick Winston)** — rule-based inference and search, with the deduction traced by hand.
- [Natural Number Game](https://adam.math.hhu.de/) — **Lean community (Kevin Buzzard, Jon Eugster et al.)** — a free browser game that teaches formal proof by making you build one; the fastest hands-on route into inference.

## Videos
- [Stanford CS221: Artificial Intelligence (Autumn 2021)](https://www.youtube.com/playlist?list=PLoROMvodv4rOca_Ovz1DvdtWuz8BfSWL2) — **Stanford Online** — propositional and first-order logic, modus ponens, resolution, and their complexity.
- [Reasoning: Goal Trees and Rule-Based Expert Systems](https://www.youtube.com/watch?v=leXa7EKUPFk) — **MIT OpenCourseWare (Patrick Winston)** — forward and backward chaining shown as an executing system, not a definition.

## Key Papers
- [Programs with Common Sense](http://www-formal.stanford.edu/jmc/mcc59.pdf) — **John McCarthy (1959)** — the case for deriving behaviour from logical consequence.
- [Computer Science as Empirical Inquiry: Symbols and Search](https://dl.acm.org/doi/10.1145/360018.360022) — **Newell & Simon (1976)** — inference framed as heuristic search through a space of symbol structures, which is what solvers still do.
- [The Third AI Summer: AAAI Robert S. Engelmore Memorial Lecture](https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/19122) — **Henry Kautz (2022)** — a leading satisfiability researcher on where logical inference did and did not deliver.

## Articles / Blogs (free, no paywall)
- [Classical Logic](https://plato.stanford.edu/entries/logic-classical/) — **Stanford Encyclopedia of Philosophy (Stewart Shapiro)** — precise definitions of syntax, semantics, soundness, and completeness, free and citable.
- [Logic and Artificial Intelligence](https://plato.stanford.edu/entries/logic-ai/) — **Stanford Encyclopedia of Philosophy (Richmond Thomason)** — non-monotonic reasoning, the frame problem, and the limits of deduction for common sense.
- [SWI-Prolog](https://www.swi-prolog.org/) — **SWI-Prolog project** — the free implementation to run the examples in; the documentation doubles as a resolution tutorial.

## Books (free, with chapters)
- [*Logic and Proof*](https://avigad.github.io/logic_and_proof/) — **Avigad, Lewis & van Doorn (Carnegie Mellon University)** — free online; classical logic taught with machine-checked exercises.
- [*Artificial Intelligence: A Modern Approach* — Ch. 7 "Logical Agents", Ch. 9 "Inference in First-Order Logic"](https://aima.cs.berkeley.edu/) — **Russell & Norvig** — the reference treatment of resolution, unification, and chaining.
- [*Learn Prolog Now!*](https://lpn.swi-prolog.org/) — **Blackburn, Bos & Striegnitz** — free; logic programming from unification to cuts, with runnable code.

## In this platform
- Before this: [Knowledge Representation](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-representation/knowledge-representation) · [Symbolic AI and Good Old-Fashioned AI](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/symbolic-ai-and-good-old-fashioned-ai/symbolic-ai-and-good-old-fashioned-ai)
- After this: [Knowledge Graphs](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-graphs/knowledge-graphs) · [Neuro-Symbolic AI](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai/neuro-symbolic-ai) · [Neural Theorem Proving](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/differentiable-reasoning/neural-theorem-proving/neural-theorem-proving)
- Applied: [Tool Use and Function Calling](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/tool-use/tool-use) · [Chain-of-Thought and Reasoning](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/chain-of-thought-and-reasoning/chain-of-thought-and-reasoning)
