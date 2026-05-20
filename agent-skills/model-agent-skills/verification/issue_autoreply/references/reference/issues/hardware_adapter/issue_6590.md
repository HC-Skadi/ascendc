# Issue #6590: implement batch invariant with ascendc

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
there are batch invariant ops implemented by triton and ascendc, this pr aims to choose which kind of ops to be used to enable batch invariant. #5487

### Does this PR introduce _any_ user-facing change?
no
### How was this patch tested?

- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/d7e17aaacd5ed1b4b4be6bcfef3a1b7cbc84fc9a


## 基本信息
- **编号**: #6590
- **作者**: Ronald1995
- **创建时间**: 2026-02-06T03:51:31Z
- **关闭时间**: 2026-02-10T06:15:26Z
- **标签**: module:core

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6590)
