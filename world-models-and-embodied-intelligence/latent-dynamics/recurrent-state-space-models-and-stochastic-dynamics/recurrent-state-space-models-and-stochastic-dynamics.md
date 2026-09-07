---
id: "world-models-and-embodied-intelligence/latent-dynamics/recurrent-state-space-models-and-stochastic-dynamics"
topic: "Recurrent State-Space Models and Stochastic Dynamics"
level: advanced
built_from: ["observation-state-action-and-partial-observability", "rnn-lstm-gru"]
leads_to: ["imagination-based-learning-dreamer", "model-predictive-control-with-learned-models"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Recurrent State-Space Models and Stochastic Dynamics"
minutes: 16
category: latent-dynamics
---

# Recurrent State-Space Models and Stochastic Dynamics
> A **recurrent state-space model (RSSM)** splits the latent state in two: a **deterministic** path
> that carries memory reliably forward, and a **stochastic** variable that absorbs everything the
> agent could not have known. Purely deterministic latents cannot represent uncertainty; purely
> stochastic ones forget. RSSM keeps both, and it is the engine inside every Dreamer.

**Why it matters:** the deterministic/stochastic split is the single most quoted design decision in
latent world models, and the reason PlaNet worked where earlier latent models did not. The 2020
follow-up added a second twist worth knowing: **discrete (categorical) latents** beat Gaussians for
video-game dynamics, because the world's futures are multi-modal — a door is open or shut, not
0.5 open. Expect to be asked why a Gaussian latent blurs, and what a straight-through estimator is
doing in the backward pass.

**Start here — suggested path:**

1. **Meet the architecture** — read [Learning Latent Dynamics for Planning from Pixels](https://arxiv.org/abs/1811.04551) — **Hafner et al. (2019)**. *PlaNet introduces RSSM: the deterministic-plus-stochastic latent and the multi-step overshooting objective.*
2. **See it drive behaviour** — watch [Dream to Control: Learning Behaviors by Latent Imagination](https://www.youtube.com/watch?v=BDxRNnhPTlU) — **Danijar Hafner**. *The author's own talk; the clearest account of what the latent state has to support.*
3. **Get the discrete-latent upgrade** — read [Mastering Atari with Discrete World Models](https://arxiv.org/abs/2010.02193) — **Hafner et al. (2021)**. *Categorical latents and straight-through gradients; why they fit multi-modal futures.*
4. **Read the lab write-up** — read [Mastering Atari with Discrete World Models](https://research.google/blog/mastering-atari-with-discrete-world-models/) — **Google Research**. *The same result with the diagrams and the intuition, minus the equations.*
5. **Contrast with pixel-space dynamics** — skim [Model-Based Reinforcement Learning for Atari](https://arxiv.org/abs/1903.00374) — **Kaiser et al. (2020)**. *SimPLe predicts frames directly; comparing it with RSSM shows exactly what latent dynamics saves.*

## Courses (free)

- [CS 285: Deep RL, 2023](https://www.youtube.com/playlist?list=PL_iWQOsE6TfVYGEGiAOMaOzzv41Jfm_Ps) — **UC Berkeley (Sergey Levine, RAIL)** — the model-learning lectures cover latent-space dynamics and compounding model error.
- [Tutorial on Model-Based Methods in Reinforcement Learning](https://sites.google.com/view/mbrl-tutorial) — **Igor Mordatch & Jessica Hamrick (ICML 2020)** — where latent dynamics sits among the alternatives.

## Videos

- [Dream to Control: Learning Behaviors by Latent Imagination](https://www.youtube.com/watch?v=BDxRNnhPTlU) — **Danijar Hafner** — the primary-author talk on the latent model and the actor-critic trained inside it.
- [World Models](https://www.youtube.com/watch?v=dPsXxLyqpfs) — **Yannic Kilcher** — the mixture-density recurrent network that preceded RSSM, explained in full.
- [CS 285: Lecture 12, Part 1 — Model-Based RL with Policies](https://www.youtube.com/watch?v=UQGS4ycGv8g) — **RAIL (Sergey Levine)** — how a learned latent model is used to train a policy, and where it breaks.

## Key Papers

- [Learning Latent Dynamics for Planning from Pixels](https://arxiv.org/abs/1811.04551) — **Hafner et al. (2019)** — the RSSM paper; deterministic-plus-stochastic latents, latent overshooting.
- [Mastering Atari with Discrete World Models](https://arxiv.org/abs/2010.02193) — **Hafner et al. (2021)** — DreamerV2's categorical latents; the first world-model agent at human-level Atari.
- [World Models](https://arxiv.org/abs/1803.10122) — **Ha & Schmidhuber (2018)** — the mixture-density RNN ancestor of RSSM, with temperature as an uncertainty knob.
- [Model-Based Reinforcement Learning for Atari](https://arxiv.org/abs/1903.00374) — **Kaiser et al. (2020)** — SimPLe: the pixel-space alternative and its sample-efficiency ceiling.
- [TransDreamer: Reinforcement Learning with Transformer World Models](https://arxiv.org/abs/2202.09481) — **Chen et al. (2022)** — replacing the recurrence with attention; the first step toward today's transformer world models.

## Articles / Blogs (free, no paywall)

- [PlaNet project page](https://danijar.com/project/planet/) — **Danijar Hafner** — rollout videos that make "the model imagines 50 steps ahead" concrete.
- [DreamerV2 project page](https://danijar.com/project/dreamerv2/) — **Danijar Hafner** — the discrete-latent results with the training curves and code links.
- [Mastering Atari with Discrete World Models](https://research.google/blog/mastering-atari-with-discrete-world-models/) — **Google Research** — the lab blog version, good for the intuition behind categorical latents.

## Books (free, with chapters)

- [*Probabilistic Machine Learning: Advanced Topics* — Part II "State-Space Models"](https://probml.github.io/pml-book/book2.html) — **Kevin Murphy** — free PDF; the classical inference and learning theory that RSSM approximates with neural networks.

## In this platform

- Prerequisite: [Observation, State, Action and Partial Observability](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/world-model-foundations/observation-state-action-and-partial-observability/observation-state-action-and-partial-observability) · [RNN / LSTM / GRU](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/rnn-lstm-gru/rnn-lstm-gru)
- Next: [Imagination-Based Learning (Dreamer)](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/learning-and-planning/imagination-based-learning-dreamer/imagination-based-learning-dreamer)
- The variational machinery: [Variational Autoencoders and the ELBO](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/variational-autoencoders-vae-elbo/variational-autoencoders-vae-elbo)
- Canonical home elsewhere: [Model-Based RL](/ai-ml/ai-ml-learning-resources/core-machine-learning/reinforcement-learning/model-based-reinforcement-learning/model-based-rl/model-based-rl)
