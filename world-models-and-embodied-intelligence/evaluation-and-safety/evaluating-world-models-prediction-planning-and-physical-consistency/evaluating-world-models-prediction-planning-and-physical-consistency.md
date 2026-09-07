---
id: "world-models-and-embodied-intelligence/evaluation-and-safety/evaluating-world-models-prediction-planning-and-physical-consistency"
topic: "Evaluating World Models: Prediction, Planning and Physical Consistency"
level: advanced
built_from: ["interactive-video-and-generative-simulators", "video-jepa-and-action-conditioned-jepa"]
leads_to: []
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Evaluating World Models: Prediction, Planning and Physical Consistency"
minutes: 15
category: evaluation-and-safety
---

# Evaluating World Models: Prediction, Planning and Physical Consistency
> A world model can be scored three ways: **prediction** (how close is the predicted future?),
> **planning** (does an agent using it succeed?), and **physical consistency** (does it obey object
> permanence, solidity and gravity?). These come apart badly. A model can win on pixel metrics,
> look photorealistic, and still fail a test a twelve-month-old passes.

**Why it matters:** the headline result of 2025-26 is that **visual realism and physical
understanding are uncorrelated** — Physics-IQ showed it across Sora, Runway, Lumiere, Stable Video
Diffusion and VideoPoet, and IntPhys 2 found most models at chance on occlusion-based violation of
expectation. In interviews this is the "how would you know it works?" question, and the right answer
names the failure modes: **compounding drift** over long rollouts, **hallucinated objects**, and
metrics that reward texture over dynamics.

**Start here — suggested path:**

1. **See the headline finding** — read [Do generative video models understand physical principles?](https://arxiv.org/abs/2501.09038) — **Motamed et al. (2025)**. *Physics-IQ: realism and physical understanding are essentially unrelated.*
2. **Test object permanence** — read [IntPhys 2](https://arxiv.org/abs/2506.09849) — **Bordes et al., Meta FAIR (2025)**. *Violation of expectation with occlusions; permanence, immutability, continuity, solidity.*
3. **Compare with humans** — read [Physion](https://arxiv.org/abs/2106.08261) — **Bear et al. (2021)**. *Predict whether two objects will touch; humans beat every model tested, which is the point.*
4. **Ask whether scaling fixes it** — read [How Far is Video Generation from World Model: A Physical Law Perspective](https://arxiv.org/abs/2411.02385) — **Kang et al. (2024)**. *Models interpolate within the training distribution and fail to extrapolate physical laws outside it.*
5. **Evaluate policies, not pixels** — read [WorldGym: World Model as An Environment for Policy Evaluation](https://arxiv.org/abs/2506.00613) — **(2025)**. *Using a world model as the evaluator, and what has to be true for that to be sound.*

## Courses (free)

- [Embodied AI Workshop](https://embodied-ai.org/) — **CVPR Embodied AI community** — the annual challenge results define what the field currently accepts as evidence.
- [Tutorial on Model-Based Methods in Reinforcement Learning](https://sites.google.com/view/mbrl-tutorial) — **Igor Mordatch & Jessica Hamrick (ICML 2020)** — the section on model error and how it propagates into planning failure.

## Videos

- [Genie 3: An infinite world model](https://www.youtube.com/watch?v=n5x6yXDj0uo) — **Google DeepMind (Fruchter, Parker-Holder)** — the builders discuss consistency horizons and where their model still drifts.
- [Objective-Driven AI](https://www.youtube.com/watch?v=MiqLoAZFRSE) — **Harvard CMSA (Yann LeCun)** — the argument that predicting unpredictable detail is the wrong target, which is an evaluation argument too.

## Key Papers

- [Do generative video models understand physical principles?](https://arxiv.org/abs/2501.09038) — **Motamed et al. (2025)** — the Physics-IQ benchmark and the realism-versus-understanding dissociation.
- [IntPhys 2: Benchmarking Intuitive Physics Understanding In Complex Synthetic Environments](https://arxiv.org/abs/2506.09849) — **Bordes et al. (2025)** — occlusion-focused violation of expectation; most models at chance.
- [Physion: Evaluating Physical Prediction from Vision in Humans and Machines](https://arxiv.org/abs/2106.08261) — **Bear et al. (2021)** — the human-model comparison that set the format.
- [Physion++](https://arxiv.org/abs/2306.15668) — **Tung et al. (2023)** — harder: infer mass, friction and elasticity online before predicting.
- [How Far is Video Generation from World Model: A Physical Law Perspective](https://arxiv.org/abs/2411.02385) — **Kang et al. (2024)** — the systematic in-distribution versus out-of-distribution study.
- [Hallucination in World Models is Predictable and Preventable](https://arxiv.org/abs/2606.27326) — **(2026)** — a recent treatment of the failure mode that matters most for planning.

## Articles / Blogs (free, no paywall)

- [google-deepmind/physics-IQ-benchmark](https://github.com/google-deepmind/physics-IQ-benchmark) — **Google DeepMind** — data and scoring code, so the headline claim can be reproduced.
- [facebookresearch/IntPhys2](https://github.com/facebookresearch/IntPhys2) — **Meta FAIR** — the benchmark implementation and evaluation protocol.
- [Physion project page](https://physion-benchmark.github.io/) — **Bear et al.** — scenario videos and the human-study setup.
- [Genie 3: A new frontier for world models](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) — **Google DeepMind** — worth reading for its own list of limitations, which is unusually candid.

## In this platform

- Prerequisite: [Interactive Video and Generative Simulators](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/video-and-generative-world-models/interactive-video-and-generative-simulators/interactive-video-and-generative-simulators) · [Video JEPA and Action-Conditioned JEPA](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/predictive-representation-models/video-jepa-and-action-conditioned-jepa/video-jepa-and-action-conditioned-jepa)
- Where the metrics come from: [Evaluation of Generative Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/evaluation-of-generative-models/evaluation-of-generative-models)
- Embodied benchmarks: [Embodied Agents and Perception-Action Loops](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-intelligence/embodied-intelligence/embodied-agents-and-perception-action-loops/embodied-agents-and-perception-action-loops)
- The biological reference standard: [Memory Systems, Hippocampus and Replay](/ai-ml/ai-ml-learning-resources/specialized-studies/neuroscience-and-brain-inspired-ai/memory-systems-hippocampus-replay/memory-systems-hippocampus-replay) · [Predictive Coding](/ai-ml/ai-ml-learning-resources/specialized-studies/neuroscience-and-brain-inspired-ai/predictive-coding/predictive-coding)
