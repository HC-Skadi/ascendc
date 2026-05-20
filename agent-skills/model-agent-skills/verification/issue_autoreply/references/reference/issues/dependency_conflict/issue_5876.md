# Issue #5876: [Bug]: 双机推理Qwen3-235B模型，启动时卡在Capturing CUDA graphs进度0%，卡住一小时了。

## 基本信息

- **编号**: #5876
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5876
- **创建时间**: 2026-01-14T02:51:09Z
- **关闭时间**: 2026-01-29T07:43:48Z
- **更新时间**: 2026-01-29T07:43:48Z
- **提交者**: @MaoJianwei
- **评论数**: 5

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

OS: openEuler 24.03 (LTS-SP2) (aarch64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-98.oe2403sp2)
Clang version: Could not collect
CMake version: version 4.2.1
Libc version: glibc-2.38

Python version: 3.11.13 (main, Nov 20 2025, 16:04:22) [GCC 12.3.1 (openEuler 12.3.1-98.oe2403sp2)] (64-bit runtime)
Python platform: Linux-6.6.0-28.0.0.34.oe2403.aarch64-aarch64-with-glibc2.38

CPU:
Architecture:                         aarch64
CPU op-mode(s):                       64-bit
Byte Order:                           Little Endian
CPU(s):                               192
On-line CPU(s) list:                  0-191
Vendor ID:                            HiSilicon
BIOS Vendor ID:                       HiSilicon
Model name:                           Kunpeng-920
BIOS Model name:                      HUAWEI Kunpeng 920 5250 To be filled by O.E.M. CPU @ 2.6GHz
BIOS CPU family:                      280
Model:                                0
Thread(s) per core:                   1
Core(s) per socket:                   48
Socket(s):                            4
Stepping:                             0x1
BogoMIPS:                             200.00
Flags:                                fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                            12 MiB (192 instances)
L1i cache:                            12 MiB (192 instances)
L2 cache:                             96 MiB (192 instances)
L3 cache:                             192 MiB (8 instances)
NUMA node(s):                         8
NUMA node0 CPU(s):                    0-23
NUMA node1 CPU(s):                    24-47
NUMA node2 CPU(s):                    48-71
NUMA node3 CPU(s):                    72-95
NUMA node4 CPU(s):                    96-119
NUMA node5 CPU(s):                    120-143
NUMA node6 CPU(s):                    144-167
NUMA node7 CPU(s):                    168-191
Vulnerability Gather data sampling:   Not affected
Vulnerability Itlb multihit:          Not affected
Vulnerability L1tf:                   Not affected
Vulnerability Mds:                    Not affected
Vulnerability Meltdown:               Not affected
Vulnerability Mmio stale data:        Not affected
Vulnerability Reg file data sampling: Not affected
Vulnerability Retbleed:               Not affected
Vulnerability Spec rstack overflow:   Not affected
Vulnerability Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:             Mitigation; __user pointer sanitization
Vulnerability Spectre v2:             Not affected
Vulnerability Srbds:                  Not affected
Vulnerability Tsx async abort:        Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.3
[conda] Could not collect
vLLM Version: 0.13.0
vLLM Ascend Version: 0.13.0rc2.dev15+g45c3c279e (git sha: 45c3c279e)

ENV Variables:
ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_COMPARE_TILING_EVERY_KERNEL=0
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_SHARE_MEMORY_NAME_SUFFIX=
ATB_MATMUL_SHUFFLE_K_ENABLE=1
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 25.3.rc1                 Version: 25.3.rc1                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 100.9       40                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          58626/ 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 96.2        39                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          58626/ 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 90.5        39                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          58627/ 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 97.7        39                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          58626/ 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 93.6        44                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          58626/ 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 97.0        43                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          58626/ 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 100.0       42                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          58626/ 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 93.5        42                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          58626/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 71867         |                          | 55278                   |
+===========================+===============+====================================================+
| 1       0                 | 71868         |                          | 55278                   |
+===========================+===============+====================================================+
| 2       0                 | 71869         |                          | 55278                   |
+===========================+===============+====================================================+
| 3       0                 | 71870         |                          | 55278                   |
+===========================+===============+====================================================+
| 4       0                 | 71871         |                          | 55278                   |
+===========================+===============+====================================================+
| 5       0                 | 71872         |                          | 55278                   |
+===========================+===============+====================================================+
| 6       0                 | 71873         |                          | 55278                   |
+===========================+===============+====================================================+
| 7       0                 | 71874         |                          | 55278                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/aarch64-linux

