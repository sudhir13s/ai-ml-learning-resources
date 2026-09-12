---
id: "10-generative-ai/evaluation"
topic: "Evaluation of Generative Models"
parent: "10-generative-ai"
level: advanced
built_from: ["gans-dcgan", "multivariate-gaussian", "kl-divergence", "cnns"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 10
title: "Evaluation of Generative Models"
minutes: 10
category: generative-models
---

# Evaluation of Generative Models — FID · Inception Score
> Likelihood doesn't exist (GANs) or doesn't correlate with sample quality, so we evaluate generative
> models with **feature-space statistics**. **Inception Score (IS)** rewards confident, diverse
> ImageNet classifications. **Fréchet Inception Distance (FID)** fits Gaussians to Inception features
> of real vs. generated images and measures the Fréchet distance between them — lower is better, and
> it captures *both* fidelity and diversity. **Precision/Recall** disentangles the two.

**Why it matters:** "how do you know your generator is good?" is asked of every GAN/diffusion
candidate. Interviews probe: why we can't just use log-likelihood; how IS works and its flaws (no
comparison to real data, blind to mode collapse within a class, ImageNet-biased); the **FID** formula
`‖μ_r − μ_g‖² + Tr(Σ_r + Σ_g − 2(Σ_r Σ_g)^½)` and why it's the field standard (sensitive to mode
collapse and blur, but biased by sample size); the **precision (fidelity) vs. recall (coverage)** split
that a single number hides; and **CLIP-score** for text-to-image prompt alignment.

**⭐ Start here — suggested path:**

