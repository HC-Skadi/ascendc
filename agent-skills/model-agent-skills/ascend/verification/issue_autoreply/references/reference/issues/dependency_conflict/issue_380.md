# Issue #380: [Bug]: Unable to run llama3.3 model

## 基本信息

- **编号**: #380
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/380
- **创建时间**: 2025-03-24T08:20:45Z
- **关闭时间**: 2025-05-14T02:47:34Z
- **更新时间**: 2025-05-14T02:47:35Z
- **提交者**: @LoSunny
- **评论数**: 9

## 标签

bug

## 问题描述

### Your current environment

Below are the results running [vllm-ascent collect_env.py script](https://raw.githubusercontent.com/vllm-project/vllm-ascend/main/collect_env.py)
```
$ python collect_env.py 
Collecting environment information...
Traceback (most recent call last):
  File "/home/user/userdata/vllm-ascend/collect_env.py", line 491, in <module>
    main()
  File "/home/user/userdata/vllm-ascend/collect_env.py", line 470, in main
    output = get_pretty_env_info()
  File "/home/user/userdata/vllm-ascend/collect_env.py", line 465, in get_pretty_env_info
    return pretty_str(get_env_info())
  File "/home/user/userdata/vllm-ascend/collect_env.py", line 354, in get_env_info
    vllm_version=get_vllm_version(),
  File "/home/user/userdata/vllm-ascend/collect_env.py", line 172, in get_vllm_version
    return _parse_version(__version__, __version_tuple__)
  File "/home/user/userdata/vllm-ascend/collect_env.py", line 159, in _parse_version
    if version_str.startswith('g'):
AttributeError: 'int' object has no attribute 'startswith'
[ERROR] 2025-03-24-16:04:34 (PID:103957, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```
And this is from the official `vllm` repo
```text
(vllm) user@dev-2e55ed22-654c-4ed3-a212-3936ce8faeda-f86k7:~/userdata/vllm$ python collect_env.py
/home/user/userdata/vllm/vllm/__init__.py:5: RuntimeWarning: Failed to read commit hash:
No module named 'vllm._version'
  from .version import __version__, __version_tuple__  # isort:skip
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False
CUDA used to build PyTorch: None
ROCM used to build PyTorch: N/A

OS: Ubuntu 18.04 LTS (aarch64)
GCC version: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0
Clang version: Could not collect
CMake version: Could not collect
Libc version: glibc-2.27

Python version: 3.11.11 (main, Dec 11 2024, 16:19:35) [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-5.15.0-100-generic-aarch64-with-glibc2.27
Is CUDA available: False
CUDA runtime version: No CUDA
CUDA_MODULE_LOADING set to: N/A
GPU models and configuration: No CUDA
Nvidia driver version: No CUDA
cuDNN version: No CUDA
HIP runtime version: N/A
MIOpen runtime version: N/A
Is XNNPACK available: True

CPU:
Architecture:        aarch64
Byte Order:          Little Endian
CPU(s):              192
On-line CPU(s) list: 0-191
Thread(s) per core:  1
Core(s) per socket:  48
Socket(s):           4
NUMA node(s):        8
Vendor ID:           0x48
Model:               0
Stepping:            0x1
CPU max MHz:         2600.0000
CPU min MHz:         200.0000
BogoMIPS:            200.00
L1d cache:           64K
L1i cache:           64K
L2 cache:            512K
L3 cache:            24576K
NUMA node0 CPU(s):   0-23
NUMA node1 CPU(s):   24-47
NUMA node2 CPU(s):   48-71
NUMA node3 CPU(s):   72-95
NUMA node4 CPU(s):   96-119
NUMA node5 CPU(s):   120-143
NUMA node6 CPU(s):   144-167
NUMA node7 CPU(s):   168-191
Flags:               fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.3.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250308
[pip3] transformers==4.50.0
[conda] numpy                     1.26.4                   pypi_0    pypi
[conda] pyzmq                     26.3.0                   pypi_0    pypi
[conda] torch                     2.5.1                    pypi_0    pypi
[conda] torch-npu                 2.5.1.dev20250308          pypi_0    pypi
[conda] transformers              4.50.0                   pypi_0    pypi
ROCM Version: Could not collect
Neuron SDK Version: N/A
vLLM Version: N/A (dev)
vLLM Build Flags:
CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled
GPU Topology:
Could not collect

LD_LIBRARY_PATH=/home/user/teamdata/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/home/user/teamdata/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/home/user/teamdata/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/home/user/teamdata/Ascend/ascend-toolkit/latest/tools/aml/lib64:/home/user/teamdata/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/home/user/teamdata/Ascend/ascend-toolkit/latest/lib64:/home/user/teamdata/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/home/user/teamdata/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/home/user/teamdata/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/nvidia/lib64/:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/tools/hccn_tool/:/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64/:/usr/lib/aarch64-linux-gnu/hdf5/serial:/usr/local/python3.7.5/lib:
TORCH_DEVICE_BACKEND_AUTOLOAD=1
NCCL_CUMEM_ENABLE=0
TORCHINDUCTOR_COMPILE_THREADS=1
(vllm) user@dev-2e55ed22-654c-4ed3-a212-3936ce8faeda-f86k7:~/userdata/vllm-ascend$ git branch
* (HEAD detached at v0.7.3rc1)
  main
```


### 🐛 Describe the bug

I try to run llama3.3 using vllm with the command
`vllm serve ~/userdata/models/meta-llama/Llama-3.3-70B-Instruct --tensor-parallel-size 4 --gpu-memory-utilization 1 --max-model-len 118784`
But it crashes
The logs are quite long, I paste it here https://pastebin.com/pB32KF4Q
