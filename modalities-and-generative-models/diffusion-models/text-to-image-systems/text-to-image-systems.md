---
id: "10-generative-ai/text-to-image"
topic: "Text-to-Image Systems"
parent: "10-generative-ai"
level: advanced
built_from: ["diffusion-ddpm", "latent-diffusion", "conditional-cfg", "clip", "transformers"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Text-to-Image Systems"
minutes: 10
category: diffusion-models
---

# Text-to-Image Systems — DALL·E · Imagen · Stable Diffusion
> The systems behind "type a prompt, get an image." They share a recipe: a **text encoder** (CLIP or
> a frozen T5 LLM) turns the prompt into an embedding, a **diffusion** model generates conditioned on
> it, and **classifier-free guidance** sharpens prompt adherence. They differ in *where* they diffuse
> and *how* they condition: **DALL·E 2** (unCLIP) diffuses to a CLIP image embedding then decodes;
> **Imagen** uses a frozen T5 + cascaded super-resolution; **Stable Diffusion** diffuses in a VAE
> latent with cross-attention.

**Why it matters:** the flagship application of generative AI and a favorite ML-systems-design
question. Interviews probe: the shared text-encoder → diffusion → CFG pipeline; the three design
choices that distinguish DALL·E 2 / Imagen / Stable Diffusion (CLIP-image-embedding prior vs. frozen
LLM text encoder vs. latent-space diffusion); why **Imagen found a big frozen LLM text encoder matters
more than image-model size**; CLIP's role in connecting text and images; and evaluation (FID for
fidelity, CLIP-score for prompt alignment) plus failure modes (compositionality, counting, text
rendering).

**⭐ Start here — suggested path:**

