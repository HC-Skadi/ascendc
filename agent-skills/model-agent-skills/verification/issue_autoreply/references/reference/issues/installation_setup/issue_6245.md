# Issue #6245: [Bug]: A3单机混部 vLLM0.13.0RC2镜像 部署DSV3.2报错

**类型**: Issue

## 问题背景
### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
[root@localhost hundsun]# python collect_env.py
Collecting environment information...
PyTorch version: 2.8.0+cpu
Is debug build: False

OS: openEuler 24.03 (LTS-SP2) (aarch64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-99.oe2403sp2)
Clang version: 17.0.6 ( 17.0.6-45.oe2403sp2)
CMake version: version 4.2.1
Libc version: glibc-2.38

Python version: 3.11.14 (main, Jan 21 2026, 07:05:42) [GCC 12.3.1 (openEuler 12.3.1-99.oe2403sp2)] (64-bit runtime)
Python platform: Linux-5.10.0-296.0.0.199.oe2203sp4.aarch64-aarch64-with-glibc2.38

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             640
On-line CPU(s) list:                0-639
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         -
BIOS M

## 基本信息
- **编号**: #6245
- **作者**: qxh84189941
- **创建时间**: 2026-01-26T03:01:05Z
- **关闭时间**: 2026-01-29T02:55:15Z
- **标签**: bug

## 涉及版本
- vLLM: 0.13.0

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/6245)
