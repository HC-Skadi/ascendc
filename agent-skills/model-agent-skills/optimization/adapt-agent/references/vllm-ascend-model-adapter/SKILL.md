---
name: vllm-ascend-model-adapter
description: AI-assisted model adaptation skill for running Hugging Face or local model checkpoints on Ascend NPU via vLLM-Ascend. Use when users want to adapt a new model to run on Ascend NPUs, add support for a new model architecture, validate model compatibility with vLLM-Ascend, or troubleshoot model loading issues on Ascend. This skill executes a 10-step playbook covering pre-flight analysis, Ascend compatibility gating, implementation, two-stage validation, and delivery of documentation.
---

# vLLM-Ascend Model Adapter

An AI-assisted skill for adapting models to run on Ascend NPU via vLLM-Ascend. Based on the official [vLLM-Ascend RFC #7539](https://github.com/vllm-project/vllm-ascend/issues/7539).

## When to Use This Skill

- Adding support for a new model architecture on Ascend NPUs
- Validating if an existing model works with vLLM-Ascend
- Troubleshooting model loading or inference failures on Ascend
- Understanding operator compatibility requirements for Ascend

## 10-Step Adaptation Playbook

### Step 1 — Collect Context

Confirm the following with the user:

- **Model path**: HuggingFace path or local checkpoint location
- **Implementation roots**: vLLM source paths
- **Delivery repo**: Target repository for changes
- **Default feature set to validate**:
  - All models: ACLGraph
  - MoE models: EP (expert parallel), flashcomm1
  - VL models: multimodal (text+image inference)
  - MTP: Only if checkpoint explicitly supports it

### Step 2 — Analyze Model

Inspect `config.json`, modeling files, processor files, tokenizer, and safetensors weight index.

**Model Type Classification:**
```
LLM ─┬─ Standard full attention
     ├─ Sliding window attention
     ├─ Mamba (SSM)
     ├─ Multi-latent attention (MLA)
     └─ Hybrid (MLA + Mamba layers interleaved)

VLM  ─── Vision-language model (vision encoder + language backbone)

Whisper ─ Encoder-decoder ASR model
```

**Additional Analysis:**
- Architecture class and whether it exists in `vllm/model_executor/models/registry.py`
- Attention variant (GQA / MQA / MHA / MLA / sliding window)
- Quantization type (fp8, fp4, or none)
- State-dict key prefix layout (for weight remap planning)

### Step 3 — Operator Compatibility Gate

Scan model code for operators and classify:

| Operator Type | Ascend Compatibility | Action |
|--------------|----------------------|--------|
| **Torch** (native PyTorch) | ✅ Functional | Note performance uncertainty |
| **Triton** kernel | ⚠️ Uncertain | Verify correctness and accuracy |
| **CUDA** with fallback | ❌ Use fallback | Document the fallback path |
| **CUDA** without fallback | ❌ **BLOCKED** | Early exit: file GitHub issue |
| **Triton** verification fails | ❌ **BLOCKED** | Early exit: file GitHub issue |

**CUDA Early-Exit Rule:** If any operator is pure CUDA with no Torch/Triton alternative, stop immediately and file a GitHub issue documenting:
- Which operator blocks Ascend support
- Why no fallback exists
- Recommended path forward

### Step 4 — Framework-Side Code Analysis

Identify if upstream vLLM commits changed framework modules that vllm-ascend has patched:

```
Changed vLLM framework module
        │
        ├─ Already patched by vllm-ascend?
        │       └─ YES → Check if patch still applies. Update if needed.
        │
        └─ NOT covered + Ascend-incompatible?
                └─ YES → Add minimal override under vllm-ascend/
```

### Step 5 — Choose Adaptation Strategy

| Situation | Strategy |
|----------|----------|
| Architecture exists and compatible | Reuse; patch only what's broken |
| Architecture missing or incompatible | Implement new adapter |
| Remote code needs newer transformers | Copy required files — never upgrade |
| Failure requires modeling code in vllm-ascend | **Do not proceed** — raise GitHub issue |

**New Adapter Checklist:**
1. `vllm/model_executor/models/<model>.py` — model class and weight loader
2. `vllm/transformers_utils/processors/<model>.py` — multimodal processor (VL only)
3. `vllm/model_executor/models/registry.py` — architecture name registration
4. Explicit weight remap rules: qkv sharding, QK/KV norms, RoPE variants, fp8 scale pairing

### Step 6 — Implement Minimal Code Changes

All model adaptation code goes in vLLM source only. Model-specific files must **never** be introduced in vllm-ascend.

```bash
python -m py_compile /vllm-workspace/vllm/vllm/model_executor/models/<model>.py
```

### Step 7 — Two-Stage Validation

**Both stages are REQUIRED. Dummy-only evidence is insufficient.**

**Stage A — Dummy Fast Gate:**
```bash
vllm serve /models/<model> \
  --load-format dummy \
  --dtype bfloat16 \
  --tensor-parallel-size <TP> \
  --max-model-len 131072 \
  --max-num-seqs 16 \
  --port 8000
```

**Stage B — Real-Weight Mandatory Gate:**
Same command, minus `--load-format dummy`.

### Step 8 — Validate Inference and Features

```bash
# 1. Readiness check
curl -sf http://127.0.0.1:8000/v1/models

# 2. Text inference (all models)
curl -s http://127.0.0.1:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"<name>","messages":[{"role":"user","content":"say hi"}],"temperature":0,"max_tokens":16}'

# 3. Text+image inference (VL models only)
```

**Feature Status Symbols:**
| Symbol | Meaning |
|--------|---------|
| ✅ | Supported and verified |
| ❌ | Framework-level unsupported |
| ⚠️ | Checkpoint missing (feature not in weights) |
| N/A | Not applicable |

### Step 9 — Backport, Generate Artifacts, Commit

1. Backport minimal diff from `/vllm-workspace/*` to delivery repo
2. Generate `tests/e2e/models/configs/<ModelName>.yaml`
3. Generate `docs/source/tutorials/models/<ModelName>.md`
4. Update `docs/source/tutorials/models/index.md`
5. Exactly one signed commit: `git commit -sm "feat: add <ModelName> support on Ascend NPU"`

### Step 10 — Handoff Artifacts

Final response includes (in Chinese):
- **Analysis Report**: architecture summary, incompatibility root causes, code changes, feature status matrix
- **Runbook**: server startup command, validation curl commands, fallback commands
- **SKILL.md summary** posted as comment on GitHub issue

## Fallback Ladder

When startup or inference fails, follow this ordered approach:

```
1. Reproduce once to confirm deterministic failure
        ↓
2. Add --enforce-eager → isolate graph-capture vs operator failures
        ↓
3. [VL] TORCHDYNAMO_DISABLE=1 → isolate dynamo/interpolate/contiguous failures
        ↓
4. [VL] --limit-mm-per-prompt '{"image":0,"video":0,"audio":0}'
        → isolate multimodal processor failures from model core
        ↓
5. Apply targeted code fix, loop back to Stage A
```

## Quick Reference

### Supported Models

See `./reference/supported-models.md` for the complete list.

### Quantization Support

See `./reference/quantization-guide.md` for quantization algorithms and configurations.

### Operator Compatibility

See `./reference/operator-compatibility.md` for detailed compatibility information.

### Troubleshooting

See `./reference/troubleshooting.md` for known failure signatures and resolutions.

## Workflow Checklist

See `./reference/workflow-checklist.md` for step-by-step commands.

## Output Requirements

Every adaptation must produce:
- Minimal diff (vLLM source only, never vllm-ascend modeling files)
- `tests/e2e/models/configs/<ModelName>.yaml`
- `docs/source/tutorials/models/<ModelName>.md`
- Analysis report in Chinese
- Runbook in Chinese
- Exactly one signed commit
