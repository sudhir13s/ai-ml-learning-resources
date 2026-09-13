---
id: "multimodal-and-generative-media/multimodal-learning/multimodal-rag/references"
topic: "Multimodal RAG — References"
parent: "multimodal-and-generative-media/multimodal-learning/multimodal-rag"
type: references
updated: 2026-09-13
---

# Multimodal RAG — references

> Companion link library for **[Multimodal RAG](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/multimodal-learning/multimodal-rag/multimodal-rag)** (the teaching page). Internal links and external sources, grouped by type and alphabetical within each group.

**Start here — suggested path**:

1. **Anchor on text RAG first** — read [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — **Lewis et al. (2020)**. *The original retrieve-then-generate formulation everything here extends.*
2. **Learn late interaction** — read [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://arxiv.org/abs/2004.12832) — **Khattab & Zaharia (2020)**. *MaxSim scoring over token embeddings — the machinery ColPali moves to image patches.*
3. **Read the paper that changed the pipeline** — read [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/abs/2407.01449) — **Faysse et al. (2025)**. *Page images in, multi-vector embeddings out, no OCR stage; plus the ViDoRe benchmark.*
4. **Hear the author explain the trade-offs** — watch [ColPali: Document Retrieval with Vision-Language Models only](https://www.youtube.com/watch?v=5zbwT4j_9KY) — **Manuel Faysse, interviewed on Zeta Alpha's Neural Search Talks**. *Where it wins, and the index-size problem it creates.*
5. **Build one end to end** — follow [Multimodal RAG using document retrieval and VLMs](https://huggingface.co/learn/cookbook/multimodal_rag_using_document_retrieval_and_vlms) — **Hugging Face Cookbook**. *A complete notebook: index page images, retrieve, answer with a VLM.*

**In this platform**:
- Measuring it: [RAG Evaluation](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/rag-evaluation/rag-evaluation) · [Multimodal Benchmarks and Evaluation](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/multimodal-learning/multimodal-benchmarks-and-evaluation/multimodal-benchmarks-and-evaluation)
- Prerequisites: [RAG Foundations](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/rag-foundations/rag-foundations) · [Embedding Models](/ai-ml/ai-ml-learning-resources/data-and-representation/embedding-models/embedding-models) · [Document and Chart Understanding](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/multimodal-learning/document-and-chart-understanding/document-and-chart-understanding)
- Retrieval machinery: [Vector Search](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/vector-search/vector-search) · [Hybrid Search](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/hybrid-search/hybrid-search) · [Reranking](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/reranking/reranking) · [Chunking](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/chunking/chunking)

**Videos**:
- [ColPali: Document Retrieval with Vision-Language Models only (with Manuel Faysse)](https://www.youtube.com/watch?v=5zbwT4j_9KY) — **Zeta Alpha (Neural Search Talks)** — the author on design, benchmarks and the storage cost of multi-vector indexes.

**Courses**:
- [Building Multimodal Search and RAG](https://www.deeplearning.ai/short-courses/building-multimodal-search-and-rag/) — **DeepLearning.AI × Weaviate** — free short course on shared-embedding multimodal retrieval and generation.
- [Multimodal RAG using document retrieval and VLMs](https://huggingface.co/learn/cookbook/multimodal_rag_using_document_retrieval_and_vlms) — **Hugging Face Cookbook** — the runnable reference implementation of the ColPali-style pipeline.
- [Multimodal RAG: Chat with Videos](https://www.deeplearning.ai/short-courses/multimodal-rag-chat-with-videos/) — **DeepLearning.AI × Intel** — free short course extending the pattern to video with frame-plus-transcript retrieval.

**Articles**:
- [ColPali codebase](https://github.com/illuin-tech/colpali) — **Illuin Technology** — training and inference code for ColPali, ColQwen and ColSmol.
- [ColPali: Efficient Document Retrieval with Vision Language Models](https://huggingface.co/blog/manu/colpali) — **Manuel Faysse** — the author's own walkthrough, shorter than the paper and with the motivation up front.
- [Retrieval with vision language models — ColPali](https://blog.vespa.ai/retrieval-with-vision-language-models-colpali/) — **Vespa** — a search-engine team's implementation notes: index layout, memory, and query latency in practice.
- [ViDoRe leaderboard](https://huggingface.co/spaces/vidore/vidore-leaderboard) — **ColPali team / Hugging Face** — the live visual document retrieval leaderboard; check before choosing a retriever.

**Papers**:
- [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://arxiv.org/abs/2004.12832) — **Khattab & Zaharia (2020)** — the late-interaction scoring ColPali generalizes to patches.
- [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/abs/2407.01449) — **Faysse et al. (2025)** — page-image embeddings with late interaction, plus ViDoRe; the reference method for visual document retrieval.
- [M3DocRAG: Multi-modal Retrieval is What You Need for Multi-page Multi-document Understanding](https://arxiv.org/abs/2411.04952) — **Cho et al. (2024)** — scales visual retrieval to many long documents, where single-page methods break.
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — **Lewis et al. (2020)** — the original RAG formulation and its training story.
- [VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents](https://arxiv.org/abs/2410.10594) — **Yu et al. (2024)** — measures how much information the text-extraction step throws away, end to end.
