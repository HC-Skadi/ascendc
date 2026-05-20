# Issue #1427: [Bug]: [0.7.3rc1] vlm inference based on vllm-ascend performance abnormal, inferring speed is slower than original transformers

## 基本信息

- **编号**: #1427
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1427
- **创建时间**: 2025-06-25T08:49:40Z
- **关闭时间**: 2025-07-11T15:33:56Z
- **更新时间**: 2025-07-11T15:33:56Z
- **提交者**: @magemoumou
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Huawei Cloud EulerOS 2.0 (aarch64) (aarch64)
GCC version: Could not collect
Clang version: Could not collect
CMake version: version 3.22.0
Libc version: glibc-2.34

Python version: 3.11.5 (main, Sep 11 2023, 13:14:08) [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-5.10.0-60.18.0.50.r865_35.hce2.aarch64-aarch64-with-glibc2.34

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
[pip3] numpy==1.26.4
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torchaudio==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.52.4
[pip3] transformers-stream-generator==0.0.5
[conda] numpy                     1.26.4                   pypi_0    pypi
[conda] pyzmq                     26.4.0                   pypi_0    pypi
[conda] torch                     2.5.1                    pypi_0    pypi
[conda] torch-npu                 2.5.1                    pypi_0    pypi
[conda] torchaudio                2.5.1                    pypi_0    pypi
[conda] torchvision               0.20.1                   pypi_0    pypi
[conda] transformers              4.52.4                   pypi_0    pypi
[conda] transformers-stream-generator 0.0.5                    pypi_0    pypi
vLLM Version: 0.7.3
vLLM Ascend Version: 0.7.3rc1

ENV Variables:
ASCEND_VISIBLE_DEVICES=3,6
ASCEND_RUNTIME_OPTIONS=
TORCH_PLUGIN_PKG=/usr/local/Ascend/latest/tools/ms_fmk_transplt/torch_npu_bridge
ASCEND_OPP_PATH=/usr/local/Ascend/latest/opp
LD_LIBRARY_PATH=:/usr/local/Ascend/latest/lib64/plugin/nnengine:/usr/local/Ascend/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/latest/lib64:/usr/local/Ascend/latest/lib64/plugin/opskernel:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/usr/local/cuda/compat:/usr/local/cuda/lib64/:/opt/huawei/miniconda3/lib/python3.11/site-packages/torch/lib:/opt/huawei/miniconda3/lib/python3.11/site-packages/torch_npu/lib
ASCEND_AICPU_PATH=/usr/local/Ascend/latest
ASCEND_HOME_PATH=/usr/local/Ascend/latest
TORCH_DEVICE_BACKEND_AUTOLOAD=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc3                 Version: 24.1.rc3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 3     910B4               | OK            | 87.1        48                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3034 / 32768         |
+===========================+===============+====================================================+
| 6     910B4               | OK            | 90.6        45                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          2912 / 32768         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 3       0                 | 14414         | python                   | 113                     |
| 3       0                 | 14247         | vllm                     | 115                     |
| 3       0                 | 14413         | python                   | 113                     |
+===========================+===============+====================================================+
| 6       0                 | 14412         | python                   | 115                     |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.1.T18
innerversion=V100R001C21SPC001B229
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.T18/aarch64-linux
```

</details>


### 🐛 Describe the bug

```python
**1）vllm online mode shell script is here:**
source /usr/local/Ascend/ascend-toolkit/set_env.sh
source /usr/local/Ascend/nnal/atb/set_env.sh
export PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
export MODEL_PATH=*/model
export DATA_DIR=*/pressure_test_dataset
echo "MODEL_PATH:${MODEL_PATH}"
echo "DATA_DIR:${DATA_DIR}"
**nohup vllm serve ${MODEL_PATH} --dtype bfloat16 --max-num-seqs 16 --max_model_len 32768 --gpu_memory_utilization 0.8 \
                               --kv-cache-dtype auto --enable-prefix-caching --multi-step-stream-outputs True \
                               --tensor-parallel-size 2 --pipeline-parallel-size 1 &**
```

```detail
**2）infer test performance**
according to a qwen25vl-3b，lantency is as following, which is even worse than transformers based inferring;
**2-1) when tps=1**,
2025-06-25 16:47:28,986 - INFO - 总请求数: 200
2025-06-25 16:47:28,987 - INFO - 成功: 200 (100.0%)
2025-06-25 16:47:28,987 - INFO - 失败: 0 (0.0%)
2025-06-25 16:47:28,987 - INFO - 总耗时: 135.42 秒
2025-06-25 16:47:28,987 - INFO - 平均吞吐量: 1.48 请求/秒
2025-06-25 16:47:28,987 - INFO -
请求耗时统计 (毫秒):
2025-06-25 16:47:28,987 - INFO - 最小值: 557.90
2025-06-25 16:47:28,987 - INFO - 最大值: 12780.27
2025-06-25 16:47:28,988 - INFO - 平均值: 677.03
2025-06-25 16:47:28,988 - INFO - 中位数: 608.28
2025-06-25 16:47:28,988 - INFO - 95百分位: 674.90
2025-06-25 16:47:28,989 - INFO - 99百分位: 862.35
**2-2) when tps=4**,
2025-06-25 16:03:54,356 - INFO - 总请求数: 200
2025-06-25 16:03:54,356 - INFO - 成功: 200 (100.0%)
2025-06-25 16:03:54,356 - INFO - 失败: 0 (0.0%)
2025-06-25 16:03:54,356 - INFO - 总耗时: 74.16 秒
2025-06-25 16:03:54,356 - INFO - 平均吞吐量: 2.70 请求/秒
2025-06-25 16:03:54,356 - INFO -
请求耗时统计 (毫秒):
2025-06-25 16:03:54,357 - INFO - 最小值: 1380.94
2025-06-25 16:03:54,357 - INFO - 最大值: 1596.06
2025-06-25 16:03:54,357 - INFO - 平均值: 1482.95
2025-06-25 16:03:54,357 - INFO - 中位数: 1500.68
2025-06-25 16:03:54,358 - INFO - 95百分位: 1551.34
2025-06-25 16:03:54,358 - INFO - 99百分位: 1593.44
’‘’
```
