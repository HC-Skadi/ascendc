# Issue #1024: [Usage]:  Does vllm support the parameter rope-scaling?

## 基本信息

- **编号**: #1024
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1024
- **创建时间**: 2025-05-30T01:49:51Z
- **关闭时间**: 2025-05-30T03:01:52Z
- **更新时间**: 2025-05-30T03:01:53Z
- **提交者**: @RyanOvO
- **评论数**: 2

## 标签

无

## 问题描述

### Your current environment

like this: 

`VLLM_USE_MODELSCOPE=true vllm serve ... --rope-scaling '{"rope_type":"yarn","factor":4.0,"original_max_position_embeddings":32768}' --max-model-len 131072  
`

vllm: 0.8.5
vllm-ascend: 0.8.5


