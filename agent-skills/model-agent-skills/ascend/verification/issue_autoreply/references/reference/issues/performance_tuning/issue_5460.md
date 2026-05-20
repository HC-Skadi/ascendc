# Issue #5460: 【Feature】GLM4.6 support mtp with fullgraph

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
GLM4.6 support mtp with fullgraph to improve performance

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?
`
export HCCL_BUFFSIZE=1024
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export HCCL_OP_EXPANSION_MODE=AIV

vllm serve /weight/glm4.6_w8a8_with_float_mtp \
  --data-parallel-size 1 \
  --tensor-parallel-size 16 \
  --seed 1024 \
  --served-model-name glm \
  --max-model-len 35000 \
  --max-num-batched-tokens 16384 \
  --max-num-seqs 16 \
  --trust-remote-code \
  --gpu-memory-utilization 0.9 \
  --speculative-config '{"num_speculative_tokens": 1, "model":"/weight/glm4.6_w8a8_with_float_mtp", "method":"mtp"}' \
  --compilation-config '{"cudagraph_capture_sizes": [1,2,4,8,16,32], "cudagraph_mode": "FULL_DECODE_ONLY"}' \
  --async-scheduling \
`

test case：
`
vllm bench serve \
  --backend vllm \
  --dataset-name pr

## 基本信息
- **编号**: #5460
- **作者**: 1092626063
- **创建时间**: 2025-12-29T04:02:53Z
- **关闭时间**: 2026-01-09T08:07:42Z
- **标签**: module:quantization, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5460)
