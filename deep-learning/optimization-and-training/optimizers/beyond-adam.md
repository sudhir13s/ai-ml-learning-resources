---
id: "05-deep-learning/optimizers/beyond-adam"
topic: "Optimizers: Beyond Adam"
parent: "05-deep-learning"
chapter_of: "05-deep-learning/optimizers"
chapter: 5
level: intermediate
built_from: ["05-deep-learning/optimizers"]
interview_frequency: very-high
template: concept-chapter
updated: 2026-10-08
tier: core
est_minutes: 10
leads_to: ["05-deep-learning/optimizers/choosing-an-optimizer"]
core_idea: "Adam's per-coordinate denominator is a cheap diagonal stand-in for inverse curvature; second-order and newer optimizers buy back more curvature or spend less memory per step, and against a well-tuned AdamW their measured gains shrink."
title: "Beyond Adam (second order · Lion · Muon)"
minutes: 10
category: optimization-and-training
---

# Beyond Adam: curvature, memory and the frontier

AdamW is the default, not the end of the story; this page places the methods that try to beat it.

## A glimpse of second order: why we don't use the Hessian

Every adaptive method above is secretly chasing something a **second-order** method would compute exactly. The gold standard for using curvature is **Newton's method**:

$$\theta_{t+1} = \theta_t - H_t^{-1} g_t,$$

where $H=\nabla^2 L$ is the **Hessian** (the matrix of second derivatives / curvatures). Multiplying by $H^{-1}$ rescales *and rotates* the step to account for the full curvature — on the ravine quadratic, Newton jumps to the exact minimum in **one** step, because $H^{-1}$ perfectly undoes the conditioning.

*See it on our ravine.* For $L=\tfrac12(a x^2+b y^2)$ the gradient is $g=(ax, by)$ and the Hessian is the constant diagonal $H=\operatorname{diag}(a,b)$, so $H^{-1}g = (ax/a,\ by/b) = (x, y) = \theta$.

- The Newton step is therefore $\theta - H^{-1}g = \theta - \theta = 0$ — it lands **exactly** on the minimum in a *single* step, for *any* starting point and *any* condition number $\kappa$.
- That is the power we're approximating: where SGD took dozens of zig-zag steps and Adam took ~50, Newton needs **one**.
- So why doesn't everyone use it?

**Because $H$ is hopeless at scale.** For a model with $n$ parameters, $H$ is $n\times n$.

- For a 7B-parameter model that's $(7\times10^9)^2\approx 5\times10^{19}$ entries — you cannot *store* it, let alone **invert** it ($O(n^3)$).
- Even forming it is out of reach.
- So practitioners use **approximations**:

- **Adam itself** is the cheapest one: its $1/\sqrt{\hat v}$ is a **diagonal** approximation to $H^{-1}$.
  - It captures per-parameter curvature (the diagonal of $H$) but ignores all the off-diagonal coupling between parameters.
  - "A poor man's second-order method." 
- **K-FAC** approximates $H$ as block-diagonal Kronecker factors per layer — far cheaper to invert than the full matrix, capturing within-layer curvature.
- **Shampoo** keeps small *full-matrix* preconditioners per tensor dimension (a structured, layer-wise curvature).
  - Strong but heavier per step; it and its variants have been used to speed up large-scale training.
- **Sophia** estimates a cheap **diagonal Hessian** via a Hutchinson-style probe and clips it, aiming to roughly halve the steps needed to pretrain an LLM.
- **L-BFGS** builds an implicit low-rank inverse-Hessian from a *history* of gradients (no matrix stored).
  - Excellent for **small, full-batch, deterministic** problems.
  - Doesn't tolerate mini-batch noise, so it's rare in deep learning.

> [!TIP]
> The unifying sentence that ties the whole landscape together: *Adam's $1/\sqrt{\hat v}$ is a cheap diagonal stand-in for the inverse curvature a true second-order method would compute exactly.*
> - Every fancier optimizer (K-FAC, Shampoo, Sophia) is buying back *more* of that curvature information at *more* cost per step.
> - First-order methods win in deep learning because they need only the gradient — which backprop already gives you essentially for free.

---

## Newer optimizers worth knowing

Beyond the AdamW default, a few directions appear in modern recipes and interviews:

- **Lion** (Chen et al. 2023) — a sign-based update $\theta \leftarrow \theta - \eta\,\operatorname{sign}\!\big(\beta_1 m + (1-\beta_1)g\big)$ discovered by symbolic search.
  - It keeps **one** state (vs Adam's two), so *half* the optimizer memory, with competitive results on large models.
  - The sign makes every coordinate's step the same size — a different normalization than Adam's $1/\sqrt{\hat v}$.
- **Adafactor** (Shazeer & Stern 2018) — factorizes the second-moment matrix into row and column statistics to use **sublinear** memory (it doesn't store a full per-parameter $v$).
  - Built for training huge models where Adam's two full states won't fit; used for large T5.
- **8-bit Adam** (Dettmers et al.) — stores Adam's two states in 8-bit with block-wise quantization, cutting optimizer memory ~4× with negligible quality loss; a staple of memory-constrained fine-tuning.
- **Shampoo / Sophia** — the second-order-ish methods above, aimed at faster large-scale pretraining.

### Where the frontier actually moved (2024–2026)

AdamW is still the safe default and still what most teams ship, but it is no longer unchallenged. Three threads matter:

- **Muon** (Keller Jordan, 2024) is the one that broke through. It keeps a momentum buffer like SGD, then **orthogonalizes** the resulting update *matrix*.
  - It approximately replaces $M$ by the $UV^\top$ of its singular value decomposition, computed with a few cheap Newton–Schulz iterations, so no single direction dominates the step.
  - Jeremy Bernstein derives this as steepest descent under a **spectral-norm** trust region, which is exactly what Adam's per-*element* rescaling cannot do: Adam normalizes coordinates, Muon normalizes the matrix.
  - It applies only to 2-D hidden weights (embeddings, biases and norm gains stay on AdamW).
  - It holds the NanoGPT speedrun records, and Moonshot AI scaled it to a 16B mixture-of-experts model at roughly **2× AdamW's compute efficiency**.
- **SOAP** (Vyas, Morwani et al. 2024) closes the loop with the second-order family above.
  - It shows **Shampoo is Adafactor run in Shampoo's eigenbasis**, then runs *Adam* in that eigenbasis instead — keeping the preconditioner's rotation while dropping most of its per-step cost.
  - If "Adam is a diagonal approximation to $H^{-1}$" landed, SOAP is "run Adam in a better-chosen basis." 
- **Schedule-free** methods (Defazio et al. 2024) attack a different knob: hold the learning rate constant and recover the benefit of decay by **averaging the iterates**, removing the schedule — and its committed step budget — from the recipe entirely.

> [!WARNING]
> Be skeptical of headline speedups.
> - *Fantastic Pretraining Optimizers and Where to Find Them* (Wen, Hall, Ma & Liang, Stanford 2025) re-tuned every candidate at every budget.
> - It found the claimed 1.4–2× gains shrink to roughly **1.1–1.4× over a properly tuned AdamW**, with the margin narrowing as models grow.
> - Much of a published optimizer win is a comparison against an under-tuned baseline.
> - The interview-safe statement: *"AdamW is the default; Muon is the first credible challenger with large-scale evidence; the measured gap is smaller than the abstracts claim."*

---

## References

Shared with the topic's companion file — see [Optimizers — references and further reading](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/optimizers#references-further-reading).
