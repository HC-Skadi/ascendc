# Issue #5438: [Bug]: Qwen3-VL-235B accuracy degradation in PD-separated scenario when KVcache is full

## 基本信息

- **编号**: #5438
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5438
- **创建时间**: 2025-12-27T09:21:27Z
- **关闭时间**: 2025-12-30T11:00:35Z
- **更新时间**: 2025-12-30T11:00:36Z
- **提交者**: @Levi-JQ
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
```

</details>


### 🐛 Describe the bug

复现条件
（1）使用大并发长输出bench脚本压测，观察D节点KV cache利用率
（2）KV cache打满时，使用精度测试脚本，可观察到有乱回复情况
