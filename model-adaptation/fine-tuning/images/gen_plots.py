"""Generate the quantitative figures for the Fine-Tuning workflow note.

Run inside ml-py312:
    source ~/.uv/envs/ml-py312/bin/activate
    python gen_plots.py

Produces (in this folder):
    finetune_vram.png        - training VRAM by approach (full / LoRA / QLoRA)
    finetune_loss_curve.png  - train vs val loss, the overfitting turn
    finetune_lr_schedule.png - warmup + cosine decay learning-rate schedule
    finetune_rank_tradeoff.png - LoRA rank vs trainable params vs quality
    finetune_precision_bits.png - bytes-per-parameter across precisions
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


def vram():
    """Stacked training-VRAM bars for a 7B model: full vs LoRA vs QLoRA."""
    approaches = ["Full FT\n(fp16)", "LoRA\n(fp16 base)", "QLoRA\n(4-bit base)"]
    # GB, broken into components. Full FT: weights 14 + grads 14 + optim 56 + acts ~8.
    weights = [14, 14, 5]
    grads = [14, 0.5, 0.5]
    optim = [56, 2, 2]
    acts = [8, 1.5, 0.5]

    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    x = np.arange(len(approaches))
    b1 = ax.bar(x, weights, color=BLUE, label="model weights")
    b2 = ax.bar(x, grads, bottom=weights, color=PURPLE, label="gradients")
    bottom2 = np.array(weights) + np.array(grads)
    b3 = ax.bar(x, optim, bottom=bottom2, color=RED, label="optimizer states")
    bottom3 = bottom2 + np.array(optim)
    b4 = ax.bar(x, acts, bottom=bottom3, color=AMBER, label="activations")

    totals = np.array(weights) + np.array(grads) + np.array(optim) + np.array(acts)
    for xi, t in zip(x, totals):
        ax.text(xi, t + 1.5, f"~{t:.0f} GB", ha="center", fontweight="bold", fontsize=11)

    ax.axhline(16, color=GREEN, ls="--", lw=1.6)
    ax.text(2.42, 17.5, "16 GB\nColab T4", color=GREEN, fontsize=9.5, ha="center")
    ax.set_xticks(x)
    ax.set_xticklabels(approaches)
    ax.set_ylabel("training VRAM (GB)")
    ax.set_title("Where the VRAM goes: full fine-tune is mostly optimizer state")
    ax.set_ylim(0, 100)
    ax.legend(loc="upper right", frameon=False)
    fig.tight_layout()
    fig.savefig("finetune_vram.png", bbox_inches="tight")
    plt.close(fig)


def loss_curve():
    """Train vs validation loss; validation bottoms out then rises (overfitting)."""
    epochs = np.linspace(0, 6, 200)
    train = 1.9 * np.exp(-0.7 * epochs) + 0.35
    # Validation: falls with train, then turns up past the optimum.
    val = 1.9 * np.exp(-0.7 * epochs) + 0.55 + 0.06 * (np.maximum(epochs - 2.6, 0)) ** 2

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(epochs, train, color=BLUE, lw=3, label="training loss")
    ax.plot(epochs, val, color=RED, lw=3, label="validation loss")
    stop = int(np.argmin(val))
    ax.scatter([epochs[stop]], [val[stop]], color=GREEN, zorder=5, s=70)
    ax.annotate("stop here\n(val-loss minimum)", xy=(epochs[stop], val[stop]),
                xytext=(epochs[stop] + 0.6, val[stop] + 0.55), color=GREEN, fontsize=10,
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.3))
    ax.axvspan(epochs[stop], 6, color=RED, alpha=0.06)
    ax.text(4.7, 1.6, "overfitting:\nval rises, train keeps falling",
            color=RED, fontsize=9.5, ha="center")
    ax.set_xlabel("training epoch")
    ax.set_ylabel("loss")
    ax.set_title("The only plot that matters: validation loss tells the truth")
    ax.legend(loc="upper right", frameon=False)
    ax.set_ylim(0, 2.6)
    fig.tight_layout()
    fig.savefig("finetune_loss_curve.png", bbox_inches="tight")
    plt.close(fig)


def lr_schedule():
    """Linear warmup then cosine decay of the learning rate."""
    total = 300
    warmup = 50
    peak = 2e-4
    steps = np.arange(total)
    lr = np.where(
        steps < warmup,
        peak * steps / warmup,
        peak * 0.5 * (1 + np.cos(np.pi * (steps - warmup) / (total - warmup))),
    )

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.plot(steps, lr, color=PURPLE, lw=3)
    ax.axvspan(0, warmup, color=BLUE, alpha=0.08)
    ax.annotate("warmup\n(LR ramps 0 -> peak)", xy=(warmup, peak),
                xytext=(warmup + 18, peak * 0.78), color=BLUE, fontsize=9.5,
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2))
    ax.annotate("cosine decay\n(settle into the minimum)", xy=(200, lr[200]),
                xytext=(150, peak * 0.30), color=GREEN, fontsize=9.5,
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2))
    ax.scatter([warmup], [peak], color=RED, zorder=5, s=55)
    ax.set_xlabel("training step")
    ax.set_ylabel("learning rate")
    ax.set_title("Warmup + cosine decay: ramp up, then ease into the minimum")
    ax.set_ylim(0, peak * 1.12)
    fig.tight_layout()
    fig.savefig("finetune_lr_schedule.png", bbox_inches="tight")
    plt.close(fig)


def rank_tradeoff():
    """LoRA rank r vs trainable params and (diminishing) quality gain."""
    ranks = np.array([1, 2, 4, 8, 16, 32, 64, 128])
    # Trainable params for one 4096x4096 matrix pair: 2 * 4096 * r.
    params_k = 2 * 4096 * ranks / 1000.0
    # Quality saturates: most gain by r=8-16.
    quality = 1 - np.exp(-ranks / 7.0)

    fig, ax1 = plt.subplots(figsize=(7.2, 4.4))
    ax1.set_xscale("log", base=2)
    ax1.plot(ranks, params_k, color=BLUE, lw=2.6, marker="o", ms=6,
             label="trainable params (K)")
    ax1.set_xlabel("LoRA rank  r")
    ax1.set_ylabel("trainable params per matrix (K)", color=BLUE)
    ax1.tick_params(axis="y", labelcolor=BLUE)
    ax1.set_xticks(ranks)
    ax1.set_xticklabels([str(r) for r in ranks])

    ax2 = ax1.twinx()
    ax2.plot(ranks, quality, color=GREEN, lw=2.6, marker="s", ms=6,
             label="relative quality")
    ax2.set_ylabel("relative quality reached", color=GREEN)
    ax2.tick_params(axis="y", labelcolor=GREEN)
    ax2.set_ylim(0, 1.05)
    ax2.grid(False)

    ax2.axvspan(8, 16, color=AMBER, alpha=0.12)
    ax2.annotate("sweet spot\nr = 8-16", xy=(11, 0.82), color=AMBER, fontsize=10, ha="center")
    ax1.set_title("LoRA rank: params grow linearly, quality saturates early")
    fig.tight_layout()
    fig.savefig("finetune_rank_tradeoff.png", bbox_inches="tight")
    plt.close(fig)


def precision_bits():
    """Bytes per parameter and the resulting 7B footprint across precisions."""
    names = ["FP32", "FP16/BF16", "INT8", "NF4 (4-bit)"]
    bytes_pp = [4, 2, 1, 0.5]
    gb_7b = [7 * b for b in bytes_pp]
    colors = [RED, AMBER, NAVY, GREEN]

    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    bars = ax.bar(names, gb_7b, color=colors)
    for bar, g, b in zip(bars, gb_7b, bytes_pp):
        ax.text(bar.get_x() + bar.get_width() / 2, g + 0.6,
                f"{g:.1f} GB\n({b} B/param)", ha="center", fontsize=9.5, fontweight="bold")
    ax.set_ylabel("memory for 7B weights (GB)")
    ax.set_title("Cost of one parameter: precision sets the whole budget")
    ax.set_ylim(0, 32)
    fig.tight_layout()
    fig.savefig("finetune_precision_bits.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    vram()
    loss_curve()
    lr_schedule()
    rank_tradeoff()
    precision_bits()
    print("wrote finetune_vram.png, finetune_loss_curve.png, finetune_lr_schedule.png, "
          "finetune_rank_tradeoff.png, finetune_precision_bits.png")
