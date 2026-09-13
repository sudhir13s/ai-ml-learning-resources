"""Generate the accuracy decay-vs-recovery chart for the Continuous-Training blog.

Reuses the exact simulation in flywheel_sim.py so the picture matches the
runnable numbers in the doc. Output: images/ct_decay_vs_recovery.png
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from flywheel_sim import main as run_sim

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "images")
os.makedirs(IMG, exist_ok=True)

# Muted palette (matches the doc's mermaid palette)
C_STATIC = "#8B3B4A"     # danger / decay
C_FLY = "#2E7A5A"        # success / recovery
C_TRIG = "#7D5A2C"       # warning / trigger
C_FLOOR = "#4A5B6E"      # frozen / threshold line

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.titlesize": 15,
    "axes.titleweight": "bold",
    "axes.labelsize": 11,
    "figure.dpi": 130,
})

static_hist, fly_hist, retrains = run_sim()
weeks = list(range(len(static_hist)))

fig, ax = plt.subplots(figsize=(9.0, 5.0))

ax.plot(weeks, static_hist, "-o", color=C_STATIC, lw=2.2, ms=5,
        label="Static model (never retrained)")
ax.plot(weeks, fly_hist, "-o", color=C_FLY, lw=2.2, ms=5,
        label="Flywheel (retrain on drift)")

ax.axhline(0.85, color=C_FLOOR, ls="--", lw=1.4)
ax.text(0.15, 0.857, "retrain threshold = 0.85", color=C_FLOOR,
        fontsize=9, va="bottom")

for i, w in enumerate(retrains):
    ax.axvline(w, color=C_TRIG, ls=":", lw=1.5, alpha=0.8)
    ax.annotate("retrain", xy=(w, fly_hist[w]), xytext=(w + 0.15, 0.66),
                color=C_TRIG, fontsize=9, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=C_TRIG, lw=1.2))

ax.set_title("The data flywheel beats decay: retraining snaps accuracy back")
ax.set_xlabel("Week in production (the world drifts each week)")
ax.set_ylabel("Live accuracy on fresh traffic")
ax.set_ylim(0.15, 1.0)
ax.set_xticks(weeks)
ax.grid(True, alpha=0.25)
ax.legend(loc="lower left", framealpha=0.95)

# Annotate the gap at the end
ax.annotate(
    f"gap at week {weeks[-1]}:\n{fly_hist[-1] - static_hist[-1]:.0%} higher",
    xy=(weeks[-1], static_hist[-1]), xytext=(weeks[-1] - 3.2, 0.30),
    color=C_STATIC, fontsize=9,
    arrowprops=dict(arrowstyle="->", color=C_STATIC, lw=1.2))

fig.tight_layout()
out = os.path.join(IMG, "ct_decay_vs_recovery.png")
fig.savefig(out, bbox_inches="tight")
print(f"wrote {out}")
