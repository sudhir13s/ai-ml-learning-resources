---
id: "modalities-and-generative-models/video-understanding/long-video-understanding"
topic: "Long-Video Understanding"
level: advanced
built_from: ["video-language-models", "temporal-localization-and-moment-retrieval"]
leads_to: ["modalities-and-generative-models/video-understanding/efficient-video-inference"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Long-Video Understanding"
minutes: 16
category: video-understanding
---

# Long-Video Understanding
> One hour of video at 1 frame per second is 3,600 frames; at a few hundred visual tokens per frame
> that is a million-token prompt before anyone says a word.
> Long-video understanding is the set of tricks for spending a fixed token budget well — **select**
> the frames that matter (keyframe selection, temporal search), **compress** the ones you keep
> (pooling, token merging, resamplers), or **remember** instead of re-reading (memory banks, a
> retained key-value cache) — plus the long-context machinery that lets the LLM hold what survives.

**Why it matters:** it is the difference between a demo on a 30-second clip and a product that
answers questions about a two-hour recording, and it is where 2025–26 systems still fail. The
interview question is always the arithmetic: frames × tokens-per-frame against the context window
and the attention cost, then which of selection, compression, or memory you would reach for and
what each one loses. The honest answer includes the failure mode — uniform sampling drops the single
relevant second, and aggressive compression makes the model confidently describe a scene it never saw.

**Start here — suggested path:**

1. **Do the token arithmetic** — read [Gemini 1.5](https://arxiv.org/abs/2403.05530) — **Gemini Team (2024)**. *The report that made million-token multimodal context real, with the video needle-in-a-haystack results.*
2. **See the selection lever** — [Adaptive Keyframe Sampling](https://arxiv.org/abs/2502.21271) — **Tang et al. (CVPR 2025)**. *Keyframe choice as an explicit optimization of prompt relevance against video coverage.*
3. **See the memory lever** — [MovieChat](https://arxiv.org/abs/2307.16449) — **Song et al. (2023)** and [MA-LMM](https://arxiv.org/abs/2404.05726) — **He et al. (2024)**. *Short-term and long-term memory banks instead of one enormous prompt.*
4. **See the context lever** — [LongVA](https://arxiv.org/abs/2406.16852) — **Zhang et al. (2024)** and [LongVILA](https://arxiv.org/abs/2408.10188) — **Chen et al. (2024)**. *Extend the language model's context, then let the extra length transfer to vision.*
5. **Measure honestly, then read the 2025 state of the art** — [LongVideoBench](https://longvideobench.github.io/) and [Video-MME](https://video-mme.github.io/), then [T\*: Re-thinking Temporal Search for Long-Form Video Understanding](https://arxiv.org/abs/2504.02259) — **Ye et al. (2025)**. *Benchmarks that cannot be passed by sampling eight frames, then search as the alternative to brute force.*

## Courses (free)
- [MIT 6.5940 — TinyML and Efficient Deep Learning Computing](https://hanlab.mit.edu/courses/2024-fall-65940) — **Song Han (MIT)** — free lectures and slides on long-context and memory-bound inference, which is exactly this problem.
- [CS231n 2025 Lecture 10 — Video Understanding (slides)](https://cs231n.stanford.edu/slides/2025/lecture_10.pdf) — **Ruohan Gao (Stanford)** — the encoder side, before token budgets dominate the design.
- [Community Computer Vision Course — Unit 7: Video Processing](https://huggingface.co/learn/computer-vision-course/en/unit7/video-processing/introduction-to-video) — **Hugging Face** — sampling and decoding fundamentals that decide how many tokens you even create.

## Videos
- [EfficientML.ai Lecture 15 — Long-Context LLM](https://www.youtube.com/watch?v=kgTWKjbnrBA) — **MIT HAN Lab (Song Han)** — where long-context memory and compute actually go; the numbers behind the arithmetic above.
- [Memory-Augmented Large Multimodal Model for Long-Term Video Understanding (CVPR 2024 talk page)](https://cvpr.thecvf.com/virtual/2024/poster/30043) — **Bo He et al.** — the MA-LMM authors on memory banks for hour-scale video.

## Key Papers
- [Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context](https://arxiv.org/abs/2403.05530) — **Gemini Team (2024, Google DeepMind)** — the primary source for long-context multimodal recall, including video.
- [MovieChat: From Dense Token to Sparse Memory for Long Video Understanding](https://arxiv.org/abs/2307.16449) — **Song et al. (2023)** — short- and long-term memory banks; the cleanest statement of the memory approach.
- [MA-LMM: Memory-Augmented Large Multimodal Model](https://arxiv.org/abs/2404.05726) — **He et al. (2024)** — online processing with a compressed memory rather than a growing prompt.
- [Long Context Transfer from Language to Vision (LongVA)](https://arxiv.org/abs/2406.16852) — **Zhang et al. (2024)** — extend the LLM's context and the vision side inherits it without video-specific long training.
- [Adaptive Keyframe Sampling for Long Video Understanding](https://arxiv.org/abs/2502.21271) — **Tang et al. (2025)** — keyframe selection as relevance-versus-coverage optimization; plug-and-play and reproducible.
- [Video-XL: Extra-Long Vision Language Model for Hour-Scale Video Understanding](https://arxiv.org/abs/2409.14485) — **Shu et al. (2024)** — visual context compression for hour-scale input on a single accelerator.
- [T\*: Re-thinking Temporal Search for Long-Form Video Understanding](https://arxiv.org/abs/2504.02259) — **Ye et al. (2025)** — treats finding the relevant moment as spatial-temporal search instead of uniform sampling.

## Articles / Blogs (free, no paywall)
- [Advancing the frontier of video understanding with Gemini 2.5](https://developers.googleblog.com/en/gemini-2-5-video-understanding/) — **Google** — how a frontier long-context model handles hour-scale video, from the team that built it.
- [Introducing agentic video understanding with Gemini](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/) — **Google** — the 2026 shift from "put every frame in the prompt" to an agent that searches the video, at a fraction of the tokens.
- [Video-MME benchmark](https://video-mme.github.io/) — **Fu et al.** — short, medium, and long splits with subtitles and audio; the standard scoreboard.
- [LongVideoBench](https://longvideobench.github.io/) — **Wu et al.** — referring-reasoning questions designed so that sparse frame sampling cannot pass.
- [Adaptive Keyframe Sampling reference code](https://github.com/ncTimTang/AKS) — **Tang et al.** — the selection algorithm as a drop-in module you can read in an afternoon.

## Books (free, with chapters)
- [*Multimodal Foundation Models: From Specialists to General-Purpose Assistants*](https://arxiv.org/abs/2309.10020) — **Li et al. (2023)** — free book-length background on the multimodal assistants this pushes to hour scale.
- [*Understanding Deep Learning* — Ch. 12 "Transformers"](https://udlbook.github.io/udlbook/) — **Simon Prince** — why context length costs what it does, derived rather than asserted.

## In this platform
- Prerequisites: [Video-Language Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/video-language-models/video-language-models) · [Temporal Localization & Moment Retrieval](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/temporal-localization-and-moment-retrieval/temporal-localization-and-moment-retrieval) (finding the moment is the selection problem)
- Related (canonical home): [Long-Context Architectures](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/long-context-architectures/long-context-architectures) · [KV Cache](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/kv-cache/kv-cache) (the memory this competes for)
- Next: [Efficient Video Inference](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/efficient-video-inference/efficient-video-inference)
