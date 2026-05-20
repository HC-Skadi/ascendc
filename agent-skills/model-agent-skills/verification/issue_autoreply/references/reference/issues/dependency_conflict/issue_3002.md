# Issue #3002: [Bug]: The generation of attention mask takes too much host memory

## 基本信息

- **编号**: #3002
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3002
- **创建时间**: 2025-09-18T02:31:42Z
- **关闭时间**: 2026-01-06T08:05:22Z
- **更新时间**: 2026-01-06T08:05:22Z
- **提交者**: @yiz-liu
- **评论数**: 7

## 标签

bug; guide

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Ubuntu 24.04.1 LTS (aarch64)
GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0
Clang version: Could not collect
CMake version: version 4.1.0
Libc version: glibc-2.39

Python version: 3.11.13 (main, Sep  3 2025, 13:42:11) [GCC 13.3.0] (64-bit runtime)
Python platform: Linux-5.10.0-281.0.0.184.oe2203sp4.aarch64-aarch64-with-glibc2.39

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             384
On-line CPU(s) list:                0-383
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         -
BIOS Model name:                    Kunpeng 920 5250Y To be filled by O.E.M. CPU @ 2.0GHz
BIOS CPU family:                    280
Model:                              0
Thread(s) per core:                 2
Core(s) per socket:                 48
Socket(s):                          4
Stepping:                           0x0
Frequency boost:                    disabled
CPU(s) scaling MHz:                 100%
CPU max MHz:                        2000.0000
CPU min MHz:                        1200.0000
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs sb dcpodp sve2 sveaes svepmull svebitperm svesha3 svesm4 flagm2 frint svei8mm svebf16 i8mm bf16 dgh rng ecv
L1d cache:                          12 MiB (192 instances)
L1i cache:                          24 MiB (192 instances)
L2 cache:                           192 MiB (192 instances)
L3 cache:                           336 MiB (8 instances)
NUMA node(s):                       8
NUMA node0 CPU(s):                  0-47
NUMA node1 CPU(s):                  48-95
NUMA node2 CPU(s):                  96-143
NUMA node3 CPU(s):                  144-191
NUMA node4 CPU(s):                  192-239
NUMA node5 CPU(s):                  240-287
NUMA node6 CPU(s):                  288-335
NUMA node7 CPU(s):                  336-383
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass:    Not affected
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Mitigation; CSV2, but not BHB
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] mypy==1.11.1
[pip3] mypy_extensions==1.1.0
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] sentence-transformers==5.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250911
[pip3] torchaudio==2.7.0
[pip3] torchvision==0.22.1
[pip3] transformers==4.56.1
[pip3] zmq==0.0.0
[conda] Could not collect
vLLM Version: 0.10.2rc3.dev14+g72fc8aa41 (git sha: 72fc8aa41)
vLLM Ascend Version: 0.10.2rc2.dev13+g99210941a.d20250916 (git sha: 99210941a, date: 20250916)

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
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/lib:
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
| npu-smi 25.2.0                   Version: 25.2.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 211.3       43                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 7           0    / 0          61609/ 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           44                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 7           0    / 0          61625/ 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 210.6       45                0    / 0             |
| 0     2                   | 0000:99:00.0  | 7           0    / 0          61616/ 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           45                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 7           0    / 0          61619/ 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 205.7       44                0    / 0             |
| 0     4                   | 0000:95:00.0  | 7           0    / 0          61633/ 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           44                0    / 0             |
| 1     5                   | 0000:97:00.0  | 7           0    / 0          61623/ 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 209.9       43                0    / 0             |
| 0     6                   | 0000:91:00.0  | 7           0    / 0          61625/ 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           44                0    / 0             |
| 1     7                   | 0000:93:00.0  | 7           0    / 0          61628/ 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 219.9       43                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 8           0    / 0          61602/ 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           45                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 7           0    / 0          61618/ 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 214.0       47                0    / 0             |
| 0     10                  | 0000:89:00.0  | 7           0    / 0          61578/ 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           45                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 7           0    / 0          61603/ 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 201.9       43                0    / 0             |
| 0     12                  | 0000:85:00.0  | 6           0    / 0          61614/ 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           43                0    / 0             |
| 1     13                  | 0000:87:00.0  | 7           0    / 0          61623/ 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 205.5       44                0    / 0             |
| 0     14                  | 0000:81:00.0  | 7           0    / 0          61627/ 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           43                0    / 0             |
| 1     15                  | 0000:83:00.0  | 7           0    / 0          61631/ 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 935440        |                          | 141                     |
| 0       0                 | 936673        |                          | 141                     |
| 0       0                 | 930242        |                          | 141                     |
| 0       0                 | 934451        |                          | 141                     |
| 0       0                 | 931572        |                          | 141                     |
| 0       0                 | 941045        |                          | 141                     |
| 0       0                 | 942487        |                          | 141                     |
| 0       0                 | 929673        |                          | 141                     |
| 0       1                 | 929405        |                          | 58780                   |
+===========================+===============+====================================================+
| 1       0                 | 929673        |                          | 58540                   |
| 1       1                 | 930242        |                          | 58780                   |
+===========================+===============+====================================================+
| 2       0                 | 930907        |                          | 58560                   |
| 2       1                 | 931572        |                          | 58779                   |
+===========================+===============+====================================================+
| 3       0                 | 932555        |                          | 58558                   |
| 3       1                 | 933405        |                          | 58782                   |
+===========================+===============+====================================================+
| 4       0                 | 934451        |                          | 58520                   |
| 4       1                 | 935440        |                          | 58780                   |
+===========================+===============+====================================================+
| 5       0                 | 936673        |                          | 58500                   |
| 5       1                 | 937869        |                          | 58764                   |
+===========================+===============+====================================================+
| 6       0                 | 939246        |                          | 58540                   |
| 6       1                 | 941045        |                          | 58782                   |
+===========================+===============+====================================================+
| 7       0                 | 942487        |                          | 58560                   |
| 7       1                 | 944268        |                          | 58782                   |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.3.RC1
innerversion=V100R001C23B085
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC1/aarch64-linux
```

</details>


### 🐛 Describe the bug

In `vllm_ascend.attention.attention_mask`, we have this:
```python
def _generate_attn_mask(max_seq_len, dtype):
    # Construct lower triangle matrix.
    mask_flag = torch.tril(
        torch.ones((max_seq_len, max_seq_len),
                   dtype=torch.bool)).view(max_seq_len, max_seq_len)
    # Create upper triangle matrix used to mark mask positions.
    mask_flag = ~mask_flag
    # Currently for fp16 dtype, the mask value should be set to -inf.
    # TODO: Eliminate this part in the future.
    if dtype == torch.float16:
        mask_value = torch.finfo(torch.float32).min
    else:
        mask_value = 1
    attn_mask = torch.masked_fill(torch.zeros(size=(max_seq_len, max_seq_len)),
                                  mask_flag, mask_value).to(dtype)
    return attn_mask
