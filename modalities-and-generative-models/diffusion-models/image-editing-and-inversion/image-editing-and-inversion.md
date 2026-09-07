---
id: "modalities-and-generative-models/diffusion-models/image-editing-and-inversion"
topic: "Image Editing & Inversion"
level: advanced
built_from: ["sampling-and-guidance-techniques", "controlnet-and-conditioning-adapters", "latent-diffusion-stable-diffusion"]
leads_to: ["personalization-dreambooth-textual-inversion-lora", "safety-provenance-and-watermarking"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Image Editing & Inversion"
minutes: 14
category: diffusion-models
---

# Image Editing & Inversion
> Editing a *real* photo with a diffusion model needs an extra step that pure generation does not:
> **inversion** — finding the noise (and prompt embedding) that would have produced this image, so the
> model can re-generate it with one thing changed. The three practical routes are add-noise-and-denoise
> (**SDEdit**), run the deterministic sampler backwards (**DDIM inversion**, repaired by **null-text
> inversion**), and skip inversion entirely by training an instruction-following editor
> (**InstructPix2Pix**, and the 2025 in-context editors).

**Why it matters:** every "change the background, keep the person" feature is this problem, and it is
where diffusion systems most visibly fail. Interviewers probe the **edit-fidelity trade-off**: more
noise (higher SDEdit strength) gives a stronger edit and a weaker resemblance to the original; DDIM
inversion drifts once classifier-free guidance is above ~1, which is exactly why null-text inversion
optimizes the unconditional embedding per step; and attention-map methods (**Prompt-to-Prompt**)
preserve layout by reusing cross-attention maps rather than pixels.

**Start here — suggested path:**

1. **Start with the simplest method** — read the [Diffusers image-to-image guide](https://huggingface.co/docs/diffusers/using-diffusers/img2img) — **Hugging Face**. *The `strength` parameter *is* the SDEdit trade-off; run it before reading theory.*
2. **Get the original idea** — read [SDEdit](https://arxiv.org/abs/2108.01073) — **Meng et al. (2021)**. *Noise then denoise: realism versus faithfulness controlled by a single time index.*
3. **Understand inversion properly** — read [Null-text Inversion for Editing Real Images](https://arxiv.org/abs/2211.09794) — **Mokady et al. (2022)**. *Why DDIM inversion breaks under guidance, and the per-timestep fix.*
4. **See instruction editing** — read [InstructPix2Pix](https://arxiv.org/abs/2211.09800) — **Brooks, Holynski & Efros (2022)** and its plain-language summary in [The Batch](https://www.deeplearning.ai/the-batch/instructpix2pix-for-text-to-image-editing-explained) — **DeepLearning.AI**. *Synthesize a paired dataset with GPT-3 plus Prompt-to-Prompt, then train a supervised editor.*
5. **Catch up to 2025–26** — read [FLUX.1 Kontext](https://arxiv.org/abs/2506.15742) — **Black Forest Labs (2025)**. *In-context editing inside a flow-matching transformer: no inversion, character consistency across turns.*

## Courses (free)

- [Hugging Face Diffusion Models Course](https://huggingface.co/learn/diffusion-course) — **Hugging Face** — free; the image-to-image and inpainting units are the practical foundation for every method here.
- [Stanford CME296: Diffusion & Large Vision Models](https://www.youtube.com/playlist?list=PLoROMvodv4rNdy8rt2rZ4T2xM0OjADnfu) — **Stanford Online** — covers editing and inversion within the modern vision stack.

## Videos

- [InstructPix2Pix Explained — Edit Images with Words](https://www.youtube.com/watch?v=-I9-2XK3kOs) — **Jonathan Whitaker (DataScienceCastnet)** — from a co-author of the Hugging Face Diffusion Course: the dataset-generation trick and the two guidance scales.
- [ControlNet with Diffusion Models — Explanation and PyTorch Implementation](https://www.youtube.com/watch?v=n6CwImm_WDI) — **ExplainingAI** — the conditioning path you will reuse for structure-preserving edits.

## Key Papers

- [SDEdit: Guided Image Synthesis and Editing with Stochastic Differential Equations](https://arxiv.org/abs/2108.01073) — **Meng et al. (2021)** — the realism/faithfulness dial that every image-to-image pipeline still uses.
- [Prompt-to-Prompt Image Editing with Cross-Attention Control](https://arxiv.org/abs/2208.01626) — **Hertz et al. (2022)** — edit by swapping words while reusing attention maps; the basis of layout-preserving edits.
- [Null-text Inversion for Editing Real Images](https://arxiv.org/abs/2211.09794) — **Mokady et al. (2022)** — makes classifier-free-guided DDIM inversion actually reconstruct the input.
- [InstructPix2Pix: Learning to Follow Image Editing Instructions](https://arxiv.org/abs/2211.09800) — **Brooks, Holynski & Efros (2022)** — instruction editing without inversion, via synthetic paired data.
- [FLUX.1 Kontext: Flow Matching for In-Context Image Generation and Editing](https://arxiv.org/abs/2506.15742) — **Black Forest Labs (2025)** — the current generation: sequence-concatenation editing in a 12B rectified-flow transformer.

## Articles / Blogs (free, no paywall)

- [InstructPix2Pix for Text-to-Image Editing, Explained](https://www.deeplearning.ai/the-batch/instructpix2pix-for-text-to-image-editing-explained) — **DeepLearning.AI (The Batch)** — short, accurate, and free; good orientation before the paper.
- [Diffusers image-to-image documentation](https://huggingface.co/docs/diffusers/using-diffusers/img2img) — **Hugging Face** — maintained reference for strength, inpainting, and pipeline chaining.
- [The geometry of diffusion guidance](https://sander.ai/2023/08/28/geometry.html) — **Sander Dieleman (Google DeepMind)** — the geometric picture of guidance that explains why inversion degrades as the guidance scale grows.

## In this platform

- Prerequisites: [Sampling & Guidance Techniques](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/sampling-and-guidance-techniques/sampling-and-guidance-techniques) (DDIM, the sampler you invert) · [ControlNet & Conditioning Adapters](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/controlnet-and-conditioning-adapters/controlnet-and-conditioning-adapters)
- Next: [Personalization (DreamBooth · Textual Inversion · LoRA)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/personalization-dreambooth-textual-inversion-lora/personalization-dreambooth-textual-inversion-lora) · [Safety, Provenance & Watermarking](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/safety-provenance-and-watermarking/safety-provenance-and-watermarking)
- Related: [Latent Diffusion & Stable Diffusion](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/latent-diffusion-stable-diffusion/latent-diffusion-stable-diffusion) · [Multimodal Learning](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/readme) (the vision-language models that read edit instructions)
- Field overview: [Diffusion Models index](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/readme)
