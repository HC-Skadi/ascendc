# Issue #1188: [Installation]: The relationship between vllm-ascend 0.9.0 and torch versions

## 基本信息

- **编号**: #1188
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1188
- **创建时间**: 2025-06-12T08:30:31Z
- **关闭时间**: 2025-06-15T03:00:03Z
- **更新时间**: 2025-06-15T03:29:12Z
- **提交者**: @RyanOvO
- **评论数**: 2

## 标签

installation

## 问题描述

### Your current environment

```text
vllm: 0.9.0
vllm-ascend: 0.9.0
CANN: 8.1.rc1
```


### How you are installing vllm and vllm-ascend

![Image](https://github.com/user-attachments/assets/0722eef0-73a0-4f5f-a738-6651a7fa48d4)

vllm 0.9.0 requires torch version 2.7.0. torch has this version, but Torch-NPU does not have this version. Currently, I have installed version 2.5.1 of torch and Torch-NPU.
Should we consider dealing with this situation?  Which version of torch and Torcher-NPU should I install ?

![Image](https://github.com/user-attachments/assets/272ecd54-1537-4969-9b68-2321cf388dc8)
