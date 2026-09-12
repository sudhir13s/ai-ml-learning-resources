---
id: "multimodal-and-generative-media/video-understanding/video-language-models"
topic: "Video-Language Models"
level: advanced
built_from: ["self-supervised-video-pretraining-videomae", "video-transformers-timesformer-vivit"]
leads_to: ["multimodal-and-generative-media/video-understanding/long-video-understanding", "multimodal-and-generative-media/video-understanding/efficient-video-inference"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Video-Language Models"
minutes: 16
category: video-understanding
---

# Video-Language Models
> A video-language model is a large language model (LLM) that has been given eyes and a clock: a
> video encoder turns sampled frames into visual tokens, a **connector** (linear projection,
> multilayer perceptron, or resampler) maps them into the LLM's embedding space, and the LLM
> captions, answers questions, or chats about the footage.
> Everything hard about it is a **token budget** problem — one frame costs hundreds of tokens, so
> the real design question is which frames survive and how many tokens each one is allowed.

**Why it matters:** this is the dominant video interface of 2025–26 — Qwen2.5-VL, VideoLLaMA 3,
LLaVA-Video and Gemini all take video natively, and product questions ("summarize this meeting",
"find the defect") are now asked of one model instead of a pipeline. Interviewers probe the
connector choice and its token cost, why uniform frame sampling loses the one relevant second, how
temporal position is encoded (Qwen2.5-VL's absolute-time encoding versus plain frame indices), and
how you evaluate a system whose failures are fluent, plausible, and wrong.

**Start here — suggested path:**

1. **Get the vision-language foundation** — read [An Introduction to Vision-Language Modeling](https://arxiv.org/abs/2405.17247) — **Bordes et al. (2024, Meta FAIR)**. *Encoders, connectors, training stages, and evaluation — the vocabulary the video versions extend.*
2. **Build the connector yourself** — watch [Coding a Multimodal (Vision) Language Model from scratch](https://www.youtube.com/watch?v=vAmKB7iPkWw) — **Umar Jamil**. *Once you have written the projection layer, video is just more image tokens with an ordering.*
3. **Read the founding video systems** — [Video-ChatGPT](https://arxiv.org/abs/2306.05424) — **Maaz et al. (2023)** and [Video-LLaVA](https://arxiv.org/abs/2311.10122) — **Lin et al. (2023)**. *Instruction tuning on video, and aligning image and video into one visual space before projection.*
4. **See the 2025 frontier** — [Qwen2.5-VL](https://arxiv.org/abs/2502.13923) — **Bai et al. (2025)** and [VideoLLaMA 3](https://arxiv.org/abs/2501.13106) — **Zhang et al. (2025)**. *Dynamic frame rates, absolute-time position encoding, and second-level event grounding.*
5. **Learn what actually helps** — [Apollo: An Exploration of Video Understanding in Large Multimodal Models](https://arxiv.org/abs/2412.10360) — **Zohar et al. (2024)**, then check yourself on [Video-MME](https://video-mme.github.io/). *A systematic ablation of every design knob, then a benchmark that punishes appearance shortcuts.*

## Courses (free)
- [Community Computer Vision Course — Transformers in Video Processing](https://huggingface.co/learn/computer-vision-course/en/unit7/video-processing/transformers-based-models) — **Hugging Face** — free path from video transformers to video-language models, with code.
- [CS231n 2025 Lecture 10 — Video Understanding (slides)](https://cs231n.stanford.edu/slides/2025/lecture_10.pdf) — **Ruohan Gao (Stanford)** — the encoder half of the stack, taught properly before the LLM is bolted on.
- [Stanford CS25 — Transformers United](https://web.stanford.edu/class/cs25/) — **Stanford** — the seminar where multimodal and native-video architectures are presented by the people building them.

## Videos
- [Coding a Multimodal (Vision) Language Model from scratch in PyTorch](https://www.youtube.com/watch?v=vAmKB7iPkWw) — **Umar Jamil** — full implementation of encoder, projector, and LLM interface; the connector stops being magic.
- [Lecture 18: Videos](https://www.youtube.com/watch?v=A9D6NXBJdwU) — **Michigan Online (Justin Johnson)** — the video-encoder background these models assume.

## Key Papers
- [Flamingo: a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198) — **Alayrac et al. (2022, DeepMind)** — the perceiver resampler and gated cross-attention; the ancestor of every connector.
- [Video-ChatGPT](https://arxiv.org/abs/2306.05424) — **Maaz et al. (2023)** — video instruction tuning plus the first practical evaluation protocol for video conversation.
- [Video-LLaVA](https://arxiv.org/abs/2311.10122) — **Lin et al. (2023)** — aligns image and video representations *before* projection, so one LLM handles both.
- [LLaVA-Video: Video Instruction Tuning With Synthetic Data](https://arxiv.org/abs/2410.02713) — **Zhang et al. (2024)** — shows that data quality, not architecture, drove most 2024 gains.
- [Qwen2.5-VL Technical Report](https://arxiv.org/abs/2502.13923) — **Bai et al. (2025)** — dynamic frame-rate training and absolute-time encoding for hour-long video with second-level grounding.
- [Apollo: An Exploration of Video Understanding in Large Multimodal Models](https://arxiv.org/abs/2412.10360) — **Zohar et al. (2024)** — the ablation study that says which design choices actually matter.

## Articles / Blogs (free, no paywall)
- [Qwen2.5-VL release notes](https://qwenlm.github.io/blog/qwen2.5-vl/) — **Qwen team (Alibaba)** — the authors' own account of long-video handling and temporal grounding.
- [Video-text-to-text task guide](https://huggingface.co/docs/transformers/en/tasks/video_text_to_text) — **Hugging Face** — run a video-language model end to end, including frame sampling arguments.
- [Vision Language Models in 2025](https://huggingface.co/blog/vlms-2025) — **Hugging Face** — a current survey of open models, including the video-capable ones and their trade-offs.
- [Advancing the frontier of video understanding with Gemini 2.5](https://developers.googleblog.com/en/gemini-2-5-video-understanding/) — **Google** — a frontier lab's own description of native video input, timestamps, and long-context behaviour.
- [Video Understanding with Large Language Models: A Survey](https://arxiv.org/abs/2312.17432) — **Tang et al. (2023)** — the map of the whole design space, kept useful by its taxonomy.

## Books (free, with chapters)
- [*Multimodal Foundation Models: From Specialists to General-Purpose Assistants*](https://arxiv.org/abs/2309.10020) — **Li et al. (2023, Microsoft Research)** — a free book-length treatment of visual instruction tuning and multimodal assistants.
- [*Understanding Deep Learning* — Ch. 12 "Transformers"](https://udlbook.github.io/udlbook/) — **Simon Prince** — the attention and context-length mechanics that bound how much video fits.

## In this platform
- Prerequisites: [Self-Supervised Video Pretraining](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/self-supervised-video-pretraining-videomae/self-supervised-video-pretraining-videomae) · [Video Transformers — TimeSformer & ViViT](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/video-transformers-timesformer-vivit/video-transformers-timesformer-vivit)
- Related: [Multimodal Learning](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/multimodal-learning/readme) (the image-text fusion architectures this inherits) · [Video generation](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/readme) (the generative side, owned by Diffusion)
- Next: [Long-Video Understanding](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/long-video-understanding/long-video-understanding) · [Efficient Video Inference](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/efficient-video-inference/efficient-video-inference)
