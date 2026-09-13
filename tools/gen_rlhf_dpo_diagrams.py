"""RLHF & DPO concept-page diagrams (muted palette, parallel matplotlib scale).

Figures for model-adaptation/preference-and-alignment-training/preference-and-alignment-training.md:
  1. rlhf_bradley_terry.png  -- the Bradley-Terry reward-model loss: P(chosen > rejected)
     = sigma(reward gap), and the per-pair loss -log sigma(gap). Shows the coin-flip at gap 0
     and the saturating confidence as the gap grows.
  2. rlhf_overoptimization.png -- reward over-optimization (Goodhart): as the policy drifts
     (KL) from the reference, the proxy reward keeps rising but the true/gold reward peaks and
     falls. Why RLHF needs a KL leash.
  3. dpo_margin.png -- DPO directly optimizes the preference: as the implicit-reward margin
     grows, the DPO loss falls and P(chosen > rejected) = sigmoid(margin) rises.
  4. dpo_update.png -- a measured DPO run on a toy 2-token policy: the chosen response's
     log-prob rises and the rejected response's falls, and the implicit-reward margin grows,
     step by step, exactly as the derivation promises.

Run:
  /Users/sudhirsingh/.uv/envs/ml-py312/bin/python3 tools/gen_rlhf_dpo_diagrams.py
"""
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "..", "model-adaptation/preference-and-alignment-training", "images")
OUT = os.path.abspath(OUT)
os.makedirs(OUT, exist_ok=True)

BLUE, PURPLE, GREEN, RED, SLATE, AMBER, NAVY = (
    "#3A6B96", "#5D4A8A", "#2E7A5A", "#8B3B4A", "#4A5B6E", "#7A6528", "#2A5B80")
plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans"})


def _despine(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


def bradley_terry():
    """The reward-model objective: a sigmoid of the reward gap, plus its per-pair loss."""
    gap = np.linspace(-6, 6, 400)
    prob = 1 / (1 + np.exp(-gap))           # P(chosen > rejected) = sigma(gap)
    loss = np.log1p(np.exp(-gap))           # -log sigma(gap), numerically safe
    fig, ax1 = plt.subplots(figsize=(8.6, 5.0))
    ax1.plot(gap, prob, color=BLUE, lw=2.8, label="P(chosen ≻ rejected) = σ(gap)")
    ax1.set_xlabel("reward gap  r(chosen) − r(rejected)")
    ax1.set_ylabel("P(chosen ≻ rejected)", color=BLUE)
    ax1.tick_params(axis="y", labelcolor=BLUE); _despine(ax1)
    ax1.set_ylim(0, 1.02)
    # coin flip at gap 0
    ax1.scatter([0], [0.5], color=RED, s=70, zorder=5, edgecolor="white")
    ax1.annotate("gap 0 → 0.5\n(coin flip, no opinion)", (0, 0.5),
                 textcoords="offset points", xytext=(12, -34), fontsize=9, color=RED,
                 arrowprops=dict(arrowstyle="->", color=RED))
    # confident-correct point
    ax1.scatter([3], [1/(1+np.exp(-3))], color=GREEN, s=70, zorder=5, edgecolor="white")
    ax1.annotate("gap +3 → 0.95\n(confident, low loss)", (3, 1/(1+np.exp(-3))),
                 textcoords="offset points", xytext=(-150, -2), fontsize=9, color=GREEN,
                 arrowprops=dict(arrowstyle="->", color=GREEN))
    ax2 = ax1.twinx()
    ax2.plot(gap, loss, color=PURPLE, lw=2.6, ls="--", label="per-pair loss = −log σ(gap)")
    ax2.set_ylabel("Bradley-Terry loss  −log σ(gap)", color=PURPLE)
    ax2.tick_params(axis="y", labelcolor=PURPLE)
    for s in ("top",): ax2.spines[s].set_visible(False)
    ax1.axvline(0, color=SLATE, ls=":", lw=1.0)
    ax1.set_title("The Bradley-Terry reward model: a sigmoid of the reward gap",
                  fontsize=13.5, fontweight="bold")
    l1, lab1 = ax1.get_legend_handles_labels(); l2, lab2 = ax2.get_legend_handles_labels()
    ax1.legend(l1 + l2, lab1 + lab2, frameon=False, fontsize=9.5, loc="center left")
    fig.tight_layout(); fig.savefig(f"{OUT}/rlhf_bradley_terry.png", dpi=150, bbox_inches="tight")
    plt.close(fig); print("wrote rlhf_bradley_terry.png")


def overoptimization():
    kl = np.linspace(0, 10, 200)
    proxy = 3.4 * (1 - np.exp(-0.45 * kl))                 # RM score: keeps rising, saturating
    gold = 3.0 * (1 - np.exp(-0.6 * kl)) - 0.16 * kl       # true quality: rises then falls
    peak = int(np.argmax(gold))
    fig, ax = plt.subplots(figsize=(8.6, 5.0))
    ax.plot(kl, proxy, color=RED, lw=2.6, label="Proxy reward (what the reward model says)")
    ax.plot(kl, gold, color=GREEN, lw=2.6, label="True quality (actual human preference)")
    ax.axvline(kl[peak], color=SLATE, ls="--", lw=1.6)
    ax.scatter([kl[peak]], [gold[peak]], color=AMBER, s=80, zorder=5, edgecolor="white")
    ax.annotate("sweet spot:\nstop here (KL leash)", (kl[peak], gold[peak]),
                textcoords="offset points", xytext=(8, -46), fontsize=9.5, fontweight="bold", color="#222",
                arrowprops=dict(arrowstyle="->", color=SLATE))
    ax.annotate("reward hacking:\nproxy ↑ but quality ↓", (8.2, proxy[160]),
                textcoords="offset points", xytext=(-150, -8), fontsize=9.5, color=RED, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=RED))
    ax.fill_between(kl[peak:], gold[peak:], proxy[peak:], color=RED, alpha=0.10)
    ax.set_xlabel("KL divergence from the reference model  (how far the policy drifts)")
    ax.set_ylabel("reward")
    ax.set_title("Reward over-optimization: why RLHF needs a KL leash", fontsize=13.5, fontweight="bold")
    ax.legend(frameon=False, fontsize=9.5, loc="lower right"); _despine(ax); ax.set_ylim(0, 3.6)
    fig.tight_layout(); fig.savefig(f"{OUT}/rlhf_overoptimization.png", dpi=150, bbox_inches="tight")
    plt.close(fig); print("wrote rlhf_overoptimization.png")


