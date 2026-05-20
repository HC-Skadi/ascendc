# Issue #4013: [Bug]: DeepSeek w8a8 OOM while loading weight with MoonCake

## 基本信息

- **编号**: #4013
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4013
- **创建时间**: 2025-11-05T13:52:25Z
- **关闭时间**: 2025-11-06T07:18:02Z
- **更新时间**: 2025-11-06T07:18:03Z
- **提交者**: @mitseng
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Debian GNU/Linux 12 (bookworm) (x86_64)
GCC version: (Debian 12.2.0-14+deb12u1) 12.2.0
Clang version: Could not collect
CMake version: version 4.1.2
Libc version: glibc-2.36

Python version: 3.11.9 (main, Dec 26 2024, 11:08:39) [GCC 12.2.0] (64-bit runtime)
Python platform: Linux-5.10.135.bsk.6-amd64-x86_64-with-glibc2.36

CPU:
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Address sizes:                   46 bits physical, 57 bits virtual
Byte Order:                      Little Endian
CPU(s):                          180
On-line CPU(s) list:             0-179
Vendor ID:                       GenuineIntel
Model name:                      Intel(R) Xeon(R) Platinum 8457C
CPU family:                      6
Model:                           143
Thread(s) per core:              2
Core(s) per socket:              45
Socket(s):                       2
Stepping:                        8
BogoMIPS:                        5199.90
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid pni pclmulqdq monitor ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch cpuid_fault invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves avx_vnni avx512_bf16 wbnoinvd arat avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid cldemote movdiri movdir64b fsrm md_clear serialize tsxldtrk arch_lbr amx_bf16 avx512_fp16 amx_tile amx_int8 arch_capabilities
Hypervisor vendor:               KVM
Virtualization type:             full
L1d cache:                       4.2 MiB (90 instances)
L1i cache:                       2.8 MiB (90 instances)
L2 cache:                        180 MiB (90 instances)
L3 cache:                        195 MiB (2 instances)
NUMA node(s):                    2
NUMA node0 CPU(s):               0-89
NUMA node1 CPU(s):               90-179
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Mmio stale data:   Not affected
Vulnerability Retbleed:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp
Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:        Mitigation; Enhanced IBRS, IBPB conditional, RSB filling
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Mitigation; TSX disabled

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1
[pip3] torchaudio==2.8.0+cpu
[pip3] torchvision==0.22.1+cpu
[pip3] transformers==4.57.1
[conda] Could not collect
vLLM Version: 0.11.0
vLLM Ascend Version: 0.11.0rc1.dev186+g66b67f9cf (git sha: 66b67f9cf)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=9,10,11,15,3,12,6,1,5,8,2,13,7,14,0,4
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_PROCESS_LOG_PATH=/var/log/tiger/ascend_diag_logs/run_0/process_log
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/mnt/bn/nas-assinfra-hl-03/work/Mooncake/build/mooncake-transfer-engine/src/:/usr/local/Ascend/ascend-toolkit/latest/python/site-packages:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/x86_64:/opt/tiger/native_libhdfs/lib/native:/opt/tiger/jdk/jdk8u265-b01/jre/lib/amd64/server:/opt/tiger/yarn_deploy/hadoop_current/lib/native:/opt/tiger/yarn_deploy/hadoop_current/lib/native/ufs:/opt/tiger/yarn_deploy/hadoop/lib/native:/opt/tiger/yarn_deploy/hadoop_current/lib/native:/opt/tiger/yarn_deploy/hadoop_current/lzo/lib:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver::/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/toolbox/latest/Ascend-DMI/lib64
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
| npu-smi 24.1.rc2                 Version: 24.1.rc2                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2C              | OK            | 450.6       78                0    / 0             |
| 0                         | 0000:75:01.0  | 100         0    / 0          54735/ 65536         |
+===========================+===============+====================================================+
| 1     910B2C              | OK            | 449.7       77                0    / 0             |
| 0                         | 0000:6F:01.0  | 100         0    / 0          54712/ 65536         |
+===========================+===============+====================================================+
| 2     910B2C              | OK            | 91.7        47                0    / 0             |
| 0                         | 0000:71:01.0  | 0           0    / 0          54715/ 65536         |
+===========================+===============+====================================================+
| 3     910B2C              | OK            | 96.1        49                0    / 0             |
| 0                         | 0000:6B:01.0  | 0           0    / 0          54712/ 65536         |
+===========================+===============+====================================================+
| 4     910B2C              | OK            | 450.1       75                0    / 0             |
| 0                         | 0000:69:01.0  | 100         0    / 0          54711/ 65536         |
+===========================+===============+====================================================+
| 5     910B2C              | OK            | 97.4        48                0    / 0             |
| 0                         | 0000:67:01.0  | 0           0    / 0          54712/ 65536         |
+===========================+===============+====================================================+
| 6     910B2C              | OK            | 449.8       75                0    / 0             |
| 0                         | 0000:65:01.0  | 100         0    / 0          54713/ 65536         |
+===========================+===============+====================================================+
| 7     910B2C              | OK            | 450.2       78                0    / 0             |
| 0                         | 0000:73:01.0  | 100         0    / 0          54711/ 65536         |
+===========================+===============+====================================================+
| 8     910B2C              | OK            | 96.5        47                0    / 0             |
| 0                         | 0000:75:02.0  | 0           0    / 0          54715/ 65536         |
+===========================+===============+====================================================+
| 9     910B2C              | OK            | 450.1       78                0    / 0             |
| 0                         | 0000:6F:02.0  | 100         0    / 0          54712/ 65536         |
+===========================+===============+====================================================+
| 10    910B2C              | OK            | 137.4       49                0    / 0             |
| 0                         | 0000:71:02.0  | 0           0    / 0          54710/ 65536         |
+===========================+===============+====================================================+
| 11    910B2C              | OK            | 109.4       49                0    / 0             |
| 0                         | 0000:6B:02.0  | 0           0    / 0          54709/ 65536         |
+===========================+===============+====================================================+
| 12    910B2C              | OK            | 104.6       48                0    / 0             |
| 0                         | 0000:69:02.0  | 0           0    / 0          54711/ 65536         |
+===========================+===============+====================================================+
| 13    910B2C              | OK            | 450.3       77                0    / 0             |
| 0                         | 0000:67:02.0  | 100         0    / 0          54710/ 65536         |
+===========================+===============+====================================================+
| 14    910B2C              | OK            | 109.6       45                0    / 0             |
| 0                         | 0000:65:02.0  | 0           0    / 0          54710/ 65536         |
+===========================+===============+====================================================+
| 15    910B2C              | OK            | 116.9       54                0    / 0             |
| 0                         | 0000:73:02.0  | 0           0    / 0          54710/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 265997        | python3                  | 51358                   |
+===========================+===============+====================================================+
| 1       0                 | 265997        | python3                  | 51358                   |
+===========================+===============+====================================================+
| 2       0                 | 265997        | python3                  | 51358                   |
+===========================+===============+====================================================+
| 3       0                 | 265997        | python3                  | 51358                   |
+===========================+===============+====================================================+
| 4       0                 | 265997        | python3                  | 51358                   |
+===========================+===============+====================================================+
| 5       0                 | 265997        | python3                  | 51358                   |
+===========================+===============+====================================================+
| 6       0                 | 265997        | python3                  | 51358                   |
+===========================+===============+====================================================+
| 7       0                 | 265997        | python3                  | 51358                   |
+===========================+===============+====================================================+
| 8       0                 | 265997        | python3                  | 51358                   |
+===========================+===============+====================================================+
| 9       0                 | 265997        | python3                  | 51358                   |
+===========================+===============+====================================================+
| 10      0                 | 265997        | python3                  | 51358                   |
+===========================+===============+====================================================+
| 11      0                 | 265997        | python3                  | 51358                   |
+===========================+===============+====================================================+
| 12      0                 | 265997        | python3                  | 51358                   |
+===========================+===============+====================================================+
| 13      0                 | 265997        | python3                  | 51358                   |
+===========================+===============+====================================================+
| 14      0                 | 265997        | python3                  | 51358                   |
+===========================+===============+====================================================+
| 15      0                 | 265997        | python3                  | 51358                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.2.RC1
innerversion=V100R001C23B001
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/x86_64-linux
```

</details>






### 🐛 Describe the bug


start command of both nodes are:

```bash
# p.sh
unset ftp_proxy
unset https_proxy
unset http_proxy
export HCCL_IF_IP=2605:340:cd51:4900:d548:f301:6e02:269c
export GLOO_SOCKET_IFNAME="eth0"  # network card name
export TP_SOCKET_IFNAME="eth0"
export HCCL_SOCKET_IFNAME="eth0"
export VLLM_USE_V1=1
# export HCCL_BUFFSIZE=1024
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/python/site-packages:$LD_LIBRARY_PATH
export PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256

