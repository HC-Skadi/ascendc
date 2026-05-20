# Issue #5771: [Bug]:DeepseekOCR模型单机单卡部署，开启入图后服务无法启动

**类型**: Issue

## 问题背景
### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```
PyTorch version: 2.8.0+cpu
Is debug build: False

OS: Ubuntu 24.04.3 LTS (aarch64)
GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0
Clang version: Could not collect
CMake version: version 4.1.2
Libc version: glibc-2.39

Python version: 3.11.10 (main, Nov  7 2025, 18:12:58) [GCC 13.3.0] (64-bit runtime)
Python platform: Linux-5.15.0-25-generic-aarch64-with-glibc2.39

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          256
On-line CPU(s) list:             0-255
Vendor ID:                       HiSilicon
BIOS Vendor ID:                  HiSilicon
Model name:                      Kunpeng-920
BIOS Model name:                 HUAWEI Kunpeng 920 7265 To be filled by O.E.M. CPU @ 3.0GHz
BIOS CPU family:                 280
Model:        

## 基本信息
- **编号**: #5771
- **作者**: wangbei25HW
- **创建时间**: 2026-01-09T09:45:21Z
- **关闭时间**: 2026-01-15T07:42:33Z
- **标签**: bug

## 涉及版本
- vLLM: 0.14.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/5771)
