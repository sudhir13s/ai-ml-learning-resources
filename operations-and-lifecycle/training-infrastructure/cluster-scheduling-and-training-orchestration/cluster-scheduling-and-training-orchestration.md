---
id: "operations-and-lifecycle/training-infrastructure/cluster-scheduling-and-training-orchestration"
topic: "Cluster Scheduling & Training Orchestration"
level: advanced
built_from: ["distributed-training-parallelism-fsdp-zero", "checkpointing-and-fault-tolerant-training"]
leads_to: ["operations-and-lifecycle/training-infrastructure/training-cost-and-capacity-planning", "18-mlops/ml-pipelines-and-orchestration"]
interview_frequency: medium
updated: 2026-09-07
tier: core
est_minutes: 17
title: "Cluster Scheduling & Training Orchestration"
minutes: 17
category: training-infrastructure
---

# Cluster Scheduling & Training Orchestration
> A web service scales by adding one replica at a time; a training job does not. It needs **all
> of its workers at once, placed close together on the network** — otherwise it either deadlocks
> waiting for a partial allocation or runs at a fraction of its speed because two ranks that talk
> constantly ended up in different racks. Cluster scheduling for training is therefore about
> **gang scheduling, topology-aware placement, queues with quotas, and preemption**. In one
> sentence: **an accelerator scheduler allocates groups, not machines — and where the group lands
> decides the throughput.**

**Why it matters:** most organisations do not have a spare cluster per team, so the scheduler is
what turns one expensive fleet into shared capacity. Interviewers probe the failure that defines
the field — **partial allocation deadlock**, where two half-scheduled jobs each hold accelerators
the other needs — and its fix, gang (all-or-nothing) scheduling. Then come quotas and borrowing
between teams, preemption and priority, and the placement question: tensor parallelism belongs
inside an NVLink island, data and pipeline parallelism can stretch across an InfiniBand or RDMA
over Converged Ethernet (RoCE) fabric. The 2025–26 shift is that this now happens on Kubernetes
as often as on Slurm, with Kueue for queuing, Volcano or the Kubeflow Trainer for gang placement,
and Dynamic Resource Allocation (DRA) for describing devices properly. The underrated trap:
**multi-instance GPU (MIG) partitions and time-slicing look like more capacity, but neither gives
a training job the bandwidth it was benchmarked with.**

**Start here — suggested path:**

