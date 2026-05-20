# Issue #5803: [Refactor] add vllm_ascend/config folder

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
1. There are two configuration files: `ascend_config.py` and `profiling_config.py`. These have been moved to `vllm_ascend/config`.

2. The file `vllm_ascend/utils.py` contains over 1,000 lines of code. To improve organization, functions related to config have been moved to `vllm_ascend/config/utils.py`.

### Does this PR introduce _any_ user-facing change?

### How was this patch tested?

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/2f4e6548efec402b913ffddc8726230d9311948d


## 基本信息
- **编号**: #5803
- **作者**: realliujiaxu
- **创建时间**: 2026-01-12T08:22:37Z
- **关闭时间**: 2026-01-31T02:14:40Z
- **标签**: module:tests, module:ops, module:core, module:quantization, merge-conflicts

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5803)
