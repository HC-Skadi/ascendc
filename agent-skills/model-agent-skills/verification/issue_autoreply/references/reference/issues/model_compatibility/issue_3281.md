# Issue #3281: [Usage]: qwen3-coder-30b-a3b

## 基本信息

- **编号**: #3281
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3281
- **创建时间**: 2025-09-30T02:55:43Z
- **关闭时间**: 2025-11-11T07:00:20Z
- **更新时间**: 2025-11-11T07:00:20Z
- **提交者**: @Jaycee
- **评论数**: 2

## 标签

无

## 问题描述

### Your current environment

When using the 0.10 image, 910b *2 , after starting the qwen3-coder-30b-a3b service, the service crashes when multiple requests are sent simultaneously.


### How would you like to use vllm on ascend
Startup parameters:
```text
["vllm","serve","/my/model/path","--host","0.0.0.0","--served-model-name","Qwen3-Coder-30B-A3B","--port","9099","--tensor-parallel-size","2","--max-model-len","61440","--gpu-memory-utilization","0.85"]
```
