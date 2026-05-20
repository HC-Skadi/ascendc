---
name: ai4s-main
description: AI for Science 昇腾 NPU 总入口 Skill，用于在用户只给出 AI for Science 需求、模型名、TensorFlow/Keras 项目、精度对齐、性能采集或性能调优诉求时，判断应该进入精度对齐、Profiling 采集、性能调优、模型迁移或 TF 框架路线，并分流到对应子 skill。
keywords:
  - ai-for-science
  - ai4s
  - precision-alignment
  - accuracy
  - dump
  - profiling
  - performance-tuning
  - migration
  - tensorflow
  - pytorch
  - ascend
---

# AI for Science 总入口 Skill

本 Skill 只负责路线判断和子 skill 分流，不展开具体迁移、精度对齐或调优细节。
当用户只给出一个宽泛的 AI for Science 需求、模型名、TensorFlow/Keras 项目，或只说“帮我迁到昇腾/做精度对齐/采集 profiling/性能调优”时，先从这里判断进入哪个子 skill。

## 五条主路线

| 方向 | 进入条件 | 推荐子 Skill |
|------|------|------|
| 精度对齐 | 需要比较 GPU 与昇腾、官方基线与昇腾之间的训练 loss、推理输出、任务指标，或要做 dump 定位与首漂移排查 | [ascend-ai4s-precision-alignment](../ai4s-precision-alignment/SKILL.md) |
| Profiling 采集 | 代码已经能训练或推理，只需要采集 trace、分析热点算子、调用栈、内存或瓶颈 | [ai4s-profiling](../ai4s-profiling/SKILL.md) |
| 性能调优 | 模型已能跑通，需要通过调度优化、绑核、内存库替换等手段提升性能 | [ai4s-perf-tuning](../ai4s-perf-tuning/SKILL.md) |
| 模型迁移 | 已知模型名，或要把 AI4S 模型从 GPU/CUDA 迁移到昇腾 NPU | [ai4s-basic](../models/ai4s-basic/SKILL.md) 或模型专属 skill |
| TF 框架 | 原项目是 TensorFlow/Keras，需要决定保留 TensorFlow 还是改写到 PyTorch | [ascend-tf-community](../tf-framework/ascend-tf-community/SKILL.md) / [tf-to-pytorch](../tf-framework/tf-to-pytorch/SKILL.md) |

## 模型分流表

| 模型或任务 | 进入的 Skill | 说明 |
|------|------|------|
| 训练 loss 对齐、推理输出对齐、指标对齐、dump 定位 | [ascend-ai4s-precision-alignment](../ai4s-precision-alignment/SKILL.md) | 用于 GPU vs Ascend 或官方基线 vs Ascend 的精度对齐与证据采集 |
| Boltz2 | [boltz2](../models/boltz2/SKILL.md) | 蛋白结构预测与端到端推理复现 |
| BoltzGen | [boltzgen](../models/boltzgen/SKILL.md) | 生成式蛋白设计与逆折叠 |
| DeepFRI，保留 TensorFlow | [deepfri-tf-npu](../models/deepfri-tf-npu/SKILL.md) | 保留 TF 运行时和原始实现 |
| DeepFRI，迁移到 PyTorch | [deepfri](../models/deepfri/SKILL.md) | 做 TF 到 PyTorch 改写与权重转换 |
| DiffSBDD | [diffsbdd](../models/diffsbdd/SKILL.md) | 结构化药物设计与扩散推理 |
| GENERator | [generator](../models/generator/SKILL.md) | DNA 序列生成模型迁移 |
| Goedel-Prover | [goedel-prover](../models/goedel-prover/SKILL.md) | 基于 vLLM 的 Lean 4 自动定理证明模型迁移 |
| OligoFormer | [oligoformer](../models/oligoformer/SKILL.md) | siRNA 效能预测与 RNA-FM 依赖适配 |
| ProteinBERT | [proteinbert](../models/proteinbert/SKILL.md) | 蛋白语言模型权重转换、embedding 与微调 |
| 未沉淀的新模型 | [ai4s-basic](../models/ai4s-basic/SKILL.md) | 先走通用迁移流程，再沉淀模型专属 skill |

## 决策规则

1. 如果用户要做训练 loss 对齐、推理结果对齐、任务指标对齐，或已经明确提到 dump 采集、dump 定位、首漂移排查，直接进入 [ascend-ai4s-precision-alignment](../ai4s-precision-alignment/SKILL.md)。
2. 如果用户已经能跑，只是想采集 profiling 或定位性能问题，直接进入 [ai4s-profiling](../ai4s-profiling/SKILL.md)。
3. 如果用户已经能跑，想做性能调优（流水优化、绑核、tcmalloc 等），进入 [ai4s-perf-tuning](../ai4s-perf-tuning/SKILL.md)。
4. 如果用户明确要保留 TensorFlow/Keras 原始实现，进入 [ascend-tf-community](../tf-framework/ascend-tf-community/SKILL.md)。
5. 如果用户明确要迁移到 PyTorch，或后续要接入 `torch_npu` 生态、统一训练推理流程，进入 [tf-to-pytorch](../tf-framework/tf-to-pytorch/SKILL.md)。
6. 如果用户已经给出具体模型名，且当前诉求主要是迁移、适配或复现，优先进入对应模型 skill；只有在没有模型专属 skill 时，才进入 [ai4s-basic](../models/ai4s-basic/SKILL.md)。
7. 本 Skill 完成分流后，就在对应子 skill 中继续执行环境、适配、验证和参考资料读取，不在这里重复展开。
