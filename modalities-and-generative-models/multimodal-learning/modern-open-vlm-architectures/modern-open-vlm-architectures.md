---
id: "modalities-and-generative-models/multimodal-learning/modern-open-vlm-architectures"
topic: "Modern Open VLM Architectures"
level: advanced
built_from: ["visual-instruction-tuning-llava", "modern-dual-encoders-siglip-and-retrieval"]
leads_to: ["modalities-and-generative-models/multimodal-learning/document-and-chart-understanding", "modalities-and-generative-models/multimodal-learning/multimodal-benchmarks-and-evaluation", "modalities-and-generative-models/multimodal-learning/unified-token-spaces-and-any-to-any-models"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Modern Open VLM Architectures"
minutes: 15
category: multimodal-learning
---

# Modern Open VLM Architectures
> Between 2024 and 2026 open vision-language models (VLMs) converged on a recognizable shape:
> a **SigLIP-class encoder that keeps the image's native resolution and aspect ratio**, a small
> projector, a strong language model, and training data that makes optical character
> recognition (OCR) and **grounding** — pointing at a region, not just describing it — first-class
> abilities rather than emergent accidents. Qwen-VL, InternVL, PaliGemma, Molmo, Pixtral and
> Llama 3.2 Vision are variations on that theme.

**Why it matters:** this is the architecture you are asked to reason about when a team says "we
need a model that reads our screenshots, invoices and dashboards."

- **The three axes that actually differ:** how many visual tokens an image costs (fixed grid vs
  tiling vs native-resolution packing), whether the language model is frozen, and whether
  grounding and OCR data were in the mix.
- **What interviewers probe:** the resolution/token-budget trade-off. Doubling resolution
  quadruples visual tokens, which quadruples prefill cost and evicts context — so every modern
  design is a token-compression scheme in disguise.
- **The failure mode people get wrong:** benchmark scores hide *resolution cliffs*. A model that
  reads a 900-pixel-wide invoice perfectly can fail the same invoice at 1800 pixels because
  tiling split a table row across two tiles.

**Start here — suggested path:**

1. **See the 2026 landscape first** — read [Vision Language Models (Better, Faster, Stronger)](https://huggingface.co/blog/vlms-2025) — **Hugging Face**. *The state-of-the-field update: any-to-any models, reasoning VLMs, agentic use, small models, multimodal retrieval.*
2. **Study one model completely** — read [PaliGemma: A versatile 3B VLM for transfer](https://arxiv.org/abs/2407.07726) — **Beyer et al. (2024)**. *Small enough to hold in your head, and unusually explicit about every training decision.*
3. **Build it line by line** — watch [Coding a Multimodal (Vision) Language Model from scratch in PyTorch](https://www.youtube.com/watch?v=vAmKB7iPkWw) — **Umar Jamil**. *Five hours implementing PaliGemma: encoder, projector, merged token sequence, attention masks, cache.*
4. **Learn the resolution trick** — read [Patch n' Pack: NaViT, a Vision Transformer for any Aspect Ratio and Resolution](https://arxiv.org/abs/2307.06304) — **Dehghani et al. (2023)**. *The sequence-packing idea underneath "native resolution" in Qwen-VL and InternVL.*
5. **Check the current frontier** — read [Qwen3-VL Technical Report](https://arxiv.org/abs/2511.21631) — **Bai et al. (2025)** — and [InternVL3](https://arxiv.org/abs/2504.10479) — **Zhu et al. (2025)**. *Native 256K-token interleaved context, dense and mixture-of-experts variants, and the current training recipes.*

## Courses (free)

- [Stanford CME296: Diffusion and Large Vision Models](https://www.youtube.com/playlist?list=PLoROMvodv4rNdy8rt2rZ4T2xM0OjADnfu) — **Stanford Online** — full lecture series covering large vision models alongside diffusion; the university-level companion to this page.
- [Hugging Face Community Computer Vision Course — multimodal unit](https://huggingface.co/learn/computer-vision-course/en/unit4/multimodal-models/vlm-intro) — **Hugging Face** — free notebooks for loading, prompting and fine-tuning current open VLMs.

## Videos

- [Coding a Multimodal (Vision) Language Model from scratch in PyTorch](https://www.youtube.com/watch?v=vAmKB7iPkWw) — **Umar Jamil** — the whole PaliGemma stack implemented and explained; the best "I finally see it" resource here.
- [Vision in the Age of LLMs (ETH Zurich Robot Learning, 2026)](https://www.youtube.com/watch?v=0XB7fNS_ONg) — **Lucas Beyer (guest lecture, Oier Mees' course)** — PaliGemma's co-author on design choices that survived contact with 2026.

## Key Papers

- [PaliGemma: A versatile 3B VLM for transfer](https://arxiv.org/abs/2407.07726) — **Beyer et al. (2024)** — SigLIP encoder plus Gemma, with every pretraining and transfer decision ablated; the best model to learn the architecture from.
- [Qwen3-VL Technical Report](https://arxiv.org/abs/2511.21631) — **Bai et al. (2025)** — native 256K interleaved context, dense and mixture-of-experts variants, strong video and grounding; the 2026 open reference point.
- [InternVL3: Exploring Advanced Training and Test-Time Recipes for Open-Source Multimodal Models](https://arxiv.org/abs/2504.10479) — **Zhu et al. (2025)** — native multimodal pretraining rather than text-model retrofit, with the training recipe published.
- [Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Vision-Language Models](https://arxiv.org/abs/2409.17146) — **Deitke et al. (2024)** — fully open data, and the *pointing* supervision that made grounding a trainable skill.
- [Patch n' Pack: NaViT, a Vision Transformer for any Aspect Ratio and Resolution](https://arxiv.org/abs/2307.06304) — **Dehghani et al. (2023)** — variable-resolution sequence packing; the mechanism behind today's native-resolution encoders.
- [SmolVLM: Redefining small and efficient multimodal models](https://arxiv.org/abs/2504.05299) — **Marafioti et al. (2025)** — what you can drop and still see: token compression and resolution choices at 256M–2B parameters.

## Articles / Blogs (free, no paywall)

- [Vision Language Models (Better, Faster, Stronger)](https://huggingface.co/blog/vlms-2025) — **Hugging Face** — the 2025–26 update to the field: reasoning, agents, omni models, multimodal retrieval.
- [Qwen2.5-VL](https://qwenlm.github.io/blog/qwen2.5-vl/) — **Qwen Team, Alibaba** — the authors on dynamic resolution, absolute-time video encoding, and grounded output formats.
- [PaliGemma architecture explained](https://developers.googleblog.com/en/gemma-explained-paligemma-architecture/) — **Google** — a short, precise walkthrough of how the image tokens meet the language model.
- [Molmo blog](https://molmo.allenai.org/blog) — **Allen Institute for AI** — why open *data* (PixMo) mattered more than the architecture, and how pointing was collected.
- [Vision LLM notes](https://simonwillison.net/tags/vision-llms/) — **Simon Willison** — a practitioner's running log of what each new open VLM can actually do on real files.

## In this platform

- Prerequisites: [Visual Instruction Tuning (LLaVA)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/visual-instruction-tuning-llava/visual-instruction-tuning-llava) · [Modern Dual Encoders (SigLIP and retrieval)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/modern-dual-encoders-siglip-and-retrieval/modern-dual-encoders-siglip-and-retrieval) · [Vision Transformers](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/vision-transformers/vision-transformers)
- Next: [Document and Chart Understanding](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/document-and-chart-understanding/document-and-chart-understanding) · [Unified Token Spaces and Any-to-Any Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/unified-token-spaces-and-any-to-any-models/unified-token-spaces-and-any-to-any-models)
- Serving cost: [KV Cache](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/kv-cache/kv-cache) · [Inference Optimization](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/inference-optimization/inference-optimization) — visual tokens are prefill you pay for on every request
