---
id: "multimodal-and-generative-media/audio-and-speech/music-and-audio-generation-overview"
topic: "Music & Audio Generation — Overview"
level: intermediate
built_from: ["audio-tokenization-and-neural-codecs"]
leads_to: []
interview_frequency: low
updated: 2026-09-07
tier: core
est_minutes: 13
title: "Music & Audio Generation — Overview"
minutes: 13
category: audio-and-speech
---

# Music & Audio Generation — Overview
> Text-to-music and text-to-audio split into two families. **Codec language models** (AudioLM,
> MusicLM, MusicGen) generate discrete audio tokens autoregressively and decode them with a neural
> codec. **Latent diffusion** models (Stable Audio) denoise in the continuous latent space of an
> autoencoder, conditioned on a text embedding, which makes long stereo output at 44.1 kHz
> practical.

**Why it matters:** music is the honest stress test for audio generation — it needs long-range
structure (minutes, not seconds), stereo, and 44.1 kHz fidelity, so every weakness in a codec or a
sampler shows up immediately. Interviewers probe the token-versus-latent trade (autoregressive
quality and control versus diffusion speed and length), how conditioning works when paired
text-music data is scarce (joint embedding models such as MuLan and CLAP), and why evaluation is
unsolved: Fréchet Audio Distance correlates only loosely with what listeners prefer.

**Start here — suggested path:**

1. **Get the intuition for raw audio** — read [Generating music in the waveform domain](https://sander.ai/2020/03/24/audio-generation.html) — **Sander Dieleman (DeepMind)**. *Why audio is hard: sample rates, perceptual irrelevance, and the case for modeling in a learned space.*
2. **See the token approach** — read [AudioLM](https://arxiv.org/abs/2209.03143) — **Borsos et al., Google (2022)**. *Semantic tokens for structure, acoustic tokens for fidelity; the hierarchy every codec LM reuses.*
3. **Read the open workhorse** — read [Simple and Controllable Music Generation (MusicGen)](https://arxiv.org/abs/2306.05284) — **Copet et al., Meta (2023)**. *A single-stage transformer over interleaved codebooks, with melody conditioning; the model most people can actually run.*
4. **Contrast with diffusion** — read [Fast Timing-Conditioned Latent Audio Diffusion (Stable Audio)](https://arxiv.org/abs/2402.04825) — **Evans et al., Stability AI (2024)**. *Timing conditioning for variable-length stereo output; where diffusion wins.*
5. **Watch the researcher's talk** — watch [Generating music in the raw audio domain](https://www.youtube.com/watch?v=y8mOZSJA7Bc) — **Sander Dieleman**, at the **London Machine Learning Meetup**. *The design considerations behind all of the above, from someone who built them.*

## Courses (free)
- [Deep Learning (for Audio) with Python](https://www.youtube.com/playlist?list=PL-wATfeyAMNrtbkCNsLcpoAyBBRJZVlnf) — **Valerio Velardo - The Sound of AI** — free ground-up course from a music-AI practitioner; the on-ramp to generative audio.
- [Hugging Face Audio Course — Unit 3: Transformer architectures for audio](https://huggingface.co/learn/audio-course/chapter3/introduction) — **Hugging Face** — free; how sequence models are applied to audio, which is the shared substrate here.

## Videos
- [Sander Dieleman: Generating music in the raw audio domain](https://www.youtube.com/watch?v=y8mOZSJA7Bc) — **London Machine Learning Meetup** — a leading audio-generation researcher on why the representation choice decides everything.

## Key Papers
- [AudioLM: A Language Modeling Approach to Audio Generation](https://arxiv.org/abs/2209.03143) — **Borsos et al. (2022)** — semantic plus acoustic tokens; long-term coherence without any symbolic representation.
- [MusicLM: Generating Music From Text](https://arxiv.org/abs/2301.11325) — **Agostinelli et al., Google (2023)** — text-conditioned music via a joint text-music embedding; the first convincing text-to-music.
- [Simple and Controllable Music Generation (MusicGen)](https://arxiv.org/abs/2306.05284) — **Copet et al., Meta (2023)** — one-stage codebook interleaving, open weights and code; the practical baseline.
- [AudioGen: Textually Guided Audio Generation](https://arxiv.org/abs/2209.15352) — **Kreuk et al., Meta (2022)** — sound effects and environmental audio rather than music; the same recipe, different data.
- [Fast Timing-Conditioned Latent Audio Diffusion (Stable Audio)](https://arxiv.org/abs/2402.04825) — **Evans et al., Stability AI (2024)** — latent diffusion with timing conditioning for variable-length stereo.
- [Stable Audio Open](https://arxiv.org/abs/2407.14358) — **Evans et al., Stability AI (2024)** — an openly licensed text-to-audio model trained only on Creative Commons data; the reproducible reference.
- [Fréchet Audio Distance: A Metric for Evaluating Music Enhancement Algorithms](https://arxiv.org/abs/1812.08466) — **Kilgour et al., Google (2018)** — the standard generative-audio metric, and its limits.
- [Jukebox: A Generative Model for Music](https://arxiv.org/abs/2005.00341) — **Dhariwal et al., OpenAI (2020)** — hierarchical VQ-VAE over raw audio with vocals; historically important, and a lesson in cost.

## Articles / Blogs (free, no paywall)
- [Generating music in the waveform domain](https://sander.ai/2020/03/24/audio-generation.html) — **Sander Dieleman** — the definitive free essay on why audio generation is structured the way it is.
- [Diffusion is spectral autoregression](https://sander.ai/2024/09/02/spectral-autoregression.html) — **Sander Dieleman** — a frequency-domain reading of diffusion that connects directly to audio representations.
- [AudioLM: a language modeling approach to audio generation](https://research.google/blog/audiolm-a-language-modeling-approach-to-audio-generation/) — **Google Research** — the authors' post, with the samples that make the two-token-type argument.
- [AudioCraft (MusicGen, AudioGen, EnCodec)](https://github.com/facebookresearch/audiocraft) — **Meta FAIR** — training and inference code for the open models above.
- [*Fundamentals of Music Processing* — FMP notebooks](https://www.audiolabs-erlangen.de/resources/MIR/FMP/C0/C0.html) — **Meinard Müller** — free executable book on music representations, the background this field assumes.

## In this platform
- Prerequisite: [Audio Tokenization & Neural Codecs](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/audio-tokenization-and-neural-codecs/audio-tokenization-and-neural-codecs)
- Diffusion mechanics live with their owner: [Diffusion Models](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/readme) · [Sampling & Guidance Techniques](/ai-ml/ai-ml-learning-resources/models-and-architectures/generative-model-families/diffusion-models/sampling-and-guidance-techniques/sampling-and-guidance-techniques)
- Representation background: [Audio Representations](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/audio-representations-waveform-spectrogram-mel-mfcc/audio-representations-waveform-spectrogram-mel-mfcc)
- Sub-area index: [Audio & Speech](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/readme)
