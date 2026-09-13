"""A PPO-with-KL-leash step you can run on a CPU in seconds, in plain PyTorch.

The teaching toy behind the "running alignment" chapter of the preference-alignment page.
It keeps exactly the load-bearing pieces of PPO-RLHF and removes everything else:

  * a tiny one-step "language model" policy (prompt token -> next-token distribution);
  * a frozen reference, snapshotted from the policy before training (the SFT model's role);
  * a hand-coded reward that prefers the SAFE answer token (+1) over anything else (0) --
    a stand-in for a trained reward model;
  * a running-mean baseline, so advantage = reward - baseline (a stand-in for the critic);
  * the clipped surrogate min(ratio*A, clip(ratio, 1-eps, 1+eps)*A), re-used for several
    epochs per rollout batch so the ratio actually moves away from 1 and the clip can bind;
  * the KL-to-reference penalty beta * KL(pi || pi_ref), computed exactly over the vocabulary.

What the script proves, printed:

  1. The clipped-step arithmetic from the main page (A = +0.60, ratio = 1.40, eps = 0.2)
     comes out of the same `clipped_surrogate` function the training loop uses: 0.72.
  2. A training trace for beta = 0.02: mean reward climbs and P(safe) goes to ~1.
  3. A beta sweep checked against the closed-form optimum of the KL-regularized objective,
     pi*(y) = pi_ref(y) * exp(r(y) / beta) / Z. PPO lands on that optimum -- the same
     boxed result the DPO derivation starts from.

Run (CPU, no downloads):
    python ppo_toy.py
"""

from __future__ import annotations

import copy
import math

import torch
import torch.nn as nn
import torch.nn.functional as F

SEED = 0
VOCAB_SIZE = 16
HIDDEN_SIZE = 32
PROMPT_TOKEN, SAFE_TOKEN = 1, 7
CLIP_EPSILON = 0.2
LEARNING_RATE = 5e-3
GROUP_SIZE = 64          # rollouts sampled per step
PPO_EPOCHS = 4           # optimizer passes over each rollout batch (why the clip can bind)
BASELINE_MOMENTUM = 0.2  # running-mean baseline: a toy stand-in for the value model
TRACE_BETA = 0.02
TRACE_STEPS = 60
TRACE_LOG_STEPS = (1, 10, 20, 40, 60)
SWEEP_BETAS = (0.5, 1.0, 2.0)
SWEEP_STEPS = 600


class TinyPolicy(nn.Module):
    """A one-step language model: a prompt token in, next-token logits out."""

    def __init__(self, vocab_size: int, hidden_size: int) -> None:
        super().__init__()
        self.embed = nn.Embedding(vocab_size, hidden_size)
        self.head = nn.Sequential(
            nn.Linear(hidden_size, hidden_size), nn.Tanh(), nn.Linear(hidden_size, vocab_size)
        )

    def forward(self, prompt_ids: torch.Tensor) -> torch.Tensor:
        return self.head(self.embed(prompt_ids))  # [B] -> [B, V]


def clipped_surrogate(
    new_log_probs: torch.Tensor, old_log_probs: torch.Tensor, advantages: torch.Tensor, epsilon: float
) -> tuple[torch.Tensor, float]:
    """PPO's pessimistic surrogate, averaged over rollouts, plus the fraction that got clipped."""
    ratio = torch.exp(new_log_probs - old_log_probs)                # pi_new / pi_old per rollout
    unclipped = ratio * advantages
    clipped = torch.clamp(ratio, 1 - epsilon, 1 + epsilon) * advantages
    clip_fraction = ((ratio - 1).abs() > epsilon).float().mean().item()
    return torch.min(unclipped, clipped).mean(), clip_fraction


def show_clipped_step_arithmetic() -> None:
    """Reproduce the main page's worked clipped step with the training loop's own function."""
    advantage = torch.tensor([1.0 - 0.40])                          # reward 1.0 minus baseline 0.40
    old_log_prob = torch.tensor([math.log(0.10)])
    new_log_prob = torch.tensor([math.log(0.14)])                   # 40% more likely: ratio 1.40
    surrogate, _ = clipped_surrogate(new_log_prob, old_log_prob, advantage, CLIP_EPSILON)
    ratio = math.exp((new_log_prob - old_log_prob).item())
    print("Clipped-step arithmetic (eps = 0.2):")
    print(f"  advantage = {advantage.item():+.2f}   ratio = {ratio:.2f}")
    print(f"  unclipped = {ratio * advantage.item():.2f}   clipped = {1.2 * advantage.item():.2f}"
          f"   surrogate = min = {surrogate.item():.2f}")


