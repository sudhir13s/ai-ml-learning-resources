"""Autoscaling a GPU inference fleet on CPU versus queue depth, simulated second by second.

A replica is one engine that batches up to 32 sequences; each chat request holds a
slot for 6 seconds; a new replica needs 150 seconds to boot. Traffic is quiet, then
steady, then spikes. Three policies face the same traffic: scale on CPU with a warm
floor, scale on queue depth with a warm floor, and scale on queue depth down to zero.
Deterministic and dependency-free, so the numbers on the page reproduce exactly.
"""
from __future__ import annotations

import math
from collections import deque
from dataclasses import dataclass, field

SIM_SECONDS = 2400
SLOTS_PER_REPLICA = 32
SERVICE_SECONDS = 6
COLD_START_SECONDS = 150
SYNC_PERIOD_SECONDS = 15
SCALE_DOWN_WINDOW_SECONDS = 300
MAX_REPLICAS = 12
TARGET_IN_FLIGHT_PER_REPLICA = 24   # 75 percent of the slots
TARGET_CPU_PERCENT = 70.0


@dataclass(frozen=True)
class Policy:
    name: str
    signal: str            # "cpu" or "queue"
    min_replicas: int


@dataclass
class Fleet:
    ready: int
    booting: deque = field(default_factory=deque)      # ready-at times
    running: deque = field(default_factory=deque)      # finish times, non-decreasing
    waiting: deque = field(default_factory=deque)      # arrival times
    below_target_since: int | None = None


@dataclass(frozen=True)
class RunResult:
    policy: Policy
    waits_s: list[int]
    ready_series: list[int]
    queue_series: list[int]
    replica_hours: float
    still_waiting: int


def arrivals_per_second(t: int) -> int:
    if t < 300:
        return 0            # overnight quiet
    if t < 900:
        return 6            # steady daytime load
    if t < 1500:
        return 30           # launch spike
    return 6


def host_cpu_percent(fleet: Fleet) -> float:
    """An engine pod's CPU barely moves with load: the GPU does the work."""
    if fleet.ready == 0:
        return 0.0
    busy_fraction = len(fleet.running) / (fleet.ready * SLOTS_PER_REPLICA)
    return 25.0 + 15.0 * busy_fraction


def desired_replicas(policy: Policy, fleet: Fleet) -> int:
    if policy.signal == "cpu":
        wanted = math.ceil(fleet.ready * host_cpu_percent(fleet) / TARGET_CPU_PERCENT)
    else:
        in_flight = len(fleet.running) + len(fleet.waiting)
        wanted = math.ceil(in_flight / TARGET_IN_FLIGHT_PER_REPLICA)
    return max(policy.min_replicas, min(MAX_REPLICAS, wanted))


def reconcile(policy: Policy, fleet: Fleet, t: int) -> None:
    """Scale up at once (new replicas still boot); scale down only after a quiet window."""
    desired = desired_replicas(policy, fleet)
    current = fleet.ready + len(fleet.booting)
    if desired > current:
        fleet.booting.extend([t + COLD_START_SECONDS] * (desired - current))
        fleet.below_target_since = None
        return
    if desired == current:
        fleet.below_target_since = None
        return
    if fleet.below_target_since is None:
        fleet.below_target_since = t
        return
    spare_slots = (fleet.ready - 1) * SLOTS_PER_REPLICA - len(fleet.running)
    if t - fleet.below_target_since >= SCALE_DOWN_WINDOW_SECONDS and spare_slots >= 0:
        fleet.ready -= 1
        fleet.below_target_since = t


def step(fleet: Fleet, t: int, waits_s: list[int]) -> None:
    while fleet.booting and fleet.booting[0] <= t:
        fleet.booting.popleft()
        fleet.ready += 1
    while fleet.running and fleet.running[0] <= t:
        fleet.running.popleft()
    fleet.waiting.extend([t] * arrivals_per_second(t))
    free_slots = fleet.ready * SLOTS_PER_REPLICA - len(fleet.running)
    while free_slots > 0 and fleet.waiting:
        waits_s.append(t - fleet.waiting.popleft())
        fleet.running.append(t + SERVICE_SECONDS)
        free_slots -= 1


def simulate(policy: Policy) -> RunResult:
    fleet = Fleet(ready=policy.min_replicas)
    waits_s: list[int] = []
    ready_series: list[int] = []
    queue_series: list[int] = []
    replica_seconds = 0
    for t in range(SIM_SECONDS):
        step(fleet, t, waits_s)
        if t % SYNC_PERIOD_SECONDS == 0:
            reconcile(policy, fleet, t)
        replica_seconds += fleet.ready + len(fleet.booting)    # booting GPUs bill too
        ready_series.append(fleet.ready)
        queue_series.append(len(fleet.waiting))
    return RunResult(policy, waits_s, ready_series, queue_series,
                     replica_seconds / 3600, len(fleet.waiting))


def percentile(values: list[int], pct: float) -> int:
    ordered = sorted(values)
    rank = max(0, math.ceil(pct / 100 * len(ordered)) - 1)
    return ordered[rank]


POLICIES = [
    Policy("CPU signal, floor 2", "cpu", 2),
    Policy("queue signal, floor 2", "queue", 2),
    Policy("queue signal, floor 0", "queue", 0),
]


def main() -> None:
    print(f"{'policy':<24}{'served':>8}{'p50 wait':>10}{'p99 wait':>10}"
          f"{'peak':>6}{'replica-h':>11}{'unserved':>10}")
    for policy in POLICIES:
        run = simulate(policy)
        print(f"{policy.name:<24}{len(run.waits_s):>8}"
              f"{percentile(run.waits_s, 50):>9}s{percentile(run.waits_s, 99):>9}s"
              f"{max(run.ready_series):>6}{run.replica_hours:>11.2f}{run.still_waiting:>10}")
    first_wait = simulate(POLICIES[2]).waits_s[0]
    print(f"\nfloor 0: the first request of the morning waited {first_wait}s for a cold start")


if __name__ == "__main__":
    main()
