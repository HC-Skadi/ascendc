# Issue #3994: [Bug]: [Nightly]Qwen3-235B-w8a8 server started failed

## 基本信息

- **编号**: #3994
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3994
- **创建时间**: 2025-11-05T01:22:22Z
- **关闭时间**: 2025-12-15T07:36:08Z
- **更新时间**: 2025-12-15T07:36:38Z
- **提交者**: @jiangyunfan1
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

RuntimeError: The size of tensor a (6) must match the size of tensor b (3) at non-singleton dimension 0
https://github.com/vllm-project/vllm-ascend/actions/runs/19065510094/job/54455045953?pr=3973
