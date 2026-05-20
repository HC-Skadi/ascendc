# Issue #5496: [Refactor][EAGLE] 4/N delete propose and dummy_run in mtp_proposer

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR deletes `propose` and `dummy_run` in mtp_proposer and thus removes mtp_proposer. The main changes are described below:
1. step 0 is separated from rest steps (graph mode is determined independently)
2. common metadata is updated and attn metadata is rebuilt for rest steps (not directly operate on attn metadata now)
3. pcp/dcp related code is transferred here without too much change (todo)

### Does this PR introduce _any_ user-facing change?
N/A

### How was this patch tested?
by ci

- vLLM version: v0.13.0
- vLLM main: https://github.com/vllm-project/vllm/commit/45c1ca1ca1ee8fa06df263c8715e8a412ff408d4


## 基本信息
- **编号**: #5496
- **作者**: slippersss
- **创建时间**: 2025-12-30T01:42:28Z
- **关闭时间**: 2026-01-21T12:59:17Z
- **标签**: ready, ready-for-test, merge-conflicts

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5496)