python -m vllm.entrypoints.openai.api_server \
  --model /mnt/bn/nas-assinfra-hl-03/ckpt/DeepSeek-V3.1-Terminus-w8a8-QuaRot \
  --host 0.0.0.0 \
  --port 8004 \
  --api-server-count 1 \
  --tensor-parallel-size 16 \
  --no-enable-expert-parallel \
  --seed 1024 \
  --enforce-eager \
  --distributed-executor-backend mp \
  --served-model-name deepseek_v3 \
  --max-model-len 1024 \
  --max-num-batched-tokens 1024 \
  --max-num_seqs 1 \
  --trust-remote-code \
  --gpu-memory-utilization 0.96 \
  --kv-transfer-config \
  '{"kv_connector": "MooncakeConnector",
  "kv_role": "kv_producer",
  "kv_port": "30000",
  "engine_id": "0",
  "kv_connector_module_path": "vllm_ascend.distributed.mooncake_connector",
  "kv_connector_extra_config": {
            "prefill": {
                    "dp_size": 1,
                    "tp_size": 16
             },
             "decode": {
                    "dp_size": 1,
                    "tp_size": 16
             }
      }
  }'

# d.sh
unset ftp_proxy
unset https_proxy
unset http_proxy
export HCCL_IF_IP=2605:340:cd51:4900:548a:4861:b062:2eb8
export GLOO_SOCKET_IFNAME="eth0"  # network card name
export TP_SOCKET_IFNAME="eth0"
export HCCL_SOCKET_IFNAME="eth0"
export VLLM_USE_V1=1
# export HCCL_BUFFSIZE=2048
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/python/site-packages:$LD_LIBRARY_PATH
export PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256

