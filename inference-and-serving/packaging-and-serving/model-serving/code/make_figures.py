"""Draw the two figures for the LLM serving engines page from request_lifecycle.py.

Every plotted number comes from the same functions the page's program prints, so the
charts cannot drift from the text. Writes PNGs into ../images.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from request_lifecycle import (
    BITS_PER_WEIGHT, ENGINE, LONG_CONTEXT_TOKENS, MISTRAL_7B, OUTPUT_TOKENS, PROMPT_TOKENS,
    TPOT_MS, TTFT_MS, blocks_for, end_to_end_ms, kv_bytes_per_token, vram_budget,
)

OUT_DIR = Path(__file__).resolve().parent.parent / "images"
ADMIT_MS = 3.0
BLUE, PURPLE, GREEN, RED, AMBER, GREY = "#3A6B96", "#5D4A8A", "#2E7A5A", "#8B3B4A", "#7A6528", "#4A5B6E"

plt.rcParams.update({
    "figure.facecolor": "white", "axes.facecolor": "white", "axes.edgecolor": "#888",
    "text.color": "#222", "axes.labelcolor": "#222", "xtick.color": "#222", "ytick.color": "#222",
    "font.size": 11, "axes.grid": True, "grid.color": "#ddd", "grid.linewidth": 0.6,
})


def block_timeline() -> None:
    times, blocks = [0.0, ADMIT_MS], [0, blocks_for(PROMPT_TOKENS, ENGINE)]
    for token in range(2, OUTPUT_TOKENS + 1):
        times.append(TTFT_MS + TPOT_MS * (token - 1))
        blocks.append(blocks_for(PROMPT_TOKENS + token - 1, ENGINE))
    finish = end_to_end_ms(TTFT_MS, TPOT_MS, OUTPUT_TOKENS)
    times.append(finish + 1)
    blocks.append(0)

    fig, ax = plt.subplots(figsize=(8.2, 4.4))
    ax.step(times, blocks, where="post", color=PURPLE, lw=2.4)
    ax.axvline(TTFT_MS, color=GREEN, ls="--", lw=1.6)
    ax.text(TTFT_MS + 15, 8, f"first token\n{TTFT_MS:.0f} ms", color=GREEN, fontsize=9.5)
    ax.axvline(finish, color=RED, ls="--", lw=1.6)
    ax.text(finish - 250, 8, f"EOS at {finish:,.0f} ms\nall 41 blocks freed", color=RED, fontsize=9.5)
    ax.annotate("prefill: 38 blocks at once", xy=(ADMIT_MS, 38), xytext=(260, 20),
                color=AMBER, fontsize=9.5, arrowprops=dict(arrowstyle="->", color=AMBER))
    ax.annotate("decode: +1 block per 16 tokens", xy=(TTFT_MS + TPOT_MS * 41, 41), xytext=(560, 30),
                color=BLUE, fontsize=9.5, arrowprops=dict(arrowstyle="->", color=BLUE))
    ax.set_ylim(0, 46)
    ax.set_xlabel("time since the request arrived (ms)")
    ax.set_ylabel("KV blocks held (16 tokens each)")
    ax.set_title("One request's KV memory: allocated at prefill, grown in decode, freed at EOS")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "request_block_lifecycle.png", dpi=130)
    plt.close(fig)


def vram_by_precision() -> None:
    usable = ENGINE.gpu_memory_gb * ENGINE.gpu_memory_utilization
    reserve = ENGINE.gpu_memory_gb - usable
    per_request = kv_bytes_per_token(MISTRAL_7B, ENGINE) * LONG_CONTEXT_TOKENS / 1e9
    labels = list(BITS_PER_WEIGHT)
    budgets = [vram_budget(MISTRAL_7B, ENGINE, name, LONG_CONTEXT_TOKENS) for name in labels]

    fig, ax = plt.subplots(figsize=(9.0, 4.4))
    for row, budget in enumerate(budgets):
        left = 0.0
        segments = [(budget.weights_gb, RED, "weights"), (ENGINE.runtime_overhead_gb, GREY, "runtime overhead"),
                    (budget.kv_cache_gb, GREEN, "KV cache"), (reserve, "#BBBBBB", "held back (utilization 0.90)")]
        for width, color, name in segments:
            ax.barh(row, width, left=left, color=color, edgecolor="white", label=name if row == 0 else None)
            left += width
        ax.text(ENGINE.gpu_memory_gb + 0.3, row,
                f"{budget.concurrent_long_requests} x 8K requests", va="center", fontsize=10)
    ax.set_yticks(range(len(labels)), labels)
    ax.invert_yaxis()
    ax.set_xlim(0, 30)
    ax.set_xlabel(f"GPU memory (GB) on a 24 GB card; one 8K-token request holds {per_request:.2f} GB of KV")
    ax.set_title("Smaller weights leave more KV cache, and KV cache is concurrency")
    ax.legend(loc="upper center", bbox_to_anchor=(0.45, -0.22), fontsize=8.5, ncol=4, frameon=False)
    fig.tight_layout()
    fig.savefig(OUT_DIR / "vram_budget_by_precision.png", dpi=130)
    plt.close(fig)


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    block_timeline()
    vram_by_precision()
    print("wrote", sorted(path.name for path in OUT_DIR.glob("*.png")))


if __name__ == "__main__":
    main()
