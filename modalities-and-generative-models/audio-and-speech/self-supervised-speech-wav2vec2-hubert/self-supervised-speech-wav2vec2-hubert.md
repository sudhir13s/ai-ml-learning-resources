---
id: "modalities-and-generative-models/audio-and-speech/self-supervised-speech-wav2vec2-hubert"
topic: "Self-Supervised Speech — wav2vec 2.0 and HuBERT"
level: advanced
built_from: ["asr-fundamentals-ctc-seq2seq-wer", "contrastive-self-supervised-learning"]
leads_to: ["whisper-and-weakly-supervised-asr", "speaker-identification-and-diarization"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 15
title: "Self-Supervised Speech — wav2vec 2.0 and HuBERT"
minutes: 15
category: audio-and-speech
---

# Self-Supervised Speech — wav2vec 2.0 and HuBERT
> Transcribed speech is expensive; raw speech is nearly free. Self-supervised speech models learn
> representations from unlabeled audio and then need only a little labeled data to reach strong
> accuracy. **wav2vec 2.0** masks spans of a latent audio sequence and solves a contrastive task
> against quantized targets; **HuBERT** replaces the contrastive loss with masked prediction of
> offline cluster labels; **WavLM** adds denoising and speaker-mixing so one model serves the whole
> task stack.

**Why it matters:** these encoders are the backbone of low-resource ASR, speaker verification,
diarization and emotion recognition, and they are what "pretrain then fine-tune" means in speech.
wav2vec 2.0 reached 5.2% WER on clean LibriSpeech using **ten minutes** of labeled audio.
Interviewers probe the difference between contrastive and masked-prediction objectives, why HuBERT
needs an iterative re-clustering loop, and which layers carry phonetic versus speaker information —
the practical question when you pick a layer to fine-tune.

**Start here — suggested path:**

1. **Ground the objective** — read [wav2vec 2.0](https://arxiv.org/abs/2006.11477) — **Baevski, Zhou, Mohamed & Auli (2020)**. *Masking in latent space, product quantization, and the contrastive loss, from the authors.*
2. **See the alternative loss** — read [HuBERT](https://arxiv.org/abs/2106.07447) — **Hsu et al. (2021)**. *Why predicting offline k-means cluster labels is more stable than contrasting, and how the iterations bootstrap.*
3. **Watch the field mapped** — watch [Deep Learning for Speech Processing (MLSS 2021 Taipei)](https://www.youtube.com/watch?v=kGVAU6ldLvg) — **Hung-yi Lee (National Taiwan University)**. *A speech researcher's overview of self-supervised speech models and what each layer learns.*
4. **Learn how they are compared** — read [SUPERB](https://arxiv.org/abs/2105.01051) — **Yang et al. (2021)**. *The frozen-encoder benchmark that made "which SSL model" an answerable question.*
5. **Fine-tune one yourself** — follow [Fine-tune wav2vec 2.0 for English ASR](https://huggingface.co/blog/fine-tune-wav2vec2-english) — **Hugging Face**. *A complete, runnable CTC fine-tuning recipe on a single GPU.*

## Courses (free)
- [Hugging Face Audio Course — Unit 3: Transformer architectures for audio](https://huggingface.co/learn/audio-course/chapter3/introduction) — **Hugging Face** — free; where wav2vec 2.0, HuBERT and Whisper are placed side by side.
- [CS224S — Spoken Language Processing](https://web.stanford.edu/class/cs224s/) — **Stanford** — public slides covering speech representation learning and its downstream uses.

## Videos
- [Deep Learning for Speech Processing (MLSS 2021 Taipei)](https://www.youtube.com/watch?v=kGVAU6ldLvg) — **Hung-yi Lee**, hosted by **AINTU** — a SUPERB co-author's tour of self-supervised speech representation learning.
- [ML for Audio Study Group — Intro to Audio and ASR Deep Dive](https://www.youtube.com/watch?v=D-MH6YjuIlE) — **Hugging Face** — how pretrained speech encoders slot into a real ASR pipeline.

## Key Papers
- [wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations](https://arxiv.org/abs/2006.11477) — **Baevski et al. (2020)** — masked contrastive learning over quantized latents; 10 minutes of labels for usable ASR.
- [HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units](https://arxiv.org/abs/2106.07447) — **Hsu et al. (2021)** — the masked-prediction recipe whose units later became "semantic tokens" for audio language models.
- [WavLM: Large-Scale Self-Supervised Pre-Training for Full Stack Speech Processing](https://arxiv.org/abs/2110.13900) — **Chen et al. (2021)** — denoising plus overlapped-speech simulation; still the strongest general encoder for speaker tasks.
- [SUPERB: Speech processing Universal PERformance Benchmark](https://arxiv.org/abs/2105.01051) — **Yang et al. (2021)** — the standard frozen-representation evaluation across ten speech tasks.
- [data2vec: A General Framework for Self-Supervised Learning in Speech, Vision and Language](https://arxiv.org/abs/2202.03555) — **Baevski et al. (2022)** — one masked-latent-prediction objective for all three modalities.
- [XLS-R: Self-Supervised Cross-Lingual Speech Representation Learning at Scale](https://arxiv.org/abs/2111.09296) — **Babu et al. (2021)** — 128 languages; the multilingual answer to low-resource ASR.

## Articles / Blogs (free, no paywall)
- [Fine-Tune Wav2Vec2 for English ASR with Transformers](https://huggingface.co/blog/fine-tune-wav2vec2-english) — **Hugging Face** — the canonical runnable recipe, including the CTC head and data collator.
- [SpeechBrain](https://speechbrain.github.io/) — **SpeechBrain team** — an open toolkit whose recipes show how SSL encoders are wired into ASR, speaker and enhancement tasks.
- [NVIDIA NeMo](https://github.com/NVIDIA/NeMo) — **NVIDIA** — production-scale pretraining and fine-tuning code for speech encoders.

## In this platform
- Prerequisites: [ASR Fundamentals](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/asr-fundamentals-ctc-seq2seq-wer/asr-fundamentals-ctc-seq2seq-wer) · [Contrastive Self-Supervised Learning](/ai-ml/ai-ml-learning-resources/deep-learning/self-supervised-learning/contrastive-self-supervised-learning/contrastive-self-supervised-learning)
- Related: [Audio Tokenization & Neural Codecs](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/audio-tokenization-and-neural-codecs/audio-tokenization-and-neural-codecs) — HuBERT units are the usual source of semantic tokens
- Next: [Whisper & Weakly-Supervised ASR](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/whisper-and-weakly-supervised-asr/whisper-and-weakly-supervised-asr) · [Speaker Identification & Diarization](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/speaker-identification-and-diarization/speaker-identification-and-diarization)
- Sub-area index: [Audio & Speech](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/readme)
