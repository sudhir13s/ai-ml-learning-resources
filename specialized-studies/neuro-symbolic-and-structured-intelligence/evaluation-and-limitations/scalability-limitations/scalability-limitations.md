---
id: "specialized-studies/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/scalability-limitations"
topic: "Scalability Limitations"
level: advanced
built_from: ["specialized-studies/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/interpretability-and-verifiability", "specialized-studies/neuro-symbolic-and-structured-intelligence/structured-reasoning/constraint-guided-learning"]
leads_to: ["specialized-studies/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/open-problems"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Scalability Limitations"
minutes: 16
category: evaluation-and-limitations
---

# Scalability Limitations
> Exact reasoning is expensive in a way that gradient descent is not. **Grounding** a first-order
> rule set instantiates it over every combination of objects; **exact probabilistic inference**
> over the result is `#P`-hard in general; and every rule in the knowledge base was written by a
> person who had to be asked. The one sentence: **the symbolic half buys guarantees with compute
> and human effort, and both bills grow faster than the neural half's.**

**Why it matters:** this is why elegant neuro-symbolic systems stay small. A method that is exact
on MNIST-addition can become intractable on a real domain, so practitioners reach for relaxations
— approximate inference, independence assumptions, fuzzy logic — and each relaxation gives back
part of the guarantee that motivated the symbolic component. The interview question worth
preparing: **what exactly did your approximation cost you**, stated as a property (soundness,
calibration, the ability to represent multiple valid options) rather than as a percentage.

**Start here — suggested path:**

1. **See the cost named** — read [A-NeSI: A Scalable Approximate Method for Probabilistic Neurosymbolic Inference](https://arxiv.org/abs/2212.12393) — **van Krieken, Thanapalasingam, Tomczak et al. (2023)**. *Why exact probabilistic reasoning over symbols is exponential, and what an approximate inference network gives up.*
2. **See what the standard shortcut breaks** — read [On the Independence Assumption in Neurosymbolic Learning](https://arxiv.org/abs/2404.08458) — **van Krieken et al. (ICML, 2024)**. *Conditionally independent symbols make models overconfident and the loss landscape disconnected.*
3. **See the semantics fail quietly** — read [Symbol Grounding in Neuro-Symbolic AI: A Gentle Introduction to Reasoning Shortcuts](https://arxiv.org/abs/2510.14538) — **Emanuele Marconato et al. (2025)**. *A system can satisfy every constraint while assigning the wrong meaning to its own symbols.*
4. **Watch the tractability theory** — watch [Tractable Probabilistic Circuits](https://www.youtube.com/watch?v=oXE5XXgLXK0) — **Simons Institute for the Theory of Computing**. *Which structural properties make an exact query cheap, and why most knowledge bases lack them.*
5. **See the human bottleneck** — read [Getting from Generative AI to Trustworthy AI: What LLMs might learn from Cyc](https://arxiv.org/abs/2308.04445) — **Doug Lenat & Gary Marcus (2023)**. *Thirty-five years of hand-curated knowledge, honestly accounted: what it bought and what it cost.*

## Courses (free)
- [CS267A: Probabilistic Programming and Relational Learning](https://web.cs.ucla.edu/~guyvdb/teaching/cs267a/) — **Guy Van den Broeck (UCLA)** — weighted model counting, lifted inference, and the complexity results that set the ceiling.
- [Neuro-Symbolic AI Summer School 2025 — Day 1](https://www.youtube.com/live/zVJ59vIden0) — **Centaur AI Institute and the Neuro-Symbolic AI Community** — the community's own account of what currently scales and what does not.

## Videos
- [Tractable Probabilistic Circuits](https://www.youtube.com/watch?v=oXE5XXgLXK0) — **Simons Institute for the Theory of Computing** — the exact-inference tractability story, told through circuit structure rather than through benchmarks.
- [Logic and Probabilistic Circuits](https://www.youtube.com/watch?v=ZW94kMFsHzc) — **Simons Institute for the Theory of Computing** — compiling logic to circuits, and where the compilation blows up.

## Key Papers
- [A-NeSI](https://arxiv.org/abs/2212.12393) — **van Krieken et al. (2023)** — approximate probabilistic neurosymbolic inference; the clearest statement of the exponential problem and one answer to it.
- [On the Independence Assumption in Neurosymbolic Learning](https://arxiv.org/abs/2404.08458) — **van Krieken et al. (2024)** — proofs that the cheap assumption biases models toward overconfidence.
- [Symbol Grounding in Neuro-Symbolic AI: A Gentle Introduction to Reasoning Shortcuts](https://arxiv.org/abs/2510.14538) — **Marconato et al. (2025)** — the failure that survives every accuracy metric: right answers from wrong concepts.
- [DeepProbLog: Neural Probabilistic Logic Programming](https://arxiv.org/abs/1805.10872) — **Manhaeve, Dumančić, Kimmig, Demeester & De Raedt (2018)** — the reference system, and the grounding cost that limits how large its programs can be.
- [Scallop: A Language for Neurosymbolic Programming](https://arxiv.org/abs/2304.04812) — **Li, Huang, Naik et al. (2023)** — provenance semirings as a tunable knob: pay less reasoning for more speed, explicitly.
- [Getting from Generative AI to Trustworthy AI: What LLMs might learn from Cyc](https://arxiv.org/abs/2308.04445) — **Lenat & Marcus (2023)** — the knowledge-acquisition bottleneck, described by the person who spent a career inside it.
- [Neurosymbolic AI: The 3rd Wave](https://arxiv.org/abs/2012.05876) — **d'Avila Garcez & Lamb (2020)** — the agenda, including the scaling obstacles the field set itself.
- [Towards Data- and Knowledge-Driven AI: A Survey on Neuro-Symbolic Computing](https://arxiv.org/abs/2210.15889) — **Wenguan Wang, Yi Yang & Fei Wu (2022)** — a systematic survey; useful for seeing which families have ever been run at scale.
- [Defining neurosymbolic AI](https://arxiv.org/abs/2507.11127) — **De Smet & De Raedt (2025)** — a precise definition, which is what makes "this does not scale" a checkable statement rather than a mood.
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) — **Kaplan, McCandlish, Henighan et al. (2020)** — the opposing curve: the neural half has a predictable return on compute that the symbolic half lacks.

## Articles / Blogs (free, no paywall)
- [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) — **Richard Sutton** — the strongest short argument against hand-built structure; read it as the case your design has to answer.
- [Statistical and Relational Artificial Intelligence lab](http://starai.cs.ucla.edu/) — **Guy Van den Broeck's group (UCLA)** — the tractability literature, including which query classes stay polynomial.
- [Automated Reasoning Group](http://reasoning.cs.ucla.edu/) — **Adnan Darwiche's group (UCLA)** — knowledge compilation and model counting: the machinery whose cost this page is about.
- [Scallop](https://www.scallop-lang.org/) — **University of Pennsylvania** — install it and watch the runtime change as you widen the provenance setting; the trade-off becomes concrete in minutes.

## Books (free, with chapters)
- [*Probabilistic Circuits: A Unifying Framework for Tractable Probabilistic Models*](http://starai.cs.ucla.edu/papers/ProbCirc20.pdf) — **Choi, Vergari & Van den Broeck** — free monograph; decomposability, smoothness, determinism, and exactly which queries each property makes cheap.

## In this platform
- Previous in this section: [Interpretability and Verifiability](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/interpretability-and-verifiability/interpretability-and-verifiability)
- Next in this section: [Open Problems](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/open-problems/open-problems)
- What is being scaled: [Constraint-Guided Learning](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/structured-reasoning/constraint-guided-learning/constraint-guided-learning) · [Neuro-Symbolic AI](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai/neuro-symbolic-ai)
- Related elsewhere: [Knowledge Representation](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-representation/knowledge-representation) · [Probabilistic Reasoning and Graphical Models](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/probabilistic-reasoning-and-graphical-models/probabilistic-reasoning-and-graphical-models)
