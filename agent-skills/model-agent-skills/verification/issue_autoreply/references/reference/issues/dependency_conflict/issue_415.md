# Issue #415: [Bug]: ModuleNotFoundError: No module named 'vllm_ascend.attention'

## 基本信息

- **编号**: #415
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/415
- **创建时间**: 2025-03-28T01:40:56Z
- **关闭时间**: 2025-05-14T03:04:09Z
- **更新时间**: 2025-05-14T03:04:10Z
- **提交者**: @xinyi0513
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

Describe the bug:
INFO 03-28 01:39:07 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 03-28 01:39:07 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 03-28 01:39:07 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-28 01:39:07 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-28 01:39:07 __init__.py:44] plugin ascend loaded.
INFO 03-28 01:39:07 __init__.py:198] Platform plugin ascend is activated
INFO 03-28 01:39:07 __init__.py:30] Available plugins for group vllm.general_plugins:
INFO 03-28 01:39:07 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 03-28 01:39:07 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 03-28 01:39:07 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-28 01:39:07 __init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 03-28 01:39:07 _custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 03-28 01:39:07 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 03-28 01:39:08 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
INFO 03-28 01:39:17 config.py:549] This model supports multiple tasks: {'generate', 'classify', 'score', 'reward', 'embed'}. Defaulting to 'generate'.
WARNING 03-28 01:39:17 arg_utils.py:1197] The model has a long context length (128000). This may cause OOM errors during the initial memory profiling phase, or result in low performance due to small KV cache space. Consider setting --max-model-len to a smaller value.
Traceback (most recent call last):
  File "/apps/xinyi/2025/inference/VLM/Qwen2.5-VL/vllm-ascend/02.code/test.py", line 10, in <module>
    llm = LLM(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 1022, in inner
    return fn(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 242, in __init__
    self.llm_engine = self.engine_class.from_engine_args(
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 486, in from_engine_args
    engine_config = engine_args.create_engine_config(usage_context)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 1334, in create_engine_config
    config = VllmConfig(
  File "<string>", line 19, in __init__
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/config.py", line 3325, in __post_init__
    current_platform.check_and_update_config(self)
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/platform.py", line 106, in check_and_update_config
    from vllm_ascend.patch import ray_patch  # noqa: F401
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/patch/__init__.py", line 21, in <module>
    import vllm_ascend.patch.patch_spec_decode_worker  # noqa
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/patch/patch_spec_decode_worker.py", line 35, in <module>
    from vllm_ascend.worker.draft_model_runner import TP1DraftModelRunner
  File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/draft_model_runner.py", line 30, in <module>
    from vllm_ascend.attention.attention import \
ModuleNotFoundError: No module named 'vllm_ascend.attention'
[ERROR] 2025-03-28-01:39:18 (PID:1090, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception

test code:
llm = LLM(
    model= "/data/models/Qwen2___5-VL-7B-Instruct/",
    limit_mm_per_prompt={"image": 16, "video": 0},
)



envirnment:
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: openEuler 22.03 (LTS-SP4) (aarch64)
GCC version: Could not collect
Clang version: Could not collect
CMake version: Could not collect
Libc version: glibc-2.34

Python version: 3.10.16 (main, Feb 13 2025, 15:02:10) [GCC 10.3.1] (64-bit runtime)
Python platform: Linux-4.19.90-2102.2.0.0068.3.ctl2.aarch64-aarch64-with-glibc2.34

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
NUMA node(s):                    4
NUMA node0 CPU(s):               0-47
NUMA node1 CPU(s):               48-95
NUMA node2 CPU(s):               96-143
NUMA node3 CPU(s):               144-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.3.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250308
[pip3] torchvision==0.20.1
[pip3] transformers==4.50.1
[conda] Could not collect
vLLM Version: 0.7.3
vLLM Ascend Version: 0.7.3rc2.dev9+g7fbdd01.d20250327

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
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
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc2.1               Version: 24.1.rc2.1                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 95.5        35                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3353 / 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 94.4        37                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3353 / 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 94.7        36                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3345 / 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 92.8        39                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3345 / 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 96.7        36                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3345 / 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 95.4        37                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3345 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 94.6        36                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3345 / 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 90.3        37                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3345 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux

