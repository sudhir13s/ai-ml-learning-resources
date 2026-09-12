---
id: "11-diffusion"
topic: "Diffusion Models"
level: advanced
built_from: ["generative-ai", "deep-learning"]
leads_to: ["multimodal", "video-understanding"]
updated: 2026-09-07
---

# Diffusion Models
> The full home for diffusion: the foundations (forward and reverse process, score-based view,
> latent diffusion, samplers and guidance) followed by the modern stack — transformer backbones,
> flow matching, few-step generation, control and editing, video and 3D, serving, and provenance.

**Start here:** [What are Diffusion Models? (Lil'Log)](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) — **Lilian Weng** — the canonical math walkthrough; read it before anything else in this topic.

## Concept Index
Every chapter is a self-contained folder (`<topic>/<topic>.md`) with its page.
> Foundations first, then top to bottom. Reading order is fixed by `metadata.yaml`.

### Foundations
1. ✅ [Conditional Generation & Classifier-Free Guidance](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/conditional-generation-and-classifier-free-guidance/conditional-generation-and-classifier-free-guidance)
2. ✅ [Diffusion Models — DDPM (forward/reverse process)](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/diffusion-models-ddpm/diffusion-models-ddpm)
3. ✅ [Score-Based & SDE Diffusion (score matching · probability-flow ODE)](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/score-based-and-sde-diffusion/score-based-and-sde-diffusion)
4. ✅ [Latent Diffusion & Stable Diffusion (VAE + U-Net + text)](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/latent-diffusion-stable-diffusion/latent-diffusion-stable-diffusion)
5. ✅ [Text-to-Image Systems (DALL·E · Imagen · Stable Diffusion)](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/text-to-image-systems/text-to-image-systems)
6. ✅ [Sampling & Guidance Techniques (DDIM · solvers · guidance scale)](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/sampling-and-guidance-techniques/sampling-and-guidance-techniques)

### Modern architectures
7. ✅ [Flow Matching & Rectified Flow (the post-DDPM formulation)](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/flow-matching-and-rectified-flow/flow-matching-and-rectified-flow) — read after the score-based chapter
8. ✅ [Diffusion Transformers (DiT · U-Net → transformer backbones)](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/diffusion-transformers-dit/diffusion-transformers-dit)

### Fast generation
9. ✅ [Consistency Models & Few-Step Generation](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/consistency-models-and-few-step-generation/consistency-models-and-few-step-generation)
10. ✅ [Distillation for Fast Sampling (progressive distillation · LCM · turbo)](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/distillation-for-fast-sampling/distillation-for-fast-sampling)

### Control, editing & personalization
11. ✅ [ControlNet & Conditioning Adapters](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/controlnet-and-conditioning-adapters/controlnet-and-conditioning-adapters)
12. ✅ [Image Editing & Inversion (SDEdit · null-text inversion · instruction editing)](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/image-editing-and-inversion/image-editing-and-inversion)
13. ✅ [Personalization (DreamBooth · textual inversion · diffusion LoRA)](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/personalization-dreambooth-textual-inversion-lora/personalization-dreambooth-textual-inversion-lora)

### Beyond still images
14. ✅ [Video Diffusion Models (temporal layers · cascaded and latent video)](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/video-diffusion-models/video-diffusion-models)
15. ✅ [3D Generation & Score Distillation (SDS · text-to-3D · Gaussian splats)](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/3d-generation-score-distillation/3d-generation-score-distillation)

### Production
16. ✅ [Diffusion Inference Optimization (samplers · caching · quantization)](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/diffusion-inference-optimization/diffusion-inference-optimization)
17. ✅ [Safety, Provenance & Watermarking (C2PA · SynthID · concept erasure)](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/safety-provenance-and-watermarking/safety-provenance-and-watermarking)

### Related concepts (covered in another section)
> Neighbouring subjects stay in their canonical home to avoid repetition.
- **VAEs, GANs, normalizing flows, evaluation metrics** → [Generative Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/generative-models/readme)
- **Audio & music diffusion** → [Audio & Speech](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/readme)
- **Video recognition, retrieval and captioning** → [Video Understanding](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/video-understanding/readme)
- **LoRA and adapter mathematics** → [LoRA & Parameter-Efficient Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/lora-and-parameter-efficient-fine-tuning/lora-and-parameter-efficient-fine-tuning)
- **Quantization and serving for neural networks** → [Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization)

## Courses (free)
- [MIT 6.S184: Flow Matching and Diffusion Models (2026)](https://www.youtube.com/playlist?list=PL57nT7tSGAAXwjhDYcxEycx5W7YoSrZyt) — **Peter Holderrieth (MIT)** — the canonical free course; lectures, notes, and labs building diffusion and flow matching together ([course site](https://diffusion.csail.mit.edu/)).
- [Stanford CME296: Diffusion & Large Vision Models](https://www.youtube.com/playlist?list=PLoROMvodv4rNdy8rt2rZ4T2xM0OjADnfu) — **Stanford Online** — the 2025 lecture series on diffusion transformers, video models, and the production stack.
- [Hugging Face Diffusion Models Course](https://huggingface.co/learn/diffusion-course) — **Hugging Face** — free, code-first; the practical companion to every chapter here.
- [Practical Deep Learning for Coders, Part 2 — Stable Diffusion from scratch](https://course.fast.ai/Lessons/part2.html) — **fast.ai (Jeremy Howard, Jonathan Whitaker, Tanishq Abraham)** — builds Stable Diffusion up from matrix multiplications.

## Videos
- [MIT 6.S184 Lecture 01 — Generative AI with SDEs](https://www.youtube.com/watch?v=GCoP2w-Cqtg) — **Peter Holderrieth (MIT)** — flows and ODEs before any diffusion notation.
- [Diffusion models from scratch in PyTorch](https://www.youtube.com/watch?v=a4Yfz2FxXiY) — **DeepFindr** — implement DDPM end to end before going modern.
- [Video Generation with Diffusion Transformers](https://www.youtube.com/watch?v=KAYYo3lNOHY) — **ExplainingAI** — the space-time patch view behind Sora-style models.

## Key Papers
- [Scalable Diffusion Models with Transformers (DiT)](https://arxiv.org/abs/2212.09748) — **Peebles & Xie (2022)** — the backbone behind modern image and video generators.
- [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747) — **Lipman et al. (2022)** — the formulation that replaced DDPM in current systems.
- [Scaling Rectified Flow Transformers (Stable Diffusion 3)](https://arxiv.org/abs/2403.03206) — **Esser et al. (2024)** — MMDiT plus rectified flow; the reference production recipe.
- [Adding Conditional Control to Text-to-Image Diffusion Models (ControlNet)](https://arxiv.org/abs/2302.05543) — **Zhang et al. (2023)** — the standard for structural control.
- [Consistency Models](https://arxiv.org/abs/2303.01469) — **Song et al. (2023)** — few-step generation.

## Articles
- [Perspectives on diffusion](https://sander.ai/2023/07/20/perspectives.html) — **Sander Dieleman (Google DeepMind)** — how the field's best practitioner thinks about the design space.
- [Diffusion Meets Flow Matching: Two Sides of the Same Coin](https://diffusionflow.github.io/) — **Google DeepMind** — the equivalence between the two frameworks, worked out.
- [The Annotated Diffusion Model](https://huggingface.co/blog/annotated-diffusion) — **Hugging Face** — runnable code plus math, line by line.
- [Diffusion Models for Video Generation](https://lilianweng.github.io/posts/2024-04-12-diffusion-video/) — **Lilian Weng** — the free survey of video architectures.

## Books
- [*Understanding Deep Learning* — Ch. 18 "Diffusion models"](https://udlbook.github.io/udlbook/) — **Simon Prince** — free, rigorous, visual.
- [*Probabilistic Machine Learning: Advanced Topics* — Ch. 25 "Diffusion models"](https://probml.github.io/pml-book/book2.html) — **Kevin Murphy** — free PDF; samplers, the probability-flow ODE, and guidance.

## In this platform
- Foundations: [Generative Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/generative-models/readme)
- Intuition (the *why*): [Diffusion forward and reverse process](/ai-ml/ai-ml-intuitions/generation/diffusion-and-score-models/diffusion-forward-and-reverse-process-intuition)
