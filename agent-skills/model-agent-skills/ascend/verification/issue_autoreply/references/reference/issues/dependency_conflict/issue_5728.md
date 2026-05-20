# Issue #5728: [Bug]: Qwen-Image NPU Inference

## 基本信息

- **编号**: #5728
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5728
- **创建时间**: 2026-01-08T09:56:07Z
- **关闭时间**: 2026-01-08T10:01:46Z
- **更新时间**: 2026-01-08T10:02:02Z
- **提交者**: @May-Z-H
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

Collecting environment information...
==============================
        System Info
==============================
OS                           : Ubuntu 22.04.5 LTS (aarch64)
GCC version                  : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version                : Could not collect
CMake version                : version 4.2.0
Libc version                 : glibc-2.35

==============================
       PyTorch Info
==============================
PyTorch version              : 2.8.0+cpu
Is debug build               : False
CUDA used to build PyTorch   : None
ROCM used to build PyTorch   : N/A

==============================
      Python Environment
==============================
Python version               : 3.11.13 (main, Nov 20 2025, 16:02:27) [GCC 11.4.0] (64-bit runtime)
Python platform              : Linux-5.10.0-136.12.0.86.r1526_92.hce2.aarch64-aarch64-with-glibc2.35

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
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         Kunpeng-920
BIOS Model name:                    HUAWEI Kunpeng 920 5250
Model:                              0
Thread(s) per core:                 1
Core(s) per socket:                 48
Socket(s):                          4
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

==============================
Versions of relevant libraries
==============================
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.1
[pip3] triton-ascend==3.2.0.dev2025123114
[conda] Could not collect

==============================
         vLLM Info
==============================
ROCM Version                 : Could not collect
vLLM Version                 : 0.12.0
vLLM Build Flags:
  CUDA Archs: Not Set; ROCm: Disabled
GPU Topology:
  Could not collect

==============================
     Environment Variables
==============================
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1

### 🐛 Describe the bug


`python examples/offline_inference/text_to_image/text_to_image.py \
  --model /home/models/Qwen-Image \
  --prompt "a cup of coffee on the table" \
  --seed 42 \
  --cfg_scale 4.0 \
  --num_images_per_prompt 1 \
  --num_inference_steps 20 \
  --height 1024 \
  --width 1024 \
  --output outputs/coffee.png \
  --cache_backend cache_dit
`
examples/offline_inference/text_to_image/text_to_image.py #146

`   omni.generate(args.prompt)
    print("warm up.......")
    generation_start = time.perf_counter()
    outputs = omni.generate(
        args.prompt,
        negative_prompt=args.negative_prompt,
        height=args.height,
        width=args.width,
        generator=generator,
        true_cfg_scale=args.cfg_scale,
        guidance_scale=args.guidance_scale,
        num_inference_steps=args.num_inference_steps,
        num_outputs_per_prompt=args.num_images_per_prompt,
    )
    generation_end = time.perf_counter()
    generation_time = generation_end - generation_start`

**Logs are no longer being printed, and there are no processes on the card. The detailed log is as follows**
`INFO 01-08 17:29:58 [omni.py:711] [Summary] {'e2e_requests': 1,████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:38<00:00, 38.95s/img, est. speed stage-0 img/s: 0.00, avg e2e_lat: 0.0ms]
INFO 01-08 17:29:58 [omni.py:711]  'e2e_total_time_ms': 38948.00567626953,
INFO 01-08 17:29:58 [omni.py:711]  'e2e_sum_time_ms': 38946.76733016968,
INFO 01-08 17:29:58 [omni.py:711]  'e2e_total_tokens': 0,
INFO 01-08 17:29:58 [omni.py:711]  'e2e_avg_time_per_request_ms': 38946.76733016968,
INFO 01-08 17:29:58 [omni.py:711]  'e2e_avg_tokens_per_s': 0.0,
INFO 01-08 17:29:58 [omni.py:711]  'wall_time_ms': 38948.00567626953,
INFO 01-08 17:29:58 [omni.py:711]  'final_stage_id': {'0_429f04f5-c042-4898-b4c6-f15b80b59b90': 0},
INFO 01-08 17:29:58 [omni.py:711]  'stages': [{'stage_id': 0,
INFO 01-08 17:29:58 [omni.py:711]              'requests': 1,
INFO 01-08 17:29:58 [omni.py:711]              'tokens': 0,
INFO 01-08 17:29:58 [omni.py:711]              'total_time_ms': 38947.049617767334,
INFO 01-08 17:29:58 [omni.py:711]              'avg_time_per_request_ms': 38947.049617767334,
INFO 01-08 17:29:58 [omni.py:711]              'avg_tokens_per_s': 0.0}],
INFO 01-08 17:29:58 [omni.py:711]  'transfers': []}
Adding requests:   0%|                                                                                                                                                                                                                                  | 0/1 [00:38<?, ?it/s]
[Stage-0] INFO 01-08 17:29:58 [omni_stage.py:636] Received shutdown signal
[Stage-0] INFO 01-08 17:29:58 [gpu_worker.py:265] Worker 0: Received shutdown message
[Stage-0] INFO 01-08 17:29:58 [gpu_worker.py:287] event loop terminated.
[Stage-0] INFO 01-08 17:29:58 [npu_worker.py:126] Worker 0: Shutdown complete.
warm up.......
Adding requests:   0%|                                                                                                                                                                                                                                  | 0/1 [00:00<?, ?it/scorrupted size vs. prev_size                                                                                                                                                                         | 0/1 [00:00<?, ?it/s, est. speed input: 0.00 unit/s, output: 0.00 unit/s`

