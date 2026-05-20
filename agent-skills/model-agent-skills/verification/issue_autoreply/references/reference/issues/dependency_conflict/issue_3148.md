# Issue #3148: [Bug]: Qwen3-8b-eagle3启动失败

## 基本信息

- **编号**: #3148
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3148
- **创建时间**: 2025-09-24T08:16:37Z
- **关闭时间**: 2025-10-10T09:22:39Z
- **更新时间**: 2025-10-10T09:22:39Z
- **提交者**: @sunchendd
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

版本0.10.2rc1
问题描述：
Qwen3-8b-eagle3启动失败

### 🐛 Describe the bug

启动脚本
ASCEND_RT_VISIBLE_DEVICES=15 python -m vllm.entrypoints.openai.api_server     --host 0.0.0.0     --served-model-name Qwen3-8B     --port 8000     --model /data/weight/scd/Qwen3-8B/     --seed 42     -tp 1     --speculative_config '{"model": "/data/weight/scd/AngelSlim/Qwen3-8B_eagle3/", "draft_tensor_parallel_size": 1, "num_speculative_tokens": 5, "method": "eagle3"}'

报错日志

[log.txt.txt](https://github.com/user-attachments/files/22509207/log.txt.txt)

