# Issue #6545: [CI] fix ds32 nightly cudagraph sizes

**类型**: Pull Request

## 问题背景
### What this PR does / why we need it?

  This PR fixes the cudagraph_capture_sizes configuration for DeepSeek-V3.2 W8A8 single node and dual node nightly test.

  When using MTP (Multi-Token Prediction) with tensor parallelism, the maximum value in cudagraph_capture_sizes should reach tp * (mtp + 1) to fully utilize the NPU graph performance benefits.

  For the single node test configuration:
  - tensor_parallel_size = 8
  - num_speculative_tokens (mtp) = 3
  - The maximum cudagraph_capture_size should be: 8 * (3 + 1) = 32

  The current configuration only goes up to 16, which limits the NPU graph utilization. This change extends the capture sizes to reach the optimal maximum of 32.

###  Does this PR introduce any user-facing change?

  No. This is a test configuration fix only.

###  How was this patch tested?

  Existing nightly CI test for DeepSeek-V3.2 W8A8 will verify the fix.

## 基本信息
- **编号**: #6545
- **作者**: starmountain1997
- **创建时间**: 2026-02-04T09:24:51Z
- **关闭时间**: 2026-02-06T02:32:20Z
- **标签**: 无

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/pull/6545)
