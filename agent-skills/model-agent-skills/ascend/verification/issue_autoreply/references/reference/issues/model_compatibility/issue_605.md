# Issue #605: [Feature] Support the v1 connector API

## 基本信息

- **编号**: #605
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/605
- **创建时间**: 2025-04-22T03:23:09Z
- **关闭时间**: 2025-12-24T10:59:08Z
- **更新时间**: 2025-12-24T10:59:08Z
- **提交者**: @jianzs
- **评论数**: 5

## 标签

feature request

## 问题描述

### 🚀 The feature, motivation and pitch

The vLLM community has merged the v1 Connector API (https://github.com/vllm-project/vllm/pull/15960). However, it is currently not functional in the Ascend environment. The issue lies in the Attention module where there's a flag `use_direct_call`. When this flag is set to True, the execution branch skips two layer kv cache APIs, making it impossible to implement layer-wise kv transfer. These two APIs are only called within unified attention functions.

The `use_direct_call` is determined by the following condition in the source code:

https://github.com/vllm-project/vllm/blob/1311913f5537b36a7b12f481ebd15f7ad775db58/vllm/attention/layer.py#L140-L145

Since the Ascend platform is neither considered as cuda nor cpu, `use_direct_call` is set to True, leading to an unsupported execution branch.

Has anyone encountered similar issues when working with graph mode on the Ascend platform? What would be the recommended solution?

This appears to be a common issue when using the v1 connector API on custom platforms, suggesting it might be an inherent issue within vLLM. However, I haven't been able to identify a suitable solution. For more context about this issue, please refer to this PR in the vLLM community: https://github.com/vllm-project/vllm/pull/16921

### Alternatives

_No response_

### Additional context

_No response_
