"""Two-sample Kolmogorov-Smirnov (KS) drift check, from scratch and with SciPy.

Three parts, all deterministic and CPU-only:
  1. The by-hand example from the page: two four-value score samples, the
     empirical CDF table, the statistic D, and why D = 0.5 is not evidence at N = 4.
  2. The drift detector on a realistic window: a matched production sample and a
     shifted one, scored against a 10,000-value reference.
  3. The large-sample trap: a business-irrelevant 0.05-standard-deviation shift
     becomes "statistically significant" once the window is big enough.

Run: uv run --python 3.12 --with numpy --with scipy python ks_drift_check.py
"""
import numpy as np
from scipy import stats

ALPHA = 0.05
C_ALPHA = np.sqrt(-np.log(ALPHA / 2) / 2)  # 1.358 for alpha = 0.05
SEED = 0


def empirical_cdf(sample: np.ndarray, points: np.ndarray) -> np.ndarray:
    """Fraction of `sample` that is <= each value in `points`."""
    return np.searchsorted(np.sort(sample), points, side="right") / sample.size


def ks_statistic(reference: np.ndarray, production: np.ndarray) -> float:
    """Largest vertical gap between the two empirical CDFs.

    The gap can only change where one of the step functions steps, so checking
    every pooled observation is enough to find the maximum.
    """
    pooled = np.concatenate([reference, production])
    gaps = np.abs(empirical_cdf(reference, pooled) - empirical_cdf(production, pooled))
    return float(gaps.max())


def critical_d(n: int, m: int) -> float:
    """Large-sample rejection threshold: reject 'same distribution' when D exceeds it."""
    return float(C_ALPHA * np.sqrt((n + m) / (n * m)))


def show_by_hand_example() -> None:
    reference = np.array([0.1, 0.2, 0.3, 0.4])
    production = np.array([0.3, 0.4, 0.5, 0.6])
    grid = np.unique(np.concatenate([reference, production]))
    print("== 1. BY HAND: four scores each ==")
    print("   x    CDF_ref  CDF_prod  gap")
    for x, cdf_r, cdf_p in zip(grid, empirical_cdf(reference, grid), empirical_cdf(production, grid)):
        print(f"  {x:.1f}   {cdf_r:5.2f}    {cdf_p:5.2f}   {abs(cdf_r - cdf_p):.2f}")
    scratch_d = ks_statistic(reference, production)
    library = stats.ks_2samp(reference, production)
    print(f"  D from scratch = {scratch_d:.2f}   D from scipy = {library.statistic:.2f}")
    print(f"  p-value = {library.pvalue:.3f}  (n = m = 4, so even a 0.5 gap could be chance)")


def show_drift_windows(rng: np.random.Generator) -> None:
    reference = rng.normal(0.0, 1.0, 10_000)   # what the model was validated on
    prod_ok = rng.normal(0.0, 1.0, 5_000)      # production that still matches
    prod_drift = rng.normal(0.6, 1.3, 5_000)   # production after a campaign shifted it
    print("\n== 2. DRIFT WINDOWS: reference n = 10,000, production n = 5,000 ==")
    print(f"  critical D at alpha {ALPHA}: {critical_d(10_000, 5_000):.4f}")
    for name, sample in [("prod_ok", prod_ok), ("prod_drift", prod_drift)]:
        result = stats.ks_2samp(reference, sample)
        scratch_d = ks_statistic(reference, sample)
        verdict = "DRIFT" if result.pvalue < ALPHA else "ok"
        print(f"  {name:10s} D={result.statistic:.3f} (scratch {scratch_d:.3f})  "
              f"p={result.pvalue:.2e} -> {verdict}")


def show_large_sample_trap(rng: np.random.Generator) -> None:
    shift = 0.05  # standard deviations: far too small to hurt a fraud model
    print(f"\n== 3. THE LARGE-SAMPLE TRAP: a fixed {shift} standard-deviation shift ==")
    print("        N     D     critical D    p-value   verdict")
    for n in [1_000, 10_000, 100_000, 1_000_000]:
        reference = rng.normal(0.0, 1.0, n)
        production = rng.normal(shift, 1.0, n)
        result = stats.ks_2samp(reference, production)
        verdict = "DRIFT" if result.pvalue < ALPHA else "ok"
        print(f"  {n:>9,}  {result.statistic:.4f}   {critical_d(n, n):.4f}     "
              f"{result.pvalue:.2e}   {verdict}")


def main() -> None:
    rng = np.random.default_rng(SEED)
    show_by_hand_example()
    show_drift_windows(rng)
    show_large_sample_trap(rng)


if __name__ == "__main__":
    main()