def dpo_margin():
    m = np.linspace(-4, 4, 200)
    loss = np.log1p(np.exp(-m))           # -log sigmoid(m), numerically safe
    win = 1 / (1 + np.exp(-m))            # sigmoid(m) = P(chosen > rejected)
    fig, ax1 = plt.subplots(figsize=(8.6, 5.0))
    ax1.plot(m, loss, color=PURPLE, lw=2.8, label="DPO loss = −log σ(margin)")
    ax1.set_xlabel("implicit-reward margin  β·[ (logπ/π_ref)$_{chosen}$ − (logπ/π_ref)$_{rejected}$ ]")
    ax1.set_ylabel("DPO loss", color=PURPLE)
    ax1.tick_params(axis="y", labelcolor=PURPLE); _despine(ax1)
    ax2 = ax1.twinx()
    ax2.plot(m, win, color=GREEN, lw=2.8, ls="--", label="P(chosen ≻ rejected) = σ(margin)")
    ax2.set_ylabel("P(chosen ≻ rejected)", color=GREEN)
    ax2.tick_params(axis="y", labelcolor=GREEN)
    for s in ("top",): ax2.spines[s].set_visible(False)
    ax1.axvline(0, color=SLATE, ls=":", lw=1.2)
    ax1.text(0.1, 2.3, "init: policy = reference\nmargin 0, loss = log 2", fontsize=9, color=SLATE)
    ax1.set_title("DPO directly raises the preferred response's probability", fontsize=13.5, fontweight="bold")
    l1, lab1 = ax1.get_legend_handles_labels(); l2, lab2 = ax2.get_legend_handles_labels()
    ax1.legend(l1 + l2, lab1 + lab2, frameon=False, fontsize=9.5, loc="upper center")
    fig.tight_layout(); fig.savefig(f"{OUT}/dpo_margin.png", dpi=150, bbox_inches="tight")
    plt.close(fig); print("wrote dpo_margin.png")


