---
id: "multimodal-and-generative-media/multimodal-learning/document-and-chart-understanding/references"
topic: "Document and Chart Understanding — References"
parent: "multimodal-and-generative-media/multimodal-learning/document-and-chart-understanding"
type: references
updated: 2026-09-14
---

# Document and Chart Understanding — references

> Companion link library for **[Document and Chart Understanding](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/multimodal-learning/document-and-chart-understanding/document-and-chart-understanding)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **See why the pipeline had to go** — read [OCR-free Document Understanding Transformer (Donut)](https://arxiv.org/abs/2111.15664) — **Kim et al. (2022)**. *The paper that removed OCR from the loop, with the error-compounding argument made concretely.*
2. **Learn the pretraining trick** — read [Pix2Struct: Screenshot Parsing as Pretraining for Visual Language Understanding](https://arxiv.org/abs/2210.03347) — **Lee et al. (2023)**. *Predicting the HTML of a masked screenshot teaches structure — a beautifully chosen pretext task.*
3. **Understand what "hard" means here** — read [ChartQA](https://arxiv.org/abs/2203.10244) — **Masry et al. (2022)** — and [DocVQA](https://arxiv.org/abs/2007.00398) — **Mathew et al. (2021)**. *The two benchmarks that define the task; read the question types, not just the scores.*
4. **Run a modern pipeline** — read [olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language Models](https://arxiv.org/abs/2502.18443) — **Poznanski et al. (2025)** — and its [project page](https://olmocr.allenai.org/). *An open, cost-measured, production-scale PDF-to-text system.*
5. **Fine-tune one** — work through the [Donut tutorials](https://github.com/NielsRogge/Transformers-Tutorials/tree/master/Donut) — **Niels Rogge (Hugging Face)**. *Document visual question answering and parsing, end to end in notebooks.*

**In this platform**:
- Related: [Chunking](/ai-ml/practitioner-workflows/llm-applications/chunking/chunking) · [Question Answering](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/question-answering/question-answering)
- Prerequisites: [Modern Open VLM Architectures](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/multimodal-learning/modern-open-vlm-architectures/modern-open-vlm-architectures) · [OCR](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/computer-vision/ocr/ocr) — the classical pipeline these models replace
- Next: [Multimodal RAG](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/multimodal-learning/multimodal-rag/multimodal-rag) — document understanding is what makes a page retrievable

**Courses**:
- [Hugging Face Community Computer Vision Course — multimodal unit](https://huggingface.co/learn/computer-vision-course/en/unit4/multimodal-models/vlm-intro) — **Hugging Face** — free VLM material that the document models specialize.
- [Visual question answering task guide](https://huggingface.co/docs/transformers/en/tasks/visual_question_answering) — **Hugging Face** — the runnable baseline task that document VQA extends.

**Articles**:
- [Accelerating Document AI](https://huggingface.co/blog/document-ai) — **Hugging Face** — the task taxonomy (classification, parsing, document VQA, table extraction) with models per task.
- [Donut tutorials](https://github.com/NielsRogge/Transformers-Tutorials/tree/master/Donut) — **Niels Rogge (Hugging Face)** — fine-tuning notebooks for document parsing and document VQA.
- [olmOCR](https://olmocr.allenai.org/) — **Allen Institute for AI** — the toolkit, demo and evaluation behind the paper; open weights and open pipeline.
- [Vision Language Models (Better, Faster, Stronger)](https://huggingface.co/blog/vlms-2025) — **Hugging Face** — the 2025–26 document and OCR sections track which open models actually read pages well.

**Papers**:
- [ChartQA: A Benchmark for Question Answering about Charts with Visual and Logical Reasoning](https://arxiv.org/abs/2203.10244) — **Masry et al. (2022)** — separates chart *reading* from chart *reasoning*; still the standard chart evaluation.
- [DocVQA: A Dataset for VQA on Document Images](https://arxiv.org/abs/2007.00398) — **Mathew, Karatzas & Jawahar (2021)** — the benchmark that defined document question answering.
- [OCR-free Document Understanding Transformer (Donut)](https://arxiv.org/abs/2111.15664) — **Kim et al. (2022)** — end-to-end image-to-structured-output; the origin of the OCR-free line.
- [olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language Models](https://arxiv.org/abs/2502.18443) — **Poznanski et al. (2025)** — an open, fully documented PDF-to-text pipeline with real throughput and cost numbers.
- [Pix2Struct: Screenshot Parsing as Pretraining for Visual Language Understanding](https://arxiv.org/abs/2210.03347) — **Lee et al. (2023)** — screenshot-to-HTML pretraining plus variable-resolution inputs; strong on charts and user interfaces.
- [SmolDocling: An ultra-compact vision-language model for end-to-end multi-modal document conversion](https://arxiv.org/abs/2503.11576) — **Nassar et al. (2025)** — 256M parameters converting whole pages to structured output; the small-model end of the trade-off.
