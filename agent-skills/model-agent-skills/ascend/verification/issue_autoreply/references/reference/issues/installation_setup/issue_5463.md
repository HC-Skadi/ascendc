# Issue #5463: [RFC]: Refactor Attention module

## 基本信息

- **编号**: #5463
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5463
- **创建时间**: 2025-12-29T04:19:12Z
- **关闭时间**: 2026-01-19T06:22:20Z
- **更新时间**: 2026-01-21T03:35:22Z
- **提交者**: @weijinqian0
- **评论数**: 0

## 标签

RFC

## 问题描述

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
(3) The parameter list in the build function is aligned with the native VLLM. @JC-ut0 
5. Delete attn_state. @LICO1314 
6. CP attention, abstract parent class. done
(1) mla cp isolate. 
(2) extract common cp module.
https://github.com/vllm-project/vllm-ascend/pull/5490

<img width="1524" height="692" alt="Image" src="https://github.com/user-attachments/assets/fd661848-cde8-47f4-a038-6818b31953fd" />

7. mla_v1 use FIA operator. @LICO1314 1 wait fia ready  https://github.com/vllm-project/vllm-ascend/pull/5704
8. Device adaptor. @weijinqian0   wait A5 ready
https://github.com/vllm-project/vllm-ascend/pull/5735 
9. function called update_attn_params move to attention module. @drslark @LICO1314  ttps://github.com/vllm-project/vllm-ascend/pull/5532  https://github.com/vllm-project/vllm-ascend/pull/6041 
10. AttentionBuilder Inherit from base class in vllm.  @LICO1314   https://github.com/vllm-project/vllm-ascend/pull/5916
11. Add some comments for CommonMetadata and others. https://github.com/vllm-project/vllm-ascend/pull/5789 @LICO1314 
12. move AttentionSpec to Attention @LICO1314  https://github.com/vllm-project/vllm-ascend/pull/5834
### Feedback Period.

_No response_

### CC List.

_No response_

### Any Other Things.

_No response_
