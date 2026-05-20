# Issue #3024: [Bug]: Multiple calls (maybe >100) to eagle3-qwen3-8b often incurs "attn_mask index out of range"

## 基本信息

- **编号**: #3024
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3024
- **创建时间**: 2025-09-19T02:16:14Z
- **关闭时间**: 2025-09-28T10:09:27Z
- **更新时间**: 2025-09-28T10:09:27Z
- **提交者**: @liuruijin17
- **评论数**: 8

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

OS: EulerOS 2.0 (SP10) (aarch64)
GCC version: (GCC) 12.4.0
Clang version: Could not collect
CMake version: version 4.0.3
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
[pip3] gpytorch==1.12
[pip3] modelarts-pytorch-model-server==1.0.6
[pip3] mypy==1.15.0
[pip3] mypy-extensions==1.0.0
[pip3] numpy==1.26.4
[pip3] onnx==1.17.0
[pip3] onnxruntime==1.15.1
[pip3] optree==0.14.1
[pip3] pyzmq==26.2.1
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.dev20250724
[pip3] torchaudio==2.8.0
[pip3] torchvision==0.22.1
[pip3] transformers==4.56.1
[pip3] transformers-stream-generator==0.0.5
[pip3] zmq==0.0.0
[conda] gpytorch                  1.12                      <pip>
[conda] modelarts-pytorch-model-server 1.0.6                     <pip>
[conda] numpy                     1.26.4                    <pip>
[conda] optree                    0.14.1                    <pip>
[conda] pyzmq                     26.2.1                    <pip>
[conda] torch                     2.7.1+cpu                 <pip>
[conda] torch_npu                 2.7.1.dev20250724           <pip>
[conda] torchaudio                2.8.0                     <pip>
[conda] torchvision               0.22.1                    <pip>
[conda] transformers              4.56.1                    <pip>
[conda] transformers-stream-generator 0.0.5                     <pip>
[conda] zmq                       0.0.0                     <pip>
vLLM Version: 0.10.2
vLLM Ascend Version: 0.10.2rc2.dev21+g367edff5a (git sha: 367edff5a)

ENV Variables:
ASCEND_VISIBLE_DEVICES=7,0,1,2,3,4,5,6
ASCEND_RUNTIME_OPTIONS=
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/home/ma-user/tool/gcc-12.4.0/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/home/ma-user/tool/gcc-12.4.0/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/toolbox/latest/Ascend-DMI/lib64:/usr/lib/aarch64-linux-gnu/hdf5/serial:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/:/usr/local/seccomponent/lib/:/usr/local/seccomponent/lib/openssl/
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_HOME_PATH=/home/ma-user/Ascend/ascend-toolkit/latest
ASCEND_AUTOML_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0.3                 Version: 24.1.0.3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 94.7        54                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3396 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 94.9        52                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3394 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 95.6        51                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3201 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 92.6        52                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3201 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 99.6        52                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3381 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 97.4        54                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3200 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 94.9        54                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3201 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 97.3        51                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3200 / 65536         |
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
| No running processes found in NPU 7                                                            |
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

I use the modelarts so actually my CANN is installed in /home/ma-user and the CANN version is 8.2.RC1 in fact 


### 🐛 Describe the bug

I modify the main branch as PR #2979 did, however the eagle3 qwen3-8b serve enouters the error after I send multiple requests (>100), the full log can be found at comments in #2979 

```
python -m vllm.entrypoints.openai.api_server \
    --host 0.0.0.0 \
    --served-model-name Qwen3-8B-EAGLE3 \
    --port 8000 \
    --model /home/ma-user/work/Qwen/Qwen3-8B/ \
    --seed 42 \
    -tp 1 \
    --speculative_config '{"model": "/home/ma-user/work/Qwen/qwen3_8b_eagle3/", "draft_tensor_parallel_size": 1, "num_speculative_tokens": 5, "method": "eagle3"}'
```

