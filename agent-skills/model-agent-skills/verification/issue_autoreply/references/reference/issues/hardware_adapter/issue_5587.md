# Issue #5587: Ears,a efficient adaptive rejection sampling for accelerating speculator

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
https://github.com/vllm-project/vllm-ascend/issues/5471

### Does this PR introduce _any_ user-facing change?
Added macro definition switch VLLM_EARS_TOLERANCE

### How was this patch tested?
export ASCEND_RT_VISIBLE_DEVICES=14,15
export VLLM_EARS_TOLERANCE=0.3
vllm serve /data2/weights/Qwen_Qwen3-32B \
    -tp 2 \
    --port 9000 \
    --served-model-name Qwen3-32B \
    --speculative-config '{
    "model": "/data2/weights/scd/RedHatAI/Qwen3-32B-speculator.eagle3",
    "num_speculative_tokens": 4,
    "method": "eagle3",
    "draft_tensor_parallel_size": 1
  }'

evalscope perf --url "http://localhost:9001/v1/chat/completions" --parallel 1 --model Qwen3-32B --number 10 --api openai --dataset openqa --temperature 0.9 --stream

<img width="427" height="236" alt="image" src="https://github.com/user-attachments/assets/c3525d3c-5f27-4d82-8939-d9ffb60302e0" />

evalscope eval --model Qwen3-32B --api-url http://localhost:9000/v1 

## 基本信息
- **编号**: #5587
- **作者**: sunchendd
- **创建时间**: 2026-01-04T09:39:35Z
- **关闭时间**: 2026-01-26T06:46:12Z
- **标签**: module:core, merge-conflicts

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5587)
