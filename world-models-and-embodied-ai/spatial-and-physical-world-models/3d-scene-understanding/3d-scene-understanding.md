---
id: "world-models-and-embodied-ai/spatial-and-physical-world-models/3d-scene-understanding"
topic: "3D Scene Understanding"
level: intermediate
built_from: ["world-models-and-embodied-ai/spatial-and-physical-world-models/spatial-representations", "3d-and-depth-estimation"]
leads_to: ["world-models-and-embodied-ai/spatial-and-physical-world-models/object-permanence", "world-models-and-embodied-ai/memory-and-cognitive-maps/spatial-memory"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "3D Scene Understanding"
minutes: 16
category: spatial-and-physical-world-models
---

# 3D Scene Understanding
> Turning images into a **usable 3D account of a scene** — depth per pixel, camera poses, room
> layout, object extents, and the relations between them. Classical pipelines solved this by
> optimisation (structure from motion, bundle adjustment); 2025's systems do it in one
> **feed-forward pass**. The one sentence: **perception now outputs geometry directly, and the
> open question is whether the model also understands what that geometry means.**

**Why it matters:** **VGGT** won the Best Paper award at the 2025 Conference on Computer Vision
and Pattern Recognition (CVPR) for predicting cameras, depth, point maps and tracks in under a
second, and **DUSt3R** removed camera calibration from the loop entirely. Meanwhile **VSI-Bench**
showed that multimodal large language models (MLLMs) that describe a room fluently still answer
"how far is the sofa from the door?" barely above chance. Interviewers probe exactly that split:
**geometric reconstruction is close to solved; spatial reasoning over the reconstruction is not.**

**Start here — suggested path:**

1. **See feed-forward 3D** — read [VGGT: Visual Geometry Grounded Transformer](https://arxiv.org/abs/2503.11651) — **Wang, Chen, Karaev, Vedaldi, Rupprecht & Novotny (CVPR 2025 Best Paper)**. *One transformer, one pass: cameras, depth maps, point maps and 3D tracks together.*
2. **See where it started** — read [DUSt3R: Geometric 3D Vision Made Easy](https://arxiv.org/abs/2312.14132) — **Wang, Leroy, Cabon et al., NAVER Labs (2023)**. *Two uncalibrated images in, aligned point maps out — no known intrinsics, no bundle adjustment.*
3. **Get monocular depth right** — skim [Depth Anything V2](https://depth-anything-v2.github.io/) — **Yang, Kang, Huang et al. (2024)**. *The practical depth backbone; synthetic-data training plus a teacher-student pipeline.*
4. **Meet the reasoning gap** — read [Thinking in Space: How Multimodal LLMs See, Remember, and Recall Spaces](https://arxiv.org/abs/2412.14171) — **Yang, Yang, Gupta, Han, Fei-Fei & Xie (2024)**. *VSI-Bench: models build implicit local maps but fail at egocentric-allocentric transformation.*
5. **Hear the systems view** — watch [From SLAM to Spatial AI](https://www.youtube.com/watch?v=BRRtlR0C_CY) — **Andrew Davison (Imperial College, at MIT Robotics)**. *Why a map is not the goal; the representation must serve the task the robot has.*

## Courses (free)

- [CS231A: Computer Vision, From 3D Reconstruction to Recognition](https://web.stanford.edu/class/cs231a/) — **Stanford** — cameras, epipolar geometry, structure from motion and multi-view stereo; the foundation the feed-forward models compress.
- [MIT 6.S980: Machine Learning for Inverse Graphics](https://www.scenerepresentations.org/courses/inverse-graphics-23/) — **Vincent Sitzmann (MIT)** — the learned half: scene representations, differentiable rendering, and 3D-aware networks.

## Videos

- [MIT Robotics — From SLAM to Spatial AI](https://www.youtube.com/watch?v=BRRtlR0C_CY) — **Andrew Davison (Imperial College London)** — the seminar that frames scene understanding as a systems problem, not a benchmark.
- [With Spatial Intelligence, AI Will Understand the Real World](https://www.youtube.com/watch?v=y8NtMZ7VGmU) — **Fei-Fei Li (TED)** — why 3D understanding is the bottleneck between perception and action.

## Key Papers

- [VGGT: Visual Geometry Grounded Transformer](https://arxiv.org/abs/2503.11651) — **Wang et al. (2025)** — CVPR 2025 Best Paper; the current default for one-shot multi-view 3D.
- [DUSt3R: Geometric 3D Vision Made Easy](https://arxiv.org/abs/2312.14132) — **Wang et al. (2023)** — pairwise point-map regression that dissolved the calibration requirement.
- [Grounding Image Matching in 3D with MASt3R](https://arxiv.org/abs/2406.09756) — **Leroy, Cabon & Revaud (2024)** — the matching head that makes DUSt3R usable for large-scale reconstruction.
- [Depth Anything V2](https://arxiv.org/abs/2406.09414) — **Yang et al. (2024)** — the monocular depth model most downstream embodied stacks actually call.
- [Thinking in Space: How Multimodal Large Language Models See, Remember, and Recall Spaces](https://arxiv.org/abs/2412.14171) — **Yang et al. (2024)** — VSI-Bench; the clearest measurement of the spatial-reasoning gap.
- [SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities](https://arxiv.org/abs/2401.12168) — **Chen et al., Google DeepMind (2024)** — synthesising 3D spatial question-answer data at scale to close part of that gap.
- [Holistic Evaluation of Multimodal LLMs on Spatial Intelligence](https://arxiv.org/abs/2508.13142) — **Cai et al. (2025)** — the 2025 follow-up that separates metric, relational and perspective-taking failures.

## Articles / Blogs (free, no paywall)

- [VGGT code and models](https://github.com/facebookresearch/vggt) — **Meta AI / Visual Geometry Group, Oxford** — weights, demo and the inference path; the fastest way to see the output format.
- [DUSt3R project page](https://dust3r.europe.naverlabs.com/) — **NAVER Labs Europe** — interactive results plus the global-alignment procedure explained.
- [Thinking in Space project page](https://vision-x-nyu.github.io/thinking-in-space.github.io/) — **Yang, Xie et al. (NYU)** — the cognitive-map probes and per-task breakdowns, worth more than the leaderboard number.

## Books (free, with chapters)

- [*Computer Vision: Algorithms and Applications* — Ch. 11 "Structure from motion" and Ch. 13 "3D reconstruction"](https://szeliski.org/Book/) — **Richard Szeliski** — free PDF; the classical solution these models learned to imitate.

## In this platform

- Previous: [Spatial Representations](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/spatial-and-physical-world-models/spatial-representations/spatial-representations) · next: [Object Permanence](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/spatial-and-physical-world-models/object-permanence/object-permanence)
- Canonical home elsewhere: [3D and Depth Estimation](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/3d-and-depth-estimation/3d-and-depth-estimation) · [Semantic Segmentation](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/semantic-segmentation/semantic-segmentation)
- Where it is used: [Embodied Agents and Perception-Action Loops](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/embodied-intelligence/embodied-agents-and-perception-action-loops/embodied-agents-and-perception-action-loops) · [Spatial Memory](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/memory-and-cognitive-maps/spatial-memory/spatial-memory)
