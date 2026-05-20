# Workflow Checklist — vLLM-Ascend Model Adapter

## Prerequisites

### Environment Setup

```bash
# Verify vLLM import path
python -c "import vllm; print(vllm.__file__)"
# Expected: /vllm-workspace/vllm/vllm/__init__.py

# Verify vllm-ascend installation
python -c "import vllm_ascend; print(vllm_ascend.__file__)"

# Check CANN version
ascend-cann-py -v

# Check NPU status
npu-smi info
```

### Directory Structure

```
/vllm-workspace/vllm           # vLLM source (editable install)
/vllm-workspace/vllm-ascend   # vllm-ascend source (editable install)
/workspace                      # Working directory for vllm serve
/models/<model-name>           # Model checkpoint root
```

---

## Step-by-Step Checklist

### Step 1: Collect Context

- [ ] Confirm model path (HF or local)
- [ ] Confirm implementation roots
- [ ] Confirm delivery repo
- [ ] Determine feature set to validate:
  - [ ] ACLGraph (all models)
  - [ ] EP / FlashComm1 (MoE only)
  - [ ] Multimodal (VL only)
  - [ ] MTP (if checkpoint supports)

### Step 2: Analyze Model

- [ ] Inspect `config.json`
- [ ] Inspect modeling files
- [ ] Inspect processor files (VL)
- [ ] Inspect tokenizer
- [ ] Inspect safetensors weight index

**Model Type Classification:**
- [ ] LLM (Standard/MQA/GQA/MLA/Sliding/Mamba)
- [ ] VLM (vision encoder + language backbone)
- [ ] Whisper (encoder-decoder ASR)

**Additional Analysis:**
- [ ] Architecture class in `registry.py`?
- [ ] Attention variant (GQA/MQA/MHA/MLA/sliding)
- [ ] Quantization type (fp8/fp4/none)
- [ ] State-dict key prefix layout

### Step 3: Operator Compatibility Gate

Scan for operators and classify:

| Operator Type | Check | Action |
|-------------|-------|--------|
| Torch native | [ ] | Note performance uncertainty |
| Triton | [ ] | Verify correctness |
| CUDA with fallback | [ ] | Use fallback |
| CUDA without fallback | [ ] | **EARLY EXIT** |

**If CUDA without fallback detected:**
- [ ] File GitHub issue with:
  - Blocking operator details
  - Why no fallback exists
  - Recommended path forward
- [ ] Stop workflow

### Step 4: Framework-Side Code Analysis

- [ ] Identify changed vLLM framework modules
- [ ] Check if vllm-ascend has patches for these modules
- [ ] Verify patches still apply after upstream changes
- [ ] Add minimal overrides if needed

### Step 5: Choose Adaptation Strategy

