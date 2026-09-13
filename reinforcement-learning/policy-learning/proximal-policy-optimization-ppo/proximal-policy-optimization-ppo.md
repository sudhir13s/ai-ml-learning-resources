---
id: "08-rl/ppo"
topic: "Proximal Policy Optimization (PPO)"
core_idea: "PPO clips the probability ratio between the new and old policy so no single update moves the policy too far, giving trust-region stability with first-order optimization — and it is the optimizer inside RLHF."
parent: "08-reinforcement-learning"
level: advanced
built_from: ["policy-gradients-reinforce", "actor-critic", "trpo"]
interview_frequency: very-high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Proximal Policy Optimization (PPO)"
minutes: 10
category: policy-learning
---

# Proximal Policy Optimization (PPO)
> TRPO's reliability without TRPO's machinery. PPO keeps the policy update inside a trust region using
> a **clipped surrogate objective**: it multiplies the advantage by the probability ratio
> `r(θ) = π_new/π_old`, then *clips* that ratio to `[1−ε, 1+ε]` so the update can't move the policy too
> far in one step — all with plain first-order SGD. Simple, stable, sample-efficient enough to reuse a
> batch for several epochs. It is the default deep-RL algorithm and the RL engine inside RLHF.

**Why it matters:** the single most-asked deep-RL interview topic. Write the clipped objective, explain
why clipping approximates TRPO's KL trust region, how the min(clipped, unclipped) prevents over-large
updates in both directions, the roles of the value loss and entropy bonus, and — crucially — how PPO is
the optimizer in **RLHF** (the policy is the LLM, the reward comes from a learned reward model, plus a
KL penalty to the reference model).

## References

The curated link library for this topic — in this platform, videos, courses, articles, papers, books — lives in a companion file so it can be reused as a standalone reference list:

**→ [Proximal Policy Optimization (PPO) — references](/ai-ml/ai-ml-learning-resources/reinforcement-learning/policy-learning/proximal-policy-optimization-ppo/proximal-policy-optimization-ppo#references-further-reading)**
