---
id: "modalities-and-generative-models/audio-and-speech/speaker-identification-and-diarization"
topic: "Speaker Identification & Diarization"
level: intermediate
built_from: ["audio-representations-waveform-spectrogram-mel-mfcc", "self-supervised-speech-wav2vec2-hubert"]
leads_to: ["modalities-and-generative-models/audio-and-speech/realtime-and-streaming-voice-agents"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Speaker Identification & Diarization"
minutes: 14
category: audio-and-speech
---

# Speaker Identification & Diarization
> Speaker recognition answers *who is speaking*; diarization answers *who spoke when*. The standard
> pipeline segments the audio, embeds each segment into a fixed-length **speaker embedding**
> (x-vector, ECAPA-TDNN), and clusters the embeddings. End-to-end neural diarization (EEND)
> replaces that pipeline with one model that predicts per-speaker activity directly — which is the
> only way to get overlapping speech right.

**Why it matters:** transcription without speaker labels is unusable for meetings, call centres and
medical notes, so diarization sits on top of nearly every real ASR deployment. Interviewers probe
the metric — **diarization error rate (DER)** = missed speech + false alarm + speaker confusion,
and whether overlap is scored at all — plus the two hard cases everyone hits: unknown speaker count
and overlapping speech, which clustering pipelines handle badly by construction.

**Start here — suggested path:**

1. **See the pipeline whole** — read [pyannote.audio 2.1 speaker diarization pipeline: principle, benchmark and recipe](https://www.isca-archive.org/interspeech_2023/bredin23_interspeech.html) — **Hervé Bredin (Interspeech 2023)**. *Segmentation, embedding, clustering — with the recipe for adapting it to your own data.*
2. **Learn the embedding** — read [ECAPA-TDNN](https://arxiv.org/abs/2005.07143) — **Desplanques, Thienpondt & Demuynck (2020)**. *Channel attention, propagation and aggregation; the speaker embedding most systems still use.*
3. **Hear the field's own account** — watch [Speaker diarization, a (love) loss story](https://www.youtube.com/watch?v=CtjDotATEI0) — **Hervé Bredin**, hosted by **Center for Language & Speech Processing (CLSP), JHU**. *A JSALT 2025 plenary: where clustering pipelines break and what the losses should be.*
4. **Understand the end-to-end alternative** — read [End-to-End Neural Speaker Diarization with Permutation-Free Objectives](https://arxiv.org/abs/1909.06247) — **Fujita et al. (2019)**. *Why permutation-invariant training is needed, and how overlap becomes trivial once it is.*
5. **Run it** — use [pyannote/speaker-diarization-3.1](https://huggingface.co/pyannote/speaker-diarization-3.1) — **pyannote**. *An open pretrained pipeline; combine it with a transcript and you have speaker-attributed text.*

## Courses (free)
- [Hugging Face Audio Course — Unit 5: Speech recognition](https://huggingface.co/learn/audio-course/chapter5/introduction) — **Hugging Face** — free; the transcription half that diarization is attached to.
- [CS224S — Spoken Language Processing](https://web.stanford.edu/class/cs224s/) — **Stanford** — public course material covering speaker and conversational speech processing.

## Videos
- [JSALT 2025 Plenary — Speaker diarization, a (love) loss story](https://www.youtube.com/watch?v=CtjDotATEI0) — **Hervé Bredin**, via **CLSP, JHU** — the pyannote author on what diarization losses should optimize; the best single talk on the topic.

## Key Papers
- [X-Vectors: Robust DNN Embeddings for Speaker Recognition](https://www.danielpovey.com/files/2018_icassp_xvectors.pdf) — **Snyder, Garcia-Romero, Sell, Povey & Khudanpur (2018)** — the time-delay network embedding that replaced i-vectors; free PDF from the authors.
- [ECAPA-TDNN: Emphasized Channel Attention, Propagation and Aggregation](https://arxiv.org/abs/2005.07143) — **Desplanques et al. (2020)** — the speaker-verification embedding that is still the default baseline.
- [End-to-End Neural Speaker Diarization with Self-Attention](https://arxiv.org/abs/1909.06247) — **Fujita et al. (2019)** — EEND: permutation-invariant training, overlap handled natively.
- [Powerset Multi-Class Cross Entropy Loss for Neural Speaker Diarization](https://arxiv.org/abs/2310.13025) — **Plaquet & Bredin (2023)** — the loss behind pyannote 3.x; reframes overlap as a single multi-class problem.
- [WavLM: Large-Scale Self-Supervised Pre-Training for Full Stack Speech Processing](https://arxiv.org/abs/2110.13900) — **Chen et al. (2021)** — speaker-aware pretraining; the encoder most modern speaker systems start from.
- [WeSpeaker: A Research and Production Oriented Speaker Embedding Learning Toolkit](https://arxiv.org/abs/2210.17016) — **Wang et al. (2022)** — the open toolkit and its recipe choices, written up honestly.

## Articles / Blogs (free, no paywall)
- [pyannote.audio](https://github.com/pyannote/pyannote-audio) — **Hervé Bredin and contributors** — the reference open diarization toolkit; the pipeline code is short enough to read.
- [SpeechBrain](https://speechbrain.github.io/) — **SpeechBrain team** — recipes for speaker verification, diarization and enhancement with pretrained models.
- [VoxCeleb datasets](https://www.robots.ox.ac.uk/~vgg/data/voxceleb/) — **Oxford VGG** — the benchmark corpora every speaker system reports on, free for research.
- [WhisperX](https://arxiv.org/abs/2303.00747) — **Bain et al. (2023)** — how diarization is glued to Whisper transcripts in practice, with forced alignment.

## In this platform
- Prerequisites: [Audio Representations](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/audio-representations-waveform-spectrogram-mel-mfcc/audio-representations-waveform-spectrogram-mel-mfcc) · [Self-Supervised Speech](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/self-supervised-speech-wav2vec2-hubert/self-supervised-speech-wav2vec2-hubert)
- Pairs with: [Whisper & Weakly-Supervised ASR](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/whisper-and-weakly-supervised-asr/whisper-and-weakly-supervised-asr) — transcription plus diarization is the deployed unit
- Next: [Realtime & Streaming Voice Agents](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/realtime-and-streaming-voice-agents/realtime-and-streaming-voice-agents)
- Sub-area index: [Audio & Speech](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/readme)
