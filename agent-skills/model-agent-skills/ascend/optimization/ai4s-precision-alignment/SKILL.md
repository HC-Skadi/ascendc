---
name: ascend-ai4s-precision-alignment
description: 面向昇腾 NPU 的 AI4S 模型精度对齐与问题定位。用于比较 GPU 与昇腾或官方基线与昇腾之间的训练 loss、推理输出和任务指标，梳理模型特定的对齐要求，并在精度不一致时采集和分析定向 dump 证据。使用本 skill 时必须先确认官方 README、官方示例或 benchmark 是否已给出基线；若官方未提供，必须先询问用户 GPU 基线来源，禁止默认使用 CPU 结果作为最终对齐基线。
---

# 昇腾 AI4S 精度对齐

## 概述

用于在昇腾 NPU 结果与可信基线之间做 AI4S 模型精度对齐。先确认基线来源，再固定对比约束，然后根据现象进入训练对齐、推理对齐或 dump 排查流程。

## 快速开始

1. 先确认模型类型与基线来源。
   判断模型属于哪类 AI4S 任务；如不清楚，读取 `references/model-family-hints.md`。
   先检查官方 README、官方示例、官方 benchmark 或官方文档是否已经给出训练或推理基线。
2. 再固定对比约束。
   记录模型仓库与 commit、checkpoint、数据集划分、seed、batch size、精度模式、优化器、scheduler、分布式策略、loss 定义和后处理逻辑。
3. 再选择流程。
   `loss` 或收敛异常时进入训练对齐。
   任务指标或样例输出异常时进入推理对齐。
   仅在高层比较已经确认真实差异后进入 dump 排查。
4. 最后输出结论。
   明确说明是否对齐、比较覆盖范围、使用了什么阈值、最可能原因是什么，以及下一步需要补什么证据。

## 强制规则

- 先查官方基线，再写或运行精度对比脚本。
- 基线来源优先级固定为：
  1. 官方 README、官方示例、官方 benchmark、官方文档
  2. 用户提供的 GPU 真实运行结果
- 如果官方没有提供足够基线，必须先询问用户 GPU 基线来源；不能默认基线存在。
- 禁止默认做 `CPU vs NPU` 或 `CPU vs Ascend` 作为最终精度对齐结论。
- 只有以下三种情况可以做 CPU 对比：
  1. 用户明确要求检查 CPU vs NPU
  2. 官方文档明确把 CPU 结果当作标准基线
  3. 只把 CPU 结果当作本地调试辅助，用于定位 PyTorch/NPU 路径问题
- 如果做了 CPU 对比但它不是官方或用户确认的正式基线，报告中必须明确标注“仅用于调试，不作为最终精度对齐结论”。
- 阈值必须在比较前声明。不能先看到 mismatch，再临时放宽阈值后直接写成“全部对齐”。
- 官方样例级基线只能证明“样例级推理对齐”，不能直接上升为“整个模型已完成精度对齐”。
- 只比较严格同条件的运行结果。不要拿 seed、数据顺序、loss reduction、batch shape、prompt 模板、解码参数或后处理不同的结果直接对比。
- 每一个“不对齐”判断都要附证据：命令、版本、配置片段、日志片段、样例输入输出和比较脚本。

## 基线来源策略

按以下顺序确认基线：

1. 官方 README、官方示例、官方 benchmark 或官方文档
2. 用户提供的 GPU 真实运行结果

如果第 1 类来源不存在或不足以支撑结论，必须先向用户确认以下内容后再继续：

- 是否已有 GPU 侧真实结果
- 如果有，结果放在哪个本地目录
- 目录中是训练日志、推理输出、指标文件还是 dump 文件
- 是否希望 agent 直接读取本地目录继续分析
- 如果没有现成结果，是否由用户先在 GPU 上跑出结果后再继续

更详细的协作规则见 `references/baseline-policy.md`。

## 本地目录工作流

当用户提供 GPU 目录或对比目录时，按以下顺序执行：

1. 运行 `scripts/scan_baseline_bundle.py <dir>` 识别目录中的日志、指标、输出、配置和 dump 文件。
2. 如果是训练场景，优先比较日志和指标；必要时用 `scripts/compare_loss.py`。
3. 如果是推理场景，优先比较输出文件和指标文件；必要时用 `scripts/compare_inference.py`。
4. 只有在高层比较确认存在真实差异后，才进入 dump 采集和首漂移定位。

目录规范见 `references/baseline-bundle-spec.md`。

