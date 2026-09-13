---
id: "19-advanced-math/game-theory-multi-agent"
topic: "Game Theory & Multi-Agent Math"
core_idea: "When several learners optimize against each other, the target is an equilibrium rather than a minimum, so GAN training, self-play and multi-agent RL are all problems of finding and reaching one."
parent: "19-advanced-research-mathematics"
level: advanced
built_from: ["probability", "convex-analysis-duality", "optimization"]
interview_frequency: medium
updated: 2026-06-20
tier: core
est_minutes: 10
title: "Game Theory & Multi-Agent Math"
minutes: 10
category: advanced-mathematics-for-ai-research
---

# Game Theory & Multi-Agent Math
> The mathematics of strategic interaction among rational agents: normal- and extensive-form games,
> dominant strategies, **Nash equilibrium** (and its existence via fixed-point theorems), mixed
> strategies, minimax/zero-sum duality, correlated equilibria, and the learning dynamics
> (no-regret, fictitious play) by which agents *reach* equilibria. The decision-theoretic backbone of
> multi-agent RL, mechanism design, and adversarial training.

**Why it matters:** GAN training is a two-player minimax game (and its instabilities are
equilibrium-finding instabilities); adversarial robustness is a game against a perturbing adversary;
multi-agent RL, self-play (AlphaGo/AlphaZero), and RLHF reward modeling all live here. Minimax duality
ties straight back to convex duality (card 4), and "what is a Nash equilibrium, and why does one
always exist?" is a recurring interview question.

## References

The curated link library for this topic — in this platform, videos, courses, articles, papers, books — lives in a companion file so it can be reused as a standalone reference list:

**→ [Game Theory & Multi-Agent Math — references](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/advanced-mathematics-for-ai-research/game-theory-and-multi-agent-math/game-theory-and-multi-agent-math#references-further-reading)**
