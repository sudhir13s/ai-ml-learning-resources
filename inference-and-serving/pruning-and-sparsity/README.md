# Pruning and Sparsity — topic specification

**Purpose:** the model-layer home for removing weights from a trained network — which weights to zero, what the zeros actually buy in memory and speed, and how to recover the accuracy they cost.

## Files in this topic

- **`pruning-and-sparsity.md`** — the teaching page, a `concept-deep` page at the `standard` tier.
- **`pruning-and-sparsity.references.md`** — the companion link library: papers, courses, videos, documentation and in-platform links.
- **`code/sparsity_accuracy_cliff.py`** — the runnable PyTorch script behind every number on the page.
  - A 3×4 matrix worked two ways (global and per-row masks).
  - The one-shot sparsity sweep that shows the accuracy cliff.
  - An iterative prune-and-fine-tune schedule that pushes the cliff back.
  - A dense-versus-compressed-sparse-row (CSR) storage comparison.
- **`images/compress_pruning_curve.png`** — test accuracy against sparsity for the one-shot sweep. Its values are the script's measured output, rounded.
- **`images/compress_stack.png`** — the illustrative size chart for stacking distillation, pruning and quantization on one model.

## What the teaching page covers today

- **The problem:** most of a trained network's weights barely contribute to its output.
- **Intuition:** why deleting the smallest weights barely changes what the network computes.
- **Unstructured vs structured pruning:** scattered zeros versus removing whole channels, with the arithmetic for shrinking the dense matrix.
- **Magnitude pruning, derived:** the mask, the threshold as a percentile, and the off-by-one between the two ways of computing it.
- **Two worked examples:** one row of eight weights, then a 3×4 matrix pruned globally and per row.
- **Global ranking and the iterative loop:** why one threshold shared across layers beats a fixed rate per layer, and why pruning is done gradually.
- **Sparsity is not a smaller file and not a speedup:** measured dense and CSR storage sizes, and what hardware needs before zeros save time.
- **Code — the sparsity–accuracy cliff:** a one-shot sweep and an iterative schedule, both with real output.
- **Reading the cliff:** the curve, the knee, and the random-guess floor.
- **Where pruning sits among the three levers:** a router from the binding constraint (memory, latency, storage or architecture) to quantization, pruning or distillation.
- **Stacking the levers:** why the savings multiply.
- **Recovering accuracy:** fine-tuning with a fixed mask.
- **Pitfalls**, **In production** and the **References** pointer.

## Still to author

- **Importance beyond magnitude.** This section will explain the scores that replace |w|:
  - **Optimal Brain Damage** and **Optimal Brain Surgeon**, which score a weight by the loss increase that the Hessian predicts for removing it.
  - **Movement pruning**, which scores weights by how they change during fine-tuning.
  - **Wanda**, which scores by |weight| × input-activation norm.
  - **SparseGPT**, which prunes a large language model in one shot with a layer-wise reconstruction solve.
  - Each score will be applied to the page's 3×4 matrix, so the reader sees its mask differ from the magnitude mask.
- **A structured pruning worked example.** Removing attention heads, multilayer-perceptron channels and whole layers from a small transformer.
  - The parameter and floating-point-operation counts of the dense matrices that remain, worked out explicitly.
  - Measured latency before and after on CPU.
- **2:4 semi-structured sparsity.** The rule that exactly two of every four weights are nonzero.
  - Why that pattern lets Sparse Tensor Cores skip work.
  - A conversion with `torch.sparse.to_sparse_semi_structured`.
  - The documented speedups quoted with their hardware conditions, since the kernel needs a supported GPU.
- **Iterative schedules.** The cubic sparsity schedule of Zhu and Gupta, derived.
  - The prune → fine-tune loop written as a reusable PyTorch function with `torch.nn.utils.prune`.
  - A curve of the schedule next to the accuracy it keeps.
- **The Lottery Ticket Hypothesis.** A full treatment: rewinding weights to their initial values, iterative magnitude pruning, and a small reproduction showing a sparse subnetwork that trains to dense accuracy.
- **Sparse storage formats.** Coordinate (COO) and CSR layouts drawn out on the 3×4 example.
  - The byte count of each index array, and the sparsity at which CSR starts to beat dense storage.
- **Diagrams:**
  - A heatmap of the mask on a real layer.
  - The shapes of unstructured and structured sparsity side by side.
  - The block layout of a 2:4 pattern.
  - The iterative schedule curve.
- **What-if ablations, recap and rapid-fire.** Each ablation will predict and then measure the result.
  - Per-layer instead of global thresholds.
  - Pruning biases.
  - Skipping fine-tuning.
  - Magnitude versus random masks.
  - The page will close with a recap and interview rapid-fire questions.
