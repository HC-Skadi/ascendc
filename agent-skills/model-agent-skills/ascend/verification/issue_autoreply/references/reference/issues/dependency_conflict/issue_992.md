# Issue #992: [Bug]: 发送请求卡死 偶现

## 基本信息

- **编号**: #992
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/992
- **创建时间**: 2025-05-28T09:45:13Z
- **关闭时间**: 2025-07-13T09:37:35Z
- **更新时间**: 2025-07-13T09:37:35Z
- **提交者**: @wenba0
- **评论数**: 2

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

昇腾800I-A2机器，模型Qwen2-VL-7B-Instruct，数据为textvqa
发送请求后卡死，偶现；问题解决：重新拉起服务化，重新发送
