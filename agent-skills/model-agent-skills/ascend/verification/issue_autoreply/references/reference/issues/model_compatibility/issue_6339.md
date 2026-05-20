# Issue #6339: [Feature]KV pool supports sparse attention

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
The kv pooling feature is adapted to Sparse Attention to support models such as Deepseek V3.2.

### Does this PR introduce _any_ user-facing change?
NA

### How was this patch tested?
```
vllm serve /mnt/weight/DeepSeek-V3.2-Exp-W8A8 \
  --host $local_ip \
  --port 8002 \
  --served-model-name model \
  --data-parallel-size 1 \
  --tensor-parallel-size 8 \
  --prefill-context-parallel-size 2 \
  --decode-context-parallel-size 1 \
  --cp-kv-cache-interleave-size 128 \
  --block-size 128 \
  --enable-expert-parallel \
  --no-enable-prefix-caching \
  --no-enable-chunked-prefill \
  --max-num-seqs 4 \
  --max-model-len 8192 \
  --max-num-batched-tokens 8192 \
  --gpu-memory-utilization 0.95 \
  --trust-remote-code \
  --enforce-eager \
  --quantization ascend \
  --additional_config '{"ascend_scheduler_config":{"enabled":false}}' \
  --kv-transfer-config \
    '{
            "kv_connector": "AscendStoreConnector",
   

## 基本信息
- **编号**: #6339
- **作者**: luoxiaolin712
- **创建时间**: 2026-01-28T06:43:37Z
- **关闭时间**: 2026-02-05T02:36:52Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6339)
