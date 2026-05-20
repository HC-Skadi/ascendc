# Issue #825: [Bug]: Many unused `UserWorkspaceSize0` log print

## 基本信息

- **编号**: #825
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/825
- **创建时间**: 2025-05-12T11:12:57Z
- **关闭时间**: 2025-06-16T03:28:45Z
- **更新时间**: 2025-06-16T03:28:45Z
- **提交者**: @sunyi0505
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

推理过程中调用torch_npu.npu_mrope接口会一直打印UserWorkspaceSize0，最后导致日志太大无法打开
接口调用位置在 vllm_ascend/ops/rotary_embedding.py
