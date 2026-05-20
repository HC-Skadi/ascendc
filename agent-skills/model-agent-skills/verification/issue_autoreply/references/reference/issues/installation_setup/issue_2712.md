# Issue #2712: [Bug]:  设置pipeline-parallel-size推理时显示通信问题；create_config:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:148 HCCL function error: hcclCommInitRootInfoConfig(numRanks, &rootInfo, rank, config, &(comm->hcclComm_)), error code is 1

## 基本信息

- **编号**: #2712
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2712
- **创建时间**: 2025-09-03T03:14:03Z
- **关闭时间**: 2025-12-23T12:06:26Z
- **更新时间**: 2025-12-23T12:06:26Z
- **提交者**: @zhuyingying-byte
- **评论数**: 2

## 标签

310p

## 问题描述

### Your current environment
 npu环境：
```
+--------------------------------------------------------------------------------------------------------+
| npu-smi 25.2.0                                   Version: 25.2.0                                       |
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Name                  | Health          | Power(W)     Temp(C)           Hugepages-Usage(page) |
| Chip    Device                | Bus-Id          | AICore(%)    Memory-Usage(MB)                        |
+===============================+=================+======================================================+
| 0       310P3                 | OK              | NA           48                0     / 0             |
| 0       0                     | 0000:01:00.0    | 0            1851 / 21527                            |
+===============================+=================+======================================================+
| 32      310P3                 | OK              | NA           50                0     / 0             |
| 0       1                     | 0000:02:00.0    | 0            1852 / 21527                            |
+===============================+=================+======================================================+
| 96      310P3                 | OK              | NA           52                0     / 0             |
| 0       2                     | 0000:04:00.0    | 0            1851 / 21527                            |
+===============================+=================+======================================================+
| 32768   310P3                 | OK              | NA           50                0     / 0             |
| 0       3                     | 0000:81:00.0    | 0            1852 / 21527                            |
+===============================+=================+======================================================+
| 32800   310P3                 | OK              | NA           53                0     / 0             |
| 0       4                     | 0000:82:00.0    | 0            1853 / 21527                            |
+===============================+=================+======================================================+
| 32896   310P3                 | OK              | NA           52                0     / 0             |
| 0       5                     | 0000:85:00.0    | 0            1853 / 21527                            |
+===============================+=================+======================================================+
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Chip                  | Process id      | Process name             | Process memory(MB)        |
+===============================+=================+======================================================+
| No running processes found in NPU 0                                                                    |
+===============================+=================+======================================================+
| No running processes found in NPU 32                                                                   |
+===============================+=================+======================================================+
| No running processes found in NPU 96                                                                   |
+===============================+=================+======================================================+
| No running processes found in NPU 32768                                                                |
+===============================+=================+======================================================+
| No running processes found in NPU 32800                                                                |
+===============================+=================+======================================================+
| No running processes found in NPU 32896                                                                |
+===============================+=================+======================================================+
```
#驱动环境：
```
package_name=Ascend-cann-toolkit
version=8.2.RC1
innerversion=V100R001C22SPC001B231
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux
```
#其他环境：
```
==============================
        System Info
==============================
OS                           : Ubuntu 22.04.5 LTS (aarch64)
GCC version                  : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version                : Could not collect
CMake version                : version 4.0.3
Libc version                 : glibc-2.35

==============================
       PyTorch Info
==============================
PyTorch version              : 2.5.1
Is debug build               : False
CUDA used to build PyTorch   : None
ROCM used to build PyTorch   : N/A

==============================
      Python Environment
==============================
Python version               : 3.10.17 (main, May 27 2025, 01:33:16) [GCC 11.4.0] (64-bit runtime)
Python platform              : Linux-4.19.90-2102.2.0.0062.ctl2.aarch64-aarch64-with-glibc2.35

==============================
       CUDA / GPU Info
==============================
Is CUDA available            : False
CUDA runtime version         : No CUDA
CUDA_MODULE_LOADING set to   : N/A
GPU models and configuration : No CUDA
Nvidia driver version        : No CUDA
cuDNN version                : No CUDA
HIP runtime version          : N/A
MIOpen runtime version       : N/A
Is XNNPACK available         : True

==============================
          CPU Info
==============================
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          128
On-line CPU(s) list:             0-127
Vendor ID:                       HiSilicon
Model name:                      Kunpeng-920
Model:                           0
Thread(s) per core:              1
Core(s) per cluster:             64
Socket(s):                       -
Cluster(s):                      2
Stepping:                        0x1
CPU max MHz:                     2600.0000
CPU min MHz:                     200.0000
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm
L1d cache:                       8 MiB (128 instances)
L1i cache:                       8 MiB (128 instances)
L2 cache:                        64 MiB (128 instances)
L3 cache:                        128 MiB (4 instances)
NUMA node(s):                    4
NUMA node0 CPU(s):               0-31
NUMA node1 CPU(s):               32-63
NUMA node2 CPU(s):               64-95
NUMA node3 CPU(s):               96-127
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Vulnerable
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

==============================
Versions of relevant libraries
==============================
[pip3] numpy==1.26.4
[pip3] pyzmq==27.0.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.post1.dev20250619
[pip3] torchvision==0.20.1
[pip3] transformers==4.52.4
[conda] Could not collect

==============================
         vLLM Info
==============================
ROCM Version                 : Could not collect
Neuron SDK Version           : N/A
vLLM Version                 : 0.9.2
vLLM Build Flags:
  CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled
GPU Topology:
  Could not collect

==============================
     Environment Variables
==============================
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
TORCH_DEVICE_BACKEND_AUTOLOAD=1
NCCL_CUMEM_ENABLE=0
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1
```
# 容器启动命令：
```
export VLLM_IMAGE=quay.io/ascend/vllm-ascend:v0.9.2rc1-310p
docker run --rm \
--name vllm-ascend \
--network=host \
--device /dev/davinci0 \
--device /dev/davinci2 \
--device /dev/davinci4 \
--device /dev/davinci6 \
--device /dev/davinci8 \
--device /dev/davinci10 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend:/usr/local/Ascend \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-v /home/models/:/workspace \
-v /home/HwHiAiUser/zhuyy4/:/workspace/test \
-p  8000:8000 \
-it $VLLM_IMAGE bash
```
# 服务启动命令：
```
vllm serve /workspace/Qwen2.5-VL-32B-Instruct --tensor-parallel-size 1 --pipeline-parallel-size 6 --enforce-eager --dtype float16 --max-model-len 4096 --gpu-memory-utilization 0.9 --allowed-local-media-path /workspace --compilation-config '{"custom_ops":["none", "+rms_norm", "+rotary_embedding"]}'
```
# 推理命令：
```
curl http://localhost:8000/v1/completions \
-H "Content-Type: application/json" \
-d '{
     "prompt": "The future of AI is",
     "max_tokens": 64,
     "top_p": 0.95,
     "top_k": 50,
     "temperature": 0.6
}'
```
# 推理报错信息：
INFO 09-03 03:00:37 [logger.py:43] Received request cmpl-2f5a65e708294fa3a135312f7221a591-0: prompt: 'The future of AI is', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.05, temperature=0.6, top_p=0.95, top_k=50, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=64, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None), prompt_token_ids: [785, 3853, 315, 15235, 374], prompt_embeds shape: None, lora_request: None, prompt_adapter_request: None.
INFO 09-03 03:00:37 [async_llm.py:270] Added request cmpl-2f5a65e708294fa3a135312f7221a591-0.
(VllmWorker rank=0 pid=7225) /vllm-workspace/vllm/vllm/distributed/parallel_state.py:489: UserWarning: The given buffer is not writable, and PyTorch does not support non-writable tensors. This means you can write to the underlying (supposedly non-writable) buffer using the tensor. You may want to copy the buffer to protect its data or make it writable before converting it to a tensor. This type of warning will be suppressed for the rest of this program. (Triggered internally at /pytorch/torch/csrc/utils/tensor_new.cpp:1560.)
(VllmWorker rank=0 pid=7225)   object_tensor = torch.frombuffer(pickle.dumps(obj), dtype=torch.uint8)
.[rank0]:[W903 03:02:37.426431790 compiler_depend.ts:164] Warning: Warning: Device do not support double dtype now, dtype cast repalce with float. (function operator())
(VllmWorker rank=0 pid=7225) ERROR 09-03 03:02:37 [multiproc_executor.py:522] WorkerProc hit an exception.
(VllmWorker rank=0 pid=7225) ERROR 09-03 03:02:37 [multiproc_executor.py:522] Traceback (most recent call last):
(VllmWorker rank=0 pid=7225) ERROR 09-03 03:02:37 [multiproc_executor.py:522]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 517, in worker_busy_loop
(VllmWorker rank=0 pid=7225) ERROR 09-03 03:02:37 [multiproc_executor.py:522]     output = func(*args, **kwargs)
(VllmWorker rank=0 pid=7225) ERROR 09-03 03:02:37 [multiproc_executor.py:522]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 223, in execute_model
(VllmWorker rank=0 pid=7225) ERROR 09-03 03:02:37 [multiproc_executor.py:522]     get_pp_group().send_tensor_dict(output.tensors,
(VllmWorker rank=0 pid=7225) ERROR 09-03 03:02:37 [multiproc_executor.py:522]   File "/vllm-workspace/vllm/vllm/distributed/parallel_state.py", line 678, in send_tensor_dict
(VllmWorker rank=0 pid=7225) ERROR 09-03 03:02:37 [multiproc_executor.py:522]     torch.distributed.send(tensor,
(VllmWorker rank=0 pid=7225) ERROR 09-03 03:02:37 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/distributed/c10d_logger.py", line 83, in wrapper
(VllmWorker rank=0 pid=7225) ERROR 09-03 03:02:37 [multiproc_executor.py:522]     return func(*args, **kwargs)
(VllmWorker rank=0 pid=7225) ERROR 09-03 03:02:37 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 2151, in send
(VllmWorker rank=0 pid=7225) ERROR 09-03 03:02:37 [multiproc_executor.py:522]     group.send([tensor], group_dst_rank, tag).wait()
(VllmWorker rank=0 pid=7225) ERROR 09-03 03:02:37 [multiproc_executor.py:522] RuntimeError: create_config:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:148 HCCL function error: hcclCommInitRootInfoConfig(numRanks, &rootInfo, rank, config, &(comm->hcclComm_)), error code is 1
(VllmWorker rank=0 pid=7225) ERROR 09-03 03:02:37 [multiproc_executor.py:522] [ERROR] 2025-09-03-03:02:37 (PID:7225, Device:0, RankID:-1) ERR02200 DIST call hccl api failed.
(VllmWorker rank=0 pid=7225) ERROR 09-03 03:02:37 [multiproc_executor.py:522] 
[rank1]:[W903 03:02:37.591197060 compiler_depend.ts:164] Warning: Warning: Device do not support double dtype now, dtype cast repalce with float. (function operator())
(VllmWorker rank=1 pid=7226) ERROR 09-03 03:02:37 [multiproc_executor.py:522] WorkerProc hit an exception.
(VllmWorker rank=1 pid=7226) ERROR 09-03 03:02:37 [multiproc_executor.py:522] Traceback (most recent call last):
(VllmWorker rank=1 pid=7226) ERROR 09-03 03:02:37 [multiproc_executor.py:522]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 517, in worker_busy_loop
(VllmWorker rank=1 pid=7226) ERROR 09-03 03:02:37 [multiproc_executor.py:522]     output = func(*args, **kwargs)
(VllmWorker rank=1 pid=7226) ERROR 09-03 03:02:37 [multiproc_executor.py:522]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 214, in execute_model
(VllmWorker rank=1 pid=7226) ERROR 09-03 03:02:37 [multiproc_executor.py:522]     get_pp_group().recv_tensor_dict(
(VllmWorker rank=1 pid=7226) ERROR 09-03 03:02:37 [multiproc_executor.py:522]   File "/vllm-workspace/vllm/vllm/distributed/parallel_state.py", line 735, in recv_tensor_dict
(VllmWorker rank=1 pid=7226) ERROR 09-03 03:02:37 [multiproc_executor.py:522]     torch.distributed.recv(tensor,
(VllmWorker rank=1 pid=7226) ERROR 09-03 03:02:37 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/distributed/c10d_logger.py", line 83, in wrapper
(VllmWorker rank=1 pid=7226) ERROR 09-03 03:02:37 [multiproc_executor.py:522]     return func(*args, **kwargs)
(VllmWorker rank=1 pid=7226) ERROR 09-03 03:02:37 [multiproc_executor.py:522]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 2203, in recv
(VllmWorker rank=1 pid=7226) ERROR 09-03 03:02:37 [multiproc_executor.py:522]     pg.recv([tensor], group_src_rank, tag).wait()
(VllmWorker rank=1 pid=7226) ERROR 09-03 03:02:37 [multiproc_executor.py:522] RuntimeError: create_config:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:148 HCCL function error: hcclCommInitRootInfoConfig(numRanks, &rootInfo, rank, config, &(comm->hcclComm_)), error code is 1
(VllmWorker rank=1 pid=7226) ERROR 09-03 03:02:37 [multiproc_executor.py:522] [ERROR] 2025-09-03-03:02:37 (PID:7226, Device:1, RankID:-1) ERR02200 DIST call hccl api failed.
(VllmWorker rank=1 pid=7226) ERROR 09-03 03:02:37 [multiproc_executor.py:522] 

# 其他信息：
用vllm serve /workspace/Qwen2.5-VL-7B-Instruct \
    --tensor-parallel-size 2 \
    --enforce-eager \
    --dtype float16 \
    --allowed-local-media-path /workspace \
    --compilation-config '{"custom_ops":["none", "+rms_norm", "+rotary_embedding"]}'
可以成功启动Qwen2.5VL-7B且能正常推理，但是用--tensor-parallel-size 1 --pipeline-parallel-size 3 会报和上面相同的错，不用pipeline-parallel-size，--tensor-parallel-size 4的时候启动32B会说显存不够, --tensor-parallel-size=5不能被text_encoder 16整除，=6 不能被vision_encoder整除。 1.对于RuntimeError: create_config:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:148 HCCL function error: hcclCommInitRootInfoConfig(numRanks, &rootInfo, rank, config, &(comm->hcclComm_)), error code is 1 这个问题应该怎么做才能解决问题呢？（此外error_code=1 是什么问题，有什么文档或者网站可以知道error_code分别表示什么吗？）
```
### How would you like to use vllm on ascend

vllm serve /workspace/Qwen2.5-VL-32B-Instruct --tensor-parallel-size 1 --pipeline-parallel-size 6 --enforce-eager --dtype float16 --allowed-local-media-path /workspace --compilation-config '{"custom_ops":["none", "+rms_norm", "+rotary_embedding"]}' 希望这样启动后能正常推理。

