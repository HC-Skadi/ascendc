# Issue #642: [New Model]: Qwen3 support

## 基本信息

- **编号**: #642
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/642
- **创建时间**: 2025-04-24T07:29:34Z
- **关闭时间**: 2025-06-15T07:25:10Z
- **更新时间**: 2025-06-15T07:25:10Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

new model

## 问题描述

### The model to consider.

- `Qwen/Qwen3-8B`
- `Qwen/Qwen3-MoE-15B-A2B`

### The closest model vllm already supports.

_No response_

### What's your difficulty of supporting the model you want?

First priority:
- [x] Add CI for `Qwen/Qwen3-0.6B`: https://github.com/vllm-project/vllm-ascend/pull/717
- [x] Download models and run test (functional / accuray / perf) for `Qwen/Qwen3-8B`
  - [x] functional: @wangxiyuan
     - [x] offline test
     - [x] online test
  - [x] accruracy: @hfadzxy 
  - [x] perf: @@Potabk 
- [x] Update `Single NPU (Qwen2.5 7B)` to `Single NPU (Qwen3 8B)`: https://github.com/vllm-project/vllm-ascend/pull/711
- [x] Announcement on wechat post on Open Source Now: `使用vLLM Ascend 部署 Qwen3`
- [x] Validate on Qwen3 docker image:
     - [x] 0.8.4rc2
     - [x] 0.8.4rc2-openeuler

Second priority:
- [x] Fix MOE error: https://github.com/vllm-project/vllm-ascend/pull/709
- [ ] Add CI for `Qwen/Qwen3-MoE-15B-A2B`
- [ ] Download models and run test (functional / accuray / perf) for `Qwen/Qwen3-MoE-15B-A2B`
- [ ] Announcement on wechat post on Open Source Now: `使用 vLLM Ascend 部署 Qwen/Qwen3-MoE`