1. **Build intuition** — watch [How AI Image Generators Work (Stable Diffusion / DALL·E)](https://www.youtube.com/watch?v=1CIpzeNxIhU) — **Computerphile**. *The shared prompt → image pipeline in plain language.*
2. **See why it works** — read [How DALL·E 2 Actually Works](https://www.assemblyai.com/blog/how-dall-e-2-actually-works/) — **AssemblyAI**. *CLIP + diffusion prior + decoder (unCLIP), clearly.*
3. **Get the math** — watch [How does DALL·E 2 actually work?](https://www.youtube.com/watch?v=F1X4fHzF4mQ) — **AssemblyAI** + read [How Imagen Actually Works](https://www.assemblyai.com/blog/how-imagen-actually-works/). *Contrast the unCLIP prior with Imagen's frozen-T5 + cascade.*
4. **Read the sources** — [CLIP](https://arxiv.org/abs/2103.00020) → [GLIDE](https://arxiv.org/abs/2112.10741) → [DALL·E 2 / unCLIP](https://arxiv.org/abs/2204.06125) → [Imagen](https://arxiv.org/abs/2205.11487). *The shared building blocks, then the two flagship systems.*
5. **Make it concrete** — run [Stable Diffusion with Diffusers](https://huggingface.co/blog/stable_diffusion) — **Hugging Face**, and vary the prompt + guidance scale. *Generating and steering images cements the pipeline.*

## Courses (free)
- [Hugging Face — Diffusion Models Course](https://huggingface.co/learn/diffusion-course/unit0/1) — **Hugging Face** — free, code-first; build text-conditioned diffusion with `diffusers`.
- [Stanford CS231n — Generative Models notes](https://cs231n.github.io/) — **Stanford** — situates text-to-image within the broader generative-models map.

## Videos
- [How AI Image Generators Work (Stable Diffusion / DALL·E)](https://www.youtube.com/watch?v=1CIpzeNxIhU) — **Computerphile** — the best plain-language tour of the prompt → image pipeline.
- [How does DALL·E 2 actually work?](https://www.youtube.com/watch?v=F1X4fHzF4mQ) — **AssemblyAI** — the unCLIP design: CLIP embeddings, diffusion prior, and decoder.
- [DALL·E 2 Explained](https://www.youtube.com/watch?v=qTgPSKKjfVg) — **OpenAI** — the official short overview of capabilities and the two-stage architecture.
- [Diffusion models explained: how does OpenAI's GLIDE work?](https://www.youtube.com/watch?v=344w5h24-h8) — **AI Coffee Break (Letitia)** — text conditioning + guidance in the model that seeded DALL·E 2.

## Key Papers
- [Learning Transferable Visual Models From Natural Language Supervision (CLIP)](https://arxiv.org/abs/2103.00020) — **Radford et al. (2021)** — the text–image embedding space every system relies on.
- [Hierarchical Text-Conditional Image Generation with CLIP Latents (DALL·E 2 / unCLIP)](https://arxiv.org/abs/2204.06125) — **Ramesh et al. (2022)** — diffusion prior to a CLIP image embedding + decoder.
- [Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding (Imagen)](https://arxiv.org/abs/2205.11487) — **Saharia et al. (2022)** — frozen T5 text encoder + cascaded super-resolution.
- [GLIDE: Text-Guided Diffusion with CLIP/Classifier-Free Guidance](https://arxiv.org/abs/2112.10741) — **Nichol et al. (2022)** — the text-guided-diffusion precursor that established CFG for images.
- [Scaling Rectified Flow Transformers for High-Resolution Image Synthesis (Stable Diffusion 3)](https://arxiv.org/abs/2403.03206) — **Esser et al. (2024)** — the 2024–26 shape of a text-to-image system: rectified-flow objective, MMDiT transformer, three text encoders including T5.
- [Scalable Diffusion Models with Transformers (DiT)](https://arxiv.org/abs/2212.09748) — **Peebles & Xie (2023)** — the transformer backbone that replaced the U-Net in SD3, FLUX, and the video systems.
- [Muse: Text-To-Image Generation via Masked Generative Transformers](https://arxiv.org/abs/2301.00704) — **Chang et al. (2023)** — the non-diffusion branch: parallel masked-token decoding over a discrete image tokenizer, an order of magnitude fewer forward passes.

## Articles / Blogs (free, no paywall)
- [How DALL·E 2 Actually Works](https://www.assemblyai.com/blog/how-dall-e-2-actually-works/) — **AssemblyAI** — the clearest unCLIP walkthrough: CLIP, prior, decoder, upsamplers.
- [How Imagen Actually Works](https://www.assemblyai.com/blog/how-imagen-actually-works/) — **AssemblyAI** — frozen T5 encoder, diffusion, and the super-resolution cascade.
- [The Illustrated Stable Diffusion](https://jalammar.github.io/illustrated-stable-diffusion/) — **Jay Alammar** — the open-source system's components, visually.
- [Announcing Black Forest Labs (FLUX.1)](https://bfl.ai/announcements/24-08-01-bfl) — **Black Forest Labs** — the release note for the FLUX family from the original Stable Diffusion authors: a 12B rectified-flow transformer, and the current open-weights reference point.
- [Perspectives on diffusion](https://sander.ai/2023/07/20/perspectives.html) — **Sander Dieleman (Google DeepMind)** — the several equivalent ways to read a text-to-image model (denoiser, score, flow, autoregression in frequency), which is what makes the 2024–26 rectified-flow shift legible.

## Books (free, with chapters)
- [Understanding Deep Learning — **Ch. 18 "Diffusion models"**](https://udlbook.github.io/udlbook/) — **Simon Prince** — free PDF; conditional/text-guided diffusion in the diffusion chapter.
- [Probabilistic Machine Learning: Advanced Topics — **Ch. 25 "Diffusion models"**](https://probml.github.io/pml-book/book2.html) — **Kevin Murphy** — free PDF; conditional generation and guidance.

## In this platform
- Concept depth (the *why*): [ai-ml-intuitions 5.03 Diffusion Models](/ai-ml/ai-ml-intuitions/generation/diffusion-and-score-models/diffusion-forward-and-reverse-process-intuition)
- Prereq: [07 Latent Diffusion & Stable Diffusion](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/latent-diffusion-stable-diffusion/latent-diffusion-stable-diffusion) · [04 Conditional Generation & CFG](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/conditional-generation-and-classifier-free-guidance/conditional-generation-and-classifier-free-guidance) · [05 Diffusion Models (DDPM)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/diffusion-models-ddpm/diffusion-models-ddpm)
- Related: [Deep Learning — Transformer Architecture](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/transformer-architecture/transformer-architecture) (the text encoders) · [LLMs](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme)
- Next concepts: [12 Evaluation of Generative Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/evaluation-of-generative-models/evaluation-of-generative-models) · [13 Sampling & Guidance Techniques](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/sampling-and-guidance-techniques/sampling-and-guidance-techniques)
- Where these systems went in 2025–26: [Diffusion Transformers (DiT)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/diffusion-transformers-dit/diffusion-transformers-dit) · [Flow Matching & Rectified Flow](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/flow-matching-and-rectified-flow/flow-matching-and-rectified-flow) · [Video Diffusion Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/video-diffusion-models/video-diffusion-models) · [Consistency Models & Few-Step Generation](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/consistency-models-and-few-step-generation/consistency-models-and-few-step-generation)
- Field overview: [9. Generative AI](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/readme)
