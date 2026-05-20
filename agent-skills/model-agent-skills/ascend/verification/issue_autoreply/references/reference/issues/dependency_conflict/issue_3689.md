# Issue #3689: [Bug]: Qwen3-Next gets many repetitive, redundant tokens.

## 基本信息

- **编号**: #3689
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3689
- **创建时间**: 2025-10-24T00:57:54Z
- **关闭时间**: 2025-10-25T06:32:27Z
- **更新时间**: 2025-10-25T06:32:27Z
- **提交者**: @drslark
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
CMake version: version 4.1.0
Libc version: glibc-2.35

Python version: 3.11.13 (main, Jul 26 2025, 07:27:32) [GCC 11.4.0] (64-bit runtime)
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
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1
[pip3] transformers==4.56.1
[conda] Could not collect
vLLM Version: 0.11.1.dev0+gb8b302cde.d20251020 (git sha: b8b302cde, date: 20251020)
vLLM Ascend Version: 0.11.0rc1.dev103+gdaa4dd0a5.d20251020 (git sha: daa4dd0a5, date: 20251020)

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
| npu-smi 25.3.rc1                 Version: 25.3.rc1                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 166.6       37                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          3150 / 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           36                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          2886 / 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 161.9       37                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          3156 / 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           37                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          2875 / 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 160.6       36                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3149 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           36                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          2886 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 166.3       37                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3154 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           39                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          2875 / 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 171.5       37                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          58072/ 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           38                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          58039/ 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 162.5       37                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          58071/ 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           36                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          58037/ 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 205.0       40                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          56896/ 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           37                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          57087/ 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 195.6       40                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          56969/ 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           39                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          57132/ 65536         |
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
| 4       0                 | 1534604       |                          | 54963                   |
| 4       1                 | 1539371       |                          | 55217                   |
+===========================+===============+====================================================+
| 5       0                 | 1545073       |                          | 54963                   |
| 5       1                 | 1550598       |                          | 55217                   |
+===========================+===============+====================================================+
| 6       0                 | 1756550       |                          | 116                     |
| 6       0                 | 1732918       |                          | 53740                   |
| 6       1                 | 1756550       |                          | 54252                   |
+===========================+===============+====================================================+
| 7       0                 | 3910682       |                          | 116                     |
| 7       0                 | 3896157       |                          | 53798                   |
| 7       1                 | 3910682       |                          | 54310                   |
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

Codes to reproduce this bug.

