# Issue #5292: [Bug]: incorrect prefix passing in vLLM

## 基本信息

- **编号**: #5292
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5292
- **创建时间**: 2025-12-23T09:19:08Z
- **关闭时间**: 2026-01-06T01:13:48Z
- **更新时间**: 2026-01-06T01:13:48Z
- **提交者**: @kunpengW-code
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>
vllm                              0.13.0+empty                         

vllm_ascend                 0.12.0rc2.dev113+g14931d2a8.d20251219

### 🐛 Describe the bug

When matmul_and_reduce is enabled, the prefix attribute is required. However, in some models, the prefix is not passed correctly, causing errors when starting the service.
ERROR info：
raise ValueError(f"Duplicate layer name: (prefix}")
