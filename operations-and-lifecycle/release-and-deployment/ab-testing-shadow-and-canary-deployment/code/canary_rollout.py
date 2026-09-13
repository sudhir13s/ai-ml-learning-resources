"""Canary rollout controller for iris-classifier (CPU, offline, standard library only).

Routes 10,000 requests a minute between the production model (v6) and a candidate by a
stable hash of the request key, ramps the candidate through 5% -> 25% -> 50% -> 100% with
a ten-minute bake at each stage, and aborts to 0% the first minute the candidate's error
rate breaches the 2% service-level objective. A healthy and a broken candidate run through
the same schedule so the blast radius of each outcome can be counted, not estimated.

Run:  uv run --python 3.12 python canary_rollout.py
"""
from __future__ import annotations

import hashlib
import random
from dataclasses import dataclass

REQUESTS_PER_MINUTE = 10_000
ERROR_RATE_SLO = 0.02
FULL_TRAFFIC_PCT = 100
HASH_BITS = 53


@dataclass(frozen=True)
class Stage:
    """One rung of the ramp: the candidate's traffic share and how long it must stay green."""

    traffic_pct: int
    bake_minutes: int


STAGES = (Stage(5, 10), Stage(25, 10), Stage(50, 10), Stage(FULL_TRAFFIC_PCT, 0))


@dataclass(frozen=True)
class Candidate:
    name: str
    error_probability: float


@dataclass(frozen=True)
class MinuteReport:
    minute: int
    traffic_pct: int
    candidate_requests: int
    candidate_errors: int

    @property
    def error_rate(self) -> float:
        return self.candidate_errors / max(self.candidate_requests, 1)


@dataclass(frozen=True)
class RolloutResult:
    candidate: Candidate
    is_promoted: bool
    minutes: tuple[MinuteReport, ...]

    @property
    def errored_requests(self) -> int:
        return sum(report.candidate_errors for report in self.minutes)


def stable_fraction(key: str, salt: str = "iris-v7-rollout") -> float:
    """Map a request key to a uniform number in [0, 1) that every replica agrees on."""
    digest = hashlib.blake2b(f"{salt}:{key}".encode(), digest_size=8).digest()
    return (int.from_bytes(digest, "big") >> (64 - HASH_BITS)) / float(1 << HASH_BITS)


def routes_to_candidate(key: str, traffic_pct: int) -> bool:
    return stable_fraction(key) < traffic_pct / 100


def serve_one_minute(minute: int, stage: Stage, candidate: Candidate,
                     rng: random.Random) -> MinuteReport:
    candidate_requests = 0
    candidate_errors = 0
    for request_index in range(REQUESTS_PER_MINUTE):
        if not routes_to_candidate(f"req-{minute}-{request_index}", stage.traffic_pct):
            continue
        candidate_requests += 1
        if rng.random() < candidate.error_probability:
            candidate_errors += 1
    return MinuteReport(minute, stage.traffic_pct, candidate_requests, candidate_errors)


def simulate_rollout(candidate: Candidate, seed: int = 0) -> RolloutResult:
    """Walk the ramp minute by minute; abort the moment one minute breaches the SLO."""
    rng = random.Random(seed)
    reports: list[MinuteReport] = []
    minute = 0
    for stage in STAGES:
        if stage.traffic_pct == FULL_TRAFFIC_PCT:
            return RolloutResult(candidate, True, tuple(reports))
        for _ in range(stage.bake_minutes):
            report = serve_one_minute(minute, stage, candidate, rng)
            reports.append(report)
            minute += 1
            if report.error_rate >= ERROR_RATE_SLO:
                return RolloutResult(candidate, False, tuple(reports))
    return RolloutResult(candidate, True, tuple(reports))


def print_rollout(result: RolloutResult) -> None:
    print(f"\n== {result.candidate.name} (true error rate "
          f"{result.candidate.error_probability:.1%}) ==")
    print(f"{'stage':>6} | {'minutes':>7} | {'req/min on candidate':>20} | "
          f"{'worst minute':>12} | decision")
    print("-" * 72)
    for stage in STAGES[:-1]:
        stage_reports = [r for r in result.minutes if r.traffic_pct == stage.traffic_pct]
        if not stage_reports:
            break
        mean_requests = sum(r.candidate_requests for r in stage_reports) / len(stage_reports)
        worst = max(stage_reports, key=lambda r: r.error_rate)
        breached = worst.error_rate >= ERROR_RATE_SLO
        decision = "ABORT -> route 0%" if breached else "green -> advance"
        print(f"{stage.traffic_pct:>5}% | {len(stage_reports):>7} | {mean_requests:>20.0f} | "
              f"{worst.error_rate:>11.2%} | {decision}")
    outcome = "PROMOTED to 100%" if result.is_promoted else "ABORTED"
    print(f"outcome: {outcome} after {len(result.minutes)} min; "
          f"errored requests served by the candidate: {result.errored_requests}")


def main() -> None:
    healthy = simulate_rollout(Candidate("iris-classifier:v7", error_probability=0.004))
    broken = simulate_rollout(Candidate("iris-classifier:v8", error_probability=0.08))
    print(f"traffic: {REQUESTS_PER_MINUTE:,} req/min   SLO: candidate error rate "
          f"< {ERROR_RATE_SLO:.0%}   ramp: 5 -> 25 -> 50 -> 100% (10-min bakes)")
    print_rollout(healthy)
    print_rollout(broken)

    minutes_exposed = len(broken.minutes)
    straight_to_full = REQUESTS_PER_MINUTE * broken.candidate.error_probability * minutes_exposed
    print(f"\nblast radius of v8: canary {broken.errored_requests} errored requests vs "
          f"{straight_to_full:.0f} if shipped straight to 100% for the same "
          f"{minutes_exposed} min ({straight_to_full / broken.errored_requests:.0f}x)")

    user_keys = [f"user-{index}" for index in range(REQUESTS_PER_MINUTE)]
    on_at_5 = {key for key in user_keys if routes_to_candidate(key, 5)}
    on_at_25 = {key for key in user_keys if routes_to_candidate(key, 25)}
    print(f"sticky ramp: {len(on_at_5)} users on v7 at 5%, {len(on_at_25)} at 25%; "
          f"every 5% user still on v7 at 25%? {on_at_5 <= on_at_25}")


if __name__ == "__main__":
    main()
