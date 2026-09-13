"""Generate the extra quantitative figures for the Continuous-Training workflow note.

Run inside ml-py312:
    source ~/.uv/envs/ml-py312/bin/activate
    python make_extra_charts.py

Produces (in images/):
    ct_psi_drift.png            - PSI bar chart: reference vs drifted live histogram, PSI score
    ct_full_vs_incremental.png  - cost-vs-freshness trade-off of full vs incremental retrain
    ct_replay_forgetting.png    - replay buffer vs naive retrain on a frozen regression set
    ct_cadence_cost.png         - retrain cadence vs compute cost vs staleness window
"""
import os
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "images")
os.makedirs(IMG, exist_ok=True)

# Muted palette aligned with the repo's diagram colors.
BLUE = "#3A6B96"
NAVY = "#2A5B80"
PURPLE = "#5D4A8A"
GREEN = "#2E7A5A"
RED = "#8B3B4A"
AMBER = "#7A6528"
WARN = "#7D5A2C"
SLATE = "#4A5B6E"

plt.rcParams.update({
    "figure.dpi": 130,
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.titlesize": 14,
    "axes.titleweight": "bold",
    "axes.labelsize": 11,
    "axes.grid": True,
    "grid.alpha": 0.25,
    "axes.spines.top": False,
    "axes.spines.right": False,
})


def psi_drift():
    """PSI worked example: reference vs live bin proportions and the per-bin PSI terms.

    Uses the exact numbers walked through in the doc's runnable PSI demo so the
    picture matches the printed output.
    """
    bins = ["b0", "b1", "b2", "b3", "b4"]
    ref = np.array([0.20, 0.20, 0.20, 0.20, 0.20])
    live = np.array([0.05, 0.10, 0.20, 0.30, 0.35])
    terms = (live - ref) * np.log(live / ref)
    psi = terms.sum()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.2, 4.4))

    x = np.arange(len(bins))
    w = 0.38
    ax1.bar(x - w / 2, ref, w, color=SLATE, label="reference (training)")
    ax1.bar(x + w / 2, live, w, color=RED, label="live (this week)")
    ax1.set_xticks(x)
    ax1.set_xticklabels(bins)
    ax1.set_ylabel("proportion of traffic")
    ax1.set_title("Feature histogram drifted right")
    ax1.legend(loc="upper left", frameon=False, fontsize=9)
    ax1.set_ylim(0, 0.42)

    colors = [GREEN if t < 0.02 else (WARN if t < 0.06 else RED) for t in terms]
    ax2.bar(x, terms, color=colors)
    ax2.set_xticks(x)
    ax2.set_xticklabels(bins)
    ax2.set_ylabel("per-bin PSI contribution")
    ax2.set_title(f"PSI = sum of bin terms = {psi:.3f}  (> 0.2: retrain)")
    ax2.axhline(0, color=SLATE, lw=1.0)
    fig.tight_layout()
    fig.savefig(os.path.join(IMG, "ct_psi_drift.png"), bbox_inches="tight")
    plt.close(fig)


def full_vs_incremental():
    """Full retrain vs incremental update: cost vs robustness to large drift."""
    fig, ax = plt.subplots(figsize=(8.6, 4.6))
    drift = np.linspace(0, 1, 200)             # 0 = no drift, 1 = regime change
    # Incremental: cheap, tracks small drift, but degrades under big/concept drift.
    incr_quality = 0.95 - 0.55 * drift ** 1.8
    # Full retrain from scratch on a wide window: costlier, robust to big drift.
    full_quality = 0.93 - 0.10 * drift
    ax.plot(drift, full_quality, color=GREEN, lw=3, label="full retrain (wide window)")
    ax.plot(drift, incr_quality, color=BLUE, lw=3, ls="--",
            label="incremental update (fresh window only)")
    ax.axvspan(0, 0.35, color=BLUE, alpha=0.06)
    ax.axvspan(0.6, 1.0, color=GREEN, alpha=0.06)
    ax.text(0.17, 0.50, "small/steady drift:\nincremental is\ncheap & enough",
            color=BLUE, fontsize=9.5, ha="center")
    ax.text(0.8, 0.62, "concept drift / regime change:\nfull retrain wins",
            color=GREEN, fontsize=9.5, ha="center")
    ax.set_xlabel("magnitude of drift since last full retrain")
    ax.set_ylabel("post-retrain quality")
    ax.set_title("Full vs incremental retrain: pick by how far the world moved")
    ax.set_ylim(0.2, 1.0)
    ax.legend(loc="upper right", frameon=False)
    fig.tight_layout()
    fig.savefig(os.path.join(IMG, "ct_full_vs_incremental.png"), bbox_inches="tight")
    plt.close(fig)


