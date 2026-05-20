# Issue #628: [Bug]: deepseek-v2-lite-w8a8 quantizaion inference repeated output

## 基本信息

- **编号**: #628
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/628
- **创建时间**: 2025-04-23T06:37:34Z
- **关闭时间**: 2025-05-14T05:59:32Z
- **更新时间**: 2025-05-16T14:30:19Z
- **提交者**: @Potabk
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
INFO 04-23 06:24:43 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 04-23 06:24:43 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 04-23 06:24:43 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 04-23 06:24:43 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 04-23 06:24:43 [__init__.py:44] plugin ascend loaded.
INFO 04-23 06:24:43 [__init__.py:230] Platform plugin ascend is activated
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.0
Libc version: glibc-2.35

Python version: 3.10.15 (main, Nov 27 2024, 06:51:55) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-vhulk2211.3.0.h1960.eulerosv2r10.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Vendor ID:                          HiSilicon
Model name:                         Kunpeng-920
Model:                              0
Thread(s) per core:                 1
Core(s) per cluster:                48
Socket(s):                          -
Cluster(s):                         4
Stepping:                           0x1
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                          12 MiB (192 instances)
L1i cache:                          12 MiB (192 instances)
L2 cache:                           96 MiB (192 instances)
L3 cache:                           192 MiB (8 instances)
NUMA node(s):                       8
NUMA node0 CPU(s):                  0-23
NUMA node1 CPU(s):                  24-47
NUMA node2 CPU(s):                  48-71
NUMA node3 CPU(s):                  72-95
NUMA node4 CPU(s):                  96-119
NUMA node5 CPU(s):                  120-143
NUMA node6 CPU(s):                  144-167
NUMA node7 CPU(s):                  168-191
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.3.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250320
[pip3] torchvision==0.20.1
[pip3] transformers==4.51.3
[conda] Could not collect
vLLM Version: 0.8.4
vLLM Ascend Version: 0.1.dev159+g66a0837 (git sha: 66a0837)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc3                 Version: 24.1.rc3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B4               | OK            | 90.8        39                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          29070/ 32768         |
+===========================+===============+====================================================+
| 1     910B4               | OK            | 86.7        40                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          2824 / 32768         |
+===========================+===============+====================================================+
| 3     910B4               | OK            | 92.4        39                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          2834 / 32768         |
+===========================+===============+====================================================+
| 4     910B4               | OK            | 82.6        40                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          2826 / 32768         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 5063          | python3.10               | 26293                   |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux
```

</details>


### 🐛 Describe the bug

I'm using deekseek-v2-lite w8a8 quantization feature, and i encountered an unexpected bug:
The model is quantized following to the https://github.com/vllm-project/vllm-ascend/pull/580#issuecomment-2816747613，
serving command:
```
vllm serve dspk-fully-quant-w8a8 --max-model-len 4096  -tp 1 --trust-remote-code
```
and the server setup normally:
```
INFO 04-23 06:20:25 [api_server.py:1081] Starting vLLM API server on http://0.0.0.0:8000
INFO 04-23 06:20:25 [launcher.py:26] Available routes are:
INFO 04-23 06:20:25 [launcher.py:34] Route: /openapi.json, Methods: GET, HEAD
INFO 04-23 06:20:25 [launcher.py:34] Route: /docs, Methods: GET, HEAD
INFO 04-23 06:20:25 [launcher.py:34] Route: /docs/oauth2-redirect, Methods: GET, HEAD
INFO 04-23 06:20:25 [launcher.py:34] Route: /redoc, Methods: GET, HEAD
INFO 04-23 06:20:25 [launcher.py:34] Route: /health, Methods: GET
INFO 04-23 06:20:25 [launcher.py:34] Route: /load, Methods: GET
INFO 04-23 06:20:25 [launcher.py:34] Route: /ping, Methods: GET, POST
INFO 04-23 06:20:25 [launcher.py:34] Route: /tokenize, Methods: POST
INFO 04-23 06:20:25 [launcher.py:34] Route: /detokenize, Methods: POST
INFO 04-23 06:20:25 [launcher.py:34] Route: /v1/models, Methods: GET
INFO 04-23 06:20:25 [launcher.py:34] Route: /version, Methods: GET
INFO 04-23 06:20:25 [launcher.py:34] Route: /v1/chat/completions, Methods: POST
INFO 04-23 06:20:25 [launcher.py:34] Route: /v1/completions, Methods: POST
INFO 04-23 06:20:25 [launcher.py:34] Route: /v1/embeddings, Methods: POST
INFO 04-23 06:20:25 [launcher.py:34] Route: /pooling, Methods: POST
INFO 04-23 06:20:25 [launcher.py:34] Route: /score, Methods: POST
INFO 04-23 06:20:25 [launcher.py:34] Route: /v1/score, Methods: POST
INFO 04-23 06:20:25 [launcher.py:34] Route: /v1/audio/transcriptions, Methods: POST
INFO 04-23 06:20:25 [launcher.py:34] Route: /rerank, Methods: POST
INFO 04-23 06:20:25 [launcher.py:34] Route: /v1/rerank, Methods: POST
INFO 04-23 06:20:25 [launcher.py:34] Route: /v2/rerank, Methods: POST
INFO 04-23 06:20:25 [launcher.py:34] Route: /invocations, Methods: POST
INFO 04-23 06:20:25 [launcher.py:34] Route: /metrics, Methods: GET
INFO:     Started server process [4918]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
the client input:
```
curl http://localhost:8000/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "dspk-fully-quant-w8a8",
        "prompt": "deepseek是什么？",
        "max_tokens": "128",
        "top_p": "0.95",
        "top_k": "40",
        "temperature": "0.0"
    }'
```
but the output is strange：
```
{"id":"cmpl-0797e36c26c5492ea68c93a0d97fc478","object":"text_completion","created":1745389315,"model":"dspk-fully-quant-w8a8","choices":[{"index":0,"text":"\n\n\n20132012111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","logprobs":null,"finish_reason":"length","stop_reason":null,"prompt_logprobs":null}],"usage":{"prompt_tokens":5,"total_tokens":133,"completion_tokens":128,"prompt_tokens_details":null}}
```
