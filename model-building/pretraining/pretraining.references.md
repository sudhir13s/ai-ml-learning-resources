---
id: "09-llms/pretraining-at-scale/references"
topic: "Pretraining at Scale — References"
parent: "09-llms/pretraining-at-scale"
type: references
updated: 2026-09-07
---

# Pretraining at Scale — references and further reading

> Companion link library for **[Pretraining at Scale](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining)** (the concept page). This file holds the curated links — external sources *and* internal links to related pages on this platform — kept separate so it can be reused as a standalone reference list. Grouped by type, best-first. Every entry is from a primary author or a recognized deep explainer — chosen for depth on *this* topic (the systems of pretraining), not popularity. Everything here is free / open-access.

**Start here — suggested path**:
1. **See a real run end to end** — watch [Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU) (**Andrej Karpathy**). *An actual pretraining run: data, init, warmup+cosine, grad clip, throughput — the whole stack in motion.*
2. **Do the cost math** — read [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) (**EleutherAI**). *Memory, the 6ND compute rule, and the optimizer-state tax you budget every run from.*
3. **Understand the parallelism** — read [How to Train Really Large Models on Many GPUs](https://lilianweng.github.io/posts/2021-09-25-train-large/) (**Lilian Weng**). *Data / tensor / pipeline parallelism and ZeRO, explained cleanly.*
4. **Read a full open recipe** — skim the [Llama 2 paper](https://arxiv.org/abs/2307.09288) (**Touvron et al.**). *A concretely documented pretraining recipe: data, hyperparameters, tokens-per-parameter.*
5. **See the data pipeline in detail** — read the [FineWeb blog](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) (**Hugging Face**). *How 15T clean tokens are actually produced from Common Crawl — dedup, filtering, decontamination.*

**Videos**:
- [Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU) — **Andrej Karpathy** — a full from-scratch pretraining run with the real recipe (warmup+cosine, grad clip, grad accumulation, bf16) and live throughput/MFU.
- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — where pretraining sits in the full pipeline (data → base model → SFT → RLHF), and why the base model is ~all the capability.
- [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) — **Andrej Karpathy** — tokenization at scale, the first stage of every data pipeline.
- [Stanford CS336 — Language Modeling from Scratch, Spring 2025 (lectures)](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) — **Stanford Online** — the systems lectures: data, parallelism, scaling laws, and training infrastructure at scale, taught from a real build.
- [Build a Large Language Model (From Scratch) — video series](https://www.youtube.com/playlist?list=PLTKMiZHVd_2IIEsoJrWACkIxLRdfMlw11) — **Sebastian Raschka** — the pretraining loop implemented step by step alongside the book, from data loader to trained checkpoint.
- [Let's build GPT: from scratch, in code](https://www.youtube.com/watch?v=kCc8FmEb1nY) — **Andrej Karpathy** — a real training loop for a transformer, the five lines the chapters build on.
- [The spelled-out intro to neural networks and backpropagation: micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0) — **Andrej Karpathy** — build autograd from zero; what `.backward()` records and replays.
- [Gradient descent, how neural networks learn](https://www.youtube.com/watch?v=IHZwWFHWa-w) — **3Blue1Brown** — the optimizer step, visualized.
- [Backpropagation, intuitively](https://www.youtube.com/watch?v=Ilg3gGewQ5U) — **3Blue1Brown** — what the backward pass is really doing.

**Interactive & visual**:
- [LLM Visualizer (3D)](https://bbycroft.net/llm) — **Brendan Bycroft** — walk a token through a small GPT's full forward pass; makes the per-token compute the 6ND rule counts concrete.
- [The Annotated FineWeb](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) — **Hugging Face** — an interactive walkthrough of a real web-scale data pipeline, with ablations on each filtering stage.

**Courses (free)**:
- [Stanford CS336 — Language Modeling from Scratch](https://stanford-cs336.github.io/spring2025/) — **Stanford** — the definitive build-an-LLM course: data, tokenization, parallelism, and training systems.
- [Stanford CS224n — NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) — **Stanford** — pretraining and transformers within the broader NLP curriculum.
- [Practical Deep Learning for Coders](https://www.fast.ai/) — **fast.ai (Jeremy Howard)** — top-down, training-first deep learning; the loop before the theory.

**Articles / blogs (free, no paywall)**:
- [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) — **EleutherAI** — the full memory/compute/parallelism arithmetic for real runs, including 6ND and optimizer-state memory.
- [How to Train Really Large Models on Many GPUs](https://lilianweng.github.io/posts/2021-09-25-train-large/) — **Lilian Weng (OpenAI)** — data, tensor, and pipeline parallelism plus ZeRO, in one clear survey.
- [The Technology Behind BLOOM Training](https://huggingface.co/blog/bloom-megatron-deepspeed) — **Hugging Face** — a real 176B run: 3D parallelism (Megatron + DeepSpeed ZeRO), the exact engineering this page describes.
- [Efficient Training on Multiple GPUs](https://huggingface.co/docs/transformers/en/perf_train_gpu_many) — **Hugging Face** — practical DP / TP / PP / ZeRO guidance and when to reach for each.
- [Methods and tools for efficient training on a single GPU — gradient accumulation](https://huggingface.co/docs/transformers/en/perf_train_gpu_one#gradient-accumulation) — **Hugging Face** — states the equal-batch equivalence: accumulating $K$ micro-batches simulates one batch of size $mK$.
- [FineWeb: decanting the web for the finest text data at scale](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) — **Hugging Face** — a web-scale data pipeline in full: extraction, dedup, quality filtering, decontamination, ablations.
- [Understanding Large Language Models](https://magazine.sebastianraschka.com/p/understanding-large-language-models) — **Sebastian Raschka** — a guided path through the foundational pretraining papers.
- [OLMo 2: the best fully open language model to date](https://allenai.org/blog/olmo2) — **Allen Institute for AI (2025)** — a fully open 2025 pretraining report: data mix, staged curriculum, mid-training anneal, and stability fixes, with every artifact released.
- [SmolLM3: smol, multilingual, long-context reasoner](https://huggingface.co/blog/smollm3) — **Hugging Face (2025)** — a complete 2025 small-model pretraining recipe published in full: 11T-token mixture, three-stage data schedule, long-context extension, and the ablations behind each choice.
- [The FLOPs Calculator for Transformer models](https://kipp.ly/transformer-inference-arithmetic/) — **Kipply** — the per-token FLOP accounting behind the 6N forward+backward rule.
- [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/) — **Andrej Karpathy** — the practitioner's checklist for making a training loop actually work; the troubleshooting gallery's ancestor.
- [Automatic Mixed Precision examples](https://pytorch.org/docs/stable/notes/amp_examples.html) — **PyTorch maintainers** — the `autocast` + `GradScaler` patterns behind the mixed-precision chapter.
- [Optimization — Build the Neural Network](https://pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) — **PyTorch maintainers** — the five-line loop, step by step, from the framework that runs it.
- [Getting started with Fully Sharded Data Parallel (FSDP)](https://pytorch.org/tutorials/intermediate/FSDP_tutorial.html) — **PyTorch maintainers** — sharding weights, gradients and optimizer state across GPUs; the launch recipe the scaling chapter points at.
- [ZeRO tutorial](https://www.deepspeed.ai/tutorials/zero/) — **DeepSpeed (Microsoft)** — the three ZeRO stages from the team that built them.

**Key papers**:
- [Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165) — **Brown et al. (2020)** — the 175B/300B-token run that defined "scale," and (in hindsight) the canonical under-trained model.
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) — **Kaplan et al. (2020)** — the source of the $C \approx 6ND$ training-compute estimate and the original scaling-law curves.
- [Training Compute-Optimal Large Language Models (Chinchilla)](https://arxiv.org/abs/2203.15556) — **Hoffmann et al. (2022)** — the ~20-tokens-per-parameter compute-optimal result; full derivation lives on the Scaling Laws page.
- [PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311) — **Chowdhery et al. (2022)** — defines **MFU** (model FLOPs utilization) and reports ~46% on a 540B run.
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — **Vaswani et al. (2017)** — the Transformer, and (§5.3) the original linear-warmup learning-rate schedule.
- [SGDR: Stochastic Gradient Descent with Warm Restarts](https://arxiv.org/abs/1608.03983) — **Loshchilov & Hutter (2016)** — the cosine-annealing learning-rate decay used in the warmup→cosine schedule.
- [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://arxiv.org/abs/2307.09288) — **Touvron et al. (2023)** — a fully documented open pretraining recipe: data, hyperparameters, tokens-per-parameter.
- [Megatron-LM: Training Multi-Billion Parameter Models Using Model Parallelism](https://arxiv.org/abs/1909.08053) — **Shoeybi et al. (2019)** — the tensor-parallelism approach for splitting a layer's matmuls across GPUs.
- [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](https://arxiv.org/abs/1910.02054) — **Rajbhandari et al. (2019)** — sharding optimizer state / gradients / weights across data-parallel GPUs; the basis of FSDP.
- [PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel](https://arxiv.org/abs/2304.11277) — **Zhao et al. (2023)** — the primary FSDP source, completing the ZeRO→FSDP pair: how Fully Sharded Data Parallel is implemented and scaled in PyTorch.
- [Mixed Precision Training](https://arxiv.org/abs/1710.03740) — **Micikevicius et al. (2017)** — fp16/bf16 training with an fp32 master copy and loss scaling.
- [Decoupled Weight Decay Regularization (AdamW)](https://arxiv.org/abs/1711.05101) — **Loshchilov & Hutter (2017)** — why weight decay must be decoupled from the Adam step; the optimizer every LLM uses.
- [GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism](https://arxiv.org/abs/1811.06965) — **Huang et al. (2018)** — pipeline parallelism and the micro-batching that shrinks the pipeline bubble.
- [Deduplicating Training Data Makes Language Models Better](https://arxiv.org/abs/2107.06499) — **Lee et al. (2021)** — why deduplication improves quality and reduces memorization.
- [Textbooks Are All You Need (phi-1)](https://arxiv.org/abs/2306.11644) — **Gunasekar et al. (2023)** — the existence proof that data *quality* can beat 10× the data *quantity*.
- [The Pile: An 800GB Dataset of Diverse Text](https://arxiv.org/abs/2101.00027) — **Gao et al. (2020)** — a curated, well-documented open pretraining corpus and its mixture.
- [Scaling Language Models: Methods, Analysis & Insights (Gopher)](https://arxiv.org/abs/2112.11446) — **Rae et al. (2021)** — a large run with extensive data-pipeline and training-stability detail.
- [2 OLMo 2 Furious](https://arxiv.org/abs/2501.00656) — **OLMo team, Allen Institute for AI (2025)** — the most transparent modern pretraining paper: data curation, the Dolmino mid-training mix, loss-spike diagnosis, and the exact recipe that closed the gap to closed models.
- [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980) — **Kingma & Ba (2014)** — the two moments AdamW stores per weight and the bias correction the chapters work by hand.
- [Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour](https://arxiv.org/abs/1706.02677) — **Goyal et al. (2017)** — the linear learning-rate warmup behind large-batch training.
- [An Empirical Model of Large-Batch Training](https://arxiv.org/abs/1812.06162) — **McCandlish et al. (2018)** — gradient-noise scaling and the critical batch size; why quadrupling the batch only halves the noise.
- [Delving Deep into Rectifiers](https://arxiv.org/abs/1502.01852) — **He et al. (2015)** — Kaiming initialization for ReLU networks; where the loop begins.
- [Understanding the difficulty of training deep feedforward neural networks](http://proceedings.mlr.press/v9/glorot10a.html) — **Glorot & Bengio (2010)** — variance-preserving (Xavier) initialization.
- [On the difficulty of training Recurrent Neural Networks](https://arxiv.org/abs/1211.5063) — **Pascanu et al. (2013)** — norm-based gradient clipping against exploding gradients.

**Books (free chapters)**:
- [Speech and Language Processing, 3rd ed. — Ch. 10 "Large Language Models"](https://web.stanford.edu/~jurafsky/slp3/10.pdf) — **Jurafsky & Martin** — pretraining corpora, tokenization, and the next-token objective at scale.
- [Dive into Deep Learning — Optimization chapter](https://d2l.ai/chapter_optimization/index.html) — **Zhang et al.** — Adam, learning-rate schedules, and the optimization machinery large runs rely on.
- [*Deep Learning* — Ch. 8 "Optimization for Training Deep Models"](https://www.deeplearningbook.org/) — **Goodfellow, Bengio & Courville (2016)** — free online; initialization, momentum, adaptive methods and the theory under the chapters.

**In this platform**:
- Concept page (full explanation): [Pretraining at Scale](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining)
- The five depth chapters: [The training loop](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining-the-training-loop) · [Batching, precision and memory](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining-batching-precision-and-memory) · [Schedule, clipping and checkpoints](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining-schedule-clipping-and-checkpoints) · [Scaling out](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining-scaling-out) · [TinyReg end to end](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining-tinyreg-end-to-end)
- The intuitions the chapters lean on: [Weight initialization](/ai-ml/ai-ml-intuitions/training-stability/gradient-health/weight-initialization-intuition) · [Adam](/ai-ml/ai-ml-intuitions/learning-and-optimization/adaptive-optimization/adam-intuition) · [AdamW](/ai-ml/ai-ml-intuitions/learning-and-optimization/adaptive-optimization/adamw-intuition) · [Learning rate schedules](/ai-ml/ai-ml-intuitions/learning-and-optimization/adaptive-optimization/learning-rate-schedules-intuition) · [Gradient clipping](/ai-ml/ai-ml-intuitions/training-stability/gradient-health/gradient-clipping-intuition) · [Loss scaling](/ai-ml/ai-ml-intuitions/training-stability/numerical-stability/loss-scaling-intuition) · [Neural scaling laws and Chinchilla](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/scaling-behavior/neural-scaling-laws-and-chinchilla-intuition)
- Where the recorded runs live: [Experiment Tracking](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/experiment-tracking/experiment-tracking) · the production loop: [ml-platform](/python/python-production-examples/ml-platform/readme)
- The objective being trained (don't re-derive it): [Language Modeling Objectives](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/language-modeling-objectives/language-modeling-objectives)
- The budget allocation (6ND derived, Chinchilla compute-optimal split): [Scaling Laws](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/scaling-laws/scaling-laws)
- Foundations: [Transformer Architecture](/ai-ml/ai-ml-learning-resources/models-and-architectures/attention-and-transformers/transformer-architecture/transformer-architecture) · [Tokenization & Subword Algorithms](/ai-ml/ai-ml-learning-resources/multimodal-and-generative-media/natural-language-processing/tokenization-and-subword-algorithms/tokenization-and-subword-algorithms)
- What pretraining produces, then what's done to it: [Decoder-only Architecture](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/decoder-only-models/decoder-only-models) · [Supervised Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/supervised-fine-tuning/supervised-fine-tuning) · [RLHF and DPO](/ai-ml/ai-ml-learning-resources/model-adaptation/preference-and-alignment-training/preference-and-alignment-training)
