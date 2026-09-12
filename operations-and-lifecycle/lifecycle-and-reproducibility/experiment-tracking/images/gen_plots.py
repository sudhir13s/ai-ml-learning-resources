"""Generate the quantitative figures for the Experiment Tracking & Reproducibility workflow note.

Run inside ml-py312:
    source ~/.uv/envs/ml-py312/bin/activate
    python gen_plots.py

Produces (in this folder):
    sweep_grid_vs_random.png - why random search beats grid for the same budget
    sweep_convergence.png      - best-so-far loss vs trials for grid / random / Bayesian
    runs_over_sweep.png        - per-run val loss + the monotone best-so-far line
"""
import hashlib
import json
import math
import random

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Muted palette aligned with the repo's diagram colors.
BLUE = "#3A6B96"
PURPLE = "#5D4A8A"
GREEN = "#2E7A5A"
RED = "#8B3B4A"
AMBER = "#7A6528"
SLATE = "#4A5B6E"
NAVY = "#2A5B80"

plt.rcParams.update({
    "figure.dpi": 130,
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "axes.grid": True,
    "grid.alpha": 0.25,
    "axes.spines.top": False,
    "axes.spines.right": False,
})


def grid_vs_random():
    """Bergstra & Bengio (2012): for the same budget, random covers the important
    hyperparameter at more distinct values than grid. Two panels, 9 trials each, with
    marginal-effect curves showing one parameter matters (sharp peak) and one doesn't (flat).
    """
    fig, (axg, axr) = plt.subplots(1, 2, figsize=(9.8, 4.9), sharey=True)
    opt_x = 0.62  # true optimum of the important parameter

    # --- left: grid ---
    gx = np.array([0.2, 0.5, 0.8])
    gy = np.array([0.2, 0.5, 0.8])
    GX, GY = np.meshgrid(gx, gy)
    axg.scatter(GX.ravel(), GY.ravel(), s=70, color=AMBER, zorder=4,
                edgecolor="white", linewidth=0.8)
    axg.axvline(opt_x, color=SLATE, ls="--", lw=1.4, alpha=0.85)
    closest = gx[np.argmin(np.abs(gx - opt_x))]
    axg.scatter([closest], [gy[np.argmin(np.abs(gx - opt_x))]], s=130,
                facecolors="none", edgecolors=RED, linewidth=2.2, zorder=5)
    axg.set_title("Grid: important param at only 3 values", fontsize=11.5, pad=8)
    axg.set_xlabel("important hyperparameter (sharp effect)")
    axg.set_ylabel("unimportant hyperparameter (flat effect)")
    axg.set_xlim(0, 1)
    axg.set_ylim(0, 1.18)

    # --- right: random ---
    rng = np.random.default_rng(0)
    rx = rng.uniform(0.04, 0.96, 9)
    ry = rng.uniform(0.04, 0.96, 9)
    axr.scatter(rx, ry, s=70, color=GREEN, zorder=4, edgecolor="white", linewidth=0.8)
    axr.axvline(opt_x, color=SLATE, ls="--", lw=1.4, alpha=0.85)
    near = int(np.argmin(np.abs(rx - opt_x)))
    axr.scatter([rx[near]], [ry[near]], s=130, facecolors="none", edgecolors=GREEN,
                linewidth=2.2, zorder=5)
    axr.annotate("lands near\nthe optimum", xy=(rx[near], ry[near]),
                 xytext=(rx[near] + 0.16, ry[near] - 0.04), color=GREEN, fontsize=9.5,
                 ha="left", arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.3))
    axr.set_title("Random: important param at 9 distinct values", fontsize=11.5, pad=8)
    axr.set_xlabel("important hyperparameter (sharp effect)")
    axr.set_xlim(0, 1)
    axr.set_ylim(0, 1.18)

    # marginal-effect curves along the top of each panel (purple sharp peak = matters,
    # grey flat = doesn't), drawn in the headroom above the trial points.
    xs = np.linspace(0, 1, 200)
    peak = np.exp(-((xs - opt_x) ** 2) / (2 * 0.09 ** 2))
    for ax in (axg, axr):
        ax.plot(xs, 1.00 + 0.13 * peak, color=PURPLE, lw=1.8, alpha=0.9)
        ax.plot(xs, np.full_like(xs, 1.02), color="#9aa3ad", lw=1.6, alpha=0.9)
    axg.text(0.02, 1.10, "purple = effect on loss (sharp peak vs flat)",
             color=PURPLE, fontsize=8.5)

    fig.suptitle("Same 9 trials: random probes the parameter that matters far more densely",
                 fontsize=13.5, fontweight="bold", y=0.99)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig("sweep_grid_vs_random.png", bbox_inches="tight")
    plt.close(fig)


