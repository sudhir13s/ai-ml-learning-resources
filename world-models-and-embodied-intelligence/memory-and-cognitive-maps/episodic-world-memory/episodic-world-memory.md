---
id: "world-models-and-embodied-intelligence/memory-and-cognitive-maps/episodic-world-memory"
topic: "Episodic World Memory"
level: advanced
built_from: ["world-models-and-embodied-intelligence/latent-dynamics/recurrent-state-space-models-and-stochastic-dynamics", "world-models-and-embodied-intelligence/video-and-generative-world-models/interactive-video-and-generative-simulators"]
leads_to: ["world-models-and-embodied-intelligence/memory-and-cognitive-maps/spatial-memory", "world-models-and-embodied-intelligence/memory-and-cognitive-maps/persistent-environment-state"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Episodic World Memory"
minutes: 16
category: memory-and-cognitive-maps
---

# Episodic World Memory
> A recurrent state is a **summary**; episodic memory is a **record**. Long-horizon world models
> need both — a compact state to roll dynamics forward, and an addressable store of past frames
> and poses so a scene the agent walked away from ten minutes ago comes back the same. The one
> sentence: **consistency over minutes is a retrieval problem, not a bigger-hidden-state problem.**

**Why it matters:** **Genie 3** (Google DeepMind, August 2025) is the headline result — real-time
interactive worlds that stay consistent for **several minutes**, with the consistency described as
emerging from the model's memory of what it already generated. **WorldMem** (NeurIPS 2025) makes
the mechanism explicit with a memory bank of frames tagged by pose and timestamp. Interviewers
probe the trade-off: **context length is quadratic and forgetful; retrieval is cheap but needs a
key**. The underrated failure mode: a model that is locally smooth and globally amnesiac — every
frame plausible, the room different each time you turn around.

**Start here — suggested path:**

1. **See the 2025 capability** — read [Genie 3: A new frontier for world models](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) — **Google DeepMind**. *Real-time navigable worlds at 24 frames per second, with minutes-scale visual memory stated as a headline property.*
2. **Hear the builders on memory** — watch [Genie 3: An infinite world model](https://www.youtube.com/watch?v=n5x6yXDj0uo) — **Google DeepMind (Shlomi Fruchter, Jack Parker-Holder)**. *What "consistent for minutes" costs, and where it still breaks.*
3. **See the explicit mechanism** — read [WorldMem: Long-term Consistent World Simulation with Memory](https://arxiv.org/abs/2504.12369) — **Xiao, Zhou, Yang et al. (NeurIPS 2025)**. *A memory bank of frames plus pose and timestamp, read by memory attention; revisited views reconstruct.*
4. **Learn the training trick behind long rollouts** — read [Diffusion Forcing: Next-token Prediction Meets Full-Sequence Diffusion](https://arxiv.org/abs/2407.01392) — **Chen, Martí Monsó, Du et al. (MIT, 2024)**. *Per-token noise levels give stable, arbitrarily long, guidable sequence rollouts.*
5. **See the pre-video ancestor** — skim [Unsupervised Predictive Memory in a Goal-Directed Agent](https://arxiv.org/abs/1803.10760) — **Wayne, Hung, Amos et al., DeepMind (2018)**. *MERLIN: an external memory written by a predictive objective, which is still the cleanest statement of the idea.*

## Courses (free)

- [CS 285: Deep Reinforcement Learning](http://rail.eecs.berkeley.edu/deeprlcourse/) — **UC Berkeley (Sergey Levine)** — the model-learning lectures; where compounding error over long rollouts is derived rather than asserted.
- [Tutorial on Model-Based Methods in Reinforcement Learning](https://sites.google.com/view/mbrl-tutorial) — **Igor Mordatch & Jessica Hamrick (ICML 2020)** — what a model is used for, which determines what its memory must preserve.

## Videos

- [Genie 3: An infinite world model](https://www.youtube.com/watch?v=n5x6yXDj0uo) — **Google DeepMind (Fruchter, Parker-Holder)** — the researchers on memory, consistency and the remaining limits.
- [Genie 3: Creating dynamic worlds that you can navigate in real-time](https://www.youtube.com/watch?v=PDKhUknuQDg) — **Google DeepMind** — the demonstration reel; watch specifically for revisited viewpoints.

## Key Papers

- [WorldMem: Long-term Consistent World Simulation with Memory](https://arxiv.org/abs/2504.12369) — **Xiao et al. (2025)** — memory units keyed by pose and time, with dynamic evolution modelled rather than frozen.
- [Video World Models with Long-term Spatial Memory](https://arxiv.org/abs/2506.05284) — **Wu, Zhang, Chen et al. (2025)** — a geometry-grounded memory that survives viewpoint change better than a frame buffer.
- [Long-Context State-Space Video World Models](https://arxiv.org/abs/2505.20171) — **Po, Wu, Chen et al. (2025)** — state-space layers for linear-cost long context, and the accuracy it buys over windowed attention.
- [Diffusion Forcing: Next-token Prediction Meets Full-Sequence Diffusion](https://arxiv.org/abs/2407.01392) — **Chen et al. (2024)** — the training scheme that makes long, stable, controllable rollouts practical.
- [Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391) — **Bruce, Dennis, Edwards et al., Google DeepMind (2024)** — the latent-action foundation the Genie line builds memory on top of.
- [Unsupervised Predictive Memory in a Goal-Directed Agent](https://arxiv.org/abs/1803.10760) — **Wayne et al. (2018)** — MERLIN: prediction as the objective that decides what is worth storing.
- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985) — **Assran et al., Meta FAIR (2025)** — the contrast case: strong short-horizon latent prediction, without an episodic store.

## Articles / Blogs (free, no paywall)

- [WorldMem project page](https://xizaoqu.github.io/worldmem/) — **Xiao et al.** — side-by-side revisits with and without the memory bank; the failure mode becomes obvious in ten seconds.
- [Diffusion Forcing project page](https://boyuan.space/diffusion-forcing/) — **Boyuan Chen (MIT)** — rollouts, code and the noise-schedule intuition in one place.
- [Genie 2: A large-scale foundation world model](https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/) — **Google DeepMind** — the previous generation, useful as the baseline Genie 3's memory claim is measured against.
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) — **Lilian Weng** — the agent-side vocabulary for short-term versus long-term memory and retrieval, which this literature reuses.

## Books (free, with chapters)

- [*Reinforcement Learning: An Introduction* — Ch. 8 "Planning and Learning with Tabular Methods"](http://incompleteideas.net/book/the-book-2nd.html) — **Sutton & Barto** — Dyna's model store is the tabular ancestor of every episodic world memory.

## In this platform

- Next in this sub-area: [Spatial Memory](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/memory-and-cognitive-maps/spatial-memory/spatial-memory) · [Persistent Environment State](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/memory-and-cognitive-maps/persistent-environment-state/persistent-environment-state)
- Section context: [Interactive Video and Generative Simulators](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/video-and-generative-world-models/interactive-video-and-generative-simulators/interactive-video-and-generative-simulators) · [Recurrent State-Space Models and Stochastic Dynamics](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/latent-dynamics/recurrent-state-space-models-and-stochastic-dynamics/recurrent-state-space-models-and-stochastic-dynamics)
- Canonical home elsewhere: [Agent Memory](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/memory/memory) · [Video Diffusion Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/video-diffusion-models/video-diffusion-models)
- The brain's version: [Memory Systems, Hippocampus and Replay](/ai-ml/ai-ml-learning-resources/specialized-studies/neuroscience-and-brain-inspired-ai/memory-systems-hippocampus-replay/memory-systems-hippocampus-replay)
