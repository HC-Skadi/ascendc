# Issue #734: [Guide]: Usage on Speculative Decoding and MTP

## 基本信息

- **编号**: #734
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/734
- **创建时间**: 2025-04-30T01:57:18Z
- **关闭时间**: 2025-06-15T07:47:03Z
- **更新时间**: 2025-06-15T07:47:03Z
- **提交者**: @MengqingCao
- **评论数**: 1

## 标签

guide

## 问题描述

### How to use Speculative Decoding and MTP on vLLM Ascend

Please refer to [vLLM official doc on Speculative Decoding](https://docs.vllm.ai/en/latest/features/spec_decode.html) as a usage guide.

> [!NOTE]  
> When using Speculative Decoding and MTP, there are some limits on vllm-ascend compared with vllm:
> 
> 1. When request preemption is triggered, there exsists precision issue with Speculative Decoding, except for MTP.
> 2. Speculative Decoding with multi-step preparation on npu is not supported, only support replacing by circle `for` on cpu to simulate multi-step preparation.
> 3. Only BatchExpansionTop1Scorer is supported now, MQAScorer is not supported.
