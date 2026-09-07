---
id: "07-computer-vision/3d-and-depth-estimation"
topic: "3D & Depth Estimation"
parent: "07-computer-vision"
level: advanced
built_from: ["cnns", "image-representation-and-filtering", "linear-algebra"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 10
title: "3D & Depth Estimation"
minutes: 10
category: computer-vision
---

# 3D & Depth Estimation
> Recover the third dimension from images. **Stereo** triangulates depth from two calibrated views via
> **epipolar geometry** and disparity; **monocular depth** estimation predicts a depth map from a single
> image with a CNN (MiDaS, Depth Anything); **structure-from-motion / multi-view** reconstructs 3D from
> many images; and **NeRF** represents a scene as a neural field for photorealistic novel-view synthesis.

**Why it matters:** the 3D-vision question for robotics, AR/VR, and autonomous-driving roles — the
pinhole camera model, why stereo gives metric depth but monocular is scale-ambiguous, how disparity
relates to depth (`depth ∝ 1/disparity`), epipolar geometry, and what NeRF's volumetric rendering does.
It tests whether you can reason geometrically, not just run a CNN.

**⭐ Start here — suggested path:**

1. **Monocular intuition** — watch ⭐ [How Neural Nets estimate depth from 2D images](https://www.youtube.com/watch?v=sz30TDttIBA). *Why a single image can predict depth and where it's ambiguous.*
2. **The 2D vs 3D framing** — read [Depth map](https://en.wikipedia.org/wiki/Depth_map) + [Neural Radiance Field overview](https://en.wikipedia.org/wiki/Neural_radiance_field). *Depth maps, disparity, and the NeRF idea.*
3. **NeRF in depth** — watch [NeRF Explained (Yannic Kilcher)](https://www.youtube.com/watch?v=CRlN-cYFxTk), then [Lecture 17: 3D Vision (EECS 498)](https://www.youtube.com/watch?v=S1_nCdLUQQ8) — **Michigan Online (Justin Johnson)**. *Volumetric rendering, then the full menu of 3D representations (voxels, point clouds, meshes, implicit fields).*
4. **Read the sources** — [Depth Map Prediction (Eigen)](https://arxiv.org/abs/1406.2283) → [MiDaS](https://arxiv.org/abs/1907.01341) (robust monocular depth) → ⭐ [NeRF](https://arxiv.org/abs/2003.08934). *Deep monocular depth, then neural scene representation.*
5. **Make it concrete** — explore the [NeRF project page](https://www.matthewtancik.com/nerf). *See the results and the rendering pipeline, with code.*
6. **See where this went in 2025–26** — read [Depth Anything V2](https://arxiv.org/abs/2406.09414) — **Yang et al. (2024)**. *Monocular depth is now a single pretrained model you call, trained largely on synthetic labels plus pseudo-labelled real images.*

## Courses (free)
- [First Principles of Computer Vision — Imaging & Stereo](https://fpcv.cs.columbia.edu/) — **Shree Nayar (Columbia)** — the camera model, epipolar geometry, and stereo, free.
- [Stanford CS231n](https://cs231n.github.io/) — **Stanford** — deep monocular depth and 3D representations appear in the later lectures.

## Videos
- [How Neural Nets estimate depth from 2D images](https://www.youtube.com/watch?v=sz30TDttIBA) — **Neural Breakdown with AVB** — monocular depth (MiDaS, Depth Anything), clearly explained.
- [NeRF: Neural Radiance Fields (Paper Explained)](https://www.youtube.com/watch?v=CRlN-cYFxTk) — **Yannic Kilcher** — volumetric rendering and novel-view synthesis from sparse views.
- [Lecture 17: 3D Vision (EECS 498)](https://www.youtube.com/watch?v=S1_nCdLUQQ8) — **Michigan Online (Justin Johnson)** — depth maps, voxels, point clouds, meshes, and implicit functions compared as representations.
- [Computer Vision Lecture 6.1 — Stereo Reconstruction](https://www.youtube.com/watch?v=VV9Eg--iEk8) — **Tübingen Machine Learning (Andreas Geiger)** — epipolar geometry and the disparity–depth relation that monocular methods only approximate.
- [Overview — Optical Flow](https://www.youtube.com/watch?v=lnXFcmLB7sM) — **First Principles of Computer Vision (Shree Nayar)** — motion/geometry foundations underpinning multi-view 3D.

## Key Papers
- [Depth Map Prediction from a Single Image (Eigen et al.)](https://arxiv.org/abs/1406.2283) — **Eigen et al. (2014)** — the first deep monocular depth network.
- [Towards Robust Monocular Depth Estimation (MiDaS)](https://arxiv.org/abs/1907.01341) — **Ranftl et al. (2019)** — cross-dataset training for robust, transferable depth.
- [NeRF: Representing Scenes as Neural Radiance Fields](https://arxiv.org/abs/2003.08934) — **Mildenhall et al. (2020)** — neural volumetric scene representation; a landmark.
- [Depth Anything V2](https://arxiv.org/abs/2406.09414) — **Yang et al. (2024)** — the 2025–26 default for monocular relative depth: synthetic labels plus large-scale pseudo-labelling, robust enough to use zero-shot.
- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985) — **Assran et al. (2025)** — where 3D understanding is heading: learned world models predicting in latent space instead of reconstructing geometry.

## Articles / Blogs (free, no paywall)
- [Depth map](https://en.wikipedia.org/wiki/Depth_map) — **Wikipedia** — depth maps, disparity, and the depth–disparity relationship.
- [Neural radiance field](https://en.wikipedia.org/wiki/Neural_radiance_field) — **Wikipedia** — the NeRF representation and volumetric rendering, free.
- [NeRF project page](https://www.matthewtancik.com/nerf) — **Mildenhall et al.** — results, method, and code, fully open.

## Books (free, with chapters)
- [Computer Vision: Algorithms and Applications, 2nd ed. — **Ch. 11 (Stereo)** + **Ch. 12 (3D reconstruction)**](https://szeliski.org/Book/) — **Richard Szeliski** — the geometric-vision backbone, free.
- [Dive into Deep Learning — **Ch. 14 (Computer Vision)**](https://d2l.ai/chapter_computer-vision/index.html) — **Zhang et al.** — the CNN backbone deep depth models build on, with code.

## In this platform
- Concept depth (the *why*): [ai-ml-intuitions 1.05 Spectral Methods (PCA / SVD)](/ai-ml/ai-ml-intuitions/representation/dimensionality-and-latent-structure/pca-and-svd-intuition) (the linear-algebra under projective geometry)
- Foundation: [Image Representation & Filtering](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/image-representation-and-filtering/image-representation-and-filtering) · [Deep Learning › CNNs & Convolution](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/cnns-and-convolution/cnns-and-convolution)
- Related: [Optical Flow & Video Understanding](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/optical-flow-and-video/optical-flow-and-video) (motion-based geometry) · image generation → [GenAI](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/readme)
