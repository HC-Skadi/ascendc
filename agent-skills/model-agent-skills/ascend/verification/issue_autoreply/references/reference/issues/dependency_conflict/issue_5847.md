# Issue #5847: [Bug]: v0.13.0.rc1 推理存在cpu内存泄漏

## 基本信息

- **编号**: #5847
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5847
- **创建时间**: 2026-01-13T07:30:54Z
- **关闭时间**: 2026-01-14T08:29:02Z
- **更新时间**: 2026-01-14T08:29:02Z
- **提交者**: @glowwormX
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.8.0+cpu
Is debug build: False

OS: Huawei Cloud EulerOS 2.0 (aarch64) (aarch64)
GCC version: (conda-forge gcc 13.1.0-0) 13.1.0
Clang version: Could not collect
CMake version: version 4.2.1
Libc version: glibc-2.34

Python version: 3.10.18 | packaged by conda-forge | (main, Jun  4 2025, 14:39:45) [GCC 13.3.0] (64-bit runtime)
Python platform: Linux-4.19.90-vhulk2211.3.0.h1543.eulerosv2r10.aarch64-aarch64-with-glibc2.34

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       HiSilicon
Model name:                      Kunpeng-920
Model:                           0
Thread(s) per core:              1
Core(s) per cluster:             48
Socket(s):                       -
Cluster(s):                      4
Stepping:                        0x1
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       12 MiB (192 instances)
L1i cache:                       12 MiB (192 instances)
L2 cache:                        96 MiB (192 instances)
L3 cache:                        192 MiB (8 instances)
NUMA node(s):                    8
NUMA node0 CPU(s):               0-23
NUMA node1 CPU(s):               24-47
NUMA node2 CPU(s):               48-71
NUMA node3 CPU(s):               72-95
NUMA node4 CPU(s):               96-119
NUMA node5 CPU(s):               120-143
NUMA node6 CPU(s):               144-167
NUMA node7 CPU(s):               168-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Mmio stale data:   Not affected
Vulnerability Retbleed:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] gpytorch==1.14.2
[pip3] numpy==1.26.4
[pip3] pyzmq==27.0.1
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0
[pip3] torchaudio==2.7.0
[pip3] torchdata==0.11.0
[pip3] torchprofile==0.0.4
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.3
[conda] gpytorch                                    1.14.2             pypi_0                pypi
[conda] numpy                                       1.26.4             py310hcbab775_0       conda-forge
[conda] pyzmq                                       27.0.1             pypi_0                pypi
[conda] torch                                       2.8.0+cpu          pypi_0                pypi
[conda] torch-npu                                   2.8.0              pypi_0                pypi
[conda] torchaudio                                  2.7.0              pypi_0                pypi
[conda] torchdata                                   0.11.0             pypi_0                pypi
[conda] torchprofile                                0.0.4              pypi_0                pypi
[conda] torchvision                                 0.23.0             pypi_0                pypi
[conda] transformers                                4.57.3             pypi_0                pypi
vLLM Version: 0.13.0
vLLM Ascend Version: 0.13.0rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=2,3,0,1
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/home/ma-user/work/dataset/openLLM_guian_obs/env_config/cann8.3.rc2/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/home/ma-user/work/dataset/openLLM_guian_obs/env_config/cann8.3.rc2/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/home/ma-user/work/dataset/openLLM_guian_obs/env_config/cann8.3.rc2/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/home/ma-user/work/dataset/openLLM_guian_obs/env_config/cann8.3.rc2/nnal/atb/latest/atb/cxx_abi_0/lib:/home/ma-user/work/dataset/openLLM_guian_obs/env_config/cann8.3.rc2/nnal/atb/latest/atb/cxx_abi_0/examples:/home/ma-user/work/dataset/openLLM_guian_obs/env_config/cann8.3.rc2/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/home/ma-user/work/dataset/openLLM_guian_obs/env_config/cann8.3.rc2/ascend-toolkit/latest/tools/aml/lib64:/home/ma-user/work/dataset/openLLM_guian_obs/env_config/cann8.3.rc2/ascend-toolkit/latest/tools/aml/lib64/plugin:/home/ma-user/work/dataset/openLLM_guian_obs/env_config/cann8.3.rc2/ascend-toolkit/latest/lib64:/home/ma-user/work/dataset/openLLM_guian_obs/env_config/cann8.3.rc2/ascend-toolkit/latest/lib64/plugin/opskernel:/home/ma-user/work/dataset/openLLM_guian_obs/env_config/cann8.3.rc2/ascend-toolkit/latest/lib64/plugin/nnengine:/home/ma-user/work/dataset/openLLM_guian_obs/env_config/cann8.3.rc2/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/toolbox/latest/Ascend-DMI/lib64:/usr/lib/aarch64-linux-gnu/hdf5/serial:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/:/usr/local/seccomponent/lib/:/usr/local/seccomponent/lib/openssl/:/usr/local/mindspore-lite/mindspore-lite-2.3.0-linux-aarch64/tools/converter/lib:/usr/local/mindspore-lite/mindspore-lite-2.3.0-linux-aarch64/runtime/lib:/usr/local/mindspore-lite/mindspore-lite-2.3.0-linux-aarch64/runtime/third_party/dnnl:/usr/lib64:/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib
ASCEND_AICPU_PATH=/home/ma-user/work/dataset/openLLM_guian_obs/env_config/cann8.3.rc2/ascend-toolkit/latest
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/home/ma-user/work/dataset/openLLM_guian_obs/env_config/cann8.3.rc2/ascend-toolkit/latest
ASCEND_AUTOML_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools
ATB_MATMUL_SHUFFLE_K_ENABLE=1
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
| 0     910B4               | OK            | 152.0       49                0    / 0             |
| 0                         | 0000:C1:00.0  | 67          0    / 0          30237/ 32768         |
+===========================+===============+====================================================+
| 1     910B4               | OK            | 162.7       50                0    / 0             |
| 0                         | 0000:01:00.0  | 67          0    / 0          29980/ 32768         |
+===========================+===============+====================================================+
| 2     910B4               | OK            | 156.2       51                0    / 0             |
| 0                         | 0000:C2:00.0  | 67          0    / 0          29977/ 32768         |
+===========================+===============+====================================================+
| 3     910B4               | OK            | 159.8       51                0    / 0             |
| 0                         | 0000:02:00.0  | 68          0    / 0          29986/ 32768         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 2385579       | VLLMWorker_TP            | 134                     |
| 0       0                 | 2385580       | VLLMWorker_TP            | 134                     |
| 0       0                 | 2385581       | VLLMWorker_TP            | 134                     |
| 0       0                 | 2385578       | VLLMWorker_TP            | 27170                   |
+===========================+===============+====================================================+
| 1       0                 | 2385579       | VLLMWorker_TP            | 27160                   |
+===========================+===============+====================================================+
| 2       0                 | 2385580       | VLLMWorker_TP            | 27160                   |
+===========================+===============+====================================================+
| 3       0                 | 2385581       | VLLMWorker_TP            | 27160                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.0.T13
innerversion=V100R001C18B521
compatible_version=[V100R001C15,V100R001C18],[V100R001C30],[V100R001C13],[V100R003C11],[V100R001C29],[V100R001C10]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.T13/aarch64-linux
```

</details>


### 🐛 Describe the bug

verl切换到vllm-v0.13.0后发现训练因cpu内存不足停止，之前v0.11.0是正常的 [相关verl-issues](https://github.com/volcengine/verl/issues/4200#issuecomment-3693842576)

后续单独用vllm-ascend测试后发现依然有内存泄漏情况

服务端：
```
pkill -f -9 'VLLM'

