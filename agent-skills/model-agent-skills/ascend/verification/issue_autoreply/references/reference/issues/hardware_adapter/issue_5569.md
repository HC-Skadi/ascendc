# Issue #5569: [Graph][Fusion] Add AddRMSNormSPPattern and AddRMSNormSPPatternWithBias

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR builds upon PR https://github.com/vllm-project/vllm-ascend/pull/5011 and aims to further enhance the npu_graph_ex_passes module. Based on prior work, we have added graph optimization support for the add_rms_quant fused operator in scenarios where a bias term is present—ensuring the fusion pattern is correctly registered and matched into the computation graph.

For validation, we switched to the Qwen3-235B-A22B-W8A8 model for SPPatternWithBias and Qwen3-32B model for SPPattern. Benchmark results show that, compared to the unfused baseline, enabling this fusion pass significantly improves inference throughput for W8A8 quantized models.
For more details can refer to the RFC:https://github.com/vllm-project/vllm-ascend/issues/4715
### Does this PR introduce _any_ user-facing change?
no
### How was this patch tested?
```
llm = LLM(
        model=model,
        tensor_parallel_size=GPUs_per_dp_rank,
        enforce_eager=False,
    

## 基本信息
- **编号**: #5569
- **作者**: ForBetterCodeNine
- **创建时间**: 2026-01-04T02:39:31Z
- **关闭时间**: 2026-01-07T01:03:45Z
- **标签**: 无

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5569)