1. **Learn the classical model** — read the [Slurm quick start](https://slurm.schedmd.com/quickstart.html) — **SchedMD**. *Partitions, jobs, steps and `srun` versus `sbatch`; almost every high-performance-computing cluster and many accelerator fleets still speak this vocabulary.*
2. **Understand queueing on Kubernetes** — watch [Building a Batch System for the Cloud with Kueue](https://www.youtube.com/watch?v=5qasif08vnM) — **Aldo Culquicondor (Google) & Kante Yin (DaoCloud), CNCF**. *Why pod-level scheduling is the wrong altitude for a training job, and what job-level admission fixes.*
3. **Place the job on the network, not just the cluster** — read [Topology-Aware Scheduling](https://kueue.sigs.k8s.io/docs/concepts/topology_aware_scheduling/) — **Kueue maintainers**, alongside the [Slurm topology guide](https://slurm.schedmd.com/topology.html). *Two schedulers, one idea: express the fabric so the allocator can keep tightly-coupled ranks together.*
4. **See a research answer to sharing** — read [Gandiva: Introspective Cluster Scheduling for Deep Learning](https://www.usenix.org/conference/osdi18/presentation/xiao) — **Xiao et al. (Microsoft, OSDI 2018)**. *Deep-learning jobs are predictable and interruptible at mini-batch boundaries; that single observation enables migration, packing and time slicing.*
5. **Run one job across whatever you can get** — work through the [SkyPilot documentation](https://docs.skypilot.co/en/latest/) — **the SkyPilot team (UC Berkeley Sky Computing Lab)**. *One declarative job specification, then automatic placement across clouds, regions and preemptible capacity.*

## Courses (free)

- [Full Stack Deep Learning — "Development Infrastructure & Tooling"](https://fullstackdeeplearning.com/course/2022/lecture-2-development-infrastructure-and-tooling/) — **Josh Tobin, Sergey Karayev & Charles Frye** — free lecture notes and video that map the whole stack from a single workstation to a shared, scheduled cluster, and say plainly what each tier buys.

## Videos

- [Building a Batch System for the Cloud with Kueue](https://www.youtube.com/watch?v=5qasif08vnM) — **Aldo Culquicondor (Google) & Kante Yin (DaoCloud), CNCF** — cluster queues, cohorts and quota borrowing explained by the maintainers who built them.
- [Ray Train: Distributed Solutions for Removing Training Bottlenecks](https://www.youtube.com/watch?v=BuYkzhlCeEg) — **Justin Yu & Timothy Seah (Anyscale), Ray Summit 2025** — the actor-based alternative: the framework, not the cluster manager, owns worker groups and their recovery.
- [SkyPilot at 100k+ GPU Scale at Meta AI (FAIR)](https://www.youtube.com/watch?v=Pas2NE76220) — **Lucca Bertoncini (Meta), SkyPilot** — what queuing, quota and placement look like when the fleet is genuinely enormous, from the operator's side.

## Key Papers

- [Large-scale cluster management at Google with Borg](https://research.google/pubs/large-scale-cluster-management-at-google-with-borg/) — **Verma et al. (2015, EuroSys)** — the ancestor of Kubernetes and the source of the priority, quota and admission model everything here inherits.
- [Gandiva: Introspective Cluster Scheduling for Deep Learning](https://www.usenix.org/conference/osdi18/presentation/xiao) — **Xiao et al. (2018, OSDI, Microsoft)** — exploits the repetitive structure of training to migrate, pack and time-slice jobs mid-run.
- [Pollux: Co-adaptive Cluster Scheduling for Goodput-Optimized Deep Learning](https://arxiv.org/abs/2008.12260) — **Qiao et al. (2021, OSDI)** — schedules for *goodput*, jointly tuning allocation, batch size and learning rate instead of treating resources as fixed.
- [Singularity: Planet-Scale, Preemptive and Elastic Scheduling of AI Workloads](https://arxiv.org/abs/2202.07848) — **Shukla et al. (2022, Microsoft)** — transparent checkpointing and device-proxy migration so jobs can be preempted and resized without cooperating code.
- [SkyPilot: An Intercloud Broker for Sky Computing](https://www.usenix.org/conference/nsdi23/presentation/yang-zongheng) — **Yang et al. (2023, NSDI, UC Berkeley)** — treating several clouds as one capacity pool, with placement chosen by price and availability.

## Articles / Blogs (free, no paywall)

- [Slurm quick start](https://slurm.schedmd.com/quickstart.html) and the [Topology Guide](https://slurm.schedmd.com/topology.html) — **SchedMD** — the job model plus the block and tree topology plugins that keep a job's ranks on adjacent switches.
- [Kueue concepts](https://kueue.sigs.k8s.io/docs/concepts/) — **Kubernetes WG Batch** — cluster queues, local queues, cohorts and quota borrowing: the vocabulary of multi-tenant fairness on Kubernetes.
- [Kubeflow Trainer](https://www.kubeflow.org/docs/components/trainer/) — **Kubeflow maintainers** — the training-job custom resource: worker groups, gang semantics and framework plugins for PyTorch and JAX.
- [Volcano scheduler introduction](https://volcano.sh/en/docs/schduler_introduction/) — **Volcano maintainers (CNCF)** — plugin-based gang scheduling, fair-share and binpack policies for batch workloads on Kubernetes.
- [Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/) — **Kubernetes documentation** — the modern way to request devices with attributes and sharing semantics instead of an opaque integer count.
- [Multi-Instance GPU user guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/) — **NVIDIA** — hard partitions with isolated memory and bandwidth, and how they differ from time-slicing, which oversubscribes a device with no isolation at all.
- [NCCL environment variables](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html) — **NVIDIA** — the knobs that decide which fabric collectives use; the fastest way to discover that a job silently fell back to a slower path.

## Books (free, with chapters)

- [*Machine Learning Engineering Open Book*](https://github.com/stas00/ml-engineering) — **Stas Bekman** — the chapters on network fabrics, node health checks and multi-node debugging are the practical complement to any scheduler's documentation.

## In this platform

- Prerequisites: [Distributed Training — Parallelism, FSDP & ZeRO](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/distributed-training-parallelism-fsdp-zero/distributed-training-parallelism-fsdp-zero) — why placement changes throughput · [Checkpointing & Fault-Tolerant Training](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/checkpointing-and-fault-tolerant-training/checkpointing-and-fault-tolerant-training) — what makes a job safe to preempt
- Also assumed: [GPUs & Accelerators for Deep Learning](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/gpus-and-accelerators-for-deep-learning/gpus-and-accelerators-for-deep-learning) — the NVLink and fabric numbers placement is optimizing
- Next in this sub-area: [Training Cost & Capacity Planning](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/training-infrastructure/training-cost-and-capacity-planning/training-cost-and-capacity-planning) — what the queue is rationing
- The workflow layer above: [ML Pipelines & Orchestration](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/ml-pipelines-and-orchestration/ml-pipelines-and-orchestration) · [Data & Training Platforms](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/data-and-training-platforms/readme)
- Serving shares the same fleet: [Scaling Inference](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/scaling-inference/scaling-inference) · [Cost Optimization for ML Systems](/ai-ml/ai-ml-learning-resources/operations-and-lifecycle/governance-and-economics/cost-optimization/cost-optimization)
- What runs on the allocation: [Pretraining at Scale](/ai-ml/ai-ml-learning-resources/model-building/pretraining/pretraining) · [Supervised Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/supervised-fine-tuning/supervised-fine-tuning) · practitioner workflow [Model Training](/ai-ml/practitioner-workflows/training-and-adaptation/model-training)
