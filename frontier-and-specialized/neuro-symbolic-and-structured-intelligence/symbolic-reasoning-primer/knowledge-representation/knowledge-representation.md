---
id: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-representation"
topic: "Knowledge Representation"
level: intermediate
built_from: ["symbolic-ai-and-good-old-fashioned-ai"]
leads_to: ["frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/logic-and-inference", "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-graphs"]
interview_frequency: low
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Knowledge Representation"
minutes: 15
category: symbolic-reasoning-primer
---

# Knowledge Representation
> How you write down what a system knows so that something can **compute with it**: facts,
> entities, relations, types, rules, defaults, and constraints, in a formalism with a defined
> meaning. A representation is a bargain — it fixes what can be expressed, what can be inferred,
> and how expensive inference will be.

**Why it matters:** every knowledge-grounded system in 2026 is making representation choices, even
when nobody calls them that. A retrieval index, a tool schema, a function-calling signature, a
database of entities behind an agent — each one decides what the model can be held to. The
interview probe is the trade-off nobody escapes: **expressiveness versus tractability**, because
the richer the language, the more expensive (or undecidable) reasoning in it becomes.

**Start here — suggested path:**

1. **See the classical toolkit** — watch [Reasoning: Goal Trees and Rule-Based Expert Systems](https://www.youtube.com/watch?v=leXa7EKUPFk) — **MIT OpenCourseWare (Patrick Winston)**. *Rules, goal trees, and self-explanation, from a system you can follow line by line.*
2. **Read the founding proposal** — [Programs with Common Sense](http://www-formal.stanford.edu/jmc/mcc59.pdf) — **John McCarthy (1959)**. *Represent knowledge declaratively; let a general procedure draw the consequences.*
3. **Get the modern textbook treatment** — skim [*Artificial Intelligence: A Modern Approach* Part III](https://aima.cs.berkeley.edu/) — **Russell & Norvig**. *Ontologies, categories, events, defaults, and where each formalism's cost lies.*
4. **See representation as an engineering artifact** — read [Knowledge Graphs](https://kgbook.org/) Ch. 2-3 — **Hogan et al.** *How the same ideas are actually deployed: nodes, edges, schemas, shapes, and identity.*
5. **Understand the honest limits** — read [Logic and Artificial Intelligence](https://plato.stanford.edu/entries/logic-ai/) — **Stanford Encyclopedia of Philosophy (Richmond Thomason)**. *Why common-sense knowledge resisted formalization for forty years — the reason learning came back.*

## Courses (free)
- [MIT 6.034 Artificial Intelligence (Fall 2010)](https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/) — **MIT OpenCourseWare (Patrick Winston)** — representations first, algorithms second; still the clearest course on the subject.
- [Stanford CS221: Artificial Intelligence — Principles and Techniques](https://stanford-cs221.github.io/autumn2024/) — **Stanford (Percy Liang, Dorsa Sadigh)** — constraint satisfaction and logic modules give the current formal treatment.
- [Stanford CS520: Knowledge Graphs](https://web.stanford.edu/class/cs520/) — **Stanford (Vinay Chaudhri et al.)** — free seminar materials on how representation choices play out in deployed knowledge bases.

## Videos
- [MIT 6.034 Artificial Intelligence, Fall 2010 (full lecture series)](https://www.youtube.com/playlist?list=PLUl4u3cNGP63gFHB6xb-kVBiQHYe_4hSi) — **MIT OpenCourseWare** — the representation lectures (goal trees, rules, frames, constraint propagation) in sequence.
- [Stanford CS221: Artificial Intelligence (Autumn 2021)](https://www.youtube.com/playlist?list=PLoROMvodv4rOca_Ovz1DvdtWuz8BfSWL2) — **Stanford Online** — the constraint-satisfaction and logic blocks, taught for a modern audience.

## Key Papers
- [Programs with Common Sense](http://www-formal.stanford.edu/jmc/mcc59.pdf) — **John McCarthy (1959)** — the advice taker: the first argument for declarative knowledge plus general inference.
- [Steps Toward Artificial Intelligence](https://courses.csail.mit.edu/6.803/pdf/steps.pdf) — **Marvin Minsky (1961)** — the survey that framed representation, search, and learning as one problem.
- [Knowledge Graphs](https://arxiv.org/abs/2003.02320) — **Hogan et al. (2020)** — the comprehensive modern survey: data models, schemas, identity, context, and reasoning.
- [Knowledge Graphs: A Guided Tour](https://drops.dagstuhl.de/entities/document/10.4230/OASIcs.AIB.2022.1) — **Aidan Hogan (2022)** — a compact tour of representation choices and their consequences, from a leading author.

## Articles / Blogs (free, no paywall)
- [Logic and Artificial Intelligence](https://plato.stanford.edu/entries/logic-ai/) — **Stanford Encyclopedia of Philosophy** — free and rigorous on what formal representation promised and delivered.
- [Defeasible Reasoning](https://plato.stanford.edu/entries/reasoning-defeasible/) — **Stanford Encyclopedia of Philosophy** — defaults and exceptions: the part of common sense that classical logic handles badly.
- [Wikidata SPARQL tutorial](https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial) — **Wikimedia (Wikidata community)** — query the largest open knowledge base in the world and feel the representation from the inside.

## Books (free, with chapters)
- [*Artificial Intelligence: A Modern Approach* — Ch. 12 "Knowledge Representation"](https://aima.cs.berkeley.edu/) — **Russell & Norvig** — categories, objects, events, mental states, and default reasoning; free sample chapters on the book site.
- [*Knowledge Graphs*](https://kgbook.org/) — **Hogan, Blomqvist, Cochez et al.** — free open-access book; the current standard reference for representing knowledge at scale.

## In this platform
- Orientation: [Symbolic AI and Good Old-Fashioned AI](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/symbolic-ai-and-good-old-fashioned-ai/symbolic-ai-and-good-old-fashioned-ai) · [Neuro-Symbolic AI Overview](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/neuro-symbolic-ai-overview/neuro-symbolic-ai-overview)
- Next in this primer: [Logic and Inference](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/logic-and-inference/logic-and-inference) · [Knowledge Graphs](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-graphs/knowledge-graphs)
- Where representation meets learning: [Neuro-Symbolic AI](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai/neuro-symbolic-ai) · [Probabilistic Reasoning and Graphical Models](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/probabilistic-reasoning-and-graphical-models/probabilistic-reasoning-and-graphical-models)
