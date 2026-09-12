---
id: "15-rag-and-llm-apps/embedding-models-for-retrieval/references"
topic: "Embedding Models for Retrieval — References"
parent: "15-rag-and-llm-apps/embedding-models-for-retrieval"
type: references
updated: 2026-09-07
---

# Embedding Models for Retrieval — references and further reading

> Companion link library for **[Embedding Models for Retrieval](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/embedding-models/embedding-models)** (the concept page). This file holds the curated links — external sources *and* internal links to related pages on this platform — kept separate so it can be reused as a standalone reference list. Grouped by type, best-first. Every entry is a free, no-paywall link from a primary author or a recognized deep explainer — chosen for depth on *this* topic (the embedding model that defines retrieval geometry), not popularity.

**Start here — suggested path**:
1. **See what an embedding *is* for search** — watch [Intro to Sentence Embeddings with Transformers](https://www.youtube.com/watch?v=WS1uVMGhlWQ) (**James Briggs**). *Grounds the "sentence → vector → cosine similarity" pipeline you retrieve with.*
2. **Connect it to retrieval** — watch [Introduction to Semantic Search](https://www.youtube.com/watch?v=OcJZ6XWrTEA) (**Luis Serrano, Cohere**). *Why dense retrieval beats keyword search, told visually.*
3. **Get the asymmetry right** — read [Sentence-Transformers: Semantic Search](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html). *Symmetric vs asymmetric search and how to encode queries vs documents correctly.*
4. **Choose a model deliberately** — read [Choosing an Embedding Model](https://www.pinecone.io/learn/series/rag/embedding-models-rundown/) (**Pinecone**) + the [MTEB blog](https://huggingface.co/blog/mteb) (**Hugging Face**). *How to read the Retrieval task — not the headline average.*
5. **Read the source** — skim [Dense Passage Retrieval](https://arxiv.org/abs/2004.04906) (**Karpukhin et al. 2020**). *The dual-encoder + in-batch negatives that proved dense retrievers beat BM25.*

**Videos**:
- [Intro to Sentence Embeddings with Transformers](https://www.youtube.com/watch?v=WS1uVMGhlWQ) — **James Briggs** — from BERT token vectors to pooled sentence embeddings; the foundation of dense retrieval.
- [Introduction to Semantic Search](https://www.youtube.com/watch?v=OcJZ6XWrTEA) — **Luis Serrano (Cohere)** — clear visual case for embedding-based retrieval over keyword search.
- [Sentence Transformers and Embedding Evaluation](https://www.youtube.com/watch?v=apuDeylm1uE) — **Nils Reimers (Cohere)** — the creator of Sentence-Transformers on how these models are actually trained and, more usefully, how to judge whether one fits *your* corpus rather than a leaderboard.
- [Multilingual and cross-lingual embeddings](https://www.youtube.com/watch?v=Axk4NIk3edg) — **Nils Reimers (Cohere)** — why one vector space can hold many languages, and the failure modes when queries and documents are not in the same one.

**Interactive & visual**:
- [Embedding Projector](https://projector.tensorflow.org/) — **TensorFlow** — explore a real embedding space in 2D/3D; *see* semantically similar text cluster, the geometry retrieval relies on.
- [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) — **Hugging Face** — the live, interactive leaderboard; filter by the **Retrieval** task and your language to choose a model.

**Courses (free)**:
- [Sentence Transformers — official training & usage docs](https://www.sbert.net/) — **Nils Reimers / UKP** — the canonical free guide to using and fine-tuning bi-encoders (pooling, normalization, losses).
- [LangChain: Chat with Your Data — Embeddings & VectorStores](https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/) — **DeepLearning.AI** — hands-on lesson on embedding documents and querying by similarity.

**Articles / blogs (free, no paywall)**:
- [Semantic Search (asymmetric vs symmetric)](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) — **Sentence-Transformers** — the canonical how-to for query vs document encoding and when search is asymmetric.
- [Choosing an Embedding Model](https://www.pinecone.io/learn/series/rag/embedding-models-rundown/) — **Pinecone** — practical rundown of model families and selection criteria for RAG.
- [MTEB: Massive Text Embedding Benchmark](https://huggingface.co/blog/mteb) — **Hugging Face** — what the leaderboard measures and how to read the Retrieval task.
- [Embeddings guide](https://platform.openai.com/docs/guides/embeddings) — **OpenAI** — the maintained reference for `text-embedding-3-small` (1536) / `-large` (3072) and the Matryoshka `dimensions` parameter that lets you truncate them.
- [Introducing Embed v3](https://cohere.com/blog/introducing-embed-v3) — **Cohere** — the embed-v3 family, input types (`search_query`/`search_document`), and the asymmetric treatment baked in.

**Key papers**:
- [Representation Learning with Contrastive Predictive Coding (InfoNCE)](https://arxiv.org/abs/1807.03748) — **van den Oord, Li & Vinyals (2018)** — introduces the **InfoNCE** loss (Eq. 4) used to train retrieval embedders contrastively; the source for the loss on the concept page.
- [Dense Passage Retrieval for Open-Domain QA (DPR)](https://arxiv.org/abs/2004.04906) — **Karpukhin et al. (2020)** — the dual encoder trained with **in-batch negatives**; proved learned dense retrieval beats BM25.
- [Sentence-BERT](https://arxiv.org/abs/1908.10084) — **Reimers & Gurevych (2019)** — siamese/triplet training + mean-pooling that makes BERT usable for fast similarity search (the bi-encoder + pooling on the page).
- [Matryoshka Representation Learning (MRL)](https://arxiv.org/abs/2205.13147) — **Kusupati et al. (2022)** — nested embeddings you can truncate; the source for the dimension-shortening (`dimensions` parameter) on the page.
- [Text Embeddings by Weakly-Supervised Contrastive Pre-training (E5)](https://arxiv.org/abs/2212.03533) — **Wang et al. (2022)** — a leading open retrieval-embedding recipe and the source of the `"query:"`/`"passage:"` asymmetric prefixes.
- [MTEB: Massive Text Embedding Benchmark](https://arxiv.org/abs/2210.07316) — **Muennighoff et al. (2022)** — the benchmark (incl. the Retrieval task) behind the leaderboard you cite when choosing a model.
- [Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models](https://arxiv.org/abs/2506.05176) — **Qwen team (2025)** — the current shape of a strong open embedding family: an instruction-following embedder derived from a general LLM, in several sizes, with Matryoshka dimensions and a matching reranker.
- [ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://arxiv.org/abs/2112.01488) — **Santhanam et al. (2022)** — the alternative to a single pooled vector: keep one embedding per token and score with MaxSim. Worth knowing because 2025-26 stacks increasingly reach for late interaction when one vector per chunk loses too much.

**Books (free, with chapters)**:
- [Speech and Language Processing, 3rd ed. — Ch. 6 "Vector Semantics and Embeddings"](https://web.stanford.edu/~jurafsky/slp3/6.pdf) — **Jurafsky & Martin** — the reference chapter on vector semantics, cosine, and the geometry underlying retrieval embeddings (free PDF).

**In this platform**:
- Concept page (full explanation): [Embedding Models for Retrieval](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/embedding-models/embedding-models)
- Prereqs (the pipeline + chunks this embeds): [01 RAG Fundamentals](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/rag-foundations/rag-foundations) · [02 Document Chunking Strategies](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/chunking/chunking)
- Foundations (the *why* behind vectors & similarity): [ai-ml-intuitions 1.02 Dense Embeddings](/ai-ml/ai-ml-intuitions/representation/embedding-spaces/dense-embeddings-intuition) · [1.06 Vector Similarities — Scaled Dot-Product](/ai-ml/ai-ml-intuitions/representation/similarity-and-distance/scaled-dot-product-intuition) · [06. NLP — Sentence & Document Embeddings](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/sentence-and-document-embeddings/sentence-and-document-embeddings)
- Next in this domain (search the geometry): [04 Vector Databases & ANN Indexes](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/vector-search/vector-search) · [05 Hybrid Search (BM25 + Dense)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/hybrid-search/hybrid-search) · [06 Re-ranking with Cross-Encoders](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/reranking/reranking)
