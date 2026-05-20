# Issue #6842: [Bug]: 310P 使用quay.io/ascend/vllm-ascend:v0.14.0rc1-310p-openeuler部署qwen3-vl时报错

**类型**: Issue

## 问题背景
### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.9.0+cpu
Is debug build: False

OS: openEuler 24.03 (LTS-SP2) (aarch64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-99.oe2403sp2)
Clang version: Could not collect
CMake version: version 4.2.1
Libc version: glibc-2.38

Python version: 3.11.14 (main, Jan 21 2026, 08:13:04) [GCC 12.3.1 (openEuler 12.3.1-99.oe2403sp2)] (64-bit runtime)
Python platform: Linux-5.10.0-274.0.0.177.oe2203sp4.aarch64-aarch64-with-glibc2.38

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             48
On-line CPU(s) list:                0-47
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         Kunpeng-920
BIOS Model name:                    HUAWEI Kunpeng 920 321

## 基本信息
- **编号**: #6842
- **作者**: fengle-great
- **创建时间**: 2026-02-27T03:14:56Z
- **关闭时间**: 2026-02-28T02:17:15Z
- **标签**: bug

## 涉及版本
- vLLM: 0.14.1

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/6842)
