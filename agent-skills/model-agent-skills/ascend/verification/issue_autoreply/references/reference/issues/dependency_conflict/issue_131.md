# Issue #131: Qwen2.5-VL-7B的问题

## 基本信息

- **编号**: #131
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/131
- **创建时间**: 2025-02-21T08:05:56Z
- **关闭时间**: 2025-04-10T09:13:54Z
- **更新时间**: 2025-04-10T09:13:55Z
- **提交者**: @ffanyt
- **评论数**: 8

## 标签

bug

## 问题描述

我的命令是：
`vllm serve /home/share/models/Qwen2.5-VL-3B-Instruct --limit_mm_per_prompt image=5 \
    --dtype float16 \
    --port 10004 \
    --tensor-parallel-size 4 \
    --gpu-memory-utilization 0.9 \
     --max-model-len 32768`

我发现7B的模型会回答感叹号

![Image](https://github.com/user-attachments/assets/2bdbc0c7-1754-4630-ba96-6b223b66ad54)

而3b的模型一切正常
