# Issue #5606: [Bug]: Exception in Qwen3-Next-80B-A3B-Instruct-W8A8  decode.

## 基本信息

- **编号**: #5606
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5606
- **创建时间**: 2026-01-05T08:05:49Z
- **关闭时间**: 2026-01-07T01:34:31Z
- **更新时间**: 2026-01-07T13:02:38Z
- **提交者**: @kruskr
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

PyTorch version: 2.8.0+cpu
Is debug build: False

OS: openEuler 24.03 (LTS-SP2) (aarch64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-98.oe2403sp2)
Clang version: Could not collect
CMake version: version 4.2.0
Libc version: glibc-2.38

Python version: 3.11.13 (main, Nov 20 2025, 16:04:22) [GCC 12.3.1 (openEuler 12.3.1-98.oe2403sp2)] (64-bit runtime)
Python platform: Linux-5.10.0-288.0.0.191.oe2203sp4.aarch64-aarch64-with-glibc2.38

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             96
On-line CPU(s) list:                0-95
Vendor ID:                          HiSilicon
Model name:                         Kunpeng-920
Model:                              0
Thread(s) per core:                 1
Core(s) per cluster:                48
Socket(s):                          -
Cluster(s):                         2
Stepping:                           0x1
Frequency boost:                    disabled
CPU(s) scaling MHz:                 100%
CPU max MHz:                        2600.0000
CPU min MHz:                        200.0000
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                          6 MiB (96 instances)
L1i cache:                          6 MiB (96 instances)
L2 cache:                           48 MiB (96 instances)
L3 cache:                           96 MiB (4 instances)
NUMA node(s):                       4
NUMA node0 CPU(s):                  0-23
NUMA node1 CPU(s):                  24-47
NUMA node2 CPU(s):                  48-71
NUMA node3 CPU(s):                  72-95
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
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.12.0
vLLM Ascend Version: 0.12.0rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 25.2.2                   Version: 25.2.2                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B4-1             | OK            | 78.2        40                0    / 0             |
| 0                         | 0000:0E:00.0  | 0           0    / 0          61825/ 65536         |
+===========================+===============+====================================================+
| 1     910B4-1             | OK            | 77.9        41                0    / 0             |
| 0                         | 0000:0F:00.0  | 0           0    / 0          61825/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 19334         | VLLMWorker_TP            | 58472                   |
+===========================+===============+====================================================+
| 1       0                 | 19341         | VLLMWorker_TP            | 58472                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/aarch64-linux


### 🐛 Describe the bug

It was successfully deployed the Qwen3-Next-80B-A3B-Instruct-W8A8(downloaded from https://modelscope.cn/models/vllm-ascend/Qwen3-Next-80B-A3B-Instruct-W8A8/files ) using vLLM, the full command llike below:
vllm  serve vllm serve 
	--model /data/xinference/Qwen3-Next-80B-A3B-Instruct-W8A8 
	--served-model-name Qwen3-Next
	--tensor-parallel-size 2 
	--max-num-seqs 4 
	--max-model-len 128 
	--compilation_config '{"cudagraph_capture_sizes":[1,4,8,20]}' 
	--quantization ascend 
	--gpu-memory-utilization 0.8
 when  called the api like that “curl http://localhost:1064/v1/chat/completions  -H "Content-Type: application/json" -d '{ "model": "Qwen3-Next","messages": [ {"role": "user", "content": "hello,tell me joke about joker"} ],"max_tokens": 100}”，the returns alway be "!!!!!!!!!!!!!!!!!!!!!!!!", namely that "{"id":"chatcmpl-9cec3068eb76ac3b","object":"chat.completion","created":1767600136,"model":"Qwen3-Next","choices":[{"index":0,"message":{"role":"assistant","content":"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!","refusal":null,"annotations":null,"audio":null,"function_call":null,"tool_calls":[],"reasoning":null,"reasoning_content":null},"logprobs":null,"finish_reason":"length","stop_reason":null,"token_ids":null}],"service_tier":null,"system_fingerprint":null,"usage":{"prompt_tokens":16,"total_tokens":116,"completion_tokens":100,"prompt_tokens_details":null},"prompt_logprobs":null,"prompt_token_ids":null,"kv_transfer_params":null}"
is that a bug or something wrong in the command?
