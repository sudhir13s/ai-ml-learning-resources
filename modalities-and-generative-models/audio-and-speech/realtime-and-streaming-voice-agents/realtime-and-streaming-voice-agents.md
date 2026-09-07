---
id: "modalities-and-generative-models/audio-and-speech/realtime-and-streaming-voice-agents"
topic: "Realtime & Streaming Voice Agents"
level: advanced
built_from: ["whisper-and-weakly-supervised-asr", "modern-tts-and-voice-cloning", "audio-tokenization-and-neural-codecs"]
leads_to: ["agent-foundations"]
interview_frequency: high
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Realtime & Streaming Voice Agents"
minutes: 16
category: audio-and-speech
---

# Realtime & Streaming Voice Agents
> A voice agent is a latency budget with a model inside it. The **cascaded** design chains
> streaming speech recognition, a language model and streaming speech synthesis, with **voice
> activity detection (VAD)** and turn detection deciding when the user has finished. The
> **speech-to-speech** design — Moshi, GPT-Realtime, Qwen-Omni — removes the text bottleneck and
> models audio tokens directly, which is what makes true **full-duplex** conversation (listening
> while speaking, and being interrupted) possible.

**Why it matters:** conversation feels natural under roughly 300–500 ms of response latency, and a
cascade spends that budget three times over; Moshi reports 160 ms theoretical and 200 ms practical
latency end to end. Interviewers probe where the milliseconds go, how **barge-in** is handled
(echo cancellation, halting generation, and reconciling what the user actually heard), why VAD
alone makes a bad turn detector, and the honest trade: cascades are debuggable and swappable,
speech-to-speech models are faster and keep prosody but are harder to control and evaluate.

**Start here — suggested path:**

1. **See the full-duplex end state** — read [Moshi: A Speech-Text Foundation Model for Real-Time Dialogue](https://arxiv.org/abs/2410.00037) — **Défossez et al., Kyutai (2024)**. *Two parallel audio streams plus an "inner monologue" text stream; the clearest architecture for real conversation.*
2. **Learn the production API surface** — read [Introducing gpt-realtime and Realtime API updates](https://openai.com/index/introducing-gpt-realtime/) — **OpenAI**. *Speech-to-speech in production: sessions, interruptions, tool calls, and telephony.*
3. **Build the cascade properly** — read the [LiveKit Agents documentation](https://docs.livekit.io/agents/) — **LiveKit**. *The reference open framework: transport, VAD, turn detection, and the agent loop.*
4. **Fix turn-taking** — read [Using a transformer to improve end-of-turn detection](https://blog.livekit.io/using-a-transformer-to-improve-end-of-turn-detection/) — **LiveKit**. *Why silence thresholds interrupt people, and what a semantic turn detector fixes.*
5. **Place it in the agent stack** — read [Agent Foundations](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-foundations/agent-foundations). *Voice is an interface on the agent loop; tools, memory and planning are unchanged.*

## Courses (free)
- [Hugging Face Audio Course — Unit 7: Putting it all together](https://huggingface.co/learn/audio-course/chapter7/introduction) — **Hugging Face** — free; builds a speech-to-speech pipeline from recognition, translation and synthesis.
- [CS224S — Spoken Language Processing](https://web.stanford.edu/class/cs224s/) — **Stanford** — dialogue systems and conversational speech, the academic frame for voice agents.

## Videos
- [LiveKit DevDay 2025 Keynote](https://www.youtube.com/watch?v=Ly8_qOgPoBk) — **LiveKit** — the maintainers on what production voice agents actually need: transport, latency, interruption.

## Key Papers
- [Moshi: A Speech-Text Foundation Model for Real-Time Dialogue](https://arxiv.org/abs/2410.00037) — **Défossez et al., Kyutai (2024)** — full-duplex speech-to-speech with the streaming Mimi codec; 160 ms theoretical latency.
- [Qwen2.5-Omni Technical Report](https://arxiv.org/abs/2503.20215) — **Qwen Team (2025)** — the Thinker-Talker split and time-aligned multimodal rotary position embedding for streaming speech output.
- [Generative Spoken Dialogue Language Modeling (dGSLM)](https://arxiv.org/abs/2203.16502) — **Nguyen et al., Meta (2022)** — the first two-channel dialogue model with natural overlaps and backchannels; the ancestor of full-duplex systems.
- [WavChat: A Survey of Spoken Dialogue Models](https://arxiv.org/abs/2411.13577) — **Ji et al. (2024)** — the map of cascaded versus end-to-end spoken dialogue systems and their evaluation.
- [Distil-Whisper](https://arxiv.org/abs/2311.00430) — **Gandhi, von Platen & Rush (2023)** — how the recognition leg of a cascade is made fast enough to stream.

## Articles / Blogs (free, no paywall)
- [Introducing gpt-realtime and Realtime API updates for production voice agents](https://openai.com/index/introducing-gpt-realtime/) — **OpenAI** — the current speech-to-speech production model and its interruption and tool-calling semantics.
- [Realtime API documentation](https://platform.openai.com/docs/guides/realtime) — **OpenAI** — session lifecycle, streaming audio in and out, server-side VAD; the concrete contract.
- [LiveKit Agents](https://docs.livekit.io/agents/) — **LiveKit** — open-source framework docs; the clearest free explanation of the voice-agent pipeline.
- [Using a transformer to improve end-of-turn detection](https://blog.livekit.io/using-a-transformer-to-improve-end-of-turn-detection/) — **LiveKit** — semantic turn detection versus silence thresholds, with measurements.
- [Pipecat](https://github.com/pipecat-ai/pipecat) — **Pipecat contributors** — an open real-time voice framework whose pipeline abstractions are worth reading.
- [Silero VAD](https://github.com/snakers4/silero-vad) — **Silero team** — the MIT-licensed voice activity detector nearly every stack uses; fast enough per 30 ms chunk to be free.
- [Moshi — reference implementation](https://github.com/kyutai-labs/moshi) — **Kyutai** — PyTorch, MLX and Rust code for a full-duplex model you can actually run.

## In this platform
- Prerequisites: [Whisper & Weakly-Supervised ASR](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/whisper-and-weakly-supervised-asr/whisper-and-weakly-supervised-asr) · [Modern TTS & Voice Cloning](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/modern-tts-and-voice-cloning/modern-tts-and-voice-cloning) · [Audio Tokenization & Neural Codecs](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/audio-tokenization-and-neural-codecs/audio-tokenization-and-neural-codecs)
- Speaker attribution in multi-party calls: [Speaker Identification & Diarization](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/speaker-identification-and-diarization/speaker-identification-and-diarization)
- The agent loop this sits on (canonical home): [Agent Foundations](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/agent-foundations/agent-foundations)
- Sub-area index: [Audio & Speech](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/readme)
