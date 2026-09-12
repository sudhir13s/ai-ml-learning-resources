---
id: "world-models-and-embodied-ai/learning-and-planning/search-and-rollouts-muzero"
topic: "Search and Rollouts (MuZero)"
level: advanced
built_from: ["imagination-based-learning-dreamer", "markov-decision-processes"]
leads_to: ["world-models-and-embodied-ai/learning-and-planning/model-predictive-control-with-learned-models"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Search and Rollouts (MuZero)"
minutes: 15
category: learning-and-planning
---

# Search and Rollouts (MuZero)
> AlphaZero plans with a **given** simulator. MuZero throws the simulator away and learns three
> functions — **representation** (observation to latent), **dynamics** (latent plus action to next
> latent and reward), **prediction** (latent to policy and value) — then runs Monte Carlo tree search
> (MCTS) in that latent space. The model is never asked to reconstruct the world; it only has to
> predict **reward, value and policy** accurately enough for search to pick the right move.

**Why it matters:** this is the cleanest demonstration in the field that a world model does not need
to be a simulator of appearances — it needs to be **sufficient for the decision**. That reframing is
the most quotable idea in model-based reinforcement learning (RL), and the standard senior interview
follow-up: what does MuZero's latent state actually mean? (Nothing interpretable. It is trained only
through the search targets, which is precisely the point.)

**Start here — suggested path:**

1. **Get the idea without the maths** — read [MuZero: Mastering Go, chess, shogi and Atari without rules](https://deepmind.google/blog/muzero-mastering-go-chess-shogi-and-atari-without-rules/) — **Google DeepMind**. *The three learned functions and how search uses them, with the AlphaGo lineage.*
2. **Watch the paper walked through** — watch [MuZero: Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model](https://www.youtube.com/watch?v=We20YSAJZSE) — **Yannic Kilcher**. *Where the gradients come from and why value-equivalence is enough.*
3. **Read the source** — read [Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model](https://arxiv.org/abs/1911.08265) — **Schrittwieser et al. (2020)**. *The algorithm, the MCTS targets, and the Atari plus board-game results in one place.*
4. **Trace the lineage backwards** — skim [Mastering Chess and Shogi by Self-Play (AlphaZero)](https://arxiv.org/abs/1712.01815) — **Silver et al. (2017)**. *The same search with a perfect model; the contrast is what MuZero contributes.*
5. **See where the sample efficiency went** — read [Mastering Atari Games with Limited Data](https://arxiv.org/abs/2111.00210) — **Ye et al. (2021)**. *EfficientZero: MuZero at 100k frames, using self-supervised consistency to stabilise the learned dynamics.*

## Courses (free)

- [RL Course — Lecture 8: Integrating Learning and Planning](https://www.youtube.com/watch?v=ItMutbeOHtc) — **Google DeepMind (David Silver)** — model learning, Dyna and MCTS derived from scratch; the prerequisite lecture for MuZero.
- [CS 285: Deep RL, 2023](https://www.youtube.com/playlist?list=PL_iWQOsE6TfVYGEGiAOMaOzzv41Jfm_Ps) — **UC Berkeley (Sergey Levine, RAIL)** — the planning-with-learned-models lectures, including tree search and shooting methods.

## Videos

- [MuZero (paper explained)](https://www.youtube.com/watch?v=We20YSAJZSE) — **Yannic Kilcher** — the reference technical walkthrough.
- [MuZero — RL paper explained](https://www.youtube.com/watch?v=mH7f7N7s79s) — **Aleksa Gordić (The AI Epiphany)** — a second pass with more time on the MCTS implementation details.
- [From AlphaGo to MuZero](https://www.youtube.com/watch?v=lVMgxtm5L-U) — **Harvard CMSA (Thore Graepel, DeepMind)** — the whole lineage told by someone who worked on it.
- [RL Course — Lecture 8: Integrating Learning and Planning](https://www.youtube.com/watch?v=ItMutbeOHtc) — **Google DeepMind (David Silver)** — the classical foundation: search, simulation and planning.

## Key Papers

- [Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model](https://arxiv.org/abs/1911.08265) — **Schrittwieser et al. (2020)** — MuZero; value-equivalent latent dynamics plus MCTS.
- [Mastering Chess and Shogi by Self-Play with a General RL Algorithm](https://arxiv.org/abs/1712.01815) — **Silver et al. (2017)** — AlphaZero, the known-model baseline MuZero matches without the rules.
- [Mastering Atari Games with Limited Data](https://arxiv.org/abs/2111.00210) — **Ye et al. (2021)** — EfficientZero: the sample-efficiency fixes that made MuZero practical at small data budgets.
- [World Models](https://arxiv.org/abs/1803.10122) — **Ha & Schmidhuber (2018)** — the contrasting design: a model trained to reconstruct, not to be value-equivalent.

## Articles / Blogs (free, no paywall)

- [MuZero: Mastering Go, chess, shogi and Atari without rules](https://deepmind.google/blog/muzero-mastering-go-chess-shogi-and-atari-without-rules/) — **Google DeepMind** — the authors' own explainer, with the clearest diagram of the three networks.
- [A (Long) Peek into Reinforcement Learning](https://lilianweng.github.io/posts/2018-02-19-rl-overview/) — **Lilian Weng** — situates search-based planning inside the broader RL map.

## Books (free, with chapters)

- [*Reinforcement Learning: An Introduction* — Ch. 8 "Planning and Learning with Tabular Methods" (§8.11 Monte Carlo Tree Search)](http://incompleteideas.net/book/the-book-2nd.html) — **Sutton & Barto** — MCTS derived from rollout algorithms, free and authoritative.
- [*Algorithms for Decision Making*](https://algorithmsbook.com/) — **Kochenderfer, Wheeler & Wray** — online planning, forward search and sparse sampling, with implementations.

## In this platform

- Prerequisite: [Imagination-Based Learning (Dreamer)](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/learning-and-planning/imagination-based-learning-dreamer/imagination-based-learning-dreamer) · [Markov Decision Processes](/ai-ml/ai-ml-learning-resources/reinforcement-learning/foundations/markov-decision-processes/markov-decision-processes)
- Next: [Model Predictive Control with Learned Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/learning-and-planning/model-predictive-control-with-learned-models/model-predictive-control-with-learned-models)
- Canonical home elsewhere: [Model-Based RL](/ai-ml/ai-ml-learning-resources/reinforcement-learning/model-based-reinforcement-learning/model-based-rl/model-based-rl)