source /home/ma-user/work/dataset/openLLM_guian_obs/env_config/cann8.3.rc2/ascend-toolkit/set_env.sh
source /home/ma-user/work/dataset/openLLM_guian_obs/env_config/cann8.3.rc2/nnal/atb/set_env.sh
source /cache/verl_1118_env_main_py310_vllm_v13_rc1/bin/activate
set -x
pip list|grep vllm
pip list|grep torch
python -c "import platform, torch, torch_npu, transformers; print('Python:', platform.python_version()); print('PyTorch:', torch.__version__); print('PyTorch_npu:', torch_npu.__version__) ; print('CANN:', torch.version.cann); print('transformers:', transformers.__version__)"

export VLLM_ASCEND_ENABLE_NZ=0
export VLLM_USE_V1=1

vllm serve /home/ma-user/work/dataset/openLLM_guian/Qwen3/Qwen3-32B --max_model_len 32768 --max_num_seqs 64 --gpu_memory_utilization 0.9 --tensor_parallel_size 4 --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "cudagraph_capture_sizes": [128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1]}'
```

客户端脚本：
```
#!/bin/bash

API_URL="http://localhost:8000/v1/completions"

MODEL_NAME="/home/ma-user/work/dataset/openLLM_guian/Qwen3/Qwen3-32B"

