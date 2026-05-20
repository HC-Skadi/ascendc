# Issue #3037: [Bug]: Qwen3-next inference failure because of ```ACL stream synchronize failed, error code:507035```

## 基本信息

- **编号**: #3037
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3037
- **创建时间**: 2025-09-19T07:55:21Z
- **关闭时间**: 2025-09-19T08:25:19Z
- **更新时间**: 2025-09-28T10:19:03Z
- **提交者**: @wxsIcey
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

Python version: 3.11.13 (main, Jul 26 2025, 09:30:19) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-182.0.0.95.r1941_123.hce2.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                         aarch64
CPU op-mode(s):                       64-bit
Byte Order:                           Little Endian
CPU(s):                               320
On-line CPU(s) list:                  0-319
Vendor ID:                            HiSilicon
BIOS Vendor ID:                       HiSilicon
BIOS Model name:                      Kunpeng 920 7285Z
Model:                                0
Thread(s) per core:                   1
Core(s) per socket:                   80
Socket(s):                            4
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
[pip3] pyzmq==27.0.1
[pip3] sentence-transformers==5.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchvision==0.22.1
[pip3] transformers==4.56.0
[pip3] zmq==0.0.0
[conda] Could not collect
vLLM Version: 0.9.1
vLLM Ascend Version: 0.9.2rc2.dev255+gcf96366.d20250830 (git sha: cf96366, date: 20250830)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
VLLM_USE_MODELSCOPE=True
PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
| 0     Ascend910           | OK            | 178.8       36                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          3421 / 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           36                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          3193 / 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 185.4       36                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          3415 / 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           36                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          3188 / 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 176.8       36                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3412 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           37                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          3189 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 178.3       36                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3412 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           36                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          3186 / 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 180.7       37                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          3402 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           36                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          3199 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 188.7       36                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          3398 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           36                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          3201 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 183.1       37                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          3399 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           36                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          3203 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 186.6       37                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          35943/ 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           38                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          35651/ 65536         |
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
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| 7       0                 | 1789313       |                          | 32575                   |
| 7       1                 | 1789313       |                          | 32519                   |
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

