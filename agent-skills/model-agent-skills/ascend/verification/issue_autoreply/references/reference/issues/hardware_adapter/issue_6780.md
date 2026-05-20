# Issue #6780: [DOC] add request forwarding

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

  - New section: "Request Forwarding" documentation in docs/source/tutorials/models/DeepSeek-V3.2.md                                                                                                      
  - Environment fix: Changed VLLM_ASCEND_ENABLE_FLASHCOMM1 from 0 to 1 in the DeepSeek-V3 configuration examples

### Does this PR introduce _any_ user-facing change?

  Documentation update only - provides new configuration guidance for request forwarding setups

### How was this patch tested?

- vLLM version: v0.15.0
- vLLM main: https://github.com/vllm-project/vllm/commit/9562912cead1f11e8540fb91306c5cbda66f0007


## 基本信息
- **编号**: #6780
- **作者**: starmountain1997
- **创建时间**: 2026-02-24T03:43:14Z
- **关闭时间**: 2026-02-25T06:43:51Z
- **标签**: documentation

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6780)
