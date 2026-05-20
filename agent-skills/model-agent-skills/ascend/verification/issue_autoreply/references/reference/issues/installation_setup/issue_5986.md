# Issue #5986: [CI] optimize lint term

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This patch purpose to optimize the lint check term. The main idea is to reduce unnecessary installation time.
1. The installation of vllm is not must, only append the path of vllm src to the `PATHONPATH` is effective
2. This installation of `requirements-dev.txt` is not must, we have a pre-built image `quay.io/ascend-ci/vllm-ascend:lint` with all the requirements installed in advance. 
    **NOTE**: the conditions for triggering image builds are: 1).Daily scheduled build; 2) Build when requirements are modified; 3) Manual build. This ensures that the dependencies in our image are up-to-date to the greatest extent possible.
3. The `mypy` was separated from the `pre-commit` hook for performance reasons; we found that integrating `mypy` into the `pre-commit` hook resulted in poor performance.
4. Reduce the CPU core consumption from 16 -> 8

### Does this PR introduce _any_ user-facing change?
The end-to-end lint time was optimized from 20mi

## 基本信息
- **编号**: #5986
- **作者**: Potabk
- **创建时间**: 2026-01-19T02:34:46Z
- **关闭时间**: 2026-01-22T07:46:59Z
- **标签**: 无

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5986)
