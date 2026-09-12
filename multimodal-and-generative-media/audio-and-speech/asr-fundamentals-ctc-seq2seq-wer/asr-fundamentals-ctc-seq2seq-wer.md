---
id: "multimodal-and-generative-media/audio-and-speech/asr-fundamentals-ctc-seq2seq-wer"
topic: "ASR Fundamentals — CTC, Seq2Seq and WER"
level: intermediate
built_from: ["audio-representations-waveform-spectrogram-mel-mfcc", "sequence-to-sequence-and-encoder-decoder"]
leads_to: ["multimodal-and-generative-media/audio-and-speech/self-supervised-speech-wav2vec2-hubert", "multimodal-and-generative-media/audio-and-speech/whisper-and-weakly-supervised-asr"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 16
title: "ASR Fundamentals — CTC, Seq2Seq and WER"
minutes: 16
category: audio-and-speech
---

# ASR Fundamentals — CTC, Seq2Seq and WER
> Automatic speech recognition (ASR) maps a long audio sequence to a much shorter text sequence
> with **no alignment given**. Three families solve that: **connectionist temporal classification
> (CTC)**, which sums over every alignment using a blank symbol; **attention-based sequence-to-
> sequence**, which lets a decoder attend over the whole utterance; and the **RNN-Transducer
> (RNN-T)**, which adds a prediction network so the model can stream. Accuracy is reported as
> **word error rate (WER)**.

**Why it matters:** every deployed speech system is one of these three, and the choice is a latency
decision as much as an accuracy one — CTC and RNN-T stream, plain attention seq2seq does not.
Interviewers probe the conditional-independence assumption CTC makes (and why it therefore needs an
external language model), how the blank token enables the forward-backward sum over alignments, and
the traps in WER: it is unbounded above, punctuation and casing are usually stripped, and a 5% WER
on read speech can be 25% on a noisy phone call.

**Start here — suggested path:**

1. **Understand alignment-free training** — read [Sequence Modeling with CTC](https://distill.pub/2017/ctc/) — **Awni Hannun (Distill, 2017)**. *The visual, interactive explanation of the blank symbol, the alignment lattice and the forward-backward algorithm.*
2. **Watch it derived** — watch [Lecture 16: Connectionist Temporal Classification](https://www.youtube.com/watch?v=RowViowx1Bg) — **Carnegie Mellon University Deep Learning (11-785)**. *A full lecture deriving the CTC loss and its decoding, from a course that teaches it properly.*
3. **Read the textbook account** — read [*Speech and Language Processing*, Ch. 16](https://web.stanford.edu/~jurafsky/slp3/16.pdf) — **Jurafsky & Martin**. *Encoder-decoder ASR, CTC, and the WER definition with worked examples, free.*
4. **See the architectures that won** — read [Conformer](https://arxiv.org/abs/2005.08100) — **Gulati et al. (2020)** and [Sequence Transduction with Recurrent Neural Networks](https://arxiv.org/abs/1211.3711) — **Graves (2012)**. *Convolution-augmented encoders, and the transducer that makes streaming possible.*
5. **Calibrate on real numbers** — browse the [Open ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard) — **Hugging Face, NVIDIA, Cambridge, Mistral**. *WER and real-time factor for 60+ systems; the honest picture of what "good" means today.*

## Courses (free)
- [Hugging Face Audio Course — Unit 5: Automatic speech recognition](https://huggingface.co/learn/audio-course/chapter5/introduction) — **Hugging Face** — free and hands-on: fine-tune and evaluate a real ASR model end to end.
- [CS224S — Spoken Language Processing](https://web.stanford.edu/class/cs224s/) — **Stanford** — the standard university treatment of ASR, from phonetics to end-to-end models.

## Videos
- [Lecture 16: Connectionist Temporal Classification, Sequence prediction](https://www.youtube.com/watch?v=RowViowx1Bg) — **Carnegie Mellon University Deep Learning** — the CTC loss derived on the board, alignments and all.
- [Lecture 17: CTC and Sequence-to-Sequence Prediction](https://www.youtube.com/watch?v=5Rj0J9AuGw0) — **Carnegie Mellon University Deep Learning** — CTC decoding, beam search, and the move to attention-based models.
- [ML for Audio Study Group — Intro to Audio and ASR Deep Dive](https://www.youtube.com/watch?v=D-MH6YjuIlE) — **Hugging Face** — the engineering view: data, features, models and evaluation in one sitting.

## Key Papers
- [Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with RNNs](https://www.cs.toronto.edu/~graves/icml_2006.pdf) — **Graves, Fernández, Gomez & Schmidhuber (2006)** — the original CTC paper, free from the author's page.
- [Sequence Transduction with Recurrent Neural Networks (RNN-T)](https://arxiv.org/abs/1211.3711) — **Graves (2012)** — adds a prediction network to CTC; the architecture behind most on-device streaming ASR.
- [Listen, Attend and Spell](https://arxiv.org/abs/1508.01211) — **Chan, Jaitly, Le & Vinyals (2015)** — the first strong attention-based encoder-decoder ASR system.
- [Deep Speech 2](https://arxiv.org/abs/1512.02595) — **Amodei et al. (2015)** — end-to-end CTC ASR at scale in English and Mandarin; the paper that made end-to-end mainstream.
- [Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100) — **Gulati et al. (2020)** — the encoder block still used across ASR toolkits in 2026.
- [Open ASR Leaderboard: Towards Reproducible and Transparent Multilingual and Long-Form Speech Recognition Evaluation](https://arxiv.org/abs/2510.06961) — **Open ASR Leaderboard team (2025)** — how WER should be measured, and what today's systems actually score.

## Articles / Blogs (free, no paywall)
- [Sequence Modeling with CTC](https://distill.pub/2017/ctc/) — **Awni Hannun (Distill)** — still the single best explanation of CTC; interactive alignment diagrams.
- [Open ASR Leaderboard: trends and insights](https://huggingface.co/blog/open-asr-leaderboard) — **Hugging Face** — what the 2025 leaderboard says about accuracy versus throughput.
- [NVIDIA NeMo — ASR toolkit](https://github.com/NVIDIA/NeMo) — **NVIDIA** — production CTC, RNN-T and attention recipes; the reference implementations to read.

## Books (free, with chapters)
- [*Speech and Language Processing* — Ch. 16 "Automatic Speech Recognition and Text-to-Speech"](https://web.stanford.edu/~jurafsky/slp3/16.pdf) — **Jurafsky & Martin** — free draft; the canonical textbook treatment of CTC, encoder-decoder ASR and WER.

## In this platform
- Prerequisites: [Audio Representations](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/audio-representations-waveform-spectrogram-mel-mfcc/audio-representations-waveform-spectrogram-mel-mfcc) · [Sequence-to-Sequence & Encoder-Decoder](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/sequence-to-sequence-and-encoder-decoder/sequence-to-sequence-and-encoder-decoder)
- Decoding (canonical home): [Decoding Strategies](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/decoding-strategies/decoding-strategies) — beam search and its variants, shared with ASR
- Next: [Self-Supervised Speech](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/self-supervised-speech-wav2vec2-hubert/self-supervised-speech-wav2vec2-hubert) · [Whisper & Weakly-Supervised ASR](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/whisper-and-weakly-supervised-asr/whisper-and-weakly-supervised-asr)
- Sub-area index: [Audio & Speech](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/readme)
