---
id: "15-rag-and-llm-apps/embedding-models-for-retrieval/references"
topic: "Embedding Models for Retrieval — References"
parent: "15-rag-and-llm-apps/embedding-models-for-retrieval"
type: references
updated: 2026-09-13
---

# Embedding Models for Retrieval — references

> Companion link library for **[Embedding Models for Retrieval](/ai-ml/ai-ml-learning-resources/data-and-representation/embedding-models/embedding-models)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **See what an embedding is for search** — watch [Intro to Sentence Embeddings with Transformers](https://www.youtube.com/watch?v=WS1uVMGhlWQ) (**James Briggs**). *Grounds the sentence → vector → cosine pipeline that retrieval runs on.*
2. **Connect it to retrieval** — watch [Introduction to Semantic Search](https://www.youtube.com/watch?v=OcJZ6XWrTEA) (**Luis Serrano, Cohere**). *Why dense retrieval beats keyword search, told visually.*
3. **Get the asymmetry right** — read [Semantic Search: symmetric and asymmetric](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) (**Sentence-Transformers**). *How to encode queries versus documents.*
4. **Choose a model deliberately** — read [Choosing an Embedding Model](https://www.pinecone.io/learn/series/rag/embedding-models-rundown/) (**Pinecone**) and the [MTEB blog](https://huggingface.co/blog/mteb) (**Hugging Face**). *Read the Retrieval task, not the headline average.*
5. **Read the source** — skim [Dense Passage Retrieval](https://arxiv.org/abs/2004.04906) (**Karpukhin et al. 2020**). *The dual encoder and in-batch negatives that proved dense retrievers beat BM25.*

**In this platform**:
- Intuition behind vectors and similarity: [Dense Embeddings](/ai-ml/ai-ml-intuitions/representation/embedding-spaces/dense-embeddings-intuition) · [Scaled Dot-Product](/ai-ml/ai-ml-intuitions/representation/similarity-and-distance/scaled-dot-product-intuition)
- Interview framing of the same material: [Embeddings and Similarity Search](/ai-ml/ai-ml-learning-resources/data-and-representation/embedding-models/embeddings-and-similarity-search)
- Searching the geometry this model builds: [Hybrid Search](/ai-ml/practitioner-workflows/llm-applications/hybrid-search/hybrid-search) · [Re-ranking](/ai-ml/practitioner-workflows/llm-applications/reranking/reranking) · [Vector Search](/ai-ml/ai-ml-learning-resources/data-and-representation/vector-search/vector-search)
- Applied inside an application: [RAG Pipeline](/ai-ml/practitioner-workflows/llm-applications/rag-pipeline)
- Sentence and document embeddings in language processing: [Sentence and Document Embeddings](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/sentence-and-document-embeddings/sentence-and-document-embeddings)

**Videos**:
- [Intro to Sentence Embeddings with Transformers](https://www.youtube.com/watch?v=WS1uVMGhlWQ) — **James Briggs** — from BERT token vectors to pooled sentence embeddings; the foundation of dense retrieval.
- [Introduction to Semantic Search](https://www.youtube.com/watch?v=OcJZ6XWrTEA) — **Luis Serrano (Cohere)** — a clear visual case for embedding-based retrieval over keyword search.
- [Multilingual and cross-lingual embeddings](https://www.youtube.com/watch?v=Axk4NIk3edg) — **Nils Reimers (Cohere)** — why one vector space can hold many languages, and the failure modes when queries and documents are not in the same one.
- [Sentence Transformers and Embedding Evaluation](https://www.youtube.com/watch?v=apuDeylm1uE) — **Nils Reimers (Cohere)** — how these models are trained and how to judge whether one fits your corpus rather than a leaderboard.

**Courses**:
- [LangChain: Chat with Your Data — Embeddings and VectorStores](https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/) — **DeepLearning.AI** — a hands-on lesson on embedding documents and querying by similarity.

**Interactive**:
- [Embedding Projector](https://projector.tensorflow.org/) — **TensorFlow** — explore a real embedding space in 2D and 3D, and watch semantically similar text cluster.
- [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) — **Hugging Face** — the live leaderboard; filter by the Retrieval task and your language to choose a model.

**Articles**:
- [Choosing an Embedding Model](https://www.pinecone.io/learn/series/rag/embedding-models-rundown/) — **Pinecone** — a practical rundown of model families and selection criteria.
- [Introducing Embed v3](https://cohere.com/blog/introducing-embed-v3) — **Cohere** — the embed-v3 family and its input types (`search_query` / `search_document`), with the asymmetric treatment baked in.
- [MTEB: Massive Text Embedding Benchmark](https://huggingface.co/blog/mteb) — **Hugging Face** — what the leaderboard measures and how to read the Retrieval task rather than the headline average.

**Papers**:
- [ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://arxiv.org/abs/2112.01488) — **Santhanam et al. (2022)** — one embedding per token scored with MaxSim, the alternative when one pooled vector per chunk loses too much.
- [Dense Passage Retrieval for Open-Domain Question Answering](https://arxiv.org/abs/2004.04906) — **Karpukhin et al. (2020)** — the dual encoder trained with in-batch negatives; proved learned dense retrieval beats BM25.
- [Matryoshka Representation Learning](https://arxiv.org/abs/2205.13147) — **Kusupati et al. (2022)** — nested embeddings you can truncate; the source for dimension shortening on the concept page.
- [MTEB: Massive Text Embedding Benchmark](https://arxiv.org/abs/2210.07316) — **Muennighoff et al. (2022)** — the benchmark, including the Retrieval task, behind the leaderboard.
- [Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models](https://arxiv.org/abs/2506.05176) — **Qwen team (2025)** — an instruction-following embedder derived from a general language model, in several sizes, with Matryoshka dimensions and a matching reranker.
- [Representation Learning with Contrastive Predictive Coding](https://arxiv.org/abs/1807.03748) — **van den Oord, Li and Vinyals (2018)** — introduces the InfoNCE loss used to train retrieval embedders contrastively.
- [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084) — **Reimers and Gurevych (2019)** — siamese training plus mean pooling that made BERT usable for fast similarity search.
- [Text Embeddings by Weakly-Supervised Contrastive Pre-training](https://arxiv.org/abs/2212.03533) — **Wang et al. (2022)** — the E5 recipe and the source of the `query:` / `passage:` asymmetric prefixes.

**Documentation**:
- [Embeddings guide](https://platform.openai.com/docs/guides/embeddings) — **OpenAI** — the maintained reference for `text-embedding-3-small` and `-large`, and the Matryoshka `dimensions` parameter.
- [Semantic Search: symmetric and asymmetric](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) — **Sentence-Transformers** — how to encode queries versus documents, and when search is asymmetric.
- [Sentence Transformers](https://www.sbert.net/) — **Nils Reimers / UKP Lab** — the canonical guide to using and fine-tuning bi-encoders: pooling, normalization and losses.

**Books**:
- [*Introduction to Information Retrieval* — Ch. 6 "Scoring, term weighting and the vector space model"](https://nlp.stanford.edu/IR-book/html/htmledition/scoring-term-weighting-and-the-vector-space-model-1.html) — **Manning, Raghavan and Schütze** — free online; the vector-space cosine that the concept page derives by hand.
- [*Speech and Language Processing* (3rd ed.) — Ch. 6 "Vector Semantics and Embeddings"](https://web.stanford.edu/~jurafsky/slp3/6.pdf) — **Jurafsky and Martin** — the reference chapter on vector semantics, cosine and the geometry underneath retrieval embeddings.
