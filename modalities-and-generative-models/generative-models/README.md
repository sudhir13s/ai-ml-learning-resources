---
id: "10-generative-ai"
topic: "Generative AI"
level: advanced
built_from: ["deep-learning"]
updated: 2026-06-27
---

# Generative AI
> Models that *create* — images, audio, video, 3D — via VAEs, GANs, and (today) diffusion.
> (Text generation lives under [LLMs](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme).)

**⭐ Start here:** [What are Diffusion Models?](https://www.youtube.com/watch?v=fbLgFrlTnGU) — **Ari Seff** — the clearest intro to the method behind Stable Diffusion / DALL·E.

## 📑 Concept Index
Every chapter is a self-contained folder (`NN-Concept/NN-Concept.md`) with its page.
> **✅ ready · ⬜ coming soon.** New to generative modeling? Start with the field overview below, then work top to bottom.

### Likelihood-based models (VAEs, flows, autoregressive)
1. ✅ [Variational Autoencoders (VAE · ELBO · reparameterization)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/variational-autoencoders-vae-elbo/variational-autoencoders-vae-elbo)
8. ✅ [Normalizing Flows (RealNVP · Glow · exact likelihood)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/normalizing-flows/normalizing-flows)
10. ✅ [Autoregressive Image Generation (PixelRNN · PixelCNN)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/autoregressive-image-generation-pixelcnn/autoregressive-image-generation-pixelcnn)

### Adversarial models (GANs)
2. ✅ [GANs & DCGAN (the adversarial game)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/gans-and-dcgan/gans-and-dcgan)
3. ✅ [GAN Training Pathologies & WGAN (mode collapse · Wasserstein)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/gan-training-and-wgan/gan-training-and-wgan)
4. ✅ [Conditional Generation & Classifier-Free Guidance (cGAN · CFG)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/conditional-generation-and-classifier-free-guidance/conditional-generation-and-classifier-free-guidance)

### Diffusion & score-based models
5. ✅ [Diffusion Models — DDPM (forward/reverse process)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/diffusion-models-ddpm/diffusion-models-ddpm)
6. ✅ [Score-Based & SDE Diffusion (score matching · probability-flow ODE)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/score-based-and-sde-diffusion/score-based-and-sde-diffusion)
7. ✅ [Latent Diffusion & Stable Diffusion (VAE + U-Net + text)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/latent-diffusion-stable-diffusion/latent-diffusion-stable-diffusion)

### Energy-based models & systems
9. ✅ [Energy-Based Models (EBM · contrastive divergence)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/energy-based-models/energy-based-models)
11. ✅ [Text-to-Image Systems (DALL·E · Imagen · CLIP guidance)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/text-to-image-systems/text-to-image-systems)

### Sampling, guidance & evaluation
12. ✅ [Evaluation of Generative Models (FID · Inception Score · precision/recall)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/evaluation-of-generative-models/evaluation-of-generative-models)
13. ✅ [Sampling & Guidance Techniques (DDIM · ancestral · guidance scale)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/sampling-and-guidance-techniques/sampling-and-guidance-techniques)

### Related concepts (covered in another section)
> These topics are foundational or live in another domain, so they're kept in one place to avoid repetition.
- **Autoencoders (plain / denoising / sparse)** — the deterministic precursor to the VAE → [Deep Learning · Autoencoders](/ai-ml/ai-ml-learning-resources/deep-learning/neural-architectures/autoencoders/autoencoders)
- **LLM text generation & autoregressive language models** — GPT-style next-token generation → [LLMs](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme)
- **Decoding strategies for text** (greedy · beam · top-k · top-p) → [NLP · Decoding Strategies](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/natural-language-processing/decoding-strategies/decoding-strategies)
- **Gaussian Mixture Models & the EM algorithm** — the classic latent-variable model → [Unsupervised Learning · GMM & EM](/ai-ml/ai-ml-learning-resources/core-machine-learning/unsupervised-learning/clustering/gaussian-mixture-models-and-em/gaussian-mixture-models-and-em)
- **Information theory** (entropy · cross-entropy · KL divergence) — the objective under every likelihood model → [Foundations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme)

## 🎓 Courses (free)
- [How Diffusion Models Work](https://www.deeplearning.ai/short-courses/how-diffusion-models-work/) — **DeepLearning.AI** — free short course, build one.
- [Hugging Face Diffusion Models Course](https://huggingface.co/learn/diffusion-course) — **Hugging Face** — free, code-first.

## 🎥 Videos
- [Diffusion models from scratch in PyTorch](https://www.youtube.com/watch?v=a4Yfz2FxXiY) — **DeepFindr** — implement DDPM end to end.
- [Variational Autoencoders](https://www.youtube.com/watch?v=9zKuYvjFFS8) — **Arxiv Insights** — the best VAE intro.

## 📄 Key Papers
- [DDPM (Denoising Diffusion Probabilistic Models)](https://arxiv.org/abs/2006.11239) — **Ho et al. (2020)** — the modern diffusion formulation.
- [High-Resolution Image Synthesis with Latent Diffusion](https://arxiv.org/abs/2112.10752) — **Rombach et al. (2022)** — Stable Diffusion.
- [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661) — **Goodfellow et al. (2014)** — the GAN that started it.

## 📰 Articles
- [What are Diffusion Models? (Lil'Log)](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) — **Lilian Weng** — the canonical math walkthrough.
- [The Annotated Diffusion Model](https://huggingface.co/blog/annotated-diffusion) — **Hugging Face** — runnable code + math.

## 🔗 In this platform
- Math: [ai-ml-intuitions Module 5 (Generation)](../../../ai-ml-intuitions/generation/)
