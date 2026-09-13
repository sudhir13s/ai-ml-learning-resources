---
id: "inference-and-serving/packaging-and-serving/llm-serving-engines/references"
topic: "LLM Serving Engines (vLLM · SGLang · TGI · TensorRT-LLM) — References"
parent: "inference-and-serving/packaging-and-serving/llm-serving-engines"
type: references
updated: 2026-09-13
---

# LLM Serving Engines (vLLM · SGLang · TGI · TensorRT-LLM) — references

> Companion link library for **[LLM Serving Engines](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/llm-serving-engines/llm-serving-engines)** (the teaching page). External sources and internal links, grouped by type, alphabetical within each group; every entry is from a primary author or a recognized deep explainer.

**Start here — suggested path**:

1. **See the engine from its creators** — watch [Fast LLM Serving with vLLM and PagedAttention](https://www.youtube.com/watch?v=5ZlavKF_98U). *Paging and batching explained by the people who built them.*
2. **Read the design** — read [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180). *Block tables and why KV waste drops to a few percent.*
3. **Stand one up** — work through [vLLM — Online Serving](https://docs.vllm.ai/en/latest/serving/online_serving/). *`vllm serve` and the OpenAI-compatible endpoints Atlas uses.*
4. **Add tenants** — read [vLLM — LoRA Adapters](https://docs.vllm.ai/en/latest/features/lora.html), then [S-LoRA](https://arxiv.org/abs/2311.03285). *The flags first, then how thousands of adapters share one GPU.*
5. **Know the alternative** — read [SGLang: Efficient Execution of Structured Language Model Programs](https://arxiv.org/abs/2312.07104). *When shared prefixes and structured output make RadixAttention the better engine.*

**In this platform**:
- [Continuous Batching and Scheduling](/ai-ml/ai-ml-learning-resources/inference-and-serving/continuous-batching-and-scheduling/continuous-batching-and-scheduling) — the per-step scheduler every engine runs.
- [Inference Optimization](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization) — why decode is memory-bound, PagedAttention and the serving levers.
- [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache) — the per-token cache formula behind every block on the page.
- [KV Cache in Production](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache-in-production) — the engines' cache bets, preemption and disaggregated serving.
- [LoRA and Parameter-Efficient Fine-Tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/lora-and-parameter-efficient-fine-tuning/lora-and-parameter-efficient-fine-tuning) — the adapters swapped per tenant.
- [Model Packaging and Containerization](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/model-packaging-and-containerization/model-packaging-and-containerization) — shipping weights safely before an engine loads them.
- [Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization) — the quality and cost side of the precision table.
- [Scaling Inference](/ai-ml/ai-ml-learning-resources/inference-and-serving/packaging-and-serving/scaling-inference/scaling-inference) — many engine replicas under variable traffic.
- [Speculative Decoding](/ai-ml/ai-ml-learning-resources/inference-and-serving/speculative-decoding/speculative-decoding) — a latency lever for the decode loop.

**Videos**:
- [Fast LLM Serving with vLLM and PagedAttention](https://www.youtube.com/watch?v=5ZlavKF_98U) — **Anyscale** — the vLLM authors on paging and batching.
- [vLLM: Easy, Fast, and Cheap LLM Serving for Everyone](https://www.youtube.com/watch?v=9ih0EmcXRHE) — **PyTorch (Woosuk Kwon and Xiaoxuan Liu, UC Berkeley)** — engine architecture from its creators.
- [vLLM Office Hours: Distributed Inference with vLLM](https://www.youtube.com/watch?v=LH2QZehVJoc) — **Neural Magic (vLLM maintainers)** — what changes once one model spans several GPUs.

**Articles**:
- [How continuous batching enables 23x throughput in LLM inference while reducing p50 latency](https://www.anyscale.com/blog/continuous-batching-llm-inference) — **Anyscale (Cade Daniel et al.)** — the canonical measurement of batching in real engines.
- [vLLM V1: a major upgrade to vLLM's core architecture](https://blog.vllm.ai/2025/01/27/v1-alpha-release.html) — **vLLM maintainers** — the scheduler and KV-cache manager rewrite behind current defaults.

**Papers**:
- [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180) — **Kwon et al. (2023)** — the vLLM paper: block tables and near-zero KV waste.
- [S-LoRA: Serving Thousands of Concurrent LoRA Adapters](https://arxiv.org/abs/2311.03285) — **Sheng et al. (2023)** — unified paging of adapters and KV cache for multi-tenant serving.
- [SGLang: Efficient Execution of Structured Language Model Programs](https://arxiv.org/abs/2312.07104) — **Zheng et al. (2023)** — RadixAttention and fast constrained decoding.

**Documentation**:
- [SGLang documentation](https://docs.sglang.ai/) — **SGLang team** — launching and tuning the RadixAttention engine.
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) — **NVIDIA** — building compiled engines and in-flight batching.
- [Text Generation Inference — LoRA](https://huggingface.co/docs/text-generation-inference/conceptual/lora) — **Hugging Face** — `LORA_ADAPTERS` and per-request `adapter_id` for existing TGI deployments.
- [Text Generation Inference repository](https://github.com/huggingface/text-generation-inference) — **Hugging Face** — the maintenance-mode notice and the recommended successors.
- [vLLM — LoRA Adapters](https://docs.vllm.ai/en/latest/features/lora.html) — **vLLM maintainers** — `--enable-lora`, `--lora-modules`, `--max-loras` and `--max-lora-rank`.
- [vLLM — Online Serving](https://docs.vllm.ai/en/latest/serving/online_serving/) — **vLLM maintainers** — `vllm serve` and the OpenAI-compatible endpoints.
- [vLLM — Production Metrics](https://docs.vllm.ai/en/latest/usage/metrics.html) — **vLLM maintainers** — the queue, KV-usage and latency metrics named in the pitfalls.

**Books**:
- [AI Engineering — Ch. 9 "Inference Optimization"](https://huyenchip.com/books/) — **Chip Huyen (2025)** — serving end to end, from engine choice to cost.
