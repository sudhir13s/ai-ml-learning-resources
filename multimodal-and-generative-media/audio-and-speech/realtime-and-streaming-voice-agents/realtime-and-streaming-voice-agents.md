---
id: "multimodal-and-generative-media/audio-and-speech/realtime-and-streaming-voice-agents"
topic: "Realtime & Streaming Voice Agents"
core_idea: "A voice agent is designed around a latency budget of a few hundred milliseconds: cascades are debuggable but slow, while speech-to-speech models are fast and full-duplex but harder to control."
level: advanced
built_from: ["whisper-and-weakly-supervised-asr", "modern-tts-and-voice-cloning", "audio-tokenization-and-neural-codecs"]
leads_to: ["16-agentic-ai/llm-agents-overview"]
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

## References

The curated link library for this topic — in this platform, videos, courses, articles, papers — lives in a companion file so it can be reused as a standalone reference list:

**→ [Realtime & Streaming Voice Agents — references](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/audio-and-speech/realtime-and-streaming-voice-agents/realtime-and-streaming-voice-agents#references-further-reading)**