def convergence():
    """Best-so-far loss vs number of trials for grid, random, and Bayesian search.

    Same search space; Bayesian reaches the target in the fewest trials, random next,
    grid slowest. Models each as the running min of a strategy-specific trial stream.
    """
    n = 40
    floor = 0.40
    t = np.arange(1, n + 1)

    # Construct the three best-so-far curves directly (smooth, monotone, illustrative)
    # so the ordering Bayesian < random < grid is unambiguous.
    grid_best = floor + 0.04 + 2.9 * np.exp(-(t - 1) / 24.0)          # slow exponential descent
    random_best = floor + 0.18 + 2.9 * np.exp(-(t - 1) / 4.2)         # faster; plateaus above target later
    bayes_best = floor + 0.02 + 2.9 * np.exp(-(t - 1) / 2.6)          # fastest; settles lowest

    def best_so_far(x):
        return np.minimum.accumulate(x)

    fig, ax = plt.subplots(figsize=(7.4, 4.6))
    ax.plot(t, grid_best, color=AMBER, lw=2.6, label="grid search")
    ax.plot(t, random_best, color=GREEN, lw=2.8, label="random search")
    ax.plot(t, bayes_best, color=PURPLE, lw=3.0, label="Bayesian search")

    target = 0.85
    ax.axhline(target, color=SLATE, ls="--", lw=1.2, alpha=0.8)
    ax.text(n * 0.70, target + 0.12, "target loss", color=SLATE, fontsize=9.5)

    def first_cross(b):
        idx = np.argmax(b <= target)
        return idx + 1 if b[idx] <= target else None

    bx = first_cross(bayes_best)
    rx = first_cross(random_best)
    if bx:
        ax.scatter([bx], [target], color=PURPLE, zorder=5, s=60)
        ax.annotate(f"Bayesian hits target\n~trial {bx}", xy=(bx, target),
                    xytext=(bx + 1.5, target + 0.85), color=PURPLE, fontsize=9.5,
                    arrowprops=dict(arrowstyle="->", color=PURPLE, lw=1.2))
    if rx:
        ax.scatter([rx], [target], color=GREEN, zorder=5, s=60)
        ax.annotate(f"random ~trial {rx}", xy=(rx, target),
                    xytext=(rx + 1.5, target + 1.7), color=GREEN, fontsize=9.5,
                    arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2))

    ax.set_xlabel("number of trials evaluated")
    ax.set_ylabel("best validation loss so far")
    ax.set_title("Trials to a good config: Bayesian < random < grid")
    ax.legend(loc="upper right", frameon=False)
    ax.set_xlim(1, n)
    fig.tight_layout()
    fig.savefig("sweep_convergence.png", bbox_inches="tight")
    plt.close(fig)


def runs_over_sweep():
    """Reproduce the exact sweep from the Code Example and plot per-run val loss plus the
    monotone best-so-far line. Uses the SAME objective + sampler + seed as the runnable code,
    so the figure matches the numbers printed in the note (best ~0.6258)."""
    def train_and_eval(lr, weight_decay, hidden, seed):
        r = random.Random(seed)
        loss = (math.log10(lr) + 2.0) ** 2
        loss += (math.log10(weight_decay) + 4.0) ** 2 * 0.20
        loss += ((hidden - 128) / 128) ** 2 * 0.50
        loss += 0.40
        loss += r.uniform(-0.02, 0.02)
        return round(loss, 4)

    def sample_config(r):
        return {
            "lr": 10 ** r.uniform(-4, -1),
            "weight_decay": 10 ** r.uniform(-6, -2),
            "hidden": r.choice([64, 128, 256, 512]),
        }

    r = random.Random(0)
    losses = []
    for _ in range(25):
        cfg = sample_config(r)
        losses.append(train_and_eval(cfg["lr"], cfg["weight_decay"], cfg["hidden"], seed=42))
    losses = np.array(losses)
    best = np.minimum.accumulate(losses)
    x = np.arange(1, len(losses) + 1)
    best_idx = int(np.argmin(losses))

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(x, losses, color=BLUE, lw=1.8, marker="o", ms=4, alpha=0.85,
            label="each run's val loss")
    ax.step(x, best, color=GREEN, lw=2.8, where="post", label="best so far (only steps down)")
    ax.scatter([best_idx + 1], [losses[best_idx]], color=AMBER, zorder=6, s=90,
               edgecolor="white", linewidth=0.8)
    ax.annotate(f"best run: val_loss={losses[best_idx]:.3f}",
                xy=(best_idx + 1, losses[best_idx]),
                xytext=(best_idx + 2.5, losses[best_idx] + 2.2), color=AMBER, fontsize=9.5,
                arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.3))
    ax.set_xlabel("run number")
    ax.set_ylabel("validation loss")
    ax.set_title("A logged sweep: noisy trials, but the best result is never lost")
    ax.legend(loc="upper right", frameon=False)
    ax.set_xlim(1, len(losses))
    fig.tight_layout()
    fig.savefig("runs_over_sweep.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    grid_vs_random()
    convergence()
    runs_over_sweep()
    print("wrote sweep_grid_vs_random.png, sweep_convergence.png, runs_over_sweep.png")
