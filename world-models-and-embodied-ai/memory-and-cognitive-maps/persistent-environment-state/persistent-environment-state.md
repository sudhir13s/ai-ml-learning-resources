---
id: "world-models-and-embodied-ai/memory-and-cognitive-maps/persistent-environment-state"
topic: "Persistent Environment State"
level: advanced
built_from: ["world-models-and-embodied-ai/memory-and-cognitive-maps/episodic-world-memory", "world-models-and-embodied-ai/spatial-and-physical-world-models/object-permanence"]
leads_to: ["world-models-and-embodied-ai/evaluation-and-safety/evaluating-world-models-prediction-planning-and-physical-consistency", "world-models-and-embodied-ai/embodied-intelligence/embodied-agents-and-perception-action-loops"]
interview_frequency: low
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Persistent Environment State"
minutes: 16
category: memory-and-cognitive-maps
---

# Persistent Environment State
> Memory keeps what the model **saw**; persistent state keeps what the world **is**. If an agent
> knocks a cup off a table, leaves the room and comes back, the cup should still be on the floor —
> and it should still be on the floor in the next episode if the simulator is meant to be an
> environment rather than a video. The one sentence: **persistence is edits committed to world
> state, not frames retrieved from a buffer.**

**Why it matters:** it is the line between a generative video model and a usable **simulator**.
**Genie 3** advertises promptable world events and minutes-scale consistency; **WorldMem** shows
recorded changes (an object placed, wheat growing) reproduced on revisit. Evaluation caught up in
2025 with **WorldScore**, which scores controllability and 3D consistency rather than frame
prettiness. Interviewers probe **what exactly is the state** — pixels, latents, an explicit object
list, or a scene graph — and the underrated failure mode: **silent state reset**, where the model
re-renders a plausible room instead of the room the agent modified.

**Start here — suggested path:**

1. **See the target behaviour** — read [Genie 3: A new frontier for world models](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) — **Google DeepMind**. *Promptable world events plus consistency over minutes; read the limitations paragraph as carefully as the claims.*
2. **See state written and read back** — read [WorldMem: Long-term Consistent World Simulation with Memory](https://arxiv.org/abs/2504.12369) — **Xiao et al. (NeurIPS 2025)**. *Interactions are recorded into memory units and reproduced when the viewpoint returns.*
3. **Learn how it is scored** — read [WorldScore: A Unified Evaluation Benchmark for World Generation](https://arxiv.org/abs/2504.00983) — **Duan, Guo, Chen et al., Stanford (2025)**. *Controllability, 3D consistency and dynamics as separate axes, so "looks good" stops being the metric.*
4. **See the object-level route** — skim [Object-Centric Learning with Slot Attention](https://arxiv.org/abs/2006.15055) — **Locatello et al. (2020)**. *If state lives in slots, persistence becomes a per-object property you can inspect and edit.*
5. **See a persistent generated world** — read [Persistent Nature: A Generative Model of Unbounded 3D Worlds](https://arxiv.org/abs/2303.13515) — **Chai, Tucker, He & Isola (2023)**. *An explicit scene representation behind the generator so the same terrain persists as the camera roams.*

## Courses (free)

- [Tutorial on Model-Based Methods in Reinforcement Learning](https://sites.google.com/view/mbrl-tutorial) — **Igor Mordatch & Jessica Hamrick (ICML 2020)** — what a model must guarantee to be planned through, which is exactly what persistence buys.
- [Embodied AI Workshop](https://embodied-ai.org/) — **CVPR Embodied AI community** — the simulators and rearrangement tasks where persistent state is the whole task.

## Videos

- [Genie 3: An infinite world model](https://www.youtube.com/watch?v=n5x6yXDj0uo) — **Google DeepMind (Fruchter, Parker-Holder)** — the builders on promptable events and what still resets.
- [Genie 3: Creating dynamic worlds that you can navigate in real-time](https://www.youtube.com/watch?v=PDKhUknuQDg) — **Google DeepMind** — watch for revisits and for edits that survive them.

## Key Papers

- [WorldMem: Long-term Consistent World Simulation with Memory](https://arxiv.org/abs/2504.12369) — **Xiao et al. (2025)** — the clearest demonstration of environment changes surviving time and viewpoint gaps.
- [WorldScore: A Unified Evaluation Benchmark for World Generation](https://arxiv.org/abs/2504.00983) — **Duan et al., Stanford (2025)** — the evaluation that makes persistence claims falsifiable.
- [Video World Models with Long-term Spatial Memory](https://arxiv.org/abs/2506.05284) — **Wu et al. (2025)** — geometry-anchored state, which is what makes a revisit reproduce rather than re-imagine.
- [Long-Context State-Space Video World Models](https://arxiv.org/abs/2505.20171) — **Po et al. (2025)** — the cheaper-context route to the same property, with its own trade-offs.
- [Persistent Nature: A Generative Model of Unbounded 3D Worlds](https://arxiv.org/abs/2303.13515) — **Chai et al. (2023)** — an explicit world representation underneath a generative renderer.
- [Object-Centric Learning with Slot Attention](https://arxiv.org/abs/2006.15055) — **Locatello et al. (2020)** — object-level state, the representation persistence is easiest to define over.
- [Cosmos World Foundation Model Platform for Physical AI](https://arxiv.org/abs/2501.03575) — **NVIDIA (2025)** — open world foundation models built to be driven as environments, with the tokenizer and post-training recipes released.
- [VBench: Comprehensive Benchmark Suite for Video Generative Models](https://arxiv.org/abs/2311.17982) — **Huang, He, Yu et al. (2023)** — the video-quality baseline WorldScore deliberately departs from; useful as contrast.

## Articles / Blogs (free, no paywall)

- [WorldScore project page](https://haoyi-duan.github.io/WorldScore/) — **Duan et al. (Stanford)** — the leaderboard and per-axis breakdowns; the axis spread is the interesting part.
- [WorldMem project page](https://xizaoqu.github.io/worldmem/) — **Xiao et al.** — revisit videos with and without memory, plus the code.
- [NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/) — **NVIDIA** — the physical-AI framing, with open weights and the world-foundation-model vocabulary.

## In this platform

- Previous: [Cognitive Maps](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/memory-and-cognitive-maps/cognitive-maps/cognitive-maps) · sub-area start: [Episodic World Memory](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/memory-and-cognitive-maps/episodic-world-memory/episodic-world-memory)
- Where it is generated: [Interactive Video and Generative Simulators](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/video-and-generative-world-models/interactive-video-and-generative-simulators/interactive-video-and-generative-simulators) · [Video Diffusion Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/video-diffusion-models/video-diffusion-models)
- How it is scored: [Evaluating World Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/evaluation-and-safety/evaluating-world-models-prediction-planning-and-physical-consistency/evaluating-world-models-prediction-planning-and-physical-consistency)
- What it depends on: [Object Permanence](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/spatial-and-physical-world-models/object-permanence/object-permanence) · [Latent Prediction and Object-Centric Representations](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/predictive-representation-models/latent-prediction-and-object-centric-representations/latent-prediction-and-object-centric-representations)
