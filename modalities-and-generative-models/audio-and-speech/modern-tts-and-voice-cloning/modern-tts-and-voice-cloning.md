---
id: "modalities-and-generative-models/audio-and-speech/modern-tts-and-voice-cloning"
topic: "Modern TTS & Voice Cloning"
level: advanced
built_from: ["tts-fundamentals-tacotron-vits-vocoders", "audio-tokenization-and-neural-codecs"]
leads_to: ["modalities-and-generative-models/audio-and-speech/realtime-and-streaming-voice-agents"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Modern TTS & Voice Cloning"
minutes: 15
category: audio-and-speech
---

# Modern TTS & Voice Cloning
> Since 2023 the dominant recipe is **text-to-speech as language modeling**: encode a few seconds
> of reference audio into codec tokens, prepend them plus the text as a prompt, and let a
> transformer continue the token sequence in that voice. **VALL-E** framed it; **XTTS**,
> **F5-TTS**, **Kokoro** and **Chatterbox** made it open, multilingual and small enough to run on a
> laptop. Zero-shot voice cloning from ~5 seconds is now a commodity — which is exactly the problem.

**Why it matters:** this is where TTS interviews go in 2026 — in-context learning for voices, the
autoregressive-versus-flow-matching split (VALL-E's codec LM versus F5-TTS's non-autoregressive
flow matching), and the engineering trade of quality against latency and licence. It is also the
clearest consent-and-safety question in applied audio: watermarking, spoofing detection and
speaker-consent verification are part of the system design, not an afterthought.

**Start here — suggested path:**

1. **Learn the prompting reframe** — read [VALL-E: Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers](https://arxiv.org/abs/2301.02111) — **Wang et al., Microsoft (2023)**. *Treating TTS as next-token prediction over EnCodec tokens; the autoregressive-plus-non-autoregressive two-stage decoder.*
2. **Contrast the non-autoregressive branch** — read [F5-TTS](https://arxiv.org/abs/2410.06885) — **Chen et al. (2024)**. *Flow matching with a diffusion transformer, no duration model, no explicit alignment — the other half of the field.*
3. **See what open models look like now** — read the [Kokoro-82M model card](https://huggingface.co/hexgrad/Kokoro-82M) — **hexgrad** and [Chatterbox](https://github.com/resemble-ai/chatterbox) — **Resemble AI**. *82M parameters on CPU, and a permissively licensed cloning model with emotion control.*
4. **Understand multilinguality** — read [XTTS](https://arxiv.org/abs/2406.04904) — **Casanova et al., Coqui (2024)**. *Zero-shot cloning across 16 languages, and what breaks in low-resource ones.*
5. **Take the safety half seriously** — read [Proactive Detection of Voice Cloning with Localized Watermarking (AudioSeal)](https://arxiv.org/abs/2401.17264) — **San Roman et al., Meta (2024)** and browse [ASVspoof](https://www.asvspoof.org/). *Watermarking and anti-spoofing, the two defenses that actually ship.*

## Courses (free)
- [Hugging Face Audio Course — Unit 6: From text to speech](https://huggingface.co/learn/audio-course/chapter6/introduction) — **Hugging Face** — free; the practical baseline this page builds past.
- [Pre-trained models for text-to-speech](https://huggingface.co/learn/audio-course/chapter6/pre-trained_models) — **Hugging Face** — hands-on comparison of modern open TTS checkpoints.

## Videos
- [ML for Audio Study Group — Text to Speech Deep Dive](https://www.youtube.com/watch?v=aLBedWj-5CQ) — **Hugging Face** — the stack view that makes the shift from acoustic models to codec language models legible.

## Key Papers
- [VALL-E: Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers](https://arxiv.org/abs/2301.02111) — **Wang et al. (2023)** — the paper that turned TTS into in-context learning over audio tokens.
- [VALL-E 2: Human Parity Zero-Shot Text to Speech](https://arxiv.org/abs/2406.05370) — **Chen et al. (2024)** — repetition-aware sampling and grouped codec modeling; the fixes for the original's instability.
- [Voicebox: Text-Guided Multilingual Universal Speech Generation at Scale](https://arxiv.org/abs/2306.15687) — **Le et al., Meta (2023)** — flow matching with infilling; editing and denoising as the same objective.
- [NaturalSpeech 3: Zero-Shot Speech Synthesis with Factorized Codec and Diffusion Models](https://arxiv.org/abs/2403.03100) — **Ju et al. (2024)** — factorizes content, prosody, timbre and acoustic detail into separate token streams.
- [XTTS: A Massively Multilingual Zero-Shot Text-to-Speech Model](https://arxiv.org/abs/2406.04904) — **Casanova et al. (2024)** — 16 languages including low-resource ones; the open multilingual reference.
- [F5-TTS: A Fairytaler that Fakes Fluent and Faithful Speech with Flow Matching](https://arxiv.org/abs/2410.06885) — **Chen et al. (2024)** — non-autoregressive flow matching; fast inference without a duration predictor.
- [Proactive Detection of Voice Cloning with Localized Watermarking (AudioSeal)](https://arxiv.org/abs/2401.17264) — **San Roman et al., Meta (2024)** — sample-level watermark detection robust to editing; the defense to know.

## Articles / Blogs (free, no paywall)
- [Kokoro-82M model card](https://huggingface.co/hexgrad/Kokoro-82M) — **hexgrad** — an 82M-parameter, Apache-licensed TTS model that runs on CPU; the efficiency end of the field.
- [Chatterbox](https://github.com/resemble-ai/chatterbox) — **Resemble AI** — MIT-licensed zero-shot cloning with an exaggeration control and a built-in watermark.
- [Parler-TTS](https://github.com/huggingface/parler-tts) — **Hugging Face** — fully open training code and data recipes; describe the voice you want in natural language.
- [Coqui TTS](https://github.com/coqui-ai/TTS) — **Coqui** — the reference open implementation of XTTS and its cloning interface.
- [ASVspoof challenge](https://www.asvspoof.org/) — **ASVspoof consortium** — the community benchmark for spoofed-speech detection; datasets and baselines are free.

## In this platform
- Prerequisites: [TTS Fundamentals](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/tts-fundamentals-tacotron-vits-vocoders/tts-fundamentals-tacotron-vits-vocoders) · [Audio Tokenization & Neural Codecs](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/audio-tokenization-and-neural-codecs/audio-tokenization-and-neural-codecs)
- Sampling controls carry over from text: [Decoding Strategies](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/natural-language-processing/decoding-strategies/decoding-strategies)
- Flow matching and diffusion background: [Diffusion Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/readme)
- Next: [Realtime & Streaming Voice Agents](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/realtime-and-streaming-voice-agents/realtime-and-streaming-voice-agents)
- Sub-area index: [Audio & Speech](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/readme)
