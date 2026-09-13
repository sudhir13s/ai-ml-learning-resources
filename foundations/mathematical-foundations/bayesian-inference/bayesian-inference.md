---
id: "01-foundations/bayesian-inference"
topic: "Bayesian Inference (priors, posteriors, MAP)"
parent: "01-foundations"
level: advanced
built_from: ["01-foundations/probability-and-bayes-theorem", "01-foundations/maximum-likelihood-estimation"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Bayesian Inference (priors, posteriors, MAP)"
minutes: 10
category: mathematical-foundations
---

# Bayesian Inference — priors, posteriors, MAP
> Bayesian inference treats parameters as *random* and updates a prior into a posterior with data:
> `posterior ∝ likelihood × prior`. The **MAP** estimate is the posterior's peak; full Bayes keeps
> the whole posterior to quantify uncertainty. This is the basis for regularization-as-priors,
> Bayesian models, and the ELBO behind VAEs.

**Why it matters:** the MLE-vs-MAP-vs-full-Bayes distinction is a frequent interview topic, as is
"L2 regularization = Gaussian prior" and "L1 = Laplace prior." You should derive a posterior for a
simple model (e.g. Beta–Binomial), explain conjugacy, and articulate when uncertainty (full
posterior) matters versus a point estimate.

## How to work through it

1. **The mindset** — watch [StataCorp: Introduction to Bayesian statistics, part 1](https://www.youtube.com/watch?v=0F0QoMCSKJ4) and revisit [3B1B: Bayes' theorem](https://www.youtube.com/watch?v=HZGCoVF3YvM). *Priors → posteriors as belief updating.*
2. **MLE vs MAP vs Bayes** — read [MML Ch. 8.3–8.4 (MLE, MAP, Bayesian inference)](https://mml-book.github.io/book/mml-book.pdf). *The three estimators and where the prior enters.*
3. **A worked posterior** — read [Think Bayes Ch. 1–3](https://allendowney.github.io/ThinkBayes2/) (Beta–Binomial, conjugacy). *Compute a posterior in Python end to end.*
4. **Regularization as a prior** — connect L2/L1 penalties to Gaussian/Laplace priors (covered in CS229 / MML). *The cleanest "why does regularization work" answer.*
5. **Connect to ML** — read [ai-ml-intuitions 5.02 Latent-Variable Models (ELBO/VAEs)](/ai-ml/ai-ml-intuitions/generation/latent-variable-generation/latent-variable-models-and-elbo-intuition). *Where Bayesian inference scales to deep generative models.*

## References

- **In this platform**:
  - [Latent-Variable Models (ELBO/VAEs)](/ai-ml/ai-ml-intuitions/generation/latent-variable-generation/latent-variable-models-and-elbo-intuition) — where Bayesian inference scales to deep generative models.
  - [Maximum Likelihood Estimation](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/maximum-likelihood-estimation/maximum-likelihood-estimation) — a prerequisite: the estimate a prior turns into maximum a posteriori.
  - [Probability & Bayes' Theorem](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/probability-and-bayes-theorem/probability-and-bayes-theorem) — a prerequisite this page builds on.
  - [Probability & Bayes' Theorem, the intuition](/ai-ml/ai-ml-intuitions/foundational-mental-models/probability-and-belief/probability-and-bayes-intuition) — the intuition for updating a belief.
- **Videos**:
  - [Bayes theorem, the geometry of changing beliefs](https://www.youtube.com/watch?v=HZGCoVF3YvM) — **3Blue1Brown** — the update rule that drives all of it.
  - [Introduction to Bayesian statistics, part 1: the basic concepts](https://www.youtube.com/watch?v=0F0QoMCSKJ4) — **StataCorp** — priors, likelihoods, and posteriors clearly framed.
  - [The Bayesian Trap](https://www.youtube.com/watch?v=R13BD8qKeTg) — **Veritasium** — why the prior (base rate) cannot be ignored.
  - [You Know I'm All About that Bayes (Crash Course Statistics #24)](https://www.youtube.com/watch?v=9TDjifpGj-k) — **CrashCourse** — Bayesian vs frequentist thinking, accessibly.
- **Courses**:
  - [Harvard Stat 110: Probability (Bayes & conditioning)](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo) — **Joe Blitzstein (Harvard)** — the probabilistic foundations of Bayesian reasoning, free.
- **Interactive**:
  - [Seeing Theory — Ch. 5 (Bayesian Inference)](https://seeing-theory.brown.edu/bayesian-inference/index.html) — **Brown University** — interactive priors/likelihoods/posteriors.
- **Articles**:
  - [Stanford CS229 — MAP / Bayesian methods notes](https://cs229.stanford.edu/notes2021fall/cs229-notes1.pdf) — **Stanford (Ng et al.)** — MAP estimation and priors as regularization.
- **Papers**:
  - [Auto-Encoding Variational Bayes (VAE)](https://arxiv.org/abs/1312.6114) — **Kingma & Welling (2014)** — Bayesian inference scaled to deep models via the evidence lower bound.
- **Books**:
  - [Bayes Rules! An Introduction to Applied Bayesian Modeling](https://www.bayesrulesbook.com/) — **Johnson, Ott & Dogucu** — free full text: priors, posteriors, conjugate families, then Markov chain Monte Carlo and posterior checking; the most complete open textbook for building the workflow rather than just the formula.
  - [Mathematics for Machine Learning — **Ch. 8.3–8.4 (Estimation & Bayesian Inference)**](https://mml-book.github.io/book/mml-book.pdf) — **Deisenroth, Faisal & Ong** — maximum likelihood, maximum a posteriori, full Bayesian inference, and the role of priors.
  - [Think Bayes — **Ch. 1–5**](https://allendowney.github.io/ThinkBayes2/) — **Allen B. Downey** — Bayes, conjugacy, and estimation in code; free.
</content>
