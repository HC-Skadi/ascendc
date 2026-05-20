# Issue #5524: [Bug][Structured Output]: xgrammar type mismatching error on `apply_token_bitmask_inplace_cpu`

**类型**: Issue

## 问题背景
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

![Image](htt

## 基本信息
- **编号**: #5524
- **作者**: wjunLu
- **创建时间**: 2025-12-30T09:49:15Z
- **关闭时间**: 2026-01-23T01:52:57Z
- **标签**: bug

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/5524)