```python
prompts = ["以下是中国关于计算机网络考试的单项选择题，请选出其中的正确答案。回答的最后一行应采用以下格式：”answer:$LETTER“（不带引号），其中LETTER 是ABCD之一。回答之前先一步步思考。\n\n一个TCP连接的数据传输阶段，如果发送端的发送窗口值由2000变为3000，意味着发送端可以____。\nA. 在收到一个确认之前可以发送3000个TCP报文段\nB. 在收到一个确认之前可以发送1000B\nC. 在收到一个确认之前可以发送3000B\nD. 在收到一个确认之前可以发送2000个TCP报文段"]

sampling_params = SamplingParams(temperature=0.7, top_p=0.8, top_k=20, max_tokens=10000)

llm = LLM(model="/home/model/Qwen3-Next-80B-A3B-Instruct",
          tensor_parallel_size=4,
          enforce_eager=True,
          distributed_executor_backend="mp",
          gpu_memory_utilization=0.7,
          max_model_len=32768)

outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

And this is the buggy result.
```text
Prompt: '以下是中国关于计算机网络考试的单项选择题，请选出其中的正确答案。回答的最后一行应采用以下格式：”answer:$LETTER“（不带引号），其中LETTER 是ABCD之一。回答之前先一步步思考。\n\n一个TCP连接的数据传输阶段，如果发送端的发送窗口值由2000变为3000，意味着发送端可以____。\nA. 在收到一个确认之前可以发送3000个TCP报文段\nB. 在收到一个确认之前可以发送1000B\nC. 在收到一个确认之前可以发送3000B\nD. 在收到一个确认之前可以发送2000个TCP报文段', Generated text: '\n\n首先，问题是关于TCP协议的。题目说：“一个TCP连接中，发送端在收到对端的确认之前，最多可以发送多少个字节的数据？”然后给出了选项，但问题中没有列出选项，我需要基于常识来回答。\n\n题目说：“TCP/IP协议中，TCP协议采用（ ）来实现流量控制”，然后选项是A. 滑动窗口，B. � 什么的，但题目没全给。但在用户消息中，是“TCP/IP协议中，采用（ ）技术来实现流量控制”，所以是选择题。\n\n但用户说：“TCP/IP协议中，通过（）技术实现流量控制”，然后选项没给，但在上下文是选择题。\n\n回顾用户消息：用户说“在TCP/IP协议中，流量控制是通过什么方式实现的？”，但原消息是：“TCP/IP协议中，采用（ ）来实现流量控制？”\n\n原问题： “TCP/IP协议中，采用（ ）来实现流量控制？”\n\nA. �  B.  C. D.  但没给出选项，我需要推断。\n\n在TCP/IP中，流量控制是通过滑动窗口机制实现的。具体来说，接收方通过在TCP报头中的“窗口大小”（Window Size）字段来通告其接收窗口的大小，发送方根据这个来调整发送速率。\n\n所以，TCP/IP协议中，用于实现流量控制的机制是“滑动窗口”机制。\n\n选项可能包括：A. 滑动窗口 B. 停等协议 等等。\n\n但问题说：“TCP/IP协议采用（ ）实现流量控制。”\n\n在TCP协议中，流量控制是通过“滑动窗口”机制实现的。\n\n所以，答案应该是：B. 滑动窗口\n\n但题目说：“TCP/IP协议采用（）实现流量控制”，然后选项是A. B. C. D.\n\n但题目是：“在TCP/IP协议中，采用（ ）技术实现流量控制？”\n\n选项：A. 1  B. 2  C. 3  D. 4  — 但选项没给，可能是A、B、C、D选项。\n\n在问题中，它说：“TCP/IP协议采用（ ）技术实现流量控制”，然后选项A B C D。\n\n但题目说：“TCP/IP协议采用（）实现流量控制”，所以（ ）是填空。\n\n但题目说：“TCP/IP协议采用（）”，然后选项A B C D。\n\n在用户消息中，是“C. 128D” 但123是数字，可能打错了。\n\n用户消息："C. 123" 但C是选项，A B C D 选项。\n\n看用户消息："C. 1210" 但1010是1010，可能打字错误。\n\n在用户消息："C. 1024" 但1024是数字，1024是数字，1024是数字。\n\n在用户消息："C. 1024"  C. 1024? C. 128? 等等。\n\n看用户消息："C. 1024" 但C是选项，1024是数字。\n\n用户说：“C. 1024” 但C是C，C是C。\n\n看用户消息："C. 1024" 和 "D. 10" 但C和D是选项。\n\n用户说：“TCP/IP协议的C” — C是C，但C是什么？\n\n用户说：“TCP/IP协议采用1024” 1024是数字，1024是数字，但1024是数字，不是字符。\n\n1024是数字，1024B是1024字节，B是字节。\n\n在TCP/IP，端口是16位，16位端口，但端口号是16位，但TCP头有端口。\n\n我  think  for TCP, the port number is 16-bit, but for flow control, it\'s the window size.\n\n在TCP中，窗口大小字段是16位，所以最大窗口大小是65535字节。\n\n但现代TCP有窗口缩放选项，可以更大。\n\n但在这个问题中，可能是基本的。\n\n题目说：“TCP/IP协议中，采用（）技术实现流量控制”\n\n选项：A. 1001  B. 1010  C. 1110  D. 1110  之类的，但题目没说。\n\n题目说：“C. 1010” 但C是C，D是D，C和D是选项。\n\n看用户消息：\n\n“C. 1010 1000 1000 1011 1001” 等等，用户说 C. 1101 1010 1010 1101，但1010是12，1010是12，1101是13，等等。\n\n在用户消息中，用户说：“C. 1011  D. 1010  C. 1111 1101  D. 1001”\n\n这很混乱。\n\n也许 C 选项是 1101，D 选项是 1010，但 C 和 D 是选项，A、B、C、D。\n\n题目说：“A. 1001 1111 1000” — 但这是三个值？不，A 选项是 A，B，C，D 选项。\n\n题目说：“A. 1011 1011 1110 1111” —— 但那是 16 位？1010 1010 1010 是 12 . 1010 是 12，1010 二进制是 12，但 1010 是 12 二进制？1010 二进制是 1210 二进制？1010 二进制是 1010 二进制，但 1010 二进制是 10，十进制。\n\n我们来澄清一下。\n\n在二进制中，1010 二进制是 1010 二进制，也就是 1010 二进制，也就是十进制的 10，但 1010 二进制是 1010 二进制，也就是 1010 二进制，也就是 10 位二进制数，但 1010 二进制是 1010，是十进制 8，如果 4 位。\n\n我  混乱了。\n\n我们来澄清一下。\n\n在 TCP 中，MSS 是 1460，但 TCP 头部是 20 字节，所以对于 1500 的 MTU，1460 是数据，20 字节头部，1460+40=1024？MTU 1500，IP 头 20，TCP 头 20，但 TCP 头是 20 字节，IP 头 20，所以 TCP 段是 1460 数据 + 20 个 TCP 头 + 20 IP �，但 IP 头是 20，TCP 头 20，所以 40 个字节的 TCP 头，MTU 1500，所以 1500 字节数据 + 20 个 TCP 头，但 TCP 头是 20 字节，所以 1460 字节的数据 + 20 字节 IP 头，但 IP 头是 20 字节，TCP 头 20 字节，所以 IP 数据报是 1500 字节，包括 20 字节 IP 头和 1460 字节数据。\n\n但题目是“TCP/IP 协议”，而“C”是“C 语言”，但 C 语言是编程语言。\n\n在题目中，它写着“C 语言”，但 C 语言是编程语言，不是 TCP。\n\n在上下文中，C 语言是 C 语言，C 语言是编程语言，TCP 是协议。\n\nC 语言和 C 语言是不同的。\n\nC 语言是编程语言，C 语言。\n\nTCP 代表“Transmission Control Protocol”。\n\n所以，C 语言（C 语言）和 TCP（Transmission Control）是不同的。\n\nC 语言是编程语言，TCP 是协议。\n\n所以 C 语言是 C 语言，TCP 是协议，C 代表 C 语言，C 语言和 C 语言是一样的？C 语言是 C 语言，C 语言是 C 语言。\n\nC 语言是编程语言，C 语言是 C 语言。\n\nC 语言是 C 语言，C++ 是 C++，C 语言是 C 语言。\n\nC 语言是 C 语言，C 语言。\n\nC 语言是 1972 年的，TCP 是 1974 年。\n\n但就本题而言，我们可能不需要管这些。\n\n但用户要求的是 C 语言，C 语言是 C 语言。\n\n在 C 语言中，我们有 int、char 等。\n\n但 TCP 是 IP 之上的。\n\n对于这个问题，我们可能不需要 C 语言。\n\n但题目是“C 语言”，C 语言。\n\nC 语言是 1972 年由 Dennis Ritchie 为 Unix 开发的。\n\nC 语言和 C 语言是相同的。\n\nC 语言是 1972 年由 Dennis Ritchie 开发的。\n\nTCP 也是 1970 年代。\n\n但 TCP/IP 与 C 语言是分开的。\n\nC 语言是 1972 年由 Dennis Ritchie 为 Unix 开发的。\n\nTCP 也由 Vint Cerf 在 1970 年代开发。\n\n但 C 语言和 C 语言是不同的。\n\nC 语言是 Dennis Ritchie 在 1972 年为 Unix 开发的。\n\nTCP 也是 1970 年代由 Vint Cerf 和 Bob Kahn 开发的。\n\n但 TCP 本身是 1974 年。\n\n但题目中，C 语言是 C 语言，C 语言是 1972 年由 Dennis Ritchie 开投入的。\n\nC 语言是 1972 年，B 语言是 1972 年，C 语言是 1972 年。\n\n1972 年，C 语言。\n\n1970：Thompson 用 B 语言写了一个 Unix。\n\n1971：C 语言，1972。\n\n1972 年，C 语言。\n\n1972：C 语言。\n\nTCP 是 1970 年代。\n\n但 TCP/IP 于 1974 年由 Vinton Cerf 和 Bob Kahn 设计。\n\n1974：A TCP/IP 模型。\n\n1983 年，ARPANET 采用 TCP/IP。\n\n但为简单起见，对于这个问题，我们可能不需要它。\n\n但题目是“C 语言”和“C 语言”，C 语言是 1972 年由 Dennis Ritchie 开发的。\n\nC 语言是 1972 年。\n\nTCP 也是 1970 年代。\n\n但 C 语言和 C 语言是不同的。\n\nC 语言是 1972 年由 Dennis Ritchie 为 Unix 设计的。\n\nTCP 也是 1970 年代。\n\n但 C 语言和 C 语言是不同的。\n\nC 语言是 Dennis Ritchie 在 1972 年为 Unix 开发的。\n\nTCP 也是 1974 年，Vinton Cerf 和 Bob Kahn。\n\n但 TCP 是协议，C 语言是编程语言。\n\nC 语言是 1972 年由 Dennis Ritchie 为 Unix 开发的。\n\nC 语言是 1972 年，B 语言是 1972，C 语言是 1972，K&R C。\n\nK&R C 是 1972 年。\n\nTCP 也是 1974 年。\n\n但 C 语言和 C 语言是不同的。\n\nC 语言是 Dennis Ritchie 1972 年为 Unix 设计的。\n\nTCP 也是 1970 年代。\n\n但 TCP 和 IP 是 1970 年代。\n\n但 C 语言是 1972 年，B 语言是 1970，C 语言是 1972，C 语言。\n\nC 语言是 1972 年，B 语言是 1oire，C 语言是 1972 年。\n\n1970：C 语言。\n\n1972：C 语言。\n\n1972：C 语言。\n\nC 语言是 1972 年。\n\n1972 年，Dennis Ritchie 为 Unix 开发了 C 语言。\n\nTCP 1974，1981。\n\n但为了这个问题，我们可能不需要它。\n\n但题目是“C 语言”，C 语言。\n\nC 语言是 1972 年。\n\nC 语言是 1972 年，B 语言是 1970，C 语言是 1972。\n\nC 语言是 1972 年，B 语言 1970，C 语言 1972，B 是 1972，B 1972，C 1970，1978 年。\n\nC 语言是 1972 年，B 语言是 C 语言，1972，C 语言是 1972，B 1973。\n\nC 语言：1972-1973 由 Dennis Ritchie 开发。\n\nC 语言是 1972 年，K&R C 1972。\n\n1972 年，K&R C。\n\nTCP 1974，1982。\n\n但为简单起见，对于这个问题，我们可能不需要它。\n\n但问题是，对于这个多项选择题，我们可能需要选择 C 作为 C 语言。\n\n但题目是“C 语言”和“C 语言”是 C 语言，C 语言。\n\nC 语言是 1972 年由 Dennis Ritchie 开发的。\n\nC 语言是 1972 年，B 语言是 1970，C 语言是 1972。\n\n1970：B 语言，1972 C 语言，C 语言 1972，K&R C。\n\nC 语言是 1972 年，K&R C 1972。\n\nC 语言是 1972 年，B 语言是 1,972 年。\n\n1972 年，K&R C 语言。\n\n但 C 语言是 1972 年，C 语言。\n\nC 语言是 1972 年，B 语言是 1972，K&R C 1972。\n\nC 语言是 1972 年，B 是 1970，B 是 1972，C 1972 1972。\n\nC 语言是 1972 年，B 是 1972，C 1972 1972 1972 19認め 1974 1972。\n\nI think I\'m confusing.\n\nLet\'s not go there.\n\nFor the purpose of this problem, the answer is C for C, but C is C.\n\nI think the question is multiple choice with A B C D.\n\nBut the user said "C. C++" and "C++" for C++.\n\nLet\'s assume the question is multiple choice with options A B C D.\n\nFor C++, it\'s C++.\n\nBut for the answer, we need to choose the option.\n\nBut the user asked for the answer.\n\nPerhaps for the question, the answer is C. C++.\n\nBut let\'s see the question: "C++ 语言" C++ language.\n\nIn Chinese, C++ is C++.\n\nThe question is: C 语言 C 语言，C 语言。\n\nC 语言是 C 语言。\n\nC 语言是 C 语言。\n\nC 语言是 C 语言。\n\nC 语言是 C 语言。\n\nC 语言是 C 语言。\n\nC 语言是 C 语言。\n\nC 语言是 C 语言。\n\nC 语言是 C 语言。\n\nC 语言是 C 语言。\n\nC 语言是 C 语言。\n\nC 语言是 C 语言。\n\nC 语言是 C 语言。\n\nC 语言是 C 语言。\n\nC 语言是 C 语言。\n\nC 语言是 C 语言。\n\nC 语言。\n\nC 语言是 C 语言。\n\nC 语言是 C 语言。\n\nC 语言是 C 语言。\n\nC 语言是 C 语言。\n\nC 语言是 C 语言。\n\nC 语言。\n\nC 语言是 C 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言。\n\nC 语言'
```

We can see that text '\n\nC 语言。' is repeating.
