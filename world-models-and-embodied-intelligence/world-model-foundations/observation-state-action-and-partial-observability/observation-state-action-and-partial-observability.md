---
id: "world-models-and-embodied-intelligence/world-model-foundations/observation-state-action-and-partial-observability"
topic: "Observation, State, Action and Partial Observability"
level: intermediate
built_from: ["markov-decision-processes", "what-is-a-world-model"]
leads_to: ["recurrent-state-space-models-and-stochastic-dynamics", "latent-prediction-and-object-centric-representations"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Observation, State, Action and Partial Observability"
minutes: 14
category: world-model-foundations
---

# Observation, State, Action and Partial Observability
> An agent never sees the state of the world; it sees an **observation**. A camera frame hides
> what is behind the robot, how fast the ball is moving, and whether the door is locked. The
> partially observable Markov decision process (POMDP) is the formalism for that gap, and a
> **learned latent state** is what a world model builds to close it.

**Why it matters:** this is where world models stop being a video-generation trick and become
decision-making machinery. A single frame is not Markovian, so a policy conditioned on one frame
cannot be optimal; the fix is a **belief** — a distribution over what the world could be, updated
with every observation. Interviewers probe exactly this: why stacking four frames works for Atari,
why it fails for occlusion and object permanence, and what a recurrent latent state buys you.

**Start here — suggested path:**

1. **Separate the three words** — read [Spinning Up: Key concepts in RL](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html) — **OpenAI**. *States vs observations, fully vs partially observed, in half a page.*
2. **Get the formalism** — watch [Lecture 15: Partially Observable MDPs](https://www.youtube.com/watch?v=2dNp7QyoF_k) — **Pieter Abbeel (CS287, UC Berkeley)**. *Belief states, the belief-MDP construction, and why exact POMDP planning is intractable.*
3. **Ground it in the textbook** — read [*Algorithms for Decision Making*, Part IV "State Uncertainty"](https://algorithmsbook.com/) — **Kochenderfer, Wheeler & Wray**. *Belief updating, conditional plans and approximate POMDP solvers, with runnable Julia.*
4. **See the deep-learning answer** — read [Learning Latent Dynamics for Planning from Pixels](https://arxiv.org/abs/1811.04551) — **Hafner et al. (2019)**. *PlaNet learns a latent state from images and plans in it — a belief state you train rather than derive.*
5. **See it done end-to-end today** — skim [V-JEPA 2](https://arxiv.org/abs/2506.09985) — **Meta FAIR (2025)**. *An action-conditioned latent state learned from internet video, then used to plan robot motions toward image goals.*

## Courses (free)

- [CS 285: Deep RL, 2023](https://www.youtube.com/playlist?list=PL_iWQOsE6TfVYGEGiAOMaOzzv41Jfm_Ps) — **UC Berkeley (Sergey Levine, RAIL)** — the lectures that treat state, observation and the Markov property carefully before any algorithm.
- [Deep RL Course](https://huggingface.co/learn/deep-rl-course/unit0/introduction) — **Hugging Face** — free and hands-on; the place to feel the difference between a frame and a state by breaking an agent with occlusion.

## Videos

- [Lecture 15: Partially Observable MDPs](https://www.youtube.com/watch?v=2dNp7QyoF_k) — **Pieter Abbeel (CS287, UC Berkeley)** — the canonical lecture on belief states and POMDP solution methods.
- [L1: MDPs, Exact Solution Methods, Max-ent RL](https://www.youtube.com/watch?v=2GwBez0D20A) — **Pieter Abbeel (Foundations of Deep RL)** — the fully observed baseline you need before the partially observed case makes sense.

## Key Papers

- [Learning Latent Dynamics for Planning from Pixels](https://arxiv.org/abs/1811.04551) — **Hafner et al. (2019)** — PlaNet: a learned latent state that makes image-based control planable.
- [Deep Variational Reinforcement Learning for POMDPs](https://arxiv.org/abs/1806.02426) — **Igl et al. (2018)** — the explicit link between variational belief inference and deep RL.
- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985) — **Meta FAIR (2025)** — a modern latent state that transfers to robots without task-specific data.
- [Reinforcement Learning: An Overview](https://arxiv.org/abs/2412.05265) — **Kevin Murphy (2024)** — a current, well-organised reference that states the POMDP setting precisely.

## Articles / Blogs (free, no paywall)

- [Key concepts in RL](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html) — **OpenAI (Josh Achiam)** — the crispest short statement of state vs observation and what "Markov" buys you.
- [A (Long) Peek into Reinforcement Learning](https://lilianweng.github.io/posts/2018-02-19-rl-overview/) — **Lilian Weng** — the landscape article; the model-based and belief sections are the relevant ones here.
- [PlaNet: Learning latent dynamics for planning from pixels](https://danijar.com/project/planet/) — **Danijar Hafner** — the author's project page, with videos of what the learned state actually predicts.

## Books (free, with chapters)

- [*Reinforcement Learning: An Introduction* — Ch. 3 "Finite Markov Decision Processes" and §17.3 "Observations and State"](http://incompleteideas.net/book/the-book-2nd.html) — **Sutton & Barto** — the definition, then the honest discussion of what happens when the state is hidden.
- [*Algorithms for Decision Making* — Part IV "State Uncertainty"](https://algorithmsbook.com/) — **Kochenderfer, Wheeler & Wray** — belief updates and POMDP algorithms, free and complete.

## In this platform

- Prerequisite: [Markov Decision Processes](/ai-ml/ai-ml-learning-resources/core-machine-learning/reinforcement-learning/foundations/markov-decision-processes/markov-decision-processes) · [What Is a World Model](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/world-model-foundations/what-is-a-world-model/what-is-a-world-model)
- Next: [Recurrent State-Space Models and Stochastic Dynamics](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/latent-dynamics/recurrent-state-space-models-and-stochastic-dynamics/recurrent-state-space-models-and-stochastic-dynamics)
- Sequence models that carry the belief: [RNN / LSTM / GRU](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/rnn-lstm-gru/rnn-lstm-gru)
- Object permanence and occlusion as a benchmark: [Evaluating World Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/evaluation-and-safety/evaluating-world-models-prediction-planning-and-physical-consistency/evaluating-world-models-prediction-planning-and-physical-consistency)
