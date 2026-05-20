# Issue #6629: [Refact]Refact MLA/SFA weight prefetch to consist with moe weight prefetch

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
1. [Refact] Refact MLA/SFA weight prefetch to consist with moe weight prefetch
2. Remove duplicated o_proj weight prefetch in forward for MLA/SFA

### Does this PR introduce _any_ user-facing change?
NA

### How was this patch tested?

1) Performance result:
Perf test data:
*) MLA:

|      | 1st test | 2nd test | Output Token Throughput(Avg) | Performance improvement percentage |
| --- | --- | --- | --- | --- |
| o_proj duplicate prefetch | 11.9669 token/s | 12.0287 token/s  | 11.9978 | 
| o_proj no duplicate prefetch | 12.5594 token/s | 12.6216 token/s | 12.5905 | 4.94%| |

single layer performace improve: 5%~8%

*) SFA:

|      | 1st test | 2nd test | Output Token Throughput(Avg) | Performance improvement percentage |
| --- | --- | --- | --- | --- |
| o_proj duplicate prefetch | 13.0523 token/s  | 13.1084 token/s | 13.08035 | |
| o_proj no duplicate prefetch | 13.9844 token/s  | 14.1678 token/s  | 14.0761 | 7.6% |

2)

## 基本信息
- **编号**: #6629
- **作者**: leo-pony
- **创建时间**: 2026-02-09T06:51:14Z
- **关闭时间**: 2026-02-10T06:14:37Z
- **标签**: module:ops, ready, ready-for-test

## 涉及版本
- vLLM: v0.15.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6629)
