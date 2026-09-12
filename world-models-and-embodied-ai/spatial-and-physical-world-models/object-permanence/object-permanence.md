---
id: "world-models-and-embodied-ai/spatial-and-physical-world-models/object-permanence"
topic: "Object Permanence"
level: intermediate
built_from: ["world-models-and-embodied-ai/spatial-and-physical-world-models/3d-scene-understanding", "world-models-and-embodied-ai/world-model-foundations/observation-state-action-and-partial-observability"]
leads_to: ["world-models-and-embodied-ai/spatial-and-physical-world-models/intuitive-physics", "world-models-and-embodied-ai/memory-and-cognitive-maps/persistent-environment-state"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Object Permanence"
minutes: 15
category: spatial-and-physical-world-models
---

# Object Permanence
> **Object permanence** is the belief that a thing keeps existing, keeps its identity and keeps
> obeying physics while nobody can see it. Human infants have it within months; video models
> trained on the whole internet still lose an object the moment a box slides in front of it. The
> one sentence: **object permanence is the difference between modelling pixels and modelling
> things.**

**Why it matters:** it is the cleanest probe of whether a world model has state at all. **IntPhys
2** (Meta, 2025) built its entire benchmark on occlusion and found most video models at chance
(50%) where humans are near-perfect. Tracking systems hit the same wall: **SAM 2**'s memory bank
exists precisely so a mask survives an occlusion. Interviewers probe the distinction between
**re-detection** (finding a similar-looking blob later) and **permanence** (asserting the same
object continued to exist, unseen). The underrated failure mode: a tracker that scores well by
**identity switching** on re-appearance, which no aggregate metric catches.

**Start here — suggested path:**

1. **Get the developmental grounding** — watch [Allen School Distinguished Lecture](https://www.youtube.com/watch?v=u4jUxjf0bAY) — **Elizabeth Spelke (Harvard)**. *Core knowledge: infants represent objects as cohesive, continuous and solid before they have language for any of it.*
2. **Read the machine-learning translation** — skim [Building Machines That Learn and Think Like People](https://arxiv.org/abs/1604.00289) — **Lake, Ullman, Tenenbaum & Gershman (2016)**. *Why "intuitive physics and psychology as start-up software" became a research programme.*
3. **See the benchmark** — read [IntPhys 2: Benchmarking Intuitive Physics Understanding In Complex Synthetic Environments](https://arxiv.org/abs/2506.09849) — **Bordes, Garrido, Kao, Williams, Rabbat & Dupoux, Meta (2025)**. *Violation-of-expectation tests built only from occlusions; permanence, immutability, continuity, solidity.*
4. **See it as a tracking problem** — read [Learning to Track with Object Permanence](https://arxiv.org/abs/2103.14258) — **Tokmakov, Li, Burgard & Gaidon (2021)**. *Supervise the tracker on invisible objects, and it starts to hallucinate them correctly.*
5. **See the production answer** — read [SAM 2: Segment Anything in Images and Videos](https://arxiv.org/abs/2408.00714) — **Ravi et al., Meta (2024)**. *A streaming memory bank is what carries a mask through an occlusion; the design is explicit about it.*

## Courses (free)

- [RES.9-003 Brains, Minds and Machines Summer Course](https://ocw.mit.edu/courses/res-9-003-brains-minds-and-machines-summer-course-summer-2015/) — **MIT OpenCourseWare (CBMM)** — the full lecture archive on core knowledge, intuitive physics and how infants are tested; the material behind most of this page.
- [CS231A: Computer Vision, From 3D Reconstruction to Recognition](https://web.stanford.edu/class/cs231a/) — **Stanford** — the tracking and multi-view geometry prerequisites for reasoning about occluded objects.

## Videos

- [Allen School Distinguished Lecture: Elizabeth Spelke](https://www.youtube.com/watch?v=u4jUxjf0bAY) — **Paul G. Allen School, University of Washington** — Spelke on core systems, from the person whose experiments defined the field.
- [A Conversation with Josh Tenenbaum](https://www.youtube.com/watch?v=NTbPgkt9oMA) — **MIT CBMM** — the bridge from infant experiments to probabilistic programs and machine benchmarks.
- [RSS 2020 keynote and question-and-answer](https://www.youtube.com/watch?v=D9xVj7oLVh4) — **Josh Tenenbaum (MIT), Robotics: Science and Systems** — intuitive physics, planning and problem-solving, argued for a robotics audience.

## Key Papers

- [IntPhys: A Framework and Benchmark for Visual Intuitive Physics Reasoning](https://arxiv.org/abs/1803.07616) — **Riochet, Ynocente Castro, Bernard, Lerer, Fergus, Izard & Dupoux (2018)** — the original violation-of-expectation benchmark for machines.
- [IntPhys 2: Benchmarking Intuitive Physics Understanding In Complex Synthetic Environments](https://arxiv.org/abs/2506.09849) — **Bordes et al., Meta (2025)** — the occlusion-only successor; the current measurement of the gap.
- [Learning to Track with Object Permanence](https://arxiv.org/abs/2103.14258) — **Tokmakov et al. (2021)** — supervising trajectories through full occlusion rather than only on visible frames.
- [Object Permanence Emerges in a Random Walk along Memory](https://arxiv.org/abs/2204.01784) — **Tokmakov, Jabri, Li & Gaidon (2022)** — permanence learned without occlusion labels, from self-supervised temporal correspondence.
- [SAM 2: Segment Anything in Images and Videos](https://arxiv.org/abs/2408.00714) — **Ravi et al., Meta (2024)** — the memory-attention design that keeps object identity across disappearance.
- [CoTracker: It is Better to Track Together](https://arxiv.org/abs/2307.07635) — **Karaev, Rocco, Graham, Neverova, Vedaldi & Rupprecht (2023)** — joint point tracking; correlating points is what lets occluded ones be inferred.
- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985) — **Assran et al., Meta FAIR (2025)** — a latent predictor whose surprise signal responds to impossible-object videos.
- [Building Machines That Learn and Think Like People](https://arxiv.org/abs/1604.00289) — **Lake, Ullman, Tenenbaum & Gershman (2016)** — the position paper that put developmental core knowledge on the machine-learning agenda.

## Articles / Blogs (free, no paywall)

- [IntPhys 2 code and data](https://github.com/facebookresearch/IntPhys2) — **Meta AI** — the scenes, the scoring protocol and baseline results; run your own model against it in an afternoon.
- [CoTracker project page](https://co-tracker.github.io/) — **Visual Geometry Group, Oxford** — occlusion visualisations that make the permanence failure obvious at a glance.
- [SAM 2 repository](https://github.com/facebookresearch/sam2) — **Meta AI** — the memory bank and streaming inference, in code.

## In this platform

- Previous: [3D Scene Understanding](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/spatial-and-physical-world-models/3d-scene-understanding/3d-scene-understanding) · next: [Intuitive Physics](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/spatial-and-physical-world-models/intuitive-physics/intuitive-physics)
- Why state is not a frame: [Observation, State, Action and Partial Observability](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/world-model-foundations/observation-state-action-and-partial-observability/observation-state-action-and-partial-observability) · [Latent Prediction and Object-Centric Representations](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/predictive-representation-models/latent-prediction-and-object-centric-representations/latent-prediction-and-object-centric-representations)
- Canonical home elsewhere: [Instance Segmentation](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/instance-segmentation/instance-segmentation) · [Optical Flow and Video](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/optical-flow-and-video/optical-flow-and-video)
- How it is scored: [Evaluating World Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/evaluation-and-safety/evaluating-world-models-prediction-planning-and-physical-consistency/evaluating-world-models-prediction-planning-and-physical-consistency)