| Situation | Strategy Selected |
|-----------|-------------------|
| Architecture exists + compatible | [ ] Reuse; patch only broken |
| Architecture missing/incompatible | [ ] Implement new adapter |
| Remote code needs newer transformers | [ ] Copy files (don't upgrade) |
| Requires modeling code in vllm-ascend | [ ] **Do NOT proceed** - raise issue |

**If new adapter needed:**
- [ ] Create `vllm/model_executor/models/<model>.py`
- [ ] Create `vllm/transformers_utils/processors/<model>.py` (VL)
- [ ] Add to `vllm/model_executor/models/registry.py`
- [ ] Define weight remap rules

### Step 6: Implement Minimal Code Changes

**Code Location Rule:** All model adaptation code goes in `/vllm-workspace/vllm` ONLY.

- [ ] Implement model adapter in vLLM source
- [ ] No modeling files in vllm-ascend
- [ ] Weight mapping explicit and auditable

**Compile Check:**
```bash
python -m py_compile /vllm-workspace/vllm/vllm/model_executor/models/<model>.py
```

### Step 7: Two-Stage Validation

#### Stage A: Dummy Fast Gate

```bash
vllm serve /models/<model> \
  --load-format dummy \
  --dtype bfloat16 \
  --tensor-parallel-size <TP> \
  --max-model-len 131072 \
  --max-num-seqs 16 \
  --port 8000
```

- [ ] Service starts successfully
- [ ] Smoke inference request succeeds
- [ ] ACLGraph evidence collected

**Quick Test:**
```bash
curl -sf http://127.0.0.1:8000/v1/models
curl -s http://127.0.0.1:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"<name>","messages":[{"role":"user","content":"hi"}],"max_tokens":16}'
```

#### Stage B: Real-Weight Mandatory Gate

Same command minus `--load-format dummy`:

```bash
vllm serve /models/<model> \
  --dtype bfloat16 \
  --tensor-parallel-size <TP> \
  --max-model-len 131072 \
  --max-num-seqs 16 \
  --port 8000
```

- [ ] Service starts successfully
- [ ] Real-weight inference produces HTTP 200
- [ ] Non-empty output generated

**Stage B CANNOT be skipped.**

### Step 8: Validate Inference and Features

```bash
# 1. Readiness
curl -sf http://127.0.0.1:8000/v1/models

# 2. Text inference (all models)
curl -s http://127.0.0.1:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"<name>","messages":[{"role":"user","content":"say hi"}],"temperature":0,"max_tokens":16}'

# 3. Text+image inference (VL models)
curl -s http://127.0.0.1:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"<name>","messages":[{"role":"user","content":"describe image"}],"images":["<base64_image>"]}'
```

**Feature Status Matrix:**

| Feature | Status | Notes |
|---------|--------|-------|
| ACLGraph | ✅/❌ | |
| EP | ✅/❌/N/A | |
| FlashComm1 | ✅/❌/N/A | |
| Multimodal | ✅/❌/N/A | |
| MTP | ✅/❌/⚠️ | |

**Capacity Baseline:**
- [ ] max-model-len=128k validated
- [ ] max-num-seqs=16 validated

### Step 9: Generate Artifacts and Commit

#### Code Changes

- [ ] Backport minimal diff from `/vllm-workspace/*` to delivery repo
- [ ] All code in vLLM source only
- [ ] No modeling files in vllm-ascend

#### Test Config

```yaml
# tests/e2e/models/configs/<ModelName>.yaml
model_name: <HF path>
hardware: Ascend <A2/A3>
tasks:
  - name: <task>
    metrics:
      - name: <metric>
        value: <result>
num_fewshot: <N>
```

#### Tutorial Doc

```markdown
# docs/source/tutorials/models/<ModelName>.md

## Introduction
## Supported Features
## Environment Preparation
## Deployment
## Functional Verification
## Accuracy Evaluation
## Performance
```

- [ ] Create tutorial doc
- [ ] Update `docs/source/tutorials/models/index.md`

#### Commit

```bash
git add .
git commit -sm "feat: add <ModelName> support on Ascend NPU"
```

### Step 10: Handoff Artifacts

**Analysis Report (Chinese):**
- [ ] Architecture summary
- [ ] Model type classification
- [ ] Operator compatibility findings
- [ ] Framework-side changes
- [ ] Code changes and rationale
- [ ] Feature status matrix (✅/❌/⚠️/N/A)
- [ ] Dummy-vs-real validation matrix
- [ ] max-model-len (theoretical vs practical)
- [ ] Fallback ladder evidence

**Runbook (Chinese):**
- [ ] Server startup command
- [ ] Validation curl commands
- [ ] Eager/TorchDynamo fallback commands

---

## Quality Gate Checklist

All items must be true before sign-off:

- [ ] `vllm serve` starts from `/workspace` on port 8000
- [ ] `GET /v1/models` returns HTTP 200
- [ ] Text inference returns HTTP 200 with non-empty output
- [ ] VL models: text+image inference returns HTTP 200
- [ ] All features reported with status
- [ ] max-model-len=128k + max-num-seqs=16 capacity baseline
- [ ] Real-weight evidence present (not dummy-only)
- [ ] `tests/e2e/models/configs/<ModelName>.yaml` exists
- [ ] `docs/source/tutorials/models/<ModelName>.md` exists
- [ ] `index.md` updated
- [ ] Exactly one signed commit
- [ ] SKILL.md summary posted on GitHub issue

---

## Quick Command Reference

### Start Dummy Validation

```bash
vllm serve <model_path> \
  --load-format dummy \
  --dtype bfloat16 \
  --tensor-parallel-size 4 \
  --max-model-len 131072 \
  --max-num-seqs 16 \
  --port 8000
```

### Start Real Validation

```bash
vllm serve <model_path> \
  --dtype bfloat16 \
  --tensor-parallel-size 4 \
  --max-model-len 32768 \
  --max-num-seqs 16 \
  --trust-remote-code \
  --port 8000
```

### Test Inference

```bash
curl -sf http://127.0.0.1:8000/v1/models

curl -s http://127.0.0.1:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"<name>","messages":[{"role":"user","content":"Hello"}],"max_tokens":16}'
```

### Isolate Graph Issues

```bash
--enforce-eager
```

### VL Model Isolation

```bash
TORCHDYNAMO_DISABLE=1
--limit-mm-per-prompt '{"image":0}'
```
