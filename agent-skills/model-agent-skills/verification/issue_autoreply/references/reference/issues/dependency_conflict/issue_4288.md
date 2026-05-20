# Issue #4288: [Bug]: [Nightly]multi-node A3 eplb failed

## 基本信息

- **编号**: #4288
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4288
- **创建时间**: 2025-11-20T01:58:18Z
- **关闭时间**: 2025-11-20T02:06:05Z
- **更新时间**: 2025-11-20T02:06:05Z
- **提交者**: @jiangyunfan1
- **评论数**: 0

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

https://github.com/vllm-project/vllm-ascend/actions/runs/19508448638/job/55854114399
https://github.com/vllm-project/vllm-ascend/actions/runs/19508448638/job/55855036389
The task failed while the env DYNAMIC_EPLB is set
