"""Generate the quantitative figures for the Synthetic Data Generation workflow note.

Run inside ml-py312:
    source ~/.uv/envs/ml-py312/bin/activate
    python gen_plots.py

Produces (in this folder):
    syndata_funnel.png        - the generate -> filter -> dedup yield funnel (counts dropping)
    syndata_diversity.png     - n-gram diversity before vs after the dedup/filter pass
    syndata_quality_quantity.png - downstream accuracy vs dataset size, by data quality
    syndata_collapse.png      - model collapse: diversity decaying over recursive generations
    syndata_method_cost.png   - cost vs capability for the four generation methods
"""
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


def funnel():
    """The yield funnel: raw generations shrink as each quality gate removes examples."""
    stages = ["Generated\n(raw)", "After\nformat filter", "After quality\nfilter", "After\ndedup", "Final\ndataset"]
    counts = [1000, 870, 690, 540, 540]
    colors = [BLUE, NAVY, AMBER, PURPLE, GREEN]

    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    bars = ax.bar(stages, counts, color=colors, width=0.62)
    for b, c in zip(bars, counts):
        ax.text(b.get_x() + b.get_width() / 2, c + 14, f"{c}", ha="center",
                va="bottom", fontsize=10, fontweight="bold")
    # annotate the drops between stages
    for i in range(1, len(counts)):
        drop = counts[i - 1] - counts[i]
        if drop > 0:
            ax.annotate(f"-{drop}", xy=(i - 0.5, (counts[i - 1] + counts[i]) / 2),
                        color=RED, fontsize=9.5, ha="center", fontweight="bold")
    ax.set_ylabel("examples surviving")
    ax.set_title("The generation funnel: 1000 raw samples -> 540 clean examples (54% yield)")
    ax.set_ylim(0, 1120)
    fig.tight_layout()
    fig.savefig("syndata_funnel.png", bbox_inches="tight")
    plt.close(fig)


def diversity():
    """Distinct-n diversity before vs after the dedup/filter pass, for two n-gram sizes."""
    labels = ["distinct-1\n(unigrams)", "distinct-2\n(bigrams)"]
    before = [0.18, 0.41]
    after = [0.34, 0.67]
    x = np.arange(len(labels))
    w = 0.36

    fig, ax = plt.subplots(figsize=(7.0, 4.4))
    b1 = ax.bar(x - w / 2, before, w, color=RED, label="raw generations (repetitive)")
    b2 = ax.bar(x + w / 2, after, w, color=GREEN, label="after dedup + filter")
    for bars in (b1, b2):
        for b in bars:
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.012,
                    f"{b.get_height():.2f}", ha="center", va="bottom", fontsize=10)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("distinct-n  (unique n-grams / total)")
    ax.set_title("Diversity rises after filtering: fewer near-duplicate samples")
    ax.set_ylim(0, 0.82)
    ax.legend(loc="upper left", frameon=False)
    fig.tight_layout()
    fig.savefig("syndata_diversity.png", bbox_inches="tight")
    plt.close(fig)


def quality_quantity():
    """Downstream accuracy vs dataset size, for clean-synthetic vs noisy-synthetic data."""
    n = np.array([100, 250, 500, 1000, 2000, 4000, 8000])
    # clean data: rises and saturates high. noisy data: rises then plateaus low (label noise caps it).
    clean = 0.92 - 0.42 * np.exp(-n / 900.0)
    noisy = 0.74 - 0.30 * np.exp(-n / 700.0)

    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    ax.plot(n, clean, "-o", color=GREEN, lw=2.6, ms=5, label="clean synthetic (filtered)")
    ax.plot(n, noisy, "-o", color=RED, lw=2.6, ms=5, label="noisy synthetic (unfiltered)")
    ax.axvline(500, color=SLATE, ls="--", lw=1.2, alpha=0.8)
    ax.annotate("a few hundred CLEAN examples\nbeat thousands of noisy ones",
                xy=(500, clean[2]), xytext=(1500, 0.62), color=BLUE, fontsize=10,
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.3))
    ax.set_xlabel("number of synthetic training examples")
    ax.set_ylabel("downstream task accuracy")
    ax.set_title("Quality beats quantity: noisy data plateaus, clean data climbs")
    ax.set_xscale("log")
    ax.set_ylim(0.4, 0.95)
    ax.legend(loc="lower right", frameon=False)
    fig.tight_layout()
    fig.savefig("syndata_quality_quantity.png", bbox_inches="tight")
    plt.close(fig)


def collapse():
    """Model collapse: train on your own output recursively and diversity decays each round."""
    gens = np.arange(0, 8)
    # diversity decays geometrically when each generation trains on the previous one's output.
    healthy = 0.67 * np.ones_like(gens, dtype=float)
    collapsing = 0.67 * (0.78 ** gens)

    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    ax.plot(gens, healthy, "-", color=GREEN, lw=2.6,
            label="anchored to real data (stable)")
    ax.plot(gens, collapsing, "-o", color=RED, lw=2.6, ms=5,
            label="recursive synthetic-only (collapsing)")
    ax.fill_between(gens, collapsing, healthy, color=RED, alpha=0.06)
    ax.annotate("each round trains on the\nlast round's output ->\ndiversity decays",
                xy=(5, collapsing[5]), xytext=(2.4, 0.22), color=RED, fontsize=9.5,
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.3))
    ax.set_xlabel("generation (round of recursive training)")
    ax.set_ylabel("output diversity (distinct-2)")
    ax.set_title("Model collapse: synthetic-only loops lose diversity each round")
    ax.set_ylim(0, 0.78)
    ax.legend(loc="upper right", frameon=False)
    fig.tight_layout()
    fig.savefig("syndata_collapse.png", bbox_inches="tight")
    plt.close(fig)


def method_cost():
    """Cost (LLM calls / $) vs capability for the four generation methods."""
    methods = ["Simple\nprompting", "Self-\nInstruct", "Evol-\nInstruct", "Distill from\nstronger model"]
    cost = [1.0, 2.5, 4.0, 6.0]          # relative generation cost (LLM calls)
    capability = [0.45, 0.70, 0.85, 0.92]  # relative downstream quality reached
    colors = [BLUE, NAVY, AMBER, GREEN]

    fig, ax = plt.subplots(figsize=(7.4, 4.6))
    ax.scatter(cost, capability, s=180, c=colors, zorder=5)
    for m, x, y in zip(methods, cost, capability):
        ax.annotate(m, xy=(x, y), xytext=(x + 0.12, y - 0.045), fontsize=10)
    ax.plot(cost, capability, color=SLATE, ls="--", lw=1.4, alpha=0.7, zorder=1)
    ax.set_xlabel("relative generation cost  (LLM calls / $)")
    ax.set_ylabel("relative downstream capability")
    ax.set_title("Generation methods: more cost buys more diversity/difficulty")
    ax.set_xlim(0.3, 7.2)
    ax.set_ylim(0.35, 1.0)
    fig.tight_layout()
    fig.savefig("syndata_method_cost.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    funnel()
    diversity()
    quality_quantity()
    collapse()
    method_cost()
    print("wrote: syndata_funnel.png, syndata_diversity.png, syndata_quality_quantity.png, "
          "syndata_collapse.png, syndata_method_cost.png")
