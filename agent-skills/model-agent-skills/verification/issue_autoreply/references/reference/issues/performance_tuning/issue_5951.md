# Issue #5951: [1/N][Feat] Xlite Qwen3 MoE Support

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This patch adds support for the Qwen3-MoE model in Xlite. For more details about Xlite, please refer to the following link:https://atomgit.com/openeuler/GVirt/blob/master/xlite/README.md.

Qwen3-MoE TODO List:
- [ ] Qwen3-235B-A22B support
- [ ] Qwen3-MoE weights NZ support
- [ ] Qwen3-MoE data parallel support

## Qwen3-30B-A3B-Instruct-2507 910B3(A2) Online Inference Performance Comparison
- aclgraph: main(69b170b8b59600ada841600eb16794eba59477af)
- xlite-full: main + xlite-full
- xlite-decode-only: main + xlite-decode-only
- diff1: Performance comparison between xlite-full and aclgraph
- diff2: Performance comparison between xlite-decode-only and aclgraph

| maxconcurrency | item | TTFT(ms) |  | TPOT(ms) |  | QPS (req/s) | OutputSpeed (token/s) |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Avg | P99 | Avg | P99 |  |  |
| 1 | baseline-aclgraph | 205.07 | 287.29 | 12.34 | 12.65 | 0.14 | 78.81 |
| 1 | xlite-full |

## 基本信息
- **编号**: #5951
- **作者**: changdawei1
- **创建时间**: 2026-01-16T07:07:38Z
- **关闭时间**: 2026-01-21T01:26:03Z
- **标签**: documentation, module:tests, module:core, ready, ready-for-test

## 涉及版本
- vLLM: v0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/5951)
