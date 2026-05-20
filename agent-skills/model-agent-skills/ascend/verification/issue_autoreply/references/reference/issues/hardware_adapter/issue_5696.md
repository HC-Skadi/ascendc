# Issue #5696: Optimize the print info format when deprecated code is used in vllm-ascend

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
Optimize the warning print information format when detects depredated code is used in vllm-ascend.

### Does this PR introduce _any_ user-facing change?
NA

### How was this patch tested?
Test result as following:
Before:
<img width="2347" height="440" alt="23a8688baa93fd16128d4c2f7d8d0bf7" src="https://github.com/user-attachments/assets/5ac5e80c-362d-4a71-8c84-a2bd7e0f33af" />

After:
<img width="1938" height="262" alt="da783817d42060ff619eb4fd3295be8f" src="https://github.com/user-attachments/assets/12c8eb38-8789-464c-b9bf-99d863e3d24d" />

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d


## 基本信息
- **编号**: #5696
- **作者**: leo-pony
- **创建时间**: 2026-01-07T09:44:44Z
- **关闭时间**: 2026-01-08T01:26:49Z
- **标签**: module:core

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5696)
