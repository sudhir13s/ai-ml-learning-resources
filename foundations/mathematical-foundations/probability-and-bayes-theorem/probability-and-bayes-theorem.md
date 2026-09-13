---
id: "01-foundations/probability-and-bayes-theorem"
topic: "Probability & Bayes' Theorem"
parent: "01-foundations"
level: beginner
built_from: []
interview_frequency: very-high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Probability & Bayes' Theorem"
minutes: 10
category: mathematical-foundations
---

# Probability & Bayes' Theorem
> Probability is the calculus of uncertainty: events, conditional probability, independence, and
> the law of total probability. Bayes' theorem — `P(H|D) ∝ P(D|H)·P(H)` — is the rule for updating
> beliefs with evidence, and it's the backbone of classification, Naive Bayes, Bayesian inference,
> and probabilistic modeling.

**Why it matters:** Bayes is the most-asked probability topic in ML interviews — the classic
"medical test" base-rate problem, deriving Naive Bayes, and reasoning about posteriors. You should
be fluent with conditional probability, independence, and decomposing joint distributions.

## How to work through it

1. **Build the intuition** — watch [3B1B: Bayes' theorem](https://www.youtube.com/watch?v=HZGCoVF3YvM) and [StatQuest: Bayes' Theorem, Clearly Explained](https://www.youtube.com/watch?v=9wCnvr7Xw4E). *The geometry of updating beliefs, then a clean worked example.*
2. **The base-rate trap** — watch [Veritasium: The Bayesian Trap](https://www.youtube.com/watch?v=R13BD8qKeTg). *Why ignoring priors produces the famous medical-test mistake.*
3. **Pin the rules** — read [CS229 Probability Review](https://cs229.stanford.edu/section/cs229-prob.pdf): conditional probability, independence, Bayes, total probability. *The ML reference sheet.*
4. **Go deeper** — watch a few [Harvard Stat 110 lectures](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo) (Blitzstein) on conditional probability and Bayes. *The gold-standard probability course, free.*
5. **Connect to ML** — read [ai-ml-intuitions 0.01 Probability & Bayes' Theorem](/ai-ml/ai-ml-intuitions/foundational-mental-models/probability-and-belief/probability-and-bayes-intuition). *The platform's deep dive and ML framing.*

## References

- **In this platform**:
  - [Bayesian Inference](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/bayesian-inference/bayesian-inference) — builds directly on this page: Bayes' rule applied to model parameters.
  - [Probability & Bayes' Theorem](/ai-ml/ai-ml-intuitions/foundational-mental-models/probability-and-belief/probability-and-bayes-intuition) — the intuition, and the machine-learning framing.
  - [Random Variables & Distributions](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/random-variables-and-distributions/random-variables-and-distributions) — builds directly on this page: probability attached to numbers.
- **Videos**:
  - [Bayes theorem, the geometry of changing beliefs](https://www.youtube.com/watch?v=HZGCoVF3YvM) — **3Blue1Brown** — the definitive visual intuition for Bayes.
  - [Bayes' Theorem, Clearly Explained](https://www.youtube.com/watch?v=9wCnvr7Xw4E) — **StatQuest (Josh Starmer)** — a clean, worked numerical example.
  - [Stat 110 — Conditional Probability & Bayes (Lecture)](https://www.youtube.com/watch?v=P7NE4WF8j-Q) — **Joe Blitzstein (Harvard)** — rigorous conditional probability and Bayes.
  - [The Bayesian Trap](https://www.youtube.com/watch?v=R13BD8qKeTg) — **Veritasium** — why base rates matter (the medical-test classic).
- **Courses**:
  - [Harvard Stat 110: Probability](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo) — **Joe Blitzstein (Harvard)** — the gold-standard probability course; full lectures + book free.
  - [Khan Academy — Probability](https://www.khanacademy.org/math/statistics-probability/probability-library) — **Khan Academy** — conditional probability, independence, and Bayes with exercises.
- **Interactive**:
  - [Explained Visually — Conditional Probability](https://setosa.io/ev/conditional-probability/) — **Victor Powell & Lewis Lehe** — drag the sample space and watch `P(A|B)` change; conditioning as restriction, before any algebra.
  - [Seeing Theory — Ch. 1–2 (Basic Probability, Compound Probability)](https://seeing-theory.brown.edu/) — **Brown University** — interactive, animated probability fundamentals.
- **Articles**:
  - [CS229 Probability Review](https://cs229.stanford.edu/section/cs229-prob.pdf) — **Stanford (Ng et al.)** — probability spaces, conditional probability, independence, and Bayes for ML.
- **Books**:
  - [Introduction to Probability — **Ch. 2 (Conditional Probability & Bayes)**](http://probabilitybook.net/) — **Blitzstein & Hwang** — the Stat 110 textbook; 1st-edition PDF free online.
  - [Mathematics for Machine Learning — **Ch. 6 (Probability & Distributions)**](https://mml-book.github.io/book/mml-book.pdf) — **Deisenroth, Faisal & Ong** — probability foundations and Bayes' rule, scoped for ML.
  - [Think Bayes (online) — Ch. 1 (Bayes's Theorem)](https://allendowney.github.io/ThinkBayes2/chap01.html) — **Allen B. Downey** — Bayes in Python, free and computational.
</content>
