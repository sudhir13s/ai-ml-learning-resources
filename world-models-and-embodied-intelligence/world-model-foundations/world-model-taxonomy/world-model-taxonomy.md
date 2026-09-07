---
id: "world-models-and-embodied-intelligence/world-model-foundations/world-model-taxonomy"
topic: "World Model Taxonomy"
level: intermediate
built_from: ["what-is-a-world-model"]
leads_to: ["world-models-and-embodied-intelligence/world-model-foundations/observation-state-action-and-partial-observability", "world-models-and-embodied-intelligence/predictive-representation-models/jepa-foundations"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 14
title: "World Model Taxonomy"
minutes: 14
category: world-model-foundations
---

# World Model Taxonomy
> "World model" names at least three different things. **Generative (pixel-space)** models predict
> the next frame you would see. **Latent** models predict the next compressed state. **Joint-embedding
> predictive architectures (JEPA)** predict a *representation* of the future and never reconstruct
> pixels at all. Cutting across that: some world models are **simulators** you look at, others are
> **planning models** an agent computes with.

**Why it matters:** the taxonomy is the answer to "is Sora a world model?" — a question that gets
asked in interviews precisely because it has no one-word answer. Pixel prediction spends capacity on
texture and lighting that no planner needs; latent and JEPA models spend it on what changes the
decision. Naming the axis (**what is predicted**, **in what space**, **conditioned on what action**,
**used by whom**) is what separates a fluent answer from a name-dropping one.

**Start here — suggested path:**

1. **Fix the three prediction targets** — read [Understanding World or Predicting Future? A Comprehensive Survey of World Models](https://arxiv.org/abs/2411.14499) — **Ding et al. (2024)**. *The cleanest split: models that build an internal understanding vs models that forecast futures.*
2. **See why latent beats pixels** — read [Generative modelling in latent space](https://sander.ai/2025/04/15/latents.html) — **Sander Dieleman**. *Why almost every modern generative system predicts in a compressed space, and what that costs.*
3. **Hear the JEPA argument** — watch [A Path Towards Autonomous Machine Intelligence](https://www.youtube.com/watch?v=OKkEdTchsiE) — **IHES (Yann LeCun)**. *The case that reconstructing pixels is the wrong objective for a world model.*
4. **Take the simulator side seriously** — read [Is Sora a World Simulator? A Comprehensive Survey on General World Models and Beyond](https://arxiv.org/abs/2405.03520) — **Zhu et al. (2024)**. *The "scale video generation and physics emerges" position, surveyed with its evidence and its critics.*
5. **Place the embodied variants** — skim [A Comprehensive Survey on World Models for Embodied AI](https://arxiv.org/abs/2510.16732) — **(2025)**. *How the same taxonomy is used in robotics: prediction, planning, simulation, evaluation.*

## Courses (free)

- [Tutorial on Model-Based Methods in Reinforcement Learning](https://sites.google.com/view/mbrl-tutorial) — **Igor Mordatch & Jessica Hamrick (ICML 2020)** — slides and video that organise model-based methods by what the model is used for, not by architecture.
- [CS25: Transformers United](https://web.stanford.edu/class/cs25/) — **Stanford** — the seminar's world-modeling weeks track how the taxonomy shifted after video models arrived.

## Videos

- [A Path Towards Autonomous Machine Intelligence](https://www.youtube.com/watch?v=OKkEdTchsiE) — **IHES (Yann LeCun)** — the generative-vs-predictive distinction argued from first principles.
- [From Machine Learning to Autonomous Intelligence](https://www.youtube.com/watch?v=pd0JmT6rYcI) — **LMU München (Yann LeCun)** — the same architecture with more time spent on energy-based and hierarchical variants.

## Key Papers

- [Understanding World or Predicting Future? A Comprehensive Survey of World Models](https://arxiv.org/abs/2411.14499) — **Ding et al. (2024)** — the reference taxonomy, with generative games, driving, robotics and social simulation as case studies.
- [Is Sora a World Simulator? A Comprehensive Survey on General World Models and Beyond](https://arxiv.org/abs/2405.03520) — **Zhu et al. (2024)** — the survey written around exactly the interview question.
- [A Comprehensive Survey on World Models for Embodied AI](https://arxiv.org/abs/2510.16732) — **(2025)** — the robotics-facing cut: policy learning, planning, simulation, evaluation.
- [3D and 4D World Modeling: A Survey](https://arxiv.org/abs/2509.07996) — **(2025)** — the spatial branch: video-based, occupancy-based and LiDAR-based world modelling.
- [A Tutorial on World Models and Physical AI](https://arxiv.org/abs/2606.12783) — **Il-Seok Oh (2026)** — explicit-vs-implicit world models, with the rollout-planning distinction made carefully.

## Articles / Blogs (free, no paywall)

- [Generative modelling in latent space](https://sander.ai/2025/04/15/latents.html) — **Sander Dieleman (Google DeepMind)** — the definitive practitioner account of why prediction moved into latent space.
- [Cosmos Predict](https://research.nvidia.com/labs/dir/cosmos-predict1/) — **NVIDIA Research** — the industrial statement of the learned-simulator branch: open world foundation models built to be post-trained for robots and vehicles.
- [Genie 2: A large-scale foundation world model](https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/) — **Google DeepMind** — an action-conditioned generative simulator, useful to contrast with action-free video models.

## In this platform

- Prerequisite: [What Is a World Model](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/world-model-foundations/what-is-a-world-model/what-is-a-world-model)
- The three branches in detail: [JEPA Foundations](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/predictive-representation-models/jepa-foundations/jepa-foundations) · [Recurrent State-Space Models and Stochastic Dynamics](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/latent-dynamics/recurrent-state-space-models-and-stochastic-dynamics/recurrent-state-space-models-and-stochastic-dynamics) · [Interactive Video and Generative Simulators](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/video-and-generative-world-models/interactive-video-and-generative-simulators/interactive-video-and-generative-simulators)
- Canonical home elsewhere: [Video Diffusion Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/video-diffusion-models/video-diffusion-models) · [Variational Autoencoders and the ELBO](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/variational-autoencoders-vae-elbo/variational-autoencoders-vae-elbo)
