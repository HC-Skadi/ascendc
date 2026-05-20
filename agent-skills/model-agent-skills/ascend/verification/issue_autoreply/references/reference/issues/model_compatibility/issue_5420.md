# Issue #5420: [Refactor][EAGLE] 3/N delete redundant methods in mtp_proposer

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR aims to delete redundant methods in mtp_proposer. All the deleted methods now can be found in eagle_proposer. We also remove some methods in eagle_proposer since they are identical to those in vllm-eagle.

RFC: #5467

### Does this PR introduce _any_ user-facing change?
N/A

### How was this patch tested?
by ci

- vLLM version: release/v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/81786c87748b0177111dfdc07af5351d8389baa1


## 基本信息
- **编号**: #5420
- **作者**: slippersss
- **创建时间**: 2025-12-27T04:00:01Z
- **关闭时间**: 2026-01-06T08:47:40Z
- **标签**: module:tests, ready, ready-for-test

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5420)
