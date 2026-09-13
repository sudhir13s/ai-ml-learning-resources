---
id: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/rules-constraints-and-ontologies"
topic: "Rules, Constraints and Ontologies"
core_idea: "Symbolic knowledge in working systems is production rules, constraints or ontologies, and choosing among them means trading expressiveness against tractability, where too rich a formalism returns no answer."
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

## References

The curated link library for this topic — in this platform, videos, courses, articles, papers, books — lives in a companion file so it can be reused as a standalone reference list:

**→ [Rules, Constraints and Ontologies — references](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/rules-constraints-and-ontologies/rules-constraints-and-ontologies#references-further-reading)**
