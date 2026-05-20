# Issue #6842: [Bug]: 310P 使用quay.io/ascend/vllm-ascend:v0.14.0rc1-310p-openeuler部署qwen3-vl时报错

## 基本信息

- **编号**: #6842
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6842
- **创建时间**: 2026-02-27T03:14:56Z
- **关闭时间**: 2026-02-28T02:17:15Z
- **更新时间**: 2026-02-28T02:17:15Z
- **提交者**: @fengle-great
- **评论数**: 1

## 标签

bug

## 问题描述

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
BIOS Model name:                    HUAWEI Kunpeng 920 3210 To be filled by O.E.M. CPU @ 2.6GHz
BIOS CPU family:                    280
Model:                              0
Thread(s) per core:                 1
Core(s) per socket:                 24
Socket(s):                          2
Stepping:                           0x1
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                          3 MiB (48 instances)
L1i cache:                          3 MiB (48 instances)
L2 cache:                           24 MiB (48 instances)
L3 cache:                           48 MiB (2 instances)
NUMA node(s):                       2
NUMA node0 CPU(s):                  0-23
NUMA node1 CPU(s):                  24-47
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass:    Not affected
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.9.0+cpu
[pip3] torch_npu==2.9.0
[pip3] torchvision==0.24.0
[pip3] transformers==4.57.6
[pip3] triton-ascend==3.2.0
[conda] Could not collect
vLLM Version: 0.14.1
vLLM Ascend Version: 0.14.0rc1

