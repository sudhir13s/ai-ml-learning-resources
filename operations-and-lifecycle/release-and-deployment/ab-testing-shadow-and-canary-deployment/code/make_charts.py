"""Generate the charts for the A/B, shadow and canary page.

Run:  uv run --python ~/.uv/envs/ml-py312/bin/python make_charts.py
Writes to ../images (muted palette, light background):
  canary_traffic.png           - replayed from canary_rollout.simulate_rollout (real numbers)
  mlops_strategy_compare.png   - illustrative relative scores for five rollout strategies
"""
from __future__ import annotations

import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canary_rollout import Candidate, simulate_rollout  # noqa: E402

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images")
GREEN, RED, AMBER = "#2E7A5A", "#8B3B4A", "#7A6528"
PROMOTED_HOLD_MINUTES = 10

plt.rcParams.update({
    "figure.facecolor": "white", "axes.facecolor": "white",
    "axes.edgecolor": "#888", "axes.labelcolor": "#222",
    "xtick.color": "#222", "ytick.color": "#222", "text.color": "#222",
    "font.size": 11, "axes.grid": True, "grid.color": "#ddd", "grid.linewidth": 0.6,
})


def traffic_series(result):
    minutes = [report.minute for report in result.minutes]
    traffic = [report.traffic_pct for report in result.minutes]
    end = len(result.minutes)
    final_pct = 100 if result.is_promoted else 0
    hold = PROMOTED_HOLD_MINUTES if result.is_promoted else 40 - end
    minutes += list(range(end, end + hold + 1))
    traffic += [final_pct] * (hold + 1)
    return minutes, traffic


def save(fig, name: str) -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, name)
    fig.savefig(path, dpi=130)
    plt.close(fig)
    print("wrote", os.path.normpath(path))


def chart_canary_traffic() -> None:
    healthy = simulate_rollout(Candidate("iris-classifier:v7", 0.004))
    broken = simulate_rollout(Candidate("iris-classifier:v8", 0.08))
    healthy_minutes, healthy_traffic = traffic_series(healthy)
    broken_minutes, broken_traffic = traffic_series(broken)

    fig, ax = plt.subplots(figsize=(7.8, 4.4))
    ax.step(healthy_minutes, healthy_traffic, where="post", color=GREEN, lw=2.6,
            label="v7 healthy: promoted")
    ax.fill_between(healthy_minutes, 0, healthy_traffic, step="post", color=GREEN, alpha=0.08)
    ax.step(broken_minutes, broken_traffic, where="post", color=RED, lw=2.6,
            label="v8 broken: aborted")
    ax.set_xlabel("minutes since the canary opened")
    ax.set_ylabel("% of live traffic on the candidate")
    ax.set_title("Canary ramp: advance on green, snap to 0% on the first breach")
    ax.set_ylim(-4, 108)
    ax.set_yticks([0, 5, 25, 50, 100])
    ax.legend(loc="lower right", bbox_to_anchor=(1.0, 0.08), frameon=True)
    ax.annotate("v8: 8.3% errors in its\nfirst 5% minute -> abort", xy=(1, 4), xytext=(4, 38),
                color=RED, fontsize=9, arrowprops=dict(arrowstyle="->", color=RED, lw=1.3))
    ax.annotate("each step = a 10-minute\nbake that must stay green", xy=(20, 50),
                xytext=(2, 72), color=GREEN, fontsize=9,
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.3))
    fig.tight_layout()
    save(fig, "canary_traffic.png")


def chart_strategy_compare() -> None:
    """Illustrative 0-10 scores, chosen to make the trade-offs visible at a glance."""
    strategies = ["Recreate", "Rolling", "Blue-Green", "Canary", "Shadow"]
    blast = np.array([10, 6, 4, 2, 0])
    cost = np.array([1, 2, 8, 4, 6])
    speed = np.array([2, 4, 10, 8, 10])

    x = np.arange(len(strategies))
    width = 0.26
    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    ax.bar(x - width, blast, width, color=RED, label="blast radius if bad (lower=safer)")
    ax.bar(x, cost, width, color=AMBER, label="extra infra cost")
    ax.bar(x + width, speed, width, color=GREEN, label="rollback speed (higher=faster)")
    ax.set_xticks(x)
    ax.set_xticklabels(strategies)
    ax.set_ylabel("relative score (0-10)")
    ax.set_title("Deployment strategies: safety vs cost vs rollback speed")
    ax.set_ylim(0, 13)
    ax.legend(loc="upper center", ncol=3, frameon=True, fontsize=8.5)
    fig.tight_layout()
    save(fig, "mlops_strategy_compare.png")


if __name__ == "__main__":
    chart_canary_traffic()
    chart_strategy_compare()
