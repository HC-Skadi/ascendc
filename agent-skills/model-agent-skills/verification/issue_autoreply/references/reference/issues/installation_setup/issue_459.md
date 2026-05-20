# Issue #459: [Bug]: trl vllm-serve支持

## 基本信息

- **编号**: #459
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/459
- **创建时间**: 2025-04-02T01:25:08Z
- **关闭时间**: 2025-05-16T01:57:01Z
- **更新时间**: 2025-05-16T01:57:18Z
- **提交者**: @jiangix-paper
- **评论数**: 5

## 标签

feature request

## 问题描述

### Your current environment

vllm 0.7.1
vllm ascend 0.7.1
trl 0.16.0

### 🐛 Describe the bug

trl 0.16.0版本中已支持多机grpo，实现方式是vllm在单独节点推理，其他节点用来训练。其中，推理节点和训练节点之间的参数通信是通过

vllm.distribute中的PyNcclCommunicator.broadcast实现的，具体代码在：
https://github.com/huggingface/trl/blob/main/trl/scripts/vllm_serve.py

<img width="604" alt="Image" src="https://github.com/user-attachments/assets/71e581f4-035f-48fb-b111-f962fbd3e495" />

我尝试将此套方案在NPU部署，发现并未成功更新vllm的参数，感觉像是vllm在npu上不支持这么操作？不知道理解是否正确？还请帮忙看一下这个问题，非常感谢
