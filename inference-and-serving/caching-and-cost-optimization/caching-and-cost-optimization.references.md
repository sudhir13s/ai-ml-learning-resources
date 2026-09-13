---
id: "15-rag-and-llm-apps/caching-and-cost-optimization/references"
topic: "Caching & Cost Optimization for LLM Apps — References"
parent: "15-rag-and-llm-apps/caching-and-cost-optimization"
type: references
updated: 2026-09-13
---

# Caching & Cost Optimization — references

> Companion link library for **[Caching & Cost Optimization](/ai-ml/ai-ml-learning-resources/inference-and-serving/caching-and-cost-optimization/caching-and-cost-optimization)** — grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Get the semantic-cache picture** — watch [What is a semantic cache?](https://www.youtube.com/watch?v=AtVTT_s8AGc) (**Redis**). *Embed the query, match a stored one, skip the model call — the loop the page builds.*
2. **Meet the false-hit tradeoff** — read [What is Semantic Caching?](https://redis.io/blog/what-is-semantic-caching/) (**Redis**). *Why a similarity threshold saves money and can also serve the wrong answer.*
3. **Contrast it with prompt caching** — read [Prompt caching with Claude](https://www.anthropic.com/news/prompt-caching) (**Anthropic**). *Exact-prefix reuse inside the provider, and the cache-write against cache-read price split.*
4. **Read the reference design** — read [GPTCache: An Open-Source Semantic Cache for LLM Applications](https://aclanthology.org/2023.nlposs-1.24/) (**Fu Bang, 2023**). *Embed, match by similarity and threshold, serve the stored answer.*
5. **Run a real cache** — run [GPTCache](https://github.com/zilliztech/GPTCache) (**Zilliz**). *The embedding, similarity evaluation, store and eviction pieces as working code.*

**In this platform**:
- [Dense Embeddings (intuition)](/ai-ml/ai-ml-intuitions/representation/embedding-spaces/dense-embeddings-intuition) — the embedding geometry a semantic cache matches on.
- [Hallucination & Grounding](/ai-ml/ai-ml-learning-resources/evaluation/hallucination-and-grounding/hallucination-and-grounding) — the same reject-threshold tradeoff, applied to grounding instead of cache admission.
- [Hybrid Search](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/hybrid-search/hybrid-search) — the dense encoder the cache reuses.
- [Inference Optimization & Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization) — what a cache miss costs on self-hosted hardware, down to dollars per million tokens.
- [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache) — the model-internal cache that prompt and prefix caching reuse across requests.
- [LLM App Orchestration](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/agentic-ai/llm-app-orchestration/llm-app-orchestration) — the pipeline the cache sits in front of.
- [Long-Context vs RAG](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/long-context-vs-rag/long-context-vs-rag) — the token cost model the savings arithmetic reuses.
- [RAG Fundamentals](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/rag-foundations/rag-foundations) — the retrieve-then-generate call a semantic hit skips.
- [Retrieval-Augmented Generation (intuition)](/ai-ml/ai-ml-intuitions/memory-retrieval-and-context/retrieval-augmented-generation/rag-intuition) — the *why* behind the pipeline being cached.
- [Vector Databases & ANN](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/vector-search/vector-search) — fast nearest-neighbour lookup for a large cache.

**Videos**:
- [What is a semantic cache?](https://www.youtube.com/watch?v=AtVTT_s8AGc) — **Redis** — a short breakdown of how a semantic cache skips redundant LLM calls by matching similar queries.

**Courses**:
- [Efficiently Serving LLMs](https://www.deeplearning.ai/courses/efficiently-serving-llms) — **DeepLearning.AI × Predibase** — KV caching, batching, quantization and LoRA serving built up in code, the machinery behind the cost of a miss.
- [LangChain for LLM Application Development](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/) — **DeepLearning.AI × LangChain** — caching and efficient chains as part of building real apps.

**Articles**:
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — **Anthropic (2025)** — why a stable, append-only context prefix is a cost decision: every edit above the breakpoint throws away the cache.
- [Prompt caching with Claude](https://www.anthropic.com/news/prompt-caching) — **Anthropic** — the explicit-breakpoint model and the cache-write vs cache-read price split.
- [What is Semantic Caching?](https://redis.io/blog/what-is-semantic-caching/) — **Redis** — how similarity-based caching works, the false-hit risk, and when it pays off.

**Papers**:
- [Efficient Memory Management for LLM Serving with PagedAttention (vLLM)](https://arxiv.org/abs/2309.06180) — **Kwon et al. (2023)** — the block-sharing substrate behind engine-side prefix caching.
- [GPT Semantic Cache: Reducing LLM Costs and Latency via Semantic Embedding Caching](https://arxiv.org/abs/2411.05276) — **Regmi & Pun (2024)** — embedding-based query caching; up to ~68% fewer API calls, with the similarity-threshold tradeoff.
- [GPTCache: An Open-Source Semantic Cache for LLM Applications Enabling Faster Answers and Cost Savings](https://aclanthology.org/2023.nlposs-1.24/) — **Fu Bang (2023, NLP-OSS @ EMNLP)** — the reference semantic cache: embed, match by similarity and threshold, serve the stored answer.
- [MeanCache: User-Centric Semantic Caching for LLM Web Services](https://arxiv.org/abs/2403.02694) — **Gill et al. (2024)** — a privacy-aware, per-user semantic cache and the false-hit calibration problem.
- [Prompt Cache: Modular Attention Reuse for Low-Latency Inference](https://arxiv.org/abs/2311.04934) — **Gim et al. (2023, MLSys 2024)** — reusing precomputed attention for recurring prompt segments; the mechanism behind provider prompt caching.

**Documentation**:
- [Automatic prefix caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching.html) — **vLLM** — hashing KV blocks so a shared prefix is computed once; on by default since vLLM V1.
- [LangChain — LLM caching (how-to)](https://python.langchain.com/docs/how_to/llm_caching/) — **LangChain** — `set_llm_cache(InMemoryCache())` and semantic-cache backends, the API used on the page.
- [LLM inference optimization](https://huggingface.co/docs/transformers/en/llm_optims) — **Hugging Face Transformers** — caching, batching, and the latency and cost levers in runnable code.
- [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) — **Anthropic** — the `cache_control` request format, TTLs, and cache-write and cache-read pricing.
- [Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching) — **OpenAI** — automatic prefix caching, the 1,024-token minimum, and the cached-token discount.

**Books**:
- [AI Engineering](https://huyenchip.com/books/) — **Chip Huyen (2025)** — the inference-optimization chapter: latency, throughput, and caching layers for foundation-model applications.

**Resources**:
- [GPTCache](https://github.com/zilliztech/GPTCache) — **Zilliz** — the reference semantic-cache library to read and run: embedding, similarity evaluation, cache store, and eviction.
