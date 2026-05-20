# Issue #6551: [Refactor]refactor p2p connector

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Redundant code is removed, and repeated logic is combined through the p2p connector refactor, making the code easy to extend.

### Does this PR introduce _any_ user-facing change?
NA

### How was this patch tested?
P节点：
```
vllm serve /mnt/weight/DeepSeek-V3.2-Exp-W8A8 \
  --host 0.0.0.0 \
  --port 8002 \
  --data-parallel-size 2 \
  --tensor-parallel-size 8 \
  --enable-expert-parallel \
  --seed 1024 \
  --served-model-name model \
  --max-model-len 8192 \
  --max-num-batched-tokens 8192 \
  --max-num-seqs 16 \
  --enforce-eager \
  --trust-remote-code \
  --gpu-memory-utilization 0.92 \
  --quantization ascend \
  --async-scheduling \
  --additional-config '{"ascend_scheduler_config":{"enabled":true}}' \
  --kv-transfer-config \
  '{
        "kv_connector": "MultiConnector",
        "kv_role": "kv_producer",
        "kv_connector_extra_config": {
                "use_layerwise": false,
                "connector

## 基本信息
- **编号**: #6551
- **作者**: luoxiaolin712
- **创建时间**: 2026-02-05T03:03:48Z
- **关闭时间**: 2026-02-07T01:27:16Z
- **标签**: 无

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6551)
