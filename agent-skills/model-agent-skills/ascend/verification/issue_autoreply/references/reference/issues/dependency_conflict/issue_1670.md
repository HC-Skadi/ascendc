# Issue #1670: [Bug]: 910B Free GPU OOM

## 基本信息

- **编号**: #1670
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1670
- **创建时间**: 2025-07-08T08:34:46Z
- **关闭时间**: 2025-07-08T09:15:51Z
- **更新时间**: 2025-07-08T09:15:51Z
- **提交者**: @coyzeng
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text

```

</details>


### 🐛 Describe the bug

910B Free GPU OOM

RuntimeError: NPU out of memory. Tried to allocate 88.00 MiB (NPU 0; 60.96 GiB total capacity; 4.24 GiB already allocated; 4.24 GiB current active; 7.47 MiB free; 4.37 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.
