# Issue #1000: [Bug]: Qwen2-VL-7B-Instruct oom on single card (64GB)

## 基本信息

- **编号**: #1000
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1000
- **创建时间**: 2025-05-29T02:20:50Z
- **关闭时间**: 2025-07-13T09:30:46Z
- **更新时间**: 2025-07-13T09:30:46Z
- **提交者**: @wenba0
- **评论数**: 1

## 标签

bug; module:multimodal

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

Qwen2-VL-7B-Instruct模型，相同的64G显存，A100单张卡就可以拉起来，昇腾800I-A2需要两张卡才能拉起来

