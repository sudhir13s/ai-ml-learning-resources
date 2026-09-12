---
id: "classical-machine-learning"
topic: "Classical Machine Learning"
level: intermediate
built_from: ["ai-ml-orientation", "programming-and-data-foundations", "mathematical-foundations"]
updated: 2026-09-13
---

# Classical Machine Learning

> The algorithms that predate deep learning and still decide most production outcomes: fit a
> function to labelled data, or find structure without labels. This section is also where
> evaluation is taught properly — the bias-variance decomposition, cross-validation, calibration
> and error analysis are the vocabulary every later section borrows. On tabular data,
> gradient-boosted trees remain the thing to beat. Learning a policy from reward is its own
> section now: [Reinforcement Learning](/ai-ml/ai-ml-learning-resources/reinforcement-learning/readme).

**Start here:** [Bias-Variance Tradeoff](/ai-ml/ai-ml-learning-resources/classical-machine-learning/model-selection-and-evaluation/bias-variance-tradeoff/bias-variance-tradeoff) if you want the one idea the whole section is organized around, or [Supervised Learning](/ai-ml/ai-ml-learning-resources/classical-machine-learning/supervised-learning/readme) to start with the algorithms.

## Sub-areas

Each sub-area has its own curated index; each page inside is a resource card with a definition,
a five-step start-here path, and verified courses, videos, papers, articles and books.

1. [Supervised Learning](/ai-ml/ai-ml-learning-resources/classical-machine-learning/supervised-learning/readme) — **13 pages** — regression, classification, and trees and ensembles: linear and logistic models, support vector machines, k-nearest neighbours, random forests and gradient boosting.
2. [Unsupervised Learning](/ai-ml/ai-ml-learning-resources/classical-machine-learning/unsupervised-learning/readme) — **11 pages** — clustering, dimensionality reduction, density estimation, anomaly detection and association rules: structure with no answer key.
3. [Model Selection and Evaluation](/ai-ml/ai-ml-learning-resources/classical-machine-learning/model-selection-and-evaluation/readme) — **6 pages** — where error comes from, how to estimate generalization honestly, whether a probability means what it says, and how to read the failures.

## Courses (free)

