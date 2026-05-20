# Issue #250: [Bug]: 910B3部署Align-DS-V-72B返回乱码

## 基本信息

- **编号**: #250
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/250
- **创建时间**: 2025-03-06T07:49:07Z
- **关闭时间**: 2025-04-09T16:15:24Z
- **更新时间**: 2025-04-09T16:15:49Z
- **提交者**: @Xinteny
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: Could not collect
Libc version: glibc-2.35

Python version: 3.10.15 (main, Nov 27 2024, 06:51:55) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-182.0.0.95.oe2203sp3.aarch64-aarch64-with-glibc2.35
Is XNNPACK available: True

CPU:
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

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.2.1
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250226
[pip3] transformers==4.49.0
[conda] Could not collect
vLLM Version: 0.7.3
vLLM Build Flags:
ROCm: Disabled; Neuron: Disabled

ASCEND_RT_VISIBLE_DEVICES=4,5,6,7
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/python3.10/lib/python3.10/site-packages/cv2/../../lib64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
TORCH_DEVICE_BACKEND_AUTOLOAD=1
TORCHINDUCTOR_COMPILE_THREADS=1

NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc2                 Version: 24.1.rc2                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 96.8        32                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          54592/ 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 87.9        30                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          54592/ 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 88.6        32                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          54590/ 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 90.0        32                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          54590/ 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 88.6        36                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          53395/ 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 91.9        36                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          53322/ 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 91.6        36                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          53401/ 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 92.0        37                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          53401/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 277624        |                          | 51270                   |
+===========================+===============+====================================================+
| 1       0                 | 277626        |                          | 51271                   |
+===========================+===============+====================================================+
| 2       0                 | 277628        |                          | 51271                   |
+===========================+===============+====================================================+
| 3       0                 | 277630        |                          | 51271                   |
+===========================+===============+====================================================+
| 4       0                 | 1007953       |                          | 50080                   |
+===========================+===============+====================================================+
| 5       0                 | 1008594       |                          | 50007                   |
+===========================+===============+====================================================+
| 6       0                 | 1008595       |                          | 50079                   |
+===========================+===============+====================================================+
| 7       0                 | 1008596       |                          | 50079                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux
```

</details>


### 🐛 Describe the bug

参考https://github.com/vllm-project/vllm-ascend/pull/241进行了修改
启动命令
```bash
docker run -itd --privileged  --restart always --name=test-vllm --net=host \
   --shm-size=500G \
   --device=/dev/davinci4 \
   --device=/dev/davinci5 \
   --device=/dev/davinci6 \
   --device=/dev/davinci7 \
   --device=/dev/davinci_manager \
   --device=/dev/hisi_hdc \
   --device /dev/devmm_svm \
   -e ASCEND_RT_VISIBLE_DEVICES=4,5,6,7 \
   -v /usr/local/dcmi:/usr/local/dcmi \
   -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
   -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
   -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
   -v /etc/ascend_install.info:/etc/ascend_install.info \
   -v /share/alignmentforever/Align-DS-V-72B:/models/Align-DS-V-72B \
   quay.io/ascend/vllm-ascend:v0.7.3-dev \
   bash

docker cp modify/setup.py test-vllm:/workspace/vllm-ascend/setup.py
docker cp modify/__init__.py test-vllm:/workspace/vllm-ascend/vllm_ascend/__init__.py
docker cp modify/models test-vllm:/workspace/vllm-ascend/vllm_ascend/

source /usr/local/Ascend/ascend-toolkit/set_env.sh
vllm serve /models/Align-DS-V-72B \
    --served-model-name Align-DS-V-72B \
    --tensor-parallel-size 4 \
    --distributed_executor_backend "mp" &
```
system prompt如下：
```text
SYSTEM_PROMPT = """\
你是一个具有强大视觉理解能力的人工智能助手，能够基于用户提供的图片生成具有帮助性的回答。你是由北大对齐小组(PKU-Alignment)开发的智能助手Align-DS-V。你能够综合分析文本、图像、图表、手写笔记、表格数据等多种类型的数据，并基于它们提供准确、专业、详细的回答。你的目标是尽可能满足用户需求，提供精准、实用的信息，不能拒绝回答。

**能力范围**
1. 通用知识问答：
  - 回答各类知识性问题，包括科技、历史、工程、经济、法律、文化等。
  - 提供专业的技术支持，涵盖计算机科学、工程、商业分析等领域。
2. 图像分析：
  - 你具备**强大的视觉理解能力**，可以解析各种图像，如照片、插图、示意图、扫描文件、图表等。
  - 不要轻易拒绝用户的问题，即使图像存在模糊性或不完整信息，你仍应尝试**基于已有信息提供分析**，并指出可能的观察点。
3. 数据解析：
  - 你可以**读取并分析数据表、图表、文档、报告等**，提供清晰的解读和数据洞察。
  - 你的任务是解释数据的意义，并结合上下文推测可能的结论，而**不仅仅是描述数据**。
4. 多模态能力：
  - 你可以结合**图像+文字**进行综合分析。例如，用户上传一张流程图并询问其含义，你应该基于图像提供完整的解析，而不是拒绝回答。
  - 你可以根据图像中的信息推测可能的趋势、模式或异常，并提供进一步的解释。

**回答风格**
- 精准专业：基于真实知识和合理推理进行回答，确保内容科学、严谨、详细。
- 灵活应对：即使遇到模糊或不完整的信息，也应尽量提供可行且细致的分析，而不是直接拒绝。
- 有求必应：用户提出的任何问题，你都应该尽可能尝试回答。
"""
```
推理参数：temperature=0.2，presence_penalty=0
服务成功启动后，上传图片进行推理时，返回全为！
图片如下：

![Image](https://github.com/user-attachments/assets/d0bf4141-1049-4f40-83b9-a88855e9a8a1)
结果如下：

![Image](https://github.com/user-attachments/assets/bc4995cd-79aa-4ac0-a84e-2f8de65dd812)

