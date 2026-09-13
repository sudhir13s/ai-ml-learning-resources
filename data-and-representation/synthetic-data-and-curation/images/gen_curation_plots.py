"""Figures for the web-corpus curation chapter of Synthetic Data and Data Curation.

    uv run --python 3.12 --with matplotlib --with numpy python gen_curation_plots.py

Writes next to this script:
    dedup_savings.png     - illustrative: deduplicated data reaches a target quality in fewer steps
    filter_yield.png      - illustrative FineWeb-style funnel: most of a raw crawl is filtered away
    minhash_accuracy.png  - simulated: MinHash estimates tighten as the signature lengthens
    lsh_s_curve.png       - exact: probability two documents become LSH candidates vs similarity
"""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402  (backend must be chosen first)

OUTPUT_DIR = Path(__file__).resolve().parent

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


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / name, bbox_inches="tight")
    plt.close(fig)


def filter_yield():
    """Documents surviving each curation gate (millions), FineWeb-style attrition."""
    stages = ["Raw\ncrawl", "Language\nID", "Quality\nheuristics", "PII /\nsafety",
              "Exact\ndedup", "Near-dup\n(MinHash)", "Final\ncorpus"]
    surviving = [1000, 620, 410, 395, 250, 190, 190]
    colors = [SLATE, BLUE, AMBER, NAVY, PURPLE, RED, GREEN]

    fig, ax = plt.subplots(figsize=(8.0, 4.6))
    bars = ax.bar(range(len(stages)), surviving, color=colors, alpha=0.9)
    for i, (bar, value) in enumerate(zip(bars, surviving)):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 12, f"{value}M",
                ha="center", fontsize=9.5, color="#222")
        if i > 0:
            kept = surviving[i] / surviving[i - 1] * 100
            ax.text(bar.get_x() + bar.get_width() / 2, value / 2, f"{kept:.0f}%",
                    ha="center", fontsize=9, color="#fff", fontweight="bold")
    ax.set_xticks(range(len(stages)))
    ax.set_xticklabels(stages, fontsize=9)
    ax.set_ylabel("documents surviving (millions)")
    ax.set_title("The curation funnel (illustrative): a raw crawl keeps ~19%")
    ax.text(3.0, 760, "% = fraction of the PREVIOUS stage kept", color="#444", fontsize=9)
    save(fig, "filter_yield.png")


def dedup_savings():
    """Illustrative saturating curves: the deduplicated corpus climbs faster per step."""
    steps = np.linspace(0, 100, 400)
    quality_with_duplicates = 1 - np.exp(-steps / 38)
    quality_deduplicated = 1 - np.exp(-steps / 9)
    target = 0.9
    steps_deduplicated = -9 * np.log(1 - target)
    steps_with_duplicates = -38 * np.log(1 - target)

    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    ax.plot(steps, quality_deduplicated, color=GREEN, lw=3, label="deduplicated data")
    ax.plot(steps, quality_with_duplicates, color=RED, lw=2.6, ls="--",
            label="data with duplicates")
    ax.axhline(target, color=SLATE, ls=":", lw=1.4)
    ax.scatter([steps_deduplicated], [target], color=GREEN, zorder=5, s=60)
    ax.scatter([steps_with_duplicates], [target], color=RED, zorder=5, s=60)
    ax.annotate(f"deduplicated: ~{steps_deduplicated:.0f}%", xy=(steps_deduplicated, target),
                xytext=(steps_deduplicated + 4, 0.68), color=GREEN, fontsize=9.5,
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.3))
    ax.annotate(f"with duplicates: ~{steps_with_duplicates:.0f}%",
                xy=(steps_with_duplicates, target), xytext=(steps_with_duplicates - 34, 0.95),
                color=RED, fontsize=9.5, arrowprops=dict(arrowstyle="->", color=RED, lw=1.3))
    ax.text(50, 0.42, "illustrative shape:\nsame quality, fewer steps", color="#333",
            fontsize=10, ha="center")
    ax.set_xlabel("training steps (% of budget)")
    ax.set_ylabel("model quality (normalized)")
    ax.set_title("Duplicates spend compute re-learning text the model has seen")
    ax.legend(loc="lower right", frameon=False)
    ax.set_ylim(0, 1.02)
    save(fig, "dedup_savings.png")


def minhash_accuracy():
    """Each slot agrees with probability J, so the estimate is Binomial(n, J) / n."""
    rng = np.random.default_rng(1)
    true_jaccard = 0.6
    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    for length, color in zip([16, 64, 256], [AMBER, BLUE, GREEN]):
        estimates = rng.binomial(length, true_jaccard, size=4000) / length
        spread = np.sqrt(true_jaccard * (1 - true_jaccard) / length)
        ax.hist(estimates, bins=30, range=(0.2, 1.0), alpha=0.55, color=color, density=True,
                label=f"signature length = {length}  (std = {spread:.3f})")
    ax.axvline(true_jaccard, color=RED, ls="--", lw=1.8)
    ax.text(true_jaccard + 0.01, ax.get_ylim()[1] * 0.9, f"true Jaccard = {true_jaccard}",
            color=RED, fontsize=9.5)
    ax.set_xlabel("estimated Jaccard (fraction of signature slots that agree)")
    ax.set_ylabel("density")
    ax.set_title("MinHash: longer signatures estimate similarity more tightly")
    ax.legend(loc="upper left", frameon=False, fontsize=9)
    save(fig, "minhash_accuracy.png")


def lsh_s_curve():
    """P(candidate) = 1 - (1 - s^r)^b for a 64-slot signature cut three ways."""
    similarity = np.linspace(0, 1, 400)
    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    for bands, rows, color in [(32, 2, AMBER), (16, 4, BLUE), (8, 8, GREEN)]:
        probability = 1 - (1 - similarity ** rows) ** bands
        threshold = (1 / bands) ** (1 / rows)
        ax.plot(similarity, probability, color=color, lw=2.6,
                label=f"b={bands} bands x r={rows} rows  (knee ~ {threshold:.2f})")
    ax.axvline(0.462, color=RED, ls=":", lw=1.6)
    ax.text(0.475, 0.62, "TinyCorpus pair\ns = 0.462", color=RED, fontsize=9.5)
    ax.set_xlabel("true Jaccard similarity s of two documents")
    ax.set_ylabel("probability they become candidates")
    ax.set_title("LSH banding turns similarity into a soft threshold")
    ax.legend(loc="lower right", bbox_to_anchor=(1.0, 0.12), frameon=True, framealpha=0.95,
              fontsize=9)
    save(fig, "lsh_s_curve.png")


if __name__ == "__main__":
    filter_yield()
    dedup_savings()
    minhash_accuracy()
    lsh_s_curve()
    print("wrote filter_yield.png, dedup_savings.png, minhash_accuracy.png, lsh_s_curve.png")
