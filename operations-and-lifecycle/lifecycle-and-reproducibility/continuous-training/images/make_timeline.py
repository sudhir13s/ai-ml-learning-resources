"""Generate the retraining-trigger timeline chart for the Continuous-Training blog.

Shows the same 12 weeks under three trigger policies stacked as timelines:
- Scheduled: retrain every 4 weeks no matter what (can fire too late OR waste compute).
- Drift-triggered: retrain when an input-distribution drift score crosses a band.
- Performance-triggered: retrain when live accuracy drops below a floor.

Output: images/ct_trigger_timeline.png
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "images")
os.makedirs(IMG, exist_ok=True)

C_SCHED = "#2A5B80"   # navy
C_DRIFT = "#5D4A8A"   # process
C_PERF = "#2E7A5A"    # success
C_LATE = "#8B3B4A"    # danger - fired too late
C_GRID = "#4A5B6E"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.titlesize": 15,
    "axes.titleweight": "bold",
    "axes.labelsize": 11,
    "figure.dpi": 130,
})

WEEKS = 12
# (label, color, weeks_fired, note_per_fire)
policies = [
    ("Scheduled\n(every 4 wks)", C_SCHED, [0, 4, 8],
     {0: "fixed", 4: "fixed", 8: "fixed"}),
    ("Drift-triggered\n(input PSI band)", C_DRIFT, [3, 7, 10],
     {3: "PSI>0.2", 7: "PSI>0.2", 10: "PSI>0.2"}),
    ("Performance-triggered\n(acc < floor)", C_PERF, [4, 9],
     {4: "acc<0.85", 9: "acc<0.85"}),
]

fig, ax = plt.subplots(figsize=(9.2, 4.2))

for row, (label, color, fires, notes) in enumerate(policies):
    y = len(policies) - 1 - row
    ax.hlines(y, -0.5, WEEKS - 0.5, color=C_GRID, lw=1.0, alpha=0.4)
    for w in fires:
        ax.scatter(w, y, s=240, color=color, zorder=3, edgecolors="white", lw=1.5)
        ax.annotate(notes[w], xy=(w, y), xytext=(w, y + 0.22),
                    ha="center", fontsize=8, color=color, fontweight="bold")

ax.set_yticks(range(len(policies)))
ax.set_yticklabels([p[0] for p in reversed(policies)], fontsize=10)
ax.set_xticks(range(WEEKS))
ax.set_xlabel("Week in production")
ax.set_xlim(-0.7, WEEKS - 0.3)
ax.set_ylim(-0.5, len(policies) - 0.3)
ax.set_title("Three retraining triggers, same 12 weeks: when does each fire?")
ax.grid(False)
for spine in ("top", "right", "left"):
    ax.spines[spine].set_visible(False)

fig.tight_layout()
out = os.path.join(IMG, "ct_trigger_timeline.png")
fig.savefig(out, bbox_inches="tight")
print(f"wrote {out}")