def replay_forgetting():
    """Catastrophic forgetting: naive fresh-only retrain vs replay buffer, on two test sets."""
    labels = ["This week\n(new world)", "Last year\n(regression set)"]
    naive = [0.94, 0.41]      # great on new, forgot the old
    replay = [0.92, 0.88]     # slightly less on new, keeps the old
    x = np.arange(len(labels))
    w = 0.38
    fig, ax = plt.subplots(figsize=(8.0, 4.6))
    ax.bar(x - w / 2, naive, w, color=RED, label="naive retrain (fresh window only)")
    ax.bar(x + w / 2, replay, w, color=GREEN, label="replay buffer (mix old + new)")
    for xi, (a, b) in enumerate(zip(naive, replay)):
        ax.text(xi - w / 2, a + 0.015, f"{a:.2f}", ha="center", fontsize=9, color=RED)
        ax.text(xi + w / 2, b + 0.015, f"{b:.2f}", ha="center", fontsize=9, color=GREEN)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("accuracy")
    ax.set_ylim(0, 1.05)
    ax.set_title("Catastrophic forgetting: replay protects the frozen regression set")
    ax.legend(loc="lower center", frameon=False)
    fig.tight_layout()
    fig.savefig(os.path.join(IMG, "ct_replay_forgetting.png"), bbox_inches="tight")
    plt.close(fig)


def cadence_cost():
    """Retrain cadence trade-off: more frequent => higher compute, lower staleness window."""
    cadence_days = np.array([1, 3, 7, 14, 30, 90])
    compute_cost = 30.0 / cadence_days        # relative compute (more often = costlier)
    staleness = cadence_days / 2.0             # average data-staleness window (days)

    fig, ax1 = plt.subplots(figsize=(8.6, 4.6))
    ax1.plot(cadence_days, compute_cost, color=WARN, lw=3, marker="o", ms=6,
             label="compute cost (relative)")
    ax1.set_xlabel("retrain cadence (days between scheduled retrains)")
    ax1.set_ylabel("relative compute cost", color=WARN)
    ax1.tick_params(axis="y", labelcolor=WARN)
    ax1.set_xscale("log")
    ax1.set_xticks(cadence_days)
    ax1.set_xticklabels([str(d) for d in cadence_days])

    ax2 = ax1.twinx()
    ax2.plot(cadence_days, staleness, color=BLUE, lw=3, marker="s", ms=6,
             label="avg staleness window (days)")
    ax2.set_ylabel("avg data-staleness window (days)", color=BLUE)
    ax2.tick_params(axis="y", labelcolor=BLUE)
    ax2.grid(False)
    ax2.spines["top"].set_visible(False)

    ax1.axvspan(5, 9, color=GREEN, alpha=0.08)
    ax1.text(7, ax1.get_ylim()[1] * 0.78, "common\nsweet spot\n~weekly",
             color=GREEN, fontsize=9.5, ha="center")
    ax1.set_title("Retrain cadence: trading compute against how stale the model gets")
    fig.tight_layout()
    fig.savefig(os.path.join(IMG, "ct_cadence_cost.png"), bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    psi_drift()
    full_vs_incremental()
    replay_forgetting()
    cadence_cost()
    print("wrote ct_psi_drift.png, ct_full_vs_incremental.png, "
          "ct_replay_forgetting.png, ct_cadence_cost.png")
