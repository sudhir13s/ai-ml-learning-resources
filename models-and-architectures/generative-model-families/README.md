---
id: "models-and-architectures/generative-model-families"
topic: "Generative Model Families"
level: advanced
built_from: ["classic-architectures", "attention-and-transformers"]
updated: 2026-09-13
---

# Generative Model Families

> Models whose goal is to produce a sample rather than predict a label, grouped by the way they
> model the data distribution. Two sub-areas: the family map that ends in diffusion, and the
> diffusion line itself, which is deep enough to be its own course. Text generation is the
> [Large Language Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/readme)
> sub-area; the modalities these models generate for live in
> [Multimodal and Generative Media](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/readme).

**Start here:** [Variational Autoencoders and the ELBO](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/generative-models/variational-autoencoders-vae-elbo/variational-autoencoders-vae-elbo) for the latent-variable view, then [Diffusion Models (DDPM)](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/diffusion-models-ddpm/diffusion-models-ddpm) — the family the generative frontier runs through.

## Sub-areas

1. [Generative Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/generative-models/readme) — **7 pages** — the family map: variational autoencoders and the evidence lower bound, generative adversarial networks and their training, normalizing flows, energy-based models, autoregressive image generation, and how generative models are evaluated.
2. [Diffusion Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/readme) — **17 pages** — forward and reverse processes, the score-based view, latent diffusion, samplers and guidance, diffusion transformers, flow matching, few-step distillation, control and editing, video and 3D, serving and provenance.

## Courses (free)

- [Stanford CS236 — Deep Generative Models](https://deepgenerativemodels.github.io/) — **Stefano Ermon (Stanford)** — the score-based and diffusion lectures, from the group that co-invented score matching.
- [MIT 6.S184: Flow Matching and Diffusion Models](https://diffusion.csail.mit.edu/) — **Peter Holderrieth and Ezra Erives (MIT)** — the current objective behind most new generative systems, taught from first principles.
- [Hugging Face Diffusion Models Course](https://huggingface.co/learn/diffusion-course) — **Hugging Face** — free and code-first; conditioning, guidance and fine-tuning with runnable notebooks.

## Videos

- [Variational Autoencoders and Diffusion Models](https://www.youtube.com/watch?v=pea3sH6orMc) — **Tim Salimans (Google DeepMind)** — a researcher who built progressive distillation explaining why few-step sampling works.

## Key Papers

- [Classifier-Free Diffusion Guidance](https://arxiv.org/abs/2207.12598) — **Ho and Salimans (2022)** — one model, condition dropout and extrapolation at sampling time; the knob every image model exposes.
- [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) — **Ho, Jain and Abbeel (2020)** — the paper that made diffusion the dominant generative family.

## Articles / Blogs (free, no paywall)

- [What are Diffusion Models?](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) — **Lilian Weng** — the canonical open math walkthrough from forward process to the training loss.
- [Generative Modeling by Estimating Gradients of the Data Distribution](https://yang-song.net/blog/2021/score/) — **Yang Song** — the score-based view of diffusion from its originator; the natural second read.
- [Learning the integral of a diffusion model](https://sander.ai/2026/05/06/flow-maps.html) — **Sander Dieleman** — the unifying flow-map perspective on diffusion, flow matching and few-step generation.

## Books (free, with chapters)

- [*Understanding Deep Learning* — Ch. 18 "Diffusion models"](https://udlbook.github.io/udlbook/) — **Simon Prince** — free PDF; the clearest careful derivation of the denoising objective.
- [*Probabilistic Machine Learning: Advanced Topics* — Ch. 25 "Diffusion models"](https://probml.github.io/pml-book/book2.html) — **Kevin Murphy** — free PDF; the rigorous modern treatment.

## In this platform

- Section index: [Models and Architectures](/ai-ml/ai-ml-learning-resources/models-and-architectures/readme)
- Where these models meet their modalities: [Computer Vision](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/readme) · [Audio and Speech](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/readme) · [Video and Generative World Models](/ai-ml/ai-ml-learning-resources/world-models-and-embodied-ai/video-and-generative-world-models/interactive-video-and-generative-simulators/interactive-video-and-generative-simulators)
- Text generation by diffusion: [Diffusion Language Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/diffusion-language-models/diffusion-language-models)
- The mental models: [Diffusion Forward and Reverse Process](/ai-ml/ai-ml-intuitions/generation/diffusion-and-score-models/diffusion-forward-and-reverse-process-intuition) · [Latent Variable Models and the ELBO](/ai-ml/ai-ml-intuitions/generation/latent-variable-generation/latent-variable-models-and-elbo-intuition)