```

</details>


### 🐛 Describe the bug

两台A2服务器，每台910B3 NPU 8卡。
使用v0.13.0rc1-openeuler镜像，部署Qwen3-235B模型的双机 **TP16+EP** 推理，
启动时卡在“Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):   0%”，进度0%，卡住一小时了。


vllm输出：
```
(Worker_TP0_EP0 pid=48) INFO 01-14 01:49:24 [backends.py:278] Compiling a graph for compile range (1, 4096) takes 55.98 s
(Worker_TP2_EP2 pid=50) INFO 01-14 01:49:36 [worker.py:287] Available memory: 25084186112, total memory: 65452113920
(Worker_TP4_EP4 pid=52) INFO 01-14 01:49:36 [worker.py:287] Available memory: 25084329472, total memory: 65452113920
(Worker_TP1_EP1 pid=49) INFO 01-14 01:49:36 [worker.py:287] Available memory: 25086021120, total memory: 65452113920
(Worker_TP0_EP0 pid=48) INFO 01-14 01:49:36 [worker.py:287] Available memory: 25084038656, total memory: 65452113920
(Worker_TP5_EP5 pid=53) INFO 01-14 01:49:36 [worker.py:287] Available memory: 25086684672, total memory: 65452113920
(Worker_TP6_EP6 pid=54) INFO 01-14 01:49:36 [worker.py:287] Available memory: 25083870720, total memory: 65452113920
(Worker_TP3_EP3 pid=51) INFO 01-14 01:49:36 [worker.py:287] Available memory: 25086332416, total memory: 65452113920
(Worker_TP7_EP7 pid=55) INFO 01-14 01:49:36 [worker.py:287] Available memory: 25086332416, total memory: 65452113920
(EngineCore_DP0 pid=38) INFO 01-14 01:49:37 [kv_cache_utils.py:1291] GPU KV cache size: 521,088 tokens
(EngineCore_DP0 pid=38) INFO 01-14 01:49:37 [kv_cache_utils.py:1296] Maximum concurrency for 32,768 tokens per request: 15.90x
Capturing CUDA graphs (mixed prefill-decode, PIECEWISE):   0%|                                                             | 0/6 [00:00<?, ?it/s](EngineCore_DP0 pid=38) INFO 01-14 01:50:37 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically
 happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP0 pid=38) INFO 01-14 01:51:37 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically
 happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP0 pid=38) INFO 01-14 01:52:37 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically
 happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP0 pid=38) INFO 01-14 01:53:37 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically
 happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).
(EngineCore_DP0 pid=38) INFO 01-14 01:54:37 [shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically
 happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization).

后续周期性重复输出No available shared memory broadcast block found in 60 seconds. ...
```

.

VLLM相关进程一直在占用CPU 69~100%，但启动过程没有进展。
```
MiB Mem : 2062816.+total, 1418251.+free,  42258.3 used, 610907.9 buff/cache
MiB Swap:   4096.0 total,   4095.5 free,      0.5 used. 2020558.+avail Mem

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
  71852 root      20   0 4056100   1.2g 315176 R  99.0   0.1  62:28.45 VLLM::EngineCor
  71870 root      20   0 8200.3g   2.8g 564268 S  77.1   0.1  50:41.60 VLLM::Worker_TP
  71872 root      20   0 8200.3g   2.8g 565144 S  75.2   0.1  52:35.65 VLLM::Worker_TP
  71873 root      20   0 8200.3g   2.8g 550812 S  72.4   0.1  51:47.46 VLLM::Worker_TP
  71874 root      20   0 8200.3g   2.8g 554036 S  70.5   0.1  51:14.78 VLLM::Worker_TP
  71871 root      20   0 8200.3g   2.8g 555076 S  69.5   0.1  51:37.73 VLLM::Worker_TP
  71869 root      20   0 8200.3g   2.8g 567512 S  68.6   0.1  51:22.53 VLLM::Worker_TP
  71867 root      20   0 8200.6g   2.8g 559004 S  67.6   0.1  50:22.48 VLLM::Worker_TP
  71868 root      20   0 8200.3g   2.8g 560932 S  67.6   0.1  49:12.86 VLLM::Worker_TP
 155274 m005227+  20   0   29468   7880   3336 R   3.8   0.0   0:00.31 top
     16 root      20   0       0      0      0 I   1.0   0.0   0:09.82 rcu_sched
```

