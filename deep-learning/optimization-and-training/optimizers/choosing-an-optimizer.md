---
id: "05-deep-learning/optimizers/choosing-an-optimizer"
topic: "Optimizers: Choosing One"
parent: "05-deep-learning"
chapter_of: "05-deep-learning/optimizers"
chapter: 6
level: intermediate
built_from: ["05-deep-learning/optimizers"]
interview_frequency: very-high
template: concept-chapter
updated: 2026-10-08
tier: core
est_minutes: 14
core_idea: "Pick AdamW for transformers and SGD with Nesterov momentum for vision, tune the learning rate first, budget about 16 bytes per parameter for Adam's state, and guard the run with warmup, decay and clipping."
title: "Choosing an Optimizer"
minutes: 14
category: optimization-and-training
---

# Choosing an optimizer: from the default to a stable run

This page turns the course into decisions: which optimizer, which knobs, and what to check when training misbehaves.

## Where each optimizer is used

- **AdamW** — the default for **transformers, LLMs, and diffusion models**. Heterogeneous/sparse gradients and huge parameter counts are its sweet spot, and its robustness de-risks expensive runs.
- **SGD + momentum / Nesterov** — still standard for **CNNs / vision** (ResNets), where a tuned SGD generalizes better.
- **Adafactor / 8-bit Adam / ZeRO** — when **optimizer-state memory** is the binding constraint (huge models, limited VRAM).
- **Lion** — when you want Adam-like results at half the optimizer memory and are willing to retune.
- **L-BFGS** — small, full-batch, low-noise problems (classical ML, some physics-informed nets), almost never deep nets.

---

## Optimizer-state memory: the load-bearing fact for LLM training

A point worth its own section because it dominates LLM-training cost. Adam/AdamW stores **two extra full-precision states per parameter** — $m$ and $v$ — on top of the weights and gradients.

In mixed-precision training the standard accounting (per parameter) is roughly:

- FP16 weights: 2 bytes, plus an FP32 master copy: 4 bytes,
- FP32 gradient: 4 bytes,
- Adam $m$ (FP32): 4 bytes, Adam $v$ (FP32): 4 bytes.

That's **~16–18 bytes per parameter** before activations — and the **optimizer states alone are 8 of those bytes, twice the size of the FP16 weights.**

- For a 7B model the Adam states are $\sim 7\text{B}\times 8 \approx 56$ GB on their own.
- This is *the* reason full fine-tuning is so expensive.
- It is the direct motivation for **8-bit Adam, Adafactor, ZeRO state-sharding**, and parameter-efficient methods.

> [!TIP]
> This is exactly why [LoRA/PEFT](/ai-ml/ai-ml-learning-resources/model-adaptation/lora-and-parameter-efficient-fine-tuning/lora-and-parameter-efficient-fine-tuning) saves so much memory.
> - By training only a few million low-rank adapter parameters instead of all 7B, you only pay Adam's $2\times$ state overhead on the *adapters*.
> - That shrinks optimizer memory from tens of GB to a fraction of a GB.
> - The optimizer-state cost is the bridge between "optimizers" and "why PEFT exists." 

---

## Application: choosing and configuring an optimizer

**Step 1 — pick it.** Transformer / LLM / diffusion → **AdamW**. CNN/vision tuned for best test accuracy → **SGD + Nesterov momentum**. Memory-bound huge model → **Adafactor / 8-bit Adam**. Prototyping anything → AdamW (robust by default).

**Step 2 — set the knobs.** AdamW defaults are stable:

- $\beta_1=0.9$, $\beta_2=0.999$ (drop $\beta_2$ to $0.95$ for large LLMs, which makes $v$ more responsive to recent gradient scale).
- $\epsilon=10^{-8}$ (raise to $10^{-6}$ in mixed precision).
- Weight decay $0.01$–$0.1$ (excluding biases and norm params).
- The **one** knob you must always tune is the **learning rate**.

