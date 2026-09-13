---
id: "01-foundations/taylor-expansion"
topic: "Taylor Expansion"
parent: "01-foundations"
level: intermediate
built_from: ["01-foundations/derivatives-and-gradients", "01-foundations/jacobian-and-hessian"]
interview_frequency: medium
updated: 2026-06-20
tier: core
est_minutes: 10
title: "Taylor Expansion"
minutes: 10
category: mathematical-foundations
---

# Taylor Expansion
> A Taylor expansion approximates a function near a point by a polynomial built from its
> derivatives there: value + slope·Δ + ½·curvature·Δ² + …. It's the lens through which optimization
> "sees" the loss locally — gradient descent uses the first-order term, Newton's method the
> second-order (Hessian) term.

**Why it matters:** the first- and second-order Taylor expansions are the formal justification for
gradient descent and Newton's method, and they underpin convergence analysis and curvature
arguments. Interviewers ask you to write the quadratic Taylor model of a loss and read off the
optimal step — pure Taylor.

## How to work through it

1. **Intuition** — watch [3B1B: Taylor series](https://www.youtube.com/watch?v=3d6DsjIBzJ4). *Why successive derivatives reconstruct a function, with the best visual treatment available.*
2. **Single-variable formalism** — read [Paul's Online Notes: Taylor Series](https://tutorial.math.lamar.edu/Classes/CalcII/TaylorSeries.aspx). *The expansion, remainder term, and worked examples.*
3. **Multivariable + the quadratic model** — read [MML Ch. 5.8 (Linearization & Multivariate Taylor)](https://mml-book.github.io/book/mml-book.pdf). *The gradient + Hessian quadratic form used in optimization.*
4. **See it drive optimization** — read [Boyd & Vandenberghe Ch. 9.5 (Newton's method)](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf). *The second-order Taylor model is exactly the Newton step.*

## References

- **In this platform**:
  - [Convexity](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/convexity/convexity) — builds directly on this page: curvature decides whether a function is convex.
  - [Derivatives & Gradients](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/derivatives-and-gradients/derivatives-and-gradients) — a prerequisite this page builds on.
  - [Gradient Descent & SGD](/ai-ml/ai-ml-intuitions/learning-and-optimization/first-order-optimization/gradient-descent-and-stochastic-gradient-descent-intuition) — the step that a first-order Taylor model justifies.
  - [Gradient Descent — theory](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/gradient-descent-theory/gradient-descent-theory) — builds directly on this page: convergence arguments built on the quadratic model.
  - [Jacobian & Hessian](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/jacobian-and-hessian/jacobian-and-hessian) — a prerequisite: the Hessian is the second-order term.
  - [Jacobian & Hessian, the intuition](/ai-ml/ai-ml-intuitions/learning-and-optimization/gradients-and-credit-assignment/jacobians-and-hessians-intuition) — curvature, and what it does to training.
- **Videos**:
  - [Taylor Series and Maclaurin Series](https://www.youtube.com/watch?v=LDBnS4c7YbA) — **The Organic Chemistry Tutor** — building the polynomial term by term, with worked examples.
  - [Taylor series | Essence of Calculus Ch. 11](https://www.youtube.com/watch?v=3d6DsjIBzJ4) — **3Blue1Brown** — the definitive visual intuition.
  - [The essence of calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM) — **3Blue1Brown** — the derivative groundwork Taylor stands on.
  - [The paradox of the derivative | Ch. 2](https://www.youtube.com/watch?v=9vKqVkMQHKk) — **3Blue1Brown** — local linear approximation, the order-1 Taylor term.
- **Courses**:
  - [Khan Academy — Taylor & Maclaurin series](https://www.khanacademy.org/math/ap-calculus-bc/bc-series-new/bc-10-11/v/maclaurin-and-taylor-series-intuition) — **Khan Academy** — guided build-up with exercises.
  - [MIT 18.01 Single Variable Calculus — Taylor series unit](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/) — **MIT OCW** — derivation and convergence of Taylor/Maclaurin series.
- **Articles**:
  - [CS231n — Optimization notes (local approximation)](https://cs231n.github.io/optimization-1/) — **Stanford** — how the first-order Taylor model justifies a gradient step.
  - [Paul's Online Notes — Taylor Series](https://tutorial.math.lamar.edu/Classes/CalcII/TaylorSeries.aspx) — **Paul Dawkins** — the single-variable expansion and remainder, with examples.
- **Books**:
  - [Calculus (OpenStax) — **Vol. 2, Ch. 6 (Power & Taylor Series)**](https://openstax.org/details/books/calculus-volume-2) — **OpenStax** — free, thorough single-variable treatment.
  - [Convex Optimization — Ch. 9.5 (Newton's method)](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf) — **Boyd & Vandenberghe** — the quadratic Taylor model as the basis of Newton's method (free PDF).
  - [Mathematics for Machine Learning — **Ch. 5.8 (Taylor)**](https://mml-book.github.io/book/mml-book.pdf) — **Deisenroth, Faisal & Ong** — the multivariable Taylor expansion with gradient and Hessian.
</content>
