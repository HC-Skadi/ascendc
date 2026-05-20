# Issue #732: [Guide]: Usage on auto prefix caching

## 基本信息

- **编号**: #732
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/732
- **创建时间**: 2025-04-30T01:43:07Z
- **关闭时间**: 2025-06-15T07:46:11Z
- **更新时间**: 2025-09-09T07:21:49Z
- **提交者**: @MengqingCao
- **评论数**: 0

## 标签

guide

## 问题描述

### How to use Auto Prefix Caching on vllm-ascend
Please refer to [vLLM official doc on Auto Prefix Caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching.html) as a usage guide.
> [!NOTE]  
> 
> **`block_size >= 128 and block_size % 128 == 0`** is required when using Auto Prefix Caching (APC) in vllm-ascend. 
