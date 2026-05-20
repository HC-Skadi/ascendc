# Issue #1464: [Bug]:  Lora feature cannot be used in Aclgraph mode

## 基本信息

- **编号**: #1464
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1464
- **创建时间**: 2025-06-26T12:00:44Z
- **关闭时间**: 2025-08-19T02:31:48Z
- **更新时间**: 2025-08-19T02:31:48Z
- **提交者**: @NNUCJ
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 3.22.1
Libc version: glibc-2.35

Python version: 3.11.10 (main, May 10 2025, 15:46:23) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-216.0.0.115.oe2203sp4.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             640
On-line CPU(s) list:                0-639
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
BIOS Model name:                    Kunpeng 920 7285Z
Model:                              0
Thread(s) per core:                 2
Core(s) per socket:                 80
Socket(s):                          4
Stepping:                           0x0
Frequency boost:                    disabled
CPU max MHz:                        3000.0000
CPU min MHz:                        400.0000
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs sb dcpodp flagm2 frint svei8mm svef32mm svef64mm svebf16 i8mm bf16 dgh rng ecv
L1d cache:                          20 MiB (320 instances)
L1i cache:                          20 MiB (320 instances)
L2 cache:                           400 MiB (320 instances)
L3 cache:                           560 MiB (8 instances)
NUMA node(s):                       8
NUMA node0 CPU(s):                  0-79
NUMA node1 CPU(s):                  80-159
NUMA node2 CPU(s):                  160-239
NUMA node3 CPU(s):                  240-319
NUMA node4 CPU(s):                  320-399
NUMA node5 CPU(s):                  400-479
NUMA node6 CPU(s):                  480-559
NUMA node7 CPU(s):                  560-639
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
[pip3] mindietorch==2.1rc1+torch2.1.0.abi0
[pip3] numpy==1.26.4
[pip3] onnx==1.18.0
[pip3] pyzmq==27.0.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.post1.dev20250619
[pip3] torchvision==0.16.0
[pip3] transformers==4.52.4
[conda] Could not collect
vLLM Version: 0.9.1
vLLM Ascend Version: 0.9.0rc2.dev33+gbf17152 (git sha: bf17152)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=16
ATB_LOG_TO_FILE_FLUSH=0
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_SLOG_PRINT_TO_STDOUT=0
ASCEND_GLOBAL_EVENT_ENABLE=0
ATB_CONTEXT_HOSTTILING_RING=1
ATB_OPERATION_EXECUTE_ASYNC=1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_CONTEXT_HOSTTILING_SIZE=102400
ASCEND_GLOBAL_LOG_LEVEL=3
ASCEND_CUSTOM_OPP_PATH=/usr/local/Ascend/mindie/latest/mindie-rt/ops/vendors/aie_ascendc:/usr/local/Ascend/mindie/latest/mindie-rt/ops/vendors/customize:
PYTORCH_INSTALL_PATH=/usr/local/lib/python3.11/site-packages/torch
PYTORCH_NPU_INSTALL_PATH=/usr/local/lib/python3.11/site-packages/torch_npu
ATB_SPEED_HOME_PATH=/usr/local/Ascend/atb-models
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/lib:/lib:/usr/local/Ascend/atb-models/lib:/usr/local/Ascend/mindie/latest/mindie-llm/lib:/usr/local/Ascend/mindie/latest/mindie-llm/lib/grpc:/usr/local/Ascend/mindie/latest/mindie-service/lib:/usr/local/Ascend/mindie/latest/mindie-service/lib/grpc:/usr/local/Ascend/mindie/latest/mindie-torch/lib:/usr/local/Ascend/mindie/latest/mindie-rt/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_USE_TILING_COPY_STREAM=0
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1
CANN:
package_name=Ascend-cann-toolkit
version=8.2.RC1
innerversion=V100R001C22B079
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux
```

</details>


### 🐛 Describe the bug

Use the following shell script to enable the lora feature and stack aclgraph to launch online services
```shell
export VLLM_USE_V1=1
vllm serve Qwen2.5-7B-Instruct \
    --tensor-parallel-size 4 \
    --additional-config '{"ascend_scheduler_config":{"enabled":true}}' \
    --enable-lora \
    --lora-modules lora1=Komodo-LoRA lora2=Komodo-LoRA

