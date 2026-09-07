---
id: "12-multimodal"
topic: "Multimodal Models"
level: advanced
built_from: ["llms", "computer-vision", "diffusion"]
leads_to: ["video-understanding", "agentic-ai"]
updated: 2026-09-07
---

# Multimodal Models
> Models that *understand and reason across modalities* — image+text (vision-language models,
> VLMs), audio, video, and any-to-any architectures. Image *generation* lives in
> [Diffusion](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/readme) and
> [Generative Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/readme); this sub-area is about joint
> representation, fusion, multimodal reasoning, and how all of it is evaluated.

**Start here:** [Generalized Visual Language Models (Lil'Log)](https://lilianweng.github.io/posts/2022-06-09-vlm/) — **Lilian Weng** — the canonical map of how vision meets language models — then [Vision Language Models (Better, Faster, Stronger)](https://huggingface.co/blog/vlms-2025) — **Hugging Face** — for where the field stands in 2025–26.

## Concept index

Every page is a self-contained folder (`<topic>/<topic>.md`). Read them in this order: contrastive
alignment first (CLIP), then instruction-tuned VLMs, then fusion and any-to-any architectures,
then applications and evaluation.

### Representation alignment

1. [CLIP and Contrastive Vision-Language Pretraining](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/clip-and-contrastive-vision-language-pretraining/clip-and-contrastive-vision-language-pretraining)
2. [Modern Dual Encoders — SigLIP and Retrieval](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/modern-dual-encoders-siglip-and-retrieval/modern-dual-encoders-siglip-and-retrieval)

### Vision-language models (VLMs)

3. [Interleaved and Few-Shot VLMs — the Flamingo Lineage](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/interleaved-and-few-shot-vlms-flamingo/interleaved-and-few-shot-vlms-flamingo)
4. [Visual Instruction Tuning — the LLaVA Recipe](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/visual-instruction-tuning-llava/visual-instruction-tuning-llava)
5. [Modern Open VLM Architectures](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/modern-open-vlm-architectures/modern-open-vlm-architectures) — dynamic resolution, native OCR, grounding

### Fusion and any-to-any

6. [Fusion Strategies — Early, Late and Native Multimodality](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/fusion-strategies-early-late-and-native-multimodality/fusion-strategies-early-late-and-native-multimodality)
7. [Unified Token Spaces and Any-to-Any Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/unified-token-spaces-and-any-to-any-models/unified-token-spaces-and-any-to-any-models)

### Applications and evaluation

8. [Document and Chart Understanding](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/document-and-chart-understanding/document-and-chart-understanding)
9. [Multimodal RAG](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/multimodal-rag/multimodal-rag)
10. [Multimodal Benchmarks and Evaluation](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/multimodal-learning/multimodal-benchmarks-and-evaluation/multimodal-benchmarks-and-evaluation)

### Related concepts (covered in another section)

> Kept in their canonical home to avoid repetition.

- **Vision Transformers (ViT)** — the visual backbone → [Computer Vision · Vision Transformers](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/vision-transformers/vision-transformers)
- **Contrastive self-supervision** — the loss CLIP reuses → [Deep Learning · Contrastive / Self-Supervised Learning](/ai-ml/ai-ml-learning-resources/deep-learning/self-supervised-learning/contrastive-self-supervised-learning/contrastive-self-supervised-learning)
- **Text-to-image generation** → [Diffusion](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/diffusion-models/readme) · [Generative Models](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/generative-models/readme)
- **Speech understanding and audio tokens** → [Audio and Speech](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/audio-and-speech/readme)
- **Video-language models** → [Video Understanding](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/video-understanding/readme)
- **LLM decoder architecture, instruction tuning** → [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme)

## Courses (free)

- [Hugging Face Community Computer Vision Course — multimodal unit](https://huggingface.co/learn/computer-vision-course/en/unit4/multimodal-models/pre-intro) — **Hugging Face** — free, code-first VLM material from contrastive encoders to full models.
- [Stanford CME296: Diffusion and Large Vision Models](https://www.youtube.com/playlist?list=PLoROMvodv4rNdy8rt2rZ4T2xM0OjADnfu) — **Stanford Online** — full lecture series on large vision models and diffusion; the university companion to this sub-area.
- [Stanford CS231n — Lecture 16, "Vision and Language" (slides)](https://cs231n.stanford.edu/slides/2025/lecture_16.pdf) — **Stanford (Spring 2025)** — the current academic overview in one deck.

## Videos

- [OpenAI CLIP: Connecting Text and Images (Paper Explained)](https://www.youtube.com/watch?v=T9XSU0pKX2E) — **Yannic Kilcher** — the clearest CLIP walkthrough.
- [Coding a Multimodal (Vision) Language Model from scratch in PyTorch](https://www.youtube.com/watch?v=vAmKB7iPkWw) — **Umar Jamil** — PaliGemma implemented line by line.
- [Vision in the Age of LLMs (ETH Zurich Robot Learning, 2026)](https://www.youtube.com/watch?v=0XB7fNS_ONg) — **Lucas Beyer (guest lecture, Oier Mees' course)** — SigLIP's and PaliGemma's co-author on the 2026 state of vision encoders.

## Key Papers

- [Learning Transferable Visual Models From Natural Language Supervision (CLIP)](https://arxiv.org/abs/2103.00020) — **Radford et al. (2021)** — the alignment paper everything builds on.
- [Flamingo: a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198) — **Alayrac et al. (2022)** — the interleaved, few-shot VLM blueprint.
- [Visual Instruction Tuning (LLaVA)](https://arxiv.org/abs/2304.08485) — **Liu et al. (2023)** — the open-VLM recipe.
- [Sigmoid Loss for Language Image Pre-Training (SigLIP)](https://arxiv.org/abs/2303.15343) — **Zhai et al. (2023)** — the loss behind today's default vision towers.
- [Qwen3-VL Technical Report](https://arxiv.org/abs/2511.21631) — **Bai et al. (2025)** — the 2026 open frontier: native 256K interleaved context, grounding, video.

## Articles

- [Multimodality and Large Multimodal Models](https://huyenchip.com/2023/10/10/multimodal.html) — **Chip Huyen** — systems-level survey of multimodal model design.
- [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms) — **Sebastian Raschka** — the two dominant fusion designs, drawn and compared.
- [Vision Language Models Explained](https://huggingface.co/blog/vlms) — **Hugging Face** — practical tour of open VLMs, with fine-tuning code.
- [Vision Language Models (Better, Faster, Stronger)](https://huggingface.co/blog/vlms-2025) — **Hugging Face** — the 2025–26 update: reasoning, agents, omni models, multimodal retrieval.

## Books (free, with chapters)

- [*Understanding Deep Learning* — Ch. 12 "Transformers"](https://udlbook.github.io/udlbook/) — **Simon Prince** — free PDF; the backbone both towers of a VLM assume.

## In this platform

- Backbones: [Computer Vision](/ai-ml/ai-ml-learning-resources/modalities-and-generative-models/computer-vision/readme) · Language side: [LLMs, Applications and Agents](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/readme)
- Concept depth (the *why*): [Multimodal LLMs (intuition)](/ai-ml/ai-ml-intuitions/multimodal-integration/modality-fusion/multimodal-llms-intuition)
