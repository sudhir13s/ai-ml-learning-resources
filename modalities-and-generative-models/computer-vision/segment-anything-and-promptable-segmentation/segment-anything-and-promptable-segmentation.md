---
id: "modalities-and-generative-models/computer-vision/segment-anything-and-promptable-segmentation"
topic: "Segment Anything and Promptable Segmentation"
level: intermediate
built_from: ["semantic-segmentation", "instance-segmentation", "vision-transformers"]
leads_to: ["07-computer-vision/detection-and-segmentation-metrics", "07-computer-vision/optical-flow-and-video"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Segment Anything and Promptable Segmentation"
minutes: 16
category: computer-vision
---

# Segment Anything and Promptable Segmentation
> **Segment Anything (SAM)** turned segmentation into a *promptable* task: give the model a click, a
> box, a rough mask — and in SAM 3, a noun phrase — and it returns the mask, without ever having
> been trained on that object class. A heavy image encoder runs once; a tiny decoder answers each
> prompt in milliseconds. The one sentence: **a segmentation foundation model separates "look at the
> image" from "answer this prompt", so one model serves every downstream task.**

**Why it matters:** in 2026 most segmentation pipelines start from SAM masks plus a labeller rather
than a per-dataset mask head, and the lineage now runs SAM (images, 2023) → SAM 2 (streaming video
memory, 2024) → SAM 3 (open-vocabulary concept prompts, 2025). Interviewers probe three things: how
**ambiguity** is handled (the model returns several masks with predicted quality scores rather than
guessing), what the **data engine** actually is (model-assisted annotation feeding back into
training — 1.1 billion masks for SAM 1, over 4 million unique concepts for SAM 3), and the limit
people underrate: **SAM 1 and SAM 2 give you masks with no semantics**, so "which object is this?"
remains your problem.

**Start here — suggested path:**

1. **Read the founding paper** — read [Segment Anything](https://arxiv.org/abs/2304.02643) — **Kirillov, Mintun, Ravi et al. (Meta AI, 2023)**. *The promptable task, the encoder-prompt-decoder split, and the data engine, in one argument.*
2. **Run it on your own images** — work through [segment-anything](https://github.com/facebookresearch/segment-anything) — **Meta AI (FAIR)**. *Notebooks for point, box, and automatic mask generation; the ambiguity heads become visible immediately.*
3. **Add the time axis** — read [SAM 2: Segment Anything in Images and Videos](https://arxiv.org/abs/2408.00714) — **Ravi, Gabeur, Hu et al. (Meta AI, 2024)**. *A streaming memory bank carries a mask across frames, so one prompt tracks an object through a video.*
4. **See the 2025 jump** — watch [Introducing Meta Segment Anything Model 3](https://www.youtube.com/watch?v=G4OLPDjwncw) — **AI at Meta**. *Concept prompts: "every striped shirt" instead of a click per instance.*
5. **Read SAM 3 properly** — read [SAM 3: Segment Anything with Concepts](https://arxiv.org/abs/2511.16719) — **Carion et al. (Meta, 2025)**. *Promptable concept segmentation, the presence head that separates recognition from localization, and the decoupled detector-tracker.*

## Courses (free)
- [Stanford CS231n: Deep Learning for Computer Vision](https://cs231n.github.io/) — **Stanford** — free notes; the detection and segmentation unit is the background this page assumes.
- [Hugging Face Computer Vision Course](https://huggingface.co/learn/computer-vision-course) — **Hugging Face community** — free, with a segmentation chapter and runnable SAM inference.

## Videos
- [Introducing Meta Segment Anything Model 3 (SAM 3)](https://www.youtube.com/watch?v=G4OLPDjwncw) — **AI at Meta** — the authors' own presentation of unified detection, segmentation, and tracking.
- [Lecture 16: Detection and Segmentation](https://www.youtube.com/watch?v=9AyMR4IhSWQ) — **Michigan Online (Justin Johnson)** — the pre-foundation-model landscape SAM replaced; watch this first if "panoptic" is still fuzzy.

## Key Papers
- [Segment Anything](https://arxiv.org/abs/2304.02643) — **Kirillov et al. (2023)** — the promptable segmentation task, the SA-1B dataset of over 1 billion masks, and zero-shot transfer results.
- [SAM 2: Segment Anything in Images and Videos](https://arxiv.org/abs/2408.00714) — **Ravi et al. (2024)** — memory attention over past frames turns segmentation into tracking, in real time.
- [SAM 3: Segment Anything with Concepts](https://arxiv.org/abs/2511.16719) — **Carion et al. (2025)** — open-vocabulary concept prompts, a 4-million-concept data engine, and roughly double the accuracy of previous systems on the new benchmark.
- [Segment Anything in Medical Images](https://arxiv.org/abs/2304.12306) — **Ma, He, Li, Han, You & Wang (2024)** — MedSAM: what fine-tuning a promptable model on 1.5 million medical image-mask pairs buys, and where it still fails.
- [The Segment Anything Model (SAM) for Remote Sensing Applications: From Zero to One Shot](https://arxiv.org/abs/2306.16623) — **Osco, Wu, de Lemos et al. (2023)** — the first careful evaluation on satellite and aerial imagery; scale and modality shift are the hard part.
- [Segment Anything Is Not Always Perfect: An Investigation of SAM on Different Real-world Applications](https://arxiv.org/abs/2304.05750) — **Ji, Li, Bi, Liu, Li & Cheng (2023)** — the failure catalogue: camouflage, low contrast, thin structures, and fine boundaries.
- [On Efficient Variants of Segment Anything Model: A Survey](https://arxiv.org/abs/2410.04960) — **Sun, Liu, Shen, Zhu & Hu (2024)** — distilled and re-architected SAMs for edge deployment, compared on the same axes.

## Articles / Blogs (free, no paywall)
- [segment-anything](https://github.com/facebookresearch/segment-anything) — **Meta AI (FAIR)** — model, checkpoints, and the automatic mask generator; the reference implementation.
- [sam2](https://github.com/facebookresearch/sam2) — **Meta AI (FAIR)** — video predictor and the SA-V dataset tooling, with notebooks for interactive tracking.
- [sam3](https://github.com/facebookresearch/sam3) — **Meta Superintelligence Labs** — inference and fine-tuning code, checkpoints, and examples for concept prompting.
- [Segment anything in medical images](https://www.nature.com/articles/s41467-024-44824-z) — **Ma et al., *Nature Communications* (2024)** — the open-access MedSAM paper; read the failure analysis before trusting any clinical claim.
- [segment-geospatial](https://samgeo.gishub.org/) — **Qiusheng Wu (University of Tennessee)** — SAM wired into geospatial workflows; documented, installable, and the fastest route to a real remote-sensing experiment.

## Books (free, with chapters)
- [*Computer Vision: Algorithms and Applications*, 2nd ed. — Ch. 6.4 "Semantic and instance segmentation"](https://szeliski.org/Book/) — **Richard Szeliski** — free; the segmentation taxonomy SAM sits on top of.
- [*Dive into Deep Learning* — Ch. 14 "Computer Vision"](https://d2l.ai/chapter_computer-vision/index.html) — **Zhang, Lipton, Li & Smola** — free, runnable; detection and dense prediction foundations with code.

## In this platform
- Foundation: [Semantic Segmentation (FCN, U-Net, DeepLab)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/semantic-segmentation/semantic-segmentation) · [Instance Segmentation (Mask R-CNN)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/instance-segmentation/instance-segmentation) · [Object Detection](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/object-detection/object-detection)
- The backbone and pretraining it relies on: [Vision Transformers](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/vision-transformers/vision-transformers) · [Self-Supervised Vision](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/self-supervised-vision/self-supervised-vision)
- How masks are scored: [Detection and Segmentation Metrics (IoU, mAP)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/detection-and-segmentation-metrics/detection-and-segmentation-metrics)
- Where video comes in: [Optical Flow and Video Understanding](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/optical-flow-and-video/optical-flow-and-video) · [Video Understanding](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/readme)
- Adjacent: [3D and Depth Estimation](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/3d-and-depth-estimation/3d-and-depth-estimation)