- [CS229: Machine Learning — lecture notes](https://cs229.stanford.edu/main_notes.pdf) — **Stanford (Andrew Ng)** — the rigorous version of this entire section in one free PDF; derivations for every method here.
- [Machine Learning Specialization (free to audit)](https://www.coursera.org/specializations/machine-learning-introduction) — **Andrew Ng (DeepLearning.AI)** — the applied counterpart: supervised, unsupervised and recommenders with working code.
- [CS 285: Deep Reinforcement Learning — full lecture series](https://www.youtube.com/playlist?list=PL_iWQOsE6TfVYGEGiAOMaOzzv41Jfm_Ps) — **UC Berkeley RAIL (Sergey Levine)** — the standard graduate deep-RL course, recorded in full and free.
- [UCL Course on Reinforcement Learning](https://www.davidsilver.uk/teaching/) — **David Silver (DeepMind)** — the classic lecture series that derives the Bellman equations and dynamic programming.
- [Spinning Up in Deep RL](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html) — **OpenAI** — the cleanest modern introduction to states, returns, policies and value functions, with reference implementations.

## Videos

- [Reinforcement Learning: Essential Concepts](https://www.youtube.com/watch?v=Z-T0iJEXiwM) — **StatQuest with Josh Starmer** — gentle visual grounding for value, return and the one-step recursion.
- [RL Lecture 7: Policy Gradient Methods](https://www.youtube.com/watch?v=KHZVXao4qXs) — **David Silver (DeepMind)** — the actor-critic foundation, derived on a whiteboard by one of its practitioners.
- [Deep RL Bootcamp Lecture 4A: Policy Gradients](https://www.youtube.com/watch?v=S_gwYj1Q-44) — **Pieter Abbeel (UC Berkeley)** — the baseline and advantage construction, explained by the person who taught most of the field it.
- [MIT Data-Centric AI, Lecture 1](https://www.youtube.com/watch?v=ayzOzZGHZy4) — **MIT (Introduction to Data-Centric AI)** — why the measurement problem in section 4 is usually a dataset problem.

## Key Papers

- [A Few Useful Things to Know About Machine Learning](https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf) — **Pedro Domingos (2012)** — the best short statement of what generalization is and what it is not; read it before any algorithm.
- [Random Search for Hyper-Parameter Optimization](https://jmlr.org/papers/v13/bergstra12a.html) — **Bergstra and Bengio (JMLR, 2012)** — the canonical grid-versus-random result.
- [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599) — **Guo, Pleiss, Sun and Weinberger (2017)** — accuracy and honesty are different properties, and modern models trade the second for the first.
- [On Discriminative vs. Generative Classifiers](https://ai.stanford.edu/~ang/papers/nips01-discriminativegenerative.pdf) — **Ng and Jordan (2002)** — the logistic-regression versus naive-Bayes comparison, and what sample size does to it.
- [Reinforcement Learning: A Survey](https://www.jair.org/index.php/jair/article/view/10166) — **Kaelbling, Littman and Moore (JAIR, 1996)** — the survey that set the field's vocabulary, and still the clearest statement of the Bellman equations as the basis for value-based RL.

## Articles / Blogs (free, no paywall)

- [MLU-Explain](https://mlu-explain.github.io/) — **Amazon Machine Learning University (Jared Wilber and colleagues)** — interactive visual essays on cross-validation, bias-variance, random forests and the ROC curve.
- [Understanding the Bias-Variance Tradeoff](https://scott.fortmann-roe.com/docs/BiasVariance.html) — **Scott Fortmann-Roe** — the clearest free essay on the decomposition, with the dartboard picture everyone remembers.
- [A (Long) Peek into Reinforcement Learning](https://lilianweng.github.io/posts/2018-02-19-rl-overview/) — **Lilian Weng** — the whole RL formalism derived carefully in one post.
- [Policy Gradient Algorithms](https://lilianweng.github.io/posts/2018-04-08-policy-gradient/) — **Lilian Weng** — the actor-critic family from REINFORCE to PPO, in one place.
- [The Multi-Armed Bandit Problem and Its Solutions](https://lilianweng.github.io/posts/2018-01-23-multi-armed-bandit/) — **Lilian Weng** — epsilon-greedy, upper confidence bound and Thompson sampling with the regret analysis.

## Books (free, with chapters)

- [*An Introduction to Statistical Learning*](https://www.statlearning.com/) — **James, Witten, Hastie and Tibshirani** — free PDF with Python labs; the best applied first text for sections 1, 2 and 4.
- [*The Elements of Statistical Learning*](https://hastie.su.domains/ElemStatLearn/) — **Hastie, Tibshirani and Friedman** — free PDF; the rigorous companion, and the source of the bias-variance derivation.
- [*Reinforcement Learning: An Introduction*, 2nd ed.](http://incompleteideas.net/book/RLbook2020.pdf) — **Sutton and Barto** — free PDF; the standard text for section 3, chapter for chapter.
- [*Foundations of Machine Learning*](https://www.cs.nyu.edu/~mohri/mlbook/) — **Mohri, Rostamizadeh and Talwalkar** — free slides and materials; the learning-theory framing behind why any of this generalizes.
- [*Probabilistic Machine Learning: An Introduction*](https://probml.github.io/pml-book/book1.html) — **Kevin Murphy** — free PDF; the modern probabilistic treatment, with the decision theory section 4 depends on.

## In this platform

- Before this section: [Foundations](/ai-ml/ai-ml-learning-resources/foundations/readme) — [AI/ML Orientation](/ai-ml/ai-ml-learning-resources/foundations/ai-ml-orientation/readme) · [Programming and Data Foundations](/ai-ml/ai-ml-learning-resources/foundations/programming-and-data-foundations/readme) · [Mathematical Foundations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme)
- After this section: [Reinforcement Learning](/ai-ml/ai-ml-learning-resources/reinforcement-learning/readme) · [Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/readme) · [Models and Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/readme)
- Where RL reappears at LLM scale: [RLHF and DPO](/ai-ml/ai-ml-learning-resources/model-adaptation/preference-and-alignment-training/preference-and-alignment-training) · [Reinforcement Learning Post-Training — GRPO and Verifiable Rewards](/ai-ml/ai-ml-learning-resources/model-adaptation/reinforcement-learning-posttraining/reinforcement-learning-posttraining) · [World Models and Embodied AI](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/readme)
- Where evaluation continues after deployment: [Monitoring and Reliability](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/readme)
- The mental models: [Bias-Variance Tradeoff](/ai-ml/ai-ml-intuitions/objectives-and-evaluation/generalization/bias-variance-tradeoff-intuition) · [Bagging and Boosting](/ai-ml/ai-ml-intuitions/architectural-mechanisms/composition/bagging-and-boosting-intuition) · [PCA and SVD](/ai-ml/ai-ml-intuitions/representation/dimensionality-and-latent-structure/pca-and-svd-intuition) · [Bellman Equation and Q-Learning](/ai-ml/ai-ml-intuitions/decision-making-and-control/value-learning/bellman-equation-and-q-learning-intuition)
