# Issue #4483: [Bug]: Qwen3-next-80B-A3B multiple request concurrency failures

## 基本信息

- **编号**: #4483
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4483
- **创建时间**: 2025-11-27T03:00:33Z
- **关闭时间**: 2026-01-06T12:26:08Z
- **更新时间**: 2026-01-06T12:26:08Z
- **提交者**: @leo-pony
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
vllm-ascend 0.11.0.rc1
```

</details>


### 🐛 Describe the bug

Qwen3-next-80B-A3B multiple request concurrency running fail, 
error information:
RuntimeError: copy between host_and device_opapi, 
UCE  ERROR, error code is 507053

detail detail:
<img width="1342" height="853" alt="Image" src="https://github.com/user-attachments/assets/cc0abceb-1da7-432c-9911-81d7e6e7e938" />
