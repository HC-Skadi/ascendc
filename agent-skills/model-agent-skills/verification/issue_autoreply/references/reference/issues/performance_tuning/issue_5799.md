# Issue #5799: [MM][Perf] Merge Q/K split to simplify AscendApplyRotaryEmb for better performance

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
- Use upstream util function (`_pre_process()` and `_post_process()`) to reduce redundant codes. (Find more details at https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/rotary_embedding/common.py#L184-L213)
- Merge Q/K split to simplify the logic of calling `torch_npu.npu_rotary_mul()` for better performance (TPOT has been reduced by **6.22%**).

### Does this PR introduce _any_ user-facing change?
no.

### How was this patch tested?
#### ✅ Functional test

Launch the server:

```bash
export VLLM_USE_MODELSCOPE=True
vllm serve /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-VL-7B-Instruct \
--dtype bfloat16 \
--limit-mm-per-prompt '{"image": 1}' \
--max-model-len 16384 \
--max-num-batched-tokens 16384
```

Query the server:

```bash
curl -X POST http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "/root/.cache/modelscope/hub/models/Qwen

## 基本信息
- **编号**: #5799
- **作者**: shen-shanshan
- **创建时间**: 2026-01-12T07:43:24Z
- **关闭时间**: 2026-01-13T07:47:24Z
- **标签**: module:ops, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5799)
