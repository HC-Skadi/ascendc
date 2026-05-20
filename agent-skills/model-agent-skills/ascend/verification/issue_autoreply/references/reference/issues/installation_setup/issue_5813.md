# Issue #5813: [Bug]: 部署Qwen3-8B-W8A8  layers.0.mlp.gate_up_proj.deq_scale

**类型**: Issue

## 问题背景
### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
[root@DS-01 0.13.0]# docker exec -it c8a bash -c "python -m vllm.collect_env"
Collecting environment information...
==============================
        System Info
==============================
OS                           : Ubuntu 22.04.5 LTS (aarch64)
GCC version                  : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version                : Could not collect
CMake version                : version 4.2.1
Libc version                 : glibc-2.35

==============================
       PyTorch Info
==============================
PyTorch version              : 2.8.0+cpu
Is debug build               : False
CUDA used to build PyTorch   : None
ROCM used to build PyTorch   : N/A

==============================
      Python Environment
==============================
Python version               : 3.11.13 (main, Nov 20 2025, 16:02:27) [GCC 11.4.0] (64-bit runtime)
Python pla

## 基本信息
- **编号**: #5813
- **作者**: impptg
- **创建时间**: 2026-01-12T10:02:36Z
- **关闭时间**: 2026-01-15T07:54:21Z
- **标签**: bug

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/5813)
