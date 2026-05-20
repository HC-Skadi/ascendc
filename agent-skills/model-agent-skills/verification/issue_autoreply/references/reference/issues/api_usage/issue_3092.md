# Issue #3092: [Bug]: vllm-ascend:v0.10.2rc1-310p-openeuler在300I Pro推理卡上运行OpenBMB/MiniCPM-V报错

## 基本信息

- **编号**: #3092
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3092
- **创建时间**: 2025-09-22T07:48:01Z
- **关闭时间**: 2025-12-23T12:08:30Z
- **更新时间**: 2025-12-23T12:08:30Z
- **提交者**: @WangLu95
- **评论数**: 1

## 标签

question; 310p

## 问题描述

### Your current environment

我用的是你们官方的docker 
硬件是300I Pro

### 🐛 Describe the bug

vllm-ascend-V  | (APIServer pid=1)     raise ImportError(
vllm-ascend-V  | (APIServer pid=1) ImportError: This modeling file requires the following packages that were not found in your environment: timm. Run `pip install timm`
vllm-ascend-V  | (APIServer pid=1) [ERROR] 2025-09-22-06:31:49 (PID:1, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
上面是运行MiniCPM-V的报错
gemma-3直接会部署失败
而运行InternVL2_5-8B、llava-v1.6-mistral-7b-hf、Phi-3.5-Vison这几个模型启动时不会报错，但存在累计大概14-30请求后，再请求就卡死的情况（能请求不报错就是不返回）
我看您们说300I推理卡是实验性的，就想了解在300I的硬件上到底能支持什么多模态大模型？是只有Qwen吗？
