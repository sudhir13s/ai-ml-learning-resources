---
id: "world-models-and-embodied-intelligence/embodied-intelligence/embodied-agents-and-perception-action-loops"
topic: "Embodied Agents and Perception-Action Loops"
level: intermediate
built_from: ["observation-state-action-and-partial-observability", "model-predictive-control-with-learned-models"]
leads_to: ["world-models-and-embodied-intelligence/embodied-intelligence/vision-language-action-models"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Embodied Agents and Perception-Action Loops"
minutes: 15
category: embodied-intelligence
---

# Embodied Agents and Perception-Action Loops
> An embodied agent closes a loop: **perceive, decide, act, change the world, perceive again**.
> Unlike a chatbot, its own actions determine its next inputs — so errors compound, data is
> expensive, and the distribution shifts under you. Simulators exist because that loop is too slow
> and too destructive to run only on real hardware.

**Why it matters:** embodiment is where world models are forced to be honest — a wrong prediction
becomes a dropped mug. The practical vocabulary an interviewer expects: the **sim-to-real gap**,
**domain randomisation** (train across randomised textures, lighting and physics so reality looks
like one more variation), and why **parallel GPU simulation** (thousands of environments at once)
changed what is trainable.

**Start here — suggested path:**

1. **Frame the loop** — read [Embodied AI Agents: Modeling the World](https://arxiv.org/abs/2506.22355) — **Meta FAIR (2025)**. *A current, readable statement of what an embodied agent needs beyond a language model.*
2. **Meet the simulators** — browse [AI Habitat](https://aihabitat.org/) — **Meta AI**. *Photorealistic indoor simulation for navigation and rearrangement, with the benchmark tasks defined.*
3. **See the GPU-parallel generation** — read [ManiSkill3](https://arxiv.org/abs/2410.00425) — **Tao et al. (2024)**. *Contact-rich manipulation at 30,000-plus frames per second; the throughput that makes sim-based training routine.*
4. **Learn the sim-to-real toolkit** — read [Domain Randomization for Transferring Deep Neural Networks](https://arxiv.org/abs/1703.06907) — **Tobin et al. (2017)**. *The idea in its simplest form: randomise the simulator until reality is in-distribution.*
5. **Hear where the field went** — watch [Robotic Foundation Models](https://www.youtube.com/watch?v=ET2HsfLrNMs) — **OpenDriveLab (Sergey Levine, CVPR 2024)**. *Why generalist policies replaced per-task controllers, and what data actually drives progress.*

## Courses (free)

- [CS 285: Deep RL, 2023](https://www.youtube.com/playlist?list=PL_iWQOsE6TfVYGEGiAOMaOzzv41Jfm_Ps) — **UC Berkeley (Sergey Levine, RAIL)** — the closest thing to a full course on learning-based control, free with assignments.
- [Embodied AI Workshop](https://embodied-ai.org/) — **CVPR Embodied AI community** — the annual survey of benchmarks, challenges and talks; the best single index of what "embodied AI" currently measures.
- [ManiSkill documentation and tutorials](https://maniskill.readthedocs.io/en/latest/) — **UC San Diego (Hao Su Lab)** — free, runnable notebooks that get an agent acting in simulation in minutes.

## Videos

- [Robotic Foundation Models](https://www.youtube.com/watch?v=ET2HsfLrNMs) — **OpenDriveLab (Sergey Levine)** — the CVPR 2024 talk on generalist robot policies and the data flywheel.
- [Lecture 15: Partially Observable MDPs](https://www.youtube.com/watch?v=2dNp7QyoF_k) — **Pieter Abbeel (CS287, UC Berkeley)** — the formal reason a robot's camera frame is not a state.

## Key Papers

- [Embodied AI Agents: Modeling the World](https://arxiv.org/abs/2506.22355) — **Meta FAIR (2025)** — world models, memory and multimodal perception as the components of an embodied agent.
- [Habitat 3.0: A Co-Habitat for Humans, Avatars and Robots](https://arxiv.org/abs/2310.13724) — **Puig et al. (2024)** — human-robot cohabitation simulation; the benchmark for social embodied tasks.
- [ManiSkill3: GPU Parallelized Robotics Simulation and Rendering](https://arxiv.org/abs/2410.00425) — **Tao et al. (2024)** — the throughput and task diversity that define the current simulation baseline.
- [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](https://arxiv.org/abs/1703.06907) — **Tobin et al. (2017)** — the canonical sim-to-real technique.
- [Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey](https://arxiv.org/abs/2009.13303) — **Zhao, Queralta & Westerlund (2020)** — the organised map of transfer techniques and their failure modes.

## Articles / Blogs (free, no paywall)

- [AI Habitat](https://aihabitat.org/) — **Meta AI** — simulator, datasets and tasks in one place; [habitat-lab](https://github.com/facebookresearch/habitat-lab) is the training code.
- [mani-skill/ManiSkill](https://github.com/mani-skill/ManiSkill) — **Hao Su Lab, UC San Diego** — the manipulation benchmark and simulator, actively maintained.
- [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) — **Google DeepMind** — the physics engine underneath much of this work, open-source since 2022.
- [The Promise of Generalist Robotic Policies](https://sergeylevine.substack.com/p/the-promise-of-generalist-robotic) — **Sergey Levine** — a clear-eyed account of what generalist embodied policies can and cannot yet do.

## In this platform

- Prerequisite: [Observation, State, Action and Partial Observability](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/world-model-foundations/observation-state-action-and-partial-observability/observation-state-action-and-partial-observability) · [Model Predictive Control with Learned Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/learning-and-planning/model-predictive-control-with-learned-models/model-predictive-control-with-learned-models)
- Next: [Vision-Language-Action Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/embodied-intelligence/vision-language-action-models/vision-language-action-models)
- Perception it depends on: [3D and Depth Estimation](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/3d-and-depth-estimation/3d-and-depth-estimation) · [Optical Flow and Video](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/optical-flow-and-video/optical-flow-and-video)
- Learning on real hardware: [Imagination-Based Learning (Dreamer)](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/learning-and-planning/imagination-based-learning-dreamer/imagination-based-learning-dreamer)
