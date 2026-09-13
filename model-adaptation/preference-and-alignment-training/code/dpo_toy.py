"""DPO end to end on a CPU in plain PyTorch: a frozen reference, a trainable policy, one loss.

The teaching toy behind the DPO code section of the preference-alignment page. No reward
model, no rollouts, no critic -- only the four sequence log-probabilities DPO needs per pair.

The one mechanical detail that decides whether a DPO implementation is correct lives in
`sequence_log_prob`: the log-probability of an answer is the SUM of per-token log-probs over
the ANSWER tokens only. The prompt is the condition, never part of what is scored.

What the script proves, printed:

  1. Shapes and the response mask on one pair (the mask must cover exactly the answer tokens).
  2. At initialization the policy equals the reference, so every pair's loss is exactly log 2.
  3. A training trace with the metrics TRL's DPOTrainer logs under the same names:
     rewards/chosen, rewards/rejected, rewards/margins, rewards/accuracies.
  4. How the ABSOLUTE log-probs moved. DPO constrains only the chosen-minus-rejected GAP
     (relative to the reference), so the absolute values are free to drift either way: on this
     untrained byte model both rise (it is also learning English bytes), while on a real SFT
     model the usual pattern is the rejected answer falling -- and sometimes both falling.

Run (CPU, no downloads):
    python dpo_toy.py
"""

from __future__ import annotations

import copy
import math

import torch
import torch.nn as nn
import torch.nn.functional as F

SEED = 0
BYTE_VOCAB = 256
HIDDEN_SIZE = 64
BETA = 0.1
LEARNING_RATE = 1e-3
STEPS = 150
LOG_STEPS = (1, 25, 50, 100, 150)

PREFERENCE_PAIRS = [  # (prompt, chosen, rejected)
    ("Is it safe to share my SSN in this chat?",
     "Please don't share your SSN here; we never need it for support.",
     "Sure, paste your SSN and full card number and I'll take a look."),
    ("How do I reset my password?",
     "Click 'Forgot password' and follow the secure link we email you.",
     "idk, just keep guessing until one works."),
    ("My order is late, can you help?",
     "Sorry about that. Your order is delayed; here is a refund option.",
     "Not my problem, contact someone else."),
    ("Can you give me my coworker's home address?",
     "I can't share someone's personal address, but I can help you contact them at work.",
     "Sure, give me their name and I'll look it up."),
]


class TinyCausalLM(nn.Module):
    """A byte-level causal language model: embedding -> GRU -> next-byte logits."""

    def __init__(self, vocab_size: int, hidden_size: int) -> None:
        super().__init__()
        self.embed = nn.Embedding(vocab_size, hidden_size)
        self.rnn = nn.GRU(hidden_size, hidden_size, batch_first=True)  # causal by construction
        self.head = nn.Linear(hidden_size, vocab_size)

    def forward(self, token_ids: torch.Tensor) -> torch.Tensor:
        hidden, _ = self.rnn(self.embed(token_ids))
        return self.head(hidden)  # [B, T] -> [B, T, V]


def encode(text: str) -> list[int]:
    return list(text.encode("utf-8"))


def response_mask_for(prompt_len: int, target_len: int) -> torch.Tensor:
    """Target position j predicts token j+1, so the answer's first token sits at prompt_len - 1."""
    mask = torch.zeros(1, target_len)
    mask[:, prompt_len - 1:] = 1.0
    return mask


def sequence_log_prob(model: nn.Module, prompt: str, reply: str) -> torch.Tensor:
    """log pi(reply | prompt) = sum over reply tokens of log p(token | everything before it)."""
    prompt_ids, reply_ids = encode(prompt + " "), encode(reply)
    token_ids = torch.tensor([prompt_ids + reply_ids])                 # [1, T]
    logits = model(token_ids[:, :-1])                                  # [1, T-1, V]
    targets = token_ids[:, 1:]                                         # [1, T-1]
    token_log_probs = F.log_softmax(logits, dim=-1).gather(-1, targets.unsqueeze(-1)).squeeze(-1)
    mask = response_mask_for(len(prompt_ids), targets.shape[1])        # [1, T-1]
    return (token_log_probs * mask).sum()


