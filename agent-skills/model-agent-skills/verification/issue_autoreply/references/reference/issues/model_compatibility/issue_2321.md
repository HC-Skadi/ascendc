# Issue #2321: [RFC]: Refactoring fused_moe

## 基本信息

- **编号**: #2321
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2321
- **创建时间**: 2025-08-11T12:26:41Z
- **关闭时间**: 2025-12-13T01:43:21Z
- **更新时间**: 2025-12-13T01:43:22Z
- **提交者**: @shiyuan680
- **评论数**: 1

## 标签

RFC

## 问题描述

### Motivation.

This RFC proposes optimize fused_moe‘s implemention, change branch's condition, simplfy code and make it easier to maintain and develop.

### Proposed Change.

The specific updates to the code structure design are as follows: 
① A new folder named fused_moe has been created, along with a new file called select_expert.py
 (1) The select_experts branches of the AscendUnquantizedFusedMoEMethod and AscendW8A8DynamicFusedMoEMethod classes have been abstracted into a new public method called select_expert 
(2) The branches are divided into two parts: methods using fused operators and those not using fused operators 
(3) Some complex calculations have been split into individual function implementations.
② Split multiple fused_experts_with_xxx functions into token_dispatcher class and mlp function, unifying the entry point for fused_experts computation. 
(1) A new MoETokenDispatcher parent class will be added, with core functionalities for permutation and unpermutation, as well as the initialization of some necessary parameters and some common functions. 
(2) In the All2All scenario, two subclasses `UnquantizedTokenDispatcherWithAll2AllV` and `QuantizedTokenDispatcherWithAll2All` will be added, inheriting from MoETokenDispatcher, each implementing their own permutation and unpermutation functions. 
(3) In the AllGather scenario, three subclasses `UnquantizedTokenDispatcherWithAllGather`, `QuantizedTokenDispatcherWithAllGather`, and `UnquantizedTokenDispatcherWithFusedExpertsMoge` will be added, inheriting from MoETokenDispatcher, each implementing their own permutation and unpermutation functions. 
(4) In the MC2 scenario, two subclasses `UnquantizedTokenDispatcherWithMC2` and `QuantizedTokenDispatcherWithMC2` will be added, inheriting from MoETokenDispatcher, each implementing their own permutation and unpermutation functions. 
(5) The apply_mlp part will create a common function in fused_moe.py, with variations for different scenarios covered by branching logic. 
(6) An instance of token_dispatcher will be initialized in modelrunner_v1.py based on ep_size, with_prefill, and quantization (similar to the judgment in fused_moe_state) and passed to forward_context for use in fused_moe.py.
(7) The unified entry point unified_fused_experts will be created in fused_moe.py, where the logic includes getting token_dispatcher -> token_dispatcher.permutation -> apply_mlp -> token_dispatcher.unpermutation.Subsequently delete the original fused_experts_with_xxx function.


### Feedback Period.

_No response_

### CC List.

_No response_

### Any Other Things.
co-owner
@henryxuxu0716 
our related pr
experts_selector
https://github.com/vllm-project/vllm-ascend/pull/2150  @shiyuan680 
all2allv
https://github.com/vllm-project/vllm-ascend/pull/2243 @Pr0Wh1teGivee
mc2 and allgather
https://github.com/vllm-project/vllm-ascend/pull/2164  @momo609
