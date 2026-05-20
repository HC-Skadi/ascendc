# Issue #3885: [Bug]: MTP aclgraph error

## 基本信息

- **编号**: #3885
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3885
- **创建时间**: 2025-10-30T01:49:56Z
- **关闭时间**: 2025-12-11T07:53:08Z
- **更新时间**: 2025-12-11T07:53:08Z
- **提交者**: @JC-ut0
- **评论数**: 2

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

Currently mtp aclgraph working fine with vllm v0.11.0, but is broken in the main branch.
The issue is that the original logic brings device-to-host operation as position is a device tensor and the indexing operation inputs_embeds[positions == 0] will trigger a d2h synchornization. This breaks the static graph mode in vllm-ascend.

https://github.com/vllm-project/vllm/pull/27643 will fix this issue