1. **Build intuition** — watch [Lecture 13 — Generative Models (CS231n)](https://www.youtube.com/watch?v=5WoItGTWV54) — **Stanford University School of Engineering**. *Why likelihood is unavailable or misleading for these models, which is the reason likelihood-free metrics exist at all.*
2. **See the metric in the field's own use** — read [How to Evaluate GANs using FID](https://wandb.ai/ayush-thakur/gan-evaluation/reports/How-to-Evaluate-GANs-using-Frechet-Inception-Distance-FID---Vmlldzo0MTAxOTc) — **Weights & Biases**. *Inception-feature Gaussians, the Fréchet distance, and IS side by side with plots.*
3. **Get the math** — watch [Lecture 20: Generative Models II (EECS 498)](https://www.youtube.com/watch?v=igP03FXZqgo) — **Michigan Online (Justin Johnson)**. *Sample quality, mode coverage, and why a single scalar cannot capture both.*
4. **Read the sources** — [Improved Techniques for Training GANs (IS)](https://arxiv.org/abs/1606.03498) → [GANs Trained by a Two Time-Scale Update Rule (FID)](https://arxiv.org/abs/1706.08500) → [Improved Precision and Recall Metric](https://arxiv.org/abs/1904.06991). *IS, then FID, then the precision/recall refinement.*
5. **Learn where FID lies** — read [The Role of ImageNet Classes in Fréchet Inception Distance](https://arxiv.org/abs/2203.06026) → [Rethinking FID (CMMD)](https://arxiv.org/abs/2401.09603). *FID's Gaussian assumption, its ImageNet-class bias, its bias with small sample counts, and the CLIP-feature MMD alternative proposed in 2024.*
6. **Make it concrete** — compute FID with [`pytorch-fid`](https://github.com/mseitzer/pytorch-fid) on your own samples. *Watching FID drop as samples improve makes it tangible — and watching it disagree with your eyes makes the critique concrete.*

## Courses (free)
- [Google — GANs: Evaluation & Common Problems](https://developers.google.com/machine-learning/gan/problems) — **Google** — free; FID/IS and the failure modes they detect (mode collapse, blur).
- [Stanford CS236 — Deep Generative Models](https://deepgenerativemodels.github.io/) — **Stanford (Ermon)** — free notes; the evaluation lecture covers likelihood-free metrics.

## Videos
- [Lecture 13 — Generative Models (CS231n)](https://www.youtube.com/watch?v=5WoItGTWV54) — **Stanford University School of Engineering** — frames why generative-model evaluation is hard and where likelihood-free metrics come from.
- [Lecture 20: Generative Models II (EECS 498)](https://www.youtube.com/watch?v=igP03FXZqgo) — **Michigan Online (Justin Johnson)** — fidelity vs coverage as separate axes, which is the whole argument for precision/recall metrics.
- [DDPM — Diffusion Models Beat GANs on Image Synthesis (Paper Explained)](https://www.youtube.com/watch?v=W-O7AZNzbzQ) — **Yannic Kilcher** — uses FID as the head-to-head yardstick; shows how the field actually compares models.
- [Stanford CS236: Deep Generative Models (full lecture series)](https://www.youtube.com/playlist?list=PLoROMvodv4rPOWA-omMM6STXaWW4FvJT8) — **Stanford Online (Stefano Ermon)** — the evaluation lecture in the context of the whole generative-model taxonomy.

## Key Papers
- [Improved Techniques for Training GANs](https://arxiv.org/abs/1606.03498) — **Salimans et al. (2016)** — introduces the **Inception Score**.
- [GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium](https://arxiv.org/abs/1706.08500) — **Heusel et al. (2017)** — introduces **FID** (and TTUR).
- [Improved Precision and Recall Metric for Assessing Generative Models](https://arxiv.org/abs/1904.06991) — **Kynkäänniemi et al. (2019)** — separates fidelity (precision) from coverage (recall).
- [The Role of ImageNet Classes in Fréchet Inception Distance](https://arxiv.org/abs/2203.06026) — **Kynkäänniemi et al. (2023)** — FID is measurably steerable by matching ImageNet class histograms; a direct attack on its use as a ranking metric.
- [Rethinking FID: Towards a Better Evaluation Metric for Image Generation](https://arxiv.org/abs/2401.09603) — **Jayasumana et al. (2024)** — the Gaussian assumption, sample-size bias, and Inception's blind spots; proposes CMMD (CLIP features + maximum mean discrepancy).

## Articles / Blogs (free, no paywall)
- [How to Implement the Fréchet Inception Distance (FID) from Scratch](https://machinelearningmastery.com/how-to-implement-the-frechet-inception-distance-fid-from-scratch/) — **Jason Brownlee** — the FID computation with runnable code.
- [How to Evaluate GANs using Fréchet Inception Distance (FID)](https://wandb.ai/ayush-thakur/gan-evaluation/reports/How-to-Evaluate-GANs-using-Frechet-Inception-Distance-FID---Vmlldzo0MTAxOTc) — **Weights & Biases** — IS and FID side by side, with plots, free.
- [FID: Fréchet Inception Distance](https://strikingloo.github.io/wiki/fid) — **Luciano Strika** — a concise, math-first explainer of the FID formula.

## Books (free, with chapters)
- [Probabilistic Machine Learning: Advanced Topics — **Ch. 26 "Evaluating generative models"**](https://probml.github.io/pml-book/book2.html) — **Kevin Murphy** — free PDF; likelihood-free metrics and their pitfalls.
- [Deep Learning — **§20.14 "Evaluating Generative Models"**](https://www.deeplearningbook.org/contents/generative_models.html) — **Goodfellow, Bengio & Courville** — why evaluation is hard and what the metrics measure, free online.

## In this platform
- Prereq: [02 GANs & DCGAN](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/generative-models/gans-and-dcgan/gans-and-dcgan) · [05 Diffusion Models (DDPM)](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/diffusion-models-ddpm/diffusion-models-ddpm) (the models you evaluate)
- Related: [03 GAN Training & WGAN](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/generative-models/gan-training-and-wgan/gan-training-and-wgan) (FID/precision-recall detect mode collapse)
- Compare with: [NLP — Evaluation Metrics (BLEU · perplexity)](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/nlp-evaluation-metrics/nlp-evaluation-metrics) (the text-generation analogue)
- Field overview: [9. Generative AI](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/generative-models/readme)