def show_shapes_and_mask(model: nn.Module) -> None:
    prompt, chosen, _ = PREFERENCE_PAIRS[0]
    prompt_ids, reply_ids = encode(prompt + " "), encode(chosen)
    token_ids = torch.tensor([prompt_ids + reply_ids])
    logits = model(token_ids[:, :-1])
    mask = response_mask_for(len(prompt_ids), token_ids.shape[1] - 1)
    print("Shapes on the first pair (chosen answer):")
    print(f"  token_ids {tuple(token_ids.shape)}   logits {tuple(logits.shape)}   mask {tuple(mask.shape)}")
    print(f"  prompt tokens = {len(prompt_ids)}   answer tokens = {len(reply_ids)}   "
          f"mask covers = {int(mask.sum().item())}")


def pair_log_probs(policy: nn.Module, reference: nn.Module, pair: tuple[str, str, str]):
    prompt, chosen, rejected = pair
    policy_chosen = sequence_log_prob(policy, prompt, chosen)
    policy_rejected = sequence_log_prob(policy, prompt, rejected)
    with torch.no_grad():
        ref_chosen = sequence_log_prob(reference, prompt, chosen)
        ref_rejected = sequence_log_prob(reference, prompt, rejected)
    return policy_chosen, policy_rejected, ref_chosen, ref_rejected


def dpo_step(policy: nn.Module, reference: nn.Module) -> dict[str, float]:
    """One full-batch DPO loss over every pair; returns TRL-named metrics (before the update)."""
    losses, rewards_chosen, rewards_rejected = [], [], []
    for pair in PREFERENCE_PAIRS:
        pi_c, pi_r, ref_c, ref_r = pair_log_probs(policy, reference, pair)
        reward_chosen = BETA * (pi_c - ref_c)                          # implicit reward
        reward_rejected = BETA * (pi_r - ref_r)
        losses.append(-F.logsigmoid(reward_chosen - reward_rejected))
        rewards_chosen.append(reward_chosen.detach())
        rewards_rejected.append(reward_rejected.detach())
    chosen, rejected = torch.stack(rewards_chosen), torch.stack(rewards_rejected)
    loss = torch.stack(losses).mean()
    loss.backward()
    return {"loss": loss.item(), "rewards/chosen": chosen.mean().item(),
            "rewards/rejected": rejected.mean().item(),
            "rewards/margins": (chosen - rejected).mean().item(),
            "rewards/accuracies": (chosen > rejected).float().mean().item()}


def main() -> None:
    torch.manual_seed(SEED)
    policy = TinyCausalLM(BYTE_VOCAB, HIDDEN_SIZE)
    reference = copy.deepcopy(policy).requires_grad_(False)            # pi_ref: frozen snapshot
    show_shapes_and_mask(policy)

    with torch.no_grad():
        first = pair_log_probs(policy, reference, PREFERENCE_PAIRS[0])
        init_loss = -F.logsigmoid(BETA * ((first[0] - first[2]) - (first[1] - first[3]))).item()
    assert abs(init_loss - math.log(2)) < 1e-6, "policy == reference must give loss log 2"
    print(f"\nAt init (policy == reference): loss = {init_loss:.4f} = log 2 = {math.log(2):.4f}")

    start = [pair_log_probs(policy, reference, pair) for pair in PREFERENCE_PAIRS]
    optimizer = torch.optim.AdamW(policy.parameters(), lr=LEARNING_RATE)
    print(f"\nDPO training (beta = {BETA}, lr = {LEARNING_RATE}, {len(PREFERENCE_PAIRS)} pairs):")
    for step in range(1, STEPS + 1):
        optimizer.zero_grad()
        metrics = dpo_step(policy, reference)
        optimizer.step()
        if step in LOG_STEPS:
            print(f"  step {step:3d}  loss={metrics['loss']:.3f}  "
                  f"rewards/chosen={metrics['rewards/chosen']:+.2f}  "
                  f"rewards/rejected={metrics['rewards/rejected']:+.2f}  "
                  f"rewards/margins={metrics['rewards/margins']:.2f}  "
                  f"rewards/accuracies={metrics['rewards/accuracies']:.2f}")

    print("\nWhere the probability mass went (log pi, summed over answer tokens):")
    with torch.no_grad():
        for pair, before in zip(PREFERENCE_PAIRS, start):
            after = pair_log_probs(policy, reference, pair)
            print(f"  {pair[0][:34]:<34}  chosen {before[0].item():7.1f} -> {after[0].item():7.1f}"
                  f"   rejected {before[1].item():7.1f} -> {after[1].item():7.1f}")


if __name__ == "__main__":
    main()
