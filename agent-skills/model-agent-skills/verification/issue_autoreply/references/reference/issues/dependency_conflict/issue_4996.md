# Issue #4996: [Bug]: DeepSeek-V3.2 may report errors during decode stage under high-load scenarios

## 基本信息

- **编号**: #4996
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4996
- **创建时间**: 2025-12-13T13:29:01Z
- **关闭时间**: 2025-12-16T10:16:44Z
- **更新时间**: 2025-12-16T10:16:44Z
- **提交者**: @rjg-lyh
- **评论数**: 3

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


### 🐛 Describe the bug

When run dsv3.2 during decode stage under high-load scenarios, some errors may report, such as lightning indexer ops error.

We will try our best to fix it as soon as possible.
