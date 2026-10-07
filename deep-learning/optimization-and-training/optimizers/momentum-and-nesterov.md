---
id: "05-deep-learning/optimizers/momentum-and-nesterov"
topic: "Optimizers: Momentum and Nesterov"
parent: "05-deep-learning"
chapter_of: "05-deep-learning/optimizers"
chapter: 1
level: intermediate
built_from: ["05-deep-learning/optimizers"]
interview_frequency: very-high
template: concept-chapter
updated: 2026-10-08
tier: core
est_minutes: 12
leads_to: ["05-deep-learning/optimizers/adaptive-learning-rates"]
core_idea: "Momentum is an exponential moving average of gradients: aligned steps add up to about 1/(1-β) times the raw step while oscillating ones cancel, and Nesterov reads the gradient where that velocity is about to land so it brakes one step early."
title: "Momentum and Nesterov"
minutes: 12
category: optimization-and-training
---

# Momentum and Nesterov: giving the step a memory

The [ravine](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/optimizers) defeats a memoryless step; this page gives the step a memory of past gradients, then makes that memory look ahead.

## Momentum, derived

Plain SGD reacts to *this* step's gradient and nothing else. Momentum gives it memory. Define a **velocity** $v_t$ as an exponentially-weighted accumulation of gradients, then step along the velocity:

$$\boxed{\;v_t = \beta\, v_{t-1} + g_t, \qquad \theta_t = \theta_{t-1} - \eta\, v_t\;}$$

with $v_0=0$ and momentum coefficient $\beta\in[0,1)$ (typically $0.9$). This is the Polyak / "heavy-ball" form (1964); PyTorch's default is the equivalent variant $v_t=\beta v_{t-1}+g_t$.

**Unroll it to see what the velocity *is*.** Expanding the recurrence,

$$v_t = g_t + \beta g_{t-1} + \beta^2 g_{t-2} + \dots = \sum_{k=0}^{t-1}\beta^k\, g_{t-k}.$$

So $v_t$ is a **discounted sum of all past gradients**, weighting recent ones most and fading old ones geometrically by $\beta^k$. With $\beta=0.9$, a gradient's weight halves about every 7 steps and the "effective window" is roughly $1/(1-\beta)=10$ gradients. **Momentum is a low-pass filter on the gradient stream.**

**Why it cancels oscillation and accelerates the valley.** Decompose the gradient into its steep-axis and shallow-axis components:

- **Steep axis** — the gradient *flips sign* every step as the ball oscillates across the ravine. In the discounted sum those alternating $+,-,+,-$ terms **cancel**, so the accumulated velocity across the steep axis stays small. The oscillation is *damped*.
- **Shallow axis** — the gradient points the *same* way every step (steadily downhill along the valley). Those aligned terms **reinforce**, so velocity *grows* toward a steady-state.

**Derive the steady-state (effective) step.** Suppose the gradient is roughly constant $g$ along the valley. The velocity approaches a fixed point $v_\infty = \beta v_\infty + g$, giving the geometric sum

$$v_\infty = \frac{g}{1-\beta}, \qquad\text{so the effective step}\quad \eta\,v_\infty = \frac{\eta}{1-\beta}\,g.$$

At $\beta=0.9$ that's a **10×** amplification of the raw-gradient step along consistent directions — momentum literally moves ten times faster down the valley than plain SGD at the same $\eta$, while *shrinking* the wasteful cross-axis motion.

> [!NOTE]
> This $1/(1-\beta)$ amplification is *why you use a smaller learning rate with momentum (and with Adam) than with plain SGD.*
> - The inertia already multiplies every consistent step by ~10; keep the old $\eta$ and you'll overshoot.
> - Reach for momentum and instinctively drop $\eta$.

> [!WARNING]
> Be careful which momentum convention a framework uses.
> - PyTorch's `SGD(momentum=β)` uses $v_t=\beta v_{t-1}+g_t$ then $\theta-=\eta v_t$ (so the effective step is $\sim\eta/(1-\beta)$).
> - Some texts write $v_t=\beta v_{t-1}+(1-\beta)g_t$ (a true exponential moving average (EMA), where the $1-\beta$ is folded in).
> - They differ by a constant factor absorbed into $\eta$ — same dynamics, but it changes what "$\eta=0.1$" *means*.
> - Always check the form before porting hyperparameters.

