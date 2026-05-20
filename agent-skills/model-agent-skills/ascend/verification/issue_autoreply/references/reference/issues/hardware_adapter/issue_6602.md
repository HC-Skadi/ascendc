# Issue #6602: [v0.13.0][Ops] Make triton rope support index_selecting from cos_sin_cache

**类型**: Pull Request

## 问题背景
<!--  Thanks for sending a pull request!

BEFORE SUBMITTING, PLEASE READ https://docs.vllm.ai/en/latest/contributing/overview.html

-->
### What this PR does / why we need it?
This PR adapts #5450, #6523 to v0.13.0, to fix #6612 .

This PR extends original `rope_triton_forward` and `split_qkv_rmsnorm_rope` to support `cos_sin_cache` && `positions` as inputs. This fully aligns to vLLM RoPE api interface. Compared with earlier implementation for RoPE, the benefits are:

1. avoiding pre-computation of `cos` `sin` before model execution, which helps to remove redundant codes. 
2. allowing eagle3 draft model to have different rope parameters with main model (see #6612 ). This help to recover accept rate && accuracy in that case.

In addition, this kernel change only introduces very small performance degradation. Those `index_select` or `chunk` operations are now changed into simple memory access in triton kernel 

**Highlights**

- **RoPE Cache Unification**: Replaced separ

## 基本信息
- **编号**: #6602
- **作者**: Angazenn
- **创建时间**: 2026-02-06T09:36:52Z
- **关闭时间**: 2026-02-11T14:05:31Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6602)
