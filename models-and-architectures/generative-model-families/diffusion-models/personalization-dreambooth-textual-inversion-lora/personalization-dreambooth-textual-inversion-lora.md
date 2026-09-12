---
id: "models-and-architectures/generative-model-families/diffusion-models/personalization-dreambooth-textual-inversion-lora"
topic: "Personalization — DreamBooth, Textual Inversion & LoRA"
level: advanced
built_from: ["latent-diffusion-stable-diffusion", "controlnet-and-conditioning-adapters"]
leads_to: ["models-and-architectures/generative-model-families/diffusion-models/image-editing-and-inversion", "models-and-architectures/generative-model-families/diffusion-models/diffusion-inference-optimization"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Personalization — DreamBooth, Textual Inversion & LoRA"
minutes: 14
category: diffusion-models
---

# Personalization — DreamBooth, Textual Inversion & LoRA
> **Personalization** teaches a general text-to-image model one specific subject — your dog, your
> product, a brand style — from three to five photos. The three methods differ in *what they change*:
> **textual inversion** learns only a new word embedding (a few kilobytes, model frozen),
> **DreamBooth** fine-tunes the whole network against a rare token plus a prior-preservation loss, and
> **LoRA** trains low-rank update matrices on the attention layers — the practical middle ground at
> a few megabytes.

**Why it matters:** it is the most-shipped diffusion feature after plain generation, and the
trade-offs are exactly the ones interviewers like. They probe: **language drift and overfitting** —
after DreamBooth, "a dog" starts producing *your* dog, which is why the class-specific
prior-preservation loss exists; why a **rare identifier token** (`sks`) beats a common word; how LoRA
rank and learning rate trade subject fidelity against prompt flexibility; and how multiple adapters
are merged or swapped at serving time without reloading the base model.

**Start here — suggested path:**

1. **See the goal** — read the [DreamBooth project page](https://dreambooth.github.io/) — **Ruiz et al. (Google Research)**. *Same subject, new contexts — the figures define the task in ten seconds.*
2. **Compare the cheapest method** — read [An Image is Worth One Word (Textual Inversion)](https://arxiv.org/abs/2208.01618) — **Gal et al. (2022)**. *Learning a single embedding, model untouched; the baseline every other method is judged against.*
3. **Get the fine-tuning mechanism** — read [DreamBooth](https://arxiv.org/abs/2208.12242) — **Ruiz et al. (2022)**, Section 3. *The rare token, the prior-preservation loss, and the failure modes the loss prevents.*
4. **Learn the production default** — read [Using LoRA for Efficient Stable Diffusion Fine-Tuning](https://huggingface.co/blog/lora) — **Hugging Face**. *Why low-rank adapters became the shipping format: small files, hot-swappable, composable.*
5. **Train one** — follow the [Diffusers DreamBooth training guide](https://huggingface.co/docs/diffusers/training/dreambooth) — **Hugging Face** with LoRA enabled, on five images. *Twenty minutes on a free GPU; then test the "a dog" prompt to see drift for yourself.*

## Courses (free)

- [Hugging Face Diffusion Models Course](https://huggingface.co/learn/diffusion-course) — **Hugging Face** — free and code-first; the fine-tuning unit is the direct prerequisite for these recipes.
- [Stanford CME296: Diffusion & Large Vision Models](https://www.youtube.com/playlist?list=PLoROMvodv4rNdy8rt2rZ4T2xM0OjADnfu) — **Stanford Online** — adaptation and personalization inside the broader vision-model curriculum.

## Videos

- [Personalized Image Generation (using DreamBooth) explained](https://www.youtube.com/watch?v=TKTBZ5zNxT0) — **DeepFindr** — the method plus a runnable Colab; the clearest short explanation of prior preservation.
- [Lecture 10 — DreamBooth](https://www.youtube.com/watch?v=D641lhioXMc) — **UCF Center for Research in Computer Vision** — a university lecture treatment, with the ablations spelled out.

## Key Papers

- [DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation](https://arxiv.org/abs/2208.12242) — **Ruiz et al. (2022)** — rare-token binding plus prior preservation; the reference method.
- [An Image is Worth One Word: Textual Inversion](https://arxiv.org/abs/2208.01618) — **Gal et al. (2022)** — personalization as embedding search, with the model entirely frozen.
- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) — **Hu et al. (2021)** — the low-rank update that the diffusion community adopted wholesale.
- [Multi-Concept Customization of Text-to-Image Diffusion (Custom Diffusion)](https://arxiv.org/abs/2212.04488) — **Kumari et al. (2022)** — tuning only cross-attention key/value projections, and composing several concepts.
- [IP-Adapter: Text Compatible Image Prompt Adapter](https://arxiv.org/abs/2308.06721) — **Ye et al. (2023)** — training-free-at-use-time personalization: pass a reference image instead of fine-tuning.

## Articles / Blogs (free, no paywall)

- [Using LoRA for Efficient Stable Diffusion Fine-Tuning](https://huggingface.co/blog/lora) — **Hugging Face** — the canonical practitioner write-up, with memory numbers and file sizes.
- [DreamBooth training documentation](https://huggingface.co/docs/diffusers/training/dreambooth) — **Hugging Face** — maintained recipe: hyperparameters, prior-preservation data, and common failure modes.
- [Textual Inversion training documentation](https://huggingface.co/docs/diffusers/training/text_inversion) — **Hugging Face** — the lightest-weight path, useful as the baseline in any comparison.

## In this platform

- Prerequisites: [Latent Diffusion & Stable Diffusion](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/latent-diffusion-stable-diffusion/latent-diffusion-stable-diffusion) · [ControlNet & Conditioning Adapters](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/controlnet-and-conditioning-adapters/controlnet-and-conditioning-adapters)
- Canonical home for the adapter maths: [LoRA & Parameter-Efficient Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/lora-and-parameter-efficient-fine-tuning/lora-and-parameter-efficient-fine-tuning)
- Next: [Image Editing & Inversion](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/image-editing-and-inversion/image-editing-and-inversion) · [Diffusion Inference Optimization](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/diffusion-inference-optimization/diffusion-inference-optimization) (serving many adapters)
- Related: [Safety, Provenance & Watermarking](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/safety-provenance-and-watermarking/safety-provenance-and-watermarking) (likeness and consent risks) · [Transfer Learning for Vision](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/transfer-learning-for-vision/transfer-learning-for-vision)
- Field overview: [Diffusion Models index](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/readme)