The eagle3 model comes from [https://huggingface.co/Tengyunw/qwen3_8b_eagle3](url)

> [1;36m(APIServer pid=3829093)[0;0m INFO:     127.0.0.1:40084 - "POST /v1/chat/completions HTTP/1.1" 200 OK
[1;36m(APIServer pid=3829093)[0;0m INFO:     127.0.0.1:40084 - "POST /v1/chat/completions HTTP/1.1" 200 OK
[1;36m(APIServer pid=3829093)[0;0m INFO:     127.0.0.1:40084 - "POST /v1/chat/completions HTTP/1.1" 200 OK
...
[1;36m(APIServer pid=3829093)[0;0m INFO:     127.0.0.1:40084 - "POST /v1/chat/completions HTTP/1.1" 200 OK
[dump_input.py:69] Dumping input data for V1 LLM engine (v0.10.2) with config: model='/home/ma-user/work/Qwen/Qwen3-8B/', speculative_config=SpeculativeConfig(method='eagle3', model='/home/ma-user/work/Qwen/qwen3_8b_eagle3/', num_spec_tokens=5), tokenizer='/home/ma-user/work/Qwen/Qwen3-8B/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=40960, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=42, served_model_name=Qwen3-8B-EAGLE3, enable_prefix_caching=True, chunked_prefill_enabled=False, use_async_output_proc=False, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"/home/ma-user/.cache/vllm/torch_compile_cache/51a4d962d9","backend":"","custom_ops":["all"],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.mamba_mixer2","vllm.mamba_mixer","vllm.short_conv","vllm.linear_attention","vllm.plamo2_mamba_mixer","vllm.gdn_attention","vllm.unified_ascend_attention_with_output","vllm.mla_forward","vllm.unified_ascend_attention_with_output","vllm.mla_forward"],"use_inductor":false,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":1,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,488,480,464,456,440,432,416,408,392,384,368,360,344,336,328,312,304,288,280,264,256,240,232,216,208,192,184,168,160,152,136,128,112,104,88,80,64,56,40,32,16,8,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"pass_config":{},"max_capture_size":512,"local_cache_dir":"/home/ma-user/.cache/vllm/torch_compile_cache/51a4d962d9/rank_0_0/backbone"}, 
[dump_input.py:76] Dumping scheduler output for model execution: SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=chatcmpl-18bd9df5acdf4f468db76d5884cc73ce,prompt_token_ids_len=246,mm_kwargs=[],mm_hashes=[],mm_positions=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.6, top_p=0.95, top_k=20, min_p=0.0, seed=None, stop=[], stop_token_ids=[151643], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=25, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([23, 24],),num_computed_tokens=0,lora_request=None), NewRequestData(req_id=chatcmpl-ee6bd0d7da8a433a8b9426c0f68c8e70,prompt_token_ids_len=6193,mm_kwargs=[],mm_hashes=[],mm_positions=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.6, top_p=0.95, top_k=20, min_p=0.0, seed=None, stop=[], stop_token_ids=[151643], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=471, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73],),num_computed_tokens=0,lora_request=None), NewRequestData(req_id=chatcmpl-6ba000abf7034c5aa563a60a60f431b9,prompt_token_ids_len=10163,mm_kwargs=[],mm_hashes=[],mm_positions=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.6, top_p=0.95, top_k=20, min_p=0.0, seed=None, stop=[], stop_token_ids=[151643], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=434, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([20, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125],),num_computed_tokens=3584,lora_request=None), NewRequestData(req_id=chatcmpl-012f3d62612246a78b0a370057659930,prompt_token_ids_len=7840,mm_kwargs=[],mm_hashes=[],mm_positions=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.6, top_p=0.95, top_k=20, min_p=0.0, seed=None, stop=[], stop_token_ids=[151643], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=428, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([20, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159],),num_computed_tokens=3584,lora_request=None), NewRequestData(req_id=chatcmpl-5a89b9105dd14eda80fa60ee23a8771f,prompt_token_ids_len=241,mm_kwargs=[],mm_hashes=[],mm_positions=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.6, top_p=0.95, top_k=20, min_p=0.0, seed=None, stop=[], stop_token_ids=[151643], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=118, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([160, 161],),num_computed_tokens=0,lora_request=None), NewRequestData(req_id=chatcmpl-0cdc6d04f5224141aee99feb294a4581,prompt_token_ids_len=3427,mm_kwargs=[],mm_hashes=[],mm_positions=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.6, top_p=0.95, top_k=20, min_p=0.0, seed=None, stop=[], stop_token_ids=[151643], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=459, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188],),num_computed_tokens=0,lora_request=None)], scheduled_cached_reqs=CachedRequestData(req_ids=[], resumed_from_preemption=[], new_token_ids=[], new_block_ids=[], num_computed_tokens=[]), num_scheduled_tokens={chatcmpl-5a89b9105dd14eda80fa60ee23a8771f: 241, chatcmpl-012f3d62612246a78b0a370057659930: 4256, chatcmpl-18bd9df5acdf4f468db76d5884cc73ce: 246, chatcmpl-ee6bd0d7da8a433a8b9426c0f68c8e70: 6193, chatcmpl-0cdc6d04f5224141aee99feb294a4581: 3427, chatcmpl-6ba000abf7034c5aa563a60a60f431b9: 6579}, total_num_scheduled_tokens=20942, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={}, num_common_prefix_blocks=[0], finished_req_ids=[], free_encoder_mm_hashes=[], structured_output_request_ids={}, grammar_bitmask=null, kv_connector_metadata=null)
[dump_input.py:79] Dumping scheduler stats: SchedulerStats(num_running_reqs=7, num_waiting_reqs=0, step_counter=0, current_wave=0, kv_cache_usage=0.09224890829694321, prefix_cache_stats=PrefixCacheStats(reset=False, requests=6, queries=28110, hits=7168), spec_decoding_stats=None, num_corrupted_reqs=0)
[core.py:720] EngineCore encountered a fatal error.
[core.py:720] Traceback (most recent call last):
[core.py:720]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 711, in run_engine_core
[core.py:720]     engine_core.run_busy_loop()
[core.py:720]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 738, in run_busy_loop
[core.py:720]     self._process_engine_step()
[core.py:720]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 764, in _process_engine_step
[core.py:720]     outputs, model_executed = self.step_fn()
[core.py:720]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 292, in step
[core.py:720]     model_output = self.execute_model_with_error_logging(
[core.py:720]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 278, in execute_model_with_error_logging
[core.py:720]     raise err
[core.py:720]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 269, in execute_model_with_error_logging
[core.py:720]     return model_fn(scheduler_output)
[core.py:720]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/vllm/v1/executor/abstract.py", line 93, in execute_model
[core.py:720]     output = self.collective_rpc("execute_model",
[core.py:720]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 58, in collective_rpc
[core.py:720]     answer = run_method(self.driver_worker, method, args, kwargs)
[core.py:720]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/vllm/utils/__init__.py", line 3060, in run_method
[core.py:720]     return func(*args, **kwargs)
[core.py:720]   File "/home/ma-user/work/rickl/code/it_mksim/vllm_plugins/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 231, in execute_model
[core.py:720]     output = self.model_runner.execute_model(scheduler_output,
[core.py:720]   File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[core.py:720]     return func(*args, **kwargs)
[core.py:720]   File "/home/ma-user/work/rickl/code/it_mksim/vllm_plugins/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1995, in execute_model
[core.py:720]     self._draft_token_ids = self.propose_draft_token_ids(
[core.py:720]   File "/home/ma-user/work/rickl/code/it_mksim/vllm_plugins/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1642, in propose_draft_token_ids
[core.py:720]     draft_token_ids = self.drafter.generate_token_ids(
[core.py:720]   File "/home/ma-user/work/rickl/code/it_mksim/vllm_plugins/vllm-ascend/vllm_ascend/spec_decode/eagle_proposer.py", line 860, in generate_token_ids
[core.py:720]     draft_token_ids = self._propose(
[core.py:720]   File "/home/ma-user/work/rickl/code/it_mksim/vllm_plugins/vllm-ascend/vllm_ascend/spec_decode/eagle_proposer.py", line 1223, in _propose
[core.py:720]     attn_mask = self.attn_mask_builder.get_splitfuse_attn_mask(
[core.py:720]   File "/home/ma-user/work/rickl/code/it_mksim/vllm_plugins/vllm-ascend/vllm_ascend/attention/attention_mask.py", line 82, in get_splitfuse_attn_mask
[core.py:720]     attn_mask = torch.index_select(self.attn_mask_cache,
[core.py:720] IndexError: index out of range in self
