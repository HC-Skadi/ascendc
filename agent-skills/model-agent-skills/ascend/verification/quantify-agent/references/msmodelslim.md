# msmodelslim Quantization Protocol

Strict sequential protocol for model quantization, structural consultation, or debugging on Ascend NPUs.

## 0. End-to-End Iterative Workflow

Always follow this loop. Never skip evaluation before declaring success.

```
User specifies target dtype (e.g. w4a8, w8a8, w4a4)
         │
         ▼
[Step 1] Quantize with target dtype
         Use Strategy A (one-click) if a lab_practice config exists.
         Use Strategy C (custom YAML) otherwise.
         │
         ▼
[Step 2] Serve with vllm-run.md
         │
         ▼
[Step 3] Evaluate accuracy with ais_bench.md (GSM8K)
         Threshold: ≤ 1 percentage point drop vs FP16 baseline.
         │
    ┌────┴────┐
    │ PASS    │ FAIL
    ▼         ▼
  Done   [Step 4] Sensitive layer analysis → add disable_names
                  Retry quantization with the SAME target dtype.
                  Re-evaluate (Step 2–3).
                  │
             ┌────┴────┐
             │ PASS    │ FAIL
             ▼         ▼
           Done   [Step 5] Fall back to next lower compression tier,
                           then restart from Step 1 with new dtype.
```

### Compression Tier Order (highest → lowest)

| Tier | dtype | Notes |
| :--- | :--- | :--- |
| 1 | `w4a4` | Custom YAML only; use only when memory is critically constrained |
| 2 | `w4a8` | Standard aggressive; recommended starting point for MoE models |
| 3 | `w8a8` / `w8a8s` | Standard for dense models |
| 4 | `w8a16` | Conservative; good accuracy floor |
| 5 | `w16a16s` / bf16 | Near-lossless; last resort |

**Key rule**: When retrying after sensitivity analysis, always use the **user's original target dtype** — do not silently downgrade to a lower tier without confirming with the user.

______________________________________________________________________

## 1. Pre-execution Validation

Before starting any quantization task, verify that the environment and hardware are ready.

### Environment Check

Verify mandatory dependencies:

- `pip show msmodelslim torch_npu transformers`

### Model Support Check

If the current `transformers` version does not support the target model:

1. Upgrade `transformers` to the latest version and re-check support.
1. If the latest version still does not support the model, stop and inform the user — quantization cannot proceed without upstream support.

### Hardware Status

Ensure NPUs are available and not currently locked by other processes:

- `npu-smi info`

______________________________________________________________________

## 2. Quantization Execution

### Step 1A: One-Click Quantization (Start Here)

Check `msmodelslim/lab_practice` for a pre-configured YAML matching the model + target dtype. If one exists, use it.

- **`--quant_type`**: auto-matches the best YAML from `lab_practice`. Values: `w4a8`, `w4a8c8`, `w8a8`, `w8a8s`, `w8a8c8`, `w8a16`, `w16a16s`.
- **`--config_path`**: use a specific YAML directly — takes priority over `--quant_type`. These two flags are mutually exclusive.
- **Always pass** `--trust_remote_code True` for models with custom architecture (Qwen3, DeepSeek, GLM, etc.).

```bash
# Option A1: auto-match from lab_practice
msmodelslim quant \
  --model_path ${MODEL_PATH} \
  --save_path ${SAVE_PATH} \
  --device npu \
  --model_type <ModelName> \
  --quant_type <TARGET_DTYPE> \
  --trust_remote_code True

# Option A2: explicit config (preferred when a custom YAML exists)
msmodelslim quant \
  --model_path ${MODEL_PATH} \
  --save_path ${SAVE_PATH} \
  --device npu \
  --model_type <ModelName> \
  --config_path /path/to/config.yaml \
  --trust_remote_code True
```

### Step 1B: Custom YAML (When No lab_practice Config Exists)

Build a YAML config following Sections 3–4 below. Use this for: MoE models with mixed precision, models with no existing best-practice config, or when the one-click result fails accuracy.

