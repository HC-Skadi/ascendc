# Issue #167: [Usage]: npu-910b 安装vllm和vllm-ascend成功后，可以直接多卡推理模型，但是不能使用Online Serving on Multi Machine

## 基本信息

- **编号**: #167
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/167
- **创建时间**: 2025-02-26T02:35:24Z
- **关闭时间**: 2025-02-27T11:29:50Z
- **更新时间**: 2025-02-27T11:29:50Z
- **提交者**: @YuanJZhang
- **评论数**: 8

## 标签

bug

## 问题描述


npu-smi 24.1.rc2.1               Version: 24.1.rc2.1 
cann版本是8.0.0
python 3.10
torch2.51
使用https://vllm-ascend.readthedocs.io/en/latest/tutorials.html 中Online Serving on Multi Machine进行单机部署服务时报错