---

## Nesterov accelerated gradient, derived

Plain (heavy-ball) momentum has a flaw: it computes the gradient at *where you are now*, then takes a big inertial step.

- If the velocity is about to carry you past the minimum, you only find out *after* you've overshot.
- **Nesterov's accelerated gradient** (Nesterov 1983; popularized for deep nets by Sutskever et al. 2013) fixes this with a **lookahead**: evaluate the gradient at the point the momentum is *about to* take you, not where you stand.

Concretely, first take the inertial part of the step to a *lookahead* point $\tilde\theta = \theta_{t-1} - \eta\beta\,v_{t-1}$, evaluate the gradient *there*, and only then complete the update:

$$v_t = \beta\, v_{t-1} + \nabla L\big(\underbrace{\theta_{t-1} - \eta\beta\,v_{t-1}}_{\text{lookahead point}}\big), \qquad \theta_t = \theta_{t-1} - \eta\, v_t.$$

**Why this corrects overshoot.** If the velocity is about to carry you up the *far* wall of the valley, the gradient at the lookahead point already *points back*.

- Nesterov starts braking *one step early*, before it has overshot, instead of reacting a step late like plain momentum.
- It's "look before you leap": same inertia, but the gradient is sampled where you're heading.
- The result is a **provably better convergence rate** on convex problems ($O(1/t^2)$ vs momentum's $O(1/t)$) and, in practice, a slightly faster and more stable descent.
- Nesterov momentum is the standard for SGD-with-momentum in vision.

> [!TIP]
> In code, the math above is awkward (you'd need the gradient at a shifted point).
> - Frameworks use an **algebraically equivalent reformulation** in terms of the current parameters that needs only the ordinary gradient $\nabla L(\theta_{t-1})$ — that's what `torch.optim.SGD(nesterov=True)` implements.
> - Same trajectory, no extra forward pass.

---

## Example 1 — momentum vs plain GD on a ravine, one step at a time

Take the ravine $L=\tfrac12(10x^2 + y^2)$, so $g=(10x,\,y)$, start at $\theta_0=(1,\,1)$, and use $\eta=0.18$ (just *below* the steep-axis stability limit $2/10=0.2$, so stable but close — exactly where the zig-zag is most visible).

**Plain GD.** Each axis: $x_{t+1}=(1-0.18\cdot10)x_t = (1-1.8)x_t = -0.8\,x_t$; $y_{t+1}=(1-0.18)y_t=0.82\,y_t$.

| step | $x$ (steep) | $y$ (shallow) |
|---|---|---|
| 0 | $1.000$ | $1.000$ |
| 1 | $-0.800$ | $0.820$ |
| 2 | $0.640$ | $0.672$ |
| 3 | $-0.512$ | $0.551$ |

The steep coordinate **flips sign and shrinks slowly** ($|{-0.8}|=0.8$ per step — the zig-zag), while the shallow coordinate **crawls** ($0.82$ per step). Classic ravine: lots of motion across, little progress along.

**Momentum** ($\beta=0.9$, $v_0=0$, same $\eta$). Steep axis first:

- $v_1 = 0.9\cdot0 + 10\cdot1 = 10$, so $x_1 = 1 - 0.18\cdot10 = -0.8$ (same first step).
- But now $g(x_1)=10\cdot(-0.8)=-8$, so $v_2=0.9\cdot10 + (-8)=1.0$ and $x_2 = -0.8 - 0.18\cdot1.0 = -0.98$.
- The velocity has *absorbed* the sign flip (it was $+10$, the new gradient is $-8$, they partly cancel), so the steep oscillation is **damped** instead of cleanly reversing.

Meanwhile on the shallow axis the velocity *accumulates*:

- $v^y_1=1,\ v^y_2=0.9\cdot1+0.82=1.72,\ v^y_3=0.9\cdot1.72+0.51\approx2.06$.
- It grows well past the raw gradient (toward a steady-state $\sim g/(1-\beta)$), so $y$ descends **faster and faster** down the valley.
- Momentum's path is smoother *and* quicker, exactly as the algebra predicted.

---

## References

Shared with the topic's companion file — see [Optimizers — references and further reading](/ai-ml/ai-ml-learning-resources/deep-learning/optimization-and-training/optimizers/optimizers#references-further-reading).