```
import os

os.environ["VLLM_USE_MODELSCOPE"] = "True"

from vllm import LLM, SamplingParams


def main():
    prompts = [
        "The capital of France is",
    ]

    # Create a sampling params object.
    sampling_params = SamplingParams(max_tokens=100, temperature=0.6, top_k=40, top_p=0.95)
    # Create an LLM.
    llm = LLM(
        model="Qwen/Qwen3-Next-80B-A3B-Instruct",
              tensor_parallel_size=4,
              enforce_eager=True,
              trust_remote_code=True,
              max_model_len=256,
              gpu_memory_utilization=0.7,
              block_size=64,
              )

    # Generate texts from the prompts.
    outputs = llm.generate(prompts, sampling_params)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")


if __name__ == "__main__":
    main()

```
```
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [dump_input.py:69] Dumping input data for V1 LLM engine (v0.9.1) with config: model='Qwen/Qwen3-Next-80B-A3B-Instruct', speculative_config=None, tokenizer='Qwen/Qwen3-Next-80B-A3B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=256, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=True, kv_cache_dtype=auto, device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen/Qwen3-Next-80B-A3B-Instruct, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=True, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":null,"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":0,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"pass_config":{},"max_capture_size":0,"local_cache_dir":null}, 
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [dump_input.py:76] Dumping scheduler output for model execution: SchedulerOutput(scheduled_new_reqs=[], scheduled_cached_reqs=CachedRequestData(req_ids=['0'], resumed_from_preemption=[false], new_token_ids=[], new_block_ids=[null], num_computed_tokens=[5]), num_scheduled_tokens={0: 1}, total_num_scheduled_tokens=1, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={}, num_common_prefix_blocks=[0, 0, 0, 0], finished_req_ids=[], free_encoder_mm_hashes=[], structured_output_request_ids={}, grammar_bitmask=null, kv_connector_metadata=null)
[rank1]:[W919 07:42:16.183678569 compiler_depend.ts:57] Warning: EZ9999: Inner Error!
EZ9999: [PID: 931772] 2025-09-19-07:42:16.416.145 The error from device(chipId:0, dieId:1), serial number is 6, there is an exception of aivec error, core id is 7, error code = 0, dump info: pc start: 0x1242011fe000, current: 0x1242011fef4c, vec error info: 0xfb000000d7, mte error info: 0x7811b66c7f, ifu error info: 0x64e6b052ba000, ccu error info: 0x282b086451c1d46f, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c2405a0000.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
        TraceBack (most recent call last):
       The extend info: errcode:(0, 0x800, 0) errorStr: The UB address accessed by the VEC instruction is not aligned. fixp_error0 info: 0x1b66c7f, fixp_error1 info: 0x78, fsmId:0, tslot:1, thread:0, ctxid:0, blk:2, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:0, dieId:1), serial number is 6, there is an exception of aivec error, core id is 8, error code = 0, dump info: pc start: 0x1242011fe000, current: 0x1242011fef4c, vec error info: 0xfb000000d7, mte error info: 0x718f27b458, ifu error info: 0x3cb504a0b8840, ccu error info: 0x49196999335c6940, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c2405a0000.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0, 0x800, 0) errorStr: The UB address accessed by the VEC instruction is not aligned. fixp_error0 info: 0xf27b458, fixp_error1 info: 0x71, fsmId:0, tslot:1, thread:0, ctxid:0, blk:3, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:0, dieId:1), serial number is 6, there is an exception of aivec error, core id is 9, error code = 0, dump info: pc start: 0x1242011fe000, current: 0x1242011fef4c, vec error info: 0xfb000000d7, mte error info: 0xc76541e02c, ifu error info: 0xc4aab0fb8e00, ccu error info: 0x31c35c2378310e78, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c2405a0000.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0, 0x800, 0) errorStr: The UB address accessed by the VEC instruction is not aligned. fixp_error0 info: 0x541e02c, fixp_error1 info: 0xc7, fsmId:0, tslot:1, thread:0, ctxid:0, blk:4, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:0, dieId:1), serial number is 6, there is an exception of aivec error, core id is 10, error code = 0, dump info: pc start: 0x1242011fe000, current: 0x1242011fef4c, vec error info: 0xfb000000d7, mte error info: 0x3e911dd, ifu error info: 0xc8938ca34140, ccu error info: 0x402e40c848710369, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c2405a0000.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0, 0x800, 0) errorStr: The UB address accessed by the VEC instruction is not aligned. fixp_error0 info: 0x3e911dd, fixp_error1 info: 0, fsmId:0, tslot:1, thread:0, ctxid:0, blk:5, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:0, dieId:1), serial number is 6, there is an exception of aivec error, core id is 11, error code = 0, dump info: pc start: 0x1242011fe000, current: 0x1242011fef4c, vec error info: 0xfb000000d7, mte error info: 0x97e0107ae, ifu error info: 0x210042c83bc00, ccu error info: 0x24e3bf27346e037f, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c2405a0000.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0, 0x800, 0) errorStr: The UB address accessed by the VEC instruction is not aligned. fixp_error0 info: 0xe0107ae, fixp_error1 info: 0x9, fsmId:0, tslot:1, thread:0, ctxid:0, blk:6, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:0, dieId:1), serial number is 6, there is an exception of aivec error, core id is 12, error code = 0, dump info: pc start: 0x1242011fe000, current: 0x1242011fef4c, vec error info: 0xfb000000d7, mte error info: 0x722c4b07f, ifu error info: 0x4169353c9e00, ccu error info: 0x80c0832e1343de00, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c2405a0000.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0, 0x800, 0) errorStr: The UB address accessed by the VEC instruction is not aligned. fixp_error0 info: 0x2c4b07f, fixp_error1 info: 0x7, fsmId:0, tslot:1, thread:0, ctxid:0, blk:7, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:0, dieId:1), serial number is 6, there is an exception of aivec error, core id is 13, error code = 0, dump info: pc start: 0x1242011fe000, current: 0x1242011fef4c, vec error info: 0xfb000000d7, mte error info: 0x7270472c44, ifu error info: 0x682705a3e2bc0, ccu error info: 0xd76ca17433c006c2, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c2405a0000.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0, 0x800, 0) errorStr: The UB address accessed by the VEC instruction is not aligned. fixp_error0 info: 0x472c44, fixp_error1 info: 0x72, fsmId:0, tslot:1, thread:0, ctxid:0, blk:8, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:0, dieId:1), serial number is 6, there is an exception of aivec error, core id is 14, error code = 0, dump info: pc start: 0x1242011fe000, current: 0x1242011fef4c, vec error info: 0xfb000000d7, mte error info: 0x31a93b897, ifu error info: 0x69f131f9d1c0, ccu error info: 0x108a07c228099e9b, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c2405a0000.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0, 0x800, 0) errorStr: The UB address accessed by the VEC instruction is not aligned. fixp_error0 info: 0xa93b897, fixp_error1 info: 0x3, fsmId:0, tslot:1, thread:0, ctxid:0, blk:9, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:0, dieId:1), serial number is 6, there is an exception of aivec error, core id is 15, error code = 0, dump info: pc start: 0x1242011fe000, current: 0x1242011fef4c, vec error info: 0xfb000000d7, mte error info: 0xa764e80075, ifu error info: 0x7e206deb2f380, ccu error info: 0xd043eecd7c4a2a9f, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c2405a0000.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0, 0x800, 0) errorStr: The UB address accessed by the VEC instruction is not aligned. fixp_error0 info: 0x4e80075, fixp_error1 info: 0xa7, fsmId:0, tslot:1, thread:0, ctxid:0, blk:10, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:0, dieId:1), serial number is 6, there is an exception of aivec error, core id is 16, error code = 0, dump info: pc start: 0x1242011fe000, current: 0x1242011fef4c, vec error info: 0xfb000000d7, mte error info: 0x4f6f3e6f2, ifu error info: 0x1b7f8fa62b980, ccu error info: 0x3007424348c0ab4a, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c2405a0000.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0, 0x800, 0) errorStr: The UB address accessed by the VEC instruction is not aligned. fixp_error0 info: 0x6f3e6f2, fixp_error1 info: 0x4, fsmId:0, tslot:1, thread:0, ctxid:0, blk:11, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:0, dieId:1), serial number is 6, there is an exception of aivec error, core id is 17, error code = 0, dump info: pc start: 0x1242011fe000, current: 0x1242011fef4c, vec error info: 0xfb000000d7, mte error info: 0x3de7cf31f9, ifu error info: 0x7d3baff1ef480, ccu error info: 0xbe754c683c794bb0, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c2405a0000.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0, 0x800, 0) errorStr: The UB address accessed by the VEC instruction is not aligned. fixp_error0 info: 0x7cf31f9, fixp_error1 info: 0x3d, fsmId:0, tslot:1, thread:0, ctxid:0, blk:12, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:0, dieId:1), serial number is 6, there is an exception of aivec error, core id is 18, error code = 0, dump info: pc start: 0x1242011fe000, current: 0x1242011fef4c, vec error info: 0xfb000000d7, mte error info: 0x81bf3732dc, ifu error info: 0x61ff266a18580, ccu error info: 0xfc5f8e457413266, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c2405a0000.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0, 0x800, 0) errorStr: The UB address accessed by the VEC instruction is not aligned. fixp_error0 info: 0xf3732dc, fixp_error1 info: 0x81, fsmId:0, tslot:1, thread:0, ctxid:0, blk:13, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:0, dieId:1), serial number is 6, there is an exception of aivec error, core id is 19, error code = 0, dump info: pc start: 0x1242011fe000, current: 0x1242011fef4c, vec error info: 0xfb000000d7, mte error info: 0x3a58a71b1b, ifu error info: 0x2006b6c7c0d00, ccu error info: 0xf20e589007ca76da, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c2405a0000.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0, 0x800, 0) errorStr: The UB address accessed by the VEC instruction is not aligned. fixp_error0 info: 0x8a71b1b, fixp_error1 info: 0x3a, fsmId:0, tslot:1, thread:0, ctxid:0, blk:14, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:0, dieId:1), serial number is 6, there is an exception of aivec error, core id is 20, error code = 0, dump info: pc start: 0x1242011fe000, current: 0x1242011fef4c, vec error info: 0xfb000000d7, mte error info: 0x70378c3457, ifu error info: 0x30792c8e02480, ccu error info: 0x864285bc3405e162, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c2405a0000.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0, 0x800, 0) errorStr: The UB address accessed by the VEC instruction is not aligned. fixp_error0 info: 0x78c3457, fixp_error1 info: 0x70, fsmId:0, tslot:1, thread:0, ctxid:0, blk:15, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:0, dieId:1), serial number is 6, there is an exception of aivec error, core id is 5, error code = 0, dump info: pc start: 0x1242011fe000, current: 0x1242011fef4c, vec error info: 0xfb000000d7, mte error info: 0x19830df729, ifu error info: 0x3403ba8187000, ccu error info: 0xf38ccb6277801026, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c2405a0000.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0, 0x800, 0) errorStr: The UB address accessed by the VEC instruction is not aligned. fixp_error0 info: 0x30df729, fixp_error1 info: 0x19, fsmId:1, tslot:1, thread:0, ctxid:0, blk:0, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       The error from device(chipId:0, dieId:1), serial number is 6, there is an exception of aivec error, core id is 6, error code = 0, dump info: pc start: 0x1242011fe000, current: 0x1242011fef4c, vec error info: 0xfb000000d7, mte error info: 0xf5fff275fe, ifu error info: 0xa06c40d98e00, ccu error info: 0x92e0a8051a9942cb, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c2405a0000.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
       The extend info: errcode:(0, 0x800, 0) errorStr: The UB address accessed by the VEC instruction is not aligned. fixp_error0 info: 0xff275fe, fixp_error1 info: 0xf5, fsmId:1, tslot:1, thread:0, ctxid:0, blk:1, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
       Kernel task happen error, retCode=0x31, [vector core exception].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_task.cc][LINE:1539]
       AIV Kernel happen error, retCode=0x31.[FUNC:GetError][FILE:stream.cc][LINE:1183]
       [AIC_INFO] after execute:args print end[FUNC:GetError][FILE:stream.cc][LINE:1183]
       Aicore kernel execute failed, device_id=1, stream_id=2, report_stream_id=2, task_id=24192, flip_num=0, fault kernel_name=_causal_conv1d_update_kernel_0, fault kernel info ext=_causal_conv1d_update_kernel, program id=471, hash=10336353875569349306.[FUNC:GetError][FILE:stream.cc][LINE:1183]
       rtStreamSynchronize execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
       synchronize stream failed, runtime result = 507035[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
 (function copy_between_host_and_device_opapi)
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720] EngineCore encountered a fatal error.
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720] Traceback (most recent call last):
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]   File "/home/vllm/vllm/v1/engine/core.py", line 711, in run_engine_core
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]     engine_core.run_busy_loop()
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]   File "/home/vllm/vllm/v1/engine/core.py", line 738, in run_busy_loop
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]     self._process_engine_step()
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]   File "/home/vllm/vllm/v1/engine/core.py", line 764, in _process_engine_step
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]     outputs, model_executed = self.step_fn()
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]                               ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]   File "/home/vllm/vllm/v1/engine/core.py", line 292, in step
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]     model_output = self.execute_model_with_error_logging(
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]   File "/home/vllm/vllm/v1/engine/core.py", line 278, in execute_model_with_error_logging
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]     raise err
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]   File "/home/vllm/vllm/v1/engine/core.py", line 269, in execute_model_with_error_logging
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]     return model_fn(scheduler_output)
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]            ^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]   File "/home/vllm/vllm/v1/executor/multiproc_executor.py", line 176, in execute_model
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]     (output, ) = self.collective_rpc(
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]                  ^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]   File "/home/vllm/vllm/v1/executor/multiproc_executor.py", line 259, in collective_rpc
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]     result = get_response(w, dequeue_timeout,
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]   File "/home/vllm/vllm/v1/executor/multiproc_executor.py", line 243, in get_response
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720]     raise RuntimeError(
(EngineCore_DP0 pid=931761) ERROR 09-19 07:42:16 [core.py:720] RuntimeError: Worker failed with error 'ACL stream synchronize failed, error code:507035', please check the stack trace above for the root cause
Traceback (most recent call last):
  File "/home/vllm-ascend/./examples/offline_inference_npu.py", line 48, in <module>
    main()
  File "/home/vllm-ascend/./examples/offline_inference_npu.py", line 40, in main
    outputs = llm.generate(prompts, sampling_params)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vllm/vllm/entrypoints/llm.py", line 396, in generate
    outputs = self._run_engine(use_tqdm=use_tqdm)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vllm/vllm/entrypoints/llm.py", line 1550, in _run_engine
    step_outputs = self.llm_engine.step()
                   ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vllm/vllm/v1/engine/llm_engine.py", line 248, in step
    outputs = self.engine_core.get_output()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vllm/vllm/v1/engine/core_client.py", line 670, in get_output
    raise self._format_exception(outputs) from None
vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
```
