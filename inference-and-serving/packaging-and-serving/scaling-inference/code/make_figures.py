"""Draw the fleet timeline for the scaling-inference page from autoscaler_sim.py.

The chart replays the exact simulation the page prints, so its replica counts and
queue depths are the same numbers as the table. Writes PNGs into ../images.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from autoscaler_sim import POLICIES, SIM_SECONDS, arrivals_per_second, simulate

OUT_DIR = Path(__file__).resolve().parent.parent / "images"
COLORS = ["#8B3B4A", "#2E7A5A", "#3A6B96"]
STYLES = ["-", "-", "--"]

plt.rcParams.update({
    "figure.facecolor": "white", "axes.facecolor": "white", "axes.edgecolor": "#888",
    "text.color": "#222", "axes.labelcolor": "#222", "xtick.color": "#222", "ytick.color": "#222",
    "font.size": 11, "axes.grid": True, "grid.color": "#ddd", "grid.linewidth": 0.6,
})


def fleet_timeline() -> None:
    minutes = [t / 60 for t in range(SIM_SECONDS)]
    runs = [simulate(policy) for policy in POLICIES]
    fig, (traffic, replicas, queue) = plt.subplots(3, 1, figsize=(8.6, 7.6), sharex=True,
                                                   gridspec_kw={"height_ratios": [1, 1.6, 1.6]})
    traffic.fill_between(minutes, [arrivals_per_second(t) for t in range(SIM_SECONDS)],
                         step="post", color="#7A6528", alpha=0.35)
    traffic.set_ylabel("requests/s")
    traffic.set_title("Same traffic, three autoscaling policies")
    for run, color, style in zip(runs, COLORS, STYLES):
        replicas.step(minutes, run.ready_series, where="post", color=color, ls=style, lw=2,
                      label=run.policy.name)
        queue.plot(minutes, run.queue_series, color=color, ls=style, lw=2)
    replicas.set_ylabel("ready replicas")
    replicas.legend(loc="upper left", fontsize=9)
    queue.set_yscale("symlog", linthresh=10)
    queue.set_ylabel("requests waiting")
    queue.set_xlabel("minutes")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "autoscaling_policies_timeline.png", dpi=130)
    plt.close(fig)


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    fleet_timeline()
    print("wrote", sorted(path.name for path in OUT_DIR.glob("*.png")))


if __name__ == "__main__":
    main()
