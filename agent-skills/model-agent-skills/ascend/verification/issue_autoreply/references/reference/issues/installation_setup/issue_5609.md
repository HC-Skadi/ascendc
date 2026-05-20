# Issue #5609: [Bug]: Mooncake is broken in vllm-ascend v0.12.0rc1 docker image

**类型**: Issue

## 问题背景
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

## 基本信息
- **编号**: #5609
- **作者**: gcanlin
- **创建时间**: 2026-01-05T08:46:58Z
- **关闭时间**: 2026-01-06T01:03:00Z
- **标签**: bug

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/5609)
