# Issue #6577: [0.13.0][CI] Change A2 Runner

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR updates the CI runner configuration from "linux-aarch64-a2-X" to "linux-aarch64-a2b3-X" in the `test_qwen3_32b_int8.py` and `test_qwen3_next.py` files. Additionally, the "runner" field is removed from the `InternVL3_5-8B-hf.yaml` configuration. This change is necessary to align with the updated A2 runner environment in the CI system.

Fixes #

### Does this PR introduce _any_ user-facing change?
No, this PR does not introduce any user-facing changes. It is an internal CI configuration update.

### How was this patch tested?
The changes are related to CI runner configurations. The expectation is that existing CI tests will pass with these updates, validating the new runner setup.

## 基本信息
- **编号**: #6577
- **作者**: zhangxinyuehfad
- **创建时间**: 2026-02-05T12:13:09Z
- **关闭时间**: 2026-02-05T12:58:09Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6577)
