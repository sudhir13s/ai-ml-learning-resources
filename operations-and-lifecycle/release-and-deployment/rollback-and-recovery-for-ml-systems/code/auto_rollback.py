"""Automated rollback loop for iris-classifier (CPU, offline, standard library only).

Replays one canary incident minute by minute. v7 opens at 5% of 10,000 requests a minute,
ramps to 25% at minute 10, and a defect that only real load exercises pushes its error
rate up 0.3 points a minute from there. The controller fires a rollback once the error rate
has stayed above the 2% service-level objective for three consecutive minutes, and the
same incident is replayed with a human who takes twenty minutes to notice and act.

Run:  uv run --python 3.12 python auto_rollback.py
"""
from __future__ import annotations

from dataclasses import dataclass

REQUESTS_PER_MINUTE = 10_000
SLO_ERROR_PCT = 2.0
BASELINE_ERROR_PCT = 0.4
ERROR_CLIMB_PER_MINUTE = 0.3
CANARY_PCT = 5
RAMPED_PCT = 25
RAMP_MINUTE = 10
BREACH_MINUTES_TO_FIRE = 3
HUMAN_RESPONSE_MINUTES = 20
SIMULATION_MINUTES = 40


@dataclass(frozen=True)
class Minute:
    minute: int
    traffic_pct: int
    error_pct: float
    event: str

    @property
    def errored_requests(self) -> float:
        return REQUESTS_PER_MINUTE * self.traffic_pct / 100 * self.error_pct / 100


@dataclass(frozen=True)
class Incident:
    policy: str
    timeline: tuple[Minute, ...]
    first_breach_minute: int
    rollback_minute: int

    @property
    def errored_requests(self) -> float:
        return sum(minute.errored_requests for minute in self.timeline)


def v7_error_pct(minute: int) -> float:
    """v7's error rate: flat at baseline until the ramp, then climbing under load."""
    if minute < RAMP_MINUTE:
        return BASELINE_ERROR_PCT
    return round(BASELINE_ERROR_PCT + ERROR_CLIMB_PER_MINUTE * (minute - RAMP_MINUTE), 2)


def scheduled_traffic_pct(minute: int) -> int:
    return CANARY_PCT if minute < RAMP_MINUTE else RAMPED_PCT


def replay(policy: str, human_delay_minutes: int | None) -> Incident:
    """Replay the incident. None means the controller acts; a number means a human does."""
    timeline: list[Minute] = []
    consecutive_breaches = 0
    first_breach = rollback_at = -1
    for minute in range(SIMULATION_MINUTES):
        if rollback_at >= 0:
            timeline.append(Minute(minute, 0, 0.0, "v6 serves everyone"))
            continue
        traffic = scheduled_traffic_pct(minute)
        error = v7_error_pct(minute)
        is_breach = error > SLO_ERROR_PCT
        consecutive_breaches = consecutive_breaches + 1 if is_breach else 0
        if is_breach and first_breach < 0:
            first_breach = minute
        event = "ramp 5% -> 25%" if minute == RAMP_MINUTE else ""
        if is_breach:
            event = f"over SLO ({consecutive_breaches} in a row)"
        fires_automatically = (human_delay_minutes is None
                               and consecutive_breaches == BREACH_MINUTES_TO_FIRE)
        human_acts = (human_delay_minutes is not None and first_breach >= 0
                      and minute == first_breach + human_delay_minutes)
        if fires_automatically or human_acts:
            rollback_at = minute
            event = "ROLLBACK: v7 weight -> 0%"
        timeline.append(Minute(minute, traffic, error, event))
    return Incident(policy, tuple(timeline), first_breach, rollback_at)


def print_event_log(incident: Incident) -> None:
    print(f"\n== {incident.policy} ==")
    print(f"{'min':>3} | {'v7 traffic':>10} | {'v7 error':>8} | event")
    print("-" * 56)
    last_listed_breach = incident.first_breach_minute + BREACH_MINUTES_TO_FIRE - 1
    has_elided = False
    for minute in incident.timeline:
        if not minute.event or minute.event == "v6 serves everyone":
            continue
        is_repeat_breach = (minute.event.startswith("over SLO")
                            and minute.minute > last_listed_breach)
        if is_repeat_breach:
            if not has_elided:
                print("... | still over SLO, still serving 25% ...")
                has_elided = True
            continue
        print(f"{minute.minute:>3} | {minute.traffic_pct:>9}% | "
              f"{minute.error_pct:>7.1f}% | {minute.event}")
    detection = incident.rollback_minute - incident.first_breach_minute
    print(f"first breach at minute {incident.first_breach_minute}, rollback at minute "
          f"{incident.rollback_minute} ({detection} min later); "
          f"errored requests served by v7: {incident.errored_requests:,.0f}")


def main() -> None:
    automated = replay("automated trigger: 3 consecutive minutes over SLO", None)
    human = replay(f"human on call: acts {HUMAN_RESPONSE_MINUTES} min after first breach",
                   HUMAN_RESPONSE_MINUTES)
    print(f"traffic {REQUESTS_PER_MINUTE:,} req/min   SLO: error rate <= {SLO_ERROR_PCT}%   "
          f"canary {CANARY_PCT}% -> {RAMPED_PCT}% at minute {RAMP_MINUTE}")
    print_event_log(automated)
    print_event_log(human)
    ratio = human.errored_requests / automated.errored_requests
    print(f"\nwaiting for a human cost {ratio:.1f}x the errored requests of the automated trigger")


if __name__ == "__main__":
    main()
