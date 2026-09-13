---
id: "data-and-representation/synthetic-data-and-curation/references"
topic: "Synthetic Data and Data Curation — References"
parent: "data-and-representation/synthetic-data-and-curation"
type: references
updated: 2026-09-13
---

# Synthetic Data and Data Curation — references

> Companion link library for **[Synthetic Data and Data Curation](/ai-ml/ai-ml-learning-resources/data-and-representation/synthetic-data-and-curation/synthetic-data-and-curation)**. External sources and internal links, grouped by type, alphabetical within each group; everything here is free or open-access.

**Videos**:
- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — the pretraining-data and post-training-data sections show concretely what a token in a training set is and where it came from.
- [Generating Synthetic Data with LLMs](https://www.youtube.com/watch?v=GqDgsEcljaw) — **Trelis Research** — an end-to-end generation run with the filtering decisions made out loud.
- [How to Create Synthetic Datasets for LLM Fine-tuning](https://www.youtube.com/watch?v=hl5K2pf9bDc) — **Mervin Praison** — seeds to a finished instruction set, the practitioner's path.
- [Self-Instruct explained](https://www.youtube.com/watch?v=Vt8tlf3xnHU) — **Yannic Kilcher** — a close reading of the paper that started the bootstrapping loop.
- [Stanford CS336 — Lecture 1: Overview and Tokenization](https://www.youtube.com/watch?v=SQ3fZ1sAqXI) — **Stanford Online** — opens the series whose Data lectures cover Common Crawl processing end to end.
- [Synthetic Data for LLMs, why and how](https://www.youtube.com/watch?v=gg_GZuKQ4Wo) — **Sebastian Raschka** — when synthesis is the right answer, and when it quietly is not.

**Courses**:
- [Cosmopedia](https://huggingface.co/blog/cosmopedia) — **Hugging Face** — a fully documented 25-billion-token synthetic corpus: prompt design, topic clustering, dedup, and the failure cases they hit.
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) — **Hugging Face** — free and code-first; the dataset chapters give you `datasets` fluency before you attempt a pipeline.
- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Stanford** — the two Data lectures are the most rigorous free treatment of filtering, deduplication and mixture design.

**Articles**:
- [Cosmopedia: how to create large-scale synthetic data for pre-training](https://huggingface.co/blog/cosmopedia) — **Hugging Face** — the honest write-up of prompt diversity, contamination and dedup at 25-billion-token scale.
- [FineWeb: decanting the web for the finest text data at scale](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) — **Hugging Face** — the interactive blog post; the ablation plots teach the method better than the paper does.
- [SmolLM3](https://huggingface.co/blog/smollm3) — **Hugging Face** — a full open recipe for a small model, with the data mixture and staged curriculum spelled out.
- [Synthetic dataset generation techniques](https://huggingface.co/learn/cookbook/synthetic_data_generation) — **Hugging Face Cookbook** — the recipe form: prompts, filters and dedup as runnable code.
- [Tülu 3: The next era in open post-training](https://allenai.org/blog/tulu-3) — **Allen Institute for AI** — how a modern post-training data mix is assembled, decontaminated and released.

**Papers**:
- [A Careful Examination of Large Language Model Performance on Grade School Arithmetic](https://arxiv.org/abs/2405.00332) — **Zhang et al. (2024)** — a fresh GSM1k reveals which models were memorising; the contamination check to copy.
- [FineWeb2: One Pipeline to Scale Them All](https://arxiv.org/abs/2506.20920) — **Penedo et al. (2025)** — the same pipeline adapted automatically to every language; the multilingual reference.
- [Nemotron-4 340B Technical Report](https://arxiv.org/abs/2406.11704) — **NVIDIA (2024)** — a model family released explicitly as a synthetic-data generator, with the alignment data pipeline documented.
- [Rephrasing the Web](https://arxiv.org/abs/2401.16380) — **Maini et al. (2024)** — rewriting existing web text in a cleaner style is cheaper than generating from scratch and trains faster.
- [Self-Instruct: Aligning Language Models with Self-Generated Instructions](https://arxiv.org/abs/2212.10560) — **Wang et al. (2022)** — bootstrapping instruction data from a handful of seeds; the loop this page teaches.
- [SmolLM2: When Smol Goes Big — Data-Centric Training of a Small Language Model](https://arxiv.org/abs/2502.02737) — **Ben Allal et al. (2025)** — the open, reproducible answer to phi: every dataset released.
- [Textbooks Are All You Need](https://arxiv.org/abs/2306.11644) — **Gunasekar et al. (2023)** — the phi recipe: textbook-quality synthetic data beats far more web tokens.
- [The Curse of Recursion: Training on Generated Data Makes Models Forget](https://arxiv.org/abs/2305.17493) — **Shumailov et al. (2023)** — the model-collapse result behind this page's real-data floor.
- [The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://arxiv.org/abs/2406.17557) — **Penedo et al. (2024)** — ablation-driven curation, and the FineWeb-Edu classifier that made quality filtering measurable.
- [TinyStories: How Small Can Language Models Be and Still Speak Coherent English?](https://arxiv.org/abs/2305.07759) — **Eldan & Li (2023)** — a synthetic corpus narrow enough to train a coherent model at tiny scale.
- [WizardLM: Empowering Large Pre-Trained Language Models to Follow Complex Instructions](https://arxiv.org/abs/2304.12244) — **Xu et al. (2023)** — Evol-Instruct: evolve prompts toward difficulty and breadth.

**Documentation**:
- [distilabel](https://distilabel.argilla.io/latest/) — **Argilla** — the framework that runs generation, judging and dedup as a declarative pipeline.

**Books**:
- [*A Survey of Large Language Models*](https://arxiv.org/abs/2303.18223) — **Zhao et al. (2023)** — free; §4 is a citation-rich map of data collection, quality filtering and deduplication.
- [*AI Engineering*](https://huyenchip.com/books/) — **Chip Huyen (2025)** — the dataset-engineering chapters, from the author's free companion page.
- [*Hands-On Large Language Models*](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) — **Alammar & Grootendorst (2024)** — free notebooks; the data chapters run the loops this page describes.
- [*Speech and Language Processing* (3rd ed.) — Ch. 10 "Large Language Models"](https://web.stanford.edu/~jurafsky/slp3/) — **Jurafsky & Martin** — free PDF; the pretraining-data section: sources, filtering, and what the corpus decides.

**In this platform**:
- Where the curated data is consumed: [Pretraining](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining) · [Supervised Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/supervised-fine-tuning/supervised-fine-tuning) · [Instruction Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/instruction-tuning/instruction-tuning)
- Generating data *from* a stronger model: [Knowledge Distillation](/ai-ml/ai-ml-learning-resources/model-adaptation/knowledge-distillation/knowledge-distillation)
- The reasoning traces that become cold-start data: [Reinforcement Learning Post-training](/ai-ml/ai-ml-learning-resources/model-adaptation/reinforcement-learning-posttraining/reinforcement-learning-posttraining)
- Why data budget beats parameter budget: [Scaling Laws](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/scaling-laws/scaling-laws)
- Contamination is an evaluation problem too: [Model Evaluation and Benchmarks](/ai-ml/ai-ml-learning-resources/evaluation/model-evaluation-and-benchmarks/model-evaluation-and-benchmarks)
- Small models are the main beneficiary: [Small and On-Device Language Models](/ai-ml/ai-ml-learning-resources/inference-and-serving/small-and-on-device-language-models/small-and-on-device-language-models)
- The judge that gates generated rows: [LLM-as-Judge](/ai-ml/ai-ml-intuitions/objectives-evaluation/llm-as-judge-intuition)
- The runnable service: [synthetic-data-generator](/python/python-production-examples/synthetic-data-generator/readme)
