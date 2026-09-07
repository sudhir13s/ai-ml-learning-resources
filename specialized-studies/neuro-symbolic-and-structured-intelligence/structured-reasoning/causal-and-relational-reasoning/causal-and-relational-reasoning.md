---
id: "specialized-studies/neuro-symbolic-and-structured-intelligence/structured-reasoning/causal-and-relational-reasoning"
topic: "Causal and Relational Reasoning"
level: advanced
built_from: ["probabilistic-reasoning-and-graphical-models", "knowledge-graphs"]
leads_to: ["specialized-studies/neuro-symbolic-and-structured-intelligence/modern-applications/program-synthesis-and-code-reasoning"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 17
title: "Causal and Relational Reasoning"
minutes: 17
category: structured-reasoning
---

# Causal and Relational Reasoning
> Two kinds of structure a purely statistical model does not get for free. **Causal** structure says
> what happens when you *intervene* rather than merely observe — Pearl's ladder climbs from
> association to intervention to counterfactuals. **Relational** structure says the world is made of
> entities and relations, so a model should generalize over them compositionally rather than memorize
> particular arrangements.

**Why it matters:** correlation-fitted models fail exactly where decisions are made — pricing,
policy, treatment, recommendation under a changed regime — because those are interventional
questions asked of an observational fit. And the relational half explains a persistent evaluation
result: models that score well on familiar arrangements still fall over on novel compositions of the
same parts. Both gaps are why structure keeps getting added back.

**Start here — suggested path:**

1. **Take the free course** — [Introduction to Causal Inference](https://www.bradyneal.com/causal-inference-course) — **Brady Neal**. *A causality course written for machine-learning people: potential outcomes and graphs in one syllabus, with the book PDF free.*
2. **Learn the ladder** — read [The Seven Tools of Causal Inference, with Reflections on Machine Learning](https://ftp.cs.ucla.edu/pub/stat_ser/r481.pdf) — **Judea Pearl (2018)**. *Association, intervention, counterfactual — and what each rung requires you to assume.*
3. **Get the machine-learning framing** — read [Causality for Machine Learning](https://arxiv.org/abs/1911.10500) — **Bernhard Schölkopf (2019)**. *Why independent causal mechanisms explain transfer, distribution shift, and data efficiency.*
4. **Add the relational half** — read [Relational inductive biases, deep learning, and graph networks](https://arxiv.org/abs/1806.01261) — **Battaglia et al. (2018)**. *Entities, relations, and the argument that combinatorial generalization needs structure in the architecture.*
5. **Check the frontier** — read [Towards Causal Representation Learning](https://arxiv.org/abs/2102.11107) — **Schölkopf, Locatello, Bauer et al. (2021)**. *Learning the causal variables themselves, rather than assuming somebody handed you the graph.*

## Courses (free)
- [Introduction to Causal Inference](https://www.bradyneal.com/causal-inference-course) — **Brady Neal** — free course page with lectures, slides, homework, and the complete book PDF; the best free entry point for an ML audience.
- [Causal Inference Course Lectures](https://www.youtube.com/playlist?list=PLoazKTcS0Rzb6bb9L508cyJ1z-U9iWkA0) — **Brady Neal** — the full video series that accompanies it, one concept per short video.

## Videos
- [Causal Inference Course Lectures](https://www.youtube.com/playlist?list=PLoazKTcS0Rzb6bb9L508cyJ1z-U9iWkA0) — **Brady Neal** — graphical models, identification, adjustment, and estimation, taught cleanly and without economics prerequisites.
- [A brief introduction to causal inference](https://www.youtube.com/watch?v=n8HFNel9xpU) — **Brady Neal (VMLW 2021)** — a one-hour version if you want the shape before committing to the course.

## Key Papers
- [The Seven Tools of Causal Inference, with Reflections on Machine Learning](https://ftp.cs.ucla.edu/pub/stat_ser/r481.pdf) — **Judea Pearl (2018)** — the ladder of causation and the seven capabilities structural causal models buy.
- [Causality for Machine Learning](https://arxiv.org/abs/1911.10500) — **Bernhard Schölkopf (2019)** — independent causal mechanisms, and why they matter for robustness and transfer.
- [Towards Causal Representation Learning](https://arxiv.org/abs/2102.11107) — **Schölkopf, Locatello, Bauer et al. (2021)** — the agenda paper connecting causality to representation learning.
- [Relational inductive biases, deep learning, and graph networks](https://arxiv.org/abs/1806.01261) — **Battaglia et al. (2018)** — the graph-network formalism and the case for relational structure as an architectural prior.
- [Causal Inference in Statistics: An Overview](https://ftp.cs.ucla.edu/pub/stat_ser/r350.pdf) — **Judea Pearl (2009)** — the compact technical introduction to structural causal models, the do-operator, and identification.
- [Generalization without Systematicity (SCAN)](https://arxiv.org/abs/1711.00350) — **Brenden Lake & Marco Baroni (2018)** — the experiment that made compositional-generalization failure measurable rather than anecdotal.

## Articles / Blogs (free, no paywall)
- [Causal Models](https://plato.stanford.edu/entries/causal-models/) — **Stanford Encyclopedia of Philosophy** — free, precise treatment of structural equations, interventions, and counterfactuals.
- [The Book of Why — companion page](http://bayes.cs.ucla.edu/WHY/) — **Judea Pearl (UCLA Cognitive Systems Laboratory)** — free supporting material, errata, and technical notes for the popular book; the book itself is a paid pointer.

## Books (free, with chapters)
- [*Introduction to Causal Inference from a Machine Learning Perspective* — Ch. 2 "Potential Outcomes", Ch. 3 "The Flow of Association and Causation in Graphs"](https://www.bradyneal.com/Introduction_to_Causal_Inference-Dec17_2020-Neal.pdf) — **Brady Neal** — free PDF; the course's text.
- [*Causal Inference: What If*](https://miguelhernan.org/whatifbook) — **Miguel Hernán & James Robins (Harvard)** — free PDF; the rigorous standard reference for identification and estimation.

## In this platform
- Prerequisites: [Probabilistic Reasoning and Graphical Models](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/probabilistic-reasoning-and-graphical-models/probabilistic-reasoning-and-graphical-models) · [Knowledge Graphs](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-graphs/knowledge-graphs)
- The mathematical depth page (canonical home): [Causal Inference](/ai-ml/ai-ml-learning-resources/specialized-studies/advanced-mathematics-for-ai-research/causal-inference/causal-inference)
- Neighbours: [Neuro-Symbolic AI](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai/neuro-symbolic-ai) · [Program Synthesis and Code Reasoning](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/modern-applications/program-synthesis-and-code-reasoning/program-synthesis-and-code-reasoning)
