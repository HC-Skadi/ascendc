# Issue #1682: [Bug]: Assertion `(0 <= val && val < this->gxSize_)' Index 2938 out of range[0 2938)!

## 基本信息

- **编号**: #1682
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1682
- **创建时间**: 2025-07-09T02:31:34Z
- **关闭时间**: 2025-07-09T06:41:46Z
- **更新时间**: 2025-07-09T06:41:46Z
- **提交者**: @JackeyGuo
- **评论数**: 2

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

OS: Huawei Cloud EulerOS 2.0 (aarch64) (aarch64)
GCC version: (GCC) 10.3.1
Clang version: Could not collect
CMake version: version 4.0.2
Libc version: glibc-2.34

Python version: 3.10.8 (main, Jun  6 2025, 16:03:58) [GCC 10.3.1] (64-bit runtime)
Python platform: Linux-4.19.90-vhulk2211.3.0.h1543.eulerosv2r10.aarch64-aarch64-with-glibc2.34

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       HiSilicon
Model name:                      Kunpeng-920
Model:                           0
Thread(s) per core:              1
Core(s) per cluster:             48
Socket(s):                       -
Cluster(s):                      4
Stepping:                        0x1
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       12 MiB (192 instances)
L1i cache:                       12 MiB (192 instances)
L2 cache:                        96 MiB (192 instances)
L3 cache:                        192 MiB (8 instances)
NUMA node(s):                    8
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

Versions of relevant libraries:
[pip3] moxing-pytorch==2.0.1.rc0.b9ef8876
[pip3] numpy==1.26.4
[pip3] pynvml==12.0.0
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.post1.dev20250619
[pip3] torchaudio==2.7.0
[pip3] torchvision==0.20.1
[pip3] transformers==4.52.4
[pip3] transformers-stream-generator==0.0.5
[conda] No relevant packages
vLLM Version: 0.9.1
vLLM Ascend Version: 0.9.1rc2.dev0+gc30ddb8.d20250709 (git sha: c30ddb8, date: 20250709)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=1,7
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
PYTORCH_NPU_ALLOC_CONF=garbage_collection_threshold:0.95,max_split_size_mb:250
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/BiShengCompiler-4.1.0-aarch64-linux/lib:/usr/local/Ascend/toolbox/latest/Ascend-DMI/lib64:/usr/lib/aarch64-linux-gnu/hdf5/serial:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/:/usr/local/seccomponent/lib/:/usr/local/seccomponent/lib/openssl/:/usr/local/mindspore-lite/mindspore-lite-2.4.0-linux-aarch64/tools/converter/lib:/usr/local/mindspore-lite/mindspore-lite-2.4.0-linux-aarch64/runtime/lib:/usr/local/mindspore-lite/mindspore-lite-2.4.0-linux-aarch64/runtime/third_party/dnnl
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_AUTOML_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools
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
| npu-smi 23.0.5                   Version: 23.0.5                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 1     910B1               | OK            | 103.7       50                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3356 / 65536         |
+===========================+===============+====================================================+
| 7     910B1               | OK            | 100.1       51                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3353 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux

