---
id: "modalities-and-generative-models/video-understanding/temporal-localization-and-moment-retrieval"
topic: "Temporal Localization & Moment Retrieval"
level: advanced
built_from: ["action-recognition-and-video-classification"]
leads_to: ["video-language-models", "long-video-understanding"]
interview_frequency: low
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Temporal Localization & Moment Retrieval"
minutes: 14
category: video-understanding
---

# Temporal Localization & Moment Retrieval
> Real video is untrimmed, so the useful question is not "what action is this?" but **"when does it
> happen?"** — return start and end timestamps.
> **Temporal action localization** answers it from a fixed label set; **moment retrieval** answers it
> from a free-text query ("the moment she picks up the red mug"). Both are object detection with one
> spatial dimension replaced by time, and they inherit its whole toolbox: anchors or anchor-free
> regression, temporal intersection-over-union (tIoU), and non-maximum suppression.

**Why it matters:** it is the task behind video search, highlight generation, and every "jump to the
part where…" product, and it is where video-language models are still visibly weak. Interviewers
probe the metric (mean average precision averaged over tIoU thresholds — a boundary off by half a
second can zero out a detection), the fuzziness of ground-truth boundaries (annotators disagree by
seconds on when an action starts), and why long-tail moment lengths break fixed anchor designs.

**Start here — suggested path:**

1. **See the task next to classification** — watch [Lecture 18: Videos](https://www.youtube.com/watch?v=A9D6NXBJdwU) — **Michigan Online (Justin Johnson)**. *Temporal action localization and spatio-temporal detection framed as detection over time.*
2. **Read the language-query formulation** — [TALL: Temporal Activity Localization via Language Query](https://arxiv.org/abs/1705.02101) — **Gao et al. (2017)**. *The paper that defined moment retrieval and its sliding-window baseline.*
3. **Learn the two dominant designs** — [2D-TAN](https://arxiv.org/abs/1912.03590) — **Zhang et al. (2019)** and [ActionFormer](https://arxiv.org/abs/2202.07925) — **Zhang et al. (2022)**. *Enumerate candidate spans on a 2D map, versus regress boundaries anchor-free from a temporal feature pyramid.*
4. **Get the modern benchmark and detector** — [QVHighlights / Moment-DETR](https://arxiv.org/abs/2107.09609) — **Lei, Berg & Bansal (2021)** and [TriDet](https://arxiv.org/abs/2303.07347) — **Shi et al. (2023)**. *Joint moment retrieval and highlight detection; then relative boundary modeling that fixes blurry edges.*
5. **See the unified 2023–25 view** — [UniVTG](https://arxiv.org/abs/2307.16715) — **Lin et al. (2023)**, then run the [ActionFormer code](https://github.com/happyharrycn/actionformer_release). *One model for grounding, highlight detection, and summarization — and a training loop you can actually reproduce.*

## Courses (free)
- [CS231n 2025 Lecture 10 — Video Understanding (slides)](https://cs231n.stanford.edu/slides/2025/lecture_10.pdf) — **Ruohan Gao (Stanford)** — puts localization in context with classification and detection.
- [Community Computer Vision Course — Unit 7: Video Processing](https://huggingface.co/learn/computer-vision-course/en/unit7/video-processing/introduction-to-video) — **Hugging Face** — free grounding in the feature extraction every localization model consumes.

## Videos
- [Lecture 18: Videos](https://www.youtube.com/watch?v=A9D6NXBJdwU) — **Michigan Online (Justin Johnson)** — the only free lecture that treats temporal localization as a first-class task rather than a footnote.

## Key Papers
- [TALL: Temporal Activity Localization via Language Query](https://arxiv.org/abs/1705.02101) — **Gao et al. (2017)** — defines moment retrieval; the cross-modal alignment baseline everything improved on.
- [Learning 2D Temporal Adjacent Networks (2D-TAN)](https://arxiv.org/abs/1912.03590) — **Zhang et al. (2019)** — represents every candidate span on a 2D start-end map; the clearest proposal-based design.
- [ActionFormer: Localizing Moments of Actions with Transformers](https://arxiv.org/abs/2202.07925) — **Zhang, Wu & Li (2022)** — anchor-free transformer detector; the standard strong baseline.
- [QVHighlights (Moment-DETR)](https://arxiv.org/abs/2107.09609) — **Lei, Berg & Bansal (2021)** — the dataset and end-to-end detector that joined moment retrieval with highlight detection.
- [TriDet: Temporal Action Detection with Relative Boundary Modeling](https://arxiv.org/abs/2303.07347) — **Shi et al. (2023)** — handles imprecise boundaries head-on, the field's most persistent failure mode.
- [UniVTG: Towards Unified Video-Language Temporal Grounding](https://arxiv.org/abs/2307.16715) — **Lin et al. (2023)** — one pretrained model across grounding tasks; the bridge to video-language systems.

## Articles / Blogs (free, no paywall)
- [ActionFormer reference implementation](https://github.com/happyharrycn/actionformer_release) — **Zhang et al.** — training, inference, and evaluation code for temporal action localization, maintained by the authors.
- [Moment-DETR reference implementation](https://github.com/jayleicn/moment_detr) — **Jie Lei** — the QVHighlights baseline with data preparation scripts, the fastest way to reproduce the metric.
- [ActivityNet](http://activity-net.org/) — **ActivityNet team** — the long-running untrimmed-video benchmark and its evaluation protocol.
- [Charades](https://prior.allenai.org/projects/charades) — **Allen Institute for AI** — everyday untrimmed activity video with temporal annotations, freely available.

## Books (free, with chapters)
- [*Computer Vision: Algorithms and Applications*, 2nd ed. — Ch. 9 "Motion estimation"](https://szeliski.org/Book/) — **Richard Szeliski** — temporal structure in video before any learned detector.
- [*Foundations of Computer Vision* — Part XIII "Object Recognition"](https://visionbook.mit.edu) — **Torralba, Isola & Freeman** — detection framing that maps one-to-one onto the time axis, free online.

## In this platform
- Prerequisite: [Action Recognition & Video Classification](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/action-recognition-and-video-classification/action-recognition-and-video-classification)
- Related: [Object Detection](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/object-detection/object-detection) (anchors, tIoU, and non-maximum suppression in space) · [Detection & Segmentation Metrics](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/detection-and-segmentation-metrics/detection-and-segmentation-metrics)
- Next: [Video-Language Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/video-language-models/video-language-models) · [Long-Video Understanding](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/long-video-understanding/long-video-understanding)
