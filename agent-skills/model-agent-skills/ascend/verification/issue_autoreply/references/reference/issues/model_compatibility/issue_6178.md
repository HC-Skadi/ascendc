# Issue #6178: [0.13.0][Feat] Merge the multi eagle graphs to one graph

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?
This PR is mainly cherry-picked fron #5940.

Major difference from #5940 is:
1. remove `piece_all_attn_layer_name`, which is never used in #5940
2. remain `attn_metadata` update process in `attn_update_stack_num_spec_norm` instead of `common_attn_metadata` update and rebuild `attn_metadata` process in #5940

Minor change in this PR is:
1. `self.cudagraph_batch_sizes` is replaced with `self.runner.cudagraph_batch_sizes`, since the former one is not correct (self.cudagraph_batch_sizes[-1] is not guarantee to be valid)

### Does this PR introduce _any_ user-facing change?
N/A

### How was this patch tested?
by ci


## 基本信息
- **编号**: #6178
- **作者**: slippersss
- **创建时间**: 2026-01-23T04:41:47Z
- **关闭时间**: 2026-01-23T11:12:13Z
- **标签**: ready, ready-for-test

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6178)
