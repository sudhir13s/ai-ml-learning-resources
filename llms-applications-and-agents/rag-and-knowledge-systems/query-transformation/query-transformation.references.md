---
id: "15-rag-and-llm-apps/query-transformation-hyde-multi-query/references"
topic: "Query Transformation (HyDE & Multi-Query) — References"
parent: "15-rag-and-llm-apps/query-transformation-hyde-multi-query"
type: references
updated: 2026-09-07
---

# Query Transformation (HyDE & Multi-Query) — references and further reading

> Companion link library for **[Query Transformation (HyDE & Multi-Query)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/query-transformation/query-transformation)** (the concept page). This file holds the curated links — external sources *and* internal links to related pages on this platform — kept separate so it can be reused as a standalone reference list. Grouped by type, best-first. Every entry is free/open (no paywall) and chosen for depth on *this* topic — the question↔document asymmetry, HyDE, Multi-Query / RAG-Fusion, and the fusion that ties them together.

**Start here — suggested path**:
1. **Feel the problem** — read [the HyDE paper](https://arxiv.org/abs/2212.10496) (**Gao et al. 2022**), abstract + §1–3. *Why a hypothetical answer is a better retrieval probe than the raw question — the core idea, stated cleanly.*
2. **See it as query expansion** — read [query2doc](https://arxiv.org/abs/2303.07678) (**Wang et al. 2023**). *The append-the-pseudo-document variant, with concrete BM25 gains — sharpens the "replace vs append" distinction.*
3. **Build Multi-Query** — read [LangChain's MultiQueryRetriever how-to](https://python.langchain.com/docs/how_to/MultiQueryRetriever/) (**LangChain**). *Generate N reformulations, retrieve each, return the unique union — the pattern the page builds by hand.*
4. **Add the fusion** — read [RAG-Fusion: A New Take on Retrieval-Augmented Generation](https://arxiv.org/abs/2402.03367) (**Rackauckas 2024**). *Multi-Query + reciprocal rank fusion evaluated properly — the pattern most production stacks default to, with its failure cases named.*
5. **Wire HyDE in a framework** — read [LlamaIndex's HyDE query-transform docs](https://developers.llamaindex.ai/python/framework/optimizing/advanced_retrieval/query_transformations/). *`HyDEQueryTransform` + `TransformQueryEngine`, the library one-liner and its knobs.*

**Videos**:
- [RAG from Scratch, Part 6 — Query Translation and RAG-Fusion](https://www.youtube.com/watch?v=77qELPbNgxA) — **LangChain (Lance Martin)** — the multi-query + reciprocal-rank-fusion pattern built step by step by the maintainer who wrote the reference implementation.
- [Advanced RAG 05 — HyDE: Hypothetical Document Embeddings](https://www.youtube.com/watch?v=v_BnBEubv58) — **Sam Witteveen** — the paper's idea in plain terms, with the "a wrong hypothetical still retrieves the right neighbourhood" intuition.
- [Stanford CS25: Retrieval-Augmented Language Models](https://www.youtube.com/watch?v=mE7IDf2SmJg) — **Douwe Kiela (Stanford Online)** — why the query side, not just the index, is where most retrieval quality is won or lost.

**Interactive & visual**:
- [Nearest-neighbour / embedding explorer (TensorFlow Embedding Projector)](https://projector.tensorflow.org/) — **Google** — project real embeddings to 2D/3D and *see* the question↔answer gap the page measures, on your own text.
- [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) — **Hugging Face** — the retrieval benchmark to sanity-check any encoder you'd pair with HyDE/Multi-Query.

**Courses (free)**:
- [LangChain — RAG from Scratch (query translation)](https://github.com/langchain-ai/rag-from-scratch) — **LangChain** — the notebooks behind the videos above: multi-query, RAG-fusion, decomposition, step-back, and HyDE, each runnable.
- [DeepLearning.AI — Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) — **DeepLearning.AI + LlamaIndex (free short course)** — query transformation inside a full advanced-RAG pipeline, with evaluation.

**Articles / blogs (free, no paywall)**:
- [Query Transformations](https://blog.langchain.com/query-transformations/) — **Lance Martin (LangChain)** — the taxonomy of query rewrites in one place, from the maintainer's own blog.
- [How to use the MultiQueryRetriever](https://python.langchain.com/docs/how_to/MultiQueryRetriever/) — **LangChain docs** — the exact API the page cites (default 3 reformulations, unique union), with a runnable example.
- [Query Transformations](https://blog.langchain.dev/query-transformations/) — **LangChain blog (Lance Martin)** — a taxonomy of query rewrites (rewrite-retrieve-read, multi-query, HyDE, decomposition, step-back) and when each applies.
- [Advanced Retrieval — Query Transformations (HyDE)](https://developers.llamaindex.ai/python/framework/optimizing/advanced_retrieval/query_transformations/) — **LlamaIndex docs** — `HyDEQueryTransform` + `TransformQueryEngine`, including the "HyDE can produce nonsense" caveat the pitfalls section echoes.
- [Query Expansion by Prompting Large Language Models](https://arxiv.org/abs/2305.03653) — **Jagerman, Zhuang, Qin, Wang & Bendersky (2023, Google)** — the controlled study of LLM-generated query expansion against classical pseudo-relevance feedback: which prompt style helps, and by how much.

**Key papers**:
- [Precise Zero-Shot Dense Retrieval without Relevance Labels (HyDE)](https://arxiv.org/abs/2212.10496) — **Gao, Ma, Lin & Callan (2022)** — the HyDE paper: generate a hypothetical document, encode it, retrieve; the encoder's "dense bottleneck filters out the incorrect details." The primary source for this page's HyDE section.
- [Query2doc: Query Expansion with Large Language Models](https://arxiv.org/abs/2303.07678) — **Wang, Yang & Wei (2023)** — the append-the-pseudo-document variant; +3–15% for BM25 on MS-MARCO / TREC DL, and gains for dense retrievers, without fine-tuning.
- [Reciprocal Rank Fusion outperforms Condorcet and individual Rank Learning Methods](https://doi.org/10.1145/1571941.1572114) — **Cormack, Clarke & Büttcher (SIGIR 2009)** — the RRF paper: the $k=60$ default and the "high in any list wins" rank fusion the Multi-Query section reuses. ([free PDF](https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf))
- [Query Rewriting for Retrieval-Augmented Large Language Models (Rewrite-Retrieve-Read)](https://arxiv.org/abs/2305.14283) — **Ma, Gong, He, Zhao & Duan (2023)** — a trainable query-rewriter placed before retrieval; the "learn the transform" end of the design space.
- [Take a Step Back: Evoking Reasoning via Abstraction (Step-Back Prompting)](https://arxiv.org/abs/2310.06117) — **Zheng et al. (2023, Google DeepMind)** — the step-back transform (ask a more general question first), a sibling query rewrite for reasoning-heavy retrieval.
- [Dense Passage Retrieval for Open-Domain QA (DPR)](https://arxiv.org/abs/2004.04906) — **Karpukhin et al. (2020)** — the bi-encoder retrieval this page transforms the input to; grounds the question↔document asymmetry (separate query/passage encoders).

**Books (free chapters)**:
- [Speech and Language Processing, 3rd ed. — Ch. 14 "Question Answering & Information Retrieval"](https://web.stanford.edu/~jurafsky/slp3/14.pdf) — **Jurafsky & Martin** — dense retrieval, the query/passage encoders, and the retrieval metrics (recall@k, MRR) this page measures against.

**In this platform**:
- Concept page (full explanation): [Query Transformation (HyDE & Multi-Query)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/query-transformation/query-transformation)
- Foundations this builds on: [RAG Fundamentals](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/rag-foundations/rag-foundations) · [Embedding Models for Retrieval](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/embedding-models/embedding-models) · [Hybrid Search (BM25 + Dense) — the RRF this page reuses](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/hybrid-search/hybrid-search)
- Puts it to work: [Re-ranking with Cross-Encoders (the backstop after transformation)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/reranking/reranking) · [Advanced RAG (Parent-Doc, Fusion, Self-RAG)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/advanced-rag/advanced-rag) · [Agentic RAG (query decomposition, multi-hop)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/agentic-rag/agentic-rag)
- Measure it: [RAG Evaluation (recall@k, MRR, and the metrics this page reports)](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/rag-evaluation/rag-evaluation)