### Step 1C: Traditional Low-Level API (Deep Debugging Only)

Refer to the `example/` directory in the `msmodelslim` source for Python API patterns. Use only for research or granular debugging.

______________________________________________________________________

### Step 4: Sensitive Layer Analysis (Accuracy Recovery Fallback)

Run this **only after** evaluation fails (Section 0, Step 4). Do **not** run preemptively.

```bash
msmodelslim analyze \
  --model_type <TYPE> \
  --model_path <PATH> \
  --metrics kurtosis \
  --topk 15 \
  --device npu
```

Extract the top-ranked layer names from the output and add them to `disable_names` in the quantization config. Then **retry with the user's original target dtype** — do not downgrade without explicit confirmation.

- `Act Method`: default `3` (Auto-mixed)
- `Anti Method`: default `m2` (Enhanced SmoothQuant)

______________________________________________________________________

## 3. Parameter Selection

### 3.1 Activation Scope (`act.scope`) and `symmetric`

`symmetric` is **not a free choice** — it is determined by `scope`. This is a hardware constraint on Ascend NPU.

| `scope` | `symmetric` | Type | When to use |
| :--- | :--- | :--- | :--- |
| `per_token` | **`true`** | Dynamic | Default for all LLM quantization — one scale per token at runtime. Use for everything unless you have a specific reason not to. |
| `per_tensor` | **`false`** | Static | Scale fixed at calibration time. Use only for attention layers when maximizing throughput over accuracy (e.g., Qwen3-Coder-480B attn). |
| `pd_mix` | **`false`** | Hybrid | `per_token` during prefill, `per_tensor` during decode. Use **only** when KV cache is also quantized (`w8a8c8`). |

**Decision rule**: Use `per_token + symmetric: true` unless you are building a throughput-optimized config or quantizing KV cache.

______________________________________________________________________

### 3.2 Weight Scope (`weight.scope`)

| `scope` | When to use | Seen in |
| :--- | :--- | :--- |
| `per_channel` | Everything — standard for W8A8 and all W4A8 in lab_practice | All official W4A8 configs (Qwen3-235B, Qwen3-Next, Qwen3-Coder-480B, DeepSeek, GLM-5) |
| `per_group` + `ext.group_size: 256` | Only W4A4 — when absolute minimum memory is required | Qwen3-32B W4A4 only |
| `per_tensor` | Never in production — not seen in any lab_practice config | — |

______________________________________________________________________

### 3.3 Weight Method (`weight.method`)

Method is **fully determined** by dtype + scope combination:

| dtype | scope | method | Notes |
| :--- | :--- | :--- | :--- |
| `int8` | `per_channel` | `minmax` | Standard for all W8A8. Fast and sufficient. |
| `int8` | `per_channel` | `autoround` | Higher accuracy W8A8 (used for attention in W4A4 configs). |
| `int4` | `per_channel` | `ssz` | **Standard for all W4A8 in lab_practice.** Iterative MSE optimization. `ext.step` overrides iteration count (default 50). |
| `int4` | `per_group` | `autoround` | W4A4 only. SSZ does not support `per_group`. |

**Do not mix**: `ssz` with `per_group`, `gptq` with MoE experts, `autoround` with `per_channel` for INT4.

______________________________________________________________________

### 3.4 Outlier Suppression Preprocessor

Must run **before** `linear_quant`. Choose based on quantization aggressiveness and model type:

| Preprocessor | Use when | Typical subgraph types |
| :--- | :--- | :--- |
| `iter_smooth` | Dense models, W8A8 | `norm-linear`, `linear-linear`, `ov`, `up-down` |
| `flex_smooth_quant` | MoE models, standard W4A8 | Start with `norm-linear`; add `ov` if model has cross-attn/value subgraphs |
| `quarot` → `flex_smooth_quant` | W4A4, or architecturally complex W4A8 (Qwen3-Coder-480B) | `quarot` has no subgraph config |
| `quarot` → `flex_awq_ssz` → `flex_smooth_quant` | Heaviest outlier models (GLM-5, DeepSeek-V3.2) | `flex_awq_ssz` on `up-down`; `flex_smooth_quant` on remaining |