CONCURRENCY=64

REPEAT_COUNT=100

PAYLOAD="{\"model\": \"${MODEL_NAME}\", \"prompt\": \"San Francisco is a\", \"max_tokens\": 6400, \"temperature\": 0}"

free -h
echo "开始测试：并发数 ${CONCURRENCY}, 重复 ${REPEAT_COUNT} 次"
echo "------------------------------------------------------"

for (( i=1; i<=REPEAT_COUNT; i++ ))
do
    echo "[Batch $i/$REPEAT_COUNT] 发送 $CONCURRENCY 个请求..."
    
    start_time=$(date +%s.%N)

    for (( j=1; j<=CONCURRENCY; j++ ))
    do
        curl -s -X POST "${API_URL}" \
             -H "Content-Type: application/json" \
             -d "${PAYLOAD}" \
             > /dev/null &
    done

    wait

    end_time=$(date +%s.%N)
    duration=$(awk -v start="$start_time" -v end="$end_time" 'BEGIN {print end - start}')
    
    echo "批次 $i 完成，耗时: ${duration}秒. 当前内存情况:"
    
    free -h
    
    echo "------------------------------------------------------"
done

echo "所有测试完成。"


```

客户端输出：
```
               total        used        free      shared  buff/cache   available
Mem:           1.5Ti        33Gi       1.4Ti       123Mi       4.4Gi       1.4Ti
Swap:             0B          0B          0B
开始测试：并发数 64, 重复 100 次
------------------------------------------------------
[Batch 1/100] 发送 64 个请求...
批次 1 完成，耗时: 466.059秒. 当前内存情况:
               total        used        free      shared  buff/cache   available
Mem:           1.5Ti        35Gi       1.4Ti       123Mi       3.7Gi       1.4Ti
Swap:             0B          0B          0B
------------------------------------------------------
[Batch 2/100] 发送 64 个请求...
批次 2 完成，耗时: 404.206秒. 当前内存情况:
               total        used        free      shared  buff/cache   available
Mem:           1.5Ti        37Gi       1.4Ti       118Mi       4.5Gi       1.4Ti
Swap:             0B          0B          0B
------------------------------------------------------
[Batch 3/100] 发送 64 个请求...
批次 3 完成，耗时: 496.972秒. 当前内存情况:
               total        used        free      shared  buff/cache   available
Mem:           1.5Ti        39Gi       1.3Ti       118Mi       103Gi       1.4Ti
Swap:             0B          0B          0B
------------------------------------------------------
[Batch 4/100] 发送 64 个请求...
批次 4 完成，耗时: 437.555秒. 当前内存情况:
               total        used        free      shared  buff/cache   available
Mem:           1.5Ti        41Gi       1.4Ti       118Mi       5.0Gi       1.4Ti
Swap:             0B          0B          0B
------------------------------------------------------
[Batch 5/100] 发送 64 个请求...
批次 5 完成，耗时: 437.584秒. 当前内存情况:
               total        used        free      shared  buff/cache   available
Mem:           1.5Ti        43Gi       1.4Ti       118Mi       3.4Gi       1.4Ti
Swap:             0B          0B          0B
------------------------------------------------------
[Batch 6/100] 发送 64 个请求...
批次 6 完成，耗时: 404.522秒. 当前内存情况:
               total        used        free      shared  buff/cache   available
Mem:           1.5Ti        44Gi       1.4Ti       118Mi       3.9Gi       1.4Ti
Swap:             0B          0B          0B
------------------------------------------------------
[Batch 7/100] 发送 64 个请求...
批次 7 完成，耗时: 477.947秒. 当前内存情况:
               total        used        free      shared  buff/cache   available
