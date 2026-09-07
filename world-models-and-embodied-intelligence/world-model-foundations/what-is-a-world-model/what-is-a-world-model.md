---
id: "world-models-and-embodied-intelligence/world-model-foundations/what-is-a-world-model"
topic: "What Is a World Model"
level: intermediate
built_from: ["markov-decision-processes", "rnn-lstm-gru"]
leads_to: ["world-models-and-embodied-intelligence/world-model-foundations/world-model-taxonomy", "observation-state-action-and-partial-observability"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 14
title: "What Is a World Model"
minutes: 14
category: world-model-foundations
---

# What Is a World Model
> A **world model** is a learned, internal simulator: given what an agent has seen and what it is
> about to do, it predicts what happens next. Train one on enough observation, and an agent can
> *rehearse* actions inside its own head instead of paying for every mistake in the real world.
> The one sentence: **a world model turns "act and see" into "predict, then act."**

**Why it matters:** this is the organizing idea behind the 2025–26 frontier — Genie 3's real-time
interactive worlds, V-JEPA 2's zero-shot robot planning, NVIDIA Cosmos for physical artificial
intelligence (AI), and Yann LeCun's AMI Labs, founded in December 2025 explicitly to build them.
Interviewers probe the difference between a **video generator** and a **world model** (action
conditioning and controllability, not visual fidelity), and the failure mode everyone underrates:
**compounding prediction error** over long rollouts.

**Start here — suggested path:**

1. **See the original demo** — read [World Models (interactive article)](https://worldmodels.github.io/) — **David Ha & Jürgen Schmidhuber**. *The vision-memory-controller decomposition, with playable figures; an agent trained entirely inside its own dream.*
2. **Get the paper's argument** — read [World Models](https://arxiv.org/abs/1803.10122) — **Ha & Schmidhuber (2018)**. *Why a compressed latent plus a recurrent predictor is enough to learn a policy without the real environment.*
3. **Hear the position** — watch [Objective-Driven AI: Towards AI systems that can learn, remember, reason, and plan](https://www.youtube.com/watch?v=MiqLoAZFRSE) — **Harvard CMSA (Yann LeCun)**. *The argument that a predictive world model, not next-token prediction, is the missing piece.*
4. **Read the blueprint** — skim [A Path Towards Autonomous Machine Intelligence](https://openreview.net/forum?id=BZ5a1r-kVsf) — **Yann LeCun (2022)**. *The configurator/perception/world-model/cost architecture that names every part of the modern debate.*
5. **See the 2026 state of the art** — read [Genie 3: A new frontier for world models](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) — **Google DeepMind**. *Real-time, promptable, navigable worlds at 24 frames per second — a world model you can walk around inside.*

## Courses (free)

- [CS25: Transformers United](https://web.stanford.edu/class/cs25/) — **Stanford** — the seminar series that hosts the world-modeling and representation-learning talks; lecture videos and slides are linked per week.
- [CS 285: Deep RL, 2023](https://www.youtube.com/playlist?list=PL_iWQOsE6TfVYGEGiAOMaOzzv41Jfm_Ps) — **UC Berkeley (Sergey Levine, RAIL)** — the model-based lectures are the rigorous version of "learn dynamics, then plan with them."

## Videos

- [World Models](https://www.youtube.com/watch?v=dPsXxLyqpfs) — **Yannic Kilcher** — a careful walk through the Ha & Schmidhuber architecture and why dreaming works.
- [Objective-Driven AI](https://www.youtube.com/watch?v=MiqLoAZFRSE) — **Harvard CMSA (Yann LeCun)** — the case for predictive world models over generative token prediction, from the person making it.
- [Genie 3: An infinite world model](https://www.youtube.com/watch?v=n5x6yXDj0uo) — **Google DeepMind (Shlomi Fruchter, Jack Parker-Holder)** — the builders explain what "consistent for minutes" actually requires.

## Key Papers

- [World Models](https://arxiv.org/abs/1803.10122) — **Ha & Schmidhuber (2018)** — the founding paper: vision (V), memory (M), controller (C), and policies trained inside the model.
- [A Path Towards Autonomous Machine Intelligence](https://openreview.net/forum?id=BZ5a1r-kVsf) — **Yann LeCun (2022)** — the position paper that made world models the central research programme.
- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985) — **Assran et al., Meta FAIR (2025)** — a video world model that plans real robot actions zero-shot from image goals.
- [A Definition and Roadmap for World Models](https://arxiv.org/abs/2607.06401) — **Chen et al. (2026)** — a recent attempt to pin down what the term should mean and what stages come next.

## Articles / Blogs (free, no paywall)

- [World Models](https://worldmodels.github.io/) — **David Ha & Jürgen Schmidhuber** — the interactive companion; still the clearest single explanation in the field.
- [Genie 3: A new frontier for world models](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) — **Google DeepMind** — the 2025 capability jump, with the memory and consistency claims stated plainly.
- [NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/) — **NVIDIA** — the "world foundation model" framing for robotics and driving, with open weights.

## Books (free, with chapters)

- [*Reinforcement Learning: An Introduction* — Ch. 8 "Planning and Learning with Tabular Methods"](http://incompleteideas.net/book/the-book-2nd.html) — **Sutton & Barto** — the tabular ancestor of every learned world model: Dyna's plan-act-learn loop.
- [*Algorithms for Decision Making*](https://algorithmsbook.com/) — **Kochenderfer, Wheeler & Wray** — free textbook; models, beliefs and planning under uncertainty stated formally.

## In this platform

- Next in this section: [World Model Taxonomy](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/world-model-foundations/world-model-taxonomy/world-model-taxonomy) · [Observation, State, Action and Partial Observability](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/world-model-foundations/observation-state-action-and-partial-observability/observation-state-action-and-partial-observability)
- Where it pays off: [Imagination-Based Learning (Dreamer)](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/learning-and-planning/imagination-based-learning-dreamer/imagination-based-learning-dreamer) · [Interactive Video and Generative Simulators](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/video-and-generative-world-models/interactive-video-and-generative-simulators/interactive-video-and-generative-simulators)
- Canonical home elsewhere: [Model-Based RL](/ai-ml/ai-ml-learning-resources/core-machine-learning/reinforcement-learning/model-based-reinforcement-learning/model-based-rl/model-based-rl) · [Markov Decision Processes](/ai-ml/ai-ml-learning-resources/core-machine-learning/reinforcement-learning/foundations/markov-decision-processes/markov-decision-processes) · [RNN / LSTM / GRU](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/rnn-lstm-gru/rnn-lstm-gru)
- The brain's version: [Predictive Coding](/ai-ml/ai-ml-learning-resources/specialized-studies/neuroscience-and-brain-inspired-ai/predictive-coding/predictive-coding)
