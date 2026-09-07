---
id: "world-models-and-embodied-intelligence/learning-and-planning/model-predictive-control-with-learned-models"
topic: "Model Predictive Control with Learned Models"
level: advanced
built_from: ["recurrent-state-space-models-and-stochastic-dynamics", "search-and-rollouts-muzero"]
leads_to: ["embodied-agents-and-perception-action-loops"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Model Predictive Control with Learned Models"
minutes: 15
category: learning-and-planning
---

# Model Predictive Control with Learned Models
> Model predictive control (MPC) plans a short action sequence, executes only the **first** action,
> then replans from the new observation. Pair that loop with a *learned* dynamics model and you get
> the most practical form of model-based control: the constant replanning keeps model error from
> compounding, because the model is only ever trusted for a handful of steps.

**Why it matters:** MPC is where world models meet real hardware — TD-MPC2 controls 104 continuous
tasks with one set of hyperparameters, and V-JEPA 2-AC plans robot motions this way with no reward
function at all. The interview substance is **why replanning beats open-loop rollout** and how
**uncertainty** enters: probabilistic ensembles (PETS) plan against the *distribution* of models, so
the planner avoids regions where the model disagrees with itself rather than exploiting them.

**Start here — suggested path:**

1. **Get the control loop** — watch [CS 285: Lecture 12, Part 1 — Model-Based RL with Policies](https://www.youtube.com/watch?v=UQGS4ycGv8g) — **RAIL (Sergey Levine)**. *Shooting methods, replanning, and the distribution-shift problem a learned model creates.*
2. **See uncertainty done right** — read [Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models](https://arxiv.org/abs/1805.12114) — **Chua et al. (2018)**. *PETS: ensembles plus particle propagation; separating what the model does not know from what is genuinely random.*
3. **Read the modern default** — read [TD-MPC2: Scalable, Robust World Models for Continuous Control](https://arxiv.org/abs/2310.16828) — **Hansen, Su & Wang (2024)**. *Decoder-free latent model, local trajectory optimisation, a value function for the tail beyond the horizon.*
4. **Run it** — clone [nicklashansen/tdmpc2](https://github.com/nicklashansen/tdmpc2) — **Nicklas Hansen**. *324 released checkpoints, including a 317M-parameter agent that does 80 tasks; a rare reproducible baseline.*
5. **See it without rewards** — read [V-JEPA 2](https://arxiv.org/abs/2506.09985) — **Meta FAIR (2025)**. *Planning to an image goal by minimising latent distance — MPC where the cost is a representation, not a reward.*

## Courses (free)

- [Tutorial on Model-Based Methods in Reinforcement Learning](https://sites.google.com/view/mbrl-tutorial) — **Igor Mordatch & Jessica Hamrick (ICML 2020)** — the decision-time-planning half of model-based RL, taught properly.
- [CS 285: Deep RL, 2023](https://www.youtube.com/playlist?list=PL_iWQOsE6TfVYGEGiAOMaOzzv41Jfm_Ps) — **UC Berkeley (Sergey Levine, RAIL)** — lectures 10-12: optimal control, planning, and model-based RL with learned dynamics.

## Videos

- [CS 285: Lecture 12, Part 1 — Model-Based RL with Policies](https://www.youtube.com/watch?v=UQGS4ycGv8g) — **RAIL (Sergey Levine)** — the lecture that makes replanning-versus-policy an explicit design choice.
- [CS 285: Lecture 12, Part 2 — Model-Based RL with Policies](https://www.youtube.com/watch?v=2POKgmzPAto) — **RAIL (Sergey Levine)** — backprop-through-model instability, and why short horizons plus a value function fix it.

## Key Papers

- [TD-MPC2: Scalable, Robust World Models for Continuous Control](https://arxiv.org/abs/2310.16828) — **Hansen, Su & Wang (2024)** — 104 tasks, one hyperparameter set, decoder-free latent planning.
- [Temporal Difference Learning for Model Predictive Control](https://arxiv.org/abs/2203.04955) — **Hansen, Wang & Su (2022)** — the original TD-MPC: short-horizon planning plus a learned terminal value.
- [Deep RL in a Handful of Trials using Probabilistic Dynamics Models](https://arxiv.org/abs/1805.12114) — **Chua et al. (2018)** — PETS; the reference treatment of epistemic versus aleatoric uncertainty in learned dynamics.
- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985) — **Meta FAIR (2025)** — goal-conditioned planning in a self-supervised latent space, on real arms.

## Articles / Blogs (free, no paywall)

- [TD-MPC2 project page](https://www.tdmpc2.com/) — **Nicklas Hansen** — results, videos and the scaling study across model sizes.
- [nicklashansen/tdmpc2](https://github.com/nicklashansen/tdmpc2) — **Nicklas Hansen** — clean PyTorch implementation; the planner is short enough to read in one sitting.
- [The Promise of Generalist Robotic Policies](https://sergeylevine.substack.com/p/the-promise-of-generalist-robotic) — **Sergey Levine** — why control researchers moved from per-task planners to general policies, and what planning still buys.

## Books (free, with chapters)

- [*Algorithms for Decision Making* — Part II "Sequential Problems" (online planning)](https://algorithmsbook.com/) — **Kochenderfer, Wheeler & Wray** — receding-horizon control, forward search and rollout policies with code.

## In this platform

- Prerequisite: [Recurrent State-Space Models and Stochastic Dynamics](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/latent-dynamics/recurrent-state-space-models-and-stochastic-dynamics/recurrent-state-space-models-and-stochastic-dynamics) · [Search and Rollouts (MuZero)](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/learning-and-planning/search-and-rollouts-muzero/search-and-rollouts-muzero)
- The goal-conditioned variant: [Video JEPA and Action-Conditioned JEPA](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/predictive-representation-models/video-jepa-and-action-conditioned-jepa/video-jepa-and-action-conditioned-jepa)
- Where it runs: [Embodied Agents and Perception-Action Loops](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/embodied-intelligence/embodied-agents-and-perception-action-loops/embodied-agents-and-perception-action-loops)
- Canonical home elsewhere: [Model-Based RL](/ai-ml/ai-ml-learning-resources/core-machine-learning/reinforcement-learning/model-based-reinforcement-learning/model-based-rl/model-based-rl)
