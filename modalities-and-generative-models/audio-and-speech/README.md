---
id: "14-audio-and-speech"
topic: "Audio & Speech"
level: advanced
built_from: ["deep-learning", "nlp"]
leads_to: ["multimodal", "agentic-ai"]
updated: 2026-09-07
---

# Audio & Speech
> Models that *listen and talk* — audio representations and neural codecs, speech recognition
> (ASR), speech synthesis (TTS), and the realtime voice stack. Audio *diffusion* mechanics live
> with [Diffusion](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/readme); this topic owns the
> speech pipeline end to end, plus the audio-generation overview.

**Start here:** [Hugging Face Audio Course](https://huggingface.co/learn/audio-course/chapter1/introduction) — **Hugging Face** — free, code-first path through representations → ASR → TTS → a full speech-to-speech pipeline.

## Concept Index
Every chapter is a self-contained folder (`<topic>/<topic>.md`) with its page.
> Representations first — everything downstream stands on them.

### Representations & codecs
1. ✅ [Audio Representations (waveform · spectrogram · mel · MFCC)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/audio-representations-waveform-spectrogram-mel-mfcc/audio-representations-waveform-spectrogram-mel-mfcc)
2. ✅ [Audio Tokenization & Neural Codecs (SoundStream · EnCodec · Mimi · discrete audio tokens)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/audio-tokenization-and-neural-codecs/audio-tokenization-and-neural-codecs)

### Speech recognition
3. ✅ [ASR Fundamentals (CTC · seq2seq · WER and its traps)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/asr-fundamentals-ctc-seq2seq-wer/asr-fundamentals-ctc-seq2seq-wer)
4. ✅ [Self-Supervised Speech (wav2vec 2.0 · HuBERT · WavLM)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/self-supervised-speech-wav2vec2-hubert/self-supervised-speech-wav2vec2-hubert)
5. ✅ [Whisper & Large-Scale Weakly-Supervised ASR](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/whisper-and-weakly-supervised-asr/whisper-and-weakly-supervised-asr)

### Speech synthesis
6. ✅ [TTS Fundamentals (Tacotron lineage · VITS · vocoders)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/tts-fundamentals-tacotron-vits-vocoders/tts-fundamentals-tacotron-vits-vocoders)
7. ✅ [Modern TTS & Voice Cloning (codec LMs · zero-shot voices · safety)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/modern-tts-and-voice-cloning/modern-tts-and-voice-cloning)

### Systems & applications
8. ✅ [Speaker Identification & Diarization](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/speaker-identification-and-diarization/speaker-identification-and-diarization)
9. ✅ [Realtime & Streaming Voice Agents (latency budgets · VAD · barge-in · full duplex)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/realtime-and-streaming-voice-agents/realtime-and-streaming-voice-agents)
10. ✅ [Music & Audio Generation overview (codec LMs · latent diffusion)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/music-and-audio-generation-overview/music-and-audio-generation-overview)

### Related concepts (covered in another section)
> Kept in their canonical home to avoid repetition.
- **Sequence decoding (beam search · sampling controls)** → [Decoding Strategies](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/natural-language-processing/decoding-strategies/decoding-strategies)
- **Encoder-decoder sequence models** → [Sequence-to-Sequence & Encoder-Decoder](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/natural-language-processing/sequence-to-sequence-and-encoder-decoder/sequence-to-sequence-and-encoder-decoder)
- **Diffusion mechanics for audio** → [Diffusion](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/readme)
- **Audio in multimodal LLMs** → [Multimodal](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/readme)
- **Fourier analysis & signal processing math** → [Fourier Analysis & Signal Processing](/ai-ml/ai-ml-learning-resources/specialized-studies/advanced-mathematics-for-ai-research/fourier-analysis-and-signal-processing/fourier-analysis-and-signal-processing)
- **The agent loop under a voice agent** → [Agent Foundations](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-foundations/agent-foundations)

## Courses (free)
- [Hugging Face Audio Course](https://huggingface.co/learn/audio-course/chapter1/introduction) — **Hugging Face** — the practical spine for this topic, unit by unit.
- [Audio Signal Processing for Machine Learning](https://www.youtube.com/playlist?list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0) — **Valerio Velardo - The Sound of AI** — the best free ground-up course on audio features.
- [CS224S — Spoken Language Processing](https://web.stanford.edu/class/cs224s/) — **Stanford** — the university course, with public slides and assignments.

## Videos
- [ML for Audio Study Group — Intro to Audio and ASR Deep Dive](https://www.youtube.com/watch?v=D-MH6YjuIlE) — **Hugging Face** — audio data, features and ASR in one engineering-first session.
- [Deep Learning for Speech Processing (MLSS 2021 Taipei)](https://www.youtube.com/watch?v=kGVAU6ldLvg) — **Hung-yi Lee**, via **AINTU** — a speech researcher's map of representation learning.

## Key Papers
- [Robust Speech Recognition via Large-Scale Weak Supervision (Whisper)](https://arxiv.org/abs/2212.04356) — **Radford et al. (2022)** — the ASR baseline everyone deploys.
- [wav2vec 2.0](https://arxiv.org/abs/2006.11477) — **Baevski et al. (2020)** — self-supervised speech representations.
- [High Fidelity Neural Audio Compression (EnCodec)](https://arxiv.org/abs/2210.13438) — **Défossez et al. (2022)** — the codec behind audio-token language models.
- [Moshi: A Speech-Text Foundation Model for Real-Time Dialogue](https://arxiv.org/abs/2410.00037) — **Défossez et al., Kyutai (2024)** — full-duplex speech-to-speech and the streaming Mimi codec.

## Articles / Blogs (free, no paywall)
- [Sequence Modeling with CTC](https://distill.pub/2017/ctc/) — **Awni Hannun (Distill)** — the visual explanation of the loss that made end-to-end ASR possible.
- [Generating music in the waveform domain](https://sander.ai/2020/03/24/audio-generation.html) — **Sander Dieleman** — why audio generation is designed the way it is.

## Books (free, with chapters)
- [*Speech and Language Processing* — Ch. 16 "Automatic Speech Recognition and Text-to-Speech"](https://web.stanford.edu/~jurafsky/slp3/16.pdf) — **Jurafsky & Martin** — free draft, the standard reference.
- [*Fundamentals of Music Processing* — FMP notebooks](https://www.audiolabs-erlangen.de/resources/MIR/FMP/C0/C0.html) — **Meinard Müller** — a free executable book on audio and music representations.

## In this platform
- Language side: [NLP](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/natural-language-processing/readme) · [LLMs](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme) · Fusion: [Multimodal](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/readme)
