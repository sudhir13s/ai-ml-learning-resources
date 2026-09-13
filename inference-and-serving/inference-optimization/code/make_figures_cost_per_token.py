"""Generate serving_cost_per_million_tokens.png from cost_per_token.py.

The figure is drawn from the same functions that print the page's cost table, so a constant
change re-prices the table and the plot together. Every value is MODELED.

Run:
    python make_figures_cost_per_token.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402  (backend must be set before pyplot import)

from cost_per_token import (  # noqa: E402
    GPU_DOLLARS_PER_HOUR,
    LONG_CONTEXT_TOKENS,
    dollars_per_million_tokens,
    throughput_tok_per_s,
)
from inference_serving import (  # noqa: E402
    BATCH_SIZES,
    ROOFLINE_CONTEXT_TOKENS,
    roofline_crossover_batch,
)

OUTPUT_PATH = Path(__file__).resolve().parent.parent / "images" / "serving_cost_per_million_tokens.png"
SWEEP_BATCHES = [2 ** (exponent / 8) for exponent in range(0, 9 * 8 + 1)]  # 1 .. 512, smooth
SHORT_COLOR = "#3A6B96"
LONG_COLOR = "#8B3B4A"
CROSSOVER_COLOR = "#7A6528"
GRID_COLOR = "#D9D9D9"


def cost_curve(context_tokens: int, batches: list[float]) -> list[float]:
    """Modeled dollars per million tokens at each (possibly fractional) batch size."""
    return [dollars_per_million_tokens(throughput_tok_per_s(batch, context_tokens)) for batch in batches]


def main() -> None:
    fig, axis = plt.subplots(figsize=(8.5, 5.0), dpi=150)
    for context, color in ((ROOFLINE_CONTEXT_TOKENS, SHORT_COLOR), (LONG_CONTEXT_TOKENS, LONG_COLOR)):
        axis.plot(SWEEP_BATCHES, cost_curve(context, SWEEP_BATCHES), color=color, linewidth=2,
                  label=f"{context:,}-token context")
        axis.scatter(BATCH_SIZES, cost_curve(context, list(BATCH_SIZES)), color=color, s=22, zorder=3)

    crossover = roofline_crossover_batch(ROOFLINE_CONTEXT_TOKENS)
    floor = dollars_per_million_tokens(throughput_tok_per_s(512, ROOFLINE_CONTEXT_TOKENS))
    axis.axvline(crossover, color=CROSSOVER_COLOR, linestyle="--", linewidth=1.3)
    axis.annotate(f"compute roofline B* ≈ {crossover:.0f}\nfloor ${floor:.4f} / 1M",
                  xy=(crossover, floor), xytext=(14, floor * 1.05), color=CROSSOVER_COLOR, fontsize=9,
                  arrowprops={"arrowstyle": "->", "color": CROSSOVER_COLOR})
    batch_one = dollars_per_million_tokens(throughput_tok_per_s(1, ROOFLINE_CONTEXT_TOKENS))
    axis.annotate(f"batch 1: ${batch_one:.2f} / 1M", xy=(1, batch_one), xytext=(2.2, batch_one * 0.9),
                  fontsize=9, color=SHORT_COLOR)

    axis.set_xscale("log", base=2)
    axis.set_yscale("log")
    axis.set_xlabel("decode batch size B (log scale)")
    axis.set_ylabel("dollars per 1M output tokens (log scale)")
    axis.set_title(f"Self-hosted decode cost, Llama-3-8B on one A100 at ${GPU_DOLLARS_PER_HOUR:.0f}/GPU-hour (modeled)",
                   fontsize=10.5)
    axis.grid(True, which="both", color=GRID_COLOR, linewidth=0.6)
    axis.legend(frameon=False)
    for side in ("top", "right"):
        axis.spines[side].set_visible(False)
    fig.tight_layout()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH)
    print(f"wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
