---
id: "09-llms"
topic: "Large Language Models"
level: advanced
built_from: ["nlp", "deep-learning"]
updated: 2026-06-20
---

# Large Language Models (LLMs)
> Transformer language models at scale — pretraining, scaling laws, fine-tuning, alignment, and the
> systems that serve them. For *building* one from scratch, see the platform links below.

**⭐ Start here:** [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) — **Andrej Karpathy** — the best 1-hour mental model of how LLMs work.

## 📑 Concept Index
Every chapter is a self-contained folder (`NN-Concept/NN-Concept.md`) with its page, a curated
`.references.md` resource card (free, open courses · videos · papers · articles · books · cross-links),
and — for the gold demo chapter — a runnable notebook and `code/`.
> **✅ ready.** New here? Start with the field overview above, then work top to bottom.

### Pretraining & architecture
1. ✅ [Language Modeling Objectives (causal vs masked)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/language-modeling-objectives/language-modeling-objectives)
2. ✅ [Pretraining at Scale (data, compute, training dynamics)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/pretraining/pretraining)
3. ✅ [Scaling Laws (Kaplan → Chinchilla)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/scaling-laws/scaling-laws)
4. ✅ [Decoder-only Architecture (the GPT family)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/large-language-model-foundations/decoder-only-models/decoder-only-models)

### Efficient attention & inference
5. ✅ [KV Cache](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/kv-cache/kv-cache) — *gold demo chapter: page · [notebook](05-KV-Cache/05-KV-Cache.ipynb) · [code/](inference-and-runtime/kv-cache/code)*
6. ✅ [Efficient Attention (FlashAttention)](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/efficient-attention/efficient-attention)
7. ✅ [Mixture-of-Experts (MoE)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/mixture-of-experts/mixture-of-experts)
8. ✅ [Long-Context Methods (RoPE scaling, ALiBi, sparse/sliding)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/llm-model-architectures/long-context-architectures/long-context-architectures)
9. ✅ [Inference Optimization & Serving (vLLM · paged attention)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/inference-optimization/inference-optimization)

### Compression
10. ✅ [Quantization (GPTQ · AWQ · GGUF)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/quantization/quantization)
11. ✅ [Knowledge Distillation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/knowledge-distillation/knowledge-distillation)

### Adaptation & alignment
12. ✅ [LoRA / PEFT (parameter-efficient fine-tuning)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/lora-and-parameter-efficient-fine-tuning/lora-and-parameter-efficient-fine-tuning)
13. ✅ [Supervised Fine-Tuning (SFT)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/supervised-fine-tuning/supervised-fine-tuning)
14. ✅ [Instruction Tuning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/instruction-tuning/instruction-tuning)
15. ✅ [RLHF & DPO (preference alignment)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/training-and-adaptation/preference-and-alignment-training/preference-and-alignment-training)

### Prompting, reasoning & decoding
16. ✅ [Prompting & In-Context Learning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/prompting-and-in-context-learning/prompting-and-in-context-learning)
17. ✅ [Chain-of-Thought Reasoning](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/chain-of-thought-and-reasoning/chain-of-thought-and-reasoning)
18. ✅ [Decoding & Sampling for LLMs (temperature · top-k · top-p)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/inference-and-runtime/decoding-and-sampling/decoding-and-sampling)

### Evaluation & safety
19. ✅ [LLM Evaluation & Benchmarks](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/llm-evaluation/llm-evaluation)
20. ✅ [Hallucination & Alignment basics](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/reasoning-evaluation-and-alignment/safety-and-alignment/safety-and-alignment)

