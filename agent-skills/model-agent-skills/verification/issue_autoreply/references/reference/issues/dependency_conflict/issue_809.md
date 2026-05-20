# Issue #809: [Bug]: RuntimeError: shape '[-1, 3, 80, 1280]' is invalid for input size 1966080

## 基本信息

- **编号**: #809
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/809
- **创建时间**: 2025-05-12T02:17:24Z
- **关闭时间**: 2025-06-16T03:29:08Z
- **更新时间**: 2025-12-30T11:59:54Z
- **提交者**: @sunyi0505
- **评论数**: 7

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

vllm:0.7.3
vllm-ascend:0.7.3

使用verl框架对Qwen2.5-vl-7b模型进行GRPO训练，第二个step会出现RuntimeError: shape '[-1, 3, 80, 1280]' is invalid for input size 1966080

