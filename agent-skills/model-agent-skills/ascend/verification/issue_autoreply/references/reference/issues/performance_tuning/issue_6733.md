# Issue #6733: [Feat]ds3.2 support pcp

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
The ds3.2 model adaptation supports the PCP feature.

The solution is as follows: When saving the KV cache, first perform an allgather operation on the KVs, and then each node saves its own copy. When the attention or indexer performs calculations, they all gather the KV cache and then perform the calculations.

### Does this PR introduce _any_ user-facing change?
No
### How was this patch tested?
02/12 23:05:10 - AISBench - INFO - Running 1-th replica of evaluation
02/12 23:05:10 - AISBench - INFO - Task [vllm-api-general-chat/gsm8k]: {'accuracy': 96.35416666666667, 'type': 'GEN'}
02/12 23:05:10 - AISBench - INFO - time elapsed: 2.87s
02/12 23:05:12 - AISBench - INFO - Evaluation tasks completed.
02/12 23:05:12 - AISBench - INFO - Summarizing evaluation results...
dataset       version    metric    mode      vllm-api-general-chat
gsm8kdataset  -          accuracy  gen                       96.35


- vLLM version: v0.15.0
- vLLM

## 基本信息
- **编号**: #6733
- **作者**: weiguihua2
- **创建时间**: 2026-02-13T01:56:30Z
- **关闭时间**: 2026-02-25T01:46:57Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6733)