**Subgraph type selection for `flex_smooth_quant`**:

- `norm-linear` — universal, covers post-norm → linear patterns. Always include.
- `ov` — add if the model has o_proj following v_proj (cross-attention/value patterns). E.g., DeepSeek MLA.
- `up-down` — add if outliers persist in gate/up → down MLP paths. E.g., GLM-5, some DeepSeek variants.

______________________________________________________________________

### 3.5 Calibration Dataset (`dataset`)

| Dataset | Use for |
| :--- | :--- |
| `mix_calib.jsonl` | Default — general-purpose. Used when no `dataset:` field is specified. |
| `qwen3_cot.json` | Reasoning/CoT models at W8A8 (Qwen3, QwQ) |
| `qwen3_cot_w4a4.json` | Reasoning models at W4A4 or aggressive W4A8 |
| `autocodebench.jsonl` | Code models (Qwen3-Coder) |

______________________________________________________________________

### 3.6 Layer Protection

Protecting first/last layers from aggressive quantization prevents accuracy collapse. Patterns observed in lab_practice:

- **Qwen3-Coder-480B W4A8**: excludes first 5 + last 5 layers from expert W4A8 quantization
- **DeepSeek-R1-0528 W4A8**: last expert layer forced to W8A8 instead
- **GLM-5 W4A8**: entire last layer excluded
- **Universal**: `*gate` router layers are **never** quantized across all configs

**Rule of thumb**: Start without layer protection. If accuracy drops, add exclusions for the first 3–5 and last 3–5 transformer layers, or bump them to W8A8.

```yaml
# Exclude first/last N layers from W4A8 expert quantization
- type: "linear_quant"
  qconfig: *default_w4a8_dynamic
  include: ["*mlp.experts*"]
  exclude:
    - "model.layers.{0,1,2,3,4}.*"
    - "model.layers.{55,56,57,58,59}.*"  # adjust to model.num_hidden_layers - N

# OR: bump boundary layers to W8A8 instead of excluding
- type: "linear_quant"
  qconfig: *default_w8a8_dynamic
  include: ["model.layers.{0,1,2,3,4}.mlp.experts*", "model.layers.{55,56,57,58,59}.mlp.experts*"]
```

______________________________________________________________________

## 4. Mixed Quantization (Mix Quant)

Use the `group` processor to apply different qconfigs to different layer sets.

### Common MoE Strategy

- **Attention**: W8A8 dynamic — preserves accuracy on sensitive layers
- **Shared MLP**: W8A8 dynamic — better activation accuracy
- **Expert layers**: W4A8 `per_channel + ssz` — maximizes memory savings (dominant pattern in lab_practice)

### YAML Template

```yaml
apiversion: modelslim_v1
metadata:
  config_id: <model_name>_w4a8
  score: 90
  verified_model_types:
    - <ModelName>
  label:
    w_bit: 4
    a_bit: 8
    is_sparse: False
    kv_cache: False

# Reusable qconfig anchors
default_w8a8_dynamic: &default_w8a8_dynamic
  act:    {scope: "per_token",   dtype: "int8", symmetric: true, method: "minmax"}
  weight: {scope: "per_channel", dtype: "int8", symmetric: true, method: "minmax"}

default_w4a8_dynamic: &default_w4a8_dynamic
  act:    {scope: "per_token",   dtype: "int8", symmetric: true, method: "minmax"}
  weight: {scope: "per_channel", dtype: "int4", symmetric: true, method: "ssz"}

spec:
  process:
    # Step 1: Outlier suppression — see Section 3.4 for preprocessor and subgraph type selection
    - type: "flex_smooth_quant"
      enable_subgraph_type: ['norm-linear']
      include:
        - '*'

    # Step 2: Mixed quantization group
    - type: "group"
      configs:
        - type: "linear_quant"
          qconfig: *default_w8a8_dynamic
          include: ["*self_attn*"]

        - type: "linear_quant"
          qconfig: *default_w8a8_dynamic
          include: ["*mlp*"]
          exclude: ["*gate", "*mlp.experts.*"]

        - type: "linear_quant"
          qconfig: *default_w4a8_dynamic
          include: ["*mlp.experts*"]

  save:
    - type: "ascendv1_saver"
      part_file_size: 4
```