### Related concepts (canonical home is another section)
> Foundations or applications of LLMs, linked here to avoid repetition.
- **Transformer · Attention · Positional encoding** → [Deep Learning](/ai-ml/ai-ml-learning-resources/deep-learning/readme) ([Transformer](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/transformer-architecture/transformer-architecture) · [Attention](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/attention-mechanism/attention-mechanism) · [Positional Encoding](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/positional-encoding/positional-encoding))
- **Tokenization & subword (BPE/WordPiece) · Contextual embeddings (BERT)** → [NLP](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/natural-language-processing/readme) ([Tokenization](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/natural-language-processing/tokenization-and-subword-algorithms/tokenization-and-subword-algorithms) · [Contextual Embeddings](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/natural-language-processing/contextual-embeddings-elmo-bert/contextual-embeddings-elmo-bert))
- **Retrieval-Augmented Generation (RAG)** → [RAG & LLM Applications](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/overview)
- **PPO & policy-gradient mechanics** (the RL engine under RLHF) → [Reinforcement Learning](/ai-ml/ai-ml-learning-resources/core-machine-learning/reinforcement-learning/readme)

## 🎓 Courses (free)
- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — **Andrej Karpathy** — culminates in building & training a GPT from scratch.
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) — **Hugging Face** — fine-tuning, RLHF, deployment, free.
- [Stanford CS324 — Large Language Models](https://stanford-cs324.github.io/winter2022/) — **Stanford** — capabilities, harms, scaling, alignment; lecture notes free.
- [Stanford CS336 — Language Modeling from Scratch](https://stanford-cs336.github.io/spring2025/) — **Stanford** — build an LLM end to end (data → train → align → serve).

## 🎥 Videos
- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — pretraining → SFT → RLHF, end to end.
- [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) — **Karpathy** — BPE and why LLMs are weird at characters/math.
- [Transformers, the tech behind LLMs](https://www.youtube.com/watch?v=wjZofJX0v4M) — **3Blue1Brown** — the visual canon for the underlying architecture.
- [Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU) — **Karpathy** — a full pretraining run, spelled out.

## 📄 Key Papers
- [Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165) — **Brown et al. (2020)** — in-context learning emerges.
- [Training Compute-Optimal LLMs (Chinchilla)](https://arxiv.org/abs/2203.15556) — **Hoffmann et al. (2022)** — the scaling-law correction.
- [InstructGPT / RLHF](https://arxiv.org/abs/2203.02155) — **Ouyang et al. (2022)** — how chat models are aligned.
- [A Survey of Large Language Models](https://arxiv.org/abs/2303.18223) — **Zhao et al. (2023)** — the field map (pretraining → adaptation → use → eval).

## 📰 Articles / Blogs (free, no paywall)
- [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/) — **Jay Alammar** — the visual canon for decoder-only LMs.
- [Understanding Large Language Models](https://magazine.sebastianraschka.com/p/understanding-large-language-models) — **Sebastian Raschka** — a curated path through the key papers.
- [Transformer Circuits / mechanistic interpretability](https://transformer-circuits.pub/2021/framework/index.html) — **Anthropic** — how transformers actually compute.

## 📚 Books (free, with chapters)
- [Speech and Language Processing, 3rd ed. — **Ch. 10 "Large Language Models"**](https://web.stanford.edu/~jurafsky/slp3/10.pdf) — **Jurafsky & Martin** — the standard reference chapter, free PDF.

## 🔗 In this platform
- Build one: [project_06 ChatGPT-from-scratch](../../AI-ML-problemsets/projects/project_06_chatgpt_from_scratch/) · Intuition: [Module 8 — LLMs & Agentic Systems](../../ai-ml-intuitions/reasoning-and-agency/) · Systems: [LLM Systems curriculum](/ai-ml/ai-ml-learning-resources/meta/llm-systems-curriculum)
- Foundations: [Transformer Architecture](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/transformer-architecture/transformer-architecture) · [Attention](/ai-ml/ai-ml-learning-resources/deep-learning/attention-and-transformers/attention-mechanism/attention-mechanism) · [Contextual Embeddings (BERT)](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/natural-language-processing/contextual-embeddings-elmo-bert/contextual-embeddings-elmo-bert)
