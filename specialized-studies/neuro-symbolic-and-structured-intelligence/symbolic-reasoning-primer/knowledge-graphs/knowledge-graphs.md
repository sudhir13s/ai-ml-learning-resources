---
id: "specialized-studies/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-graphs"
topic: "Knowledge Graphs"
level: intermediate
built_from: ["knowledge-representation", "logic-and-inference"]
leads_to: ["specialized-studies/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai", "specialized-studies/neuro-symbolic-and-structured-intelligence/structured-reasoning/causal-and-relational-reasoning"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Knowledge Graphs"
minutes: 16
category: symbolic-reasoning-primer
---

# Knowledge Graphs
> Knowledge stored as a graph of **entities and typed relations** — usually as subject-predicate-object
> triples in the Resource Description Framework (RDF), optionally with an ontology in the Web
> Ontology Language (OWL) that lets a reasoner derive facts nobody wrote down. Two ways to use one:
> **query it** (SPARQL, Cypher) for exact answers, or **embed it** (TransE and successors) so that
> missing links can be predicted.

**Why it matters:** knowledge graphs are the symbolic memory that large language models keep being
attached to. Graph-structured retrieval, entity-grounded answers, provenance you can show a
regulator, and multi-hop questions that vector search answers badly — all of it runs through this
representation. The 2026 interview version is: *when does a graph beat a vector index, and what
does maintaining one actually cost?*

**Start here — suggested path:**

1. **Get the data model** — read [*Knowledge Graphs*](https://kgbook.org/) Ch. 2 "Data Graphs" — **Hogan, Blomqvist, Cochez et al.** *Directed labelled graphs, RDF triples, property graphs, and how they differ.*
2. **Query a real one** — work through the [Wikidata SPARQL tutorial](https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial) — **Wikimedia (Wikidata community)**. *Fifty million entities, live, in your browser; multi-hop queries stop being abstract.*
3. **Learn the schema and reasoning layer** — read [*Knowledge Graphs*](https://kgbook.org/) Ch. 4 "Schema, Identity, Context" — **Hogan et al.** *Ontologies, entailment, and the identity problems that sink real deployments.*
4. **Learn the embedding view** — read [A Review of Relational Machine Learning for Knowledge Graphs](https://arxiv.org/abs/1503.00759) — **Nickel, Murphy, Tresp & Gabrilovich (2015)**. *Latent-factor models for link prediction — the statistical half of the subject.*
5. **See the 2025 pairing with language models** — read [Unifying Large Language Models and Knowledge Graphs: A Roadmap](https://arxiv.org/abs/2306.08302) — **Pan, Luo, Wang, Chen, Wang & Wu (2023)**, then [GraphRAG](https://microsoft.github.io/graphrag/) — **Microsoft Research**. *The two directions: graphs grounding models, models building graphs.*

## Courses (free)
- [Stanford CS520: Knowledge Graphs](https://web.stanford.edu/class/cs520/) — **Stanford (Vinay Chaudhri et al.)** — free seminar materials covering creation, inference, access, and industrial practice.
- [Stanford CS224W: Machine Learning with Graphs](https://web.stanford.edu/class/cs224w/) — **Stanford (Jure Leskovec)** — free slides and notes; the canonical course for graph representation learning and knowledge-graph embeddings.

## Videos
- [KGC23 Keynote: The Future of Knowledge Graphs in a World of LLMs](https://www.youtube.com/watch?v=ww99npDh4cg) — **Denny Vrandečić (Wikimedia), The Knowledge Graph Conference** — the creator of Wikidata on what graphs still do that language models cannot.
- [Wikidata, Knowledge Graphs, and Beyond](https://www.youtube.com/watch?v=Oips1aW738Q) — **Denny Vrandečić (Columbia SPS)** — how the largest open knowledge graph is modelled, curated, and kept honest.

## Key Papers
- [Knowledge Graphs](https://arxiv.org/abs/2003.02320) — **Hogan et al. (2020)** — the definitive survey: models, schemas, identity, context, reasoning, quality, and refinement.
- [A Review of Relational Machine Learning for Knowledge Graphs](https://arxiv.org/abs/1503.00759) — **Nickel, Murphy, Tresp & Gabrilovich (2015)** — the reference for embedding-based link prediction.
- [Translating Embeddings for Modeling Multi-relational Data (TransE)](https://proceedings.neurips.cc/paper/2013/hash/1cecc7a77928ca8133fa24680a88d2f9-Abstract.html) — **Bordes, Usunier, Garcia-Durán, Weston & Yakhnenko (2013)** — the embedding model everything after it is a variation on.
- [Unifying Large Language Models and Knowledge Graphs: A Roadmap](https://arxiv.org/abs/2306.08302) — **Pan et al. (2023)** — the survey that framed the three integration patterns now standard in industry.
- [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130) — **Edge et al., Microsoft Research (2024)** — building a graph from a corpus, then answering global questions vector search cannot.

## Articles / Blogs (free, no paywall)
- [GraphRAG documentation](https://microsoft.github.io/graphrag/) — **Microsoft Research** — the open-source implementation, with an honest account of indexing cost.
- [GraphRAG: unlocking LLM discovery on narrative private data](https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/) — **Microsoft Research** — the original write-up, with the baseline comparison.
- [DBpedia](https://www.dbpedia.org/) — **DBpedia Association** — an open knowledge graph extracted from Wikipedia; the standard sandbox for experiments.
- [Knowledge Graphs: Research Directions](https://aidanhogan.com/docs/knowledge-graphs-research.pdf) — **Aidan Hogan (2020)** — a short, opinionated map of the open problems.

## Books (free, with chapters)
- [*Knowledge Graphs*](https://kgbook.org/) — **Hogan, Blomqvist, Cochez et al.** — free open-access book (also on arXiv); the standard reference, chapter by chapter.

## In this platform
- Before this: [Knowledge Representation](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/knowledge-representation/knowledge-representation) · [Logic and Inference](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/symbolic-reasoning-primer/logic-and-inference/logic-and-inference)
- The retrieval side (canonical home): [Graph RAG](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/graph-rag/graph-rag) · [Embedding Models](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/embedding-models/embedding-models) · [Vector Search](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/vector-search/vector-search)
- Next: [Neuro-Symbolic AI](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/neural-symbolic-integration/neuro-symbolic-ai/neuro-symbolic-ai) · [Causal and Relational Reasoning](/ai-ml/ai-ml-learning-resources/specialized-studies/neuro-symbolic-and-structured-intelligence/structured-reasoning/causal-and-relational-reasoning/causal-and-relational-reasoning)