**Step 3 — pair it with a schedule and guards.** Warmup + cosine decay, gradient clipping at global-norm $\sim1.0$, and the batch-size↔LR linear-scaling rule. The decision map when training misbehaves:

```mermaid
---
title: Decision map for common training problems
---
graph TD
    P{"Training problem?"}:::focus
    P -->|"loss explodes / NaN"| C["Clip gradients (global-norm ~1)<br/>+ lower LR<br/>(+ raise ε in fp16)"]
    P -->|"loss spikes early"| W["LR warmup<br/>(Adam's v̂ is noisy at start)"]
    P -->|"loss plateaus"| S["LR schedule:<br/>cosine / step decay"]
    P -->|"trains but overfits"| D["Weight decay<br/>(use AdamW, not coupled L2)"]
    P -->|"out of memory"| M["8-bit optimizer / Adafactor /<br/>ZeRO state-sharding"]
    C --> OK(["stable training"]):::success
    W --> OK
    S --> OK
    D --> OK
    M --> OK
```

> [!WARNING]
> In mixed-precision (FP16) training, the default $\epsilon=10^{-8}$ can **underflow** inside $\sqrt{\hat v}+\epsilon$ when $\hat v$ is tiny, making the denominator collapse and the step explode.
> - If FP16 diverges early while FP32 is fine, **raise $\epsilon$** (to $10^{-6}$) before suspecting anything else.
> - BF16, with its larger exponent range, mostly sidesteps this.

---

## Gradient clipping

Sometimes a single unlucky batch (or an instability early in training) produces an **enormous** gradient.

- Taken at face value it blows the weights to `NaN` in one step — the **exploding-gradient** failure, common in RNNs and early/large LLM training.
- **Gradient clipping** caps the gradient *before* the optimizer sees it:


- **Clip-by-global-norm (standard).** Compute the norm of the *entire* gradient vector (all parameters concatenated). If $\lVert g\rVert > c$, rescale $g \leftarrow c\,g/\lVert g\rVert$.
  - Keeps the *direction* intact and only caps the *magnitude* — the right thing to do.
  - LLMs almost universally clip the global norm to $\sim1.0$.
- **Clip-by-value.** Clamp each component into $[-c,c]$ independently.
  - Cruder, and it *changes the direction* (it can rotate the gradient), so it's rarely the first choice.

> [!TIP]
> Clip-by-**global-norm** over *all* parameters at once is the near-universal choice for transformer training.
> - Apply it *after* backprop and *before* `optimizer.step()`.
> - If your loss occasionally spikes to `NaN`, turning on (or tightening) gradient clipping is the very first thing to try — before touching the learning rate or the architecture.

---

## Learning-rate schedules and warmup (pointer)

The optimizer sets the *direction and per-parameter scaling*; the **schedule** sets how the global $\eta$ changes over training — and you almost never use a constant rate.

- The standard recipe is **warmup then decay**: ramp $\eta$ up from ~0 over the first few hundred/thousand steps, then anneal it down (cosine, linear, or inverse-sqrt).
- Warmup exists *specifically because* Adam's $\hat v$ estimate is unreliable in the very first steps (precisely where bias correction is working hardest).
- Big early steps are dangerous, and a gentle ramp keeps them safe.

This page deliberately stops here — the schedule has its own full treatment.

**→ [Learning-Rate Schedules & Warmup](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/learning-rate-schedules-and-warmup/learning-rate-schedules-and-warmup)** covers cosine/linear/inverse-sqrt decay, warmup length, and restarts in depth.

> [!NOTE]
> **Batch size and learning rate move together.**
> - The **linear scaling rule** (Goyal et al. 2017): multiply the batch size by $k$ and multiply $\eta$ by $\sim k$ (with warmup for stability).
> - The justification is the $1/B$ noise law derived earlier.
> - A $k\times$ larger batch gives a $\sqrt k\times$ less-noisy gradient, which can tolerate (and needs) a proportionally bigger step to make the same progress per epoch.

