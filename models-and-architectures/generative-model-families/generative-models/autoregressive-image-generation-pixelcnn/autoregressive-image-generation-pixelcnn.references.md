---
id: "10-generative-ai/autoregressive-pixelcnn/references"
topic: "Autoregressive Image Generation (PixelCNN) — References"
parent: "10-generative-ai/autoregressive-pixelcnn"
type: references
updated: 2026-09-14
---

# Autoregressive Image Generation — PixelRNN · PixelCNN — references

> Companion link library for **[Autoregressive Image Generation — PixelRNN · PixelCNN](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/generative-models/autoregressive-image-generation-pixelcnn/autoregressive-image-generation-pixelcnn)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Build intuition** — watch [Lecture 19: Generative Models I (EECS 498)](https://www.youtube.com/watch?v=Q3HU2vEhD5Y) — **Michigan Online (Justin Johnson)**. *Explicit-density models framed first, with PixelRNN/PixelCNN as the tractable-likelihood branch.*
2. **See why it works** — read [Blog: Autoregressive Models — PixelCNN](https://bjlkeng.io/posts/pixelcnn/) — **Brian Keng**. *Masked convolutions, the blind spot, and the gated fix, with code.*
3. **Get the math** — watch [L2 Autoregressive Models — CS294-158](https://www.youtube.com/watch?v=iyEOk8KCRUw) — **Pieter Abbeel (Berkeley)**. *MADE → WaveNet → PixelCNN(++); the chain-rule factorization and masking, rigorously.*
4. **Read the sources** — [Pixel Recurrent Neural Networks](https://arxiv.org/abs/1601.06759) — **van den Oord et al. (2016)** → [Conditional Image Generation with PixelCNN Decoders](https://arxiv.org/abs/1606.05328) — **van den Oord et al. (2016)**. *PixelRNN/PixelCNN, then the gated, conditional version.*
5. **Make it concrete** — work through [UvA DL — Autoregressive Image Modeling](https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial12/Autoregressive_Image_Modeling.html). *Coding masked convs and sampling pixel-by-pixel cements it.*

**In this platform**:
- Compare with: [08 Normalizing Flows](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/generative-models/normalizing-flows/normalizing-flows) (another exact-likelihood model) · [05 Diffusion Models (DDPM)](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/diffusion-models-ddpm/diffusion-models-ddpm)
- Field overview: [9. Generative AI](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/generative-models/readme)
- Concept depth (the *why*): [ai-ml-intuitions 5.05 Autoregressive Generation & Sampling](/ai-ml/ai-ml-intuitions/generation/autoregressive-generation/autoregressive-generation-and-sampling-controls-intuition)
- Prereq: [Deep Learning — CNNs & Convolution](/ai-ml/ai-ml-learning-resources/models-and-architectures/classic-architectures/cnns-and-convolution/cnns-and-convolution) (masked convolutions are the core trick)
- Related (text analogue): [LLMs](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/readme) · [NLP — Decoding Strategies](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/decoding-strategies/decoding-strategies) (sampling from autoregressive conditionals)

**Videos**:
- [Autoregressive Generative Models with Deep Learning](https://www.youtube.com/watch?v=R8fx2b8Asg0) — **Hugo Larochelle (Google Brain)** — the foundations talk (NADE/MADE) by an originator of neural AR models.
- [L2 Autoregressive Models — CS294-158 Deep Unsupervised Learning](https://www.youtube.com/watch?v=iyEOk8KCRUw) — **Pieter Abbeel (Berkeley)** — the rigorous lecture: MADE, WaveNet, PixelCNN(++), self-attention.
- [Lecture 13 — Generative Models](https://www.youtube.com/watch?v=5WoItGTWV54) — **Stanford CS231n** — places PixelRNN/PixelCNN alongside VAEs and GANs in the generative-models lecture.
- [Lecture 19: Generative Models I (EECS 498)](https://www.youtube.com/watch?v=Q3HU2vEhD5Y) — **Michigan Online (Justin Johnson)** — the taxonomy (explicit tractable, explicit approximate, implicit) with PixelRNN/PixelCNN derived in place.

**Courses**:
- [Stanford CS236 — Deep Generative Models](https://deepgenerativemodels.github.io/) — **Stanford (Ermon)** — free notes; the autoregressive-models lecture with the chain-rule view.
- [UC Berkeley CS294-158 — Deep Unsupervised Learning (Autoregressive Models)](https://sites.google.com/view/berkeley-cs294-158-sp20/home) — **Berkeley (Abbeel)** — free; the canonical autoregressive-models lecture (MADE, WaveNet, PixelCNN).

**Articles**:
- [Autoregressive Models — PixelCNN](https://bjlkeng.io/posts/pixelcnn/) — **Brian Keng** — masked convolutions, the blind-spot problem, and the gated fix, with runnable code.
- [PixelCNN](https://sergeiturukin.com/2017/02/22/pixelcnn.html) — **Sergei Turukin** — a focused walkthrough of the masking scheme and the architecture.
- [UvA DL — Autoregressive Image Modeling](https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/tutorial12/Autoregressive_Image_Modeling.html) — **University of Amsterdam** — runnable PixelCNN notebook with the exact-NLL objective.

**Papers**:
- [Autoregressive Model Beats Diffusion: Llama for Scalable Image Generation (LlamaGen)](https://arxiv.org/abs/2406.06525) — **Sun et al. (2024)** — a plain LLM stack over discrete image tokens; the 2024–26 case that the tokenizer, not the architecture, was the bottleneck.
- [Conditional Image Generation with PixelCNN Decoders](https://arxiv.org/abs/1606.05328) — **van den Oord et al. (2016)** — gated PixelCNN that fixes the blind spot and adds conditioning.
- [Pixel Recurrent Neural Networks](https://arxiv.org/abs/1601.06759) — **van den Oord, Kalchbrenner & Kavukcuoglu (2016)** — PixelRNN/PixelCNN; the autoregressive image-modeling formulation.
- [PixelCNN++](https://arxiv.org/abs/1701.05517) — **Salimans et al. (2017)** — a discretized-logistic-mixture likelihood and other improvements.
- [Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction (VAR)](https://arxiv.org/abs/2404.02905) — **Tian et al. (2024)** — predicts coarse-to-fine scales instead of raster-order pixels; the change that made autoregressive image models competitive with diffusion again.

**Books**:
- [Deep Learning — **§20.10.7 "Other Generation Schemes" & §10 (recurrent/seq models)**](https://www.deeplearningbook.org/contents/generative_models.html) — **Goodfellow, Bengio & Courville** — autoregressive generation in context, free online.
- [Probabilistic Machine Learning: Advanced Topics — **Ch. 22 "Autoregressive models"**](https://probml.github.io/pml-book/book2.html) — **Kevin Murphy** — free PDF; the modern treatment of AR generative models.
