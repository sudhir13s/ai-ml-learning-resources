---
id: "world-models-and-embodied-intelligence/learning-and-planning/imagination-based-learning-dreamer"
topic: "Imagination-Based Learning (Dreamer)"
level: advanced
built_from: ["recurrent-state-space-models-and-stochastic-dynamics"]
leads_to: ["search-and-rollouts-muzero", "model-predictive-control-with-learned-models"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Imagination-Based Learning (Dreamer)"
minutes: 16
category: learning-and-planning
---

# Imagination-Based Learning (Dreamer)
> Dreamer trains an actor and a critic **entirely on imagined rollouts** inside a learned latent
> model. Real experience is spent only on improving the model; the policy learns from millions of
> cheap dreamed trajectories. Because the rollouts happen in latent space, gradients flow back
> through the imagined future — you can backpropagate through your own imagination.

**Why it matters:** DreamerV3 was the first agent to master over 150 tasks with **one fixed set of
hyperparameters**, and the first to collect diamonds in Minecraft from scratch; the work was published
in *Nature* in 2025. **Dreamer 4** (2025) then did it purely from an offline dataset, with no
environment interaction at all. The interview substance is the failure mode: imagination is only as
good as the model, so short rollout horizons, value bootstrapping and normalisation tricks exist to
stop the policy exploiting model error.

**Start here — suggested path:**

1. **Get the loop** — read [Dream to Control: Learning Behaviors by Latent Imagination](https://arxiv.org/abs/1912.01603) — **Hafner et al. (2020)**. *Model, actor and critic; gradients propagated through imagined latent trajectories.*
2. **Watch the author explain it** — watch [Dream to Control](https://www.youtube.com/watch?v=BDxRNnhPTlU) — **Danijar Hafner**. *Twenty minutes that replace an afternoon of re-reading the paper.*
3. **See why it finally generalised** — read [Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104) — **Hafner et al. (2023; Nature 2025)**. *DreamerV3: symlog predictions, return normalisation, free bits — the robustness tricks that removed per-task tuning.*
4. **Hear the practitioner's take** — watch [Model Based RL Finally Works!](https://www.youtube.com/watch?v=vfpZu0R1s1Y) — **Edan Meyer**. *What changed between DreamerV2 and V3, framed for someone who has to implement it.*
5. **Follow it onto real robots and offline data** — read [DayDreamer](https://arxiv.org/abs/2206.14176) — **Wu et al. (2022)** — then [Training Agents Inside of Scalable World Models](https://arxiv.org/abs/2509.24527) — **Hafner, Yan & Lillicrap (2025)**. *One hour of real-robot learning; then Dreamer 4 mining diamonds from a fixed dataset.*

## Courses (free)

- [CS 285: Deep RL, 2023](https://www.youtube.com/playlist?list=PL_iWQOsE6TfVYGEGiAOMaOzzv41Jfm_Ps) — **UC Berkeley (Sergey Levine, RAIL)** — lectures 11-12 are the model-based-with-policies material Dreamer instantiates.
- [Tutorial on Model-Based Methods in Reinforcement Learning](https://sites.google.com/view/mbrl-tutorial) — **Igor Mordatch & Jessica Hamrick (ICML 2020)** — the taxonomy that places "learn in imagination" against "plan at decision time".

## Videos

- [Dream to Control: Learning Behaviors by Latent Imagination](https://www.youtube.com/watch?v=BDxRNnhPTlU) — **Danijar Hafner** — the primary-author walkthrough of the algorithm.
- [Model Based RL Finally Works!](https://www.youtube.com/watch?v=vfpZu0R1s1Y) — **Edan Meyer** — DreamerV3 explained with an implementer's eye for the robustness tricks.
- [CS 285: Lecture 12, Part 2 — Model-Based RL with Policies](https://www.youtube.com/watch?v=2POKgmzPAto) — **RAIL (Sergey Levine)** — backpropagating through a learned model, and why it is unstable without care.

## Key Papers

- [Dream to Control: Learning Behaviors by Latent Imagination](https://arxiv.org/abs/1912.01603) — **Hafner et al. (2020)** — Dreamer: actor-critic learning inside a latent world model.
- [Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104) — **Hafner et al. (2023; Nature 2025)** — DreamerV3: one configuration, 150-plus tasks, Minecraft diamonds from scratch.
- [DayDreamer: World Models for Physical Robot Learning](https://arxiv.org/abs/2206.14176) — **Wu et al. (2022)** — learning to walk in about an hour of real-world experience.
- [Training Agents Inside of Scalable World Models](https://arxiv.org/abs/2509.24527) — **Hafner, Yan & Lillicrap (2025)** — Dreamer 4: shortcut forcing and a transformer world model, trained fully offline.
- [Mastering Atari with Discrete World Models](https://arxiv.org/abs/2010.02193) — **Hafner et al. (2021)** — the intermediate step, and the source of the discrete-latent design.

## Articles / Blogs (free, no paywall)

- [DreamerV3 project page](https://danijar.com/project/dreamerv3/) — **Danijar Hafner** — results, videos and the paper's own summary of what each robustness trick fixes.
- [Dreamer 4 project page](https://danijar.com/project/dreamer4/) — **Danijar Hafner** — the 2025 offline agent, with interactive world-model footage.
- [danijar/dreamerv3](https://github.com/danijar/dreamerv3) — **Danijar Hafner** — the reference implementation; a single-file-ish codebase you can actually read.
- [DayDreamer project page](https://danijar.com/project/daydreamer/) — **Danijar Hafner** — the physical-robot videos that make the sample-efficiency claim tangible.

## Books (free, with chapters)

- [*Reinforcement Learning: An Introduction* — Ch. 8 "Planning and Learning with Tabular Methods"](http://incompleteideas.net/book/the-book-2nd.html) — **Sutton & Barto** — Dyna is imagination-based learning in its simplest possible form; read it before the deep version.

## In this platform

- Prerequisite: [Recurrent State-Space Models and Stochastic Dynamics](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/latent-dynamics/recurrent-state-space-models-and-stochastic-dynamics/recurrent-state-space-models-and-stochastic-dynamics)
- Siblings: [Search and Rollouts (MuZero)](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/learning-and-planning/search-and-rollouts-muzero/search-and-rollouts-muzero) · [Model Predictive Control with Learned Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/learning-and-planning/model-predictive-control-with-learned-models/model-predictive-control-with-learned-models)
- Canonical home for the RL framing: [Model-Based RL](/ai-ml/ai-ml-learning-resources/core-machine-learning/reinforcement-learning/model-based-reinforcement-learning/model-based-rl/model-based-rl) · [Markov Decision Processes](/ai-ml/ai-ml-learning-resources/core-machine-learning/reinforcement-learning/foundations/markov-decision-processes/markov-decision-processes)
