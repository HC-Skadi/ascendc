# Issue #5916: [Refactor] AttentionBuilder inherit from base class in vllm

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

This PR makes `AscendMLAMetadataBuilder` and `AscendSFAMetadataBuilder` properly inherit from the base class `MLACommonMetadataBuilder` in vllm by adding `super().__init__()` calls.

**Changes:**
- Add `super().__init__()` call in `AscendMLAMetadataBuilder.__init__()`
- Add `super().__init__()` call in `AscendSFAMetadataBuilder.__init__()`
- Extract `ascend_chunked_prefill_workspace_size()` to `vllm_ascend/attention/utils.py` to avoid code duplication
- Override `determine_chunked_prefill_workspace_size()` to support Ascend-specific 128k tokens workspace size (vs 64k in parent class)
- Update unit tests to mock parent class `__init__` for proper isolation

**Why we need it:**
- Follow proper Python inheritance patterns by calling `super().__init__()`
- Reduce code duplication by reusing parent class initialization logic
- Better maintainability as parent class changes will be automatically inherited

Part of issue #5463 item 10


## 基本信息
- **编号**: #5916
- **作者**: LICO1314
- **创建时间**: 2026-01-15T07:25:47Z
- **关闭时间**: 2026-01-21T02:45:45Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5916)
