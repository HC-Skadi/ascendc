# Issue #5494: [RFC]: Upgrade CANN from 8.3 to 8.5

**类型**: Issue

## 问题背景
### Motivation.

The CANN 8.5 version upgrade introduced some compatibility issues; therefore, we documented the CANN 8.5 version upgrade in this RFC to ensure a smooth version upgrade.

### Proposed Change.

- Address issue
  - https://github.com/vllm-project/vllm-ascend/pull/5458
- Replace related custom ops:
  - [ ] Need replace the aclnnMoeInitRoutingV3 (https://github.com/vllm-project/vllm-ascend/pull/5251) after CANN 8.5 upgrade

- Upgrade infra

### Feedback Period.

_No response_

### CC List.

_No response_

### Any Other Things.

_No response_

## 基本信息
- **编号**: #5494
- **作者**: Yikun
- **创建时间**: 2025-12-30T00:12:37Z
- **关闭时间**: 2026-01-22T01:29:52Z
- **标签**: RFC

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/5494)
