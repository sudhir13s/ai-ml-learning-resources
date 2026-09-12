---
id: "multimodal-and-generative-media/video-understanding/action-recognition-and-video-classification"
topic: "Action Recognition & Video Classification"
level: intermediate
built_from: ["video-representations-and-temporal-modeling", "self-supervised-video-pretraining-videomae"]
leads_to: ["multimodal-and-generative-media/video-understanding/temporal-localization-and-moment-retrieval", "multimodal-and-generative-media/video-understanding/efficient-video-inference"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Action Recognition & Video Classification"
minutes: 14
category: video-understanding
---

# Action Recognition & Video Classification
> Given a trimmed clip, name the action. It is the ImageNet-style task of video — and the benchmark
> on which every backbone is compared — but the evaluation protocol carries more weight than usual:
> a clip model is trained on a few seconds and tested by **averaging predictions over multiple
> crops and temporal views**, so the same weights can report very different numbers.
> The other trap is the dataset: some benchmarks are solvable from a single frame, and some are not.

**Why it matters:** it is where "does your model actually use time?" gets answered. Kinetics-400 is
largely **appearance-driven** (scene and objects give away the label), while Something-Something v2
is deliberately **motion-driven** ("moving something up" versus "moving something down" share every
object), so a model that looks strong on one can collapse on the other. Interviewers probe exactly
that gap, plus multi-view test-time aggregation, class imbalance in long-tail action sets, and the
difference between clip-level and video-level accuracy.

**Start here — suggested path:**

1. **See the task and its baselines** — watch [Lecture 18: Videos](https://www.youtube.com/watch?v=A9D6NXBJdwU) — **Michigan Online (Justin Johnson)**. *Classification framing, clip sampling, and the standard architectures compared.*
2. **Know the two datasets that define the field** — [Kinetics](https://arxiv.org/abs/1705.06950) — **Kay et al. (2017)** and [Something-Something](https://arxiv.org/abs/1706.04261) — **Goyal et al. (2017)**. *Appearance-solvable versus motion-required; pick a benchmark that tests what you claim.*
3. **Read the strongest supervised designs** — [SlowFast](https://arxiv.org/abs/1812.03982) and [Non-local Neural Networks](https://arxiv.org/abs/1711.07971). *Two frame rates, then long-range dependencies inside the backbone.*
4. **Use a pretrained backbone properly** — [VideoMAE](https://arxiv.org/abs/2203.12602) is the standard initialization; fine-tune it with the [video classification task guide](https://huggingface.co/docs/transformers/tasks/video_classification) — **Hugging Face**. *Sampling, normalization, and the head, end to end.*
5. **Read the evaluation fine print** — [UniFormerV2](https://arxiv.org/abs/2211.09552) — **Li et al. (2022)**. *Reports the multi-view protocol explicitly, which is how you learn to compare published numbers honestly.*

## Courses (free)
- [CS231n 2025 Lecture 10 — Video Understanding (slides)](https://cs231n.stanford.edu/slides/2025/lecture_10.pdf) — **Ruohan Gao (Stanford)** — the task, the datasets, and the architecture ladder in one lecture.
- [Community Computer Vision Course — Unit 7: Video Processing](https://huggingface.co/learn/computer-vision-course/en/unit7/video-processing/introduction-to-video) — **Hugging Face** — free, code-first path from decoding frames to a trained classifier.
- [CVPR 2019 Tutorial on Action Recognition](https://feichtenhofer.github.io/cvpr2019-recognition-tutorial/) — **Feichtenhofer, Wang, Xie et al.** — full slide decks from the people who built I3D, TSN, and SlowFast.

## Videos
- [Lecture 18: Videos](https://www.youtube.com/watch?v=A9D6NXBJdwU) — **Michigan Online (Justin Johnson)** — the clearest free lecture on video classification and its baselines.
- [EfficientML.ai Lecture 17 — GAN, Video, Point Cloud](https://www.youtube.com/watch?v=o_60Yhb79W8) — **MIT HAN Lab (Song Han)** — accuracy-per-FLOP for action recognition backbones, measured rather than asserted.

## Key Papers
- [The Kinetics Human Action Video Dataset](https://arxiv.org/abs/1705.06950) — **Kay et al. (2017)** — the benchmark that made video pretraining possible, and its appearance bias.
- [The "Something Something" Video Database](https://arxiv.org/abs/1706.04261) — **Goyal et al. (2017)** — labels that cannot be guessed from one frame; the motion test.
- [SlowFast Networks for Video Recognition](https://arxiv.org/abs/1812.03982) — **Feichtenhofer et al. (2018)** — the strongest convolutional recipe and a clean ablation of frame rate.
- [Non-local Neural Networks](https://arxiv.org/abs/1711.07971) — **Wang et al. (2017)** — self-attention inside a video CNN, years before video transformers.
- [AVA: Spatio-temporally Localized Atomic Visual Actions](https://arxiv.org/abs/1705.08421) — **Gu et al. (2017)** — per-person action labels; where classification stops being enough.
- [UniFormerV2](https://arxiv.org/abs/2211.09552) — **Li et al. (2022)** — arms pretrained image ViTs with temporal modules; strong on both appearance and motion benchmarks.

## Articles / Blogs (free, no paywall)
- [Video classification task guide](https://huggingface.co/docs/transformers/tasks/video_classification) — **Hugging Face** — fine-tune VideoMAE on a small dataset with every preprocessing choice shown.
- [PyTorchVideo](https://pytorchvideo.org/) — **Meta AI** — reference clip sampling and evaluation protocols, the part most reimplementations get wrong.
- [facebookresearch/SlowFast (PySlowFast)](https://github.com/facebookresearch/SlowFast) — **Meta AI** — the original training and multi-view testing code for SlowFast, I3D, and MViT.
- [FineVideo dataset](https://huggingface.co/datasets/HuggingFaceFV/finevideo) — **Hugging Face** — an openly licensed, richly annotated video set for practising the whole pipeline.

## Books (free, with chapters)
- [*Foundations of Computer Vision* — Part XIII "Object Recognition"](https://visionbook.mit.edu) — **Torralba, Isola & Freeman** — recognition framing that transfers directly to clip labelling, free online.
- [*Dive into Deep Learning* — Ch. 14 "Computer Vision"](https://d2l.ai/chapter_computer-vision/index.html) — **Zhang, Lipton, Li & Smola** — the fine-tuning and augmentation machinery, with runnable code.

## In this platform
- Prerequisites: [Video Representations & Temporal Modeling](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/video-representations-and-temporal-modeling/video-representations-and-temporal-modeling) · [Self-Supervised Video Pretraining](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/self-supervised-video-pretraining-videomae/self-supervised-video-pretraining-videomae)
- Related: [Image Classification](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/image-classification/image-classification) (the single-frame case) · [Transfer Learning for Vision](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/transfer-learning-for-vision/transfer-learning-for-vision)
- Next: [Temporal Localization & Moment Retrieval](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/temporal-localization-and-moment-retrieval/temporal-localization-and-moment-retrieval) (when the clip is not trimmed for you)
