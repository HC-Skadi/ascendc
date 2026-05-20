# 敏感度分析流程

当量化模型相较 FP32 基线出现**精度下降**时，请使用本流程。目标是识别对量化最敏感的层，并通过 YAML 配置对这些层进行保护。

______________________________________________________________________

## 1. 触发条件

以下场景建议执行敏感度分析：

- 量化模型在目标基准上的精度下降超过可接受阈值
- 某些任务类型（数学推理、代码、长上下文）明显退化，而其他类型基本稳定
- 首层/末层保护（见 `msmodelslim.md` 第 3.6 节）未能解决问题

______________________________________________________________________

## 2. 执行敏感度分析

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

**关键参数**：

| 参数 | 建议值 | 说明 |
| :--- | :--- | :--- |
| `--metrics` | 见下表 | 按问题类型选择度量方式 |
| `--topk` | 15–20 | 输出最敏感层数量 |
| `--pattern` | `["*"]`（默认）或特定模式 | 将范围收敛到可疑层类型 |
| `--calib_dataset` | 必须与量化时一致 | 一致性非常关键，需使用量化阶段相同的数据文件 |

**度量方式选择**：

| 度量 | 适用场景 | 算法 |
| :--- | :--- | :--- |
| `kurtosis` | **默认。** 通用场景；可识别激活分布尖峰/集中层 | `E[(X-μ)⁴]/σ⁴ - 3` |
| `std` | 快速扫描；常规量化场景 | `max(|max|, |min|) / std` |
| `quantile` | 高精度目标；异常值会干扰 std 时 | 基于 IQR：`2·max_abs / 254 / (Q3−Q1)` |
| `attention_mse` | 注意力精度专项退化；DeepSeek-V3/R1 系列 | 每层 FP 与 INT 输出的 MSE |

**用 `--pattern` 缩小范围**：若怀疑某类模块（如 MLP down_proj），可仅分析该类：

```bash
--pattern '["*.down_proj*", "*.o_proj*"]'
```

______________________________________________________________________

## 3. 解读输出结果

命令会在 stdout 打印两段内容：

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

**分数含义**：分数越高代表越敏感，量化后精度损失风险越高。重点关注 Top 10–20。

**聚簇 vs 离散模式**：

- 分数集中在特定层号附近 → 按层号区间保护
- 分数在各层随机分散 → 按模块类型保护（如所有 `down_proj`）

______________________________________________________________________

## 4. 调整 YAML

根据敏感层数量和精度差距，选择以下三种策略之一。

### 策略 1：排除敏感层（最简单）

将输出中的 YAML 块直接粘贴到量化配置的 `exclude` 字段。被排除层保持 FP16/BF16。

```yaml
- type: "linear_quant"
  qconfig: *default_w4a8_dynamic
  include: ["*"]
  exclude:
    # 在此粘贴敏感度分析输出
    - "model.layers.14.mlp.down_proj"
    - "model.layers.31.self_attn.o_proj"
    - "model.layers.0.mlp.down_proj"
```

**适用场景**：精度差距较大，且被标记层占比较小（总层数 < 5%）。

**代价**：被排除层保持 FP16，会带来轻微显存增长。

______________________________________________________________________

### 策略 2：将敏感层提升到更高精度（混合精度）

不完全回退到 FP16，而是将敏感层从 W4A8 提升为 W8A8，在恢复精度的同时控制显存。

使用 `group` 处理器，在单独条目中列出敏感层并指定更高精度。对同一层，`group` 中**最后匹配**的条目生效。

```yaml
- type: "group"
  configs:
    # 基线：所有层使用 W4A8
    - type: "linear_quant"
      qconfig: *default_w4a8_dynamic
      include: ["*"]
      exclude: ["*gate"]

    # 覆盖：敏感层提升到 W8A8
    - type: "linear_quant"
      qconfig: *default_w8a8_dynamic
      include:
        - "model.layers.14.mlp.down_proj"
        - "model.layers.31.self_attn.o_proj"
        - "model.layers.0.mlp.down_proj"
```

**适用场景**：敏感层较多（5–15%）；纯排除会浪费较多显存。

______________________________________________________________________

### 策略 3：按模式保护（分数按模块类型离散时）

如果分析结果显示某类模块持续高分（如所有 `down_proj`），优先按模块类型统一保护，而非逐层号处理。

```yaml
exclude:
  - "*mlp.down_proj*"     # 所有 down_proj 层
  - "*self_attn.o_proj*"  # 所有输出投影层
```

也可以在 `group` 中统一将该类层提升到 W8A8。

______________________________________________________________________

## 5. 迭代优化

敏感度分析不是一次性修复，建议按如下闭环执行：

1. 运行分析，识别 Top-K 敏感层
1. 应用策略 1/2/3，重新量化
1. 在目标基准上评估精度（见下文 GSM8K）
1. 若仍退化：增大保护范围（提高 `--topk`）或切换度量方法
1. 若精度恢复但内存/速度不可接受：缩小保护集合

精度与性能评测命令见 [ais_bench.md](ais_bench.md)。

**典型收敛**：2–3 轮。

**何时升级到自动调优**：若手工保护 3 轮后仍无法弥合精度差距，使用带 `evaluation` 配置的 `msmodelslim tune`，并以目标基准作为优化目标。详细流程见 msmodelslim 文档中的自动调优部分。

______________________________________________________________________

## 6. 常见模式与修复建议

| 症状 | 可能原因 | 修复建议 |
| :--- | :--- | :--- |
| 数学/推理精度下降 | 首末层或 `down_proj` 异常值 | 排除或提升前 3 层 + 后 3 层 |
| 注意力相关任务退化 | `o_proj` 或 `v_proj` 敏感 | 使用 `--metrics attention_mse`，保护 `*self_attn*` |
| MoE 模型专家精度下降 | 专家 `down_proj` 异常值 | 按层号保护边界专家层 |
| 所有指标都均匀敏感 | 校准数据集不匹配 | 使用领域匹配的校准集重新分析 |
| 仅 `lm_head` 高分 | 正常现象（通常始终排除） | 确认 `lm_head` 在 `exclude` 列表中 |

______________________________________________________________________

## 7. 完整示例：带敏感度保护的 W4A8 配置

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
        # 全量层默认 W4A8
        - type: "linear_quant"
          qconfig: *default_w4a8_dynamic
          include: ["*"]
          exclude: ["*gate"]

        # 对敏感度分析命中的层使用 W8A8
        - type: "linear_quant"
          qconfig: *default_w8a8_dynamic
          include:
            # 在此粘贴 `msmodelslim analyze` 的 Top-K 输出
            - "model.layers.14.mlp.down_proj"
            - "model.layers.31.self_attn.o_proj"
            - "model.layers.0.mlp.down_proj"

  save:
    - type: "ascendv1_saver"
      part_file_size: 4

dataset: mix_calib.jsonl
```
