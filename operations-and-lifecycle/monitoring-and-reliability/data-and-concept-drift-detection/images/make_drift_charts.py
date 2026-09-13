"""Generate the drift-detection charts for this page.

  drift_psi.png            reference vs drifted production (left) and a daily PSI
                           series with the 0.1 / 0.2 bands and the stricter 0.25 cut (right)
  ks_critical_vs_n.png     the KS critical value shrinking as 1/sqrt(N) against the
                           near-constant D of a tiny 0.05-standard-deviation shift

Run: uv run --python 3.12 --with numpy --with scipy --with matplotlib python make_drift_charts.py
"""
import os
from math import erf, sqrt

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SEED = 0
C_ALPHA = 1.358  # alpha = 0.05
TINY_SHIFT = 0.05
PSI_WATCH, PSI_ACT, PSI_MAJOR = 0.10, 0.20, 0.25

C_DATA = "#3A6B96"
C_PROC = "#5D4A8A"
C_DANGER = "#8B3B4A"
C_WARN = "#7D5A2C"
C_FROZEN = "#4A5B6E"
C_OK = "#2E7A5A"

plt.rcParams.update({
    "font.size": 10, "axes.titlesize": 13, "axes.titleweight": "bold",
    "axes.labelsize": 11, "legend.fontsize": 9, "figure.dpi": 130,
})


def psi(reference: np.ndarray, production: np.ndarray, bins: int = 10) -> float:
    edges = np.quantile(reference, np.linspace(0, 1, bins + 1))
    edges[0], edges[-1] = -np.inf, np.inf
    ref_share = np.clip(np.histogram(reference, edges)[0] / reference.size, 1e-6, None)
    prod_share = np.clip(np.histogram(production, edges)[0] / production.size, 1e-6, None)
    return float(np.sum((prod_share - ref_share) * np.log(prod_share / ref_share)))


def tidy(axis) -> None:
    axis.spines["top"].set_visible(False)
    axis.spines["right"].set_visible(False)


def make_drift_psi(rng: np.random.Generator) -> None:
    reference = rng.normal(0.0, 1.0, 10_000)
    drifted = rng.normal(0.6, 1.3, 10_000)
    days = np.arange(1, 15)
    means = np.concatenate([np.zeros(6), np.linspace(0.0, 0.7, 8)])
    series = np.array([psi(reference, rng.normal(m, 1.0 + 0.4 * (m > 0), 4_000)) for m in means])

    fig, (left, right) = plt.subplots(1, 2, figsize=(11.2, 4.3))
    bins = np.linspace(-5, 6, 60)
    left.hist(reference, bins=bins, color=C_DATA, alpha=0.6, density=True, label="reference (validation)")
    left.hist(drifted, bins=bins, color=C_DANGER, alpha=0.6, density=True, label="production (drifted)")
    left.set_title("Covariate shift: the input moved")
    left.set_xlabel("order_value (standardized)")
    left.set_ylabel("Density")
    left.legend()
    tidy(left)

    right.plot(days, series, marker="o", color=C_PROC, linewidth=2.2, markersize=5)
    right.axhline(PSI_WATCH, color=C_OK, linestyle="--", linewidth=1.5)
    right.axhline(PSI_ACT, color=C_WARN, linestyle="--", linewidth=1.7)
    right.axhline(PSI_MAJOR, color=C_DANGER, linestyle=":", linewidth=1.5)
    right.text(1.2, PSI_WATCH + 0.01, "0.1  watch", color=C_OK, fontsize=9, fontweight="bold")
    right.text(1.2, PSI_ACT + 0.01, "0.2  act", color=C_WARN, fontsize=9, fontweight="bold")
    right.text(1.2, PSI_MAJOR + 0.01, "0.25  stricter major-shift cut", color=C_DANGER, fontsize=9)
    right.fill_between(days, PSI_ACT, series, where=series > PSI_ACT, color=C_WARN, alpha=0.15)
    first_act = int(days[np.argmax(series > PSI_ACT)])
    first_major = int(days[np.argmax(series > PSI_MAJOR)])
    right.set_title(f"Daily PSI: crosses 0.2 on day {first_act}")
    right.set_xlabel("Day")
    right.set_ylabel("PSI")
    right.set_ylim(0, series.max() * 1.15)
    tidy(right)

    fig.tight_layout(w_pad=3.0)
    fig.savefig(os.path.join(OUT_DIR, "drift_psi.png"), bbox_inches="tight")
    plt.close(fig)
    print("drift_psi.png  daily PSI:", " ".join(f"{v:.3f}" for v in series))
    print(f"  first day > 0.2: {first_act}   first day > 0.25: {first_major}")


def make_ks_critical(rng: np.random.Generator) -> None:
    sizes = np.logspace(2, 6, 60)
    critical = C_ALPHA * np.sqrt(2.0 / sizes)
    sampled_n = np.array([1_000, 3_000, 10_000, 30_000, 100_000, 300_000, 1_000_000])
    sampled_d = []
    for n in sampled_n:
        reference = np.sort(rng.normal(0.0, 1.0, n))
        production = np.sort(rng.normal(TINY_SHIFT, 1.0, n))
        pooled = np.concatenate([reference, production])
        gap = np.abs(np.searchsorted(reference, pooled, side="right") / n
                     - np.searchsorted(production, pooled, side="right") / n)
        sampled_d.append(gap.max())
    # Two unit normals a distance delta apart: their CDFs are furthest apart at the
    # midpoint, where the gap is Phi(delta/2) - Phi(-delta/2) = erf(delta / (2*sqrt(2))).
    population_d = erf(TINY_SHIFT / (2 * sqrt(2)))
    crossover = 2 * (C_ALPHA / population_d) ** 2

    fig, axis = plt.subplots(figsize=(8.8, 4.4))
    axis.plot(sizes, critical, color=C_DANGER, linewidth=2.2, label="critical D at alpha 0.05 (shrinks as 1/sqrt(N))")
    axis.axhline(population_d, color=C_FROZEN, linestyle="--", linewidth=1.6,
                 label=f"true D of a {TINY_SHIFT} std shift = {population_d:.4f}")
    axis.scatter(sampled_n, sampled_d, color=C_DATA, zorder=3, label="observed D in simulation")
    axis.axvline(crossover, color=C_WARN, linestyle=":", linewidth=1.6)
    axis.text(crossover * 1.15, critical.max() * 0.6, f"flagged as drift\nbeyond N = {crossover:,.0f}",
              color=C_WARN, fontsize=9, fontweight="bold")
    axis.set_xscale("log")
    axis.set_yscale("log")
    axis.set_title("KS over-sensitivity: the bar falls, the harmless gap stays")
    axis.set_xlabel("Samples per window (n = m)")
    axis.set_ylabel("KS statistic D")
    axis.legend(loc="lower left")
    tidy(axis)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "ks_critical_vs_n.png"), bbox_inches="tight")
    plt.close(fig)
    print(f"ks_critical_vs_n.png  population D={population_d:.4f}  crossover N={crossover:,.0f}")
    print("  observed D:", " ".join(f"{n}:{d:.4f}" for n, d in zip(sampled_n, sampled_d)))


def main() -> None:
    rng = np.random.default_rng(SEED)
    make_drift_psi(rng)
    make_ks_critical(rng)


if __name__ == "__main__":
    main()
