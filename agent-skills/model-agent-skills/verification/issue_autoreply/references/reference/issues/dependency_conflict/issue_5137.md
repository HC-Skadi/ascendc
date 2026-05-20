# Issue #5137: [Bug]: 910B4部署Qwen3 Next出现NPU OOM问题

## 基本信息

- **编号**: #5137
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5137
- **创建时间**: 2025-12-17T11:00:52Z
- **关闭时间**: 2025-12-24T04:06:01Z
- **更新时间**: 2026-02-06T03:47:48Z
- **提交者**: @Sariel2
- **评论数**: 4

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

根据教程启动，启动命令
```shell
vllm serve /data/models/Qwen3-Next-80B-A3B-Instruct --tensor-parallel-size 4 --max-model-len 4096 --gpu-memory-utilization 0.85 --host=0.0.0.0 --port=30601 --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}'
```

出现异常

<img width="3140" height="7932" alt="Image" src="https://github.com/user-attachments/assets/b75a4739-e2de-4245-a0f6-d4be8be686d6" />
