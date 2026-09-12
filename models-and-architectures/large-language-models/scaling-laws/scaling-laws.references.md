---
id: "09-llms/scaling-laws/references"
topic: "Scaling Laws — References"
parent: "09-llms/scaling-laws"
type: references
updated: 2026-09-07
---

# Scaling Laws — references and further reading

> Companion link library for **[Scaling Laws](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/scaling-laws/scaling-laws)** (the concept page). This file holds the curated links — external sources *and* internal links to related pages on this platform — kept separate so it can be reused as a standalone reference list. Grouped by type, best-first. Every entry is from a primary author (the paper's own authors) or a recognized deep explainer — chosen for depth on *this* topic, not popularity.

**Start here — suggested path**:
1. **Get the intuition** — watch [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) (**Andrej Karpathy**). *Why loss falls smoothly and predictably with scale — the observation the whole field plans budgets around.*
2. **See the field context** — watch [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) (**Andrej Karpathy**). *Where scaling laws sit in the full pretraining pipeline and drive the budget decisions.*
3. **Read the correction** — the [Chinchilla paper](https://arxiv.org/abs/2203.15556) (**Hoffmann et al. 2022**). *The three estimation methods → the ~20 tokens/param rule.*
4. **Read the original** — [Scaling Laws for Neural LMs](https://arxiv.org/abs/2001.08361) (**Kaplan et al. 2020**). *The first power-law fits — and the LR-schedule assumption Chinchilla overturned.*
5. **Do the compute math** — read [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) (**EleutherAI**). *The `C ≈ 6ND` arithmetic behind the laws, derived.*

**Videos**:
- [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) — **Andrej Karpathy** — the "scaling laws are remarkably smooth and predictable" insight in plain terms, with the N-vs-D trade-off drawn out.
- [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — scaling laws in the context of the full LLM training pipeline.
- [Stanford CS336 — Language Modeling from Scratch, Spring 2025 (lectures)](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) — **Stanford Online** — includes a dedicated scaling-laws lecture that fits the power laws on real runs and uses them to pick a budget.

**Courses (free)**:
- [Stanford CS324 — Large Language Models](https://stanford-cs324.github.io/winter2022/) — **Stanford (Liang, Hashimoto, et al.)** — derives and interprets the power-law fits in a full LLM course.
- [Stanford CS336 — Language Modeling from Scratch](https://stanford-cs336.github.io/spring2025/) — **Stanford** — how scaling laws guide real budget allocation and systems decisions.

**Articles / blogs (free, no paywall)**:
- [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) — **EleutherAI (Quentin Anthony et al.)** — the `C ≈ 6ND` compute arithmetic and full FLOP/memory accounting behind the laws.
- [Chinchilla's Death (and chinchilla-optimal vs inference-optimal)](https://espadrine.github.io/blog/posts/chinchilla-s-death.html) — **Thaddée Yann Tyl** — why inference cost pushes real deployments past Chinchilla-optimal, with the math.
- [Go smol or go home](https://www.harmdevries.com/post/model-size-vs-compute-overhead/) — **Harm de Vries** — the compute-overhead view of training smaller models longer; the inference-aware argument quantified.
- [Chinchilla's wild implications](https://www.lesswrong.com/posts/6Fpvch8RR29qLEWNH/chinchilla-s-wild-implications) — **nostalgebraist** — data becomes the binding constraint once you apply the Chinchilla ratio at frontier scale; an influential early reading of the data wall.
- [New Scaling Laws for LLMs (Chinchilla explained)](https://www.lesswrong.com/posts/midXmMb2Xg37F2Kgn/new-scaling-laws-for-large-language-models) — **1a3orn** — a careful, equation-by-equation walkthrough of the Chinchilla parametric fit and its three methods.
- [Will we run out of data? An analysis of the limits of scaling](https://epochai.org/blog/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data) — **Epoch AI (Villalobos et al.)** — the quantitative case for the data wall and when the high-quality token supply is exhausted.
- [How to Scale Your Model](https://jax-ml.github.io/scaling-book/) — **Google DeepMind JAX team (2025)** — the systems companion to the statistical laws: what a scaling decision costs in FLOPs, memory, and interconnect traffic on real TPU/GPU pods, derived from first principles.
- [Can AI scaling continue through 2030?](https://epoch.ai/blog/can-ai-scaling-continue-through-2030) — **Epoch AI (2024–25)** — the four binding constraints (power, chips, data, latency) with numbers; the current, careful answer to "does this curve keep going".

**Key papers**:
- [Training Compute-Optimal Large Language Models (Chinchilla)](https://arxiv.org/abs/2203.15556) — **Hoffmann et al. (2022, DeepMind)** — the compute-optimal correction; ~20 tokens/parameter; Chinchilla-70B beats Gopher-280B.
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) — **Kaplan et al. (2020, OpenAI)** — the original power-law study over N, D, C; the parametric form and the small exponents.
- [Scaling Laws for Autoregressive Generative Modeling](https://arxiv.org/abs/2010.14701) — **Henighan et al. (2020, OpenAI)** — scaling laws generalize across modalities (image, video, math), and the irreducible-loss decomposition.
- [Scaling Laws for Transfer](https://arxiv.org/abs/2102.01293) — **Hernandez et al. (2021, OpenAI)** — how scaling laws govern data efficiency under fine-tuning / transfer.
- [Emergent Abilities of Large Language Models](https://arxiv.org/abs/2206.07682) — **Wei et al. (2022)** — the original documentation of sharp capability jumps at scale.
- [Are Emergent Abilities of Large Language Models a Mirage?](https://arxiv.org/abs/2304.15004) — **Schaeffer et al. (2023, NeurIPS best paper)** — emergence as an artifact of discontinuous metrics; the "mirage" critique.
- [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971) — **Touvron et al. (2023, Meta)** — trains smaller models on far more tokens, citing inference cost; the inference-aware departure from Chinchilla.
- [Scaling Data-Constrained Language Models](https://arxiv.org/abs/2305.16264) — **Muennighoff et al. (2023)** — a scaling law for repeated data; how far you can re-use tokens before returns collapse (the data wall, quantified).
- [Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Parameters](https://arxiv.org/abs/2408.03314) — **Snell et al. (2024, Google DeepMind)** — the second scaling axis that reshaped the field in 2025: spend the budget at inference (sampling, verification, revision) instead of on parameters, and a smaller model can beat a much larger one.
- [Scaling Laws for Precision](https://arxiv.org/abs/2411.04330) — **Kumar et al. (2024)** — extends the laws to numerical precision: how low-bit training and post-training quantization change the compute-optimal point, joining scaling laws to the quantization decision.

**Books (free chapters)**:
- [Speech and Language Processing, 3rd ed. — Ch. 10 "Large Language Models"](https://web.stanford.edu/~jurafsky/slp3/10.pdf) — **Jurafsky & Martin** — model size, data, and the scaling intuition in a standard textbook chapter.
- [A Survey of Large Language Models](https://arxiv.org/abs/2303.18223) — **Zhao et al. (2023)** — §3 surveys scaling-law findings across models (a free, book-length reference).

**In this platform**:
- Concept page (full explanation): [Scaling Laws](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/scaling-laws/scaling-laws)
- The phase these laws govern: [Pretraining at Scale](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining) · [Language Modeling Objectives](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/language-modeling-objectives/language-modeling-objectives)
- The architecture being scaled: [Decoder-only Architecture](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/decoder-only-models/decoder-only-models)
- Why inference cost reshapes the optimum: [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache) · [Inference Optimization & Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization) · [Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization)
- A different way to scale parameters cheaply: [Mixture-of-Experts](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/mixture-of-experts/mixture-of-experts)
- The other scaling axis (spend compute at inference, not training): [Test-Time Computation and Scaling](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/test-time-computation-and-scaling/test-time-computation-and-scaling)
- Concept depth (the *why*): [Module 7.01 Neural Scaling Laws / Chinchilla](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/scaling-behavior/neural-scaling-laws-and-chinchilla-intuition)
