---
id: "07-computer-vision/pose-estimation"
topic: "Pose Estimation"
parent: "07-computer-vision"
level: advanced
built_from: ["cnns", "object-detection", "semantic-segmentation"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Pose Estimation"
minutes: 10
category: computer-vision
---

# Pose Estimation
> Localize a set of **keypoints** (joints: wrists, elbows, knees…) for each person in an image, then
> connect them into a skeleton. The dominant approach predicts per-joint **heatmaps** with a CNN;
> multi-person methods are **top-down** (detect people → estimate each one's pose) or **bottom-up**
> (detect all joints → group them, e.g. OpenPose's Part Affinity Fields). 3D pose lifts this to depth.

**Why it matters:** a focused vision question for AR/robotics/sports/health roles — heatmap regression vs
direct coordinate regression, top-down vs bottom-up trade-offs (accuracy vs speed/scaling with crowd
size), how Part Affinity Fields associate joints to people, and how 2D pose is lifted to 3D. It cleanly
combines detection, dense prediction, and structured output.

**⭐ Start here — suggested path:**

1. **Build intuition** — watch ⭐ [Human Pose Estimation Explained (2D & 3D)](https://www.youtube.com/watch?v=_sobpAW16c0). *The task, keypoints, and the 2D→3D distinction.*
2. **Get the body-model view** — watch [Computer Vision Lecture 12.3 — Human Body Models](https://www.youtube.com/watch?v=xLQUusO567Y) — **Tübingen Machine Learning (Andreas Geiger)**. *Keypoints, skeletons, and parametric body models (SMPL) as one family — why 3D pose is a fitting problem.*
3. **Hands-on** — watch [Human Pose Estimation with Deep Learning (LearnOpenCV)](https://www.youtube.com/watch?v=UCoR-mF3KI8). *Run a heatmap-based estimator end to end.*
4. **Read the sources** — [DeepPose](https://arxiv.org/abs/1312.4659) → [OpenPose (Part Affinity Fields)](https://arxiv.org/abs/1611.08050) → ⭐ [Simple Baselines for Pose Estimation](https://arxiv.org/abs/1804.06208). *Regression → bottom-up association → the strong heatmap baseline.*
5. **Make it concrete** — work through [MediaPipe (pose landmark detection)](https://github.com/google-ai-edge/mediapipe). *Production-grade real-time pose with code.*

## Courses (free)
- [Stanford CS231n](https://cs231n.github.io/) — **Stanford** — pose/keypoint estimation appears within the detection & dense-prediction lectures.
- [MediaPipe (pose landmark detection)](https://github.com/google-ai-edge/mediapipe) — **Google AI Edge** — the open repository and docs for running real-time on-device pose estimation.

## Videos
- [Human Pose Estimation Explained (2D & 3D)](https://www.youtube.com/watch?v=_sobpAW16c0) — **What's AI (Louis-François Bouchard)** — the clearest conceptual overview.
- [Computer Vision Lecture 12.3 — Human Body Models](https://www.youtube.com/watch?v=xLQUusO567Y) — **Tübingen Machine Learning (Andreas Geiger)** — 2D keypoints, skeletons, and parametric 3D body models in one lecture.
- [Human Pose Estimation using Deep Learning](https://www.youtube.com/watch?v=UCoR-mF3KI8) — **LearnOpenCV** — a hands-on heatmap-based walkthrough.
- [Lecture 16: Detection and Segmentation (EECS 498)](https://www.youtube.com/watch?v=9AyMR4IhSWQ) — **Michigan Online (Justin Johnson)** — the dense-prediction and keypoint-head machinery heatmap pose builds on.

## Key Papers
- [DeepPose](https://arxiv.org/abs/1312.4659) — **Toshev & Szegedy (2014)** — first deep pose method (direct joint-coordinate regression).
- [Realtime Multi-Person 2D Pose Estimation (OpenPose)](https://arxiv.org/abs/1611.08050) — **Cao et al. (2016)** — bottom-up Part Affinity Fields for joint association.
- [Simple Baselines for Human Pose Estimation and Tracking](https://arxiv.org/abs/1804.06208) — **Xiao et al. (2018)** — the strong, minimal heatmap baseline.

## Articles / Blogs (free, no paywall)
- [OpenPose (official repo + docs)](https://github.com/CMU-Perceptual-Computing-Lab/openpose) — **CMU Perceptual Computing Lab** — reference implementation and explanation, free.
- [MediaPipe solutions and model cards](https://github.com/google-ai-edge/mediapipe) — **Google AI Edge** — the landmark topology, model cards, and runnable examples.
- [MMPose documentation](https://mmpose.readthedocs.io/en/latest/) — **OpenMMLab** — the maintained open toolbox: top-down and bottom-up 2D/3D pose, whole-body and animal keypoints, with reproducible configs.
- [Human Pose Estimation with Deep Learning](https://learnopencv.com/deep-learning-based-human-pose-estimation-using-opencv-cpp-python/) — **LearnOpenCV** — heatmaps and architectures, free.

## Books (free, with chapters)
- [Computer Vision: Algorithms and Applications, 2nd ed. — **Ch. 6.4 (Pose & keypoint estimation)**](https://szeliski.org/Book/) — **Richard Szeliski** — pose estimation in the recognition landscape, free.
- [Dive into Deep Learning — **Ch. 14 (Computer Vision)**](https://d2l.ai/chapter_computer-vision/index.html) — **Zhang et al.** — the detection/dense-prediction machinery pose builds on, with code.

## In this platform
- Foundation: [Object Detection](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/object-detection/object-detection) (top-down pose needs a detector) · [Semantic Segmentation](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/semantic-segmentation/semantic-segmentation) (heatmaps are dense prediction)
- Foundation: [Deep Learning › CNNs & Convolution](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/cnns-and-convolution/cnns-and-convolution)
- Related: [Optical Flow & Video Understanding](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/optical-flow-and-video/optical-flow-and-video) (pose tracking over time)
