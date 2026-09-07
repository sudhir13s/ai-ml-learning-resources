---
id: "modalities-and-generative-models/audio-and-speech/tts-fundamentals-tacotron-vits-vocoders"
topic: "TTS Fundamentals — Tacotron, VITS and Vocoders"
level: intermediate
built_from: ["audio-representations-waveform-spectrogram-mel-mfcc", "sequence-to-sequence-and-encoder-decoder"]
leads_to: ["modalities-and-generative-models/audio-and-speech/modern-tts-and-voice-cloning"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 15
title: "TTS Fundamentals — Tacotron, VITS and Vocoders"
minutes: 15
category: audio-and-speech
---

# TTS Fundamentals — Tacotron, VITS and Vocoders
> Classical neural text-to-speech (TTS) is two models in a row: an **acoustic model** turns text
> into a mel spectrogram, and a **vocoder** turns that spectrogram into a waveform. **Tacotron 2**
> is the attention-based acoustic model, **FastSpeech 2** the non-autoregressive one with an
> explicit duration predictor, **HiFi-GAN** the vocoder that made this real-time, and **VITS**
> collapses both stages into a single end-to-end variational model.

**Why it matters:** the two-stage split explains almost every TTS failure you will hear — a
skipped or repeated word is an attention failure in the acoustic model, a buzzy or metallic voice
is a vocoder failure. Interviewers probe why autoregressive attention TTS is unstable on long or
unusual text (and how duration prediction fixes it), why generating 24,000 samples per second
directly is hard (WaveNet's answer, and why it was too slow), and where prosody actually comes
from in each design.

**Start here — suggested path:**

1. **Hear the problem** — read [WaveNet: A Generative Model for Raw Audio](https://deepmind.google/discover/blog/wavenet-a-generative-model-for-raw-audio/) — **DeepMind**. *Samples first: what modeling the waveform directly bought, and what it cost in speed.*
2. **Learn the standard pipeline** — read [Natural TTS Synthesis by Conditioning WaveNet on Mel Spectrogram Predictions (Tacotron 2)](https://arxiv.org/abs/1712.05884) — **Shen et al. (2017)**. *The acoustic-model-plus-vocoder architecture that defined the field, with audio samples on the [project page](https://google.github.io/tacotron/publications/tacotron2/).*
3. **See the deep dive** — watch [ML for Audio Study Group — Text to Speech Deep Dive](https://www.youtube.com/watch?v=aLBedWj-5CQ) — **Hugging Face**. *A practitioner walk through the whole stack: text front end, acoustic model, vocoder.*
4. **Get the textbook version** — read [*Speech and Language Processing*, Ch. 16](https://web.stanford.edu/~jurafsky/slp3/16.pdf) — **Jurafsky & Martin**. *Text normalization, grapheme-to-phoneme, and TTS evaluation (mean opinion score) done properly.*
5. **Build one** — do [Hugging Face Audio Course, Unit 6: From text to speech](https://huggingface.co/learn/audio-course/chapter6/introduction) — **Hugging Face**. *Fine-tune a real TTS model and listen to what each component contributes.*

## Courses (free)
- [Hugging Face Audio Course — Unit 6: From text to speech](https://huggingface.co/learn/audio-course/chapter6/introduction) — **Hugging Face** — free and hands-on; the acoustic model and vocoder made concrete.
- [Pre-trained models for text-to-speech](https://huggingface.co/learn/audio-course/chapter6/pre-trained_models) — **Hugging Face** — compares SpeechT5, Bark and MMS-TTS, so the architecture choices become audible.
- [CS224S — Spoken Language Processing](https://web.stanford.edu/class/cs224s/) — **Stanford** — the university treatment of speech synthesis alongside recognition.

## Videos
- [ML for Audio Study Group — Text to Speech Deep Dive](https://www.youtube.com/watch?v=aLBedWj-5CQ) — **Hugging Face** — the clearest free overview of the full TTS stack and where each model fits.

## Key Papers
- [WaveNet: A Generative Model for Raw Audio](https://arxiv.org/abs/1609.03499) — **van den Oord et al. (2016)** — dilated causal convolutions over raw samples; the quality jump that started modern TTS.
- [Natural TTS Synthesis by Conditioning WaveNet on Mel Spectrogram Predictions (Tacotron 2)](https://arxiv.org/abs/1712.05884) — **Shen et al. (2017)** — the reference acoustic model, and the mel spectrogram as the interface between stages.
- [FastSpeech 2: Fast and High-Quality End-to-End Text to Speech](https://arxiv.org/abs/2006.04558) — **Ren et al. (2020)** — non-autoregressive with explicit duration, pitch and energy; removes the attention failure modes.
- [HiFi-GAN: Generative Adversarial Networks for Efficient and High Fidelity Speech Synthesis](https://arxiv.org/abs/2010.05646) — **Kong, Kim & Bae (2020)** — the vocoder that made neural TTS real-time on CPU; multi-period discriminators.
- [VITS: Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech](https://arxiv.org/abs/2106.06103) — **Kim, Kong & Son (2021)** — one model, no separate vocoder, with a stochastic duration predictor for natural rhythm.

## Articles / Blogs (free, no paywall)
- [WaveNet: A generative model for raw audio](https://deepmind.google/discover/blog/wavenet-a-generative-model-for-raw-audio/) — **DeepMind** — the authors' post; listen to the samples before reading any equation.
- [Tacotron 2 audio samples](https://google.github.io/tacotron/publications/tacotron2/) — **Google (Tacotron team)** — side-by-side samples that make the acoustic-model-versus-vocoder split audible.
- [Coqui TTS — open-source toolkit](https://github.com/coqui-ai/TTS) — **Coqui** — reference implementations of Tacotron 2, VITS and vocoders you can train and read.

## Books (free, with chapters)
- [*Speech and Language Processing* — Ch. 16 "Automatic Speech Recognition and Text-to-Speech"](https://web.stanford.edu/~jurafsky/slp3/16.pdf) — **Jurafsky & Martin** — free draft; text normalization, the TTS front end, and evaluation.

## In this platform
- Prerequisites: [Audio Representations](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/audio-representations-waveform-spectrogram-mel-mfcc/audio-representations-waveform-spectrogram-mel-mfcc) — the mel spectrogram is the interface between the two stages · [Sequence-to-Sequence & Encoder-Decoder](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/natural-language-processing/sequence-to-sequence-and-encoder-decoder/sequence-to-sequence-and-encoder-decoder)
- Next: [Modern TTS & Voice Cloning](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/modern-tts-and-voice-cloning/modern-tts-and-voice-cloning)
- Sub-area index: [Audio & Speech](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/readme)
