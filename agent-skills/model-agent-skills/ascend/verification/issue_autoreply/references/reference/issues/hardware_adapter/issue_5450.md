# Issue #5450: [Main][Ops] Make triton rope support index_selecting from cos_sin_cache

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

This PR extends original `rope_triton_forward` and `split_qkv_rmsnorm_rope` to support `cos_sin_cache` && `positions` as inputs. This fully aligns to vLLM RoPE api interface. Compared with earlier implementation for RoPE, the benefits are:

1. avoiding pre-computation of `cos` `sin` before model execution, which helps to remove redundant codes. 
2. allowing eagle3 draft model to have different rope parameters with main model (see #6612 ). This help to recover accept rate && accuracy in that case.

In addition, this kernel change only introduces very small performance degradation. Those `index_select` or `chunk` operations are now changed into simple memory access in triton kernel (For example, https://github.com/vllm-project/vllm-ascend/pull/5450/changes#diff-a4c2d3071530df193b98f9bf38553874bc4d47571336711f116c26d019cfbb6aR77-R81).

**Highlights**

- **RoPE Cache Unification**: Replaced separate _sin and _cos global tensors with a uni

## 基本信息
- **编号**: #5450
- **作者**: Angazenn
- **创建时间**: 2025-12-28T13:29:57Z
- **关闭时间**: 2026-02-11T13:20:53Z
- **标签**: module:ops, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5450)
