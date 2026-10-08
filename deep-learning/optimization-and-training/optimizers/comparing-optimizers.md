---
id: "05-deep-learning/optimizers/comparing-optimizers"
topic: "Optimizers: Comparing Them"
parent: "05-deep-learning"
chapter_of: "05-deep-learning/optimizers"
chapter: 4
level: intermediate
built_from: ["05-deep-learning/optimizers"]
interview_frequency: very-high
template: concept-chapter
updated: 2026-10-08
tier: core
est_minutes: 12
leads_to: ["05-deep-learning/optimizers/beyond-adam"]
core_idea: "On one ravine the optimizers differ less in raw speed than in robustness: Adam tolerates a hundredfold range of learning rates where SGD and RMSprop diverge past a sharp limit, while tuned SGD with momentum can still generalize better in vision."
title: "Comparing Optimizers"
minutes: 12
category: optimization-and-training
---

# Comparing optimizers: one ravine, four rules, one debate

With every rule derived, this page runs them side by side and asks which one actually wins.

## The measured comparison: four rules on one ravine

Stochastic gradient descent (SGD), momentum, RMSprop and Adam — the rules derived on the previous pages — run for real over 80 steps on the ravine and produce the measured loss curves below, the quantitative version of the [trajectory plot](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/optimizers).

![Loss versus iteration for SGD, Momentum, RMSprop, and Adam on the same ill-conditioned ravine (log-scale loss). SGD descends steadily; Momentum overshoots and rings before settling; RMSprop and Adam rescale each axis and drive the loss down many orders of magnitude. The relative ordering is surface- and LR-dependent — the point is the qualitatively different shapes, all measured by actually running each optimizer.](images/opt_loss_curves.png)

> [!NOTE]
> Don't over-read the *ordering* in any single loss plot.
> - On a clean quadratic a well-tuned plain SGD or RMSprop is genuinely hard to beat.
> - Adam's headline advantage is **robustness across learning rates and gradient scales**, not raw speed on a toy bowl.
> - The shapes are what teach: SGD's smooth geometric decay, Momentum's overshoot-and-ring, the adaptive methods' per-axis rescaling.

---

## Race them yourself

The same four rules on the same ravine $L=\tfrac12(12x^2+y^2)$ from the same start $(-9, -4.5)$ — change one knob and watch who converges, rings, or blows up.

<!-- EXPLORER: optimizer-race {
  "heading": "SGD, Momentum, RMSprop and Adam on the ravine",
  "surface": { "kind": "ravine", "a": 12, "b": 1 },
  "domain": { "xMin": -10, "xMax": 10, "yMin": -6, "yMax": 6 },
  "start": [-9, -4.5],
  "steps": 80,
  "heightScale": "log",
  "colormap": "theme",
  "optimizers": [
    { "kind": "sgd", "lr": 0.13, "lrRange": [0.005, 0.3] },
    { "kind": "momentum", "lr": 0.012, "lrRange": [0.001, 0.3], "beta": 0.9 },
    { "kind": "rmsprop", "lr": 0.2, "lrRange": [0.005, 2], "rho": 0.9 },
    { "kind": "adam", "lr": 0.3, "lrRange": [0.005, 2], "beta1": 0.9, "beta2": 0.999 }
  ],
  "caption": "curvature 12 in x, 1 in y"
} -->
> [!EXPLORER]
> **The optimizer race**
> Four optimizers start together on the ravine; press Play or Step, drag to rotate the 3D surface, and read the paths on the contour map and the loss curves beside it. Each card has its optimizer's learning rate (and β, ρ, β₁, β₂) and its live verdict. Without the widget, the loss-curve and learning-rate-sweep figures on this page and the trajectory figure on the [first page](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/optimizers) show the same runs.

What to try, and what each move proves:

