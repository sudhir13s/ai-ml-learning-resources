"""Generate every PNG used by Training.md.

Run:  python practitioner-workflows/training-and-adaptation/model-training/images/generate_figures.py
Writes (alongside this script):
  - loss_curve.png        train vs val loss + overfitting region
  - lr_schedule.png       linear warmup + cosine decay
  - memory_breakdown.png  where VRAM goes when training a 7B model
  - chinchilla.png        compute-optimal: ~20 tokens / parameter
  - batch_throughput.png  batch size vs gradient noise & step throughput

Palette matches the repo's muted Mermaid colors; titles are clean text, no emoji.
All text uses dark slate so the figures read on light or dark backgrounds.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

# Muted palette (same hex values as the Mermaid classDefs in the doc).
INK    = "#2b2b2b"
DATA   = "#3A6B96"   # input / data (blue)
PROC   = "#5D4A8A"   # process (purple)
OK     = "#2E7A5A"   # success (green)
BAD    = "#8B3B4A"   # danger (red)
WARN   = "#7D5A2C"   # warning (brown)
FROZEN = "#4A5B6E"   # static (slate)
AMBER  = "#7A6528"   # highlight (amber)
NAVY   = "#2A5B80"   # navy alt

plt.rcParams.update({
    "figure.dpi": 130,
    "font.size": 12,
    "axes.titlesize": 15,
    "axes.titleweight": "bold",
    "axes.edgecolor": "#888",
    "axes.labelcolor": INK,
    "text.color": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "axes.grid": True,
    "grid.color": "#dddddd",
    "grid.linewidth": 0.8,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})


def save(fig, name):
    path = os.path.join(HERE, name)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", path)


# ---------------------------------------------------------------- loss_curve
def loss_curve():
    ep = np.arange(0, 21)
    train = 0.35 + 3.65 * np.exp(-0.35 * ep)
    val = 0.72 + 3.28 * np.exp(-0.38 * ep) + 0.0075 * (ep ** 2.15) * (ep > 9)
    fig, ax = plt.subplots(figsize=(7.4, 3.9))
    ax.plot(ep, train, "-o", color=DATA, lw=2.4, ms=5, label="Train loss")
    ax.plot(ep, val, "-s", color=BAD, lw=2.4, ms=5, label="Validation loss")
    ax.axvspan(10, 20, color=BAD, alpha=0.06)
    ax.text(15.5, 2.4, "overfitting\nregion", color=BAD, ha="center", fontsize=12)
    vmin = int(np.argmin(val))
    ax.scatter([vmin], [val[vmin]], s=130, color=OK, zorder=5)
    ax.annotate("stop here\n(val minimum)", xy=(vmin, val[vmin]),
                xytext=(vmin - 4.2, val[vmin] + 0.7), color=OK, fontweight="bold",
                fontsize=12, arrowprops=dict(arrowstyle="->", color=OK, lw=2))
    ax.set_title("Train vs validation loss: watch the validation minimum")
    ax.set_xlabel("Epoch"); ax.set_ylabel("Loss")
    ax.set_xlim(0, 20); ax.set_ylim(0, 4)
    ax.legend(loc="upper right", frameon=True)
    save(fig, "loss_curve.png")


# -------------------------------------------------------------- lr_schedule
def lr_schedule():
    total, warm, peak, floor = 1000, 100, 3e-4, 3e-5
    s = np.arange(total + 1)
    lr = np.where(
        s < warm, peak * s / warm,
        floor + 0.5 * (peak - floor) * (1 + np.cos(np.pi * (s - warm) / (total - warm))),
    )
    fig, ax = plt.subplots(figsize=(7.4, 3.9))
    ax.plot(s[:warm + 1], lr[:warm + 1], color=AMBER, lw=3, label="Warmup (linear)")
    ax.plot(s[warm:], lr[warm:], color=DATA, lw=3, label="Cosine decay")
    ax.axvline(warm, color=PROC, ls="--", lw=1.6, alpha=0.8)
    ax.annotate("peak LR = 3e-4\n(end of warmup)", xy=(warm, peak),
                xytext=(warm + 70, peak * 0.97), color=PROC, fontsize=11,
                arrowprops=dict(arrowstyle="->", color=PROC))
    ax.annotate("floor = 10% of peak", xy=(total, floor),
                xytext=(total - 360, floor + 4.2e-5), color=OK, fontsize=11,
                arrowprops=dict(arrowstyle="->", color=OK))
    ax.set_title("Learning-rate schedule: linear warmup + cosine decay")
    ax.set_xlabel("Training step"); ax.set_ylabel("Learning rate")
    ax.set_xlim(0, total); ax.set_ylim(0, peak * 1.08)
    ax.legend(loc="upper right", frameon=True)
    save(fig, "lr_schedule.png")


# --------------------------------------------------------- memory_breakdown
def memory_breakdown():
    """Where VRAM goes for a 7B model: FP32 full vs BF16 mixed-precision training."""
    P = 7e9
    # bytes-per-parameter for each component, by regime (standard HF/DeepSpeed figures).
    regimes = ["FP32 full\ntraining", "BF16 mixed\nprecision", "+ grad ckpt\n(activations)"]
    # FP32: w4 g4 opt8 acts6.  BF16 mixed: bf16 weights(2)+fp32 master(4)=6,
    # bf16 grads(2), AdamW fp32 states(8), activations in bf16 (~3).
    weights  = np.array([4, 6, 6])
    grads    = np.array([4, 2, 2])
    optim    = np.array([8, 8, 8])      # AdamW: two fp32 moments per param
    acts     = np.array([6, 3, 0.8])    # activations, shrunk by checkpointing
    comps = [("Weights", weights, DATA), ("Gradients", grads, PROC),
             ("Optimizer (AdamW)", optim, BAD), ("Activations", acts, WARN)]
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    bottom = np.zeros(len(regimes))
    x = np.arange(len(regimes))
    for label, vals, color in comps:
        gb = vals * P / 1e9
        ax.bar(x, gb, 0.55, bottom=bottom, label=label, color=color, edgecolor="white")
        bottom += gb
    top = bottom.max()
    for i, tot in enumerate(bottom):
        ax.text(i, tot + top * 0.02, f"{tot:.0f} GB", ha="center",
                fontweight="bold", fontsize=12)
    ax.axhline(80, color=FROZEN, ls="--", lw=1.6)
    ax.text(1.5, 84, "80 GB = one A100", color=FROZEN, ha="left", fontsize=10)
    ax.set_title("Where training VRAM goes for a 7B model", pad=14)
    ax.set_ylabel("VRAM (GB)")
    ax.set_xticks(x); ax.set_xticklabels(regimes)
    ax.set_ylim(0, top * 1.2)
    ax.legend(loc="upper right", frameon=True, fontsize=10)
    ax.grid(axis="x", visible=False)
    save(fig, "memory_breakdown.png")


# ------------------------------------------------------------------ chinchilla
def chinchilla():
    """Compute-optimal frontier: ~20 tokens per parameter (Chinchilla)."""
    params = np.array([1e8, 1e9, 7e9, 7e10, 5e11])
    tokens = 20 * params
    fig, ax = plt.subplots(figsize=(7.4, 4.0))
    ax.loglog(params, tokens, "-o", color=OK, lw=2.6, ms=8,
              label="Compute-optimal (~20 tokens / param)")
    # GPT-3 style under-trained point for contrast (175B on ~300B tokens)
    ax.loglog([1.75e11], [3e11], "X", color=BAD, ms=14, label="GPT-3: under-trained")
    ax.annotate("GPT-3\n175B / 300B tok", xy=(1.75e11, 3e11),
                xytext=(2.4e10, 9e11), color=BAD, fontsize=10,
                arrowprops=dict(arrowstyle="->", color=BAD))
    for p, t, name in [(7e9, 1.4e11, "7B\n140B tok"), (7e10, 1.4e12, "70B\n1.4T tok")]:
        ax.annotate(name, xy=(p, t), xytext=(p * 0.32, t * 2.4),
                    color=NAVY, fontsize=10,
                    arrowprops=dict(arrowstyle="->", color=NAVY))
    ax.set_title("Compute-optimal scaling: data must grow with model size")
    ax.set_xlabel("Model parameters"); ax.set_ylabel("Training tokens")
    ax.legend(loc="upper left", frameon=True, fontsize=10)
    save(fig, "chinchilla.png")


# ------------------------------------------------------------ batch_throughput
def batch_throughput():
    """Two truths about batch size: gradient noise falls as 1/sqrt(B); per-step
    throughput rises then saturates once the GPU is full."""
    B = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])
    noise = 1.0 / np.sqrt(B)                       # gradient-estimate std, normalized
    # examples/sec: linear while GPU under-filled, saturates afterwards
    sat = 700.0
    thru = sat * (1 - np.exp(-B / 90.0))
    fig, ax1 = plt.subplots(figsize=(7.4, 4.0))
    l1, = ax1.semilogx(B, noise, "-o", color=BAD, lw=2.6, ms=6, base=2,
                       label="Gradient noise (1/sqrt(B))")
    ax1.set_xlabel("Batch size"); ax1.set_ylabel("Relative gradient noise", color=BAD)
    ax1.tick_params(axis="y", labelcolor=BAD)
    ax1.set_xticks(B); ax1.set_xticklabels([str(b) for b in B], fontsize=9)
    ax2 = ax1.twinx()
    ax2.grid(False)
    l2, = ax2.semilogx(B, thru, "-s", color=OK, lw=2.6, ms=6, base=2,
                       label="Throughput (examples/sec)")
    ax2.set_ylabel("Throughput (examples/sec)", color=OK)
    ax2.tick_params(axis="y", labelcolor=OK)
    ax1.axvspan(32, 256, color=NAVY, alpha=0.07)
    ax1.text(90, 0.85, "usual\nsweet spot", color=NAVY, ha="center", fontsize=11)
    ax1.set_title("Batch size: diminishing noise reduction, saturating throughput")
    ax1.legend(handles=[l1, l2], loc="upper center", frameon=True, fontsize=10)
    save(fig, "batch_throughput.png")


if __name__ == "__main__":
    loss_curve()
    lr_schedule()
    memory_breakdown()
    chinchilla()
    batch_throughput()
    print("done")
