# Issue #2674: [Bug]: moe_dispatch_v2 & moe_combine_v2 operations do not verify improper `HCCL_BUFFSIZE`

## 基本信息

- **编号**: #2674
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2674
- **创建时间**: 2025-09-01T06:41:28Z
- **关闭时间**: 2025-10-14T12:29:34Z
- **更新时间**: 2025-10-14T12:29:34Z
- **提交者**: @linfeng-yuan
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
vllm v0.9.1
vllm-ascend v0.9.1-dev
```

</details>


### 🐛 Describe the bug

I tested the disaggregated_prefill and PD fusion deployments of deepseek with torchair graph mode. While setting `HCCL_BUFFSIZE` to 50 with `ep_size` >= 16 and actual `batch_size` == 4 for each DP group, the output log should contain `HCCL BUFFSIZE is too small` with recommended configuration. But now, the verification doesn't appear while executing the operations and the output error contains 'The DDR address of the MTE instruction is out of range' instead.