```

</details>


### 🐛 Describe the bug

[ASSERT] [CANN_VERSION : 8.1.RC1][TimeStamp : 0] /home/slave1/Ascend/8.1.RC1/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/gather_v3/gather_v3_base.h:137: Assertion `(0 <= val && val < this->gxSize_)' Index 2938 out of range[0 2938)!
[rank0]:[W709 09:55:41.717035978 compiler_depend.ts:188] Warning: EZ9999: Inner Error!
EZ9999: [PID: 4167087] 2025-07-09-09:55:37.362.309 The error from device(chipId:1, dieId:0), serial number is 3, there is an aivec error exception, core id is 4, error code = 0, dump info: pc start: 0x1240c3096f34, current: 0x1240c3097e24, vec error info: 0x770144e00c, mte error info: 0xcbfadd258f, ifu error info: 0x763f97af9dc0, ccu error info: 0x9ec1cf5034371f29, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd000288, para base: 0x1241005cec00.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_proc.cc][LINE:1434]
        TraceBack (most recent call last):
       The extend info: errcode:(0, 0, 0) errorStr: timeout or trap error. fixp_error0 info: 0xadd258f, fixp_error1 info: 0xcb, fsmId:1, tslot:2, thread:0, ctxid:0, blk:45, sublk:0, subErrType:2.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_proc.cc][LINE:1446]
       Kernel task happen error, retCode=0x31, [vector core exception].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_task.cc][LINE:1366]
       AIV Kernel happen error, retCode=0x31.[FUNC:GetError][FILE:stream.cc][LINE:1119]
       Aicore kernel execute failed, device_id=0, stream_id=2, report_stream_id=2, task_id=28475, flip_num=25, fault kernel_name=GatherV3_7869a97190b9b4d296d9414a005b954b_high_performance_80330, fault kernel info ext=none, program id=348, hash=5015448876688064660.[FUNC:GetError][FILE:stream.cc][LINE:1119]
       [AIC_INFO] after execute:args print end[FUNC:GetError][FILE:stream.cc][LINE:1119]
       rtStreamSynchronizeWithTimeout execute failed, reason=[vector core exception][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
       synchronize stream failed, runtime result = 507035[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
 (function recordEvent)
ERROR 07-09 09:55:41 [dump_input.py:69] Dumping input data
ERROR 07-09 09:55:41 [dump_input.py:71] V1 LLM engine (v0.9.1) with config: model='/home/ma-user/work/guofeng/models/Qwen2.5-VL-7B-Instruct', speculative_config=None, tokenizer='/home/ma-user/work/guofeng/models/Qwen2.5-VL-7B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=16384, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=/home/ma-user/work/guofeng/models/Qwen2.5-VL-7B-Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=True, chunked_prefill_enabled=True, use_async_output_proc=True, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"/home/ma-user/.cache/vllm/torch_compile_cache/a4343c18fc","backend":"","custom_ops":["all"],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.unified_ascend_attention_with_output","vllm.unified_ascend_attention_with_output","vllm.unified_ascend_attention_with_output"],"use_inductor":false,"compile_sizes":[],"inductor_compile_config":{},"inductor_passes":{},"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416,408,400,392,384,376,368,360,352,344,336,328,320,312,304,296,288,280,272,264,256,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"max_capture_size":512,"local_cache_dir":"/home/ma-user/.cache/vllm/torch_compile_cache/a4343c18fc/rank_0_0"}, 
ERROR 07-09 09:55:41 [dump_input.py:79] Dumping scheduler output for model execution:
ERROR 07-09 09:55:41 [dump_input.py:80] SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=chatcmpl-8916bae552d94a1d9addaf603f7fe197,prompt_token_ids_len=2938,mm_inputs=[{'image_grid_thw': tensor([[  1,  78, 138]]), 'pixel_values': tensor([[-1.7923, -1.7923, -1.7923,  ..., -1.4802, -1.4802, -1.4802],
ERROR 07-09 09:55:41 [dump_input.py:80]         [-1.7923, -1.7923, -1.7923,  ..., -1.4802, -1.4802, -1.4802],
ERROR 07-09 09:55:41 [dump_input.py:80]         [-1.7923, -1.7923, -1.7923,  ..., -1.4802, -1.4802, -1.4802],
ERROR 07-09 09:55:41 [dump_input.py:80]         ...,
ERROR 07-09 09:55:41 [dump_input.py:80]         [-1.7923, -1.7923, -1.7923,  ..., -1.4802, -1.4802, -1.4802],
ERROR 07-09 09:55:41 [dump_input.py:80]         [-1.7923, -1.7923, -1.7923,  ..., -1.4802, -1.4802, -1.4802],
ERROR 07-09 09:55:41 [dump_input.py:80]         [-1.7923, -1.7923, -1.7923,  ..., -1.4802, -1.4802, -1.4802]])}],mm_hashes=['92dbec2feb716d136cef8083160fc767364138e8e0f9c745e38ca7e09fcbac49'],mm_positions=[PlaceholderRange(offset=241, length=2691, is_embed=None)],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.05, temperature=0.3, top_p=0.8, top_k=1, min_p=0.0, seed=None, stop=[], stop_token_ids=[151643], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=10000, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([4671, 4672, 4673, 4674, 4675, 4676, 4677, 4678, 4679, 4680, 4681, 4682, 4683, 4684, 4685, 4686, 4687, 4688, 4689, 4690, 4691, 4692, 4701],),num_computed_tokens=2816,lora_request=None)], scheduled_cached_reqs=[], num_scheduled_tokens={chatcmpl-8916bae552d94a1d9addaf603f7fe197: 122}, total_num_scheduled_tokens=122, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={chatcmpl-8916bae552d94a1d9addaf603f7fe197: [0]}, num_common_prefix_blocks=[23], finished_req_ids=[], free_encoder_input_ids=[], structured_output_request_ids={}, grammar_bitmask=null, kv_connector_metadata=null)
ERROR 07-09 09:55:41 [dump_input.py:82] SchedulerStats(num_running_reqs=1, num_waiting_reqs=0, gpu_cache_usage=0.004772320540862962, prefix_cache_stats=PrefixCacheStats(reset=False, requests=1, queries=2938, hits=2816), spec_decoding_stats=None)


BUG复现条件：使用vllm server部署qwen2.5vl-7b后，第一次请求一切正常，当我手动中断后，第二次请求大约4-5次后报错。
