# Issue #3454: [Bug]: 一行代码开1T cpu内存

## 基本信息

- **编号**: #3454
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3454
- **创建时间**: 2025-10-14T11:32:57Z
- **关闭时间**: 2025-11-18T13:44:02Z
- **更新时间**: 2025-11-19T07:29:03Z
- **提交者**: @liuzhenjluccst
- **评论数**: 20

## 标签

bug

## 问题描述

### Your current environment

0.11.0rc0


### 🐛 Describe the bug

上下文256k时，8卡单实例，attn mask一行代码开了1T. Cpu内存，超出atlas主机硬件限制，见图片

![Image](https://github.com/user-attachments/assets/5e0c1bdc-5af7-4c74-9ec0-401dff94a0da)

256k乘256k，bf16为2字节再乘以2，每卡一个线程都会跑到这，所以乘以8，总计1个T
