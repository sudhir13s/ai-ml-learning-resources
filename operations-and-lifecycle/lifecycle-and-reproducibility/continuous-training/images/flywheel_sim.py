"""Simulated data flywheel (CPU, offline, deterministic).

We train a baseline classifier, then let the *world* drift week by week (the
decision boundary slowly rotates). Each week we measure live accuracy on fresh
production traffic. A drift monitor watches accuracy; when it crosses a
threshold it fires a RETRAIN trigger. We then retrain on freshly-collected,
freshly-labeled production data and measure how much accuracy recovers.

The whole point: a *static* model decays as the world moves; a *retraining
flywheel* keeps snapping it back. Same drift, two policies, side by side.
"""
import numpy as np
from sklearn.linear_model import LogisticRegression

RNG = np.random.default_rng(0)          # deterministic
N_PER_WEEK = 1500                        # production samples per week
WEEKS = 12
DRIFT_PER_WEEK = 0.18                    # radians the world rotates each week
RETRAIN_THRESHOLD = 0.85                 # accuracy floor that triggers retrain


def make_week(week: int, n: int = N_PER_WEEK):
    """Two Gaussian blobs whose separating axis ROTATES as weeks pass.

    Week 0 is the world the baseline was trained on. Later weeks rotate the
    class geometry by `DRIFT_PER_WEEK` radians/week => covariate + concept drift.
    """
    theta = DRIFT_PER_WEEK * week
    rot = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta),  np.cos(theta)]])
    y = RNG.integers(0, 2, size=n)
    centers = np.array([[-1.4, 0.0], [1.4, 0.0]])
    X = RNG.normal(0.0, 1.0, size=(n, 2)) + centers[y]
    X = X @ rot.T                         # rotate the whole world
    return X, y


def accuracy(model, X, y):
    return float((model.predict(X) == y).mean())


def main():
    # --- Baseline: train once on week 0, the "launch" distribution ----------
    X0, y0 = make_week(0)
    baseline = LogisticRegression().fit(X0, y0)

    # The retraining flywheel keeps its own model + a buffer of recent labels.
    flywheel = LogisticRegression().fit(X0, y0)

    print(f"{'week':>4} | {'static acc':>10} | {'flywheel acc':>12} | event")
    print("-" * 56)

    static_hist, flywheel_hist, retrains = [], [], []
    for week in range(WEEKS):
        Xw, yw = make_week(week)                       # this week's live traffic

        acc_static = accuracy(baseline, Xw, yw)        # frozen model, never updated
        acc_fly = accuracy(flywheel, Xw, yw)           # flywheel model BEFORE any retrain

        event = ""
        # --- Drift monitor: performance-triggered retrain -------------------
        if week > 0 and acc_fly < RETRAIN_THRESHOLD:
            # Collect + label this week's data, refit on the fresh window.
            flywheel = LogisticRegression().fit(Xw, yw)
            acc_fly_after = accuracy(flywheel, Xw, yw)  # recovery on same week
            retrains.append(week)
            event = f"RETRAIN (acc {acc_fly:.3f} -> {acc_fly_after:.3f})"
            acc_fly = acc_fly_after                      # report post-retrain acc

        static_hist.append(acc_static)
        flywheel_hist.append(acc_fly)
        print(f"{week:>4} | {acc_static:>10.3f} | {acc_fly:>12.3f} | {event}")

    print("-" * 56)
    print(f"retrains fired on weeks : {retrains}")
    print(f"static  mean acc        : {np.mean(static_hist):.3f}")
    print(f"flywheel mean acc       : {np.mean(flywheel_hist):.3f}")
    print(f"final static acc        : {static_hist[-1]:.3f}")
    print(f"final flywheel acc      : {flywheel_hist[-1]:.3f}")
    return static_hist, flywheel_hist, retrains


if __name__ == "__main__":
    main()