> [!TIP]
> Can't fit a big batch in memory? **Gradient accumulation** sums the gradients over several micro-batches before one optimizer step.
> - It simulates a larger *effective* batch — then apply the linear-scaling LR as if the batch really were that size.
> - It's how small-GPU setups train with large effective batch sizes.

---

## Recap and rapid-fire

**If you remember nothing else:** the optimizer turns a noisy mini-batch gradient into a good weight step against an ill-conditioned, non-convex surface.

- **SGD** steps downhill (noise $\propto 1/B$).
- **Momentum/Nesterov** add a velocity that averages noise, coasts through saddles, and accelerates the valley ($\sim\!1/(1-\beta)$ amplification).
- **AdaGrad** gives per-parameter rates but starves (sum of $g^2$), and **RMSprop** fixes that with an EMA.
- **Adam** = momentum + RMSprop + bias correction, and **AdamW** decouples weight decay and is the transformer/LLM default.
- Pair it with **warmup + decay** and **gradient clipping**.
- Adam's real edge is **robustness**, not raw speed — and its $1/\sqrt{\hat v}$ is a cheap diagonal stand-in for the Hessian we can't afford.

**Quick-fire — say these out loud:**

- *SGD update?* $\theta \leftarrow \theta - \eta g$, with $g$ a mini-batch estimate whose variance $\propto 1/B$.
- *Why can mini-batch noise *help*?* It rattles the iterate off saddles and out of sharp minima, biasing toward flatter, better-generalizing solutions.
- *Momentum update + effective step?* $v=\beta v+g,\ \theta-=\eta v$; effective step $\approx \eta/(1-\beta)\approx10\eta$ at $\beta=0.9$.
- *Nesterov vs momentum?* Nesterov evaluates the gradient at the *look-ahead* point $\theta-\eta\beta v$ — it starts braking a step early, so it overshoots less.
- *AdaGrad vs RMSprop?* AdaGrad sums all past $g^2$ (rate decays to 0 — the death problem); RMSprop uses an EMA (rate stays alive).
- *Adam's m and v?* $m$ = EMA of $g$ (direction); $v$ = EMA of $g^2$ (per-parameter volatility); update $\approx$ direction $\div$ volatility.
- *Why bias-correct, exactly?* $m,v$ start at 0 so $\mathbb{E}[v_t]=(1-\beta_2^t)\mathbb{E}[g^2]$ is too small early; dividing by $(1-\beta^t)$ unbiases it and prevents a huge first step.
- *Weight decay vs L2?* Identical for SGD; in Adam, L2 flows through $1/\sqrt{\hat v}$ so high-gradient weights get under-decayed — AdamW decouples the decay (better generalization, the LLM default).
- *Gradient clipping?* Cap the **global** gradient norm ($\sim1.0$) to stop exploding-gradient `NaN`s — keeps direction, caps magnitude.
- *Batch size ↔ LR?* Linear scaling rule: $\times k$ batch → $\times k$ LR (with warmup), justified by the $1/B$ noise law.
- *Adam's memory cost?* Two extra states per parameter (~$2\times$ the FP16 weights, ~56 GB for a 7B model) — the reason for 8-bit Adam, Adafactor, ZeRO, and a big motivation for LoRA/PEFT.
- *Why no second-order for deep nets?* The Hessian is $O(n^2)$ to store / $O(n^3)$ to invert; Adam's $1/\sqrt{\hat v}$ is a cheap diagonal approximation; K-FAC/Shampoo/Sophia buy back more curvature at more cost.
- *SGD vs Adam generalization?* Tuned SGD+momentum often generalizes better (vision); Adam/AdamW trains faster, tolerates the LR, and is essential for transformers/LLMs.

---

## References

Shared with the topic's companion file — see [Optimizers — references and further reading](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/optimizers#references-further-reading).
