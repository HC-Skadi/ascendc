# Issue #5550: [WIP][Feature] Support MXFP8

**类型**: Pull Request

## 问题背景
This PR introduces support for MXFP8 (Microscaling Formats) data types for inference on the Ascend NPU (A5).

This PR is a continuation of the work originally started in PR #5113. Since that PR was closed, I have ported and adapted the codebase to the current master branch to ensure this feature reaches the community.

Huge thanks to @wangyao-i  for the initial implementation and groundwork.
- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/7157596103666ee7ccb7008acee8bff8a8ff1731


## 基本信息
- **编号**: #5550
- **作者**: SlightwindSec
- **创建时间**: 2025-12-31T03:20:58Z
- **关闭时间**: 2026-01-09T10:26:22Z
- **标签**: module:ops, module:core, module:quantization, merge-conflicts

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5550)
