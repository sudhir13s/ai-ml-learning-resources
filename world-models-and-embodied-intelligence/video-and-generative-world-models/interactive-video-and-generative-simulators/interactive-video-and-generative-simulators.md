---
id: "world-models-and-embodied-intelligence/video-and-generative-world-models/interactive-video-and-generative-simulators"
topic: "Interactive Video and Generative Simulators"
level: advanced
built_from: ["world-model-taxonomy", "video-diffusion-models"]
leads_to: ["evaluating-world-models-prediction-planning-and-physical-consistency"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Interactive Video and Generative Simulators"
minutes: 16
category: video-and-generative-world-models
---

# Interactive Video and Generative Simulators
> A video generator produces a clip. A **generative simulator** produces the *next frame given your
> action* — and then the next, at interactive frame rates, staying consistent when you turn around
> and come back. That single difference, **action conditioning plus persistence**, is what turns
> video generation into a world model you can act in.

**Why it matters:** this is the most visible frontier of 2025-26 — Genie 3 generating navigable
720p worlds at 24 frames per second that stay consistent for minutes, GameNGen running DOOM as a
diffusion model at 20 frames per second, NVIDIA Cosmos shipping open world foundation models for
robotics and driving. It is also where the honest caveats live: **long-horizon drift**, memory that
only spans minutes, and benchmarks showing visual realism does not imply physical understanding.

**Start here — suggested path:**

1. **Start with the capability** — read [Genie 3: A new frontier for world models](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) — **Google DeepMind**. *Real-time promptable worlds, and the emergent memory claim stated precisely enough to argue with.*
2. **Hear the builders** — watch [Genie 3: An infinite world model](https://www.youtube.com/watch?v=n5x6yXDj0uo) — **Google DeepMind (Shlomi Fruchter, Jack Parker-Holder)**. *What "consistent for a few minutes" costs, and how it differs from Veo.*
3. **Read the founding paper** — read [Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391) — **Bruce et al., DeepMind (2024)**. *The latent action model: learning controls from unlabelled internet video, with no action labels anywhere.*
4. **See a game engine replaced** — read [Diffusion Models Are Real-Time Game Engines](https://arxiv.org/abs/2408.14837) — **Valevski et al. (2024)**. *GameNGen: DOOM at 20 frames per second, with human raters near chance at spotting the simulation.*
5. **Check the physics claim** — read [Do generative video models understand physical principles?](https://arxiv.org/abs/2501.09038) — **Motamed et al. (2025)**. *Physics-IQ: visual realism and physical understanding turn out to be uncorrelated.*

## Courses (free)

- [CS25: Transformers United](https://web.stanford.edu/class/cs25/) — **Stanford** — the seminar tracks video-model-as-world-model talks release by release; slides and recordings per week.
- [Tutorial on Model-Based Methods in Reinforcement Learning](https://sites.google.com/view/mbrl-tutorial) — **Igor Mordatch & Jessica Hamrick (ICML 2020)** — the framework for asking what a generated environment is actually *for*.

## Videos

- [Genie 3: An infinite world model](https://www.youtube.com/watch?v=n5x6yXDj0uo) — **Google DeepMind (Fruchter, Parker-Holder)** — the primary-source conversation about architecture and consistency.
- [Genie 3: A New Frontier for World Models](https://www.youtube.com/watch?v=1igh4oas1Ls) — **The TWIML AI Podcast (Sam Charrington)** — a longer, more technical interview with the same two researchers.
- [World Models](https://www.youtube.com/watch?v=dPsXxLyqpfs) — **Yannic Kilcher** — the 2018 ancestor: an agent trained inside a generated environment, which is exactly what these systems scale up.

## Key Papers

- [Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391) — **Bruce et al. (2024)** — the latent action model that makes unlabelled video controllable.
- [Diffusion Models Are Real-Time Game Engines](https://arxiv.org/abs/2408.14837) — **Valevski et al. (2024)** — GameNGen; interactive DOOM with a diffusion model, including the drift-mitigation tricks.
- [Cosmos World Foundation Model Platform for Physical AI](https://arxiv.org/abs/2501.03575) — **NVIDIA (2025)** — an open, post-trainable world foundation model plus tokenizer and data pipeline.
- [World Simulation with Video Foundation Models for Physical AI](https://arxiv.org/abs/2511.00062) — **NVIDIA (2025)** — the follow-up: video foundation models aimed squarely at simulation for robotics.
- [MineWorld: a Real-Time and Open-Source Interactive World Model on Minecraft](https://arxiv.org/abs/2504.08388) — **Guo et al. (2025)** — a fully open reproduction you can actually run and modify.
- [Is Sora a World Simulator? A Comprehensive Survey on General World Models and Beyond](https://arxiv.org/abs/2405.03520) — **Zhu et al. (2024)** — the survey built around the "video generation as world simulation" claim, evidence and objections included.
- [Do generative video models understand physical principles?](https://arxiv.org/abs/2501.09038) — **Motamed et al. (2025)** — the corrective: realism is not understanding.

## Articles / Blogs (free, no paywall)

- [Genie 3: A new frontier for world models](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) — **Google DeepMind** — the capability announcement, with the memory and consistency limits stated.
- [Genie 2: A large-scale foundation world model](https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/) — **Google DeepMind** — the previous generation; the two posts together show what scaling changed.
- [Cosmos Predict](https://research.nvidia.com/labs/dir/cosmos-predict1/) — **NVIDIA Research** — model cards, tokenizer details and post-training recipes for an open world foundation model.
- [GameNGen project page](https://gamengen.github.io/) — **Valevski et al.** — side-by-side footage of the real engine and the model; the fastest way to judge the claim.
- [Oasis project page](https://oasis-model.github.io/) — **Decart & Etched** — an open real-time Minecraft-style model with weights and a live demo.
- [NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/) — **NVIDIA** — the platform page for open world foundation models; [cosmos-predict2](https://github.com/nvidia-cosmos/cosmos-predict2) is the code.

## In this platform

- Prerequisite: [World Model Taxonomy](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/world-model-foundations/world-model-taxonomy/world-model-taxonomy)
- Canonical home for the generative machinery: [Video Diffusion Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/video-diffusion-models/video-diffusion-models) · [Diffusion Transformers (DiT)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/diffusion-transformers-dit/diffusion-transformers-dit)
- Long-video consistency elsewhere: [Long Video Understanding](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/long-video-understanding/long-video-understanding)
- Next: [Evaluating World Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/evaluation-and-safety/evaluating-world-models-prediction-planning-and-physical-consistency/evaluating-world-models-prediction-planning-and-physical-consistency)
- Agents trained inside generated worlds: [Imagination-Based Learning (Dreamer)](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/learning-and-planning/imagination-based-learning-dreamer/imagination-based-learning-dreamer)
