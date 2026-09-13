"""Generate label_lag_lead_time.png: what a monitor can see, and when.

A 1-D fraud score model is trained on day 0 with decision threshold 0. From day 30
the world drifts: the input mean moves right AND the true boundary moves with it,
so accuracy decays. We compare two ways of noticing:

  * input PSI against the frozen day-0 reference, visible the same day
  * labelled accuracy, visible only after a 60-day chargeback lag

Run: uv run --python 3.12 --with numpy --with matplotlib python make_label_lag_chart.py
"""
import os

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SEED = 0
DAYS = 150
DRIFT_START = 30
DRIFT_PER_DAY = 0.012      # standard deviations the world moves per day
WINDOW = 2_000             # scored transactions per day
LABEL_LAG = 60             # chargeback cycle in days
PSI_ACT = 0.2
ACCURACY_FLOOR = 0.85
LABEL_NOISE = 0.25

C_PROC = "#5D4A8A"
C_DANGER = "#8B3B4A"
C_WARN = "#7D5A2C"
C_OK = "#2E7A5A"
C_FROZEN = "#4A5B6E"


def psi(reference: np.ndarray, production: np.ndarray, bins: int = 10) -> float:
    edges = np.quantile(reference, np.linspace(0, 1, bins + 1))
    edges[0], edges[-1] = -np.inf, np.inf
    ref_share = np.clip(np.histogram(reference, edges)[0] / reference.size, 1e-6, None)
    prod_share = np.clip(np.histogram(production, edges)[0] / production.size, 1e-6, None)
    return float(np.sum((prod_share - ref_share) * np.log(prod_share / ref_share)))


def simulate(rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    reference = rng.normal(0.0, 1.0, 20_000)
    psi_series, accuracy_series = [], []
    for day in range(DAYS):
        drift = max(0, day - DRIFT_START) * DRIFT_PER_DAY
        scores = rng.normal(drift, 1.0, WINDOW)
        truth = (scores + rng.normal(0.0, LABEL_NOISE, WINDOW)) > drift
        predicted = scores > 0.0
        psi_series.append(psi(reference, scores))
        accuracy_series.append(float(np.mean(predicted == truth)))
    return np.array(psi_series), np.array(accuracy_series)


def main() -> None:
    rng = np.random.default_rng(SEED)
    psi_series, accuracy_series = simulate(rng)
    days = np.arange(DAYS)
    psi_alert_day = int(days[np.argmax(psi_series > PSI_ACT)])
    floor_breach_day = int(days[np.argmax(accuracy_series < ACCURACY_FLOOR)])
    label_confirm_day = floor_breach_day + LABEL_LAG

    fig, acc_axis = plt.subplots(figsize=(9.6, 4.6))
    acc_axis.plot(days, accuracy_series, color=C_OK, linewidth=2.0, label="true accuracy (unknown on the day)")
    visible = days + LABEL_LAG < DAYS
    acc_axis.plot(days[visible] + LABEL_LAG, accuracy_series[visible], color=C_OK, linestyle=":",
                  linewidth=2.0, label=f"accuracy as labels reveal it ({LABEL_LAG}-day lag)")
    acc_axis.axhline(ACCURACY_FLOOR, color=C_FROZEN, linestyle="--", linewidth=1.3)
    acc_axis.set_ylabel("Accuracy")
    acc_axis.set_xlabel("Day in production")
    acc_axis.set_ylim(0.55, 0.98)

    psi_axis = acc_axis.twinx()
    psi_axis.plot(days, psi_series, color=C_PROC, linewidth=1.8, label="input PSI (visible same day)")
    psi_axis.axhline(PSI_ACT, color=C_PROC, linestyle="--", linewidth=1.1)
    psi_axis.set_ylabel("PSI")
    psi_axis.set_ylim(0, max(0.8, psi_series.max() * 1.05))

    acc_axis.axvspan(psi_alert_day, label_confirm_day, color=C_WARN, alpha=0.12)
    acc_axis.axvline(psi_alert_day, color=C_PROC, linewidth=1.4)
    acc_axis.axvline(label_confirm_day, color=C_DANGER, linewidth=1.4)
    label_box = {"facecolor": "white", "edgecolor": "none", "alpha": 0.9, "pad": 2}
    acc_axis.text(psi_alert_day + 1, 0.885, f"PSI > 0.2\nday {psi_alert_day}", color=C_PROC,
                  fontsize=9, fontweight="bold", bbox=label_box, zorder=5)
    acc_axis.text(label_confirm_day + 1, 0.885, f"labels confirm\nday {label_confirm_day}", color=C_DANGER,
                  fontsize=9, fontweight="bold", bbox=label_box, zorder=5)
    acc_axis.text(floor_breach_day - 1, 0.60, f"true accuracy < 0.85\nday {floor_breach_day} (unseen)",
                  color=C_OK, fontsize=8.5, ha="right", bbox=label_box, zorder=5)
    acc_axis.text((psi_alert_day + label_confirm_day) / 2, 0.955,
                  f"{label_confirm_day - psi_alert_day} days of lead time", ha="center",
                  color=C_WARN, fontsize=10, fontweight="bold")
    acc_axis.set_title("The drift signal arrives weeks before the labels do")
    for spine in ("top",):
        acc_axis.spines[spine].set_visible(False)
        psi_axis.spines[spine].set_visible(False)
    lines = acc_axis.get_legend_handles_labels()
    more = psi_axis.get_legend_handles_labels()
    acc_axis.legend(lines[0] + more[0], lines[1] + more[1], loc="center left", fontsize=8.5)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "label_lag_lead_time.png"), bbox_inches="tight")
    plt.close(fig)

    print(f"accuracy day 0-29 mean: {accuracy_series[:DRIFT_START].mean():.3f}")
    print(f"PSI first > {PSI_ACT}: day {psi_alert_day} (PSI {psi_series[psi_alert_day]:.3f}, "
          f"accuracy {accuracy_series[psi_alert_day]:.3f})")
    print(f"accuracy first < {ACCURACY_FLOOR}: day {floor_breach_day}")
    print(f"labels confirm the breach: day {label_confirm_day}")
    print(f"lead time: {label_confirm_day - psi_alert_day} days")


if __name__ == "__main__":
    main()
