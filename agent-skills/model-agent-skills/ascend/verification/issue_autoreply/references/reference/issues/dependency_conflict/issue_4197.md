# Issue #4197: [Bug]: ValueError: Unknown attention backend: 'ASCEND'.

## 基本信息

- **编号**: #4197
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4197
- **创建时间**: 2025-11-14T06:58:51Z
- **关闭时间**: 2025-11-19T11:03:20Z
- **更新时间**: 2025-11-19T11:03:20Z
- **提交者**: @amy-why-3459
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
vllm:  main
vllm-ascend: main
模型：Qwen2.5-VL-7B-Instruct

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

ValueError: Unknown attention backend: 'ASCEND'. Valid options are: FLASH_ATTN, TRITON_ATTN, XFORMERS, ROCM_ATTN, ROCM_AITER_MLA, ROCM_AITER_FA, TORCH_SDPA, FLASHINFER, FLASHINFER_MLA, TRITON_MLA, CUTLASS_MLA, FLASHMLA, FLASHMLA_SPARSE, FLASH_ATTN_MLA, PALLAS, IPEX, NO_ATTENTION, FLEX_ATTENTION, TREE_ATTN, ROCM_AITER_UNIFIED_ATTN, CPU_ATTN, TORCH_SDPA
(APIServer pid=15833) Traceback (most recent call last):
