---
id: "inference-and-serving/pruning-and-sparsity/references"
topic: "Pruning and Sparsity — References"
parent: "inference-and-serving/pruning-and-sparsity"
type: references
updated: 2026-09-13
---

# Pruning and Sparsity — references

> Companion link library for **[Pruning and Sparsity](/ai-ml/ai-ml-learning-resources/inference-and-serving/pruning-and-sparsity/pruning-and-sparsity)** — grouped by type, alphabetical within each group.

**Start here — suggested path**:
1. **Get the vocabulary** — watch [Lecture 03 — Pruning and Sparsity (Part I), MIT 6.S965](https://www.youtube.com/watch?v=sZzc6tAtTrM) (**MIT HAN Lab, Song Han**). *Granularity, pruning criteria and sparsity ratios from the group behind deep compression.*
2. **Read the magnitude-pruning result** — read [Learning both Weights and Connections for Efficient Neural Networks](https://arxiv.org/abs/1506.02626) (**Han, Pool, Tran and Dally, 2015**). *Prune small weights, retrain, repeat — the loop the page derives.*
3. **Learn why zeros are not a speedup** — read [Accelerating Inference with Sparsity Using the NVIDIA Ampere Architecture and NVIDIA TensorRT](https://developer.nvidia.com/blog/accelerating-inference-with-sparsity-using-ampere-and-tensorrt/) (**NVIDIA**). *The 2:4 pattern hardware can actually accelerate.*
4. **Prune a model yourself** — run [Pruning Tutorial](https://docs.pytorch.org/tutorials/intermediate/pruning_tutorial.html) (**PyTorch**). *Local, global and custom masks with `torch.nn.utils.prune`, then made permanent.*
5. **Scale it to LLMs** — read [A Simple and Effective Pruning Approach for Large Language Models (Wanda)](https://arxiv.org/abs/2306.11695) (**Sun, Liu, Bair and Kolter, 2023**). *Weight times activation norm, with no retraining.*

## References

- **In this platform**:
  - [Knowledge Distillation](/ai-ml/ai-ml-learning-resources/model-adaptation/knowledge-distillation/knowledge-distillation) — the lever that trains a smaller dense model instead of thinning this one.
  - [model-compression (production example)](/python/python-production-examples/model-compression/readme) — magnitude and structured pruning run next to quantization and distillation, with a measured tradeoff table.
  - [Pruning and Sparsity](/ai-ml/ai-ml-learning-resources/inference-and-serving/pruning-and-sparsity/pruning-and-sparsity) — the concept page.
  - [Pruning and sparsity intuition (7.10)](/ai-ml/ai-ml-intuitions/scaling-adaptation-and-efficiency/compression/pruning-and-sparsity-intuition) — the one-page mental model: the bonsai, the mask and the sparsity-is-not-speedup table.
  - [Quantization](/ai-ml/ai-ml-learning-resources/inference-and-serving/quantization/quantization) — the lever that stores the surviving weights in fewer bits.
- **Videos**:
  - [Lecture 03 — Pruning and Sparsity (Part I), MIT 6.S965](https://www.youtube.com/watch?v=sZzc6tAtTrM) — **MIT HAN Lab (Song Han)** — granularity, pruning criteria and sparsity ratios from the group behind deep compression.
- **Courses**:
  - [MIT 6.5940 — TinyML and Efficient Deep Learning Computing](https://hanlab.mit.edu/courses/2024-fall-65940) — **Han Lab (MIT)** — two lectures and a lab on pruning and sparsity.
- **Articles**:
  - [Accelerating Inference with Sparsity Using the NVIDIA Ampere Architecture and NVIDIA TensorRT](https://developer.nvidia.com/blog/accelerating-inference-with-sparsity-using-ampere-and-tensorrt/) — **NVIDIA** — the 2:4 pattern, Sparse Tensor Cores and measured throughput and performance-per-watt gains.
- **Papers**:
  - [A Simple and Effective Pruning Approach for Large Language Models (Wanda)](https://arxiv.org/abs/2306.11695) — **Sun, Liu, Bair and Kolter (2023)** — score by |weight| × input-activation norm, per output, with no retraining.
  - [Accelerating Sparse Deep Neural Networks](https://arxiv.org/abs/2104.08378) — **Mishra et al. (2021)** — the 2:4 fine-grained structured sparsity design and its training recipe.
  - [Learning both Weights and Connections for Efficient Neural Networks](https://arxiv.org/abs/1506.02626) — **Han, Pool, Tran and Dally (2015)** — magnitude pruning with retraining; AlexNet 9× and VGG-16 13× smaller at equal accuracy.
  - [Movement Pruning: Adaptive Sparsity by Fine-Tuning](https://arxiv.org/abs/2005.07683) — **Sanh, Wolf and Rush (2020)** — score weights by how they move during fine-tuning rather than by size.
  - [Optimal Brain Damage](https://proceedings.neurips.cc/paper/1989/hash/6c9882bbac1c7093bd25041881277658-Abstract.html) — **LeCun, Denker and Solla (1989)** — second-derivative saliency: prune the weights whose removal the loss curvature says costs least.
  - [Second order derivatives for network pruning: Optimal Brain Surgeon](https://proceedings.neurips.cc/paper/1992/hash/303ed4c69846ab36c2904d3ba8573050-Abstract.html) — **Hassibi and Stork (1992)** — the full inverse Hessian, which also adjusts the surviving weights.
  - [SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot](https://arxiv.org/abs/2301.00774) — **Frantar and Alistarh (2023)** — 50% sparsity on 175B-parameter models with no retraining.
  - [Sparsity in Deep Learning: Pruning and growth for efficient inference and training in neural networks](https://arxiv.org/abs/2102.00554) — **Hoefler et al. (2021)** — the reference survey, distilled from over 300 papers.
  - [The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks](https://arxiv.org/abs/1803.03635) — **Frankle and Carbin (2019)** — dense networks contain sparse subnetworks that train to full accuracy from their original initialization.
  - [To prune, or not to prune: exploring the efficacy of pruning for model compression](https://arxiv.org/abs/1710.01878) — **Zhu and Gupta (2017)** — the gradual magnitude pruning schedule; large-sparse beats small-dense at equal size.
  - [What is the State of Neural Network Pruning?](https://arxiv.org/abs/2003.03033) — **Blalock et al. (2020)** — a meta-analysis of 81 papers and why pruning results are hard to compare.
- **Documentation**:
  - [Accelerating BERT with semi-structured (2:4) sparsity](https://docs.pytorch.org/tutorials/advanced/semi_structured_sparse.html) — **PyTorch** — `to_sparse_semi_structured` on a real model, with measured speedups on an A100.
  - [Pruning Tutorial](https://docs.pytorch.org/tutorials/intermediate/pruning_tutorial.html) — **PyTorch** — `torch.nn.utils.prune`: local, global and custom pruning, and making masks permanent.
- **Books**:
  - [Efficient Deep Learning](https://efficientdlbook.com/) — **Gaurav Menghani and Naresh Singh** — compression techniques, pruning included, in one open book.
