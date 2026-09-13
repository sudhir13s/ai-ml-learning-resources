---
id: "01-foundations/hypothesis-testing-and-confidence-intervals"
topic: "Hypothesis Testing & Confidence Intervals"
parent: "01-foundations"
level: intermediate
built_from: ["01-foundations/lln-and-clt"]
interview_frequency: high
updated: 2026-06-20
tier: core
est_minutes: 10
title: "Hypothesis Testing & Confidence Intervals"
minutes: 10
category: mathematical-foundations
---

# Hypothesis Testing & Confidence Intervals
> A hypothesis test asks "could this result be chance?" — a p-value is the probability of data this
> extreme under the null. A confidence interval reports a range of plausible values with a stated
> coverage. Together they're how you decide whether a model improvement, an A/B test, or a metric
> difference is *real*.

**Why it matters:** comparing models honestly is a core ML-engineering skill, and A/B-test
reasoning shows up in interviews. You should explain what a p-value does (and does *not*) mean,
Type I vs Type II error and power, what "95% confidence" actually claims, and why multiple
comparisons inflate false positives.

## How to work through it

1. **Hypothesis tests & null** — watch [StatQuest: Hypothesis Testing & the Null Hypothesis](https://www.youtube.com/watch?v=0oc49DyA3hU). *The framework before any formulas.*
2. **p-values, correctly** — watch [StatQuest: p-values, what they are and how to interpret them](https://www.youtube.com/watch?v=vemZtEM63GY). *Kills the most common misinterpretation.*
3. **Confidence intervals** — watch [StatQuest: Confidence Intervals, Clearly Explained](https://www.youtube.com/watch?v=TqOeMYtOc1w). *What the interval does and doesn't say.*
4. **Formalize** — read [OpenStax Introductory Statistics — Hypothesis Testing & CIs](https://openstax.org/books/introductory-statistics/pages/9-introduction). *Test statistics, errors, power, and interval construction.*
5. **Connect to ML** — read [ai-ml-intuitions 0.05 Hypothesis Testing & Confidence Intervals](/ai-ml/ai-ml-intuitions/foundational-mental-models/probability-and-belief/hypothesis-testing-and-confidence-intuition). *Evaluating model comparisons honestly.*

## References

- **In this platform**:
  - [Hypothesis Testing & Confidence Intervals](/ai-ml/ai-ml-intuitions/foundational-mental-models/probability-and-belief/hypothesis-testing-and-confidence-intuition) — the intuition, and how to compare models honestly.
  - [Law of Large Numbers & the CLT](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/lln-and-clt/lln-and-clt) — the prerequisite this page builds on.
- **Videos**:
  - [Confidence Intervals, Clearly Explained](https://www.youtube.com/watch?v=TqOeMYtOc1w) — **StatQuest (Josh Starmer)** — what coverage really means.
  - [Hypothesis Testing and the Null Hypothesis, Clearly Explained](https://www.youtube.com/watch?v=0oc49DyA3hU) — **StatQuest (Josh Starmer)** — the testing framework.
  - [P-values and significance tests](https://www.youtube.com/watch?v=KS6KEWaoOOE) — **Khan Academy** — a complementary, exercise-oriented walkthrough.
  - [p-values: what they are and how to interpret them](https://www.youtube.com/watch?v=vemZtEM63GY) — **StatQuest (Josh Starmer)** — the correct interpretation.
- **Courses**:
  - [Harvard Stat 110 → inference](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo) — **Joe Blitzstein (Harvard)** — the probability foundations behind tests and intervals, free.
  - [Khan Academy — Significance tests & confidence intervals](https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample) — **Khan Academy** — full unit with exercises.
- **Interactive**:
  - [Seeing Theory — Ch. 4 (Frequentist Inference)](https://seeing-theory.brown.edu/frequentist-inference/index.html) — **Brown University** — interactive p-values and confidence intervals.
- **Articles**:
  - [Statistical significance & A/B testing](https://www.evanmiller.org/how-not-to-run-an-ab-test.html) — **Evan Miller** — a classic free essay on testing pitfalls (peeking, multiple comparisons).
- **Books**:
  - [Introductory Statistics (OpenStax) — **Ch. 8 (Confidence Intervals), Ch. 9 (Hypothesis Testing)**](https://openstax.org/details/books/introductory-statistics) — **OpenStax** — free, thorough, with examples.
  - [Mathematics for Machine Learning — Ch. 6 (Probability)](https://mml-book.github.io/book/mml-book.pdf) — **Deisenroth, Faisal & Ong** — the distribution machinery tests are built on.
  - [OpenStax Introductory Statistics — Ch. 9 (Hypothesis Testing with One Sample)](https://openstax.org/books/introductory-statistics/pages/9-introduction) — **OpenStax** — test statistics, Type I/II errors, and power, free and rigorous.
  - [Think Stats — **Ch. 9 (Hypothesis Testing)**](https://greenteapress.com/wp/think-stats-2e/) — **Allen B. Downey** — computational hypothesis testing in Python; free.
</content>
