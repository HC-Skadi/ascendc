# Issue #176: [Bug]: Qwen/Qwen1.5-MoE-A2.7B-Chat模型启动报错

## 基本信息

- **编号**: #176
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/176
- **创建时间**: 2025-02-26T08:04:04Z
- **关闭时间**: 2025-02-26T09:58:16Z
- **更新时间**: 2025-02-26T09:58:29Z
- **提交者**: @Luo-Jinyan
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>npu910B && vllm-ascend0.7.1rc1</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

报错信息
```python
 File "vllm_ascend/ops/fused_moe.py", line 152, in forward_oot
    topk_weights, topk_ids = group_topk(
  File "vllm_ascend/ops/fused_moe.py", line 49, in group_topk
    torch_npu.npu_group_topk(input=scores, out=scores, group_num=num_expert_group, k=topk_group)
  File "venv/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
    return self._op(*args, **(kwargs or {}))
RuntimeError: npu::npu_group_topk() Expected a value of type 'int' for argument 'k' but instead found type 'NoneType'.
```
这个报错应该是因为在调用group_topk送了topk_group=None导致的，不确定这里是对支持的MoE模型有要求，还是其他原因.