### Layer Filter Rules

- `include` / `exclude` accept Glob wildcards (`*`, `?`, `[abc]`, `[!abc]`).
- `exclude` overrides `include` within the same entry.
- Always exclude `*gate` routers — they are never quantized in any lab_practice config.
- Filter by index: `"model.layers.{0,1,2,3,4}.*"` — see Section 3.6 for layer protection strategy.

______________________________________________________________________

## 5. Quick Reference: Common qconfig Patterns

```yaml
# W8A8 Static (throughput-first, e.g. attention layers)
act:    {scope: "per_tensor",  dtype: "int8", symmetric: false, method: "minmax"}
weight: {scope: "per_channel", dtype: "int8", symmetric: true,  method: "minmax"}

# W8A8 Dynamic (accuracy-first, standard for LLMs)
act:    {scope: "per_token",   dtype: "int8", symmetric: true,  method: "minmax"}
weight: {scope: "per_channel", dtype: "int8", symmetric: true,  method: "minmax"}

# W4A8 per_channel+ssz (standard for MoE experts — all official lab_practice W4A8 configs)
act:    {scope: "per_token",   dtype: "int8", symmetric: true, method: "minmax"}
weight: {scope: "per_channel", dtype: "int4", symmetric: true, method: "ssz"}

# W4A8 per_group+autoround (W4A4 only, or when per_group granularity is explicitly needed)
act:    {scope: "per_token",   dtype: "int8", symmetric: true, method: "minmax"}
weight: {scope: "per_group",   dtype: "int4", symmetric: true, method: "autoround", ext: {group_size: 256}}

# W8A8 pd_mix (only with KV cache quantization / w8a8c8)
act:    {scope: "pd_mix",      dtype: "int8", symmetric: false, method: "minmax"}
weight: {scope: "per_channel", dtype: "int8", symmetric: true,  method: "minmax"}
```

______________________________________________________________________

## 6. Hardware & Resource Management

### NPU Mandatory

- **No CPU Quantization**: `msmodelslim` operations **must** run on Ascend NPUs.
- **Multi-NPU Strategy**: If Out-of-Memory (OOM) occurs on a single device, distribute the process across multiple NPUs:
  ```bash
  export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3
  # then pass --device npu:0,1,2,3 to enable distributed layer-by-layer quantization
  ```

### Lifecycle Management

- Once a quantization command is initialized and confirmed, output the exact command for the user to run in their terminal.
- **Safety**: Terminate any background processes immediately after the main quantization loop begins to prevent resource contention.
- **Artifact Storage**: Save all generated YAML configs and shell scripts to the current working directory. Do not save them elsewhere.

______________________________________________________________________

## 7. Troubleshooting & Common Pitfalls

- **Weights Path**: Always verify that the `--model_path` contains the correct weights format (e.g., Safetensors or Bin).
- **Library Version**: Ensure `msmodelslim` version matches the `CANN` version installed on the system.
- **Permission Errors**: Check write permissions for the `--save_path`.
- **Missing `trust_remote_code`**: Models with custom architectures (Qwen3, DeepSeek, etc.) will fail silently — always pass `--trust_remote_code True`.
- **`--quant_type` + `--config_path` conflict**: These two flags are mutually exclusive; use one or the other.
- **SSZ on per_group**: SSZ does not support `per_group` scope — switch to `autoround`.
- **Symmetric mismatch**: Ascend NPU hardware acceleration requires `symmetric: true` for all activation configs.
- **MoE + GPTQ**: GPTQ is not recommended for MoE expert layers — use `ssz` (per_channel) or `autoround` (per_group) instead.
