# Sensitivity Analysis Protocol

Use this protocol when a quantized model shows **accuracy degradation** compared to the FP32 baseline. The goal is to identify which layers are most sensitive to quantization, then protect those layers via YAML adjustments.

______________________________________________________________________

## 1. Trigger Conditions

Run sensitivity analysis when:

- Quantized model accuracy drops by more than the acceptable tolerance on target benchmarks
- Specific task types (math reasoning, code, long-context) degrade while others remain stable
- First/last layer protection (Section 3.6 of msmodelslim.md) did not resolve the issue

______________________________________________________________________

## 2. Run Sensitivity Analysis

```bash
msmodelslim analyze \
  --model_type <ModelName> \
  --model_path ${MODEL_PATH} \
  --device npu \
  --metrics kurtosis \
  --calib_dataset mix_calib.jsonl \
  --topk 20 \
  --trust_remote_code True
```

**Key arguments**:

| Argument | Value | Notes |
| :--- | :--- | :--- |
| `--metrics` | See table below | Choose based on problem type |
| `--topk` | 15–20 | Number of most-sensitive layers to report |
| `--pattern` | `["*"]` (default) or specific patterns | Narrow scope to suspect layer types |
| `--calib_dataset` | Must match quantization dataset | Consistency is critical — use the same file used during quantization |

**Metric selection**:

| Metric | Use when | Algorithm |
| :--- | :--- | :--- |
| `kurtosis` | **Default.** General-purpose; detects layers with peaky/concentrated activation distributions | `E[(X-μ)⁴]/σ⁴ - 3` |
| `std` | Faster scan; regular quantization scenarios | `max(|max|, |min|) / std` |
| `quantile` | High-precision targets; anomalous outliers skew std results | IQR-based: `2·max_abs / 254 / (Q3−Q1)` |
| `attention_mse` | Attention accuracy specifically degraded; DeepSeek-V3/R1 series | Per-layer MSE between FP and INT output |

**Narrowing scope with `--pattern`**: If you suspect a specific module (e.g., MLP down_proj), limit analysis to it:

```bash
--pattern '["*.down_proj*", "*.o_proj*"]'
```

______________________________________________________________________

## 3. Interpret the Output

The command prints two sections to stdout:

```
=== Layer Analysis Results (kurtosis method) ===
Patterns analyzed: ['*']
Total layers analyzed: 256
Layer Sensitivity Scores (higher score = more sensitive):
  model.layers.14.mlp.down_proj     score=142.7
  model.layers.31.self_attn.o_proj  score=138.2
  model.layers.0.mlp.down_proj      score=131.9
  ...

=== YAML Format for quantization ===
exclude:
  - "model.layers.14.mlp.down_proj"
  - "model.layers.31.self_attn.o_proj"
  - "model.layers.0.mlp.down_proj"
  ...
=== End of YAML Format ===
```

**Reading scores**: Higher score = more sensitive = higher risk of accuracy loss when quantized. Focus on the top 10–20 entries.

**Cluster vs. scatter pattern**:

- Scores cluster around specific layer indices → protect those index ranges
- Scores scatter randomly across layers → protect by module type (e.g., all `down_proj`)

______________________________________________________________________

## 4. Adjust the YAML

Apply one of three strategies based on how many layers are sensitive and the accuracy gap.

### Strategy 1: Exclude Sensitive Layers (simplest)

Copy the YAML output block directly into your quantization config's `exclude` field. Excluded layers remain in FP16/BF16.

```yaml
- type: "linear_quant"
  qconfig: *default_w4a8_dynamic
  include: ["*"]
  exclude:
    # Paste sensitivity analysis output here:
    - "model.layers.14.mlp.down_proj"
    - "model.layers.31.self_attn.o_proj"
    - "model.layers.0.mlp.down_proj"
```

**When to use**: Accuracy gap is large; only a small number of layers (< 5% of total) are flagged.

**Cost**: Slight memory increase for excluded layers retained in FP16.

______________________________________________________________________

### Strategy 2: Promote Sensitive Layers to Higher Precision (mixed precision)

Instead of full FP16 fallback, demote sensitive layers from W4A8 → W8A8 to save memory while still recovering accuracy.

Use a `group` processor with the sensitive layers listed in a separate, higher-precision entry. The last matching entry in the group wins for a given layer.

