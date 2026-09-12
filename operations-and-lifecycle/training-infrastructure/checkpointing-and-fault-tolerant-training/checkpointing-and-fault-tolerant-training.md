---
id: "operations-and-lifecycle/training-infrastructure/checkpointing-and-fault-tolerant-training"
topic: "Checkpointing & Fault-Tolerant Training"
level: advanced
built_from: ["distributed-training-parallelism-fsdp-zero", "mixed-precision-and-memory-efficient-training"]
leads_to: ["operations-and-lifecycle/training-infrastructure/cluster-scheduling-and-training-orchestration", "18-mlops/reproducibility"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 16
title: "Checkpointing & Fault-Tolerant Training"
minutes: 16
category: training-infrastructure
---

# Checkpointing & Fault-Tolerant Training
> A synchronous training job is the most fragile distributed system in production: every rank
> depends on every other rank at every step, so one dead accelerator kills the whole run. At
> ten thousand devices, hardware failures arrive hourly, which makes the real design question
> **how much progress a failure is allowed to destroy** — the checkpoint interval — and **how
> fast the job comes back**. In one sentence: **write state often enough that lost work stays
> smaller than the time spent writing it, and restart without a human.**

**Why it matters:** Meta's Llama 3 405-billion-parameter run logged 419 unexpected interruptions
in a 54-day window on 16,384 accelerators — roughly one every three hours, with about 78% traced
to hardware. At that rate, checkpoint policy *is* throughput policy. Interviewers probe the
optimal-interval argument (the Young–Daly result: interval ≈ √(2 · checkpoint cost · mean time
between failures)), what a **sharded** checkpoint contains versus a single-rank `torch.save`,
why **asynchronous** checkpointing needs a staged copy on the host, and how a resumed run stays
bit-comparable. The failure mode nobody rehearses: **silent data corruption** — a device that
returns wrong arithmetic without raising an error, poisoning the loss and every checkpoint
written after it.

**Start here — suggested path:**

1. **See the real failure statistics** — skim section 3.3 of [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783) — **Meta AI (Grattafiori et al.)**. *Interruption counts, the failure taxonomy, and the effective-training-time number that all of this is optimizing.*
2. **Learn the checkpoint format** — read the [Asynchronous Saving with Distributed Checkpoint recipe](https://docs.pytorch.org/tutorials/recipes/distributed_async_checkpoint_recipe.html) — **PyTorch maintainers**. *Distributed Checkpoint (DCP) saves a sharded, resharding-tolerant checkpoint, so a run can resume on a different device count.*
3. **Make the write stop blocking the step** — read [Reducing Model Checkpointing Times by Over 10x](https://pytorch.org/blog/reducing-checkpointing-times/) — **PyTorch team**. *Stage to host memory, then upload on a background thread; the measurement that shows where the ten-fold gain actually comes from.*
4. **Make restarts automatic** — read the [torchrun and elastic launch documentation](https://docs.pytorch.org/docs/stable/elastic/run.html) — **PyTorch maintainers**. *Rendezvous, membership changes and worker restarts; the difference between a job that resumes and one that pages a human.*
5. **Confront silent corruption** — read [Silent Data Corruptions at Scale](https://arxiv.org/abs/2102.11245) — **Dixit et al. (Meta)**. *Fleet-scale evidence that some devices compute wrong answers quietly, and what detection at that scale costs.*

## Courses (free)

- [Stanford CS329S — Machine Learning Systems Design](https://stanford-cs329s.github.io/syllabus.html) — **Chip Huyen (Stanford)** — free syllabus, slides and lecture notes; the reliability, monitoring and failure-mode material frames checkpointing as an availability problem rather than a file-format one.

## Videos

- [PyTorch Distributed and Fault Tolerance](https://www.youtube.com/watch?v=B-BXSRwAVdE) — **Tristan Rice (Meta), on the PyTorch channel** — the current state of fault tolerance in PyTorch Distributed, including per-replica recovery that avoids restarting every rank.
- [Training LLMs at Scale — Stanford MLSys #83](https://www.youtube.com/watch?v=JA1l96tjrs4) — **Deepak Narayanan (NVIDIA), Stanford MLSys Seminars** — situates checkpointing and restart cost inside the overall goodput budget of a long run.

## Key Papers

- [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783) — **Meta AI (2024)** — the most detailed public account of interruptions, root causes and mitigations for a frontier-scale run; the numbers every reliability argument now cites.
- [MegaScale: Scaling Large Language Model Training to More Than 10,000 GPUs](https://arxiv.org/abs/2402.15627) — **Jiang et al. (2024, ByteDance)** — diagnosis-first operations: heartbeats, per-rank health checks and automatic recovery, plus a stall-detection story worth reading twice.
- [Revisiting Reliability in Large-Scale Machine Learning Research Clusters](https://arxiv.org/abs/2410.21680) — **Kokolis et al. (2024, Meta)** — eleven months of jobs on two large clusters; failure rates by job size and what actually improves effective throughput.
- [ByteCheckpoint: A Unified Checkpointing System for Large Foundation Model Development](https://arxiv.org/abs/2407.20143) — **Wan et al. (2024, ByteDance)** — automatic resharding between parallelism plans and asynchronous saving; the production answer to "we changed the topology, can we resume?"
- [CheckFreq: Frequent, Fine-Grained DNN Checkpointing](https://www.usenix.org/system/files/fast21-mohan.pdf) — **Mohan, Phanishayee & Chidambaram (2021, FAST)** — the clearest treatment of checkpoint frequency as an online tuning problem with a bounded overhead target.
- [Oobleck: Resilient Distributed Training of Large Models Using Pipeline Templates](https://arxiv.org/abs/2309.08125) — **Jang et al. (2023, SOSP)** — pre-planned pipeline templates so a failure shrinks the job instead of stopping it; elasticity without a full restart.
- [Silent Data Corruptions at Scale](https://arxiv.org/abs/2102.11245) — **Dixit et al. (2021, Meta)** — the paper that made silent corruption a first-class infrastructure concern rather than a rumour.
- [Resiliency at Scale: Managing Google's TPUv4 Machine Learning Supercomputer](https://www.usenix.org/conference/nsdi24/presentation/zu) — **Zu et al. (2024, NSDI, Google)** — optical reconfiguration and automated healing around failed hardware; a different architectural answer to the same problem.

## Articles / Blogs (free, no paywall)

- [Reducing Model Checkpointing Times by Over 10x with PyTorch Distributed Asynchronous Checkpointing](https://pytorch.org/blog/reducing-checkpointing-times/) — **PyTorch team** — the staged-copy design and its measured effect on step time.
- [Asynchronous Saving with Distributed Checkpoint (DCP)](https://docs.pytorch.org/tutorials/recipes/distributed_async_checkpoint_recipe.html) — **PyTorch maintainers** — the runnable version of the above, including what belongs in the state dictionary beyond weights.
- [torchrun (elastic launch)](https://docs.pytorch.org/docs/stable/elastic/run.html) — **PyTorch maintainers** — rendezvous backends, `--max-restarts`, and the elastic contract your training script must satisfy to be restartable.
- [torchft](https://github.com/pytorch/torchft) — **PyTorch maintainers** — per-replica fault tolerance with a lighthouse process: replicas can fail and rejoin mid-run without restarting the world.
- [NVIDIA Resiliency Extension](https://github.com/NVIDIA/nvidia-resiliency-ext) — **NVIDIA** — in-job restart, hang detection and straggler detection as a library, which is exactly the tooling most teams write badly themselves.
- [How Meta trains large language models at scale](https://engineering.fb.com/2024/06/12/data-infrastructure/training-large-language-models-at-scale-meta/) — **Engineering at Meta** — the operational view: hardware reliability, network fabric and the tooling built around long-running jobs.
- [Reproducibility notes](https://docs.pytorch.org/docs/stable/notes/randomness.html) — **PyTorch maintainers** — the seeds, data-loader worker state and deterministic-algorithm flags a resumed run must restore for a comparable curve.

## Books (free, with chapters)

- [*Site Reliability Engineering* — "Embracing Risk"](https://sre.google/sre-book/embracing-risk/) — **Google (Beyer, Jones, Petoff & Murphy)** — free full text; the failure-budget vocabulary that turns "how often should we checkpoint" into an explicit, defensible trade-off.
- [*Machine Learning Engineering Open Book*](https://github.com/stas00/ml-engineering) — **Stas Bekman** — field notes from real large-model runs: checkpoint hygiene, hardware fault triage, hanging-job debugging and network health checks.

## In this platform

- Prerequisites: [Distributed Training — Parallelism, FSDP & ZeRO](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/distributed-training-parallelism-fsdp-zero/distributed-training-parallelism-fsdp-zero) — the sharding a checkpoint has to describe · [Mixed Precision & Memory-Efficient Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/mixed-precision-and-memory-efficient-training/mixed-precision-and-memory-efficient-training) — the optimizer state that dominates checkpoint size
- Next in this sub-area: [Cluster Scheduling & Training Orchestration](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/cluster-scheduling-and-training-orchestration/cluster-scheduling-and-training-orchestration) — who restarts the job and where it lands
- Determinism and lineage: [Reproducibility](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/reproducibility/reproducibility) · [Experiment Tracking](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/experiment-tracking/experiment-tracking) · [Data & Model Versioning](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/lifecycle-and-reproducibility/data-and-model-versioning/data-and-model-versioning)
- When it goes wrong in production: [AI Incident Response & Postmortems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/monitoring-and-reliability/ai-incident-response-and-postmortems/ai-incident-response-and-postmortems)
- The platform underneath: [Data & Training Platforms](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/readme) · [Cost Optimization for ML Systems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/cost-optimization/cost-optimization)
- Where the long runs live: [Pretraining at Scale](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining) · [The Training Loop](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining-the-training-loop)