def dpo_update():
    """A MEASURED toy DPO run: optimize two scalar log-probs (chosen, rejected) under the DPO
    loss with a frozen reference, and record how they move + the implicit-reward margin grows."""
    import torch
    import torch.nn.functional as F
    torch.manual_seed(0)
    beta = 0.1
    ref_w = ref_l = torch.tensor(-5.0)           # frozen reference log-probs
    pi_w = torch.tensor(-5.0, requires_grad=True)  # policy logprob of chosen (starts == ref)
    pi_l = torch.tensor(-5.0, requires_grad=True)  # policy logprob of rejected (starts == ref)
    opt = torch.optim.SGD([pi_w, pi_l], lr=2.0)
    steps, lp_w, lp_l, margins, losses = [], [], [], [], []
    for t in range(0, 121):
        pi_logr = pi_w - pi_l
        ref_logr = ref_w - ref_l
        margin = beta * (pi_logr - ref_logr)
        loss = -F.logsigmoid(margin)
        if t % 1 == 0:
            steps.append(t); lp_w.append(pi_w.item()); lp_l.append(pi_l.item())
            margins.append(margin.item()); losses.append(loss.item())
        opt.zero_grad(); loss.backward(); opt.step()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.6, 4.8))
    # left: log-probs of chosen vs rejected over training
    ax1.plot(steps, lp_w, color=GREEN, lw=2.6, label="log π(chosen)  — rises")
    ax1.plot(steps, lp_l, color=RED, lw=2.6, label="log π(rejected) — falls")
    ax1.axhline(-5.0, color=SLATE, ls=":", lw=1.2)
    ax1.annotate("both start at the\nreference (−5.0)", (0, -5.0),
                 textcoords="offset points", xytext=(40, 6), fontsize=9, color=SLATE)
    ax1.set_xlabel("DPO training step")
    ax1.set_ylabel("log-probability")
    ax1.set_title("DPO splits chosen from rejected", fontsize=12.5, fontweight="bold")
    ax1.legend(frameon=False, fontsize=9.5, loc="center right"); _despine(ax1)
    # right: implicit-reward margin grows, loss falls
    ax2.plot(steps, margins, color=PURPLE, lw=2.8, label="implicit-reward margin  β·Δlog(π/π_ref)")
    ax2.set_xlabel("DPO training step")
    ax2.set_ylabel("margin", color=PURPLE)
    ax2.tick_params(axis="y", labelcolor=PURPLE); _despine(ax2)
    ax2b = ax2.twinx()
    ax2b.plot(steps, losses, color=AMBER, lw=2.4, ls="--", label="DPO loss = −log σ(margin)")
    ax2b.set_ylabel("DPO loss", color=AMBER)
    ax2b.tick_params(axis="y", labelcolor=AMBER)
    for s in ("top",): ax2b.spines[s].set_visible(False)
    ax2.set_title("Margin grows, loss falls", fontsize=12.5, fontweight="bold")
    l1, lab1 = ax2.get_legend_handles_labels(); l2, lab2 = ax2b.get_legend_handles_labels()
    ax2.legend(l1 + l2, lab1 + lab2, frameon=False, fontsize=8.8, loc="center right")
    fig.suptitle("A measured DPO update: chosen up, rejected down, margin grows",
                 fontsize=13.5, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(f"{OUT}/dpo_update.png", dpi=150, bbox_inches="tight")
    plt.close(fig); print("wrote dpo_update.png")


def ppo_clip():
    """PPO's clipped surrogate objective as a function of the probability ratio (A > 0 case).

    The ratio r = pi_new(a|s) / pi_old(a|s) says how much more likely the new policy makes an
    action. PPO multiplies it by the advantage A but clips it to [1-eps, 1+eps] and takes the
    pessimistic min, so past 1+eps the objective is flat and there is no gradient to over-shoot.
    """
    eps = 0.2
    ratio = np.linspace(0.0, 2.0, 400)
    advantage = 1.0
    unclipped = ratio * advantage
    surrogate = np.minimum(unclipped, np.clip(ratio, 1 - eps, 1 + eps) * advantage)
    fig, ax = plt.subplots(figsize=(8.6, 5.0))
    ax.plot(ratio, unclipped, color=SLATE, lw=1.8, ls=":", label="unclipped  ratio · A")
    ax.plot(ratio, surrogate, color=GREEN, lw=3, label="PPO objective  min(ratio·A, clip(ratio, 1±ε)·A)")
    ax.axvline(1.0, color=SLATE, ls="--", lw=1.0, alpha=0.7)
    ax.axvspan(1 - eps, 1 + eps, color=GREEN, alpha=0.07)
    ax.text(1.0, 0.18, "trust region\n[1−ε, 1+ε]", color=GREEN, fontsize=9.5, ha="center")
    ax.scatter([1 + eps], [(1 + eps) * advantage], color=RED, zorder=5, s=60, edgecolor="white")
    ax.annotate("past 1+ε: objective is flat,\nno reward for over-shooting",
                xy=(1 + eps, (1 + eps) * advantage), xytext=(1.32, 0.62), color=RED, fontsize=9.5,
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.3))
    ax.set_xlabel("probability ratio  π_new(a|s) / π_old(a|s)")
    ax.set_ylabel("surrogate objective  (advantage A > 0)")
    ax.set_title("PPO clipping: a per-step trust region on the policy update",
                 fontsize=13.5, fontweight="bold")
    ax.legend(loc="upper left", frameon=False, fontsize=9.5)
    ax.set_ylim(-0.05, 2.05); _despine(ax)
    fig.tight_layout(); fig.savefig(f"{OUT}/rlhf_ppo_clip.png", dpi=150, bbox_inches="tight")
    plt.close(fig); print("wrote rlhf_ppo_clip.png")


