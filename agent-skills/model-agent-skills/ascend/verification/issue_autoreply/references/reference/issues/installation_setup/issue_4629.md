# Issue #4629: [RFC]: Refactor Attention module

## 基本信息

- **编号**: #4629
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4629
- **创建时间**: 2025-12-02T08:26:40Z
- **关闭时间**: 2025-12-28T02:47:25Z
- **更新时间**: 2025-12-28T02:48:11Z
- **提交者**: @weijinqian0
- **评论数**: 3

## 标签

RFC

## 问题描述

# Reason
1. The Attention section has a large amount of code and many branches.
2. The functions related to Cp differ significantly from those of normal Attention, but the coupling is quite severe.
3. There are many masks due to historical reasons.
# Attention Steps
1. Remove the attention branch -- done  
https://github.com/vllm-project/vllm-ascend/pull/4531
https://github.com/vllm-project/vllm-ascend/pull/5081
2. Isolate PCP and DCP https://github.com/vllm-project/vllm-ascend/pull/4628 (1) Forward class extraction 
(2) Metadata coupling processing
(3) Builder processing
3. Unify masks, split masks, and delete all other masks (MLA 50%) @weijinqian0 @wujinyuan1@zhenwenqi2024  
(1) unify some masks. https://github.com/vllm-project/vllm-ascend/pull/4779  
(2) make attention_mask_builder singleton. https://github.com/vllm-project/vllm-ascend/pull/5389  @liweiyi @weijinqian0 
4. Metadata processing
(1) model_runner_v1  @wujinyuan1 @zhenwenqi 
https://github.com/vllm-project/vllm-ascend/pull/5160 
https://github.com/vllm-project/vllm-ascend/pull/5203
(2) Coordinate with model_runner_v2, remove unused and mergeable elements. wait @liurong ready
(3) The parameter list in the build function is aligned with the native VLLM. @JC-ut0 
5. Delete attn_state. @wujinyuan1  wait mla_cp ready
6. CP attention, abstract parent class. @wujinyuan1 
(1) mla cp isolate. https://github.com/vllm-project/vllm-ascend/pull/4933  
https://github.com/vllm-project/vllm-ascend/pull/5097
https://github.com/vllm-project/vllm-ascend/pull/5314
(2) extract common cp module.

<img width="1524" height="692" alt="Image" src="https://github.com/user-attachments/assets/fd661848-cde8-47f4-a038-6818b31953fd" />

7. MLA use FLA operator. @wujinyuan1 wait fia ready
8. Device adaptor. @wujinyuan1  wait A5 ready
9. function called update_attn_params move to attention_v1.py @wujinyuan1 
10. AttentionBuilder Inherit from base class in vllm.
(1)https://github.com/vllm-project/vllm-ascend/pull/5277
11. Add some comments for CommonMetadata and others.
