---
id: "llms-applications-and-agents/llm-model-architectures/diffusion-language-models"
topic: "Diffusion Language Models"
level: advanced
built_from: ["decoder-only-models", "diffusion-models-ddpm"]
leads_to: ["inference-optimization"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Diffusion Language Models"
minutes: 14
category: llm-model-architectures
---

# Diffusion Language Models

> The autoregressive assumption — one token at a time, left to right — is a choice, not a law. A
> **diffusion language model (dLM)** corrupts a sequence (usually by masking tokens) and trains a
> transformer to reverse that corruption, so generation becomes a handful of parallel denoising
> passes over the whole sequence instead of hundreds of sequential steps.

**Why it matters:** it is the only credible non-autoregressive challenger at scale, and 2025 produced
the first commercial ones — so it is now a fair interview question rather than a curiosity.

- **What is probed:** why discrete data breaks the Gaussian diffusion story, and the two fixes — discrete corruption processes (D3PM, absorbing-state masking) and score-entropy objectives (SEDD); why masked diffusion's objective is a weighted average of masked-language-model losses.
- **The genuine win:** **parallel decoding**. Mercury reports over 1,000 tokens per second on an H100 by emitting many tokens per pass, and any-order generation makes infilling and constrained editing natural.
- **The honest cost:** the likelihood is a bound, not an exact value; quality per unit of compute still trails a well-tuned autoregressive model; and key-value caching — the entire autoregressive inference stack — does not transfer unchanged, because tokens are revised rather than appended.

**Start here — suggested path:**

1. **Get the framing from a practitioner** — read [Diffusion language models](https://sander.ai/2023/01/09/diffusion-language.html) — **Sander Dieleman (DeepMind)**. *Why text resisted diffusion, and what the discrete-versus-continuous choice really costs.*
2. **Read the discrete foundation** — read [Structured Denoising Diffusion Models in Discrete State-Spaces (D3PM)](https://arxiv.org/abs/2107.03006) — **Austin et al. (2021)**. *Corruption as a transition matrix; absorbing-state masking is the variant that survived.*
3. **Get the modern objective** — read [SEDD](https://arxiv.org/abs/2310.16834) — **Lou, Meng & Ermon (2023)** and [MDLM](https://arxiv.org/abs/2406.07524) — **Sahoo et al. (2024)**. *Score-entropy on ratios of the data distribution, then the simple masked recipe that made results competitive.*
4. **See it at scale** — read [LLaDA](https://arxiv.org/abs/2502.09992) — **Nie et al. (2025)** and [Mercury](https://arxiv.org/abs/2506.17298) — **Inception Labs (2025)**. *An 8-billion-parameter open diffusion model, then the first commercial one with throughput numbers.*
5. **Build the intuition to code** — read [How to Build a Diffusion Language Model](https://kuleshov-group.github.io/blog/blog/2026/how-to-build-a-diffusion-language-model/) — **Kuleshov Group (Cornell)**. *The MDLM authors' own tutorial: masking diffusion, iterative refinement, variable-length generation.*

## Courses (free)

- [How to Build a Diffusion Language Model](https://kuleshov-group.github.io/blog/blog/2026/how-to-build-a-diffusion-language-model/) — **Kuleshov Group** — a workshop-lecture-derived tutorial by the authors of MDLM; the closest thing to a course on the topic.
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) — **Hugging Face** — free; establishes the autoregressive baseline these models are measured against.

## Key Papers

- [Structured Denoising Diffusion Models in Discrete State-Spaces (D3PM)](https://arxiv.org/abs/2107.03006) — **Austin et al. (2021)** — the discrete-diffusion framework, including the absorbing (mask) process.
- [Diffusion-LM Improves Controllable Text Generation](https://arxiv.org/abs/2205.14217) — **Li et al. (2022)** — the continuous-embedding route, and the controllability argument for diffusion over text.
- [Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution (SEDD)](https://arxiv.org/abs/2310.16834) — **Lou, Meng & Ermon (2023)** — score entropy: the objective that closed much of the perplexity gap.
- [Simple and Effective Masked Diffusion Language Models (MDLM)](https://arxiv.org/abs/2406.07524) — **Sahoo et al. (2024)** — the simplified masked objective as a weighted mixture of masked-language-model losses.
- [Large Language Diffusion Models (LLaDA)](https://arxiv.org/abs/2502.09992) — **Nie et al. (2025)** — an 8-billion-parameter diffusion model trained from scratch, competitive with a same-size autoregressive baseline.
- [Mercury: Ultra-Fast Language Models Based on Diffusion](https://arxiv.org/abs/2506.17298) — **Inception Labs (2025)** — the first commercial-scale diffusion LLM; the throughput numbers that make the case.

## Articles / Blogs (free, no paywall)

- [Diffusion language models](https://sander.ai/2023/01/09/diffusion-language.html) — **Sander Dieleman** — the essay that framed the whole problem: discreteness, likelihoods, and why text is hard for diffusion.
- [Continuous diffusion language models](https://sander.ai/2026/08/24/continuous-dlms.html) — **Sander Dieleman** — the 2026 follow-up on the revival of the continuous route, with historical perspective.
- [Gemini Diffusion](https://deepmind.google/models/gemini-diffusion/) — **Google DeepMind** — a frontier lab's own description of a diffusion text model and what its speed is for.

## Books (free, with chapters)

- [*Understanding Deep Learning* — Ch. 18 "Diffusion models"](https://udlbook.github.io/udlbook/) — **Simon Prince** — free PDF; the forward/reverse process and the evidence lower bound, in the notation these papers assume.

## In this platform

- The autoregressive baseline this challenges: [Decoder-Only Models](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/decoder-only-models/decoder-only-models) · [Language Modeling Objectives](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/language-modeling-objectives/language-modeling-objectives)
- Canonical home of the diffusion machinery: [Diffusion Models (DDPM)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/diffusion-models-ddpm/diffusion-models-ddpm) · [Score-Based and SDE Diffusion](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/score-based-and-sde-diffusion/score-based-and-sde-diffusion) · [Sampling and Guidance Techniques](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/sampling-and-guidance-techniques/sampling-and-guidance-techniques)
- What parallel decoding changes at serving time: [Decoding and Sampling](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/decoding-and-sampling/decoding-and-sampling) · [Inference Optimization](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/inference-optimization/inference-optimization) · [KV Cache](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/kv-cache/kv-cache)
- The attention design space it inherits: [Attention Architectures](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/attention-architectures-gqa-mla-sliding-and-linear/attention-architectures-gqa-mla-sliding-and-linear)
- Intuition track: [Diffusion Forward and Reverse Process](/ai-ml/ai-ml-intuitions/generation/diffusion-and-score-models/diffusion-forward-and-reverse-process-intuition) · [Autoregressive Generation and Sampling Controls](/ai-ml/ai-ml-intuitions/generation/autoregressive-generation/autoregressive-generation-and-sampling-controls-intuition)
