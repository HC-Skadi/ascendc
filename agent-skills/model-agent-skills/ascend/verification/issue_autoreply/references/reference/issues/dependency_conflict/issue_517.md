# Issue #517: [Bug]: 使用qwen2.5微调的模型，在910B2卡上进行推理，生成的结果都是“！”

## 基本信息

- **编号**: #517
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/517
- **创建时间**: 2025-04-14T06:57:50Z
- **关闭时间**: 2025-04-14T07:01:56Z
- **更新时间**: 2025-04-14T07:01:57Z
- **提交者**: @TW-NLP
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

基于LoRA对qwen2.5微调的模型，在910B2卡上进行推理，生成的结果都是“！”
