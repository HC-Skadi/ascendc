# Issue #5451: [Bug]: Can't recognize the PDF screenshot including many box

## 基本信息

- **编号**: #5451
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5451
- **创建时间**: 2025-12-28T15:06:12Z
- **关闭时间**: 2025-12-28T15:09:11Z
- **更新时间**: 2025-12-29T08:55:30Z
- **提交者**: @dpdpbj
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
root@36939e3863fd:/vllm-workspace# python3 collect_env.py 
Collecting environment information...
==============================
        System Info
==============================
OS                           : Ubuntu 22.04.5 LTS (x86_64)
GCC version                  : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version                : Could not collect
CMake version                : version 4.1.0
Libc version                 : glibc-2.35

==============================
       PyTorch Info
==============================
PyTorch version              : 2.7.1+cu128
Is debug build               : False
CUDA used to build PyTorch   : 12.8
ROCM used to build PyTorch   : N/A

==============================
      Python Environment
==============================
Python version               : 3.12.11 (main, Jun  4 2025, 08:56:18) [GCC 11.4.0] (64-bit runtime)
Python platform              : Linux-5.15.0-140-generic-x86_64-with-glibc2.35

==============================
       CUDA / GPU Info
==============================
Is CUDA available            : True
CUDA runtime version         : 12.8.93
CUDA_MODULE_LOADING set to   : LAZY
GPU models and configuration : 
GPU 0: NVIDIA A100-SXM4-40GB
GPU 1: NVIDIA A100-SXM4-40GB

Nvidia driver version        : 560.35.03
cuDNN version                : Could not collect
HIP runtime version          : N/A
MIOpen runtime version       : N/A
Is XNNPACK available         : True

==============================
          CPU Info
==============================
Architecture:                         x86_64
CPU op-mode(s):                       32-bit, 64-bit
Address sizes:                        48 bits physical, 48 bits virtual
Byte Order:                           Little Endian
CPU(s):                               32
On-line CPU(s) list:                  0-31
Vendor ID:                            AuthenticAMD
Model name:                           AMD EPYC 7642 48-Core Processor
CPU family:                           23
Model:                                49
Thread(s) per core:                   1
Core(s) per socket:                   32
Socket(s):                            1
Stepping:                             0
BogoMIPS:                             4599.99
Flags:                                fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm rep_good nopl cpuid extd_apicid tsc_known_freq pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm cmp_legacy svm cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw perfctr_core ssbd ibrs ibpb stibp vmmcall fsgsbase tsc_adjust bmi1 avx2 smep bmi2 rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves clzero xsaveerptr wbnoinvd arat npt lbrv nrip_save tsc_scale vmcb_clean v_vmsave_vmload umip rdpid arch_capabilities
Virtualization:                       AMD-V
Hypervisor vendor:                    KVM
Virtualization type:                  full
L1d cache:                            2 MiB (32 instances)
L1i cache:                            2 MiB (32 instances)
L2 cache:                             16 MiB (32 instances)
L3 cache:                             512 MiB (32 instances)
NUMA node(s):                         1
NUMA node0 CPU(s):                    0-31
Vulnerability Gather data sampling:   Not affected
Vulnerability Itlb multihit:          Not affected
Vulnerability L1tf:                   Not affected
Vulnerability Mds:                    Not affected
Vulnerability Meltdown:               Not affected
Vulnerability Mmio stale data:        Not affected
Vulnerability Reg file data sampling: Not affected
Vulnerability Retbleed:               Mitigation; untrained return thunk; SMT disabled
Vulnerability Spec rstack overflow:   Mitigation; SMT disabled
Vulnerability Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl and seccomp
Vulnerability Spectre v1:             Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:             Mitigation; Retpolines; IBPB conditional; STIBP disabled; RSB filling; PBRSB-eIBRS Not affected; BHI Not affected
Vulnerability Srbds:                  Not affected
Vulnerability Tsx async abort:        Not affected

==============================
Versions of relevant libraries
==============================
[pip3] numpy==2.2.6
[pip3] nvidia-cublas-cu12==12.8.3.14
[pip3] nvidia-cuda-cupti-cu12==12.8.57
[pip3] nvidia-cuda-nvrtc-cu12==12.8.61
[pip3] nvidia-cuda-runtime-cu12==12.8.57
[pip3] nvidia-cudnn-cu12==9.7.1.26
[pip3] nvidia-cufft-cu12==11.3.3.41
[pip3] nvidia-cufile-cu12==1.13.0.11
[pip3] nvidia-curand-cu12==10.3.9.55
[pip3] nvidia-cusolver-cu12==11.7.2.55
[pip3] nvidia-cusparse-cu12==12.5.7.53
[pip3] nvidia-cusparselt-cu12==0.6.3
[pip3] nvidia-nccl-cu12==2.26.2
[pip3] nvidia-nvjitlink-cu12==12.8.61
[pip3] nvidia-nvtx-cu12==12.8.55
[pip3] onnxruntime==1.23.2
[pip3] pyzmq==27.0.1
[pip3] torch==2.7.1+cu128
[pip3] torchaudio==2.7.1+cu128
[pip3] torchvision==0.22.1+cu128
[pip3] transformers==4.55.2
[pip3] triton==3.3.1
[conda] Could not collect

==============================
         vLLM Info
==============================
ROCM Version                 : Could not collect
Neuron SDK Version           : N/A
vLLM Version                 : 0.10.1.1
vLLM Build Flags:
  CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled
GPU Topology:
        GPU0    GPU1    CPU Affinity    NUMA Affinity   GPU NUMA ID
GPU0     X      PHB     0-31    0               N/A
GPU1    PHB      X      0-31    0               N/A