Mem:           1.5Ti        47Gi       1.4Ti       118Mi        22Gi       1.4Ti
Swap:             0B          0B          0B
------------------------------------------------------
[Batch 8/100] 发送 64 个请求...
批次 8 完成，耗时: 468.062秒. 当前内存情况:
               total        used        free      shared  buff/cache   available
Mem:           1.5Ti        60Gi       1.4Ti       118Mi       8.8Gi       1.4Ti
Swap:             0B          0B          0B
------------------------------------------------------
[Batch 9/100] 发送 64 个请求...
批次 9 完成，耗时: 437.082秒. 当前内存情况:
               total        used        free      shared  buff/cache   available
Mem:           1.5Ti        83Gi       1.4Ti       123Mi       8.8Gi       1.4Ti
Swap:             0B          0B          0B
------------------------------------------------------

....

[Batch 94/100] 发送 64 个请求...
批次 94 完成，耗时: 404.676秒. 当前内存情况:
               total        used        free      shared  buff/cache   available
Mem:           1.5Ti       238Gi       1.2Ti       123Mi       3.9Gi       1.2Ti
Swap:             0B          0B          0B
------------------------------------------------------
[Batch 95/100] 发送 64 个请求...
批次 95 完成，耗时: 376.537秒. 当前内存情况:
               total        used        free      shared  buff/cache   available
Mem:           1.5Ti       240Gi       1.2Ti       123Mi       3.8Gi       1.2Ti
Swap:             0B          0B          0B
------------------------------------------------------
[Batch 96/100] 发送 64 个请求...
批次 96 完成，耗时: 469.251秒. 当前内存情况:
               total        used        free      shared  buff/cache   available
Mem:           1.5Ti       242Gi       1.2Ti       123Mi       3.9Gi       1.2Ti
Swap:             0B          0B          0B
------------------------------------------------------
[Batch 97/100] 发送 64 个请求...
批次 97 完成，耗时: 364.381秒. 当前内存情况:
               total        used        free      shared  buff/cache   available
Mem:           1.5Ti       243Gi       1.2Ti       118Mi       3.9Gi       1.2Ti
Swap:             0B          0B          0B
------------------------------------------------------
[Batch 98/100] 发送 64 个请求...
批次 98 完成，耗时: 473.237秒. 当前内存情况:
               total        used        free      shared  buff/cache   available
Mem:           1.5Ti       245Gi       1.2Ti       118Mi       3.9Gi       1.2Ti
Swap:             0B          0B          0B
------------------------------------------------------
[Batch 99/100] 发送 64 个请求...
批次 99 完成，耗时: 464.302秒. 当前内存情况:
               total        used        free      shared  buff/cache   available
Mem:           1.5Ti       247Gi       1.2Ti       118Mi       3.3Gi       1.2Ti
Swap:             0B          0B          0B
------------------------------------------------------
[Batch 100/100] 发送 64 个请求...
批次 100 完成，耗时: 438.149秒. 当前内存情况:
               total        used        free      shared  buff/cache   available
Mem:           1.5Ti       249Gi       1.2Ti       118Mi       3.9Gi       1.2Ti
Swap:             0B          0B          0B
------------------------------------------------------
所有测试完成。
```
可以看到used会逐渐升高

从top中看进程使用的内存，也从最开始的4.7g升到48.8g
```
    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                                                                                         
2385581 ma-user   25   5 8203.7g   4.7g 702212 R 112.9   0.3  41:41.10 VLLM::Worker_TP                 
```  

```
    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                                                                                         
2385579 ma-user   25   5 8247.8g  48.8g 705748 R 105.9   3.2   1573:49 VLLM::Worker_TP                                                                                 
2385580 ma-user   25   5 8247.8g  48.8g 701616 R 105.0   3.2   1572:16 VLLM::Worker_TP                                                                                 
2385581 ma-user   25   5 8247.8g  48.8g 702380 R 105.0   3.2   1574:56 VLLM::Worker_TP                                                                                 
2385578 ma-user   25   5 8247.5g  48.8g 699560 R 102.0   3.2   1534:09 VLLM::Worker_TP 
```
