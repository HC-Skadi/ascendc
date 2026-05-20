# Issue #6470: [Main2Main][Deps][Misc] Upgrade vLLM to v0.15.0

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR upgrades the vLLM dependency from `v0.14.1` to `v0.15.0`. This involves:
- Updating the `VLLM_TAG` in all `Dockerfile`.
- Updating the vLLM version in `docs/source/conf.py`.
- Removing conditional code paths specific to `v0.14.1` across the codebase, which simplifies maintenance.
- Fix `TypeError: MMEncoderAttention.__init__() got an unexpected keyword argument 'multimodal_config'` due to https://github.com/vllm-project/vllm/pull/31972.
- Fix `_shared_experts: 'NoneType' object is not callable` due to https://github.com/vllm-project/vllm/pull/32082 by https://github.com/vllm-project/vllm-ascend/pull/6335.
- Fix `ReshapeAndCacheOperation setup failed!` due to https://github.com/vllm-project/vllm/pull/25954 by overriding attention metadata slots.

This upgrade is necessary to keep the project aligned with the latest features, bug fixes, and API changes in the vLLM project.

### Does this PR introduce _any_ user-facing change?
No

## 基本信息
- **编号**: #6470
- **作者**: wangxiyuan
- **创建时间**: 2026-02-02T01:11:16Z
- **关闭时间**: 2026-02-02T07:57:55Z
- **标签**: documentation, ci/build, module:tests, module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6470)
