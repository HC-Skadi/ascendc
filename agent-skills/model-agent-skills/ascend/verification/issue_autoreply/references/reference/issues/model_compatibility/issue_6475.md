# Issue #6475: [ModelRunner][Fix] Pads query_start_loc to satisfy FIA/TND constraint

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR reverts "[ModelRunner] Revert [Fix] Pads query_start_loc to satisfy FIA/TND constraint #6459 (commit 5b0a6bcfe9eca595bbcd064363596553b6bbd1fe)" and fixes a check in `model_runner_v1`.

**A key change is that we remove the strict assertion in the latest commit, as it turns out MLA + PIECEWISE will slice during computing, leaving our assertion uncalled for and will only cause false alarm.**

This handles both uniform and mixed batches (by inserting a dummy request for mixed batches), consolidates ad-hoc padding into a single helper, copies the updated buffer to the device, which prevents kernel mismatches or failures and ensure correct shapes for FIA/TND execution in full graph modes.

We currently place this helper in `execute_model`. My original design was to include it in `_prepare_inputs`, but that doesn’t work because it must run after padding. While I’d prefer to minimize the impact and reuse as much of the base class as possib

## 基本信息
- **编号**: #6475
- **作者**: yiz-liu
- **创建时间**: 2026-02-02T02:31:38Z
- **关闭时间**: 2026-02-04T13:11:09Z
- **标签**: module:tests

## 涉及版本
- vLLM: v0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6475)
