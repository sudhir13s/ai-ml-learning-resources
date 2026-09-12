---
title: "The Production Fine-Tuning Pipeline"
id: lr-fine-tuning-production-fine-tuning-pipeline
minutes: 3
core_idea: "A production fine-tune is a pipeline, not a notebook — data in, adapter out, evaluation gate, registry entry, and a rollback that does not need a rebuild."
builds_on: [pw-mlops-and-deployment]
related: [pw-continuous-training, pw-model-serving]
section: "ai-ml-learning-resources"
workflow: "fine-tuning"
chapter: 6
difficulty: intermediate
assumed_knowledge: ["transformers & attention", "LoRA", "quantization"]
related_topics: ["7.02", "7.03", "7.04", "7.05", "7.10"]
status: complete
template: workflow
category: model-adaptation
---

# Chapter 6 — The Production Fine-Tuning Pipeline

Everything the course built, assembled into the recipe you would actually
run on a GPU — and then shipped.

The output of a fine-tune is not a model. **It is a `~150 MB` adapter file**, and that changes
how you serve it: one 5 GB base model in memory, many adapters hot-swapped on top for support,
sales, and summarization, without reloading the base.

This chapter carries the production QLoRA recipe end to end — 4-bit NF4 load, adapters on the
attention projections, paged 8-bit optimizer, effective batch 16 — and ends with where the
adapter goes next.

---

## The production recipe

Every decision the course made, in one file: how you would QLoRA-fine-tune a real 7B model with `transformers` + `peft` + `trl`. It needs a CUDA GPU for 4-bit `bitsandbytes`, so this is the canonical reference rather than something that runs here — the CPU-runnable version of the same five steps is in [Apply LoRA and QLoRA](/ai-ml/ai-ml-learning-resources/model-adaptation/fine-tuning/apply-lora-and-qlora).

```python
# PRODUCTION QLoRA recipe (GPU-only: 4-bit quantization needs CUDA + bitsandbytes).
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import LoraConfig
from trl import SFTTrainer, SFTConfig
import torch

MODEL = "mistralai/Mistral-7B-Instruct-v0.3"

# 1. Load the base model in 4-bit NF4 (the "holy trinity": NF4 + double-quant + paging)
bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                         bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=torch.bfloat16)
model = AutoModelForCausalLM.from_pretrained(MODEL, quantization_config=bnb, device_map="auto")
tok = AutoTokenizer.from_pretrained(MODEL)

# 2. Define the LoRA adapters (attach to the attention projections)
lora = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.05, bias="none", task_type="CAUSAL_LM",
                  target_modules=["q_proj", "k_proj", "v_proj", "o_proj"])

# 3. Train only the adapters with SFT (paged 8-bit optimizer = the memory release valve)
trainer = SFTTrainer(
    model=model, train_dataset=dataset, peft_config=lora,
    args=SFTConfig(per_device_train_batch_size=4, gradient_accumulation_steps=4,  # effective batch 16
                   learning_rate=2e-4, num_train_epochs=3, warmup_steps=50,
                   optim="paged_adamw_8bit", bf16=True))
trainer.train()
trainer.model.save_pretrained("./mistral-support-adapter")   # ships a ~150 MB adapter, not 14 GB
```

---

## Where this leaves you

You now have the whole picture. Fine-tuning is where three forces meet: **physical constraints** (quantization gets the model onto your GPU), **mathematical efficiency** (LoRA changes well under 1% of the weights), and **instructional clarity** (clean, correctly-formatted data teaches the behavior). String them together — load in 4-bit, attach LoRA to the attention projections, train on a few hundred well-masked instruction pairs, watch the *validation* loss, and save a ~150 MB adapter — and you get a model that is surgically precise, cheap to run, and predictable. None of it requires a cluster or a research budget: **you can do this yourself, today, on a single GPU.**

---

## Production implementation

Runnable services in this estate that implement what this page teaches:

- **[fine-tuning-toolkit](/python/python-production-examples/fine-tuning-toolkit/readme)** — the adapter-producing half of that pipeline.
- **[ml-platform](/python/python-production-examples/ml-platform/readme)** — the registry, gated promotion and rollout half.
- **[mlops-lifecycle](/python/cross-service-workflows/mlops-lifecycle)** — both halves wired together across services.

## References

  - [Knowledge Distillation (7.04)](/ai-ml/ai-ml-intuitions/scaling-adaptation-efficiency/knowledge-distillation-intuition) — the other way to specialize a model.
  - [Model Serving (workflow)](/ai-ml/practitioner-workflows/inference-and-serving/model-serving) — loading one base and hot-swapping many adapters in production.
  - [RLHF & Alignment (workflow)](/ai-ml/practitioner-workflows/training-and-adaptation/preference-alignment) — the preference-tuning step that usually follows SFT.
  - [TRL / SFTTrainer documentation (Hugging Face)](https://huggingface.co/docs/trl/index) — supervised fine-tuning API.
  - [bitsandbytes 4-bit quantization (Hugging Face)](https://huggingface.co/docs/transformers/main/en/quantization/bitsandbytes) — the QLoRA backend.
