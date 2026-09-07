---
id: "modalities-and-generative-models/multimodal-learning/unified-token-spaces-and-any-to-any-models"
topic: "Unified Token Spaces and Any-to-Any Models"
level: advanced
built_from: ["fusion-strategies-early-late-and-native-multimodality", "modern-open-vlm-architectures"]
leads_to: ["modalities-and-generative-models/multimodal-learning/multimodal-benchmarks-and-evaluation"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Unified Token Spaces and Any-to-Any Models"
minutes: 14
category: multimodal-learning
---

# Unified Token Spaces and Any-to-Any Models
> An *any-to-any* model takes any mix of modalities in and emits any mix out — text, images,
> audio — from **one sequence model over one vocabulary**. Two families exist: **discretize
> everything** (a vector-quantized tokenizer turns an image into integer tokens, and one
> transformer predicts the next token, as in Chameleon and Emu3), or **mix objectives** (next-token
> prediction for text, diffusion for continuous image patches, in one transformer, as in
> Transfusion and Show-o). GPT-4o and Gemini are the closed-model expression of the same idea.

**Why it matters:** it is the current frontier design, and the question "why not just tokenize
images and use an LLM?" has a real, quantitative answer.

- **Where it is today (2026):** interleaved generation — editing an image and explaining the
  edit in one turn — is standard in frontier products and increasingly in open models.
- **What interviewers probe:** the **quantization bottleneck**. A discrete tokenizer throws away
  detail before the transformer ever sees it, which caps image fidelity; Transfusion's answer is
  to keep image latents continuous and diffuse them instead.
- **The trade-off people get wrong:** unified models are trained jointly, so understanding and
  generation compete for capacity. Gains on generation benchmarks are routinely paid for in
  visual question-answering accuracy unless the data mix is carefully balanced.

**Start here — suggested path:**

1. **Start from the tokenizer** — read [Neural Discrete Representation Learning (VQ-VAE)](https://arxiv.org/abs/1711.00937) — **van den Oord et al. (2017)**. *Why images can become integers at all, and where the information goes when they do.*
2. **Read the discrete-unification paper** — read [Chameleon: Mixed-Modal Early-Fusion Foundation Models](https://arxiv.org/abs/2405.09818) — **Chameleon Team, Meta (2024)**. *One vocabulary, one transformer, interleaved output — plus the normalization changes needed to keep training stable.*
3. **Read the continuous alternative** — read [Transfusion](https://arxiv.org/abs/2408.11039) — **Zhou et al. (2024)**. *Next-token loss on text and diffusion loss on image patches in a single model; the controlled comparison against Chameleon is the point.*
4. **See what shipped** — read [Hello GPT-4o](https://openai.com/index/hello-gpt-4o/) — **OpenAI** — and the [Gemini 2.5 Technical Report](https://arxiv.org/abs/2507.06261) — **Gemini Team (2025)**. *Native multimodal input and output as products, with the modality coverage and limitations stated by the teams that built them.*
5. **Get the representation-level intuition** — read [Generative modelling in latent space](https://sander.ai/2025/04/15/latents.html) — **Sander Dieleman**. *What latents and tokenizers do to a generative model — the deepest treatment of the choice this page hinges on.*

## Courses (free)

- [Stanford CS25: Transformers United](https://web.stanford.edu/class/cs25/) — **Stanford** — the seminar that tracks native-multimodal transformer research release by release.
- [Hugging Face Community Computer Vision Course — multimodal unit](https://huggingface.co/learn/computer-vision-course/en/unit4/multimodal-models/pre-intro) — **Hugging Face** — free background on multimodal tokenization and generation.

## Key Papers

- [Neural Discrete Representation Learning (VQ-VAE)](https://arxiv.org/abs/1711.00937) — **van den Oord, Vinyals & Kavukcuoglu (2017)** — the discrete latent codebook every token-based image model still uses.
- [Taming Transformers for High-Resolution Image Synthesis (VQGAN)](https://arxiv.org/abs/2012.09841) — **Esser, Rombach & Ommer (2021)** — adds adversarial and perceptual losses so discrete tokens reconstruct sharply enough to generate from.
- [Chameleon: Mixed-Modal Early-Fusion Foundation Models](https://arxiv.org/abs/2405.09818) — **Chameleon Team, Meta (2024)** — the fully token-based any-to-any model, with the training-stability recipe.
- [Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model](https://arxiv.org/abs/2408.11039) — **Zhou et al. (2024)** — one transformer, two objectives; sidesteps quantization loss and beats Chameleon at matched compute.
- [Show-o: One Single Transformer to Unify Multimodal Understanding and Generation](https://arxiv.org/abs/2408.12528) — **Xie et al. (2024)** — autoregressive text plus discrete diffusion for images in a single model.
- [Emerging Properties in Unified Multimodal Pretraining (BAGEL)](https://arxiv.org/abs/2505.14683) — **Deng et al. (2025)** — a large open unified model, and the capability transitions that appear only with scale.

## Articles / Blogs (free, no paywall)

- [Hello GPT-4o](https://openai.com/index/hello-gpt-4o/) — **OpenAI** — the end-to-end audio-vision-text framing that made "omni" models mainstream, with the latency argument for one model over a pipeline.
- [Gemini 2.5 Technical Report](https://arxiv.org/abs/2507.06261) — **Gemini Team (2025)** — free primary source on a natively multimodal frontier model: input modalities, long context, and evaluation.
- [Generative modelling in latent space](https://sander.ai/2025/04/15/latents.html) — **Sander Dieleman** — why the tokenizer or latent space, not the transformer, usually decides generation quality.
- [Gemini](https://deepmind.google/models/gemini/) — **Google DeepMind** — the natively multimodal closed-model line; the model cards state the input and output modalities precisely.

## Books (free, with chapters)

- [*Understanding Deep Learning* — Ch. 18 "Diffusion models"](https://udlbook.github.io/udlbook/) — **Simon Prince** — free PDF; the diffusion half of Transfusion-style hybrid objectives.

## In this platform

- Prerequisites: [Fusion Strategies](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/fusion-strategies-early-late-and-native-multimodality/fusion-strategies-early-late-and-native-multimodality) · [Modern Open VLM Architectures](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/modern-open-vlm-architectures/modern-open-vlm-architectures)
- The generation side: [Diffusion Models (DDPM)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/diffusion-models-ddpm/diffusion-models-ddpm) · [Latent Diffusion and Stable Diffusion](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/latent-diffusion-stable-diffusion/latent-diffusion-stable-diffusion) · [Text-to-Image Systems](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/text-to-image-systems/text-to-image-systems)
- Related: [Tokenization and Subword Algorithms](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/natural-language-processing/tokenization-and-subword-algorithms/tokenization-and-subword-algorithms) — the text analogue of an image codebook
- Next: [Multimodal Benchmarks and Evaluation](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/multimodal-benchmarks-and-evaluation/multimodal-benchmarks-and-evaluation)
