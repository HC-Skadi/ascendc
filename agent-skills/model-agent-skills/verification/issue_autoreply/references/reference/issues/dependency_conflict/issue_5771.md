# Issue #5771: [Bug]:DeepseekOCR模型单机单卡部署，开启入图后服务无法启动

## 基本信息

- **编号**: #5771
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5771
- **创建时间**: 2026-01-09T09:45:21Z
- **关闭时间**: 2026-01-15T07:42:33Z
- **更新时间**: 2026-01-15T07:42:33Z
- **提交者**: @wangbei25HW
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```
PyTorch version: 2.8.0+cpu
Is debug build: False

OS: Ubuntu 24.04.3 LTS (aarch64)
GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0
Clang version: Could not collect
CMake version: version 4.1.2
Libc version: glibc-2.39

Python version: 3.11.10 (main, Nov  7 2025, 18:12:58) [GCC 13.3.0] (64-bit runtime)
Python platform: Linux-5.15.0-25-generic-aarch64-with-glibc2.39

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          256
On-line CPU(s) list:             0-255
Vendor ID:                       HiSilicon
BIOS Vendor ID:                  HiSilicon
Model name:                      Kunpeng-920
BIOS Model name:                 HUAWEI Kunpeng 920 7265 To be filled by O.E.M. CPU @ 3.0GHz
BIOS CPU family:                 280
Model:                           0
Thread(s) per core:              1
Core(s) per socket:              64
Socket(s):                       4
Stepping:                        0x1
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       16 MiB (256 instances)
L1i cache:                       16 MiB (256 instances)
L2 cache:                        128 MiB (256 instances)
L3 cache:                        256 MiB (8 instances)
NUMA node(s):                    8
NUMA node0 CPU(s):               0-31
NUMA node1 CPU(s):               32-63
NUMA node2 CPU(s):               64-95
NUMA node3 CPU(s):               96-127
NUMA node4 CPU(s):               128-159
NUMA node5 CPU(s):               160-191
NUMA node6 CPU(s):               192-223
NUMA node7 CPU(s):               224-255
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
[pip3] pyzmq==27.1.0
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.3
[conda] Could not collect
vLLM Version: 0.14.0rc1.dev267+g2f4e6548e (git sha: 2f4e6548e)
vLLM Ascend Version: 0.13.0rc2.dev105+gd6bb17f10.d20260108 (git sha: d6bb17f10, date: 20260108)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_RT_VISIBLE_DEVICES=7
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
VLLM_TORCH_PROFILER_DIR=/home/w00804037/profiling_deepseekocr/
ASCEND_RUNTIME_OPTIONS=NODRV
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/lib::/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/lib::/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux/devlib
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
| npu-smi 25.3.rc1.2               Version: 25.3.rc1.2                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 94.0        46                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3454 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 89.7        48                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3424 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 92.8        46                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3431 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 92.3        46                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          29975/ 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 352.0       71                0    / 0             |
| 0                         | 0000:01:00.0  | 75          0    / 0          50616/ 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 94.1        51                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          30904/ 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 94.5        50                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          30903/ 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 92.0        50                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3448 / 65536         |
+===========================+===============+====================================================+


CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC1
innerversion=V100R001C23SPC002B201
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC1/aarch64-linux

</details>


### 🐛 Describe the bug

DeepseekOCR模型单机单卡部署，开启入图服务无法拉起

vllm serve /home/weights/DeepSeek-OCR \
    --served-model-name deepseekocr \
    --trust-remote-code \
    -tp 1  \
    --port 1055 \
    --max_model_len 8192 \
    --no-enable-prefix-caching \
    --gpu-memory-utilization 0.9 \
    --allowed-local-media-path /home/datasets \
    --async-scheduling \
    --additional-config '{
        "enable_cpu_binding": true,
        "ascend_scheduler_config": {
            "enabled": false,
            "enable_chunked_prefill": true,
            "chunked_prefill_enabled": true,
            "enable_pd_transfer": true
    	},
    	"multistream_overlap_shared_expert": true
    }' \
    --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY"}'

报错信息如下：
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888] Traceback (most recent call last):
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3035, in _torch_cuda_wrapper
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     yield
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2981, in capture_model
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     super().capture_model()
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm/vllm/v1/worker/gpu_model_runner.py", line 4782, in capture_model
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     self._capture_cudagraphs(
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm/vllm/v1/worker/gpu_model_runner.py", line 4870, in _capture_cudagraphs
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     self._dummy_run(
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return func(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2241, in _dummy_run
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     hidden_states = self._generate_dummy_run_hidden_states(
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2019, in _generate_dummy_run_hidden_states
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     hidden_states = self.model(input_ids=input_ids,
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm-ascend/vllm_ascend/compilation/acl_graph.py", line 155, in __call__
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     output = self.runnable(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return self._call_impl(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return forward_call(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm/vllm/model_executor/models/deepseek_ocr.py", line 579, in forward
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     hidden_states = self.language_model(
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]                     ^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return self._call_impl(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return forward_call(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm/vllm/model_executor/models/deepseek_v2.py", line 1473, in forward
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     hidden_states = self.model(
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]                     ^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm/vllm/compilation/decorators.py", line 442, in __call__
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return TorchCompileWithNoGuardsWrapper.__call__(self, *args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm/vllm/compilation/wrapper.py", line 223, in __call__
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return self._call_with_optional_nvtx_range(
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm/vllm/compilation/wrapper.py", line 109, in _call_with_optional_nvtx_range
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return callable_fn(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm-ascend/vllm_ascend/patch/worker/patch_deepseek.py", line 10, in forward
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     def forward(
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 929, in _fn
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return fn(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm/vllm/compilation/caching.py", line 57, in __call__
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return self.optimized_call(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/fx/graph_module.py", line 848, in call_wrapped
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return self._wrapped_call(self, *args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/fx/graph_module.py", line 424, in __call__
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     raise e
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/fx/graph_module.py", line 411, in __call__
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return self._call_impl(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return forward_call(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "<eval_with_key>.2", line 70, in forward
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     submod_0 = self.submod_0(l_inputs_embeds_, s59, l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_, l_positions_, s80, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_, l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_mlp_modules_gate_up_proj_parameters_weight_, l_self_modules_layers_modules_0_modules_mlp_modules_down_proj_parameters_weight_, l_self_modules_layers_modules_1_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_o_proj_parameters_weight_, l_self_modules_layers_modules_1_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_1_modules_mlp_modules_gate_parameters_weight_, l_self_modules_layers_modules_2_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_2_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_2_modules_self_attn_modules_o_proj_parameters_weight_, l_self_modules_layers_modules_2_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_2_modules_mlp_modules_gate_parameters_weight_, l_self_modules_layers_modules_3_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_3_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_3_modules_self_attn_modules_o_proj_parameters_weight_, l_self_modules_layers_modules_3_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_3_modules_mlp_modules_gate_parameters_weight_, l_self_modules_layers_modules_4_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_4_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_4_modules_self_attn_modules_o_proj_parameters_weight_, l_self_modules_layers_modules_4_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_4_modules_mlp_modules_gate_parameters_weight_, l_self_modules_layers_modules_5_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_5_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_5_modules_self_attn_modules_o_proj_parameters_weight_, l_self_modules_layers_modules_5_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_5_modules_mlp_modules_gate_parameters_weight_, l_self_modules_layers_modules_6_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_6_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_6_modules_self_attn_modules_o_proj_parameters_weight_, l_self_modules_layers_modules_6_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_6_modules_mlp_modules_gate_parameters_weight_, l_self_modules_layers_modules_7_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_7_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_7_modules_self_attn_modules_o_proj_parameters_weight_, l_self_modules_layers_modules_7_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_7_modules_mlp_modules_gate_parameters_weight_, l_self_modules_layers_modules_8_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_8_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_8_modules_self_attn_modules_o_proj_parameters_weight_, l_self_modules_layers_modules_8_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_8_modules_mlp_modules_gate_parameters_weight_, l_self_modules_layers_modules_9_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_9_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_9_modules_self_attn_modules_o_proj_parameters_weight_, l_self_modules_layers_modules_9_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_9_modules_mlp_modules_gate_parameters_weight_, l_self_modules_layers_modules_10_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_10_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_10_modules_self_attn_modules_o_proj_parameters_weight_, l_self_modules_layers_modules_10_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_10_modules_mlp_modules_gate_parameters_weight_, l_self_modules_layers_modules_11_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_11_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_11_modules_self_attn_modules_o_proj_parameters_weight_, l_self_modules_layers_modules_11_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_11_modules_mlp_modules_gate_parameters_weight_, l_self_modules_norm_parameters_weight_);  l_inputs_embeds_ = s59 = l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_positions_ = s80 = l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_ = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_ = l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_0_modules_mlp_modules_gate_up_proj_parameters_weight_ = l_self_modules_layers_modules_0_modules_mlp_modules_down_proj_parameters_weight_ = l_self_modules_layers_modules_1_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_o_proj_parameters_weight_ = l_self_modules_layers_modules_1_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_1_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_layers_modules_2_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_2_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_2_modules_self_attn_modules_o_proj_parameters_weight_ = l_self_modules_layers_modules_2_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_2_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_layers_modules_3_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_3_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_3_modules_self_attn_modules_o_proj_parameters_weight_ = l_self_modules_layers_modules_3_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_3_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_layers_modules_4_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_4_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_4_modules_self_attn_modules_o_proj_parameters_weight_ = l_self_modules_layers_modules_4_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_4_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_layers_modules_5_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_5_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_5_modules_self_attn_modules_o_proj_parameters_weight_ = l_self_modules_layers_modules_5_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_5_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_layers_modules_6_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_6_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_6_modules_self_attn_modules_o_proj_parameters_weight_ = l_self_modules_layers_modules_6_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_6_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_layers_modules_7_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_7_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_7_modules_self_attn_modules_o_proj_parameters_weight_ = l_self_modules_layers_modules_7_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_7_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_layers_modules_8_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_8_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_8_modules_self_attn_modules_o_proj_parameters_weight_ = l_self_modules_layers_modules_8_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_8_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_layers_modules_9_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_9_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_9_modules_self_attn_modules_o_proj_parameters_weight_ = l_self_modules_layers_modules_9_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_9_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_layers_modules_10_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_10_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_10_modules_self_attn_modules_o_proj_parameters_weight_ = l_self_modules_layers_modules_10_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_10_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_layers_modules_11_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_11_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_11_modules_self_attn_modules_o_proj_parameters_weight_ = l_self_modules_layers_modules_11_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_11_modules_mlp_modules_gate_parameters_weight_ = l_self_modules_norm_parameters_weight_ = None
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm-ascend/vllm_ascend/patch/platform/patch_compile_backend.py", line 230, in __call__
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return self.compiled_graph_for_general_shape(*args)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_inductor/compile_fx.py", line 2474, in wrapper
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return pytree.tree_unflatten(compiled_fn(*args, **kwargs), spec)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 929, in _fn
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return fn(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_functorch/aot_autograd.py", line 1241, in forward
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return compiled_fn(full_args)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py", line 384, in runtime_wrapper
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     all_outs = call_func_at_runtime_with_args(
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/utils.py", line 126, in call_func_at_runtime_with_args
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     out = normalize_as_list(f(args))
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]                             ^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py", line 750, in inner_fn
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     outs = compiled_fn(args)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py", line 556, in wrapper
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return compiled_fn(runtime_args)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/utils.py", line 100, in g
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return f(*args)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/fx/graph_module.py", line 848, in call_wrapped
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return self._wrapped_call(self, *args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/fx/graph_module.py", line 424, in __call__
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     raise e
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/fx/graph_module.py", line 411, in __call__
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return self._call_impl(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return forward_call(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "<eval_with_key>.3 from /usr/local/python3.11.10/lib/python3.11/site-packages/torch/fx/experimental/proxy_tensor.py:1301 in wrapped", line 27, in forward
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     auto_functionalized_v2_1 = torch.ops.higher_order.auto_functionalized_v2(torch.ops.vllm.unified_attention_with_output.default, query = view_10, key = view_13, value = view_7, layer_name = 'language_model.model.layers.0.self_attn.attn', output_scale = None, _output_base_index = 0, _output_size = (arg1_1, 10, 128), _output_stride = (1280, 128, 1), _output_storage_offset = 0, _output_block_scale_base_index = None, _all_bases = [empty]);  view_10 = view_13 = view_7 = empty = None
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_higher_order_ops/auto_functionalize.py", line 401, in __call__
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return super().__call__(_mutable_op, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_ops.py", line 524, in __call__
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return wrapper()
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_ops.py", line 520, in wrapper
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return self.dispatch(
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_ops.py", line 380, in dispatch
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return kernel(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_higher_order_ops/auto_functionalize.py", line 856, in auto_functionalized_v2_dense
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     out = call_op(
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]           ^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_higher_order_ops/utils.py", line 1017, in call_op
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return op(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_ops.py", line 829, in __call__
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return self._op(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm/vllm/attention/utils/kv_transfer_utils.py", line 39, in wrapper
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return func(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm/vllm/attention/layer.py", line 807, in unified_attention_with_output
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     self.impl.forward(
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 751, in forward
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     output = self.forward_impl(query, key, value, kv_cache, attn_metadata,
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 697, in forward_impl
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     output = self.forward_fused_infer_attention(
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 556, in forward_fused_infer_attention
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     attn_output, num_tokens = self.full_graph_fia(
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]                               ^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm-ascend/vllm_ascend/attention/attention_v1.py", line 361, in full_graph_fia
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     workspace = torch_npu._npu_fused_infer_attention_score_get_max_workspace(
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/site-packages/torch/_ops.py", line 1243, in __call__
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return self._op(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888] RuntimeError: operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:356 NPU function error: call aclnnFusedInferAttentionScoreV3 failed, error code is 561002
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888] [ERROR] 2026-01-09-16:59:36 (PID:12986, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888] E89999: Inner Error!
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888] E89999[PID: 12986] 2026-01-09-16:59:36.554.046 (E89999):  When layout is TND/NTD_TND, not support tiling_schedule_optimize = True or config mode is reduce-overhead![FUNC:RunBigKernelTilingWithParams][FILE:prompt_flash_attention_tiling.cpp][LINE:4157]
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]         TraceBack (most recent call last):
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]        tiling process fo ifa failed[FUNC:TilingFusedInferAttentionScore][FILE:fused_infer_attention_score_tiling.cpp][LINE:1845]
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]        FusedInferAttentionScore do tiling failed, ret is -1.
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]        Check NnopbaseExecutorDoTiling(executor) failed
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]        Check NnopbaseExecutorTilingAndUpdateBinInfo(executor) failed
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]        Check NnopbaseExecutorMatchCache(executor) failed
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]        Check NnopbaseRunForWorkspace(*executor, workspaceSize) failed
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888] 
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888] 
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888] During handling of the above exception, another exception occurred:
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888] 
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888] Traceback (most recent call last):
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm/vllm/v1/engine/core.py", line 879, in run_engine_core
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm/vllm/v1/engine/core.py", line 644, in __init__
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     super().__init__(
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm/vllm/v1/engine/core.py", line 112, in __init__
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches(
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm/vllm/v1/engine/core.py", line 270, in _initialize_kv_caches
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     self.model_executor.initialize_from_config(kv_cache_configs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm/vllm/v1/executor/abstract.py", line 116, in initialize_from_config
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     self.collective_rpc("compile_or_warm_up_model")
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm/vllm/v1/executor/uniproc_executor.py", line 75, in collective_rpc
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     result = run_method(self.driver_worker, method, args, kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm/vllm/v1/serial_utils.py", line 461, in run_method
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     return func(*args, **kwargs)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm-ascend/vllm_ascend/worker/worker.py", line 392, in compile_or_warm_up_model
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     self.model_runner.capture_model()
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2979, in capture_model
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     with _torch_cuda_wrapper(), _replace_gpu_model_runner_function_wrapper(
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/usr/local/python3.11.10/lib/python3.11/contextlib.py", line 158, in __exit__
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     self.gen.throw(typ, value, traceback)
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]   File "/home/code/main/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3044, in _torch_cuda_wrapper
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]     raise RuntimeError(f"NPUModelRunner init failed, error is {e}")
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888] RuntimeError: NPUModelRunner init failed, error is operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:356 NPU function error: call aclnnFusedInferAttentionScoreV3 failed, error code is 561002
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888] [ERROR] 2026-01-09-16:59:36 (PID:12986, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888] E89999: Inner Error!
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888] E89999[PID: 12986] 2026-01-09-16:59:36.554.046 (E89999):  When layout is TND/NTD_TND, not support tiling_schedule_optimize = True or config mode is reduce-overhead![FUNC:RunBigKernelTilingWithParams][FILE:prompt_flash_attention_tiling.cpp][LINE:4157]
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]         TraceBack (most recent call last):
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]        tiling process fo ifa failed[FUNC:TilingFusedInferAttentionScore][FILE:fused_infer_attention_score_tiling.cpp][LINE:1845]
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]        FusedInferAttentionScore do tiling failed, ret is -1.
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]        Check NnopbaseExecutorDoTiling(executor) failed
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]        Check NnopbaseExecutorTilingAndUpdateBinInfo(executor) failed
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]        Check NnopbaseExecutorMatchCache(executor) failed
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888]        Check NnopbaseRunForWorkspace(*executor, workspaceSize) failed
(EngineCore_DP0 pid=12986) ERROR 01-09 16:59:37 [core.py:888] 