## 训练精度对齐

- 先确认官方训练基线是否存在；不存在时先问用户 GPU 训练结果来源，不要先写 CPU 对比脚本。
- 先比较最终稳定的 `loss`，再看整体趋势。
- 如果每个 epoch 只打印一个 loss，比较最终值、均值、最小值、最大值和波动性。
- 如果有 step 级 loss，比较前期收敛、中期振荡和最终稳定区间。
- 如果有 `val_loss` 或 `test_loss`，优先比较这些指标，再决定训练 loss 的权重。
- 如果从第一个 batch 就出现差异，优先排查数据预处理、随机种子、前向精度和不支持算子。
- 如果前期一致、后期逐渐偏离，优先排查优化器状态、梯度缩放、reduction 语义、scheduler 行为和分布式 all-reduce 差异。
- 当用户提供目录而不是单个日志文件时，先运行 `scripts/scan_baseline_bundle.py`，再从识别出的 `log` 或 `metrics` 文件中选择训练比较输入。

## 推理精度对齐

- 先看模型 README 和官方示例，再决定比较方法。
- 如果官方已经给出推理样例或标准输出，优先直接比较 NPU 输出与官方值；不要因为当前环境能跑 PyTorch CPU 就默认改成 CPU 对比。
- 如果官方基线不足，必须先询问用户 GPU 基线来源，而不是自行构造本地 CPU 基线。
- 固定 tokenizer、归一化、padding、prompt 模板、解码参数和后处理逻辑。
- 先比较任务指标，再比较同一批样本上的原始输出。
- 对生成式模型，固定 `temperature`、`top_k`、`top_p`、`max_new_tokens` 以及采样或 beam search 相关参数。
- 如果用户已经提供 GPU 与昇腾的推理结果或结果目录，优先使用 `scripts/compare_inference.py` 做结构化比较，而不是手工逐行看文件。
- 如果官方只提供少量示例输出，最终报告必须写清“仅验证了官方示例覆盖范围”。

## 精度不对齐排查与 Dump 采集

- 只有在高层比较确认存在真实差异后，才进入 dump 采集。
- 先缩小复现范围：单卡、单进程、固定 seed、最小 batch、最小样本。
- 只采最有用的证据：输入 tensor、关键中间 tensor、最终 logits 或预测结果，以及 dtype、shape、scale 等元数据。
- 对序列模型，尽量把范围缩小到固定 `token_range` 或某个解码步。
- 写 dump 命令或产物清单前，先看 `references/msprobe-dump-guide.md` 和 `references/dump-localization-template.md`。
- 先证明漂移从哪里开始，再怀疑下游层。

## 报告约束

最终报告至少要包含：

- 基线来源及其优先级说明
- 比较覆盖范围
- 对比约束摘要
- 数值对比表
- 预先声明的阈值或验收标准
- 明确区分“已证实结论”和“合理推测”
- 下一步动作优先级

如果使用了 CPU 对比但它不是正式基线，必须单独写明：

- CPU 对比只用于调试
- 它不能证明 NPU 与官方模型一致
- 它不能替代官方基线或用户 GPU 基线

## 常见误区

读取 `references/common-pitfalls.md`，避免以下错误：

- 未确认官方基线就先写对比脚本
- 因为本地 CPU 更容易跑通，就默认做 CPU vs NPU
- 先给出 PASS 结论，再回头补找基线
- 看到 mismatch 后临时放宽阈值
- 用少量官方样例对齐结果，宣称整个模型已经完成精度对齐

## 参考资料索引

| File | Load when |
| --- | --- |
| `references/alignment-playbook.md` | 需要完整的训练或推理对齐流程时 |
| `references/baseline-policy.md` | 官方未提供基线，需要向用户确认 GPU 基线来源和协作方式时 |
| `references/baseline-bundle-spec.md` | 用户把 GPU 结果放到本地目录，需要识别目录结构和最少必备文件时 |
| `references/checklists.md` | 需要快速核对配置项或证据项时 |
| `references/inference-comparison.md` | 需要比较推理输出、指标文件或结果目录时 |
| `references/model-family-hints.md` | 需要按 AI4S 模型类型选择比较对象和判断重点时 |
| `references/dump-localization-template.md` | 需要组织 dump 采集结果并定位首漂移时 |
| `references/msprobe-dump-guide.md` | 需要做 dump 采集或定位漂移起点时 |
| `references/common-pitfalls.md` | 需要避免基线选择、CPU 对比和报告范围方面的常见错误时 |
