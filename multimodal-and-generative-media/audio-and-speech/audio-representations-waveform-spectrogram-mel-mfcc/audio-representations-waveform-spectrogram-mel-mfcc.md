---
id: "multimodal-and-generative-media/audio-and-speech/audio-representations-waveform-spectrogram-mel-mfcc"
topic: "Audio Representations — Waveform, Spectrogram, Mel, MFCC"
level: beginner
built_from: ["fourier-analysis-and-signal-processing"]
leads_to: ["multimodal-and-generative-media/audio-and-speech/audio-tokenization-and-neural-codecs", "multimodal-and-generative-media/audio-and-speech/asr-fundamentals-ctc-seq2seq-wer"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 14
title: "Audio Representations — Waveform, Spectrogram, Mel, MFCC"
minutes: 14
category: audio-and-speech
---

# Audio Representations — Waveform, Spectrogram, Mel, MFCC
> Every audio model starts by choosing what a sound *is* to the network. A **waveform** is a 1-D
> array of amplitudes sampled 16,000–48,000 times a second; a **spectrogram** is what you get after
> a short-time Fourier transform (STFT) — energy per frequency per time frame; a **mel spectrogram**
> warps those frequencies onto a perceptual scale; and **mel-frequency cepstral coefficients
> (MFCCs)** compress a mel frame into ~13–40 decorrelated numbers.

**Why it matters:** the representation decides the sequence length, the model, and the compute
budget — one second of 16 kHz audio is 16,000 samples but only ~100 mel frames, a 160× difference.
Interviewers probe the chain sampling rate → frame length → hop length → number of mel bins, why
mel and decibel scaling are logarithmic (human hearing is), and when MFCCs are the right choice
(small classical models, speaker features) versus obsolete (deep models learn better features from
mel or raw waveform directly).

**Start here — suggested path:**

1. **See the transform** — watch [But what is the Fourier Transform? A visual introduction](https://www.youtube.com/watch?v=spUNpyF58BY) — **3Blue1Brown**. *The geometric picture of frequency decomposition that every spectrogram is built on.*
2. **Build the whole feature chain** — work through [Audio Signal Processing for Machine Learning](https://www.youtube.com/playlist?list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0) — **Valerio Velardo - The Sound of AI**. *Waveform → STFT → spectrogram → mel → MFCC, each derived and then coded in Python.*
3. **Get the practitioner version** — read [Speech Processing for Machine Learning: Filter banks, MFCCs](https://haythamfayek.com/2016/04/21/speech-processing-for-machine-learning.html) — **Haytham Fayek**. *The MFCC pipeline written out step by step with the exact equations and code.*
4. **Do it in code** — run [Hugging Face Audio Course, Unit 1: Working with audio data](https://huggingface.co/learn/audio-course/chapter1/introduction) — **Hugging Face**. *Loading, resampling, framing and plotting real audio; the fastest path from theory to a tensor.*
5. **Learn the failure modes** — read the [torchaudio documentation](https://docs.pytorch.org/audio/stable/index.html) — **PyTorch team**. *Resampling, normalization and windowing defaults are where most audio bugs actually live.*

## Courses (free)
- [Hugging Face Audio Course — Unit 1: Audio data](https://huggingface.co/learn/audio-course/chapter1/introduction) — **Hugging Face** — free and code-first; the practical spine for this whole sub-area.
- [Audio Signal Processing for Machine Learning](https://www.youtube.com/playlist?list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0) — **Valerio Velardo - The Sound of AI** — the best free ground-up course on audio features, with math and Python side by side.
- [CS224S — Spoken Language Processing](https://web.stanford.edu/class/cs224s/) — **Stanford** — the university course this sub-area tracks; slides and assignments are public.

## Videos
- [But what is the Fourier Transform? A visual introduction](https://www.youtube.com/watch?v=spUNpyF58BY) — **3Blue1Brown** — the clearest intuition anywhere for what a spectrogram column means.
- [ML for Audio Study Group — Intro to Audio and ASR Deep Dive](https://www.youtube.com/watch?v=D-MH6YjuIlE) — **Hugging Face** — an engineer's tour of audio data, sample rates and features before any modeling.
- [The Fast Fourier Transform (FFT)](https://www.youtube.com/watch?v=E8HeD-MUrjY) — **Steve Brunton** — why the transform behind every STFT frame is O(n log n), which is what makes spectrograms cheap.

## Key Papers
- [SpecAugment: A Simple Data Augmentation Method for Automatic Speech Recognition](https://arxiv.org/abs/1904.08779) — **Park et al. (2019)** — masks time and frequency bands *in the spectrogram*; the clearest proof that the representation is the model's real input surface.
- [AST: Audio Spectrogram Transformer](https://arxiv.org/abs/2104.01778) — **Gong, Chung & Glass (2021)** — treats the mel spectrogram as an image of patches, the bridge from audio features to transformer models.
- [WaveNet: A Generative Model for Raw Audio](https://arxiv.org/abs/1609.03499) — **van den Oord et al. (2016)** — the counter-argument: model the waveform sample by sample and skip hand-designed features.

## Articles / Blogs (free, no paywall)
- [Speech Processing for Machine Learning: Filter banks, MFCCs and What's In-Between](https://haythamfayek.com/2016/04/21/speech-processing-for-machine-learning.html) — **Haytham Fayek** — the reference walkthrough of pre-emphasis, framing, windowing, filter banks and the discrete cosine transform.
- [librosa documentation and examples](https://librosa.org/doc/latest/index.html) — **librosa maintainers** — the de-facto Python audio library; the docs double as a feature-extraction reference.
- [torchaudio documentation](https://docs.pytorch.org/audio/stable/index.html) — **PyTorch team** — spectrogram, mel-scale and MFCC transforms as differentiable layers you can put inside a model.

## Books (free, with chapters)
- [*Fundamentals of Music Processing* — the FMP notebooks](https://www.audiolabs-erlangen.de/resources/MIR/FMP/C0/C0.html) — **Meinard Müller (AudioLabs Erlangen)** — a free, executable book: every audio representation explained and plotted in Jupyter.
- [*Spectral Audio Signal Processing* — full free book](https://www.dsprelated.com/freebooks/sasp/) — **Julius O. Smith III (Stanford CCRMA)** — the rigorous reference for STFT windows, overlap-add and spectral analysis.
- [*Speech and Language Processing* — Ch. 16 "Automatic Speech Recognition and Text-to-Speech"](https://web.stanford.edu/~jurafsky/slp3/16.pdf) — **Jurafsky & Martin** — the free draft chapter; its feature-extraction section is the textbook account.

## In this platform
- Prerequisite math: [Fourier Analysis & Signal Processing](/ai-ml/ai-ml-learning-resources/frontier-and-specialized/advanced-mathematics-for-ai-research/fourier-analysis-and-signal-processing/fourier-analysis-and-signal-processing)
- Next: [Audio Tokenization & Neural Codecs](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/audio-tokenization-and-neural-codecs/audio-tokenization-and-neural-codecs) · [ASR Fundamentals](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/asr-fundamentals-ctc-seq2seq-wer/asr-fundamentals-ctc-seq2seq-wer)
- Sub-area index: [Audio & Speech](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/readme)