```
Notice that the creation of `mask_flag` and `attn_mask` involves significant temporary memory allocations. Specifically, out-of-place operations like `torch.tril` and `torch.masked_fill` can cause peak memory usage to be roughly double the size of the final tensor during their creation. This might seem trivial, but it can become a substantial overhead with a large sequence length.

Take Qwen3-30B-A3B-Instruct-2507 as an example, where `max_seq_len` can be as large as 256K (262,144). The peak temporary memory allocation for creating the initial boolean `mask_flag` would be:

`2 * (256 * 1024)^2 * 1 byte ≈ 128 GiB`

As for `attn_mask`, things are more dreadful, since `torch.zeros` has `torch.float32` for `dtype` by default, so the peak allocation here should be:

`2 * (256 * 1024)^2 *4 byte ≈ 512 GiB`

So the max peak temporary memory allocation is `128 + 512 = 640 GiB`.

Or is it so?

Not exactly, `_generate_attn_mask` is invoked in every `NPUModelRunner.__init__`. We therefore must scale its timing by `world_size_across_dp`. For example, with four devices the actual peak temporary host memory allocation reaches **2560 GiB**.

If the container has no memory limits, this can cause catastrophic system failures (for instance, SSH becoming unresponsive). The severity of this issue cannot be overstated.

As an immediate mitigation, I recommend temporarily reducing `max_model_len` to limit peak host memory allocations until a permanent fix is implemented. Please reassure anyone who encounters this bug that there is no need to panic @wangxiyuan .

@rjg-lyh do we have an established timeline or plan to refactor `_generate_attn_mask` to address the root cause?
