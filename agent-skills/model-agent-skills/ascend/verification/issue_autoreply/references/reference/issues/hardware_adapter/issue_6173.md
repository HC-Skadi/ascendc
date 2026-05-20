# Issue #6173: [Lint]Style: Convert `vllm-ascend/` to ruff format(Batch #10)

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
**Scope of Changes**:
| File Path |
| :--- |
|`vllm_ascend/ops/layer_shard_linear.py`|
|`vllm_ascend/ops/linear.py`|
|`vllm_ascend/ops/linear_op.py`|
|`vllm_ascend/worker/worker.py`|
| ` vllm_ascend/patch/worker/patch_bert.py` |
| ` vllm_ascend/patch/worker/patch_deepseek.py` |
| ` vllm_ascend/patch/worker/patch_distributed.py` |
| ` vllm_ascend/patch/worker/patch_module.py` |
| ` vllm_ascend/patch/worker/patch_multimodal_merge.py` |
| ` vllm_ascend/patch/worker/patch_qwen3_next.py` |
| ` vllm_ascend/patch/worker/patch_qwen3_next_mtp.py` |
| ` vllm_ascend/patch/worker/patch_rejection_sampler.py` |
| ` vllm_ascend/patch/worker/patch_rope.py` |
| ` vllm_ascend/patch/worker/patch_triton.py` |
| ` vllm_ascend/patch/worker/patch_unquantized_gemm.py` |
| ` vllm_ascend/patch/worker/patch_v2_egale.py` |
|` vllm_ascend/worker/npu_input_batch.py`|
|` vllm_ascend/worker/v2/aclgraph_utils.py`|
|` vllm_ascend/worker/v2/attn_utils.py`|
|

## 基本信息
- **编号**: #6173
- **作者**: MrZ20
- **创建时间**: 2026-01-23T02:41:06Z
- **关闭时间**: 2026-02-06T07:35:06Z
- **标签**: module:ops

## 涉及版本
- vLLM: v0.14.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6173)
