# Issue #1791: [Bug]: Qwen/Qwen3-30B-A3B accuracy low when tp=2 dp=2

## 基本信息

- **编号**: #1791
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1791
- **创建时间**: 2025-07-14T13:02:25Z
- **关闭时间**: 2025-10-10T09:26:03Z
- **更新时间**: 2025-10-10T09:26:03Z
- **提交者**: @zhangxinyuehfad
- **评论数**: 3

## 标签

bug; duplicate

## 问题描述

### Your current environment

**vllm**:  v0.9.2
**vllm-ascend**: v0.9.2rc1


### 🐛 Describe the bug

**lm-eval command**:
```bash
lm_eval \
  --model vllm \
  --model_args '{
    "pretrained": "/root/.cache/modelscope/hub/models/Qwen/Qwen3-30B-A3B",
    "max_model_len": 4096,
    "dtype": "auto",
    "tensor_parallel_size": 2,
    "data_parallel_size": 2,
    "gpu_memory_utilization": 0.8,
    "enforce_eager": true,
    "enable_expert_parallel": true,
    "additional_config": {
      "expert_tensor_parallel_size": 2
    }
  }' \
  --tasks gsm8k \
  --apply_chat_template \
  --fewshot_as_multiturn \
  --batch_size auto \
  --num_fewshot 5 \
  --output ./
```
**accuracy result**:
Tasks|Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|-----|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.1653|±  |0.0102|
|     |       |strict-match    |     5|exact_match|↑  |0.1547|±  |0.0100|

