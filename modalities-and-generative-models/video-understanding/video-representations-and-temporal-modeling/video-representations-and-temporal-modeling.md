---
id: "modalities-and-generative-models/video-understanding/video-representations-and-temporal-modeling"
topic: "Video Representations & Temporal Modeling"
level: intermediate
built_from: ["classic-cnn-architectures", "optical-flow-and-video"]
leads_to: ["modalities-and-generative-models/video-understanding/video-transformers-timesformer-vivit", "modalities-and-generative-models/video-understanding/action-recognition-and-video-classification"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Video Representations & Temporal Modeling"
minutes: 14
category: video-understanding
---

# Video Representations & Temporal Modeling
> A video is not a bag of images — the same frames in a different order mean a different thing.
> **Temporal modeling** is the set of design choices that encode that order: which frames you
> sample, and where you fuse time (late fusion of per-frame features, 3D convolution, a separate
> motion stream, or two pathways running at different frame rates).
> Get these wrong and a "video model" quietly degrades into an image classifier with extra cost.

**Why it matters:** every video system starts with frames-per-clip, stride, and fusion point, and
those three numbers set both accuracy and compute. Interviewers probe why a 3D kernel multiplies
parameters and floating-point operations (FLOPs) by its temporal extent, why **two-stream** needed
precomputed optical flow while **I3D** could inflate ImageNet weights instead, and why **SlowFast**
decouples frame rate from channel width rather than paying full price for both.

**Start here — suggested path:**

1. **See the whole design space** — watch [Lecture 18: Videos](https://www.youtube.com/watch?v=A9D6NXBJdwU) — **Michigan Online (Justin Johnson)**. *Single-frame → late fusion → early fusion → 3D convolutional network (CNN) → two-stream, derived in one sitting.*
2. **Get the current academic framing** — read [CS231n 2025 Lecture 10: Video Understanding](https://cs231n.stanford.edu/slides/2025/lecture_10.pdf) — **Ruohan Gao (Stanford)**. *The 2025 version of the same map, ending at video transformers.*
3. **Read the two founding designs** — [Two-Stream Networks](https://arxiv.org/abs/1406.2199) then [C3D](https://arxiv.org/abs/1412.0767) — **Simonyan & Zisserman (2014)** · **Tran et al. (2014)**. *Explicit motion versus learned spatiotemporal filters — the split the field still argues about.*
4. **See how the field got cheap and accurate** — [I3D](https://arxiv.org/abs/1705.07750) → [TSN](https://arxiv.org/abs/1608.00859) → [SlowFast](https://arxiv.org/abs/1812.03982). *Inflate 2D weights, sample sparsely, then split appearance from motion by frame rate instead of by input.*
5. **Make it concrete** — load a pretrained clip model from [torchvision video models](https://pytorch.org/vision/main/models/video_resnet.html) and step through the tensor shapes. *Watching `[B, C, T, H, W]` flow through a 3D stem is what makes "temporal receptive field" stop being an abstraction.*

## Courses (free)
- [Stanford CS231n — Deep Learning for Computer Vision](https://cs231n.stanford.edu/) — **Stanford** — the reference course; free notes and assignments, video understanding included in the modern syllabus.
- [CS231n 2025 Lecture 10 — Video Understanding (slides)](https://cs231n.stanford.edu/slides/2025/lecture_10.pdf) — **Ruohan Gao (Stanford)** — the single best free overview of temporal architectures, current to 2025.
- [Community Computer Vision Course — Unit 7: Video Processing Basics](https://huggingface.co/learn/computer-vision-course/en/unit7/video-processing/video-processing-basics) — **Hugging Face** — frames, frame rate, and temporal redundancy before any modeling.

## Videos
- [Lecture 18: Videos](https://www.youtube.com/watch?v=A9D6NXBJdwU) — **Michigan Online (Justin Johnson)** — derives every fusion strategy from first principles; the clearest lecture on this topic anywhere.
- [EfficientML.ai Lecture 17 — GAN, Video, Point Cloud](https://www.youtube.com/watch?v=o_60Yhb79W8) — **MIT HAN Lab (Song Han)** — what temporal modeling costs in FLOPs and latency, from the group that built the temporal shift module.

## Key Papers
- [Two-Stream Convolutional Networks for Action Recognition](https://arxiv.org/abs/1406.2199) — **Simonyan & Zisserman (2014)** — appearance and stacked optical flow as separate streams; the motion baseline everything is measured against.
- [Learning Spatiotemporal Features with 3D Convolutional Networks (C3D)](https://arxiv.org/abs/1412.0767) — **Tran et al. (2014)** — the first widely used 3D CNN and the cost argument against it.
- [Quo Vadis, Action Recognition? (I3D)](https://arxiv.org/abs/1705.07750) — **Carreira & Zisserman (2017)** — inflate a pretrained 2D network into 3D; the trick that made video models trainable.
- [Temporal Segment Networks](https://arxiv.org/abs/1608.00859) — **Wang et al. (2016)** — sparse segment sampling: you do not need every frame, you need coverage.
- [SlowFast Networks for Video Recognition](https://arxiv.org/abs/1812.03982) — **Feichtenhofer et al. (2018)** — two pathways at different frame rates; the cleanest statement of the appearance/motion trade-off.

## Articles / Blogs (free, no paywall)
- [PyTorchVideo](https://pytorchvideo.org/) — **Meta AI** — the reference library for clip sampling, decoding, and pretrained video backbones, with the data pipeline spelled out.
- [torchvision video classification models](https://pytorch.org/vision/main/models/video_resnet.html) — **PyTorch** — runnable R3D / R(2+1)D / MC3 checkpoints with their exact input shapes.
- [Video classification task guide](https://huggingface.co/docs/transformers/tasks/video_classification) — **Hugging Face** — frame sampling and preprocessing decisions shown in code.
- [CVPR 2019 Tutorial on Action Recognition](https://feichtenhofer.github.io/cvpr2019-recognition-tutorial/) — **Feichtenhofer, Wang, Xie et al.** — slides from the authors of I3D, TSN, and SlowFast in one place.

## Books (free, with chapters)
- [*Foundations of Computer Vision* — Part XII "Motion"](https://visionbook.mit.edu) — **Torralba, Isola & Freeman** — motion estimation and temporal filters, free to read online.
- [*Computer Vision: Algorithms and Applications*, 2nd ed. — Ch. 9 "Motion estimation"](https://szeliski.org/Book/) — **Richard Szeliski** — the classical account of what a temporal model is approximating.

## In this platform
- Prerequisites: [Classic CNN Architectures](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/classic-cnn-architectures/classic-cnn-architectures) · [Optical Flow & Video](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/optical-flow-and-video/optical-flow-and-video) (the motion field the two-stream design consumes)
- Next: [Video Transformers — TimeSformer & ViViT](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/video-transformers-timesformer-vivit/video-transformers-timesformer-vivit) · [Action Recognition & Video Classification](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/action-recognition-and-video-classification/action-recognition-and-video-classification)
- Related: [Efficient Video Inference](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/efficient-video-inference/efficient-video-inference) (what these architectures cost at serving time) · [Computer Vision](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/readme)
