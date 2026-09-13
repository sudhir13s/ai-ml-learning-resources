---
id: "10-generative-ai/autoregressive-pixelcnn"
topic: "Autoregressive Image Generation (PixelCNN)"
core_idea: "Factoring an image into per-pixel conditionals gives exact likelihoods and stable training, with masked convolutions preventing lookahead, at the price of generating one pixel at a time."
parent: "10-generative-ai"
level: advanced
built_from: ["cnns", "softmax", "chain-rule-probability", "maximum-likelihood"]
interview_frequency: low
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Autoregressive Image Generation (PixelCNN)"
minutes: 10
category: generative-models
---

# Autoregressive Image Generation — PixelRNN · PixelCNN
> Treat an image as a sequence of pixels and model it the way a language model models text: factor the
> joint as a product of conditionals `p(x) = ∏ p(x_i | x_<i)` and predict each pixel from all the ones
> "before" it (raster order). **PixelRNN** uses recurrence; **PixelCNN** uses **masked convolutions**
> so a pixel never sees future pixels. Exact likelihoods, sharp samples — but generation is slow
> (one pixel at a time).

**Why it matters:** the image analogue of autoregressive language models, and a clean exact-likelihood
baseline. Interviews probe: the **chain-rule factorization** and the raster-scan ordering; how a
**causal mask** on the convolution kernel enforces "no peeking ahead" (and the **blind-spot** problem
that gated PixelCNN fixes with horizontal/vertical stacks); why output is a **softmax over 256
intensities** rather than a regression; and the core trade-off — exact likelihood and stable training,
but `O(H·W)` sequential sampling. It also seeds VQ-VAE / DALL·E-1, which run autoregressive models
over *discrete latent codes* instead of raw pixels.

## References

The curated link library for this topic — in this platform, videos, courses, articles, papers, books — lives in a companion file so it can be reused as a standalone reference list:

**→ [Autoregressive Image Generation — PixelRNN · PixelCNN — references](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/generative-models/autoregressive-image-generation-pixelcnn/autoregressive-image-generation-pixelcnn#references-further-reading)**
