# GPU 基线目录规范

## 适用场景

当官方没有提供可直接使用的训练或推理基线时，先向用户确认 GPU 基线协作方式；如果用户选择“把 GPU 结果放到本地目录，由 agent 继续分析”，就按本规范组织目录。

## 使用顺序

1. 先确认用户允许 agent 读取本地目录。
2. 让用户给出目录路径。
3. 先运行 `scripts/scan_baseline_bundle.py` 识别目录内容。
4. 再根据场景调用 `scripts/compare_loss.py` 或 `scripts/compare_inference.py`。

## 推荐目录结构

可以只提供 GPU 侧结果，也可以同时提供 GPU 与昇腾两侧结果。推荐结构如下：

```text
bundle-root/
  manifest.json
  training/
    gpu/
      logs/
        train.log
        eval.log
      metrics/
        metrics.json
      config/
        train.yaml
      run/
        command.txt
    ascend/
      logs/
      metrics/
      config/
      run/
  inference/
    gpu/
      inputs/
        samples.jsonl
      outputs/
        predictions.jsonl
      metrics/
        metrics.json
      config/
        infer.yaml
      run/
        command.txt
    ascend/
      inputs/
      outputs/
      metrics/
      config/
      run/
  dump/
    gpu/
      manifest.json
      tensors/
    ascend/
      manifest.json
      tensors/
```

如果用户现有目录不是这个结构，不要强行要求重构。先扫描现有目录，再基于真实文件路径工作。

## 每类场景最低需要的文件

### 训练对齐

最低建议包含：

- 训练日志，至少一份
- `val_loss` 或 `test_loss` 结果，如果有
- 训练配置文件
- 启动命令或关键运行参数

优先推荐：

- GPU 侧：`train.log`、`metrics.json`、`train.yaml`、`command.txt`
- 昇腾侧：同类文件

### 推理对齐

最低建议包含：

- 样例输入或输入标识
- 模型输出
- 指标文件
- 推理配置或启动命令

优先推荐：

- GPU 侧：`samples.jsonl`、`predictions.jsonl`、`metrics.json`、`command.txt`
- 昇腾侧：同类文件

### Dump 排查

最低建议包含：

- dump manifest
- 输入张量或输入标识
- 中间张量或最终输出
- 版本和命令记录

## 命名建议

- 训练日志：`train.log`、`eval.log`、`test.log`
- 指标文件：`metrics.json`、`scores.json`、`results.csv`
- 推理输出：`predictions.jsonl`、`outputs.json`、`answers.txt`
- 配置文件：`train.yaml`、`infer.yaml`
- 命令文件：`command.txt`
- dump 清单：`manifest.json`

## Manifest 建议字段

参考 `assets/templates/baseline-bundle-manifest.example.json`。建议至少包含：

- `bundle_version`
- `task_type`
- `model_name`
- `baseline_source`
- `sides`
- `files`
- `notes`

## 建议执行命令

```bash
python scripts/scan_baseline_bundle.py /path/to/bundle
python scripts/scan_baseline_bundle.py /path/to/bundle --expect training --write-manifest manifest.detected.json
python scripts/compare_loss.py gpu/train.log ascend/train.log --metric loss --metric val_loss
python scripts/compare_inference.py /path/to/gpu /path/to/ascend
```

## Agent 的判断原则

- 目录结构不规范不等于不能分析。先扫描，再决定缺什么。
- 如果 GPU 侧文件存在，但昇腾侧文件不存在，可以先读取 GPU 侧并告诉用户还缺哪些昇腾侧结果。
- 如果两侧文件都不完整，不要强行得出对齐结论，只返回“已发现文件”和“还缺的证据”。
