# Issue #5463: [RFC]: Refactor Attention module

**类型**: Issue

## 问题背景
### Motivation.

Source form: https://github.com/vllm-project/vllm-ascend/issues/4629

1. The Attention section has a large amount of code and many branches.
2. The functions related to Cp differ significantly from those of normal Attention, but the coupling is quite severe.
3. There are many masks due to historical reasons.

### Proposed Change.
1. Remove the attention branch -- done  
2. Isolate PCP and DCP  --done
(1) Forward class extraction 
(2) Metadata coupling processing
(3) Builder processing
3. Unify masks, split masks, and delete all other masks (MLA 50%) @weijinqian0 @wujinyuan1@zhenwenqi2024  
(1) unify some masks.
(2) make attention_mask_builder singleton. @LICO1314 @weijinqian0 
https://github.com/vllm-project/vllm-ascend/pull/4870
https://github.com/vllm-project/vllm-ascend/pull/5389 
4. Metadata processing 
(1) model_runner_v1  @wujinyuan1  @zhenwenqi 
(2) Coordinate with model_runner_v2, remove unused and mergeable elements. wait @liurong ready
(3) The parameter list 

## 基本信息
- **编号**: #5463
- **作者**: weijinqian0
- **创建时间**: 2025-12-29T04:19:12Z
- **关闭时间**: 2026-01-19T06:22:20Z
- **标签**: RFC

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/5463)
