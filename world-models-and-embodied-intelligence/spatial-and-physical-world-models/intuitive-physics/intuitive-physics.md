---
id: "world-models-and-embodied-intelligence/spatial-and-physical-world-models/intuitive-physics"
topic: "Intuitive Physics"
level: intermediate
built_from: ["world-models-and-embodied-intelligence/spatial-and-physical-world-models/object-permanence", "graph-neural-networks"]
leads_to: ["world-models-and-embodied-intelligence/spatial-and-physical-world-models/causal-world-models", "world-models-and-embodied-intelligence/evaluation-and-safety/evaluating-world-models-prediction-planning-and-physical-consistency"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 17
title: "Intuitive Physics"
minutes: 17
category: spatial-and-physical-world-models
---

# Intuitive Physics
> **Intuitive physics** is the fast, approximate physical prediction people run constantly — will
> that stack topple, will the liquid spill, will the ball clear the gap. Machines get it three
> ways: a **learned simulator** over particles or meshes, a **generative video model** that has
> absorbed physics implicitly, or a **latent predictor** trained to be surprised by impossible
> events. The one sentence: **visual realism and physical understanding are different skills, and
> current models have far more of the first.**

**Why it matters:** this is where world models are judged. **Physics-IQ** (Google DeepMind, 2025)
showed that state-of-the-art video generators score near the floor on physical prediction while
looking flawless, and **Physion** measures the same for object-level prediction. Against that,
**V-JEPA** exhibits genuine violation-of-expectation surprise from self-supervised video
pretraining alone. Interviewers probe why **learned graph simulators generalise** (they encode
locality and permutation symmetry) while pixel generators do not. The underrated failure mode:
**judging a model by frame quality**, which is uncorrelated with physical correctness.

**Start here — suggested path:**

1. **See the failure measured** — read [Do generative video models understand physical principles?](https://arxiv.org/abs/2501.09038) — **Motamed, Culp, Swersky, Jaini & Fleet, Google DeepMind (2025)**. *Physics-IQ: 396 real videos, five physical domains; realism and understanding come apart completely.*
2. **See prediction from vision benchmarked** — skim [Physion: Evaluating Physical Prediction from Vision in Humans and Machines](https://arxiv.org/abs/2106.08261) — **Bear, Wang, Curtis et al. (2021)**. *Eight scenarios, one question — will these two objects touch? — with the human ceiling measured alongside.*
3. **See surprise emerge without labels** — read [Intuitive physics understanding emerges from self-supervised pretraining on natural videos](https://arxiv.org/abs/2502.11831) — **Garrido, Ballas, LeCun et al., Meta FAIR (2025)**. *A latent video predictor shows violation-of-expectation effects that pixel-space models do not.*
4. **Learn the structured alternative** — read [Learning to Simulate Complex Physics with Graph Networks](https://arxiv.org/abs/2002.09405) — **Sanchez-Gonzalez, Godwin, Pfaff, Ying, Leskovec & Battaglia (2020)**. *Message passing over particles generalises to ten times more particles and thousands of unseen steps.*
5. **Hear the cognitive-science case** — watch [A Conversation with Josh Tenenbaum](https://www.youtube.com/watch?v=NTbPgkt9oMA) — **MIT CBMM**. *The "intuitive physics engine" hypothesis: approximate simulation in the head, and what evidence supports it.*

## Courses (free)

- [RES.9-003 Brains, Minds and Machines Summer Course](https://ocw.mit.edu/courses/res-9-003-brains-minds-and-machines-summer-course-summer-2015/) — **MIT OpenCourseWare (CBMM)** — the lecture archive on intuitive physics, probabilistic programs and mental simulation.
- [CS 285: Deep Reinforcement Learning](http://rail.eecs.berkeley.edu/deeprlcourse/) — **UC Berkeley (Sergey Levine)** — the model-learning lectures: what a dynamics model must satisfy to be planned through.

## Videos

- [A Conversation with Josh Tenenbaum](https://www.youtube.com/watch?v=NTbPgkt9oMA) — **MIT CBMM** — the intuitive-physics-engine argument, with the developmental evidence behind it.
- [RSS 2020 keynote and question-and-answer](https://www.youtube.com/watch?v=D9xVj7oLVh4) — **Josh Tenenbaum (MIT), Robotics: Science and Systems** — how approximate simulation is used for planning, not just prediction.
- [Relational inductive biases, deep learning, and graph networks](https://www.youtube.com/watch?v=56e104J4ehA) — **University of Toronto CSC2547** — a careful reading of the Battaglia framework that underlies every learned simulator.

## Key Papers

- [Do generative video models understand physical principles?](https://arxiv.org/abs/2501.09038) — **Motamed et al., Google DeepMind (2025)** — the Physics-IQ result: realism does not imply understanding.
- [Intuitive physics understanding emerges from self-supervised pretraining on natural videos](https://arxiv.org/abs/2502.11831) — **Garrido et al., Meta FAIR (2025)** — the strongest evidence that latent prediction, not pixel prediction, buys physics.
- [Physion: Evaluating Physical Prediction from Vision in Humans and Machines](https://arxiv.org/abs/2106.08261) — **Bear et al. (2021)** — the object-level prediction benchmark with a human baseline.
- [Physion++: Evaluating Physical Scene Understanding that Requires Online Inference of Different Physical Properties](https://arxiv.org/abs/2306.15668) — **Tung et al. (2023)** — mass, friction and elasticity must be inferred from the clip itself.
- [Interaction Networks for Learning about Objects, Relations and Physics](https://arxiv.org/abs/1612.00222) — **Battaglia, Pascanu, Lai, Rezende & Kavukcuoglu, DeepMind (2016)** — the founding structured physics predictor.
- [Learning to Simulate Complex Physics with Graph Networks](https://arxiv.org/abs/2002.09405) — **Sanchez-Gonzalez et al. (2020)** — graph network simulators for fluids, sand and deformables.
- [Relational inductive biases, deep learning, and graph networks](https://arxiv.org/abs/1806.01261) — **Battaglia et al. (2018)** — why locality and permutation invariance are the reason these models generalise.
- [PhysGaussian: Physics-Integrated 3D Gaussians for Generative Dynamics](https://arxiv.org/abs/2311.12198) — **Xie, Zong, Qiu et al. (2023)** — a continuum-mechanics solver run directly on a Gaussian-splat scene.
- [PhysDreamer: Physics-Based Interaction with 3D Objects via Video Generation](https://arxiv.org/abs/2404.13026) — **Zhang, Yu, Wu et al. (2024)** — material properties distilled out of a video prior, so a static scene becomes interactive.
- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985) — **Assran et al., Meta FAIR (2025)** — the model whose physical prediction transfers to robot planning.

## Articles / Blogs (free, no paywall)

- [Physics-IQ benchmark](https://physics-iq.github.io/) — **Google DeepMind** — the videos, the per-model scores and the visual comparisons; the numbers are more persuasive than the abstract.
- [Learning to Simulate project page](https://sites.google.com/view/learning-to-simulate) — **Sanchez-Gonzalez, Battaglia et al.** — rollout videos across materials, which is where the generalisation claim becomes believable.
- [Genesis: a generative physics engine for robotics](https://genesis-embodied-ai.github.io/) — **Genesis Embodied AI collaboration** — an open, fast, differentiable multi-solver simulator; the 2025 platform for physics-grounded data generation.
- [Simulation as an engine of physical scene understanding](https://doi.org/10.1073/pnas.1306572110) — **Battaglia, Hamrick & Tenenbaum (PNAS, 2013)** — the original probabilistic-simulation account of human physical judgement.

## Books (free, with chapters)

- [*Algorithms for Decision Making* — Part II "Sequential Problems"](https://algorithmsbook.com/) — **Kochenderfer, Wheeler & Wray** — free textbook; how an approximate dynamics model is consumed by a planner.

## In this platform

- Previous: [Object Permanence](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/spatial-and-physical-world-models/object-permanence/object-permanence) · next: [Causal World Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/spatial-and-physical-world-models/causal-world-models/causal-world-models)
- How it is scored: [Evaluating World Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/evaluation-and-safety/evaluating-world-models-prediction-planning-and-physical-consistency/evaluating-world-models-prediction-planning-and-physical-consistency)
- Canonical home elsewhere: [Graph Neural Networks](/ai-ml/ai-ml-learning-resources/deep-learning/scientific-and-specialized-deep-learning/graph-neural-networks/graph-neural-networks) · [Physics-Informed Neural Networks](/ai-ml/ai-ml-learning-resources/deep-learning/scientific-and-specialized-deep-learning/physics-informed-neural-networks/physics-informed-neural-networks) · [Neural Operators](/ai-ml/ai-ml-learning-resources/deep-learning/scientific-and-specialized-deep-learning/neural-operators/neural-operators)
- Related in this section: [Video JEPA and Action-Conditioned JEPA](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/predictive-representation-models/video-jepa-and-action-conditioned-jepa/video-jepa-and-action-conditioned-jepa) · [Video Understanding](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/readme)