```
&emsp;&emsp; Detailed error information
```text
ee doc below for more guidance.
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] 
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] Potential framework code culprit (scroll up for full backtrace):
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/usr/local/lib/python3.11/site-packages/torch/_ops.py", line 759, in decompose
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     return self._op_dk(dk, *args, **kwargs)
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] 
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] For more information, run with TORCH_LOGS="dynamic"
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] For extended logs when we create symbols, also add TORCHDYNAMO_EXTENDED_DEBUG_CREATE_SYMBOL="u0"
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] If you suspect the guard was triggered from C++, add TORCHDYNAMO_EXTENDED_DEBUG_CPP=1
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] For more debugging help, see https://docs.google.com/document/d/1HSuTTVvYH1pTew89Rtpeu84Ht3nQEFTYhAX3Ypa_xJs/edit?usp=sharing
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] 
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] User Stack (most recent call last):
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   (snipped, see stack below for prefix)
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm/vllm/model_executor/models/qwen2.py", line 354, in forward
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     hidden_states, residual = layer(
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm/vllm/model_executor/models/qwen2.py", line 253, in forward
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     hidden_states = self.self_attn(
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm/vllm/model_executor/models/qwen2.py", line 180, in forward
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     qkv, _ = self.qkv_proj(hidden_states)
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm/vllm/lora/layers.py", line 581, in forward
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     output_parallel = self.apply(input_, bias)
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm/vllm/lora/layers.py", line 422, in apply
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     torch.Tensor] = self.punica_wrapper.add_lora_linear(
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm-ascend/vllm_ascend/lora/punica_wrapper/punica_npu.py", line 296, in add_lora_linear
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     self.add_shrink(buffer, x, lora_a_stacked, scale, **kwargs)
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm-ascend/vllm_ascend/lora/punica_wrapper/punica_npu.py", line 175, in add_shrink
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     self._apply_shrink(y[slice_idx], x, lora_a_stacked[slice_idx],
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm-ascend/vllm_ascend/lora/punica_wrapper/punica_npu.py", line 148, in _apply_shrink
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     shrink_fun(y, x, w_t_all, scale)
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm-ascend/vllm_ascend/lora/punica_wrapper/punica_npu.py", line 36, in _shrink_prefill
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     sgmv_shrink(
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm/vllm/lora/ops/torch_ops/lora_ops.py", line 64, in sgmv_shrink
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     bgmv_shrink(inputs, lora_a_weights, output_tensor, exploded_indices,
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm/vllm/lora/ops/torch_ops/lora_ops.py", line 78, in bgmv_shrink
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     outputs = torch.einsum("bi, boi -> bo", inputs, selected_loras)
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] 
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] For C++ stack trace, run with TORCHDYNAMO_EXTENDED_DEBUG_CPP=1
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] For more information about this error, see: https://pytorch.org/docs/main/generated/exportdb/index.html#constrain-as-size-example
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] 
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] from user code:
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]    File "/home/chengjie/vllm_dev_project/vllm/vllm/model_executor/models/qwen2.py", line 354, in forward
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     hidden_states, residual = layer(
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm/vllm/model_executor/models/qwen2.py", line 253, in forward
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     hidden_states = self.self_attn(
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm/vllm/model_executor/models/qwen2.py", line 180, in forward
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     qkv, _ = self.qkv_proj(hidden_states)
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm/vllm/lora/layers.py", line 581, in forward
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     output_parallel = self.apply(input_, bias)
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm/vllm/lora/layers.py", line 422, in apply
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     torch.Tensor] = self.punica_wrapper.add_lora_linear(
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm-ascend/vllm_ascend/lora/punica_wrapper/punica_npu.py", line 296, in add_lora_linear
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     self.add_shrink(buffer, x, lora_a_stacked, scale, **kwargs)
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm-ascend/vllm_ascend/lora/punica_wrapper/punica_npu.py", line 175, in add_shrink
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     self._apply_shrink(y[slice_idx], x, lora_a_stacked[slice_idx],
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm-ascend/vllm_ascend/lora/punica_wrapper/punica_npu.py", line 148, in _apply_shrink
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     shrink_fun(y, x, w_t_all, scale)
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm-ascend/vllm_ascend/lora/punica_wrapper/punica_npu.py", line 36, in _shrink_prefill
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     sgmv_shrink(
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm/vllm/lora/ops/torch_ops/lora_ops.py", line 64, in sgmv_shrink
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     bgmv_shrink(inputs, lora_a_weights, output_tensor, exploded_indices,
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]   File "/home/chengjie/vllm_dev_project/vllm/vllm/lora/ops/torch_ops/lora_ops.py", line 78, in bgmv_shrink
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527]     outputs = torch.einsum("bi, boi -> bo", inputs, selected_loras)
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] 
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] Set TORCH_LOGS="+dynamo" and TORCHDYNAMO_VERBOSE=1 for more information
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] 
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] 
(VllmWorker rank=0 pid=976407) ERROR 06-26 19:44:33 [multiproc_executor.py:527] You can suppress this exception and fall back to eager by setting:

```
