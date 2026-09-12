---
id: "15-rag-and-llm-apps/re-ranking-cross-encoders/references"
topic: "Re-ranking (Cross-Encoders) — References"
parent: "15-rag-and-llm-apps/re-ranking-cross-encoders"
type: references
updated: 2026-09-07
---

# Re-ranking with Cross-Encoders — references and further reading

> Companion link library for **[Re-ranking with Cross-Encoders](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/reranking/reranking)** (the concept page). This file holds the curated links — external sources *and* internal links to related pages on this platform — kept separate so it can be reused as a standalone reference list. Grouped by type, best-first. Every entry is a free, no-paywall link from a primary author or a recognized deep explainer — chosen for depth on *this* topic (two-stage retrieve-then-rerank and the cross-encoder that does the precision stage), not popularity.

**Start here — suggested path**:
1. **Get the two-stage picture** — read [Rerankers and Two-Stage Retrieval](https://www.pinecone.io/learn/series/rag/rerankers/) (**Pinecone**). *Why a cheap recall stage + an accurate rerank stage beats either alone.*
2. **See the architecture difference** — read [Retrieve & Re-Rank](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) (**Sentence-Transformers**). *Bi-encoder (independent) vs cross-encoder (joint) encoding, with runnable code.*
3. **See it in a pipeline** — read [rerankers: a lightweight unified API](https://www.answer.ai/posts/2024-09-16-rerankers.html) (**Benjamin Clavié, Answer.AI**). *Cross-encoders, late-interaction models, LLM rerankers and hosted APIs behind one interface — the honest comparison of what each costs and buys.*
4. **Read the cross-encoder source** — skim [Passage Re-ranking with BERT](https://arxiv.org/abs/1901.04085) (**Nogueira & Cho 2019**). *The paper that established BERT cross-encoders as re-rankers — the score on the page.*
5. **Understand why two stages** — skim [Sentence-BERT](https://arxiv.org/abs/1908.10084) (**Reimers & Gurevych 2019**), §1–2. *The cost argument (a forward pass per pair) that forces bi-encoder retrieval + cross-encoder re-ranking.*

**Videos**:
- [Sentence Transformers and Embedding Evaluation](https://www.youtube.com/watch?v=apuDeylm1uE) — **Nils Reimers (Cohere)** — the author of Sentence-Transformers on bi-encoders versus cross-encoders and how to evaluate either honestly; the argument this page's two-stage design rests on.
- [Semantic Search and Reranking with Cohere and Pinecone](https://www.youtube.com/watch?v=e7x1wJlmDjs) — **Pinecone** — a full two-stage retrieve-then-rerank pipeline.
- [Supercharging Semantic Search with Pinecone and Cohere](https://www.youtube.com/watch?v=e2g5ya4ZFro) — **Pinecone** — how reranking refines vector-search results in practice.

**Interactive & visual**:
- [Retrieve & Re-Rank — Sentence-Transformers docs (with code)](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) — **Nils Reimers / UKP** — the canonical bi-encoder-retrieve + cross-encoder-rerank example you can run and modify.
- [Pretrained Cross-Encoders (model list + accuracy/speed table)](https://www.sbert.net/docs/cross_encoder/pretrained_models.html) — **Sentence-Transformers** — the actual `ms-marco-MiniLM` re-ranker zoo with their accuracy/latency tradeoffs, for picking a model.

**Courses (free)**:
- [Building & Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) — **DeepLearning.AI × LlamaIndex** — covers sentence-window retrieval + re-ranking as a core precision upgrade, with evaluation.
- [Sentence Transformers — Cross-Encoder docs (train & apply)](https://www.sbert.net/examples/cross_encoder/applications/README.html) — **UKP / Nils Reimers** — the free reference for training and applying cross-encoder re-rankers.

**Articles / blogs (free, no paywall)**:
- [Rerankers and Two-Stage Retrieval](https://www.pinecone.io/learn/series/rag/rerankers/) — **Pinecone** — the canonical explainer of why and how reranking works, with the two-stage funnel.
- [Retrieve & Re-Rank](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) — **Sentence-Transformers** — the bi-encoder + cross-encoder pattern with code.
- [Search Reranking with Cross-Encoders](https://developers.openai.com/cookbook/examples/search_reranking_with_cross-encoders) — **OpenAI Cookbook** — a worked example of re-ranking retrieved candidates.
- [Introducing Rerank 3](https://cohere.com/blog/rerank-3) — **Cohere** — what a production rerank endpoint does, its inputs/outputs, and when to use it.
- [Introducing Rerank 3.5](https://cohere.com/blog/rerank-3pt5) — **Cohere (2024–25)** — the current generation: multilingual, long-document, and structured (JSON/table) reranking, with the reasoning-focused evaluation numbers.
- [rerankers: a lightweight unified API for reranking](https://www.answer.ai/posts/2024-09-16-rerankers.html) — **Benjamin Clavié (Answer.AI)** — one interface over cross-encoders, ColBERT-style late interaction, LLM rerankers and hosted APIs, with a candid account of when each is worth its latency.
- [Late interaction models: what they are and why they matter](https://qdrant.tech/articles/late-interaction-models/) — **Qdrant** — ColBERT-style per-token scoring positioned against both bi-encoders and cross-encoders; the 2025-26 third option in this design space.
- [BGE-Reranker (FlagEmbedding) — model card & usage](https://huggingface.co/BAAI/bge-reranker-large) — **BAAI** — the leading open cross-encoder re-ranker family (`bge-reranker-base/large/v2-m3`), with usage and the relevance-score semantics.

**Key papers / primary sources**:
- [Passage Re-ranking with BERT](https://arxiv.org/abs/1901.04085) — **Nogueira & Cho (2019)** — feeds `[CLS] query [SEP] passage` through BERT with a linear relevance head; the cross-encoder re-ranker score on the page is taken from §3.
- [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084) — **Reimers & Gurevych (2019)** — the bi-encoder (SBERT) and the cost argument (a forward pass per pair) that motivates retrieve-then-rerank; the source for the cost-asymmetry section.
- [Cumulated Gain-based Evaluation of IR Techniques](https://dl.acm.org/doi/10.1145/582415.582418) — **Järvelin & Kekäläinen (ACM TOIS 2002)** — introduces DCG / nDCG with the $\log_2(i+1)$ rank discount; the ranking metric defined and used on the page.
- [The TREC-8 Question Answering Track Report](https://trec.nist.gov/pubs/trec8/papers/qa_report.pdf) — **Voorhees (1999)** — the QA-track evaluation that introduced **mean reciprocal rank** (MRR), averaging $1/\text{rank}$ of the first correct answer; the origin of the MRR metric on the page.
- [ColBERT: Efficient Passage Search via Contextualized Late Interaction over BERT](https://arxiv.org/abs/2004.12832) — **Khattab & Zaharia (2020)** — per-token embeddings + late MaxSim interaction; the precomputable middle ground between bi- and cross-encoders.
- [MS MARCO: A Human-Generated Machine Reading Comprehension Dataset](https://arxiv.org/abs/1611.09268) — **Bajaj et al. (2016)** — the passage-ranking dataset the `ms-marco-MiniLM` re-rankers (and most open cross-encoders) are trained on.
- [BEIR: A Heterogeneous Benchmark for Zero-Shot Evaluation of IR Models](https://arxiv.org/abs/2104.08663) — **Thakur et al. (2021)** — the benchmark suite (scifact is one of its tasks) used on the page to measure the re-ranking lift against real relevance labels; shows cross-encoder re-ranking gains (and limits) across diverse retrieval tasks.
- [Document Ranking with a Pretrained Sequence-to-Sequence Model (MonoT5)](https://arxiv.org/abs/2003.06713) — **Nogueira, Jiang, Pradeep & Lin (2020)** — re-ranking as *generation*: a T5 emits "true"/"false" for a (query, passage) pair and the softmax over those tokens is the relevance score; the seq2seq alternative to the encoder cross-encoder discussed on the page.
- [Is ChatGPT Good at Search? Investigating LLMs as Re-Ranking Agents (RankGPT)](https://arxiv.org/abs/2304.09542) — **Sun et al. (2023, EMNLP)** — listwise reranking: hand the model a *window* of candidates and have it order them, rather than scoring each pair alone. The strongest zero-shot reranker, and the reason "just ask the LLM to rank" is now a real option with a real cost.
- [ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction](https://arxiv.org/abs/2112.01488) — **Santhanam et al. (2022)** — the compressed, practical version of ColBERT; the basis of the late-interaction rerankers that ship in 2025-26 stacks.

**Data & models used on this page (all free / open, for exact reproducibility)**:
- [BeIR/scifact](https://huggingface.co/datasets/BeIR/scifact) + [BeIR/scifact-qrels](https://huggingface.co/datasets/BeIR/scifact-qrels) — **Wadden et al. / BeIR** — the real scientific-claim retrieval benchmark (5,183 abstracts, 300 test queries, human relevance judgments) the page's nDCG/MRR are measured on.
- [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) — **UKP / Sentence-Transformers** — the real 384-dim bi-encoder used for first-stage retrieval.
- [cross-encoder/ms-marco-MiniLM-L-6-v2](https://huggingface.co/cross-encoder/ms-marco-MiniLM-L-6-v2) — **Sentence-Transformers** — the real cross-encoder re-ranker whose relevance logits reorder the pool.

**Books (free, with chapters)**:
- [Introduction to Information Retrieval — Ch. 8 "Evaluation in information retrieval"](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-in-information-retrieval-1.html) — **Manning, Raghavan & Schütze** — the IR evaluation foundations (precision, MAP, the lineage of nDCG) behind measuring a re-ranker, free online.
- [Speech and Language Processing, 3rd ed. — Ch. 14 "Question Answering and Information Retrieval"](https://web.stanford.edu/~jurafsky/slp3/14.pdf) — **Jurafsky & Martin** — dense retrieval, re-ranking, and ranking metrics in one reference chapter (free PDF).

**In this platform**:
- Concept page (full explanation): [Re-ranking with Cross-Encoders](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/reranking/reranking)
- Prereqs (the first stage this re-ranks): [03 Embedding Models for Retrieval](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/embedding-models/embedding-models) · [04 Vector Databases & ANN Indexes](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/vector-search/vector-search) · [05 Hybrid Search (BM25 + Dense)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/hybrid-search/hybrid-search)
- Foundations (the *why* behind attention & similarity): [ai-ml-intuitions 1.06 Vector Similarities — Scaled Dot-Product](/ai-ml/ai-ml-intuitions/representation/similarity-and-distance/scaled-dot-product-intuition) · [05. Deep Learning — Attention Mechanism](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/attention-mechanism/attention-mechanism) · [06. NLP — Information Retrieval & Semantic Search](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/information-retrieval-and-semantic-search/information-retrieval-and-semantic-search)
- Next in this domain (raise the recall ceiling re-ranking is bounded by): [07 Query Transformation (HyDE, Multi-Query)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/query-transformation/query-transformation)
