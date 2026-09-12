---
id: "multimodal-and-generative-media/audio-and-speech/audio-tokenization-and-neural-codecs"
topic: "Audio Tokenization & Neural Codecs"
level: advanced
built_from: ["audio-representations-waveform-spectrogram-mel-mfcc"]
leads_to: ["multimodal-and-generative-media/audio-and-speech/modern-tts-and-voice-cloning", "multimodal-and-generative-media/audio-and-speech/realtime-and-streaming-voice-agents", "multimodal-and-generative-media/audio-and-speech/music-and-audio-generation-overview"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Audio Tokenization & Neural Codecs"
minutes: 15
category: audio-and-speech
---

# Audio Tokenization & Neural Codecs
> A neural audio codec turns a waveform into a short sequence of **discrete tokens** and back again.
> An encoder downsamples audio to ~12–75 frames per second, a **residual vector quantizer (RVQ)**
> snaps each frame to entries in a stack of codebooks, and a decoder reconstructs the sound. Once
> audio is tokens, a language model can generate it the same way it generates text.

**Why it matters:** discrete audio tokens are the reason 2023–2026 speech and music systems are
transformers rather than bespoke signal-processing pipelines — VALL-E, AudioLM, MusicGen and Moshi
all generate codec tokens. Interviewers probe the split between **semantic tokens** (content, from
a self-supervised speech model) and **acoustic tokens** (timbre and detail, from the codec), why
RVQ needs several codebooks per frame, and the streaming trade-off: a codec that looks ahead sounds
better but cannot run in a live conversation.

**Start here — suggested path:**

1. **Understand discrete latents first** — read [Neural Discrete Representation Learning (VQ-VAE)](https://arxiv.org/abs/1711.00937) — **van den Oord, Vinyals & Kavukcuoglu (2017)**. *The vector-quantization idea every audio codec inherits.*
2. **See the first modern codec** — read [SoundStream: An End-to-End Neural Audio Codec](https://research.google/blog/soundstream-an-end-to-end-neural-audio-codec/) — **Google Research**. *The authors' own explanation of RVQ and why one model can serve many bitrates.*
3. **Read the workhorse** — read [High Fidelity Neural Audio Compression (EnCodec)](https://arxiv.org/abs/2210.13438) — **Défossez et al. (2022)**. *The codec most open audio language models actually use, plus its adversarial and reconstruction losses.*
4. **Get the two-token-type picture** — read [AudioLM](https://arxiv.org/abs/2209.03143) — **Borsos et al. (2022)**. *Where the semantic-versus-acoustic token split is introduced and justified.*
5. **See the 2025–26 streaming state of the art** — read [Moshi (and its Mimi codec)](https://arxiv.org/abs/2410.00037) — **Défossez et al., Kyutai (2024)**. *A 12.5 Hz, 1.1 kbps fully streaming codec with 80 ms latency, built for live dialogue.*

## Courses (free)
- [Hugging Face Audio Course — Unit 3: Transformer architectures for audio](https://huggingface.co/learn/audio-course/chapter3/introduction) — **Hugging Face** — free; how audio sequences are fed to transformers, the step before token-based generation.
- [CS224S — Spoken Language Processing](https://web.stanford.edu/class/cs224s/) — **Stanford** — public slides covering discrete speech units and speech language models.

## Key Papers
- [SoundStream: An End-to-End Neural Audio Codec](https://arxiv.org/abs/2107.03312) — **Zeghidour et al. (2021)** — introduced residual vector quantization for audio; the template every later codec follows.
- [High Fidelity Neural Audio Compression (EnCodec)](https://arxiv.org/abs/2210.13438) — **Défossez, Copet, Synnaeve & Adi (2022)** — streaming encoder-decoder plus a transformer entropy model; the default open codec.
- [High-Fidelity Audio Compression with Improved RVQGAN (Descript Audio Codec)](https://arxiv.org/abs/2306.06546) — **Kumar et al. (2023)** — 90× compression of 44.1 kHz audio and a drop-in EnCodec replacement; fixes codebook collapse.
- [AudioLM: A Language Modeling Approach to Audio Generation](https://arxiv.org/abs/2209.03143) — **Borsos et al. (2022)** — the semantic-plus-acoustic token hierarchy that made audio language models work.
- [Moshi: A Speech-Text Foundation Model for Real-Time Dialogue](https://arxiv.org/abs/2410.00037) — **Défossez et al., Kyutai (2024)** — the Mimi streaming codec: 12.5 Hz frames, 1.1 kbps, distilled semantic tokens inside an acoustic codec.
- [Recent Advances in Discrete Speech Tokens: A Review](https://arxiv.org/abs/2502.06490) — **Guo et al. (2025)** — the current map of semantic, acoustic and hybrid tokenizers with their trade-offs.

## Articles / Blogs (free, no paywall)
- [SoundStream: An End-to-End Neural Audio Codec](https://research.google/blog/soundstream-an-end-to-end-neural-audio-codec/) — **Google Research** — the authors' walkthrough of RVQ, quantizer dropout and scalable bitrates.
- [EnCodec — reference implementation](https://github.com/facebookresearch/encodec) — **Meta FAIR** — runnable code and pretrained models; reading the quantizer is worth an hour.
- [Descript Audio Codec — reference implementation](https://github.com/descriptinc/descript-audio-codec) — **Descript** — clean, well-documented RVQ-GAN training code for speech, music and general audio.
- [Moshi and Mimi — reference implementation](https://github.com/kyutai-labs/moshi) — **Kyutai** — PyTorch, MLX and Rust implementations of a production streaming codec and speech-text model.
- [Towards Audio Language Modeling — an overview](https://arxiv.org/abs/2402.13236) — **Wu et al. (2024)** — a compact survey of codecs and the language models built on them.

## In this platform
- Prerequisite: [Audio Representations](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/audio-representations-waveform-spectrogram-mel-mfcc/audio-representations-waveform-spectrogram-mel-mfcc)
- The text analogue of this idea: [Tokenization & Subword Algorithms](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/tokenization-and-subword-algorithms/tokenization-and-subword-algorithms)
- Next: [Modern TTS & Voice Cloning](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/modern-tts-and-voice-cloning/modern-tts-and-voice-cloning) · [Realtime & Streaming Voice Agents](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/realtime-and-streaming-voice-agents/realtime-and-streaming-voice-agents) · [Music & Audio Generation](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/music-and-audio-generation-overview/music-and-audio-generation-overview)
- Sub-area index: [Audio & Speech](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/readme)
