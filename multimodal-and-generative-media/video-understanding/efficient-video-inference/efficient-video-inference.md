---
id: "multimodal-and-generative-media/video-understanding/efficient-video-inference"
topic: "Efficient Video Inference"
level: advanced
built_from: ["long-video-understanding", "video-transformers-timesformer-vivit"]
leads_to: []
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Efficient Video Inference"
minutes: 15
category: video-understanding
---

# Efficient Video Inference
> Video inference is dominated by redundancy: neighbouring frames are nearly identical, yet a naive
> pipeline re-encodes every one of them at full resolution.
> The efficiency toolbox exploits that — **shift instead of convolve** in time (temporal shift
> module), **merge or prune tokens** that carry no new information, **reuse state** across time via a
> retained key-value (KV) cache or memory, and **schedule frames** adaptively so easy stretches cost
> little. In streaming settings you add the hard constraint that the answer must arrive before the
> next frame does.

**Why it matters:** it is the deployment half of every video system, and the constraint that decides
whether a model runs on a server, a phone, or a camera. Interviewers probe the cost model (frames ×
tokens-per-frame × layers, and which term you attacked), why token merging is nearly free while
naive frame skipping is not, what a streaming model must keep in memory between frames, and the
quality cliff: every one of these techniques is lossy, so the real question is what you measured
after applying it.

**Start here — suggested path:**

1. **Learn the cost model** — watch [EfficientML.ai Lecture 17 — GAN, Video, Point Cloud](https://www.youtube.com/watch?v=o_60Yhb79W8) — **MIT HAN Lab (Song Han)**. *Where video FLOPs and latency actually go, measured on real hardware.*
2. **See the cheapest architectural win** — [TSM: Temporal Shift Module](https://arxiv.org/abs/1811.08383) — **Lin, Gan & Han (2018)**. *Shift channels along time inside a 2D network: 3D-CNN accuracy at 2D-CNN cost, zero extra parameters.*
3. **Cut tokens, not layers** — [Token Merging](https://arxiv.org/abs/2210.09461) — **Bolya et al. (2022)** and [vid-TLDR](https://arxiv.org/abs/2403.13347) — **Choi et al. (2024)**. *Training-free merging of redundant tokens, then the video-specific version.*
4. **Cut visual tokens inside the language model** — [FastV](https://arxiv.org/abs/2403.06764) — **Chen et al. (2024)**. *Visual attention collapses after the first few layers, so most visual tokens can be dropped mid-stack.*
5. **Go streaming** — [VideoLLM-online](https://arxiv.org/abs/2406.11816) — **Chen et al. (2024)** and [LiveVLM](https://arxiv.org/abs/2505.15269) — **Ning et al. (2025)**. *Answering while the video is still playing, with a KV cache designed for it.*

## Courses (free)
- [MIT 6.5940 — TinyML and Efficient Deep Learning Computing](https://hanlab.mit.edu/courses/2024-fall-65940) — **Song Han (MIT)** — the definitive free course on pruning, quantization, and efficient video and long-context inference.
- [EfficientML.ai](https://efficientml.ai) — **MIT HAN Lab** — slides, labs, and lecture recordings for the same course, openly hosted.
- [CS231n 2025 Lecture 10 — Video Understanding (slides)](https://cs231n.stanford.edu/slides/2025/lecture_10.pdf) — **Ruohan Gao (Stanford)** — the architectures whose costs these techniques attack.

## Videos
- [EfficientML.ai Lecture 17 — GAN, Video, Point Cloud](https://www.youtube.com/watch?v=o_60Yhb79W8) — **MIT HAN Lab (Song Han)** — efficient video recognition from the group that invented the temporal shift module.
- [EfficientML.ai Lecture 15 — Long-Context LLM](https://www.youtube.com/watch?v=kgTWKjbnrBA) — **MIT HAN Lab (Song Han)** — KV-cache growth and long-context serving, the bottleneck for video-language models.

## Key Papers
- [TSM: Temporal Shift Module for Efficient Video Understanding](https://arxiv.org/abs/1811.08383) — **Lin, Gan & Han (2018)** — the classic zero-cost temporal operator; still the reference point for edge video.
- [X3D: Expanding Architectures for Efficient Video Recognition](https://arxiv.org/abs/2004.04730) — **Feichtenhofer (2020)** — expands one axis at a time to find the accuracy-per-FLOP frontier.
- [Token Merging: Your ViT But Faster](https://arxiv.org/abs/2210.09461) — **Bolya et al. (2022)** — training-free token reduction; the single most reusable trick in this list.
- [FastV](https://arxiv.org/abs/2403.06764) — **Chen et al. (2024)** — prunes visual tokens after early layers in a vision-language model with almost no quality loss.
- [MeMViT: Memory-Augmented Multiscale Vision Transformer](https://arxiv.org/abs/2201.08383) — **Wu et al. (2022)** — caches past activations so long-term context costs memory rather than compute.
- [QuickVideo: Real-Time Long Video Understanding with System Algorithm Co-Design](https://arxiv.org/abs/2505.16175) — **Schneider et al. (2025)** — parallel decoding, prefill overlap, and memory management; the systems view rather than the model view.
- [LiveVLM: Efficient Online Video Understanding via Streaming-Oriented KV Cache and Retrieval](https://arxiv.org/abs/2505.15269) — **Ning et al. (2025)** — a fixed-size streaming cache with retrieval instead of an ever-growing prompt.

## Articles / Blogs (free, no paywall)
- [TSM project page](https://hanlab.mit.edu/projects/tsm) — **MIT HAN Lab** — measured latency on Jetson and mobile hardware, plus the online-inference variant.
- [temporal-shift-module reference code](https://github.com/mit-han-lab/temporal-shift-module) — **MIT HAN Lab** — the shift operator in a few lines, including the online streaming version.
- [vLLM multimodal inputs](https://docs.vllm.ai/en/latest/features/multimodal_inputs.html) — **vLLM team** — how a production serving engine actually accepts video and budgets its cache.
- [PyTorchVideo](https://pytorchvideo.org/) — **Meta AI** — efficient decoding and clip sampling, where a surprising share of wall-clock time is lost.
- [Introducing agentic video understanding with Gemini](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/) — **Google** — a 2026 production answer: search the video with an agent instead of encoding all of it.

## Books (free, with chapters)
- [*Understanding Deep Learning* — Ch. 12 "Transformers"](https://udlbook.github.io/udlbook/) — **Simon Prince** — the attention cost model every token-reduction method exploits.
- [*Dive into Deep Learning* — Ch. 14 "Computer Vision"](https://d2l.ai/chapter_computer-vision/index.html) — **Zhang, Lipton, Li & Smola** — the convolutional cost baseline, with runnable code.

## In this platform
- Prerequisites: [Video Transformers — TimeSformer & ViViT](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/video-transformers-timesformer-vivit/video-transformers-timesformer-vivit) · [Long-Video Understanding](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/long-video-understanding/long-video-understanding)
- Related (canonical home): [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache) · [Inference Optimization](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization) · [Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization)
- Field overview: [Video Understanding](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/readme)
