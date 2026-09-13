"""Deployment gate for iris-classifier (CPU, offline, standard library only).

A candidate may advance to the canary only if it clears three checks against the model
currently in production, both measured on the same holdout: an absolute accuracy floor,
no regression beyond a small budget, and a p95 latency budget. Every failed check is
reported, and each verdict carries the exit code a CI job returns (0 promotes, 1 blocks).

Run:  uv run --python 3.12 python deploy_gate.py
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field

PROMOTE_EXIT_CODE = 0
BLOCK_EXIT_CODE = 1


@dataclass(frozen=True)
class GatePolicy:
    """The promotion contract. It lives in the repository, so changing the bar is a
    reviewed pull request rather than a message in a chat channel."""

    min_accuracy: float = 0.90
    max_regression: float = 0.01
    max_p95_latency_ms: float = 150.0


@dataclass(frozen=True)
class EvalReport:
    """What the offline evaluation job measures for one model version on the holdout."""

    name: str
    accuracy: float
    p95_latency_ms: float


@dataclass(frozen=True)
class GateVerdict:
    """The machine-readable decision CI keys off."""

    candidate: str
    production: str
    checks: dict[str, dict[str, float | bool]]
    reasons: list[str] = field(default_factory=list)

    @property
    def is_promoted(self) -> bool:
        return not self.reasons

    def to_json(self) -> str:
        return json.dumps({
            "candidate": self.candidate,
            "prod": self.production,
            "checks": self.checks,
            "decision": "PROMOTE" if self.is_promoted else "BLOCK",
            "reasons": self.reasons,
            "exit_code": PROMOTE_EXIT_CODE if self.is_promoted else BLOCK_EXIT_CODE,
        })


def evaluate_gate(candidate: EvalReport, production: EvalReport,
                  policy: GatePolicy) -> GateVerdict:
    """Run every check and collect every failure, not just the first one."""
    clears_floor = candidate.accuracy >= policy.min_accuracy
    allowed_accuracy = production.accuracy - policy.max_regression
    has_no_regression = candidate.accuracy >= allowed_accuracy
    fits_latency = candidate.p95_latency_ms <= policy.max_p95_latency_ms

    reasons = []
    if not clears_floor:
        reasons.append(f"accuracy {candidate.accuracy:.3f} < floor {policy.min_accuracy:.3f}")
    if not has_no_regression:
        reasons.append(f"regression: {candidate.accuracy:.3f} vs prod "
                       f"{production.accuracy:.3f} (allowed drop {policy.max_regression:.3f})")
    if not fits_latency:
        reasons.append(f"p95 latency {candidate.p95_latency_ms:.0f}ms > budget "
                       f"{policy.max_p95_latency_ms:.0f}ms")

    checks = {
        "floor": {"acc": candidate.accuracy, "min": policy.min_accuracy, "pass": clears_floor},
        "no_regression": {"acc": candidate.accuracy, "prod_acc": production.accuracy,
                          "allowed_drop": policy.max_regression, "pass": has_no_regression},
        "latency": {"p95_ms": candidate.p95_latency_ms,
                    "budget_ms": policy.max_p95_latency_ms, "pass": fits_latency},
    }
    return GateVerdict(candidate.name, production.name, checks, reasons)


def main() -> None:
    policy = GatePolicy()
    production = EvalReport("iris-classifier:v6", accuracy=0.92, p95_latency_ms=115)
    candidates = [
        EvalReport("iris-classifier:v7", accuracy=0.94, p95_latency_ms=120),
        EvalReport("iris-classifier:v8", accuracy=0.95, p95_latency_ms=210),
        EvalReport("iris-classifier:v9", accuracy=0.90, p95_latency_ms=110),
        EvalReport("iris-classifier:v10", accuracy=0.88, p95_latency_ms=100),
    ]

    print(f"policy: acc>={policy.min_accuracy}  max_regression={policy.max_regression}  "
          f"p95<={policy.max_p95_latency_ms:.0f}ms   (prod {production.name} "
          f"acc={production.accuracy})\n")
    print(f"{'candidate':<22}{'acc':>6}{'p95(ms)':>9}  decision")
    print("-" * 62)
    verdicts = [evaluate_gate(candidate, production, policy) for candidate in candidates]
    for candidate, verdict in zip(candidates, verdicts):
        decision = "PROMOTE" if verdict.is_promoted else "BLOCK"
        print(f"{candidate.name:<22}{candidate.accuracy:>6.2f}"
              f"{candidate.p95_latency_ms:>9.0f}  {decision}")
        for reason in verdict.reasons:
            print(f"{'':<37}- {reason}")

    print("\nverdicts as CI sees them (one JSON line per candidate):")
    for verdict in verdicts:
        print(verdict.to_json())


if __name__ == "__main__":
    main()