Legend:

  X    = Self
  SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)
  NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node
  PHB  = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU)
  PXB  = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge)
  PIX  = Connection traversing at most a single PCIe bridge
  NV#  = Connection traversing a bonded set of # NVLinks

==============================
     Environment Variables
==============================
NVIDIA_VISIBLE_DEVICES=all
NVIDIA_REQUIRE_CUDA=cuda>=12.8 brand=unknown,driver>=470,driver<471 brand=grid,driver>=470,driver<471 brand=tesla,driver>=470,driver<471 brand=nvidia,driver>=470,driver<471 brand=quadro,driver>=470,driver<471 brand=quadrortx,driver>=470,driver<471 brand=nvidiartx,driver>=470,driver<471 brand=vapps,driver>=470,driver<471 brand=vpc,driver>=470,driver<471 brand=vcs,driver>=470,driver<471 brand=vws,driver>=470,driver<471 brand=cloudgaming,driver>=470,driver<471 brand=unknown,driver>=535,driver<536 brand=grid,driver>=535,driver<536 brand=tesla,driver>=535,driver<536 brand=nvidia,driver>=535,driver<536 brand=quadro,driver>=535,driver<536 brand=quadrortx,driver>=535,driver<536 brand=nvidiartx,driver>=535,driver<536 brand=vapps,driver>=535,driver<536 brand=vpc,driver>=535,driver<536 brand=vcs,driver>=535,driver<536 brand=vws,driver>=535,driver<536 brand=cloudgaming,driver>=535,driver<536 brand=unknown,driver>=550,driver<551 brand=grid,driver>=550,driver<551 brand=tesla,driver>=550,driver<551 brand=nvidia,driver>=550,driver<551 brand=quadro,driver>=550,driver<551 brand=quadrortx,driver>=550,driver<551 brand=nvidiartx,driver>=550,driver<551 brand=vapps,driver>=550,driver<551 brand=vpc,driver>=550,driver<551 brand=vcs,driver>=550,driver<551 brand=vws,driver>=550,driver<551 brand=cloudgaming,driver>=550,driver<551 brand=unknown,driver>=560,driver<561 brand=grid,driver>=560,driver<561 brand=tesla,driver>=560,driver<561 brand=nvidia,driver>=560,driver<561 brand=quadro,driver>=560,driver<561 brand=quadrortx,driver>=560,driver<561 brand=nvidiartx,driver>=560,driver<561 brand=vapps,driver>=560,driver<561 brand=vpc,driver>=560,driver<561 brand=vcs,driver>=560,driver<561 brand=vws,driver>=560,driver<561 brand=cloudgaming,driver>=560,driver<561 brand=unknown,driver>=565,driver<566 brand=grid,driver>=565,driver<566 brand=tesla,driver>=565,driver<566 brand=nvidia,driver>=565,driver<566 brand=quadro,driver>=565,driver<566 brand=quadrortx,driver>=565,driver<566 brand=nvidiartx,driver>=565,driver<566 brand=vapps,driver>=565,driver<566 brand=vpc,driver>=565,driver<566 brand=vcs,driver>=565,driver<566 brand=vws,driver>=565,driver<566 brand=cloudgaming,driver>=565,driver<566
NCCL_VERSION=2.25.1-1
NVIDIA_DRIVER_CAPABILITIES=compute,utility
NVIDIA_PRODUCT_NAME=CUDA
VLLM_USAGE_SOURCE=production-docker-image
CUDA_VERSION=12.8.1
CUDA_VISIBLE_DEVICES=0,1
CUDA_VISIBLE_DEVICES=0,1
LD_LIBRARY_PATH=/usr/local/cuda/lib64
NCCL_CUMEM_ENABLE=0
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1
CUDA_MODULE_LOADING=LAZY
```

</details>


### 🐛 Describe the bug
Upload following png file to MinerU.
<img width="1312" height="1884" alt="Image" src="https://github.com/user-attachments/assets/f81a7f53-1c86-4759-82ca-4280707d3a42" />

I tried the pipeline backend or vlm backend, but the information can't be extraced from the complex table. When I checkd the .md file generated by MinerU， so many `<td>`label in md file. for example:

```
# 香港特別行政區政府入境事務處 Immigration Department, the Government of the Hong Kong Special Administrative Region 從外國聘用家庭傭工申請表(由僱主填寫) Application for Employment of Domestic Helper from Abroad (to be completed by the employer)

![](images/34646abfbd23694c5691405c59b9f2cfa7b01fd4b96d901d5c0c7e8e4424fba4.jpg)

注意：(i) 僅主填寫本表格前請參閱「從外國聘用家庭傭工指南」[ID(C)969]。

Note: Employers are advised to read "Guidebook for the Employment of Domestic Helpers from Abroad" [ID(E) 969] before completing this form.

(ii) 領取本表格無須繳費。 This form is issued free of charge.   
(iii) 請用黑色或藍色筆以正楷填寫本表格。Please complete this form in BLOCK letters using black or blue pen.   
(iv) 請在適當方格內填上「√」號。 Please tick as appropriate.

此欄由辦理機關處理

FOR OFFICIAL USE ONLY

檔案條碼 Reference barcode

![](images/62e9c8dea91289ffb1bf6654cb9a554993802624fade541ed60d60a47d628998.jpg)

<table><tr><td colspan="101">1.在港的僱主資料 Particulars of Employer in Hong Kong</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>
```

I also uploaded the zip file.

<img width="1075" height="1388" alt="Image" src="https://github.com/user-attachments/assets/a61d3040-51ad-4d13-b721-3dc1d06c7a74" />

[60a70362620f9efea8d43a1db803f34dc9a05bad849dee6051138d9c6abaa69d.zip](https://github.com/user-attachments/files/24360541/60a70362620f9efea8d43a1db803f34dc9a05bad849dee6051138d9c6abaa69d.zip)
