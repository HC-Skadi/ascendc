# 推理与指标对比指南

## 目的

当用户已经提供 GPU 与昇腾的推理结果、指标文件或结果目录时，优先使用 `scripts/compare_inference.py` 做结构化对比，而不是手工逐行看文件。

## 适用输入

脚本支持以下输入形式：

- 两个 JSON 文件
- 两个 JSONL 文件
- 两个 CSV 或 TSV 文件
- 两个文本文件
- 两个目录

目录模式适合比较 GPU 目录与昇腾目录下的同名输出文件和指标文件。

## 使用建议

### 比较单个指标文件

```bash
python scripts/compare_inference.py gpu/metrics.json ascend/metrics.json
python scripts/compare_inference.py gpu/results.csv ascend/results.csv
```

### 比较单个推理输出文件

```bash
python scripts/compare_inference.py gpu/predictions.jsonl ascend/predictions.jsonl
python scripts/compare_inference.py gpu/answers.txt ascend/answers.txt
```

### 比较两个目录

```bash
python scripts/compare_inference.py gpu/ ascend/
python scripts/compare_inference.py gpu/ ascend/ --atol 1e-5 --rtol 1e-4
```

## 容差设置

- `--atol` 控制绝对误差
- `--rtol` 控制相对误差

如果项目没有官方阈值，先使用默认容差做扫描，再根据模型任务特征解释结果，不要仅凭一次数值不等就认定不对齐。

## 输出解读

脚本会给出：

- 比较类型
- 对齐成功的数值项数量
- 不一致的数值项数量
- 精确匹配与不匹配的文本或结构项数量
- 缺失键、额外键或长度不一致情况
- 前若干个差异样例

## 何时升级

- 如果只是少量浮点差异，且任务指标一致，先停留在推理层，不必马上做 dump。
- 如果指标文件差异明显，或逐样本输出从较早位置开始系统性偏离，再升级到 dump 排查。
- 如果目录对比发现两侧关键文件根本不成对，先让用户补齐目录，不要直接继续分析。
