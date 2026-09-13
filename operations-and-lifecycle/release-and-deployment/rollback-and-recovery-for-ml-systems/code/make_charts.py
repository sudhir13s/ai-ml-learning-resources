"""Generate the rollback timeline chart from the same replay auto_rollback.py prints.

Run:  uv run --python ~/.uv/envs/ml-py312/bin/python make_charts.py
Writes ../images/rollback_timeline.png (muted palette, light background).
"""
from __future__ import annotations

import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from auto_rollback import HUMAN_RESPONSE_MINUTES, SLO_ERROR_PCT, replay  # noqa: E402

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images")
BLUE, GREEN, RED, AMBER, GREY = "#3A6B96", "#2E7A5A", "#8B3B4A", "#7A6528", "#4A5B6E"

plt.rcParams.update({
    "figure.facecolor": "white", "axes.facecolor": "white",
    "axes.edgecolor": "#888", "axes.labelcolor": "#222",
    "xtick.color": "#222", "ytick.color": "#222", "text.color": "#222",
    "font.size": 11, "axes.grid": True, "grid.color": "#ddd", "grid.linewidth": 0.6,
})


def series(incident):
    minutes = [m.minute for m in incident.timeline]
    traffic = [m.traffic_pct for m in incident.timeline]
    errors = [m.error_pct if m.traffic_pct else float("nan") for m in incident.timeline]
    return minutes, traffic, errors


def chart_rollback_timeline() -> None:
    automated = replay("automated", None)
    human = replay("human", HUMAN_RESPONSE_MINUTES)
    minutes, auto_traffic, auto_errors = series(automated)
    _, human_traffic, human_errors = series(human)

    fig, (top, bottom) = plt.subplots(2, 1, figsize=(8.2, 5.8), sharex=True,
                                      gridspec_kw={"height_ratios": [1, 1.15]})
    top.step(minutes, human_traffic, where="post", color=GREY, lw=2.0, ls="--",
             label=f"human acts after {HUMAN_RESPONSE_MINUTES} min")
    top.step(minutes, auto_traffic, where="post", color=BLUE, lw=2.6,
             label="automated trigger")
    top.set_ylabel("v7 share of traffic (%)")
    top.set_ylim(-2, 32)
    top.set_yticks([0, 5, 25])
    top.set_title("One incident, two rollback policies")
    top.legend(loc="upper right", frameon=True, fontsize=9)

    bottom.plot(minutes, human_errors, color=GREY, lw=2.0, ls="--")
    bottom.plot(minutes, auto_errors, color=RED, lw=2.6, label="v7 error rate")
    bottom.axhline(SLO_ERROR_PCT, color=AMBER, lw=2.0, ls=":", label="SLO (2%)")
    bottom.axvspan(automated.first_breach_minute, automated.rollback_minute,
                   color=RED, alpha=0.10)
    bottom.annotate("3 minutes over SLO\n-> rollback at minute 18",
                    xy=(automated.rollback_minute, 2.8), xytext=(21, 1.0), color=RED,
                    fontsize=9, arrowprops=dict(arrowstyle="->", color=RED, lw=1.2))
    bottom.annotate("human rollback\nat minute 36", xy=(human.rollback_minute, 8.2),
                    xytext=(27, 8.0), color=GREY, fontsize=9,
                    arrowprops=dict(arrowstyle="->", color=GREY, lw=1.2))
    bottom.set_ylabel("v7 error rate (%)")
    bottom.set_xlabel("minutes since the canary opened")
    bottom.set_ylim(0, 9.5)
    bottom.legend(loc="upper left", frameon=True, fontsize=9)
    fig.tight_layout()
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "rollback_timeline.png")
    fig.savefig(path, dpi=130)
    plt.close(fig)
    print("wrote", os.path.normpath(path))


if __name__ == "__main__":
    chart_rollback_timeline()
