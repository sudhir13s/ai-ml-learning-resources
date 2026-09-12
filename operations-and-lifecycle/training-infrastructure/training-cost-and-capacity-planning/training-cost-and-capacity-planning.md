---
id: "operations-and-lifecycle/training-infrastructure/training-cost-and-capacity-planning"
topic: "Training Cost & Capacity Planning"
level: advanced
built_from: ["cluster-scheduling-and-training-orchestration", "distributed-training-parallelism-fsdp-zero"]
leads_to: ["18-mlops/cost-optimization", "09-llms/scaling-laws"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Training Cost & Capacity Planning"
minutes: 16
category: training-infrastructure
---

# Training Cost & Capacity Planning
> Before a single accelerator is booked, a training run can be priced on the back of an envelope.
> Training compute is roughly **6ND** floating-point operations (FLOPs) — six per parameter per
> token, for N parameters and D tokens — so wall-clock time is 6ND divided by the fleet's peak
> throughput times the fraction of it you actually achieve. That fraction is **model FLOPs
> utilisation (MFU)**, and it is where budgets die. In one sentence: **estimate the FLOPs, divide
> by realistic utilisation, multiply by the hourly price — then decide whether the tokens or the
> parameters were the wrong size.**

**Why it matters:** this is the arithmetic that turns "we want to train a model" into a number a
finance team can approve, and the fastest way to expose a plan that does not survive contact with
a cluster. Interviewers ask you to derive 6ND, to separate **MFU** from **hardware FLOPs
utilisation (HFU)** — the latter counts recomputed FLOPs, so it flatters a checkpointed run — and
to apply Chinchilla-style compute-optimal allocation between parameters and tokens. Then the
economics: reserved capacity versus on-demand versus preemptible, and the fact that a model
trained once is served for years, which is why inference-aware scaling now argues for **smaller
models trained on more tokens** than compute-optimality alone suggests. The underrated line item
is **energy**: power draw and carbon are increasingly a planning constraint, not a footnote.

**Start here — suggested path:**

1. **Derive the estimate** — read [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) — **Quentin Anthony, Stella Biderman & Hailey Schoelkopf (EleutherAI)**. *Where 6ND comes from, plus the memory formulas that decide how many devices you need before throughput even enters.*
2. **Learn the allocation rule** — read [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) — **Hoffmann et al. (DeepMind)**. *For a fixed compute budget, parameters and tokens should scale together — the result that reset every training plan after 2022.*
3. **Correct it for the service you will run** — read [Beyond Chinchilla-Optimal](https://arxiv.org/abs/2401.00448) — **Sardana et al. (MosaicML/Databricks)**. *Once inference demand is in the objective, the optimum shifts towards smaller models trained longer; this is the version that matters commercially.*
4. **Price a real run** — read [How much does it cost to train frontier AI models?](https://epoch.ai/blog/how-much-does-it-cost-to-train-frontier-ai-models) — **Ben Cottier and colleagues (Epoch AI)**. *Amortised hardware, energy and staff costs broken out for named models, with the method shown rather than asserted.*
5. **Check yourself against a published run** — skim the compute and cost sections of the [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) — **DeepSeek-AI**. *Accelerator-hours per training stage, at a total that surprised the field; a useful calibration for your own estimate.*

## Courses (free)

- [How to Scale Your Model — "Training LLaMA 3 on TPUs"](https://jax-ml.github.io/scaling-book/applied-training/) — **Google DeepMind JAX team** — a fully worked capacity plan: FLOPs, sharding, achievable utilisation and the resulting wall-clock estimate, with the arithmetic exposed.
- [Stanford CS336 — Language Modeling from Scratch (Spring 2025)](https://stanford-cs336.github.io/spring2025/) — **Percy Liang & Tatsunori Hashimoto (Stanford)** — includes a scaling-laws assignment where you fit your own curves and spend a simulated compute budget.

## Videos

- [Stanford CS336 — Language Modeling from Scratch, 2025 lecture series](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) — **Stanford Online** — the scaling-laws and systems lectures connect the FLOP budget to the hardware bill in the same derivation.
- [Inside the Frontier Data Centers hub](https://www.youtube.com/watch?v=v-1X0nEcxH8) — **Epoch AI** — how training capacity is actually tracked in the wild: power, site build-out and accelerator counts, which is where 2025–26 planning constraints now bind.
- [Stretching cloud compute dollars by a factor of 3 with SkyPilot](https://www.youtube.com/watch?v=LvldvQp-K8k) — **UW eScience Institute** — the preemptible-capacity argument made with measurements: what automatic recovery buys and what it costs in complexity.

## Key Papers

- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) — **Kaplan et al. (2020, OpenAI)** — the original power laws in parameters, data and compute; also the source of the 6ND convention used everywhere since.
- [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) — **Hoffmann et al. (2022, DeepMind)** — the Chinchilla result: earlier models were badly under-trained for their size, and the fix is more tokens rather than more parameters.
- [Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws](https://arxiv.org/abs/2401.00448) — **Sardana et al. (2024)** — adds lifetime inference demand to the objective and re-derives the optimum; essential if the model will actually be served.
- [PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/abs/2204.02311) — **Chowdhery et al. (2022, Google)** — introduces model FLOPs utilisation and separates it from hardware FLOPs utilisation; read section 5 for the definition you will be asked to state.
- [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783) — **Meta AI (2024)** — accelerator-hours, achieved utilisation and greenhouse-gas figures published for a frontier run; a rare end-to-end cost disclosure.
- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) — **DeepSeek-AI (2024)** — per-stage accelerator-hours and a total training cost that reframed what a frontier run has to cost.
- [The rising costs of training frontier AI models](https://arxiv.org/abs/2405.21015) — **Cottier, Rahman, Fattorini et al. (2024, Epoch AI)** — a cost model covering hardware amortisation, energy and staff, fitted to published runs and extrapolated.
- [Carbon Emissions and Large Neural Network Training](https://arxiv.org/abs/2104.10350) — **Patterson et al. (2021, Google & UC Berkeley)** — the four factors that dominate emissions (model, hardware, datacentre efficiency, grid mix) and why estimates vary by orders of magnitude.
- [Estimating the Carbon Footprint of BLOOM, a 176B Parameter Language Model](https://arxiv.org/abs/2211.02001) — **Luccioni, Viguier & Ligozat (2022)** — a full life-cycle accounting including manufacturing and idle time, not just the training run's electricity.

## Articles / Blogs (free, no paywall)

- [Transformer Math 101](https://blog.eleuther.ai/transformer-math/) — **EleutherAI** — the compute and memory formulas every capacity estimate starts from, with worked numbers.
- [How much does it cost to train frontier AI models?](https://epoch.ai/blog/how-much-does-it-cost-to-train-frontier-ai-models) — **Epoch AI** — the clearest public method for turning accelerator-hours into an amortised dollar figure, with its assumptions stated.
- [Let's reproduce GPT-2 (1.6B): one 8×H100 node, 24 hours, $672](https://github.com/karpathy/llm.c/discussions/677) — **Andrej Karpathy** — a complete, reproducible run with the price attached; the best sanity check that your own estimate is in the right order of magnitude.
- [ML CO2 Impact calculator](https://mlco2.github.io/impact/) — **Lacoste, Luccioni, Schmidt & Dandres** — hardware, hours, provider and region in, estimated emissions out; the standard tool for the carbon line of a model card.
- [Spot Virtual Machines](https://cloud.google.com/compute/docs/instances/spot) — **Google Cloud documentation** — preemption semantics and notice periods; the contract your checkpoint interval and restart policy must be designed against.

## Books (free, with chapters)

- [*Machine Learning Engineering Open Book*](https://github.com/stas00/ml-engineering) — **Stas Bekman** — the performance chapters give measured utilisation numbers from real runs, which is what turns a peak-FLOPs estimate into a believable one.

## In this platform

- Prerequisites: [Cluster Scheduling & Training Orchestration](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/cluster-scheduling-and-training-orchestration/cluster-scheduling-and-training-orchestration) — the capacity being rationed · [Distributed Training — Parallelism, FSDP & ZeRO](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/distributed-training-parallelism-fsdp-zero/distributed-training-parallelism-fsdp-zero) — the choices that set achieved utilisation
- The two levers on the bill: [Mixed Precision & Memory-Efficient Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/mixed-precision-and-memory-efficient-training/mixed-precision-and-memory-efficient-training) · [GPUs & Accelerators for Deep Learning](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/gpus-and-accelerators-for-deep-learning/gpus-and-accelerators-for-deep-learning)
- Preemptible capacity only pays if restarts are free: [Checkpointing & Fault-Tolerant Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/checkpointing-and-fault-tolerant-training/checkpointing-and-fault-tolerant-training)
- The serving side of the same budget is owned by [Cost Optimization for ML Systems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/cost-optimization/cost-optimization) — inference economics, autoscaling and caching live there, not here
- The theory this rests on: [Scaling Laws](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/scaling-laws/scaling-laws) · [Pretraining at Scale](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining)
- Fine-tuning budgets are a different shape: [LoRA & Parameter-Efficient Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/lora-and-parameter-efficient-fine-tuning/lora-and-parameter-efficient-fine-tuning) · [Supervised Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/supervised-fine-tuning/supervised-fine-tuning)
- The platform underneath: [Data & Training Platforms](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/readme) · [Experiment Tracking](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/experiment-tracking/experiment-tracking) · practitioner workflow [Model Training](/ai-ml/practitioner-workflows/training-and-adaptation/model-training)
