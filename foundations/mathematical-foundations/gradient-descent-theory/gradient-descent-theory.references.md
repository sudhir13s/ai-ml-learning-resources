---
id: "01-foundations/gradient-descent-theory/references"
topic: "Gradient Descent — References"
parent: "01-foundations/gradient-descent-theory"
type: references
updated: 2026-09-07
---

# Gradient Descent — References

> Companion link library for **[Gradient Descent — theory & convergence](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/gradient-descent-theory/gradient-descent-theory)** (the concept page). External sources *and* internal links to related pages on this platform, kept separate so it can be reused as a standalone reference list. Grouped by type, alphabetical within each group. Every entry is from a primary author or a recognized deep explainer — chosen for depth on *this* topic.

- **In this platform**:
  - [Convexity](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/convexity/convexity) — a prerequisite for the convergence theory.
  - [Derivatives & Gradients](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/derivatives-and-gradients/derivatives-and-gradients) — a prerequisite: the gradient the method follows.
  - [Gradient Descent & SGD](/ai-ml/ai-ml-intuitions/learning-and-optimization/first-order-optimization/gradient-descent-and-stochastic-gradient-descent-intuition) — the intuition, and why the step works.
  - [Gradient Descent — theory & convergence](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/gradient-descent-theory/gradient-descent-theory) — the concept page this list accompanies.
  - [Optimizers](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/optimizers) — the applied next layer: momentum, Adam, AdamW and learning-rate schedules, which fix the zig-zag.
- **Videos**:
  - [Convex Optimization I — Lecture 1](https://www.youtube.com/watch?v=McLq1hEq3UY) — **Stephen Boyd (Stanford)** — sets up the descent-method framework.
  - [Gradient descent, how neural networks learn (Ch. 2)](https://www.youtube.com/watch?v=IHZwWFHWa-w) — **3Blue1Brown** — gradient descent on a real loss surface.
  - [Gradient Descent, Step-by-Step](https://www.youtube.com/watch?v=sDv4f4s2SB8) — **StatQuest (Josh Starmer)** — from-scratch intuition with a worked example.
  - [Gradients and Partial Derivatives](https://www.youtube.com/watch?v=GkB4vW16QHI) — **Eugene Khutoryansky** — the steepest-descent direction visualized.
- **Courses**:
  - [Stanford CS231n — Optimization](https://cs231n.github.io/optimization-1/) — **Stanford** — gradient descent, SGD, and update rules, ML-focused.
  - [Stanford EE364a — Convex Optimization I (descent methods)](https://web.stanford.edu/class/ee364a/) — **Stephen Boyd (Stanford)** — convergence theory for gradient/descent methods.
  - [The Mathematical Engineering of Deep Learning](https://deeplearningmath.org/) — **Liquet, Moka & Nazarathy** — a free course-and-book that develops optimization for deep models from the mathematics up: gradient descent, stochastic variants, and the convergence arguments behind the learning-rate rules.
- **Interactive**:
  - [Why Momentum Really Works](https://distill.pub/2017/momentum/) — **Goh (Distill)** — interactive: change the condition number and watch gradient descent zig-zag, then watch momentum fix it.
- **Articles**:
  - [An overview of gradient descent optimization algorithms](https://www.ruder.io/optimizing-gradient-descent/) — **Sebastian Ruder** — batch/stochastic/mini-batch and the lineage of optimizers.
- **Papers**:
  - [Identifying and attacking the saddle point problem](https://arxiv.org/abs/1406.2572) — **Dauphin et al. (2014)** — why saddle points, not local minima, are the real obstacle in high-dimensional non-convex optimization.
  - [Optimization Methods for Large-Scale Machine Learning](https://arxiv.org/abs/1606.04838) — **Bottou, Curtis & Nocedal (2018)** — the definitive survey of SGD theory and convergence.
- **Books**:
  - [Convex Optimization — Ch. 9 (Unconstrained Minimization)](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf) — **Boyd & Vandenberghe** — gradient-descent convergence, step sizes, and conditioning (free PDF).
  - [Mathematics for Machine Learning — Ch. 7.1 (Gradient Descent)](https://mml-book.github.io/book/mml-book.pdf) — **Deisenroth, Faisal & Ong** — gradient descent and step-size intuition for ML (free PDF).
