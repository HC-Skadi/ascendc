# Issue #3963: [Bug]: Qwen3-Omni-30B-A3B-Thinking start serve failed due to AclrtSynchronizeStreamWithTimeout(copy_stream), error code is 107027

## 基本信息

- **编号**: #3963
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3963
- **创建时间**: 2025-11-04T01:11:45Z
- **关闭时间**: 2025-12-31T01:05:20Z
- **更新时间**: 2025-12-31T01:05:20Z
- **提交者**: @Meihan-chen
- **评论数**: 2

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

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.1.2
Libc version: glibc-2.35

Python version: 3.11.14 (main, Oct 21 2025, 18:24:34) [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-5.10.0-182.0.0.95.r1941_123.hce2.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                         aarch64
CPU op-mode(s):                       64-bit
Byte Order:                           Little Endian
CPU(s):                               320
On-line CPU(s) list:                  0-319
Vendor ID:                            HiSilicon
Model:                                0
Thread(s) per core:                   1
Core(s) per cluster:                  80
Socket(s):                            -
Cluster(s):                           4
Stepping:                             0x0
Frequency boost:                      disabled
CPU max MHz:                          3000.0000
CPU min MHz:                          400.0000
BogoMIPS:                             200.00
Flags:                                fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs sb paca pacg dcpodp flagm2 frint svei8mm svef32mm svef64mm svebf16 i8mm bf16 dgh rng ecv
L1d cache:                            20 MiB (320 instances)
L1i cache:                            20 MiB (320 instances)
L2 cache:                             400 MiB (320 instances)
L3 cache:                             560 MiB (8 instances)
NUMA node(s):                         8
NUMA node0 CPU(s):                    0-39
NUMA node1 CPU(s):                    40-79
NUMA node2 CPU(s):                    80-119
NUMA node3 CPU(s):                    120-159
NUMA node4 CPU(s):                    160-199
NUMA node5 CPU(s):                    200-239
NUMA node6 CPU(s):                    240-279
NUMA node7 CPU(s):                    280-319
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
[pip3] mypy==1.11.1
[pip3] mypy_extensions==1.1.0
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] sentence-transformers==5.1.2
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[pip3] zmq==0.0.0
[conda] numpy                                1.26.4                            pypi_0           pypi
[conda] pyzmq                                27.1.0                            pypi_0           pypi
[conda] sentence-transformers                5.1.2                             pypi_0           pypi
[conda] torch                                2.7.1+cpu                         pypi_0           pypi
[conda] torch-npu                            2.7.1.dev20250724                 pypi_0           pypi
[conda] torchvision                          0.22.1                            pypi_0           pypi
[conda] transformers                         4.57.1                            pypi_0           pypi
[conda] zmq                                  0.0.0                             pypi_0           pypi
vLLM Version: 0.11.1rc6.dev12+gb2e65cb4a (git sha: b2e65cb4a)
vLLM Ascend Version: 0.11.0rc1.dev249+g1f486b2dd (git sha: 1f486b2dd)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
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
| npu-smi 24.1.rc3.7               Version: 24.1.rc3.7                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 176.3       36                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3411 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           36                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          3208 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.2.RC1
innerversion=V100R001C22SPC001B231
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux
```

</details>



### 🐛 Describe the bug
commands
`vllm serve /root/.cache/modelscope/hub/models/Qwen/Qwen3-Omni-30B-A3B-Thinking --tensor-parallel-size 2 --enable_expert_parallel`

logs
```bash
(Worker_TP0_EP0 pid=6952) INFO 11-03 13:19:41 [model_runner_v1.py:3964] Starting to capture ACL graphs for cases: [1, 24, 64, 104, 144, 184, 224, 272, 352, 432, 512], mode: PIECEWISE, uniform_decode: False
Capturing ACL graphs (mixed prefill-decode, PIECEWISE):   9%|██████████▎                                                                                                      | 1/11 [00:01<00:11,  1.18s/it][rank1]:[W1103 13:19:43.194702705 compiler_depend.ts:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
[rank0]:[W1103 13:19:43.230947907 compiler_depend.ts:149] Warning: Waiting for pending NCCL work to finish before starting graph capture. (function operator())
Capturing ACL graphs (mixed prefill-decode, PIECEWISE):   9%|██████████▎                                                                                                      | 1/11 [00:02<00:23,  2.32s/it]
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699] WorkerProc hit an exception.
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699] Traceback (most recent call last):
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm/vllm/v1/executor/multiproc_executor.py", line 694, in worker_busy_loop
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     output = func(*args, **kwargs)
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 332, in compile_or_warm_up_model
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     self.model_runner.capture_model()
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 4075, in capture_model
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     self._capture_model()
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 4013, in _capture_model
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     self._capture_aclgraphs(
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3987, in _capture_aclgraphs
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     self._dummy_run(num_tokens,
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/opt/miniconda/envs/thinker/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     return func(*args, **kwargs)
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2899, in _dummy_run
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     hidden_states = self._generate_dummy_run_hidden_states(
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2703, in _generate_dummy_run_hidden_states
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     hidden_states = self.model(input_ids=input_ids,
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/opt/miniconda/envs/thinker/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     return self._call_impl(*args, **kwargs)
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/opt/miniconda/envs/thinker/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     return forward_call(*args, **kwargs)
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 1405, in forward
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     hidden_states = self.language_model.model(
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm/vllm/compilation/decorators.py", line 415, in __call__
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     model_output = self.forward(*args, **kwargs)
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm/vllm/model_executor/models/qwen3_omni_moe_thinker.py", line 604, in forward
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     def forward(
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/opt/miniconda/envs/thinker/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 838, in _fn
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     return fn(*args, **kwargs)
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm/vllm/compilation/caching.py", line 53, in __call__
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     return self.optimized_call(*args, **kwargs)
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/opt/miniconda/envs/thinker/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     return self._wrapped_call(self, *args, **kwargs)
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/opt/miniconda/envs/thinker/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     raise e
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/opt/miniconda/envs/thinker/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/opt/miniconda/envs/thinker/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     return self._call_impl(*args, **kwargs)
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/opt/miniconda/envs/thinker/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     return forward_call(*args, **kwargs)
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "<eval_with_key>.98", line 354, in forward
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     submod_2 = self.submod_2(getitem_3, s0, l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_, l_inputs_embeds_, l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_mlp_modules_gate_parameters_weight_, l_deepstack_input_embeds_tensors_deepstack_input_embeds_0_, l_self_modules_layers_modules_1_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_q_norm_parameters_weight_, l_self_modules_layers_modules_1_modules_self_attn_modules_k_norm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_, l_positions_, s2);  getitem_3 = l_self_modules_layers_modules_0_modules_self_attn_modules_o_proj_parameters_weight_ = l_inputs_embeds_ = l_self_modules_layers_modules_0_modules_post_attention_layernorm_parameters_weight_ = l_self_modules_layers_modules_0_modules_mlp_modules_gate_parameters_weight_ = l_deepstack_input_embeds_tensors_deepstack_input_embeds_0_ = l_self_modules_layers_modules_1_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_qkv_proj_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_q_norm_parameters_weight_ = l_self_modules_layers_modules_1_modules_self_attn_modules_k_norm_parameters_weight_ = None
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm-ascend/vllm_ascend/compilation/acl_graph.py", line 158, in __call__
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     output = self.runnable(*args, **kwargs)
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm/vllm/compilation/piecewise_backend.py", line 99, in __call__
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     return self.compiled_graph_for_general_shape(*args)
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/opt/miniconda/envs/thinker/lib/python3.11/site-packages/torch/fx/graph_module.py", line 830, in call_wrapped
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     return self._wrapped_call(self, *args, **kwargs)
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/opt/miniconda/envs/thinker/lib/python3.11/site-packages/torch/fx/graph_module.py", line 406, in __call__
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     raise e
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/opt/miniconda/envs/thinker/lib/python3.11/site-packages/torch/fx/graph_module.py", line 393, in __call__
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/opt/miniconda/envs/thinker/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     return self._call_impl(*args, **kwargs)
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/opt/miniconda/envs/thinker/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1762, in _call_impl
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     return forward_call(*args, **kwargs)
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "<eval_with_key>.3", line 16, in forward
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     moe_forward = torch.ops.vllm.moe_forward(view_1, linear_1, 'language_model.model.layers.0.mlp.experts');  view_1 = linear_1 = None
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/opt/miniconda/envs/thinker/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     return self._op(*args, **(kwargs or {}))
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 2593, in moe_forward
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     return self.forward_impl(hidden_states, router_logits)
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm-ascend/vllm_ascend/ops/fused_moe/fused_moe.py", line 340, in forward_impl
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     final_hidden_states = self.quant_method.apply(
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]                           ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm-ascend/vllm_ascend/ops/fused_moe/fused_moe.py", line 155, in apply
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     return moe_comm_method.fused_experts(
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm-ascend/vllm_ascend/ops/fused_moe/moe_comm_method.py", line 121, in fused_experts
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     results = self.token_dispatcher.token_dispatch(
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm-ascend/vllm_ascend/ops/fused_moe/token_dispatcher.py", line 536, in token_dispatch
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     ) = self._dispatch_preprocess(hidden_states, topk_ids)
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm-ascend/vllm_ascend/ops/fused_moe/token_dispatcher.py", line 616, in _dispatch_preprocess
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     ) = self._preprocess(topk_ids)
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]         ^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]   File "/workspace/thinker-2/vllm-ascend/vllm_ascend/ops/fused_moe/token_dispatcher.py", line 670, in _preprocess
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]     global_input_tokens_local_experts_indices = torch.repeat_interleave(
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]                                                 ^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699] RuntimeError: operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:47 NPU function error: c10_npu::acl::AclrtSynchronizeStreamWithTimeout(copy_stream), error code is 107027
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699] [ERROR] 2025-11-03-13:19:43 (PID:6956, Device:1, RankID:-1) ERR00100 PTA call acl api failed.
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699] EE9999: Inner Error!
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699] EE9999: [PID: 6956] 2025-11-03-13:19:43.628.317 Not allow to synchronize captured-stream, stream_id=9.[FUNC:StreamSynchronize][FILE:api_error.cc][LINE:960]
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]         TraceBack (most recent call last):
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]        rtStreamSynchronizeWithTimeout execute failed, reason=[stream is captured][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]        synchronize stream failed, runtime result = 107027[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(Worker_TP1_EP1 pid=6956) ERROR 11-03 13:19:43 [multiproc_executor.py:699]
```
