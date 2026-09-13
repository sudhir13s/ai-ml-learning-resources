---
id: "01-foundations/lagrange-multipliers"
topic: "Lagrange Multipliers & Constrained Optimization"
parent: "01-foundations"
level: advanced
built_from: ["01-foundations/derivatives-and-gradients", "01-foundations/convexity"]
interview_frequency: medium
updated: 2026-06-20
tier: core
est_minutes: 10
title: "Lagrange Multipliers & Constrained Optimization"
minutes: 10
category: mathematical-foundations
---

# Lagrange Multipliers & Constrained Optimization
> To optimize subject to constraints, look for points where the objective's gradient is parallel to
> the constraints' gradients — the multipliers measure "how hard each constraint pushes back." This
> generalizes (via KKT conditions) to inequality constraints and is the machinery behind SVMs, PCA's
> variance-maximization, and constrained maximum-likelihood.

**Why it matters:** Lagrangians are how constrained problems become unconstrained ones, and KKT
conditions characterize their solutions. Interviewers ask you to set up the Lagrangian (e.g. derive
the SVM dual, or PCA as maximizing variance subject to `‖w‖=1`), interpret the multipliers, and
state the KKT conditions.

## How to work through it

1. **Geometric intuition** — watch [Khan: Lagrange multipliers via tangency](https://www.youtube.com/watch?v=yuqB-d5MjZA). *The "gradients align at the optimum" picture, which is the whole idea.*
2. **A worked example** — watch [Dr. Trefor Bazett: Lagrange Multipliers — geometric meaning & full example](https://www.youtube.com/watch?v=8mjcnxGMwFo). *Solve a constrained problem end to end.*
3. **Formalize equality + inequality (KKT)** — read [Boyd & Vandenberghe Ch. 5 (Duality)](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf). *The Lagrangian, dual function, and KKT conditions — the rigorous core.*
4. **ML connection** — read MML Ch. 7.2 (Constrained Optimization & Lagrange Multipliers). *Constrained optimization scoped for ML, with the SVM as motivation.*
5. **See it in action** — note how PCA (maximize variance s.t. unit norm) and the hard-margin SVM dual both fall out of a Lagrangian. *These are the canonical interview applications.*

## References

- **In this platform**:
  - [Convexity](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/convexity/convexity) — the prerequisite this page builds on.
  - [Principal Component Analysis — the math](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/principal-component-analysis-math/principal-component-analysis-math) — related: PCA is itself a constrained optimization.
  - [Spectral Methods (PCA/SVD)](/ai-ml/ai-ml-intuitions/representation/dimensionality-and-latent-structure/pca-and-svd-intuition) — PCA as variance maximization under a unit-norm constraint.
  - [The Kernel Trick](/ai-ml/ai-ml-intuitions/representation/similarity-and-distance/kernel-trick-intuition) — the support vector machine setting, where the Lagrangian dual pays off.
- **Videos**:
  - [Convex Optimization I — Lecture 1](https://www.youtube.com/watch?v=McLq1hEq3UY) — **Stephen Boyd (Stanford)** — sets up the constrained-optimization framework.
  - [Lagrange Multipliers | Geometric Meaning & Full Example](https://www.youtube.com/watch?v=8mjcnxGMwFo) — **Dr. Trefor Bazett** — a complete worked constrained problem.
  - [Lagrange multipliers, using tangency to solve constrained optimization](https://www.youtube.com/watch?v=yuqB-d5MjZA) — **Khan Academy** — the geometric heart of the method.
  - [Understanding Lagrange Multipliers Visually](https://www.youtube.com/watch?v=5A39Ht9Wcu0) — **Serpentine Integral** — an extra visual angle on why gradients align.
- **Courses**:
  - [Khan Academy — Constrained optimization (Lagrange multipliers)](https://www.khanacademy.org/math/multivariable-calculus/applications-of-multivariable-derivatives/constrained-optimization/v/constrained-optimization-introduction) — **Khan Academy** — the method and examples with exercises.
  - [Stanford EE364a — Duality & KKT](https://web.stanford.edu/class/ee364a/) — **Stephen Boyd (Stanford)** — Lagrangians, duality, and KKT conditions with the free textbook.
- **Articles**:
  - [CS229 — SVM / KKT lecture notes](https://cs229.stanford.edu/notes2021fall/cs229-notes3.pdf) — **Stanford (Ng et al.)** — Lagrangian duality applied to derive the SVM.
  - [Paul's Online Notes — Lagrange Multipliers](https://tutorial.math.lamar.edu/Classes/CalcIII/LagrangeMultipliers.aspx) — **Paul Dawkins** — the method, equality constraints, and worked examples.
- **Books**:
  - [Convex Optimization — **Ch. 5 (Duality)**](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf) — **Boyd & Vandenberghe** — the Lagrangian, dual problem, and KKT conditions (free PDF).
  - [Mathematics for Machine Learning — **Ch. 7.2 (Constrained Optimization)**](https://mml-book.github.io/book/mml-book.pdf) — **Deisenroth, Faisal & Ong** — Lagrange multipliers and constrained optimization for ML.
</content>
