# Issue #4969: [New Model]: 希望新增DeepSeek-V3.2部署能力支持

## 基本信息

- **编号**: #4969
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4969
- **创建时间**: 2025-12-12T11:19:34Z
- **关闭时间**: 2025-12-23T07:48:55Z
- **更新时间**: 2025-12-23T07:48:55Z
- **提交者**: @izhaomeng
- **评论数**: 8

## 标签

new model

## 问题描述

### The model to consider.

https://huggingface.co/deepseek-ai/DeepSeek-V3.2

### The closest model vllm already supports.

https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp

### What's your difficulty of supporting the model you want?

已经试过A2 + vllm0.11.x/0.12.x/0.13.x+vllm-ascend0.11.x部署deepseek-v3.2，要么deepseek_v32 tokenizer不支持，要么tool-call-paser和reasoning-parser不支持，应该还没系统的支持。希望能增加对deepseek-v3.2模型的支持。
