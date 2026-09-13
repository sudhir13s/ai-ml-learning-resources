---
id: "09-llms/quantization/references"
topic: "Quantization — References"
parent: "09-llms/quantization"
type: references
updated: 2026-09-13
---

# Quantization — references

> Companion link library for **[Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization)** and its serving chapter — grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Derive the ruler** — watch [Quantization explained with PyTorch — post-training quantization and quantization-aware training](https://www.youtube.com/watch?v=0VdNflU08yA) (**Umar Jamil**). *The affine scale and zero-point map derived, then both regimes coded.*
2. **See the whole landscape drawn** — read [A Visual Guide to Quantization](https://www.maartengrootendorst.com/blog/quantization/) (**Maarten Grootendorst**). *Formats, PTQ against QAT, GPTQ and GGUF in one illustrated pass.*
3. **Face the crux** — read [A Gentle Introduction to 8-bit Matrix Multiplication (LLM.int8())](https://huggingface.co/blog/hf-bitsandbytes-integration) (**Hugging Face and Dettmers et al.**). *The outlier problem every method on the page is an answer to.*
4. **Go to a method's source** — read [AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration](https://arxiv.org/abs/2306.00978) (**Lin et al., 2023**). *Protect the salient channels by scaling before rounding to 4 bits.*
5. **Run the memory math** — run [Model Memory Calculator](https://huggingface.co/spaces/hf-accelerate/model-memory-usage) (**Hugging Face Accelerate**). *The page's bytes-per-parameter arithmetic for any model and precision.*

## References

- **In this platform**:
  - [Decoder-only Architecture](/ai-ml/ai-ml-learning-resources/models-and-architectures/large-language-models/decoder-only-models/decoder-only-models) — the model whose weights are being quantized.
  - [Inference Optimization and Serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/inference-optimization/inference-optimization) — where quantized weights and cache are served.
  - [Knowledge Distillation](/ai-ml/ai-ml-learning-resources/model-adaptation/knowledge-distillation/knowledge-distillation) — the lever that trains a smaller model instead of storing this one in fewer bits.
  - [KV Cache](/ai-ml/ai-ml-learning-resources/inference-and-serving/kv-cache/kv-cache) — decode is memory-bandwidth-bound; quantizing the cache is the sibling lever.
  - [LoRA and parameter-efficient fine-tuning](/ai-ml/ai-ml-learning-resources/model-adaptation/lora-and-parameter-efficient-fine-tuning/lora-and-parameter-efficient-fine-tuning) — QLoRA is an NF4 base plus LoRA adapters.
  - [model-compression (production example)](/python/python-production-examples/model-compression/readme) — quantize, prune and distil one model into a measured size, latency and quality table.
  - [Pruning and Sparsity](/ai-ml/ai-ml-learning-resources/inference-and-serving/pruning-and-sparsity/pruning-and-sparsity) — the lever that deletes weights rather than coarsening them.
  - [Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization) — the concept page.
  - [Quantization in serving](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization-in-serving) — measured CPU INT8, KV-cache headroom and cost per token.
  - [Quantization intuition (7.05)](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/compression/quantization-intuition) — the one-page mental model.
- **Videos**:
  - [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) — **Andrej Karpathy** — where precision and quantization sit in the full deployment picture.
  - [Deep Dive: Quantizing Large Language Models, part 1](https://www.youtube.com/watch?v=kw7S-3s50uk) — **Julien Simon** — a practitioner's walk through the quantization formats and libraries.
  - [QLoRA: Efficient Finetuning of Quantized LLMs (author talk)](https://www.youtube.com/watch?v=y9PHWGOa8HA) — **Tim Dettmers** — NF4, double quantization and paged optimizers from the author.
  - [Quantization explained with PyTorch — post-training quantization and quantization-aware training](https://www.youtube.com/watch?v=0VdNflU08yA) — **Umar Jamil** — the affine scale and zero-point map derived, then both regimes coded.
- **Courses**:
  - [MIT 6.5940 — TinyML and Efficient Deep Learning Computing](https://hanlab.mit.edu/courses/2024-fall-65940) — **Han Lab (MIT)** — the course behind AWQ and SmoothQuant; lectures on quantization, pruning and efficient inference.
  - [Quantization Fundamentals with Hugging Face](https://www.deeplearning.ai/short-courses/quantization-fundamentals-with-hugging-face/) — **DeepLearning.AI and Hugging Face** — linear quantization and downcasting, hands-on.
  - [Stanford CS336 — Language Modeling from Scratch](https://stanford-cs336.github.io/spring2025/) — **Stanford** — numerical precision and compression within the full systems stack.
- **Interactive**:
  - [Model Memory Calculator](https://huggingface.co/spaces/hf-accelerate/model-memory-usage) — **Hugging Face Accelerate** — the page's memory math for any model and precision.
- **Articles**:
  - [A Gentle Introduction to 8-bit Matrix Multiplication (LLM.int8())](https://huggingface.co/blog/hf-bitsandbytes-integration) — **Hugging Face and Dettmers et al.** — the outlier problem and mixed-precision decomposition, with figures.
  - [A Visual Guide to Quantization](https://www.maartengrootendorst.com/blog/quantization/) — **Maarten Grootendorst** — the definitive illustrated walkthrough of LLM quantization.
  - [Introducing NVFP4 for efficient and accurate low-precision inference](https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/) — **NVIDIA (2025)** — the 4-bit float Blackwell accelerates natively, and why its two-level scale beats INT4.
  - [Introduction to Weight Quantization](https://mlabonne.github.io/blog/posts/Introduction_to_Weight_Quantization.html) — **Maxime Labonne** — from-scratch absmax and zero-point INT8 in code.
  - [Large Transformer Model Inference Optimization](https://lilianweng.github.io/posts/2023-01-10-inference-optimization/) — **Lilian Weng** — quantization among the full menu of inference optimizations.
  - [Making LLMs even more accessible with bitsandbytes, 4-bit quantization and QLoRA](https://huggingface.co/blog/4bit-transformers-bitsandbytes) — **Hugging Face** — NF4, double quantization and QLoRA in practice.
  - [Overview of natively supported quantization schemes in Transformers](https://huggingface.co/blog/overview-quantization-transformers) — **Hugging Face** — GPTQ, bitsandbytes and AWQ side by side.
  - [PyTorch native architecture optimization: torchao](https://pytorch.org/blog/pytorch-native-architecture-optimization/) — **PyTorch team** — quantization as composable dtypes in core PyTorch, the successor to eager-mode `torch.ao.quantization`.
- **Papers**:
  - [A Survey of Quantization Methods for Efficient Neural Network Inference](https://arxiv.org/abs/2103.13630) — **Gholami et al. (2021)** — the reference survey; source of the page's general affine and symmetric formulas.
  - [AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration](https://arxiv.org/abs/2306.00978) — **Lin et al. (2023)** — protect the ~1% salient channels by per-channel scaling before 4-bit.
  - [FP8 Formats for Deep Learning](https://arxiv.org/abs/2209.05433) — **Micikevicius et al. (2022)** — the E4M3 and E5M2 formats hardware now implements.
  - [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers](https://arxiv.org/abs/2210.17323) — **Frantar et al. (2022)** — layer-wise 3–4 bit quantization with Hessian-based error compensation.
  - [KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache](https://arxiv.org/abs/2402.02750) — **Liu et al. (2024)** — the outlier asymmetry applied to the KV cache.
  - [LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale](https://arxiv.org/abs/2208.07339) — **Dettmers et al. (2022)** — emergent outlier features and the mixed-precision decomposition.
  - [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) — **Dettmers et al. (2023)** — the NF4 datatype, double quantization and paged optimizers.
  - [Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference](https://arxiv.org/abs/1712.05877) — **Jacob et al. (2017)** — the canonical affine scale-and-zero-point formulation.
  - [QuIP#: Even Better LLM Quantization with Hadamard Incoherence and Lattice Codebooks](https://arxiv.org/abs/2402.04396) — **Tseng et al. (2024)** — weight quantization pushed to 2 bits.
  - [SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models](https://arxiv.org/abs/2211.10438) — **Xiao et al. (2022)** — migrating activation outliers into the weights for W8A8.
  - [The Super Weight in Large Language Models](https://arxiv.org/abs/2411.02355) — **Yu et al. (2024)** — a handful of individual scalars can destroy quality when rounded.
- **Documentation**:
  - [bitsandbytes documentation](https://huggingface.co/docs/bitsandbytes/main/en/index) — **Hugging Face** — the reference implementation of LLM.int8() and NF4.
  - [bitsandbytes in Transformers](https://huggingface.co/docs/transformers/main/en/quantization/bitsandbytes) — **Hugging Face** — `BitsAndBytesConfig`, NF4 and nested quantization, the options used in the production recipe.
  - [llama.cpp quantization formats (k-quants) README](https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md) — **ggml-org** — GGUF k-quant naming and bit allocations.
  - [LLM inference optimization](https://huggingface.co/docs/transformers/en/llm_optims) — **Hugging Face** — bitsandbytes, GPTQ, AWQ and FP8 in practice, with code.
  - [Quantization schemes supported in Transformers](https://huggingface.co/docs/transformers/en/quantization/overview) — **Hugging Face** — the maintained comparison of schemes and the hardware each needs.
- **Books**:
  - [Efficient Deep Learning](https://efficientdlbook.com/) — **Gaurav Menghani and Naresh Singh** — a full treatment of compression techniques, quantization included.
