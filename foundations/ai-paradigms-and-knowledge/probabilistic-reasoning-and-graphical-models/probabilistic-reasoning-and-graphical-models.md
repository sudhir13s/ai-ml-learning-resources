---
id: "foundations/ai-paradigms-and-knowledge/probabilistic-reasoning-and-graphical-models"
topic: "Probabilistic Reasoning and Graphical Models"
level: intermediate
built_from: ["statistical-learning-paradigm", "neural-learning-paradigm"]
leads_to: ["foundations/ai-paradigms-and-knowledge/neuro-symbolic-ai-overview"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Probabilistic Reasoning and Graphical Models"
minutes: 16
category: ai-paradigms-and-knowledge
---

# Probabilistic Reasoning and Graphical Models
> The paradigm that handles **uncertainty explicitly**: write the joint distribution over your
> variables as a graph — Bayesian networks (directed) or Markov random fields (undirected) — where
> an absent edge is a **conditional independence** assumption. Then *inference* answers queries
> ("given these observations, what is the probability of that?") and *learning* fits the parameters.

**Why it matters:** graphical models are how you reason with incomplete evidence instead of
guessing, and they are the language behind variational autoencoders, diffusion models, expectation
maximization, Kalman filters, and the uncertainty estimates a serious production system needs. The
recurring interview question is where the cost lives: exact inference is exponential in the graph's
treewidth, so the real skill is knowing when to switch to variational or sampling methods.

**Start here — suggested path:**

1. **Get the reasoning primitive** — watch [Bayes theorem, the geometry of changing beliefs](https://www.youtube.com/watch?v=HZGCoVF3YvM) — **3Blue1Brown (Grant Sanderson)**. *Belief update seen as areas, so the algebra stops being arbitrary.*
2. **Learn the representation** — read [Bayesian networks (CS228 notes)](https://ermongroup.github.io/cs228-notes/representation/directed/) — **Stanford CS228 (Stefano Ermon, Volodymyr Kuleshov)**. *Factorized joints, d-separation, and what an edge does and does not mean.*
3. **Learn the algorithm** — read [Variable elimination (CS228 notes)](https://ermongroup.github.io/cs228-notes/inference/ve/) — **Stanford CS228**. *Exact inference and exactly where the exponential cost appears.*
4. **Take the canonical course** — [Probabilistic Graphical Models Specialization](https://www.coursera.org/specializations/probabilistic-graphical-models) — **Daphne Koller (Stanford)**. *Free to audit; the course that defines the subject.*
5. **See the modern approximate method** — read [Variational Inference: A Review for Statisticians](https://arxiv.org/abs/1601.00670) — **Blei, Kucukelbir & McAuliffe (2016)**. *How inference is actually done at scale, and the bridge to the evidence lower bound used by deep generative models.*

## Courses (free)
- [Probabilistic Graphical Models Specialization](https://www.coursera.org/specializations/probabilistic-graphical-models) — **Daphne Koller (Stanford)** — free to audit; representation, inference, and learning from the field's principal author.
- [Stanford CS228: Probabilistic Graphical Models](https://cs.stanford.edu/~ermon/cs228/index.html) — **Stanford (Stefano Ermon)** — free course page with the complete, unusually clear [course notes](https://ermongroup.github.io/cs228-notes/).

## Videos
- [Bayes theorem, the geometry of changing beliefs](https://www.youtube.com/watch?v=HZGCoVF3YvM) — **3Blue1Brown** — the visual foundation the whole paradigm rests on.
- [Machine Learning (full lecture series)](https://www.youtube.com/playlist?list=PLD0F06AA0D2E8FFBA) — **mathematicalmonk** — short, precise blackboard lectures; the graphical-model and inference segments are the best free derivations on video.

## Key Papers
- [Variational Inference: A Review for Statisticians](https://arxiv.org/abs/1601.00670) — **Blei, Kucukelbir & McAuliffe (2016)** — the standard reference for turning inference into optimization.
- [Automatic Differentiation Variational Inference](https://arxiv.org/abs/1603.00788) — **Kucukelbir, Tran, Ranganath, Gelman & Blei (2016)** — how probabilistic programming systems make variational inference automatic; the mechanism inside Stan and Pyro.
- [The Seven Tools of Causal Inference, with Reflections on Machine Learning](https://ftp.cs.ucla.edu/pub/stat_ser/r481.pdf) — **Judea Pearl (2018)** — the author of Bayesian networks on what probability alone cannot express.

## Articles / Blogs (free, no paywall)
- [CS228 course notes](https://ermongroup.github.io/cs228-notes/) — **Stefano Ermon and Volodymyr Kuleshov (Stanford)** — a free, complete textbook-quality set of notes on representation, inference, and learning.
- [Pyro examples and tutorials](https://pyro.ai/examples/) — **Pyro developers (Uber AI, now community-maintained)** — probabilistic programming in PyTorch; the practical route from a graph on paper to a fitted model.
- [Bayesian Modeling and Computation in Python](https://bayesiancomputationbook.com/welcome.html) — **Martin, Kumar & Lao** — free online book; workflow, diagnostics, and the parts of Bayesian modelling that break in practice.

## Books (free, with chapters)
- [*Probabilistic Machine Learning: An Introduction* — Ch. 4 "Statistics", Ch. 10 "Logistic Regression"](https://probml.github.io/pml-book/book1.html) — **Kevin Murphy (2022)** — free PDF; the modern unified treatment with runnable notebooks.
- [*Probabilistic Machine Learning: Advanced Topics* — Ch. 4 "Graphical Models", Ch. 9 "Variational Inference"](https://probml.github.io/pml-book/book2.html) — **Kevin Murphy (2023)** — free PDF; the current graduate-level reference for inference.
- [*Pattern Recognition and Machine Learning* — Ch. 8 "Graphical Models"](https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf) — **Christopher Bishop** — released free by Microsoft Research; still the clearest chapter on factor graphs and message passing.
- [*Probabilistic Graphical Models: Principles and Techniques* — Ch. 3 "The Bayesian Network Representation"](https://openlibrary.org/works/OL2734525W/Probabilistic_Graphical_Models) — **Koller & Friedman (2009)** — pointer only, not free; the definitive reference if you need proofs.

## In this platform
- Prerequisites here: [Probability and Bayes' Theorem](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/probability-and-bayes-theorem/probability-and-bayes-theorem) · [Bayesian Inference](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/bayesian-inference/bayesian-inference) · [Maximum Likelihood Estimation](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/maximum-likelihood-estimation/maximum-likelihood-estimation)
- Paradigm neighbours: [The Neural Learning Paradigm](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/neural-learning-paradigm/neural-learning-paradigm) · [Neuro-Symbolic AI Overview](/ai-ml/ai-ml-learning-resources/foundations/ai-paradigms-and-knowledge/neuro-symbolic-ai-overview/neuro-symbolic-ai-overview)
- Where probability meets structure: [Causal and Relational Reasoning](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/structured-reasoning/causal-and-relational-reasoning/causal-and-relational-reasoning) · [Causal Inference](/ai-ml/ai-ml-learning-resources/specialized-studies/advanced-mathematics-for-ai-research/causal-inference/causal-inference)