python -m vllm.entrypoints.openai.api_server \
  --model /mnt/bn/nas-assinfra-hl-03/ckpt/DeepSeek-V3.1-Terminus-w8a8-QuaRot \
  --host 0.0.0.0 \
  --port 8004 \
  --tensor-parallel-size 16 \
  --no-enable-expert-parallel \
  --seed 1024 \
  --distributed-executor-backend mp \
  --served-model-name deepseek_v3 \
  --max-model-len 1024 \
  --max-num-batched-tokens 512 \
  --max-num_seqs 1 \
  --trust-remote-code \
  --no-enable-prefix-caching \
  --gpu-memory-utilization 0.96 \
  --compilation-config '{"cudagraph_capture_sizes":[1]}' \
  --kv-transfer-config \
  '{"kv_connector": "MooncakeConnector",
  "kv_role": "kv_consumer",
  "kv_port": "30200",
  "engine_id": "1",
  "kv_connector_module_path": "vllm_ascend.distributed.mooncake_connector",
  "kv_connector_extra_config": {
            "prefill": {
                    "dp_size": 1,
                    "tp_size": 16
             },
             "decode": {
                    "dp_size": 1,
                    "tp_size": 16
             }
      }
  }'
```

Error logs (both nodes are same):

```text
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597] WorkerProc failed to start.
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597] Traceback (most recent call last):
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm/vllm/v1/executor/multiproc_executor.py", line 571, in worker_main
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     worker = WorkerProc(*args, **kwargs)
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm/vllm/v1/executor/multiproc_executor.py", line 437, in __init__
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     self.worker.load_model()
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 307, in load_model
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     self.model_runner.load_model()
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2653, in load_model
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     self.model = get_model(vllm_config=self.vllm_config)
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm/vllm/model_executor/model_loader/__init__.py", line 119, in get_model
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     return loader.load_model(vllm_config=vllm_config,
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm/vllm/model_executor/model_loader/base_loader.py", line 45, in load_model
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     model = initialize_model(vllm_config=vllm_config,
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm/vllm/model_executor/model_loader/utils.py", line 63, in initialize_model
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     return model_class(vllm_config=vllm_config, prefix=prefix)
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm/vllm/model_executor/models/deepseek_v2.py", line 1208, in __init__
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     self.model = DeepseekV2Model(vllm_config=vllm_config,
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm/vllm/compilation/decorators.py", line 201, in __init__
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm/vllm/model_executor/models/deepseek_v2.py", line 1135, in __init__
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     self.start_layer, self.end_layer, self.layers = make_layers(
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]                                                     ^^^^^^^^^^^^
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm/vllm/model_executor/models/utils.py", line 629, in make_layers
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     [PPMissingLayer() for _ in range(start_layer)] + [
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]                                                      ^
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm/vllm/model_executor/models/utils.py", line 630, in <listcomp>
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm/vllm/model_executor/models/deepseek_v2.py", line 1137, in <lambda>
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     lambda prefix: DeepseekV2DecoderLayer(vllm_config, prefix,
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm/vllm/model_executor/models/deepseek_v2.py", line 1037, in __init__
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     self.mlp = DeepseekV2MoE(
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]                ^^^^^^^^^^^^^^
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm/vllm/model_executor/models/deepseek_v2.py", line 220, in __init__
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     self.experts = SharedFusedMoE(
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]                    ^^^^^^^^^^^^^^^
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm-ascend/vllm_ascend/ops/common_fused_moe.py", line 418, in __init__
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     AscendFusedMoE.__init__(self, **kwargs)
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm-ascend/vllm_ascend/ops/common_fused_moe.py", line 155, in __init__
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     super().__init__(*args, **kwargs)
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 1140, in __init__
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     self.quant_method.create_weights(layer=self, **moe_quant_params)
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/mnt/bn/nas-assinfra-hl-03/work/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 366, in create_weights
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     w13_weight = torch.nn.Parameter(torch.empty(
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]                                     ^^^^^^^^^^^^
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]   File "/usr/local/lib/python3.11/site-packages/torch/utils/_device.py", line 104, in __torch_function__
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]     return func(*args, **kwargs)
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP0 pid=248987) ERROR 11-05 21:25:41 [multiproc_executor.py:597] RuntimeError: NPU out of memory. Tried to allocate 898.00 MiB (NPU 0; 60.97 GiB total capacity; 58.21 GiB already allocated; 58.21 GiB current active; 848.37 MiB free; 58.31 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.
```

### Why not EP?
 - Current hdk is too old.

### Why npu memory is high in the output of collect_env.py?
 - somebody else is using during collection(not the cause of truble).