ENV Variables:
ASCEND_TOOLKIT_LATEST_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/cann-8.5.0
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/cann-8.5.0/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/cann-8.5.0/lib64:/usr/local/Ascend/cann-8.5.0/lib64/plugin/opskernel:/usr/local/Ascend/cann-8.5.0/lib64/plugin/nnengine:/usr/local/Ascend/cann-8.5.0/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/cann-8.5.0/tools/aml/lib64:/usr/local/Ascend/cann-8.5.0/tools/aml/lib64/plugin:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/cann-8.5.0
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/cann-8.5.0
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+--------------------------------------------------------------------------------------------------------+
| npu-smi 25.3.rc1                                 Version: 25.3.rc1                                     |
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Name                  | Health          | Power(W)     Temp(C)           Hugepages-Usage(page) |
| Chip    Device                | Bus-Id          | AICore(%)    Memory-Usage(MB)                        |
+===============================+=================+======================================================+
| 0       310P3                 | OK              | NA           51                0     / 0             |
| 0       0                     | 0000:01:00.0    | 0            1615 / 44278                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 0       310P3                 | OK              | NA           51                0     / 0             |
| 1       1                     | 0000:01:00.0    | 0            1322 / 43693                            |
+===============================+=================+======================================================+
| 32      310P3                 | OK              | NA           50                0     / 0             |
| 0       2                     | 0000:02:00.0    | 0            1581 / 44278                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 32      310P3                 | OK              | NA           49                0     / 0             |
| 1       3                     | 0000:02:00.0    | 0            1354 / 43693                            |
+===============================+=================+======================================================+
| 32768   310P3                 | OK              | NA           52                0     / 0             |
| 0       4                     | 0000:81:00.0    | 0            1541 / 44278                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 32768   310P3                 | OK              | NA           46                0     / 0             |
| 1       5                     | 0000:81:00.0    | 0            1391 / 43693                            |
+===============================+=================+======================================================+
| 32800   310P3                 | OK              | NA           51                0     / 0             |
| 0       6                     | 0000:82:00.0    | 0            1716 / 44278                            |
+-------------------------------+-----------------+------------------------------------------------------+
| 32800   310P3                 | OK              | NA           52                0     / 0             |
| 1       7                     | 0000:82:00.0    | 0            1216 / 43693                            |
+===============================+=================+======================================================+
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Chip                  | Process id      | Process name             | Process memory(MB)        |
+===============================+=================+======================================================+
| No running processes found in NPU 0                                                                    |
+===============================+=================+======================================================+
| No running processes found in NPU 32                                                                   |
+===============================+=================+======================================================+
| No running processes found in NPU 32768                                                                |
+===============================+=================+======================================================+
| No running processes found in NPU 32800                                                                |
+===============================+=================+======================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.5.0
innerversion=V100R001C25SPC001B232
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/cann-8.5.0
```

</details>


### 🐛 Describe the bug

启动报错，启动命令为：```vllm serve /cloud/model/Qwen3-VL-32B-Instruct/ --host 0.0.0.0 --port 1025  --gpu-memory-utilization 0.85 --served-model-name vl_model   --tensor-parallel-size 8  --allowed-local-media-path /cloud/xxx/AIEngine/tmp/   --dtype float16 --max_model_len 40960  --enforce-eager```，日志如下：
[rank7]:[E227 10:31:12.038515350 compiler_depend.ts:444] SelfAttentionOperation setup failed!
Exception raised from OperationSetup at build/third_party/op-plugin/op_plugin/CMakeFiles/op_plugin_atb.dir/compiler_depend.ts:203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xb0 (0xffffaa70c700 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x68 (0xffffaa6aa860 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: atb::OperationSetup(atb::VariantPack, atb::Operation*, atb::Context*) + 0x278 (0xffff6c330498 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #3: <unknown function> + 0xb1b74 (0xffff6c331b74 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #4: <unknown function> + 0x2c77e24 (0xffff997b7e24 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0xa607d0 (0xffff975a07d0 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0xa613ac (0xffff975a13ac in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0xa5f2c8 (0xffff9759f2c8 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #8: <unknown function> + 0xd442c (0xffffb7cd442c in /lib64/libstdc++.so.6)
frame #9: <unknown function> + 0x7fbb4 (0xffffb7ebfbb4 in /lib64/libc.so.6)
frame #10: <unknown function> + 0xe7c0c (0xffffb7f27c0c in /lib64/libc.so.6)

[rank6]:[E227 10:31:13.352890220 compiler_depend.ts:444] SelfAttentionOperation setup failed!
Exception raised from OperationSetup at build/third_party/op-plugin/op_plugin/CMakeFiles/op_plugin_atb.dir/compiler_depend.ts:203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xb0 (0xffff8434c700 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x68 (0xffff842ea860 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: atb::OperationSetup(atb::VariantPack, atb::Operation*, atb::Context*) + 0x278 (0xffff45f90498 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #3: <unknown function> + 0xb1b74 (0xffff45f91b74 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #4: <unknown function> + 0x2c77e24 (0xffff733f7e24 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0xa607d0 (0xffff711e07d0 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0xa613ac (0xffff711e13ac in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0xa5f2c8 (0xffff711df2c8 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #8: <unknown function> + 0xd442c (0xffff9192442c in /lib64/libstdc++.so.6)
frame #9: <unknown function> + 0x7fbb4 (0xffff91b0fbb4 in /lib64/libc.so.6)
frame #10: <unknown function> + 0xe7c0c (0xffff91b77c0c in /lib64/libc.so.6)

[rank0]:[E227 10:31:13.369908650 compiler_depend.ts:444] SelfAttentionOperation setup failed!
Exception raised from OperationSetup at build/third_party/op-plugin/op_plugin/CMakeFiles/op_plugin_atb.dir/compiler_depend.ts:203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xb0 (0xffff886dc700 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x68 (0xffff8867a860 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: atb::OperationSetup(atb::VariantPack, atb::Operation*, atb::Context*) + 0x278 (0xffff4a330498 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #3: <unknown function> + 0xb1b74 (0xffff4a331b74 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #4: <unknown function> + 0x2c77e24 (0xffff77787e24 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0xa607d0 (0xffff755707d0 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0xa613ac (0xffff755713ac in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0xa5f2c8 (0xffff7556f2c8 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #8: <unknown function> + 0xd442c (0xffff95cc442c in /lib64/libstdc++.so.6)
frame #9: <unknown function> + 0x7fbb4 (0xffff95eafbb4 in /lib64/libc.so.6)
frame #10: <unknown function> + 0xe7c0c (0xffff95f17c0c in /lib64/libc.so.6)

[rank5]:[E227 10:31:13.476193390 compiler_depend.ts:444] SelfAttentionOperation setup failed!
Exception raised from OperationSetup at build/third_party/op-plugin/op_plugin/CMakeFiles/op_plugin_atb.dir/compiler_depend.ts:203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xb0 (0xffff893ac700 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x68 (0xffff8934a860 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: atb::OperationSetup(atb::VariantPack, atb::Operation*, atb::Context*) + 0x278 (0xffff4aff0498 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #3: <unknown function> + 0xb1b74 (0xffff4aff1b74 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #4: <unknown function> + 0x2c77e24 (0xffff78457e24 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0xa607d0 (0xffff762407d0 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0xa613ac (0xffff762413ac in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0xa5f2c8 (0xffff7623f2c8 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #8: <unknown function> + 0xd442c (0xffff9697442c in /lib64/libstdc++.so.6)
frame #9: <unknown function> + 0x7fbb4 (0xffff96b5fbb4 in /lib64/libc.so.6)
frame #10: <unknown function> + 0xe7c0c (0xffff96bc7c0c in /lib64/libc.so.6)

[rank3]:[E227 10:31:13.476680270 compiler_depend.ts:444] SelfAttentionOperation setup failed!
Exception raised from OperationSetup at build/third_party/op-plugin/op_plugin/CMakeFiles/op_plugin_atb.dir/compiler_depend.ts:203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xb0 (0xffffa5f4c700 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x68 (0xffffa5eea860 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: atb::OperationSetup(atb::VariantPack, atb::Operation*, atb::Context*) + 0x278 (0xffff67b90498 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #3: <unknown function> + 0xb1b74 (0xffff67b91b74 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #4: <unknown function> + 0x2c77e24 (0xffff94ff7e24 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0xa607d0 (0xffff92de07d0 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0xa613ac (0xffff92de13ac in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0xa5f2c8 (0xffff92ddf2c8 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #8: <unknown function> + 0xd442c (0xffffb354442c in /lib64/libstdc++.so.6)
frame #9: <unknown function> + 0x7fbb4 (0xffffb372fbb4 in /lib64/libc.so.6)
frame #10: <unknown function> + 0xe7c0c (0xffffb3797c0c in /lib64/libc.so.6)

[rank1]:[E227 10:31:13.511813330 compiler_depend.ts:444] SelfAttentionOperation setup failed!
Exception raised from OperationSetup at build/third_party/op-plugin/op_plugin/CMakeFiles/op_plugin_atb.dir/compiler_depend.ts:203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xb0 (0xffff7537c700 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x68 (0xffff7531a860 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: atb::OperationSetup(atb::VariantPack, atb::Operation*, atb::Context*) + 0x278 (0xffff36fc0498 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #3: <unknown function> + 0xb1b74 (0xffff36fc1b74 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #4: <unknown function> + 0x2c77e24 (0xffff64427e24 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0xa607d0 (0xffff622107d0 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0xa613ac (0xffff622113ac in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0xa5f2c8 (0xffff6220f2c8 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #8: <unknown function> + 0xd442c (0xffff8295442c in /lib64/libstdc++.so.6)
frame #9: <unknown function> + 0x7fbb4 (0xffff82b3fbb4 in /lib64/libc.so.6)
frame #10: <unknown function> + 0xe7c0c (0xffff82ba7c0c in /lib64/libc.so.6)

[rank4]:[E227 10:31:14.107249390 compiler_depend.ts:444] SelfAttentionOperation setup failed!
Exception raised from OperationSetup at build/third_party/op-plugin/op_plugin/CMakeFiles/op_plugin_atb.dir/compiler_depend.ts:203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xb0 (0xffff923ac700 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x68 (0xffff9234a860 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: atb::OperationSetup(atb::VariantPack, atb::Operation*, atb::Context*) + 0x278 (0xffff53ff0498 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #3: <unknown function> + 0xb1b74 (0xffff53ff1b74 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #4: <unknown function> + 0x2c77e24 (0xffff81457e24 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0xa607d0 (0xffff7f2407d0 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0xa613ac (0xffff7f2413ac in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0xa5f2c8 (0xffff7f23f2c8 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #8: <unknown function> + 0xd442c (0xffff9f99442c in /lib64/libstdc++.so.6)
frame #9: <unknown function> + 0x7fbb4 (0xffff9fb7fbb4 in /lib64/libc.so.6)
frame #10: <unknown function> + 0xe7c0c (0xffff9fbe7c0c in /lib64/libc.so.6)

[rank2]:[E227 10:31:14.969577420 compiler_depend.ts:444] SelfAttentionOperation setup failed!
Exception raised from OperationSetup at build/third_party/op-plugin/op_plugin/CMakeFiles/op_plugin_atb.dir/compiler_depend.ts:203 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xb0 (0xffff8a10c700 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x68 (0xffff8a0aa860 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: atb::OperationSetup(atb::VariantPack, atb::Operation*, atb::Context*) + 0x278 (0xffff4bd30498 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #3: <unknown function> + 0xb1b74 (0xffff4bd31b74 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libop_plugin_atb.so)
frame #4: <unknown function> + 0x2c77e24 (0xffff791b7e24 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0xa607d0 (0xffff76fa07d0 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0xa613ac (0xffff76fa13ac in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0xa5f2c8 (0xffff76f9f2c8 in /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #8: <unknown function> + 0xd442c (0xffff976d442c in /lib64/libstdc++.so.6)
frame #9: <unknown function> + 0x7fbb4 (0xffff978bfbb4 in /lib64/libc.so.6)
frame #10: <unknown function> + 0xe7c0c (0xffff97927c0c in /lib64/libc.so.6)

(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822] WorkerProc hit an exception.
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822] Traceback (most recent call last):
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 817, in worker_busy_loop
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     output = func(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 262, in determine_available_memory
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     self.model_runner.profile_run()
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2176, in profile_run
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     super().profile_run()
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/v1/worker/gpu_model_runner.py", line 4731, in profile_run
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     dummy_encoder_outputs = self.model.embed_multimodal(
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_vl.py", line 1913, in embed_multimodal
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     image_embeddings = self._process_image_input(multimodal_input)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_vl.py", line 1428, in _process_image_input
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     image_embeds = self.visual(pixel_values, grid_thw=grid_thw)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_vl.py", line 577, in forward
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     hidden_states = blk(
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]                     ^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_vl.py", line 249, in forward
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     x = x + self.attn(
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]             ^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 414, in forward
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     output, _ = self.proj(context_layer)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]                 ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/linear.py", line 307, in forward
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return super().forward(input_)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 1463, in forward
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     output = tensor_model_parallel_all_reduce(output_parallel)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/distributed/communication_op.py", line 14, in tensor_model_parallel_all_reduce
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return get_tp_group().all_reduce(input_)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/worker/patch_distributed.py", line 118, in all_reduce
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return torch.ops.vllm.all_reduce(input_, group_name=self.unique_name)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/_ops.py", line 1255, in __call__
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return self._op(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/distributed/parallel_state.py", line 122, in all_reduce
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return group._all_reduce_out_place(tensor)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/distributed/parallel_state.py", line 507, in _all_reduce_out_place
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return self.device_communicator.all_reduce(input_)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/distributed/device_communicators/base_device_communicator.py", line 136, in all_reduce
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     dist.all_reduce(input_, group=self.device_group)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_distributed.py", line 64, in all_reduce
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return fn(tensor, op, group, async_op)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/distributed/c10d_logger.py", line 81, in wrapper
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/distributed/distributed_c10d.py", line 2935, in all_reduce
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     work = group.allreduce([tensor], opts)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is SelfAttentionOperation.
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822] [ERROR] 2026-02-27-10:31:15 (PID:277, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822] 
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822] Traceback (most recent call last):
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 817, in worker_busy_loop
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     output = func(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 262, in determine_available_memory
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     self.model_runner.profile_run()
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2176, in profile_run
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     super().profile_run()
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/v1/worker/gpu_model_runner.py", line 4731, in profile_run
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     dummy_encoder_outputs = self.model.embed_multimodal(
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_vl.py", line 1913, in embed_multimodal
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     image_embeddings = self._process_image_input(multimodal_input)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_vl.py", line 1428, in _process_image_input
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     image_embeds = self.visual(pixel_values, grid_thw=grid_thw)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_vl.py", line 577, in forward
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     hidden_states = blk(
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]                     ^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_vl.py", line 249, in forward
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     x = x + self.attn(
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]             ^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 414, in forward
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     output, _ = self.proj(context_layer)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]                 ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return self._call_impl(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return forward_call(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/linear.py", line 307, in forward
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return super().forward(input_)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/model_executor/layers/linear.py", line 1463, in forward
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     output = tensor_model_parallel_all_reduce(output_parallel)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/distributed/communication_op.py", line 14, in tensor_model_parallel_all_reduce
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return get_tp_group().all_reduce(input_)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/worker/patch_distributed.py", line 118, in all_reduce
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return torch.ops.vllm.all_reduce(input_, group_name=self.unique_name)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/_ops.py", line 1255, in __call__
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return self._op(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/distributed/parallel_state.py", line 122, in all_reduce
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return group._all_reduce_out_place(tensor)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/distributed/parallel_state.py", line 507, in _all_reduce_out_place
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return self.device_communicator.all_reduce(input_)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/distributed/device_communicators/base_device_communicator.py", line 136, in all_reduce
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     dist.all_reduce(input_, group=self.device_group)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_distributed.py", line 64, in all_reduce
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return fn(tensor, op, group, async_op)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/distributed/c10d_logger.py", line 81, in wrapper
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     return func(*args, **kwargs)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/distributed/distributed_c10d.py", line 2935, in all_reduce
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]     work = group.allreduce([tensor], opts)
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822] RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is SelfAttentionOperation.
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822] [ERROR] 2026-02-27-10:31:15 (PID:277, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822] 
(Worker_TP0 pid=277) ERROR 02-27 10:31:15 [multiproc_executor.py:822] 
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936] EngineCore failed to start.
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936] Traceback (most recent call last):
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 927, in run_engine_core
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]     engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs)
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 692, in __init__
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]     super().__init__(
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 113, in __init__
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]     num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches(
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 243, in _initialize_kv_caches
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]     available_gpu_memory = self.model_executor.determine_available_memory()
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 126, in determine_available_memory
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]     return self.collective_rpc("determine_available_memory")
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 359, in collective_rpc
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]     return aggregate(get_response())
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]                      ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 342, in get_response
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936]     raise RuntimeError(
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936] RuntimeError: Worker failed with error 'The Inner error is reported as above. The process exits for this inner error, and the current working operator name is SelfAttentionOperation.
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936] Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936] Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936] [ERROR] 2026-02-27-10:31:15 (PID:277, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:15 [core.py:936] ', please check the stack trace above for the root cause
(EngineCore_DP0 pid=265) ERROR 02-27 10:31:24 [multiproc_executor.py:231] Worker proc VllmWorker-0 died unexpectedly, shutting down executor.
(EngineCore_DP0 pid=265) Process EngineCore_DP0:
(EngineCore_DP0 pid=265) Traceback (most recent call last):
(EngineCore_DP0 pid=265)   File "/usr/local/python3.11.14/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=265)     self.run()
(EngineCore_DP0 pid=265)   File "/usr/local/python3.11.14/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=265)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=265)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 940, in run_engine_core
(EngineCore_DP0 pid=265)     raise e
(EngineCore_DP0 pid=265)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 927, in run_engine_core
(EngineCore_DP0 pid=265)     engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs)
(EngineCore_DP0 pid=265)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=265)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 692, in __init__
(EngineCore_DP0 pid=265)     super().__init__(
(EngineCore_DP0 pid=265)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 113, in __init__
(EngineCore_DP0 pid=265)     num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches(
(EngineCore_DP0 pid=265)                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=265)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 243, in _initialize_kv_caches
(EngineCore_DP0 pid=265)     available_gpu_memory = self.model_executor.determine_available_memory()
(EngineCore_DP0 pid=265)                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=265)   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 126, in determine_available_memory
(EngineCore_DP0 pid=265)     return self.collective_rpc("determine_available_memory")
(EngineCore_DP0 pid=265)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=265)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 359, in collective_rpc
(EngineCore_DP0 pid=265)     return aggregate(get_response())
(EngineCore_DP0 pid=265)                      ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=265)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 342, in get_response
(EngineCore_DP0 pid=265)     raise RuntimeError(
(EngineCore_DP0 pid=265) RuntimeError: Worker failed with error 'The Inner error is reported as above. The process exits for this inner error, and the current working operator name is SelfAttentionOperation.
(EngineCore_DP0 pid=265) Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, please set the environment variable ASCEND_LAUNCH_BLOCKING=1.
(EngineCore_DP0 pid=265) Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
(EngineCore_DP0 pid=265) [ERROR] 2026-02-27-10:31:15 (PID:277, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(EngineCore_DP0 pid=265) ', please check the stack trace above for the root cause
(APIServer pid=245) Traceback (most recent call last):
(APIServer pid=245)   File "/usr/local/python3.11.14/bin/vllm", line 7, in <module>
(APIServer pid=245)     sys.exit(main())
(APIServer pid=245)              ^^^^^^
(APIServer pid=245)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 73, in main
(APIServer pid=245)     args.dispatch_function(args)
(APIServer pid=245)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 60, in cmd
(APIServer pid=245)     uvloop.run(run_server(args))
(APIServer pid=245)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/uvloop/__init__.py", line 92, in run
(APIServer pid=245)     return runner.run(wrapper())
(APIServer pid=245)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=245)   File "/usr/local/python3.11.14/lib/python3.11/asyncio/runners.py", line 118, in run
(APIServer pid=245)     return self._loop.run_until_complete(task)
(APIServer pid=245)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=245)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=245)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/uvloop/__init__.py", line 48, in wrapper
(APIServer pid=245)     return await main
(APIServer pid=245)            ^^^^^^^^^^
(APIServer pid=245)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1319, in run_server
(APIServer pid=245)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=245)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1338, in run_server_worker
(APIServer pid=245)     async with build_async_engine_client(
(APIServer pid=245)   File "/usr/local/python3.11.14/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=245)     return await anext(self.gen)
(APIServer pid=245)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=245)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 173, in build_async_engine_client
(APIServer pid=245)     async with build_async_engine_client_from_engine_args(
(APIServer pid=245)   File "/usr/local/python3.11.14/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=245)     return await anext(self.gen)
(APIServer pid=245)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=245)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 214, in build_async_engine_client_from_engine_args
(APIServer pid=245)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=245)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=245)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 205, in from_vllm_config
(APIServer pid=245)     return cls(
(APIServer pid=245)            ^^^^
(APIServer pid=245)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 132, in __init__
(APIServer pid=245)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=245)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=245)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 122, in make_async_mp_client
(APIServer pid=245)     return AsyncMPClient(*client_args)
(APIServer pid=245)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=245)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 824, in __init__
(APIServer pid=245)     super().__init__(
(APIServer pid=245)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 479, in __init__
(APIServer pid=245)     with launch_core_engines(vllm_config, executor_class, log_stats) as (
(APIServer pid=245)   File "/usr/local/python3.11.14/lib/python3.11/contextlib.py", line 144, in __exit__
(APIServer pid=245)     next(self.gen)
(APIServer pid=245)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 921, in launch_core_engines
(APIServer pid=245)     wait_for_engine_startup(
(APIServer pid=245)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 980, in wait_for_engine_startup
(APIServer pid=245)     raise RuntimeError(
(APIServer pid=245) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
(APIServer pid=245) [ERROR] 2026-02-27-10:31:27 (PID:245, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
(APIServer pid=245) sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute
