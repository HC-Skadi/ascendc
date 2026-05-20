# Issue #4084: [RFC]: Remove VL Modeling Files

## 基本信息

- **编号**: #4084
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4084
- **创建时间**: 2025-11-10T06:28:51Z
- **关闭时间**: 2025-12-23T14:07:48Z
- **更新时间**: 2026-02-06T02:24:02Z
- **提交者**: @shen-shanshan
- **评论数**: 1

## 标签

RFC

## 问题描述

### Motivation.

To avoid maintaining a variety of modeling files in vllm-ascend, we propose to remove all files in `models` dir in vllm-ascend. After this, the only thing a vllm plugin need to do is just registering their custom device-specific OOT ops to vllm when adding a new model.

To achieve this, there are some refactors need to be done both in vllm and vllm-ascend, such as extracting some general layers as CustomOp.

### Proposed Change.

**vllm:**

- [x] Extract Conv layer as CustomOp. @shen-shanshan https://github.com/vllm-project/vllm/pull/28455
- [x] Extract MMEncoderAttention as CustomOp. @shen-shanshan https://github.com/vllm-project/vllm/pull/30125
- [x] Extract ApplyRotaryEmb as CustomOp. @shen-shanshan https://github.com/vllm-project/vllm/pull/29873
- [x] Extract common methods for ApplyRotaryEmb. @shen-shanshan https://github.com/vllm-project/vllm/pull/31021
- [x] Support object-level enable for CustomOp. @shen-shanshan https://github.com/vllm-project/vllm/pull/30547
- [x] Use caching to remove repeated sin/cos computations. @gcanlin https://github.com/vllm-project/vllm/pull/28798
- [x] Remove redundant TP logic in split_qkv. @gcanlin https://github.com/vllm-project/vllm/pull/28271
- [x] Add developer guide for CustomOp. @shen-shanshan  https://github.com/vllm-project/vllm/pull/30886

**vllm-ascend:**

- [x] Patch VisionAttention layer and remove Qwen2.5-VL modeling files. @shen-shanshan https://github.com/vllm-project/vllm-ascend/pull/4349
- [x] Remove Qwen2-VL modeling files. @shen-shanshan https://github.com/vllm-project/vllm-ascend/pull/4534
- [x] Remove Qwen3-VL and Qwen3-VL-MoE modeling files. @shen-shanshan https://github.com/vllm-project/vllm-ascend/pull/4577
- [x] Remove patch for cos/sin cache. @shen-shanshan https://github.com/vllm-project/vllm-ascend/pull/4672
- [x] Implement CustomOp for MMEncoderAttention and remove related patch. @shen-shanshan https://github.com/vllm-project/vllm-ascend/pull/4750
- [x] Implement CustomOp for ApplyRotaryEmb and remove related patch. @shen-shanshan https://github.com/vllm-project/vllm-ascend/pull/4667
- [x] Refactor `set_ascend_forward_context()` to remove patch for ViT embedding. @gcanlin https://github.com/vllm-project/vllm-ascend/pull/5035
- [x] Implement `multimodal_cpu_fields` in model runner to guarantee that `grid_thw` should be moved to cpu before converting to numpy. @zhangxinyuehfad https://github.com/vllm-project/vllm-ascend/pull/5196

**Other related:**

- [x] Make mamba backend pluggable. @shen-shanshan https://github.com/vllm-project/vllm/pull/26487

### Feedback Period.

_No response_

### CC List.

@Yikun @wangxiyuan @gcanlin 

### Any Other Things.

_No response_
