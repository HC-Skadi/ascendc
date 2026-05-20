# Issue #5524: [Bug][Structured Output]: xgrammar type mismatching error on `apply_token_bitmask_inplace_cpu`

## 基本信息

- **编号**: #5524
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5524
- **创建时间**: 2025-12-30T09:49:15Z
- **关闭时间**: 2026-01-23T01:52:57Z
- **更新时间**: 2026-01-23T01:52:57Z
- **提交者**: @wjunLu
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```
- vllm: 0.14.0rc1.dev173+g39512aba7.empty
- vllm_ascend: 0.13.0rc2.dev15+g45c3c279e
</details>



### 🐛 Describe the bug

### 1. Issue Description
The `indices` parameter in `apply_token_bitmask_inplace_cpu` was passed incorrectly as a `torch.Tensor`, but it was expected to be a `List[int]`

<img width="2554" height="591" alt="Image" src="https://github.com/user-attachments/assets/14f1fe23-37f2-4b78-9368-277d8ddff90a" />

### 2. Cause Summary
- Upstream vllm just enabled asynchronous scheduling: https://github.com/vllm-project/vllm/pull/27614

<img width="1499" height="875" alt="Image" src="https://github.com/user-attachments/assets/1f8ee39f-989f-4b1a-ab8c-2c8f80994167" />

where the `indices` param was changed from `List[int]` to `torch.Tensor`

- Though the interface supports a union `List[int]` and `torch.Tensor` in `xgrammar`

![Image](https://github.com/user-attachments/assets/f32110cd-0463-4dc1-b3a3-fc714acd720c)

- However, the actual implementation only supports `List[int]`

![Image](https://github.com/user-attachments/assets/c106dea5-acda-4378-bb79-3685d1438537)

### 3. Solution

- Currently: skip `tests/e2e/singlecard/test_aclgraph_accuracy.p`
- Contribute an Bugfix to `xgrammar`: https://github.com/mlc-ai/xgrammar/pull/507
