# Issue #5993: [Bug]: 双机 A2 800 (64Gx8) vllm-ascend:v0.13.0rc1 部署 DeepSeek-V3.1-w8a8-mtp-QuaRot 失败

**类型**: Issue

## 问题背景
### Your current environment



#### 一、基本信息
```text
=== 操作系统信息 ===                                  
NAME="openEuler"                                     
VERSION="22.03 LTS"                                                                                       
=== 内核与架构 ===                                                                          
Linux worker-25 5.10.0-60.18.0.50.oe2203.aarch64 #1 SMP Wed Mar 30 02:43:08 UTC 2022 aarch64 aarch64 aarch64 GNU/Linux 

=== CPU 信息 ===                                                                           
Architecture:                    aarch64                                                   
CPU(s):                          192       

=== 华为服务器型号 ===                                                                      
 Product Name          : Atlas 800 9000 A2

模型参数来源：https://modelscope.cn/models/Eco-Tech/DeepSeek-V3.1-w8a8-mtp-QuaRot
```

#### 二、操作记录
##### （1）两个节点的容器启动命令
```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.13.0rc1


## 基本信息
- **编号**: #5993
- **作者**: shilongx
- **创建时间**: 2026-01-19T06:12:45Z
- **关闭时间**: 2026-01-20T03:35:18Z
- **标签**: bug

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/5993)
