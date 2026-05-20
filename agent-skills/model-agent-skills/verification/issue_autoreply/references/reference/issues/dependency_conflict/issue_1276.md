# Issue #1276: [Bug]:AttributeError: 'InternVLChatConfig' object has no attribute 'num_hidden_layers'

## 基本信息

- **编号**: #1276
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1276
- **创建时间**: 2025-06-18T09:17:57Z
- **关闭时间**: 2025-07-26T12:14:54Z
- **更新时间**: 2025-09-12T06:18:05Z
- **提交者**: @MaShengyu
- **评论数**: 8

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
 python collect_env.py
INFO 06-18 07:23:03 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-18 07:23:03 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-18 07:23:04 [__init__.py:31] Available plugins for group vllm.platform_plugins:
INFO 06-18 07:23:04 [__init__.py:33] - ascend -> vllm_ascend:register
INFO 06-18 07:23:04 [__init__.py:36] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 06-18 07:23:04 [__init__.py:234] Platform plugin ascend is activated
WARNING 06-18 07:23:08 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.2
Libc version: glibc-2.35

Python version: 3.10.17 (main, May  8 2025, 07:18:04) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.15.0-91-generic-aarch64-with-glibc2.35

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
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.52.4
[conda] Could not collect
vLLM Version: 0.9.0
vLLM Ascend Version: 0.9.0rc2

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
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
| npu-smi 24.1.0.3                 Version: 24.1.0.3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 89.2        50                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3380/ 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 93.1        52                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3377/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
+===========================+===============+====================================================+


CANN:
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux
root@DevServer-BMS-85a6d04f:/home/work/product#

```

</details>

### 🐛 Describe the bug

hi community, i am trying to run [InternVL2_5-38B](https://huggingface.co/OpenGVLab/InternVL2_5-38B) within the official docker container quay.io/ascend/vllm-ascend:v0.9.0rc2. then i get a launch error. here is my launch script:

```sh
# disable mindie_turbo
pip uninstall mindie_turbo
unset http_proxy
unset https_proxy

export VLLM_USE_V1=1

vllm serve \
/home/work/models/OpenGVLab/InternVL2_5-38B \
--port 9002 \
--max-num-seqs 16 \
--served-model-name InternVL2_5-38B \
--gpu-memory-utilization 0.9 \
--tensor-parallel-size 2
```
the error infomation is below.

```sh
root@DevServer-BMS-85a6d04f:/home/work/product/internvl2.5# ./start.sh
WARNING: Skipping mindie_turbo as it is not installed.
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
INFO 06-18 06:54:42 [importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 06-18 06:54:42 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 06-18 06:54:43 [__init__.py:31] Available plugins for group vllm.platform_plugins:
INFO 06-18 06:54:43 [__init__.py:33] - ascend -> vllm_ascend:register
INFO 06-18 06:54:43 [__init__.py:36] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 06-18 06:54:43 [__init__.py:234] Platform plugin ascend is activated
WARNING 06-18 06:54:47 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 06-18 06:54:49 [__init__.py:31] Available plugins for group vllm.general_plugins:
INFO 06-18 06:54:49 [__init__.py:33] - ascend_enhanced_model -> vllm_ascend:register_model
INFO 06-18 06:54:49 [__init__.py:33] - lora_filesystem_resolver -> vllm.plugins.lora_resolvers.filesystem_resolver:register_filesystem_resolver
INFO 06-18 06:54:49 [__init__.py:36] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
WARNING 06-18 06:54:51 [registry.py:397] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 06-18 06:54:51 [registry.py:397] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 06-18 06:54:51 [registry.py:397] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 06-18 06:54:51 [registry.py:397] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 06-18 06:54:51 [registry.py:397] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 06-18 06:54:51 [registry.py:397] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 06-18 06:54:52 [config.py:1909] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-18 06:54:54 [config.py:1909] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-18 06:54:55 [config.py:1909] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-18 06:54:55 [api_server.py:1289] vLLM API server version 0.9.0
INFO 06-18 06:54:57 [config.py:1909] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-18 06:54:57 [cli_args.py:300] non-default args: {'port': 9002, 'served_model_name': ['InternVL2_5-38B'], 'max_num_seqs': 16}
INFO 06-18 06:55:12 [config.py:793] This model supports multiple tasks: {'classify', 'generate', 'score', 'reward', 'embed'}. Defaulting to 'generate'.
WARNING 06-18 06:55:12 [arg_utils.py:1588] Detected VLLM_USE_V1=1 with npu. Usage should be considered experimental. Please report any issues on Github.
INFO 06-18 06:55:12 [config.py:1909] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 06-18 06:55:12 [config.py:2118] Chunked prefill is enabled with max_num_batched_tokens=2048.
WARNING 06-18 06:55:12 [ascend_config.py:160] ACL Graph is currently experimental. Please raise an issue on https://github.com/vllm-project/vllm-ascend/issues if you encourage any Error
INFO 06-18 06:55:12 [platform.py:183] PIECEWISE compilation enabled on NPU. use_inductor not supported - using only ACL Graph mode
Traceback (most recent call last):
  File "/usr/local/python3.10.17/bin/vllm", line 8, in <module>
    sys.exit(main())
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 56, in main
    args.dispatch_function(args)
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 42, in cmd
    uvloop.run(run_server(args))
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
    return loop.run_until_complete(wrapper())
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
    return await main
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1324, in run_server
    async with build_async_engine_client(args) as engine_client:
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 153, in build_async_engine_client
    async with build_async_engine_client_from_engine_args(
  File "/usr/local/python3.10.17/lib/python3.10/contextlib.py", line 199, in __aenter__
    return await anext(self.gen)
  File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 173, in build_async_engine_client_from_engine_args
    vllm_config = engine_args.create_engine_config(usage_context=usage_context)
  File "/vllm-workspace/vllm/vllm/engine/arg_utils.py", line 1172, in create_engine_config
    config = VllmConfig(
  File "<string>", line 20, in __init__
  File "/vllm-workspace/vllm/vllm/config.py", line 4364, in __post_init__
    current_platform.check_and_update_config(self)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/platform.py", line 189, in check_and_update_config
    update_aclgraph_sizes(vllm_config)
  File "/vllm-workspace/vllm-ascend/vllm_ascend/utils.py", line 134, in update_aclgraph_sizes
    num_hidden_layers = vllm_config.model_config.hf_config.num_hidden_layers
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/transformers/configuration_utils.py", line 211, in __getattribute__
    return super().__getattribute__(key)
AttributeError: 'InternVLChatConfig' object has no attribute 'num_hidden_layers'
[ERROR] 2025-06-18-06:55:12 (PID:4251, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
root@DevServer-BMS-85a6d04f:/home/work/product/internvl2.5#
```

seems like a model config and adaptation issue, but according to vllm-ascend [docs](https://vllm-ascend.readthedocs.io/en/v0.9.0rc2/user_guide/supported_models.html#multimodal-language-models), InternVL2.5 is already supported, and should be ok on this simple test. I want to know what caused the error, bug in code or wrong operation or document error？
