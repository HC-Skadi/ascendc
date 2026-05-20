# Issue #3439: [Misc]: 自定义算子注册问题

## 基本信息

- **编号**: #3439
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3439
- **创建时间**: 2025-10-14T03:30:55Z
- **关闭时间**: 2025-10-14T06:26:48Z
- **更新时间**: 2025-10-14T06:26:48Z
- **提交者**: @super-chao1997
- **评论数**: 0

## 标签

无

## 问题描述

### Anything you want to discuss about vllm on ascend.

vllm-ascend提供的官方镜像中torch和torch_npu版本都是2.7；
在通过Ascend Extension for PyTorch进行自定义算子注册到torch_npu，供框架调用时，没有可选的2.7版本，最高只支持2.6版本，这个问题如何解决？

<img width="1443" height="1029" alt="Image" src="https://github.com/user-attachments/assets/7ca924a8-eb90-49e4-96c6-ec0db1d7d1e3" />
