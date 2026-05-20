# Issue #3957: v0.11.0rc0 版本 单机 tp2 dp4 ep8拉起推理服务后，请求端发送单个推理请求会卡着不返回，推理服务端报错退出

## 基本信息

- **编号**: #3957
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3957
- **创建时间**: 2025-11-03T07:59:18Z
- **关闭时间**: 2025-11-19T07:47:19Z
- **更新时间**: 2025-11-19T07:47:19Z
- **提交者**: @yanggang2735
- **评论数**: 1

## 标签

installation

## 问题描述

### Your current environment

部署脚本：
python -m vllm.entrypoints.openai.api_server --model /AIdata/JW/Qwen3-30B-A3B/ --served-model-name Qwen3-30B --tensor-parallel-size 2 --data-parallel-size 4 --trust-remote-code --enable-expert-parallel --gpu-memory-utilization 0.6

推理服务报错如下：

[错误日志tp2dp4ep8单机v0.11.0rc0.txt](https://github.com/user-attachments/files/23297804/tp2dp4ep8.v0.11.0rc0.txt)

