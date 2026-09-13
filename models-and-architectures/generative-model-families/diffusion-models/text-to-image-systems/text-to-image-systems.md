---
id: "10-generative-ai/text-to-image"
topic: "Text-to-Image Systems"
core_idea: "Text-to-image systems share one pipeline of a text encoder, a conditioned diffusion model and classifier-free guidance, and differ mainly in where they diffuse and how strong the text encoder is."
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

## References

The curated link library for this topic — in this platform, videos, courses, articles, papers, books — lives in a companion file so it can be reused as a standalone reference list:

**→ [Text-to-Image Systems — DALL·E · Imagen · Stable Diffusion — references](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/text-to-image-systems/text-to-image-systems#references-further-reading)**
