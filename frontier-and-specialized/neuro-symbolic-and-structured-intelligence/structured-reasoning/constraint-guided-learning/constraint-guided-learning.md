---
id: "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/structured-reasoning/constraint-guided-learning"
topic: "Constraint-Guided Learning"
level: advanced
built_from: ["frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai", "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/logic-and-inference"]
leads_to: ["frontier-and-specialized/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/evaluating-symbolic-correctness", "frontier-and-specialized/neuro-symbolic-and-structured-intelligence/modern-applications/neuro-symbolic-language-models"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 17
title: "Constraint-Guided Learning"
minutes: 17
category: structured-reasoning
---

# Constraint-Guided Learning
> Labels are not the only supervision available. **Rules** are supervision too: a physical law, a
> class hierarchy, a safety requirement, a heuristic an expert can write in one line. Constraint-
> guided learning turns those declarations into a term in the loss, a layer in the network, or a
> generator of noisy labels. The one sentence: **tell the model what must be true, not only what
> the answer was.**

**Why it matters:** it is the cheapest way to buy data efficiency and compliance at once — fewer
labels because the rules carry information, and fewer illegal outputs because the rules are part
of the objective. The distinction interviewers probe is **soft versus hard**: a **semantic loss**
penalizes violations and still permits them, whereas a **constrained layer** makes them
unrepresentable, at a real cost in inference time. The underrated failure mode is **rule conflict
with data** — when constraints and labels disagree, the gradient quietly picks a side.

**Start here — suggested path:**

1. **See rules become a loss term** — read [A Semantic Loss Function for Deep Learning with Symbolic Knowledge](https://arxiv.org/abs/1711.11157) — **Xu, Zhang, Friedman, Liang & Van den Broeck (2018)**. *The probability that the output satisfies a logical sentence, differentiated; the reference construction for this whole area.*
2. **See the teacher-student alternative** — read [Harnessing Deep Neural Networks with Logic Rules](https://arxiv.org/abs/1603.06318) — **Hu, Ma, Liu, Hovy & Xing (2016)**. *Distil first-order rules into the network's weights instead of enforcing them at prediction time.*
3. **Get labels from rules** — read [Snorkel: Rapid Training Data Creation with Weak Supervision](https://arxiv.org/abs/1711.10160) — **Ratner, Bach, Ehrenberg, Fries, Wu & Ré (2017)**. *Labeling functions with unknown accuracies, denoised by a generative model; supervision written as code.*
4. **Watch what symbols guarantee** — watch [Symbolic reasoning for large language models](https://www.youtube.com/watch?v=wApPzSqLVhY) — **Guy Van den Broeck (AI Spotlight Seminar, AIxIA)**. *Why a constraint you can check beats a constraint you hope was learned.*
5. **Map the whole design space** — skim [Deep Learning with Logical Constraints](https://arxiv.org/abs/2205.00523) — **Giunchiglia, Stoian & Lukasiewicz (2022)**. *A survey organized by logical language and by goal — performance, data efficiency, or guaranteed compliance.*

## Courses (free)
- [CS267A: Probabilistic Programming and Relational Learning](https://web.cs.ucla.edu/~guyvdb/teaching/cs267a/) — **Guy Van den Broeck (UCLA)** — free slides and readings for tractable inference, weighted model counting, and probabilistic-logic learning; the theory behind semantic loss.
- [Neuro-Symbolic AI Summer School 2025 — Day 1](https://www.youtube.com/live/zVJ59vIden0) — **Centaur AI Institute and the Neuro-Symbolic AI Community** — the field's own school; the constraint and probabilistic-logic sessions are the applied companion to the UCLA material.

## Videos
- [Symbolic reasoning for large language models](https://www.youtube.com/watch?v=wApPzSqLVhY) — **Guy Van den Broeck (AIxIA seminar)** — what a symbolic constraint buys that scale does not, argued by one of the authors of semantic loss.
- [Tractable Probabilistic Circuits](https://www.youtube.com/watch?v=oXE5XXgLXK0) — **Simons Institute for the Theory of Computing** — the machinery that makes "probability of satisfying this constraint" computable at all, rather than approximated.

## Key Papers
- [A Semantic Loss Function for Deep Learning with Symbolic Knowledge](https://arxiv.org/abs/1711.11157) — **Xu et al. (2018)** — the canonical soft-constraint objective, with the tractability argument attached.
- [Harnessing Deep Neural Networks with Logic Rules](https://arxiv.org/abs/1603.06318) — **Hu et al. (2016)** — iterative rule distillation; the constraint survives into a rule-free deployment model.
- [Posterior Regularization for Structured Latent Variable Models](https://www.jmlr.org/papers/v11/ganchev10a.html) — **Ganchev, Graça, Gillenwater & Taskar (JMLR, 2010)** — the pre-deep-learning ancestor: constrain the posterior, not the parameters.
- [DeepProbLog: Neural Probabilistic Logic Programming](https://arxiv.org/abs/1805.10872) — **Manhaeve, Dumančić, Kimmig, Demeester & De Raedt (2018)** — neural predicates inside a probabilistic logic program, trained end to end through the inference.
- [Logic Tensor Networks](https://arxiv.org/abs/2012.13635) — **Badreddine, d'Avila Garcez, Serafini & Spranger (2022)** — first-order logic relaxed into differentiable "real logic" so knowledge and data share one loss.
- [Semantic Probabilistic Layers for Neuro-Symbolic Learning](https://arxiv.org/abs/2206.00426) — **Ahmed, Teso, Chang, Van den Broeck & Vergari (2022)** — a drop-in output layer whose predictions are guaranteed to satisfy the constraint.
- [Deep Learning with Logical Constraints](https://arxiv.org/abs/2205.00523) — **Giunchiglia, Stoian & Lukasiewicz (2022)** — the survey; read it before choosing a method.
- [ROAD-R: The Autonomous Driving Dataset with Logical Requirements](https://arxiv.org/abs/2210.01597) — **Giunchiglia, Stoian, Khan, Cuzzolin & Lukasiewicz (2022)** — a real dataset with requirements attached, and the measurement that models violate them constantly.
- [Physics Informed Deep Learning (Part I): Data-driven Solutions of Nonlinear Partial Differential Equations](https://arxiv.org/abs/1711.10561) — **Raissi, Perdikaris & Karniadakis (2017)** — the same idea with a differential equation as the constraint; the residual is the loss.
- [On the Independence Assumption in Neurosymbolic Learning](https://arxiv.org/abs/2404.08458) — **van Krieken, Thanapalasingam, Tomczak, van Harmelen & Teije (ICML, 2024)** — the sharpest critique: independent-symbol assumptions make these models overconfident and hard to optimize.

## Articles / Blogs (free, no paywall)
- [Statistical and Relational Artificial Intelligence lab](http://starai.cs.ucla.edu/) — **Guy Van den Broeck's group (UCLA)** — papers, code, and tutorials for tractable constrained learning, in one place.
- [Snorkel](https://github.com/snorkel-team/snorkel) — **Snorkel team (Stanford)** — the open-source system for programmatic supervision; the tutorials show what a labeling function looks like in practice.
- [DeepProbLog](https://github.com/ML-KULeuven/deepproblog) — **KU Leuven (De Raedt's group)** — runnable neural-probabilistic-logic programs, including the MNIST-addition example everyone cites.
- [Scallop: a language for neurosymbolic programming](https://www.scallop-lang.org/) — **University of Pennsylvania** — a Datalog-based language where the provenance semiring controls how much reasoning you pay for.

## Books (free, with chapters)
- [*Probabilistic Circuits: A Unifying Framework for Tractable Probabilistic Models*](http://starai.cs.ucla.edu/papers/ProbCirc20.pdf) — **YooJung Choi, Antonio Vergari & Guy Van den Broeck** — free monograph; the structural properties that decide whether your constraint is cheap or intractable.

## In this platform
- Previous in this section: [Compositional Reasoning](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/structured-reasoning/compositional-reasoning/compositional-reasoning)
- Prerequisites: [Neuro-Symbolic AI](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai/neuro-symbolic-ai) · [Logic and Inference](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/logic-and-inference/logic-and-inference)
- The physics case (canonical home): [Physics-Informed Neural Networks](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/scientific-and-specialized-deep-learning/physics-informed-neural-networks/physics-informed-neural-networks)
- Where the guarantee is checked: [Evaluating Symbolic Correctness](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/evaluating-symbolic-correctness/evaluating-symbolic-correctness) · [Scalability Limitations](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/neuro-symbolic-and-structured-intelligence/evaluation-and-limitations/scalability-limitations/scalability-limitations)
- Related elsewhere: [Probabilistic Reasoning and Graphical Models](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/probabilistic-reasoning-and-graphical-models/probabilistic-reasoning-and-graphical-models)
