---
id: "data-and-representation"
topic: "Data and Representation"
level: beginner
built_from: ["programming-and-data-foundations", "mathematical-foundations"]
updated: 2026-09-13
---

# Data and Representation

> Everything that happens to data before a model sees it, and how a model turns raw input into
> something it can compute on. The first stage of the model lifecycle: clean and prepare the
> data, decide what to synthesize and how to curate it, and represent it — tokens for text,
> embeddings for retrieval. Model building starts where this section ends.

**Start here:** [Exploratory Data Analysis](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/exploratory-data-analysis/exploratory-data-analysis) — look before you model — then work through the data-preparation sub-area top to bottom.

## Sub-areas and topics

1. [Data Preparation](/ai-ml/ai-ml-learning-resources/data-and-representation/data-preparation/readme) — **13 pages** — exploratory analysis, scaling and normalization, encoding, imputation, outliers, feature engineering and selection, date-time features, splits, leakage, imbalance and pipelines.
2. [Synthetic Data and Curation](/ai-ml/ai-ml-learning-resources/data-and-representation/synthetic-data-and-curation/synthetic-data-and-curation) — filtering, deduplication and quality classification, plus generating and then filtering model-written data.

Tokenization is taught where the modality lives — [Tokenization and Subword Algorithms](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/tokenization-and-subword-algorithms/tokenization-and-subword-algorithms) — and embedding models keep their home in [Embedding Models](/ai-ml/ai-ml-learning-resources/llms-applications-and-agents/rag-and-knowledge-systems/embedding-models/embedding-models) until the retrieval sub-area moves to Practitioner Workflows; both are linked, never re-homed.

## Courses (free)

- [Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction) — **Andrew Ng / DeepLearning.AI** — free to audit; the feature-engineering and data-handling lectures are the canonical first pass.
- [MIT Data-Centric AI](https://dcai.csail.mit.edu/) — **MIT (Introduction to Data-Centric AI)** — the course built on the premise that most model problems are dataset problems.

## Videos

- [MIT Data-Centric AI, Lecture 1](https://www.youtube.com/watch?v=ayzOzZGHZy4) — **MIT** — why measurement and modelling problems are usually dataset problems.

## Key Papers

- [Self-Instruct: Aligning LMs with Self-Generated Instructions](https://arxiv.org/abs/2212.10560) — **Wang et al. (2022)** — bootstrap instruction data from the model itself; the recipe underneath most open instruction sets.
- [LIMA: Less Is More for Alignment](https://arxiv.org/abs/2305.11206) — **Zhou et al. (2023)** — around a thousand high-quality examples rivalling far larger noisy mixes; the strongest statement of the quality-over-quantity case.

## Articles / Blogs (free, no paywall)

- [FineWeb: decanting the web for the finest text data at scale](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) — **Hugging Face** — a web-scale data pipeline documented in full: extraction, deduplication, filtering, decontamination.
- [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml) — **Martin Zinkevich (Google)** — 43 hard-won best practices, most of them about data.

## Books (free)

- [*An Introduction to Statistical Learning*](https://www.statlearning.com/) — **James, Witten, Hastie and Tibshirani** — free PDF with Python labs; the applied text under every preparation page.

## In this platform

- Before this section: [Foundations](/ai-ml/ai-ml-learning-resources/foundations/readme) — [Programming and Data Foundations](/ai-ml/ai-ml-learning-resources/foundations/programming-and-data-foundations/readme) · [Mathematical Foundations](/ai-ml/ai-ml-learning-resources/foundations/mathematical-foundations/readme)
- After this section: [Model Building](/ai-ml/ai-ml-learning-resources/model-building/readme) · [Model Adaptation](/ai-ml/ai-ml-learning-resources/model-adaptation/readme)
- Where prepared data is fed at scale: [Data and Training Platforms](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/readme)
- Doing it rather than reading it: [Data Preparation workflow](/ai-ml/practitioner-workflows/data-and-inputs/data-preparation) · [Synthetic Data Generation workflow](/ai-ml/practitioner-workflows/data-and-inputs/synthetic-data-generation)
