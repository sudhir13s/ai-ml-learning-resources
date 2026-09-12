---
id: "07-computer-vision/instance-segmentation"
topic: "Instance Segmentation (Mask R-CNN)"
parent: "07-computer-vision"
level: advanced
built_from: ["object-detection", "semantic-segmentation"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Instance Segmentation (Mask R-CNN)"
minutes: 10
category: computer-vision
---

# Instance Segmentation — Mask R-CNN
> Instance segmentation = detection **+** per-pixel masks: not just "there are 3 people" (semantic
> segmentation merges them) but "person #1 is *these* pixels, person #2 is *those*." **Mask R-CNN**
> extends Faster R-CNN with a parallel mask branch and replaces RoIPool with **RoIAlign** (no
> quantization), producing sharp per-instance masks — the standard architecture for this task.

**Why it matters:** the classic "explain Mask R-CNN" question — how it builds on Faster R-CNN, why
**RoIAlign** matters (the misalignment RoIPool introduces and how bilinear sampling fixes it), why the
mask branch is per-class and decoupled from classification, and the precise difference between semantic,
instance, and panoptic segmentation. A favorite for senior CV roles.

**⭐ Start here — suggested path:**

1. **Place it in the landscape** — watch [CS231n Lec 11: Detection & Segmentation](https://www.youtube.com/watch?v=nDPWywWRIRo). *Where instance segmentation sits relative to detection and semantic segmentation.*
2. **Get the architecture** — watch ⭐ [Instance Segmentation — Mask R-CNN (UCF)](https://www.youtube.com/watch?v=P2LWNdH3bi8). *RoIAlign vs RoIPool and the mask branch, lecture-quality.*
3. **Read the sources** — [Faster R-CNN](https://arxiv.org/abs/1506.01497) → ⭐ [Mask R-CNN](https://arxiv.org/abs/1703.06870). *The detector it extends, then the mask branch + RoIAlign.*
4. **Make it concrete** — work through [Detectron2](https://detectron2.readthedocs.io/en/latest/). *Run/train Mask R-CNN on COCO and inspect the masks.*
5. **See where this went in 2025–26** — read [Segment Anything](https://arxiv.org/abs/2304.02643) → [SAM 2](https://arxiv.org/abs/2408.00714) → [SAM 3](https://arxiv.org/abs/2511.16719). *Promptable, class-agnostic masks replaced the "train a mask head per dataset" workflow; SAM 2 adds video memory, SAM 3 adds open-vocabulary concepts.*

## Courses (free)
- [Stanford CS231n](https://cs231n.github.io/) — **Stanford** — Lecture 11 covers instance segmentation alongside detection and semantic segmentation.
- [Detectron2 documentation & tutorials](https://detectron2.readthedocs.io/en/latest/) — **Meta AI** — the open framework for training Mask R-CNN, with runnable tutorials.

## Videos
- [CS231n Lecture 11 — Detection & Segmentation](https://www.youtube.com/watch?v=nDPWywWRIRo) — **Stanford** — situates instance segmentation in the dense-prediction landscape.
- [Instance Segmentation — Mask R-CNN Architecture](https://www.youtube.com/watch?v=P2LWNdH3bi8) — **UCF CRCV** — RoIAlign vs RoIPool and the mask branch, lecture-quality.
- [Lecture 16: Detection and Segmentation (EECS 498)](https://www.youtube.com/watch?v=9AyMR4IhSWQ) — **Michigan Online (Justin Johnson)** — the modern treatment: semantic vs instance vs panoptic, and Mask R-CNN in full.
- [CS231n Winter 2016 Lecture 13 — Segmentation and Attention](https://www.youtube.com/watch?v=ByjaPdWXKJ4) — **Andrej Karpathy** — where per-pixel and per-instance prediction diverge, taught from first principles.

## Key Papers
- [Mask R-CNN](https://arxiv.org/abs/1703.06870) — **He et al. (2017)** — the reference instance-segmentation architecture (mask branch + RoIAlign).
- [Faster R-CNN](https://arxiv.org/abs/1506.01497) — **Ren et al. (2015)** — the detector Mask R-CNN extends; the Region Proposal Network.
- [Segment Anything (SAM)](https://arxiv.org/abs/2304.02643) — **Kirillov et al. (2023)** — promptable, class-agnostic segmentation trained on 1B masks; the zero-shot baseline every 2026 pipeline starts from.
- [SAM 2: Segment Anything in Images and Videos](https://arxiv.org/abs/2408.00714) — **Ravi et al. (2024)** — a streaming memory module carries masks across frames, making instance segmentation temporal.
- [SAM 3: Segment Anything with Concepts](https://arxiv.org/abs/2511.16719) — **Meta AI (2025)** — open-vocabulary concept prompts ("every striped shirt") instead of clicks and boxes.

## Articles / Blogs (free, no paywall)
- [COCO dataset](https://cocodataset.org/) — **COCO** — the standard instance-segmentation benchmark and annotation format.
- [Detectron2 docs](https://detectron2.readthedocs.io/en/latest/) — **Meta AI** — implementation reference and model zoo for Mask R-CNN.
- [Intersection over Union (IoU)](https://learnopencv.com/intersection-over-union-iou-in-object-detection-and-segmentation/) — **LearnOpenCV** — the overlap metric used to score masks, free.

## Books (free, with chapters)
- [Computer Vision: Algorithms and Applications, 2nd ed. — **Ch. 6.4 (Instance & semantic segmentation)**](https://szeliski.org/Book/) — **Richard Szeliski** — segmentation taxonomy and methods, free.
- [Dive into Deep Learning — **Ch. 14 (Computer Vision)**](https://d2l.ai/chapter_computer-vision/index.html) — **Zhang et al.** — detection/segmentation foundations Mask R-CNN builds on, with code.

## In this platform
- Foundation: [Object Detection](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/object-detection/object-detection) (Mask R-CNN extends Faster R-CNN) · [Semantic Segmentation](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/semantic-segmentation/semantic-segmentation)
- Where this went next: [Segment Anything & Promptable Segmentation (SAM · SAM 2 · SAM 3)](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/segment-anything-and-promptable-segmentation/segment-anything-and-promptable-segmentation)
- Metrics: [Detection & Segmentation Metrics (IoU · mAP)](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/detection-and-segmentation-metrics/detection-and-segmentation-metrics)
- Foundation: [Deep Learning › CNNs & Convolution](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/cnns-and-convolution/cnns-and-convolution)
