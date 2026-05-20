# Issue #5609: [Bug]: Mooncake is broken in vllm-ascend v0.12.0rc1 docker image

## 基本信息

- **编号**: #5609
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5609
- **创建时间**: 2026-01-05T08:46:58Z
- **关闭时间**: 2026-01-06T01:03:00Z
- **更新时间**: 2026-01-06T01:03:00Z
- **提交者**: @gcanlin
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

It seems that mooncake is broken in vllm-ascend v0.12.0rc1 docker image.

```
python -c "from mooncake.store import MooncakeDistributedStore"
corrupted size vs. prev_size
Aborted (core dumped)
```
