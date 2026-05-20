# Issue #1600: [main2mian CI]: cannot import name 'MoEConfig'

## 基本信息

- **编号**: #1600
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1600
- **创建时间**: 2025-07-03T00:52:08Z
- **关闭时间**: 2025-07-03T10:36:19Z
- **更新时间**: 2025-07-03T10:36:19Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

```
E   ImportError: cannot import name 'MoEConfig' from 'vllm.model_executor.layers.fused_moe.layer' (/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/layers/fused_moe/layer.py)
```

### 🐛 Describe the bug

https://github.com/vllm-project/vllm-ascend/actions/runs/16029006532/job/45224387842?pr=1596
