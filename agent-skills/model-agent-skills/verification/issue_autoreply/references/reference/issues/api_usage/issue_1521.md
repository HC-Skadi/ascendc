# Issue #1521: [Question]: About CPU tensor creation for attention mask and non-blocking transfer

## 基本信息

- **编号**: #1521
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1521
- **创建时间**: 2025-06-30T06:44:36Z
- **关闭时间**: 2025-12-24T10:59:26Z
- **更新时间**: 2025-12-24T10:59:26Z
- **提交者**: @jianzs
- **评论数**: 1

## 标签

question

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

https://github.com/vllm-project/vllm-ascend/blob/e4df0a4395b13967e20709ff2c9350c26b505f8c/vllm_ascend/attention/attention.py#L126-L146

I'm looking at the attention mask creation code here, and I have two concerns:

1. Performance Consideration:
   The code creates attention masks on CPU before transferring them to the device. I'm wondering about the performance implications of this approach compared to creating the masks directly on NPU.

2. Non-blocking Transfer Issue:
   The code attempts to use non-blocking transfer (`non_blocking=True`), but the CPU tensors are created without `pin_memory=True`. As far as I understand, this means the non-blocking transfer won't be effective since the memory isn't pinned.

Questions:
- Has there been any performance comparison between CPU vs NPU for attention mask creation?
- Should we consider adding `pin_memory=True` to enable proper non-blocking transfers?

