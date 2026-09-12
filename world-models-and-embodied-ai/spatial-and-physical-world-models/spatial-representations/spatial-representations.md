---
id: "world-models-and-embodied-ai/spatial-and-physical-world-models/spatial-representations"
topic: "Spatial Representations"
level: intermediate
built_from: ["world-models-and-embodied-ai/world-model-foundations/world-model-taxonomy", "3d-and-depth-estimation"]
leads_to: ["world-models-and-embodied-ai/spatial-and-physical-world-models/3d-scene-understanding", "world-models-and-embodied-ai/memory-and-cognitive-maps/spatial-memory"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Spatial Representations"
minutes: 16
category: spatial-and-physical-world-models
---

# Spatial Representations
> A **spatial representation** is the data structure an agent keeps in place of the world: a
> scene graph of objects and relations, a voxel grid of occupancy, a neural field that answers
> "what is at this point?", or a bird's-eye-view (BEV) feature plane. Each choice fixes what the
> agent can ask cheaply and what it cannot ask at all. The one sentence: **the representation you
> pick is the set of spatial questions you can still answer after perception has run.**

**Why it matters:** the 2025–26 embodied stack is a fight over this choice. **3D Gaussian
splatting** displaced neural radiance fields (NeRF) for real-time rendering; **BEV features** are
the production representation in driving stacks; **object-centric slots** are what causal and
physical reasoning need. Interviewers probe the trade-off directly — explicit (voxels, meshes,
splats) versus implicit (neural fields) versus abstract (slots, scene graphs). The failure mode
people underrate: **a photorealistic representation that supports no query an agent actually
needs**, such as "is this object supported, and by what?"

**Start here — suggested path:**

1. **See the implicit idea working** — read [NeRF: Representing Scenes as Neural Radiance Fields](https://www.matthewtancik.com/nerf) — **Mildenhall, Srinivasan, Tancik et al. (2020)**. *A scene stored as the weights of a small network, queried by 3D point and viewing direction.*
2. **Watch the mechanism** — watch [NeRF: Neural Radiance Fields](https://www.youtube.com/watch?v=JuH79E8rdKc) — **Matthew Tancik (co-author)**. *Ten minutes on volume rendering, positional encoding, and why the rays matter.*
3. **See what replaced it** — read [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) — **Kerbl, Kopanas, Leimkühler & Drettakis, Inria (2023)**. *Explicit anisotropic Gaussians plus a rasteriser: same fidelity, real-time rendering, editable geometry.*
4. **Learn the driving-stack representation** — read [Lift, Splat, Shoot](https://arxiv.org/abs/2008.05711) — **Philion & Fidler, NVIDIA (2020)**. *How arbitrary camera rigs become one shared bird's-eye-view plane an agent can plan on.*
5. **Get the abstract alternative** — read [Object-Centric Learning with Slot Attention](https://arxiv.org/abs/2006.15055) — **Locatello et al. (2020)**. *Represent a scene as a small set of interchangeable slots, so physics and causality have entities to attach to.*

## Courses (free)

- [MIT 6.S980: Machine Learning for Inverse Graphics](https://www.scenerepresentations.org/courses/inverse-graphics-23/) — **Vincent Sitzmann (MIT)** — the course on neural fields and 3D scene representation, taught by one of the people who created the area; slides and reading list are open.
- [CS231A: Computer Vision, From 3D Reconstruction to Recognition](https://web.stanford.edu/class/cs231a/) — **Stanford** — the geometry prerequisites: cameras, triangulation, structure from motion, before any learned representation.

## Videos

- [NeRF: Neural Radiance Fields](https://www.youtube.com/watch?v=JuH79E8rdKc) — **Matthew Tancik** — the author's own walkthrough; the clearest ten minutes on volume rendering.
- [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://www.youtube.com/watch?v=T_kXY43VZnk) — **Inria GraphDeco (Kerbl et al.)** — the SIGGRAPH presentation, with the adaptive-density argument made visually.
- [NeRF: Representing Scenes as Neural Radiance Fields (paper explained)](https://www.youtube.com/watch?v=CRlN-cYFxTk) — **Yannic Kilcher** — a slower read of the paper, good on why positional encoding is load-bearing.
- [With Spatial Intelligence, AI Will Understand the Real World](https://www.youtube.com/watch?v=y8NtMZ7VGmU) — **Fei-Fei Li (TED)** — the argument that spatial representation, not language, is the next frontier.

## Key Papers

- [NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis](https://arxiv.org/abs/2003.08934) — **Mildenhall et al. (2020)** — the paper that made implicit neural scene representation the default.
- [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2308.04079) — **Kerbl et al. (2023)** — explicit primitives with a differentiable rasteriser; the representation most 2025–26 systems build on.
- [Neural Fields in Visual Computing and Beyond](https://arxiv.org/abs/2111.11426) — **Xie et al. (2021)** — the survey that organises every coordinate-based representation into one framework.
- [Lift, Splat, Shoot: Encoding Images From Arbitrary Camera Rigs by Implicitly Unprojecting to 3D](https://arxiv.org/abs/2008.05711) — **Philion & Fidler (2020)** — the origin of the modern bird's-eye-view pipeline.
- [BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers](https://arxiv.org/abs/2203.17270) — **Li et al. (2022)** — BEV features with temporal attention; the reference implementation for driving perception.
- [Object-Centric Learning with Slot Attention](https://arxiv.org/abs/2006.15055) — **Locatello et al. (2020)** — the slot mechanism behind object-centric world models.
- [Contrastive Learning of Structured World Models](https://arxiv.org/abs/1911.12247) — **Kipf, van der Pol & Welling (2019)** — objects as graph nodes, dynamics as edges; a scene graph you can roll forward.

## Articles / Blogs (free, no paywall)

- [Neural Fields in Visual Computing](https://neuralfields.cs.brown.edu/) — **Xie, Takikawa, Saito, Litany et al.** — the companion site to the survey; a map of the whole representation space with per-paper links.
- [3D Gaussian Splatting project page](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) — **Inria GraphDeco** — code, viewer, datasets and side-by-side comparisons against NeRF baselines.

## Books (free, with chapters)

- [*Computer Vision: Algorithms and Applications* — Ch. 12 "Depth estimation" and Ch. 13 "3D reconstruction"](https://szeliski.org/Book/) — **Richard Szeliski** — free PDF; the classical geometry every learned representation is still measured against.

## In this platform

- Next in this sub-area: [3D Scene Understanding](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/spatial-and-physical-world-models/3d-scene-understanding/3d-scene-understanding)
- Section context: [World Model Taxonomy](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/world-model-foundations/world-model-taxonomy/world-model-taxonomy) · [Latent Prediction and Object-Centric Representations](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/predictive-representation-models/latent-prediction-and-object-centric-representations/latent-prediction-and-object-centric-representations)
- Canonical home elsewhere: [3D and Depth Estimation](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/3d-and-depth-estimation/3d-and-depth-estimation) · [3D Generation and Score Distillation](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/3d-generation-score-distillation/3d-generation-score-distillation)
- Where it is used: [Interactive Video and Generative Simulators](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/video-and-generative-world-models/interactive-video-and-generative-simulators/interactive-video-and-generative-simulators) · [Spatial Memory](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/memory-and-cognitive-maps/spatial-memory/spatial-memory)
