# Issue #6664: [npugraph_ex]enable npugraph_ex by default

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

This pull request enables the `npugraph_ex` backend by default to improve performance on Ascend NPUs, as proposed in the [RFC](https://github.com/vllm-project/vllm-ascend/issues/6214).


### Does this PR introduce _any_ user-facing change?

Yes. `npugraph_ex` is now enabled by default. Users can disable it by setting `enable: false` in the `npugraph_ex_config` section of the `additional_config`.

### How was this patch tested?

CI passed. The changes are covered by existing and new E2E tests (`test_aclgraph_accuracy.py`) and unit tests (`test_ascend_config.py`) that have been updated to reflect the new default behavior. The tests verify correctness and consistency with `npugraph_ex` enabled and disabled, as well as with the new static kernel option.


## 基本信息
- **编号**: #6664
- **作者**: huyq
- **创建时间**: 2026-02-10T09:09:58Z
- **关闭时间**: 2026-02-12T00:44:07Z
- **标签**: documentation, module:tests, module:core, ready, ready-for-test

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6664)