```yaml
- type: "group"
  configs:
    # Base: quantize everything at W4A8
    - type: "linear_quant"
      qconfig: *default_w4a8_dynamic
      include: ["*"]
      exclude: ["*gate"]

    # Override: promote sensitive layers to W8A8
    - type: "linear_quant"
      qconfig: *default_w8a8_dynamic
      include:
        - "model.layers.14.mlp.down_proj"
        - "model.layers.31.self_attn.o_proj"
        - "model.layers.0.mlp.down_proj"
```

**When to use**: Many layers are flagged (5–15%); pure exclusion would waste too much memory.

______________________________________________________________________

### Strategy 3: Pattern-Level Protection (when scores scatter by module type)

If sensitivity analysis shows a consistent module type (e.g., all `down_proj` layers score high), protect the entire module type rather than individual layer indices.

```yaml
exclude:
  - "*mlp.down_proj*"   # All down_proj layers
  - "*self_attn.o_proj*"  # All output projections
```

Or promote them all to W8A8 within a `group`.

______________________________________________________________________

## 5. Iterative Refinement

Sensitivity analysis is not a one-shot fix. Follow this loop:

1. Run analysis → identify top-K sensitive layers
1. Apply Strategy 1, 2, or 3 → re-quantize
1. Evaluate accuracy on target benchmark (see GSM8K evaluation below)
1. If still degraded: lower `--topk` threshold (protect more layers) or switch metric
1. If accuracy recovered but memory/speed unacceptable: reduce the protected set

For accuracy and performance evaluation commands, see [ais_bench.md](ais_bench.md).

**Typical convergence**: 2–3 iterations.

**When to escalate to auto-tuning**: If manual layer protection does not close the accuracy gap after 3 iterations, use `msmodelslim tune` with an `evaluation` block targeting your benchmark. See the auto-tuning workflow in the msmodelslim docs.

______________________________________________________________________

## 6. Common Patterns and Their Fixes

| Symptom | Likely Cause | Fix |
| :--- | :--- | :--- |
| Math/reasoning accuracy drops | First/last layers or `down_proj` outliers | Exclude or promote first 3 + last 3 layers |
| Attention-heavy tasks degrade | `o_proj` or `v_proj` sensitive | Run `--metrics attention_mse`, protect `*self_attn*` |
| MoE model: expert accuracy drops | Expert `down_proj` outliers | Protect boundary expert layers by index |
| All metrics show uniform sensitivity | Calibration dataset mismatch | Re-run with a domain-matched calibration set |
| High scores on `lm_head` only | Normal — always excluded | Verify `lm_head` is in `exclude` list |

______________________________________________________________________

## 7. Full Example: W4A8 Config with Sensitivity-Derived Exclusions

```yaml
apiversion: modelslim_v1
metadata:
  config_id: qwen3_32b_w4a8_sensitivity_tuned
  label:
    w_bit: 4
    a_bit: 8

default_w8a8_dynamic: &default_w8a8_dynamic
  act:    {scope: "per_token",   dtype: "int8", symmetric: true, method: "minmax"}
  weight: {scope: "per_channel", dtype: "int8", symmetric: true, method: "minmax"}

default_w4a8_dynamic: &default_w4a8_dynamic
  act:    {scope: "per_token",   dtype: "int8", symmetric: true, method: "minmax"}
  weight: {scope: "per_channel", dtype: "int4", symmetric: true, method: "ssz"}

spec:
  process:
    - type: "flex_smooth_quant"
      enable_subgraph_type: ['norm-linear']
      include: ['*']

    - type: "group"
      configs:
        # Base W4A8 for all layers
        - type: "linear_quant"
          qconfig: *default_w4a8_dynamic
          include: ["*"]
          exclude: ["*gate"]

        # W8A8 for sensitivity-analysis-derived layers
        - type: "linear_quant"
          qconfig: *default_w8a8_dynamic
          include:
            # Paste top-K output from `msmodelslim analyze` here
            - "model.layers.14.mlp.down_proj"
            - "model.layers.31.self_attn.o_proj"
            - "model.layers.0.mlp.down_proj"

  save:
    - type: "ascendv1_saver"
      part_file_size: 4

dataset: mix_calib.jsonl
```
