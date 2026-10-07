---
id: "05-deep-learning/optimizers/adaptive-learning-rates"
topic: "Optimizers: Adaptive Learning Rates"
parent: "05-deep-learning"
chapter_of: "05-deep-learning/optimizers"
chapter: 2
level: intermediate
built_from: ["05-deep-learning/optimizers"]
interview_frequency: very-high
template: concept-chapter
updated: 2026-10-08
tier: core
est_minutes: 10
leads_to: ["05-deep-learning/optimizers/adam-and-adamw"]
core_idea: "Dividing each parameter's step by the root of its squared-gradient history throttles steep directions and frees shallow ones; AdaGrad's running sum starves that rate to zero, and RMSprop's moving average keeps it alive."
title: "Adaptive Learning Rates (AdaGrad · RMSprop)"
minutes: 10
category: optimization-and-training
---

# Adaptive learning rates: a step size for every parameter

Momentum fixes the direction of the step; this page fixes its size, one parameter at a time.

## Adaptive per-parameter rates: AdaGrad, derived

Momentum fixes *direction* but still uses one global $\eta$ for every parameter. The adaptive family attacks the *other* half of the ravine: give **each parameter its own effective learning rate**, automatically scaled down for parameters with large gradients and up for those with small ones.

**AdaGrad** (Duchi, Hazan & Singer 2011) accumulates the *sum of squared gradients* per parameter and divides the step by its square root. Per coordinate $j$:

$$G_{t,j} = G_{t-1,j} + g_{t,j}^2 = \sum_{\tau=1}^{t} g_{\tau,j}^2, \qquad \theta_{t,j} = \theta_{t-1,j} - \frac{\eta}{\sqrt{G_{t,j}}+\epsilon}\, g_{t,j}.$$

The **effective learning rate** for parameter $j$ is $\eta/(\sqrt{G_{t,j}}+\epsilon)$.

- A parameter that has seen big gradients has a large $G$ and so a *small* step; one with tiny, infrequent gradients (a rare embedding row) keeps a *large* step.
- This is precisely what the ravine wants: the steep axis (big $g$) gets throttled, the shallow axis (small $g$) keeps moving.
- AdaGrad shines on **sparse features** for exactly this reason — rare features get their large step when they finally fire.

**The death problem (derive it).** $G_{t,j}$ is a *running sum* of non-negative terms, so it only ever **grows**. Even with a constant gradient $g$, after $t$ steps $G_t = t\,g^2$, so the effective rate is

$$\frac{\eta}{\sqrt{G_t}} = \frac{\eta}{\sqrt{t}\,|g|} \;\xrightarrow{t\to\infty}\; 0.$$

The learning rate **decays monotonically to zero** — it shrinks like $1/\sqrt t$ whether or not you've actually converged. On a long deep-learning run AdaGrad's steps starve and learning *stalls* well before reaching a good minimum. Great for convex, sparse problems; fatal for long non-convex training.

![Effective learning rate over 300 steps on a constant unit-gradient stream. AdaGrad (red) divides by sqrt of a running sum, so its rate decays monotonically toward zero — the death problem. RMSprop (green) divides by sqrt of an EMA, so its rate settles to a stable nonzero value and stays alive. Measured.](images/opt_adagrad_decay.png)

---

## RMSprop, derived

The fix is one word: replace the **growing sum** with a **decaying average**. **RMSprop** (Tieleman & Hinton, Coursera lecture 2012) keeps an **exponential moving average** of squared gradients instead of their cumulative sum:

$$E[g^2]_t = \rho\, E[g^2]_{t-1} + (1-\rho)\, g_t^2, \qquad \theta_t = \theta_{t-1} - \frac{\eta}{\sqrt{E[g^2]_t}+\epsilon}\, g_t,$$

with decay $\rho$ (typically $0.9$ or $0.99$).

- Because old squared gradients **fade** instead of accumulating, $E[g^2]_t$ tracks the *recent* gradient magnitude rather than the all-time total.
- On a constant gradient $g$ it converges to a *fixed point* $E[g^2]_\infty = g^2$ (not $t\,g^2$), so the effective rate **settles at a stable nonzero value** $\eta/|g|$ and never starves — exactly the green curve above.
- RMSprop made adaptive methods practical for deep nets, and its EMA-of-$g^2$ is the second moment that Adam inherits wholesale.

> [!WARNING]
> AdaGrad vs RMSprop is a favorite interview contrast — give the one-line reason.
> - AdaGrad's denominator is a **sum** (only grows → rate starves to 0).
> - RMSprop's is an **EMA** (forgets old gradients → rate stays alive).
> - Adam keeps RMSprop's EMA for precisely this reason.

---

## Example 3 — AdaGrad's effective rate shrinking over steps

Same constant gradient $g=0.1$, $\eta=0.1$, AdaGrad's $G_t=\sum g^2 = t\cdot0.01$:

| $t$ | $G_t = t\cdot0.01$ | $\sqrt{G_t}$ | effective LR $=\eta/\sqrt{G_t}$ | step $=\text{effLR}\cdot g$ |
|---|---|---|---|---|
| 1 | $0.01$ | $0.100$ | $1.000$ | $0.1000$ |
| 4 | $0.04$ | $0.200$ | $0.500$ | $0.0500$ |
| 25 | $0.25$ | $0.500$ | $0.200$ | $0.0200$ |
| 100 | $1.00$ | $1.000$ | $0.100$ | $0.0100$ |
| 400 | $4.00$ | $2.000$ | $0.050$ | $0.0050$ |

The effective rate falls like $1/\sqrt t$ — *halving every time $t$ quadruples* — and keeps shrinking forever, even though the gradient never changed and we never converged. That's the death problem in five rows. RMSprop's EMA, by contrast, would lock the effective rate at $\eta/|g|=1.0$ and hold it.

---

## References

Shared with the topic's companion file — see [Optimizers — references and further reading](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/optimizers#references-further-reading).
