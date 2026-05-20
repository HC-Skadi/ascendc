# Issue #1176: Upgrade CANN version to 8.2RC1.

## 基本信息

- **编号**: #1176
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1176
- **创建时间**: 2025-06-11T14:17:34Z
- **关闭时间**: 2025-12-30T09:41:25Z
- **更新时间**: 2025-12-30T09:41:25Z
- **提交者**: @fems14
- **评论数**: 1

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

pipline not support the newtest cann，so there are currently two implementations of chunked prefill in the warehouse. Once CANN support is available, the old version of the implementation will be removed.