def exact_kl(log_probs: torch.Tensor, ref_log_probs: torch.Tensor) -> torch.Tensor:
    """KL(pi || pi_ref) summed over the whole vocabulary (exact, no sampling)."""
    return (log_probs.exp() * (log_probs - ref_log_probs)).sum()


def run_ppo(beta: float, steps: int, log_steps: tuple[int, ...] = ()) -> tuple[float, float, float]:
    """Train the toy policy with clipped PPO + KL leash; return (P_ref(safe), P(safe), KL)."""
    torch.manual_seed(SEED)
    policy = TinyPolicy(VOCAB_SIZE, HIDDEN_SIZE)
    reference = copy.deepcopy(policy).requires_grad_(False)         # snapshot BEFORE training
    optimizer = torch.optim.Adam(policy.parameters(), lr=LEARNING_RATE)
    prompt = torch.tensor([PROMPT_TOKEN])
    with torch.no_grad():
        ref_log_probs = F.log_softmax(reference(prompt), dim=-1)[0]  # [V]
    baseline = 0.0
    for step in range(1, steps + 1):
        with torch.no_grad():                                       # rollouts from the current policy
            old_log_probs = F.log_softmax(policy(prompt), dim=-1)[0]
            actions = torch.multinomial(old_log_probs.exp(), GROUP_SIZE, replacement=True)  # [G]
            rewards = (actions == SAFE_TOKEN).float()                                       # [G]
            advantages = rewards - baseline
            baseline += BASELINE_MOMENTUM * (rewards.mean().item() - baseline)
        for _ in range(PPO_EPOCHS):
            new_log_probs = F.log_softmax(policy(prompt), dim=-1)[0]
            surrogate, clip_fraction = clipped_surrogate(
                new_log_probs[actions], old_log_probs[actions], advantages, CLIP_EPSILON)
            kl = exact_kl(new_log_probs, ref_log_probs)
            loss = -surrogate + beta * kl                           # maximize reward, on a leash
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        if step in log_steps:
            print(f"  step {step:3d}  mean_reward={rewards.mean().item():.2f}  "
                  f"P(safe)={new_log_probs[SAFE_TOKEN].exp().item():.2f}  "
                  f"KL={kl.item():.3f}  clip_frac={clip_fraction:.2f}")
    with torch.no_grad():
        final_log_probs = F.log_softmax(policy(prompt), dim=-1)[0]
    return (ref_log_probs[SAFE_TOKEN].exp().item(), final_log_probs[SAFE_TOKEN].exp().item(),
            exact_kl(final_log_probs, ref_log_probs).item())


def closed_form_safe_probability(ref_safe: float, beta: float) -> float:
    """pi*(safe) = pi_ref(safe) e^{1/beta} / (pi_ref(safe) e^{1/beta} + 1 - pi_ref(safe))."""
    tilted = ref_safe * math.exp(1.0 / beta)
    return tilted / (tilted + 1.0 - ref_safe)


def main() -> None:
    show_clipped_step_arithmetic()

    print(f"\nPPO trace (beta = {TRACE_BETA}, group = {GROUP_SIZE}, {PPO_EPOCHS} epochs per batch):")
    ref_safe, final_safe, final_kl = run_ppo(TRACE_BETA, TRACE_STEPS, TRACE_LOG_STEPS)
    print(f"  P_ref(safe) = {ref_safe:.3f}   final P(safe) = {final_safe:.3f}   final KL = {final_kl:.3f}")
    print(f"  KL ceiling for a policy that ALWAYS says safe: -log P_ref(safe) = {-math.log(ref_safe):.3f}")

    print(f"\nBeta sweep vs the closed-form optimum pi* = pi_ref * exp(r/beta) / Z ({SWEEP_STEPS} steps):")
    for beta in SWEEP_BETAS:
        ref_safe, final_safe, final_kl = run_ppo(beta, SWEEP_STEPS)
        optimum = closed_form_safe_probability(ref_safe, beta)
        print(f"  beta={beta:<4}  PPO P(safe)={final_safe:.3f}  closed-form pi*(safe)={optimum:.3f}"
              f"  KL={final_kl:.3f}")


if __name__ == "__main__":
    main()