- **Start at the defaults (the figures' rates).** SGD, RMSprop and Adam converge (final loss $2.1\times10^{-9}$, $4.3\times10^{-9}$, $2.0\times10^{-3}$); Momentum is still ringing at 0.10.
- **Push SGD's η past $2/12 \approx 0.167$.** The steep-axis factor $|1-12\eta|$ passes 1, the zig-zag grows, and the card flips to **diverged** — the stability limit derived on the [first page](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/optimizers).
- **Raise Momentum's η and watch the loop.** Velocity overshoots the walls; lower β toward 0 and it turns back into plain SGD.
- **Sweep Adam's η from 0.005 to 2.** It slows or rings but never diverges — the wide band in the learning-rate sweep figure.
- **Untick bias correction.** Adam's first step jumps about 30× too far, exactly as the [bias-correction derivation](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/adam-and-adamw) predicts.

---

## The family at a glance

Every rule in this course, side by side — what state it keeps, what it adds, and where it lands.

| Optimizer | Update (core) | State / param | Adds over the previous rung | Best at | Watch out for |
|---|---|---|---|---|---|
| **[SGD](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/optimizers)** | $\theta -= \eta g$ | none | the baseline | clean, well-conditioned problems | zig-zags on ravines; one rate for all |
| **+ [Momentum](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/momentum-and-nesterov)** | $v=\beta v+g;\ \theta-=\eta v$ | 1 vector ($v$) | velocity (low-pass filter) | ravines, saddles, noisy gradients | inertia overshoots — lower $\eta$ |
| **+ Nesterov** | lookahead gradient | 1 vector | brakes a step early | convex / vision SGD | same as momentum |
| **[AdaGrad](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/adaptive-learning-rates)** | $\theta-=\eta g/\sqrt{\sum g^2}$ | 1 vector ($G$) | per-parameter rates | sparse features, convex | rate **decays to 0** (death) |
| **[RMSprop](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/adaptive-learning-rates)** | $\theta-=\eta g/\sqrt{\mathrm{EMA}[g^2]}$ | 1 vector | a moving average (EMA) fixes the decay | recurrent networks (RNNs), non-stationary | no momentum, no bias-correct |
| **[Adam](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/adam-and-adamw)** | $\theta-=\eta\,\hat m/(\sqrt{\hat v}+\epsilon)$ | 2 vectors ($m,v$) | momentum + adaptive + bias-correct | transformers, default everywhere | not always convergent (→ AMSGrad) |
| **[AdamW](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/adam-and-adamw)** | Adam $+\ \lambda\theta$ decoupled | 2 vectors | decoupled weight decay | **the large language model (LLM) and transformer default** | use AdamW, not coupled-L2 Adam |
| **[Lion](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/beyond-adam)** | $\theta-=\eta\,\mathrm{sign}(\cdots)$ | 1 vector | half the memory of Adam | huge models, memory-bound | needs re-tuning vs Adam |

> [!NOTE]
> Read the table top-to-bottom and you've recovered the whole ladder.
> - Each row keeps everything below it and adds *one* labelled idea.
> - That single-idea-per-rung structure is the cleanest way to hold the family in your head — and to *teach* it back in an interview.

---

## The SGD-vs-Adam generalization debate

A genuine open question worth understanding, because interviewers love it and the honest answer names *both* sides.

**The phenomenon.** Adam trains *faster* and is far more forgiving of the learning rate, yet a well-tuned **SGD + momentum** often *generalizes better*.

- Lower **test** error, especially on vision tasks with convolutional networks (CNNs) (which is why ResNets are still trained with SGD+momentum to this day).
- Adam can reach a lower *training* loss while landing at a slightly *worse* test loss.

**Why (the leading explanations).** An active research area, not a settled law.

- SGD's update is a noisier, more "uniform" step that tends to settle in **flat, wide minima** (the [SGD intuition](/ai-ml/ai-ml-intuitions/learning-and-optimization/first-order-optimization/gradient-descent-and-stochastic-gradient-descent-intuition) pictures why), which generalize better than the **sharp** minima adaptive methods can be drawn toward.
- Adam's per-parameter rescaling can also interact badly with naive L2 (the very problem AdamW fixes — and AdamW closes much of the historical gap).

**So why does Adam *dominate* transformers and LLMs?** Three reasons that flip the trade-off:
1. **Heterogeneous, sparse gradients.** Token-embedding rows, attention projections, LayerNorm gains, and multilayer-perceptron (MLP) weights have *wildly* different gradient scales.
   - Adam's per-parameter rescaling is essential; one global SGD rate simply cannot serve them all.
   - SGD often won't even *converge* on a transformer at a usable rate.
2. **Robustness at scale.** You get *one* shot at a multi-million-dollar pretraining run.
   - Adam's tolerance of the learning rate and its self-normalization make training *reliable*.
   - That matters more than squeezing out a fraction of test-loss.
3. **The generalization gap is small/absent here.** For large language models trained ~once over enormous data, the flat-minima generalization edge of SGD largely evaporates, while Adam's stability advantage is decisive.

![Final loss after 80 steps versus learning rate, swept across three orders of magnitude on the ravine. SGD (red) and Momentum (amber) plunge to a deep minimum at their sweet-spot rate but then hit a cliff and diverge to the diverged line once the rate exceeds their stability limit. RMSprop (blue) has a razor-sharp optimum and also diverges past it. Adam (green) stays in a low, flat band across the entire range — it never finds the very deepest point, but it never blows up either. That wide tolerance, not raw speed, is Adam's real headline advantage. Measured.](images/opt_lr_robustness.png)

> [!NOTE]
> **The crisp interview answer:**
> - Tuned SGD+momentum can generalize better and is standard in vision.
> - Adam/AdamW trains faster, tolerates the learning rate, and is essential for transformers/LLMs because their gradients are too heterogeneous for a single global rate.
> - **AdamW is the modern default; SGD is the vision specialist.**
> - Naming both, with the *reason*, is what separates a strong answer from a memorized one.

> [!TIP]
> The plot above is *exactly* why Adam is the safe default for an expensive one-shot run.
> - You don't need to find the razor-thin optimal learning rate that SGD/RMSprop demand — anything in a broad band works, so you spend your compute training rather than tuning.
> - Adam trades a sliver of best-case performance for a huge gain in *reliability*.

---

## References

Shared with the topic's companion file — see [Optimizers — references and further reading](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/optimizers#references-further-reading).
