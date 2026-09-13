"""Draw the training/serving skew figure for the packaging page from package_and_serve.py.

It packages the same artifact the page's program builds, reads the preprocessing
statistics back out of its manifest, and plots the one request two ways: as the
model saw features in training (standardized) and as a caller who skipped the
manifest would send them (raw). Writes PNGs into ../images.
"""
from __future__ import annotations

import tempfile
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from package_and_serve import FEATURES, train_and_package

OUT_DIR = Path(__file__).resolve().parent.parent / "images"
REQUEST = {"amount_usd": 420.0, "account_age_days": 280, "txn_count_24h": 7, "distance_km": 95.0}
TRAINING_BAND = 3.0

plt.rcParams.update({
    "figure.facecolor": "white", "axes.facecolor": "white", "axes.edgecolor": "#888",
    "text.color": "#222", "axes.labelcolor": "#222", "xtick.color": "#222", "ytick.color": "#222",
    "font.size": 11, "axes.grid": True, "grid.color": "#ddd", "grid.linewidth": 0.6,
})


def skew_figure() -> None:
    manifest = train_and_package(Path(tempfile.mkdtemp(prefix="artifact-")))
    stats = manifest["preprocessing"]["standardize"]
    raw = [float(REQUEST[name]) for name in FEATURES]
    standardized = [(value - mean) / std for value, mean, std in zip(raw, stats["mean"], stats["std"])]

    fig, ax = plt.subplots(figsize=(8.4, 4.2))
    positions = range(len(FEATURES))
    ax.axhspan(-TRAINING_BAND, TRAINING_BAND, color="#2E7A5A", alpha=0.12,
               label="where training inputs lived (|z| < 3)")
    ax.bar([p - 0.2 for p in positions], standardized, width=0.4, color="#2E7A5A",
           label="standardized with the manifest's mean/std")
    ax.bar([p + 0.2 for p in positions], raw, width=0.4, color="#8B3B4A",
           label="raw, preprocessing skipped")
    for p, value in zip(positions, raw):
        ax.text(p + 0.2, value * 1.15, f"{value:g}", ha="center", fontsize=9, color="#8B3B4A")
    ax.set_yscale("symlog", linthresh=1)
    ax.set_ylim(-5, 5000)
    ax.set_xticks(list(positions), FEATURES)
    ax.set_ylabel("value the model receives (symlog)")
    ax.set_title("The same request, with and without the artifact's preprocessing")
    ax.legend(loc="upper right", fontsize=8.5)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "training_serving_skew.png", dpi=130)
    plt.close(fig)


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    skew_figure()
    print("wrote", sorted(path.name for path in OUT_DIR.glob("*.png")))


if __name__ == "__main__":
    main()