def beta_sweep():
    """Illustrative: where a sweep of KL strengths beta lands on a schematic true-quality frontier.

    Larger beta -> tighter leash -> smaller equilibrium KL drift. The frontier rises and then
    falls (over-optimization); the curve is hand-chosen for shape, not measured.
    """
    betas = np.array([0.5, 0.2, 0.12, 0.08, 0.067])
    kl_at = 1.2 / betas                                            # small beta -> large drift
    frontier_fn = lambda kl: 7.5 * np.tanh(kl / 6.0) - 0.018 * kl ** 2
    kl = np.linspace(0, 30, 400)
    fig, ax = plt.subplots(figsize=(8.6, 5.0))
    ax.plot(kl, frontier_fn(kl), color=SLATE, lw=1.6, ls=":", alpha=0.8, label="true-quality frontier (schematic)")
    ax.plot(kl_at, frontier_fn(kl_at), color=PURPLE, lw=2.4, marker="o", ms=7, label="where each β lands")
    for b, x, y in zip(betas, kl_at, frontier_fn(kl_at)):
        ax.annotate(f"β={b}", xy=(x, y), xytext=(x + 0.5, y - 1.1), color=PURPLE, fontsize=9)
    ax.annotate("large β:\ntight leash,\nbarely aligned", xy=(kl_at[0], frontier_fn(kl_at[0])),
                xytext=(0.5, 5.2), color=BLUE, fontsize=9.5,
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2))
    ax.annotate("small β:\nlong leash,\nover-optimizing", xy=(kl_at[-1], frontier_fn(kl_at[-1])),
                xytext=(kl_at[-1] + 1.2, frontier_fn(kl_at[-1]) + 2.6), color=RED, fontsize=9.5,
                ha="center", arrowprops=dict(arrowstyle="->", color=RED, lw=1.2))
    ax.set_xlabel("resulting KL drift  KL(π_θ ‖ π_ref)")
    ax.set_ylabel("true quality reached")
    ax.set_title("Tuning β: the knob that sets how far the policy may drift",
                 fontsize=13.5, fontweight="bold")
    ax.legend(loc="upper right", frameon=False, fontsize=9.5)
    ax.set_xlim(-1, 26); ax.set_ylim(-1, 9); _despine(ax)
    fig.tight_layout(); fig.savefig(f"{OUT}/rlhf_beta_sweep.png", dpi=150, bbox_inches="tight")
    plt.close(fig); print("wrote rlhf_beta_sweep.png")


if __name__ == "__main__":
    bradley_terry()
    overoptimization()
    dpo_margin()
    dpo_update()
    ppo_clip()
    beta_sweep()
    print("OUT:", OUT)
