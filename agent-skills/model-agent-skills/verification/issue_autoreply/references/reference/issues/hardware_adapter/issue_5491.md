# Issue #5491: [Graph][Fusion] Add AddRMSNorm(with bias)

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR builds upon PR #5011 and aims to further enhance the npu_graph_ex_passes module. Based on prior work, we have added graph optimization support for the add_rms_quant fused operator in scenarios where a bias term is present—ensuring the fusion pattern is correctly registered and matched into the computation graph.

For validation, we switched to the Qwen3-235B-A22B-W8A8 model. Benchmark results show that, compared to the unfused baseline, enabling this fusion pass significantly improves inference throughput for W8A8 quantized models.  
For more details can refer to the RFC:https://github.com/vllm-project/vllm-ascend/issues/4715



### Does this PR introduce _any_ user-facing change?
no
### How was this patch tested?
```
llm = LLM(
        model=model,
        tensor_parallel_size=GPUs_per_dp_rank,
        enforce_eager=False,
        enable_expert_parallel=enable_expert_parallel,
        trust_remote_code=trust_remote_code,

## 基本信息
- **编号**: #5491
- **作者**: ForBetterCodeNine
- **创建时间**: 2025-12-29T13:18:59Z
- **关闭时间**: 2025-12-31T09:10:26Z
- **标签**: 无

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5491)
