---
id: "01-foundations/chain-rule"
topic: "The Chain Rule (& Backpropagation)"
parent: "01-foundations"
level: intermediate
built_from: ["01-foundations/derivatives-and-gradients"]
interview_frequency: very-high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "The Chain Rule (& Backpropagation)"
minutes: 10
category: mathematical-foundations
---

# The Chain Rule (& Backpropagation)
> The chain rule differentiates a composition: the rate of change of `f(g(x))` is the product of
> the local rates. Stack it across the layers of a network and you get backpropagation — the
> reverse-mode accumulation of gradients that makes deep learning trainable at all.

**Why it matters:** backprop *is* the multivariable chain rule applied over a computational graph.
Interviewers ask you to differentiate composed functions by hand, explain forward vs reverse mode
(why reverse is cheap for scalar losses), and derive the gradient through a small network — all
chain rule.

## How to work through it

1. **Single-variable chain rule** — watch [3B1B: Visualizing the chain rule and product rule](https://www.youtube.com/watch?v=YG15m2VwSjA). *See where the product of derivatives comes from.*
2. **From chain rule to backprop** — watch [3B1B: Backpropagation, intuitively](https://www.youtube.com/watch?v=Ilg3gGewQ5U) then [Backpropagation calculus](https://www.youtube.com/watch?v=tIeHLnjs5U8). *The exact moment the chain rule becomes a learning algorithm.*
3. **Build it yourself** — watch [Karpathy: micrograd — the spelled-out intro to backprop](https://www.youtube.com/watch?v=VMj-3S1tku0). *Implementing reverse-mode autodiff cements it forever.*
4. **Matrix/vector form** — read [Matrix Calculus for Deep Learning](https://explained.ai/matrix-calculus/). *The vector chain rule and Jacobian-product view used in real frameworks.*
5. **Connect to ML** — read [ai-ml-intuitions 2.02 Backpropagation (The Chain Rule)](/ai-ml/ai-ml-intuitions/learning-and-optimization/gradients-and-credit-assignment/chain-rule-and-backpropagation-intuition). *The platform's deep dive on credit assignment.*

## References

- **In this platform**:
  - [Backpropagation (The Chain Rule)](/ai-ml/ai-ml-intuitions/learning-and-optimization/gradients-and-credit-assignment/chain-rule-and-backpropagation-intuition) — the intuition for credit assignment through a network.
  - [Computational Graphs / Autograd](/ai-ml/ai-ml-intuitions/learning-and-optimization/gradients-and-credit-assignment/computational-graphs-and-autograd-intuition) — the chain rule automated, the way frameworks run it.
  - [Derivatives & Gradients](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/derivatives-and-gradients/derivatives-and-gradients) — the prerequisite this page builds on.
  - [Jacobian & Hessian](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/jacobian-and-hessian/jacobian-and-hessian) — builds directly on this page: the chain rule for vector functions.
- **Videos**:
  - [Backpropagation calculus | Deep Learning Ch. 4](https://www.youtube.com/watch?v=tIeHLnjs5U8) — **3Blue1Brown** — the explicit chain-rule derivation.
  - [Backpropagation, intuitively | Deep Learning Ch. 3](https://www.youtube.com/watch?v=Ilg3gGewQ5U) — **3Blue1Brown** — chain rule as gradient flow through a network.
  - [The spelled-out intro to backpropagation (micrograd)](https://www.youtube.com/watch?v=VMj-3S1tku0) — **Andrej Karpathy** — build reverse-mode autodiff from scratch.
  - [Visualizing the chain rule and product rule | Ch. 4](https://www.youtube.com/watch?v=YG15m2VwSjA) — **3Blue1Brown** — the geometric why behind the chain rule.
- **Courses**:
  - [Khan Academy — Multivariable chain rule](https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/multivariable-chain-rule/v/multivariable-chain-rule) — **Khan Academy** — the multivariable version with exercises.
  - [Stanford CS231n — Backpropagation notes](https://cs231n.github.io/optimization-2/) — **Stanford** — the chain rule on computational graphs, with worked gradient flows.
- **Articles**:
  - [Calculus on Computational Graphs: Backpropagation](https://colah.github.io/posts/2015-08-Backprop/) — **Christopher Olah** — the clearest free essay on chain rule over graphs.
  - [Matrix Calculus for Deep Learning](https://explained.ai/matrix-calculus/) — **Parr & Howard** — the vector/matrix chain rule needed for real backprop.
  - [Paul's Online Notes — Chain Rule](https://tutorial.math.lamar.edu/Classes/CalcI/ChainRule.aspx) — **Paul Dawkins** — mechanics and worked examples.
- **Books**:
  - [Dive into Deep Learning — **§2.5 (Automatic Differentiation), §5.3 (Backprop)**](https://d2l.ai/chapter_preliminaries/autograd.html) — **Zhang et al.** — chain rule, autograd, and backprop with runnable code.
  - [Mathematics for Machine Learning — **Ch. 5 (Vector Calculus)**](https://mml-book.github.io/book/mml-book.pdf) — **Deisenroth, Faisal & Ong** — the chain rule, gradients of compositions, and automatic differentiation.
  - [The Mathematical Engineering of Deep Learning](https://deeplearningmath.org/) — **Liquet, Moka & Nazarathy** — a free book-and-course that carries the chain rule through to full backpropagation in matrix form, with the notation stated carefully enough to follow every index.
</content>
