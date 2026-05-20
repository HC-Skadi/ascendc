# Issue #135: [New Model]:  load local model is error

## 基本信息

- **编号**: #135
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/135
- **创建时间**: 2025-02-21T09:24:36Z
- **关闭时间**: 2025-02-23T11:01:51Z
- **更新时间**: 2025-02-23T11:01:51Z
- **提交者**: @fengzx99
- **评论数**: 2

## 标签

question

## 问题描述

### The model to consider.

deepseekv2

### The closest model vllm already supports.

_No response_

### What's your difficulty of supporting the model you want?

when we use the local model ,  I get the error:
huggingface_hub.errors.HFValidationError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': '/root/DeepSeek-V2-Lite'. Use `repo_type` argument if needed.

my shell:
vllm serve "/root/DeepSeek-V2-Lite" --tensor_parallel_size 8 --max-model-len 8192 --enforce-eager --trust-remote-code
