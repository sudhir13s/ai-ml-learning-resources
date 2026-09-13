---
id: "01-foundations/lln-and-clt"
topic: "Law of Large Numbers & the CLT"
parent: "01-foundations"
level: intermediate
built_from: ["01-foundations/expectation-variance-covariance"]
interview_frequency: high
updated: 2026-06-20
tier: core
est_minutes: 10
title: "Law of Large Numbers & the CLT"
minutes: 10
category: mathematical-foundations
---

# Law of Large Numbers & the Central Limit Theorem
> The **Law of Large Numbers** says sample averages converge to the true mean as you collect more
> data; the **Central Limit Theorem** says those averages are approximately Gaussian regardless of
> the original distribution. Together they justify estimation from samples, mini-batch gradients,
> bootstrap, and the ubiquity of the normal distribution.

**Why it matters:** these two theorems are *why* sampling works. Interviewers ask why mini-batch
gradients are unbiased estimates that converge, why confidence intervals shrink like `1/√n`, why so
many quantities end up Gaussian, and the difference between the LLN (the mean) and the CLT (the
*distribution* of the mean).

## How to work through it

1. **LLN intuition** — watch [Khan: Law of large numbers](https://www.youtube.com/watch?v=VpuN8vCQ--M). *Sample averages settling onto the true mean.*
2. **CLT, visually** — watch [3B1B: But what is the Central Limit Theorem?](https://www.youtube.com/watch?v=zeJD6dqJ5lo). *Why sums/averages become Gaussian, beautifully animated.*
3. **CLT, worked** — watch [StatQuest: The Central Limit Theorem, Clearly Explained](https://www.youtube.com/watch?v=YAlJCEDH2uY). *A concrete numeric demonstration.*
4. **Formalize** — read the limit-theorems chapter of [Stat 110 / Blitzstein & Hwang](http://probabilitybook.net/). *Statements, conditions, and the `1/√n` scaling.*
5. **Connect to ML** — read [ai-ml-intuitions 0.04 Law of Large Numbers & CLT](/ai-ml/ai-ml-intuitions/foundational-mental-models/probability-and-belief/law-of-large-numbers-and-central-limit-theorem-intuition). *Why mini-batch estimates work.*

## References

- **In this platform**:
  - [Expectation, Variance & Covariance](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/expectation-variance-covariance/expectation-variance-covariance) — the prerequisite this page builds on.
  - [Gradient Descent & SGD](/ai-ml/ai-ml-intuitions/learning-and-optimization/first-order-optimization/gradient-descent-and-stochastic-gradient-descent-intuition) — why mini-batch gradients work, which is this page's theorems at training time.
  - [Hypothesis Testing & Confidence Intervals](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/hypothesis-testing-and-confidence-intervals/hypothesis-testing-and-confidence-intervals) — builds directly on this page: inference from sample means.
  - [Law of Large Numbers & CLT](/ai-ml/ai-ml-intuitions/foundational-mental-models/probability-and-belief/law-of-large-numbers-and-central-limit-theorem-intuition) — the intuition for why sampling works.
- **Videos**:
  - [But what is the Central Limit Theorem?](https://www.youtube.com/watch?v=zeJD6dqJ5lo) — **3Blue1Brown** — the definitive visual CLT.
  - [Law of large numbers](https://www.youtube.com/watch?v=VpuN8vCQ--M) — **Khan Academy** — the LLN intuition.
  - [The Central Limit Theorem, Clearly Explained](https://www.youtube.com/watch?v=YAlJCEDH2uY) — **StatQuest (Josh Starmer)** — a worked demonstration.
  - [Why π is in the normal distribution](https://www.youtube.com/watch?v=cy8r7WSuT1I) — **3Blue1Brown** — deeper intuition for the Gaussian the CLT produces.
- **Courses**:
  - [Harvard Stat 110 — Law of Large Numbers & CLT](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo) — **Joe Blitzstein (Harvard)** — the rigorous treatment with free lectures.
  - [Khan Academy — Sampling distributions & CLT](https://www.khanacademy.org/math/statistics-probability/sampling-distributions-library) — **Khan Academy** — sampling distributions, LLN, and the CLT with exercises.
- **Interactive**:
  - [Seeing Theory — Ch. 4 (Frequentist Inference / CLT)](https://seeing-theory.brown.edu/probability-distributions/index.html) — **Brown University** — interactive sampling distributions and the CLT.
- **Articles**:
  - [CS229 Probability Review](https://cs229.stanford.edu/section/cs229-prob.pdf) — **Stanford (Ng et al.)** — expectation/variance and the limit-theorem context used in ML.
  - [Paul's Online Notes / OpenStax Statistics — The Central Limit Theorem](https://openstax.org/books/introductory-statistics/pages/7-1-the-central-limit-theorem-for-sample-means-averages) — **OpenStax** — the CLT for sample means, with examples (free).
- **Books**:
  - [Introduction to Probability — **Ch. 10 (Inequalities & Limit Theorems)**](http://probabilitybook.net/) — **Blitzstein & Hwang** — LLN and CLT statements/proofs; 1st-edition PDF free.
  - [Mathematics for Machine Learning — Ch. 6 (Probability & Distributions)](https://mml-book.github.io/book/mml-book.pdf) — **Deisenroth, Faisal & Ong** — moments and the Gaussian that underpin the CLT.
  - [Think Stats — **Ch. 8 (Estimation), Ch. 14 (Analytic Methods)**](https://greenteapress.com/wp/think-stats-2e/) — **Allen B. Downey** — sampling and the CLT computationally; free.
</content>
