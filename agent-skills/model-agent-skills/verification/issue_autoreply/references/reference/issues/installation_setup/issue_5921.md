# Issue #5921: [Doc] Add layer_sharding additional config for DeepSeek-V3.2-W8A8

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?


#### Documentation Improvements

New Configuration: Added the layer_sharding parameter to the DeepSeek-V3.2-W8A8 deployment tutorial. This guides users to include `["q_b_proj", "o_proj"]` in their prefill node setup for better resource utilization.

#### CI and Testing Updates

Test Config Update: Updated the multi-node E2E test configuration file: tests/e2e/nightly/multi_node/config/DeepSeek-V3_2-W8A8-A3-dual-nodes.yaml.

including disable `FLASHCOMM` and enable `FULL_DECODE_ONLY` and update performance baseline.

### Does this PR introduce any user-facing change?

Yes. The documentation now recommends a more optimized startup command for DeepSeek-V3.2-W8A8. Users following the updated tutorial will see improved performance in multi-node PD disaggregation environments.

### How was this patch tested?
CI Validation: The updated E2E test configuration has been verified through the nightly CI pipeline.

Environment: * vLLM ver

## 基本信息
- **编号**: #5921
- **作者**: starmountain1997
- **创建时间**: 2026-01-15T08:39:41Z
- **关闭时间**: 2026-01-20T04:40:54Z
- **标签**: documentation, module:tests, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5921)
