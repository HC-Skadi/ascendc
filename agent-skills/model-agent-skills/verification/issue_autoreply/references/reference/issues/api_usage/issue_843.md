# Issue #843: [Bug]: 使用--lora-modules字段加载lora模型效果不好

## 基本信息

- **编号**: #843
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/843
- **创建时间**: 2025-05-14T02:23:55Z
- **关闭时间**: 2025-06-17T12:53:00Z
- **更新时间**: 2025-07-03T09:06:06Z
- **提交者**: @joyhhheee
- **评论数**: 15

## 标签

question

## 问题描述

### Your current environment

<details>
<summary>/home/ma-user/anaconda3/envs/py310/lib/python3.10/site-packages/torch_npu/utils/collect_env.py:58: UserWarning: Warning: The /usr/local/Ascend/ascend-toolkit/latest owner does not match the current owner.
  warnings.warn(f"Warning: The {path} owner does not match the current owner.")
/home/ma-user/anaconda3/envs/py310/lib/python3.10/site-packages/torch_npu/utils/collect_env.py:58: UserWarning: Warning: The /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/ascend_toolkit_install.info owner does not match the current owner.
  warnings.warn(f"Warning: The {path} owner does not match the current owner.")
INFO 05-14 10:10:19 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-14 10:10:19 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
INFO 05-14 10:10:19 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-14 10:10:22 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-14 10:10:22 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-14 10:10:22 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-14 10:10:22 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-14 10:10:22 [__init__.py:44] plugin ascend loaded.
INFO 05-14 10:10:22 [__init__.py:230] Platform plugin ascend is activated
WARNING 05-14 10:10:24 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: EulerOS 2.0 (SP10) (aarch64)
GCC version: (conda-forge gcc 12.2.0-19) 12.2.0
Clang version: Could not collect
CMake version: version 4.0.0
Libc version: glibc-2.28

Python version: 3.10.6 | packaged by conda-forge | (main, Aug 22 2022, 20:27:42) [GCC 10.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-vhulk2211.3.0.h1543.eulerosv2r10.aarch64-aarch64-with-glibc2.28

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Thread(s) per core:              1
Core(s) per socket:              48
Socket(s):                       4
NUMA node(s):                    8
Vendor ID:                       HiSilicon
Model:                           0
Model name:                      Kunpeng-920
Stepping:                        0x1
BogoMIPS:                        200.00
L1d cache:                       12 MiB
L1i cache:                       12 MiB
L2 cache:                        96 MiB
L3 cache:                        192 MiB
NUMA node0 CPU(s):               0-23
NUMA node1 CPU(s):               24-47
NUMA node2 CPU(s):               48-71
NUMA node3 CPU(s):               72-95
NUMA node4 CPU(s):               96-119
NUMA node5 CPU(s):               120-143
NUMA node6 CPU(s):               144-167
NUMA node7 CPU(s):               168-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Mmio stale data:   Not affected
Vulnerability Retbleed:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] onnxruntime==1.21.1
[pip3] pyzmq==26.4.0
[pip3] sentence-transformers==4.1.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250320
[pip3] torchvision==0.20.1
[pip3] transformers==4.51.3
[conda] numpy                     1.26.4                    <pip>
[conda] pyzmq                     26.4.0                    <pip>
[conda] sentence-transformers     4.1.0                     <pip>
[conda] torch                     2.5.1                     <pip>
[conda] torch-npu                 2.5.1.dev20250320           <pip>
[conda] torchvision               0.20.1                    <pip>
[conda] transformers              4.51.3                    <pip>
vLLM Version: 0.1.dev1+gbdb2cdd (git sha: bdb2cdd)
vLLM Ascend Version: 0.8.4rc2.dev21+g3879d9c (git sha: 3879d9c)

ENV Variables:
ASCEND_VISIBLE_DEVICES=4,5,6,7
ASCEND_RUNTIME_OPTIONS=
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/toolbox/latest/Ascend-DMI/lib64:/usr/lib/aarch64-linux-gnu/hdf5/serial:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/:/usr/local/seccomponent/lib/:/usr/local/seccomponent/lib/openssl/:/usr/local/mindspore-lite/mindspore-lite-2.3.0-linux-aarch64/tools/converter/lib:/usr/local/mindspore-lite/mindspore-lite-2.3.0-linux-aarch64/runtime/lib:/usr/local/mindspore-lite/mindspore-lite-2.3.0-linux-aarch64/runtime/third_party/dnnl
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_AUTOML_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 23.0.6                   Version: 23.0.6                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 4     910B4               | OK            | 89.2        39                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          29096/ 32768         |
+===========================+===============+====================================================+
| 5     910B4               | OK            | 87.7        40                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          29095/ 32768         |
+===========================+===============+====================================================+
| 6     910B4               | OK            | 88.6        38                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          29096/ 32768         |
+===========================+===============+====================================================+
| 7     910B4               | OK            | 86.2        40                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          29096/ 32768         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 4       0                 | 498807        | python                   | 26323                   |
+===========================+===============+====================================================+
| 5       0                 | 499212        | python                   | 26323                   |
+===========================+===============+====================================================+
| 6       0                 | 499213        | python                   | 26323                   |
+===========================+===============+====================================================+
| 7       0                 | 499214        | python                   | 26322                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux
</summary>

```text
</details>

### 🐛 Describe the bug

```text
#!/usr/bin/env bash
. /home/ma-user/anaconda3/etc/profile.d/conda.sh

conda activate py310

export VLLM_HOST_IP=127.0.0.1
source /usr/local/Ascend/ascend-toolkit/set_env.sh
source /usr/local/Ascend/nnal/atb/set_env.sh
source /usr/local/Ascend/ascend_ops/vendors/customize/bin/set_env.bash

export INFER_MODE=DEFAULT
# maskfree-attention开关, 默认打开
export USE_MASKFREE_ATTN=1
# 在超过阈值的长度使用maskfree-attention；默认超过16k句长时使用
#export MASKFREE_ATTN_THRESHOLD=32768
export MASKFREE_ATTN_THRESHOLD=16384


# export VLLM_USE_V1=0
export VLLM_ALLOW_RUNTIME_LORA_UPDATING=True

model_path=/data/workspace/modelzoo/Qwen25-72b/Qwen2.5-72B-Instruct
rfut_path=/data/workspace/modelzoo/rfut_model/rfut_72b_lora
rfut_path_v2=/data/workspace/modelzoo/rfut_model/rfut_72b_lora_v2
docker_ip=0.0.0.0
port_num=9002


nohup python -m vllm.entrypoints.openai.api_server \
        --model ${model_path} \
        --enable-lora \
        --lora-modules rfut=${rfut_path} \
        --served-model-name="Qwen2.5-72B-Instruct" \
        --max-model-len=16384 \
        --max-num-batched-tokens=16384  \
        --enable-auto-tool-choice \
        --tool-call-parser=hermes \
        --tensor-parallel-size=8 \
        --host=${docker_ip} \
        --port=${port_num} \
        --gpu-memory-utilization=0.97 \
        --trust-remote-code \
        --disable-log-stats \
        > vllm_lora_open_${port_num}.log  2>&1 &
```



 使用--lora-modules外挂lora模型，效果不如转换成全参lora的模型
![Image](https://github.com/user-attachments/assets/8140c34e-b87f-4da4-a783-a5b181209cba)



