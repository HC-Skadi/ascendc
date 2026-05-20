# Issue #2667: [Bug]: Eagle3 Spec Decode failure

## 基本信息

- **编号**: #2667
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2667
- **创建时间**: 2025-09-01T03:26:30Z
- **关闭时间**: 2025-09-11T01:26:52Z
- **更新时间**: 2025-09-11T01:26:52Z
- **提交者**: @wxsIcey
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment
<details>
<summary>The output of `python collect_env.py`</summary>

```text
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
| npu-smi 24.1.rc3.7               Version: 24.1.rc3.7                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 178.9       36                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          3412 / 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           36                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          3189 / 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 186.1       36                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          3413 / 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           36                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          3185 / 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 176.3       36                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3412 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           37                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          3186 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 177.9       36                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3412 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           36                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          3185 / 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 180.9       37                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          3402 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           36                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          3198 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 189.1       37                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          3398 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           36                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          3201 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 183.0       38                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          3400 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           37                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          3200 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 186.2       37                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          3413 / 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           37                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          3188 / 65536         |
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
os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"
from vllm import LLM, SamplingParams


def main():
    
    prompts = [
        "please repeat the word 'hello' 10 times. give no other output than the word at least ten times in a row, in lowercase with spaces between each word and without quotes."
    ]
    
    sampling_params = SamplingParams(temperature=0.8)
    
    speculative_config = {
        "method": "eagle3",
        "model": "/root/.cache/modelscope/hub/models/vllm-ascend/EAGLE3-LLaMA3.1-Instruct-8B",
        "num_speculative_tokens": 1,
        "max_model_len": 128,
    }
    
    llm = LLM(
        model="LLM-Research/Meta-Llama-3.1-8B-Instruct",
        enable_chunked_prefill=True,
        max_num_seqs=1,
        max_num_batched_tokens=2048,
        enforce_eager=True,
        gpu_memory_utilization=0.8,
        speculative_config=speculative_config,
        max_model_len=128,
    )
    
    
    outputs = llm.generate(prompts, sampling_params=sampling_params)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")

if __name__ == "__main__":
    main()

```
```text
root@liteserver-for-vllm-ascend-00001:/home/vllm-ascend# python ./examples/test_spec_decode_eagle.py 
INFO 09-02 03:31:34 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-02 03:31:34 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-02 03:31:34 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-02 03:31:34 [__init__.py:232] Platform plugin ascend is activated
WARNING 09-02 03:31:35 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 09-02 03:31:35 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 09-02 03:31:35 [registry.py:478] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 09-02 03:31:35 [registry.py:478] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 09-02 03:31:35 [registry.py:478] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 09-02 03:31:35 [registry.py:478] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 09-02 03:31:35 [registry.py:478] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3:CustomDeepseekV3ForCausalLM.
WARNING 09-02 03:31:35 [registry.py:478] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 09-02 03:31:35 [registry.py:478] Model architecture Qwen3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3:CustomQwen3ForCausalLM.
INFO 09-02 03:31:35 [utils.py:328] non-default args: {'max_model_len': 128, 'gpu_memory_utilization': 0.8, 'max_num_batched_tokens': 2048, 'max_num_seqs': 1, 'disable_log_stats': True, 'enforce_eager': True, 'enable_chunked_prefill': True, 'speculative_config': {'method': 'eagle3', 'model': '/root/.cache/modelscope/hub/models/vllm-ascend/EAGLE3-LLaMA3.1-Instruct-8B', 'num_speculative_tokens': 2, 'max_model_len': 128}, 'model': 'LLM-Research/Meta-Llama-3.1-8B-Instruct'}
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3.1-8B-Instruct
2025-09-02 03:31:37,475 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3.1-8B-Instruct
2025-09-02 03:31:38,910 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3.1-8B-Instruct
2025-09-02 03:31:40,062 - modelscope - INFO - Target directory already exists, skipping creation.
INFO 09-02 03:31:48 [__init__.py:744] Resolved architecture: LlamaForCausalLM
`torch_dtype` is deprecated! Use `dtype` instead!
INFO 09-02 03:31:48 [__init__.py:1773] Using max model len 128
INFO 09-02 03:31:49 [__init__.py:744] Resolved architecture: LlamaForCausalLM
WARNING 09-02 03:31:49 [__init__.py:2884] Casting torch.float16 to torch.bfloat16.
INFO 09-02 03:31:49 [__init__.py:1773] Using max model len 2048
INFO 09-02 03:31:49 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=2048.
WARNING 09-02 03:31:49 [scheduler.py:269] max_num_batched_tokens (2048) exceeds max_num_seqs * max_model_len (128). This may lead to unexpected behavior.
WARNING 09-02 03:31:49 [scheduler.py:269] max_num_batched_tokens (2048) exceeds max_num_seqs * max_model_len (128). This may lead to unexpected behavior.
INFO 09-02 03:31:49 [platform.py:144] Compilation disabled, using eager mode by default
WARNING 09-02 03:31:49 [platform.py:162] compilation_config.level = CompilationLevel.NO_COMPILATION is set, Setting CUDAGraphMode to NONE
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3.1-8B-Instruct
2025-09-02 03:31:50,186 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3.1-8B-Instruct
2025-09-02 03:31:51,968 - modelscope - INFO - Target directory already exists, skipping creation.
INFO 09-02 03:31:58 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-02 03:31:58 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-02 03:31:58 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-02 03:31:58 [__init__.py:232] Platform plugin ascend is activated
WARNING 09-02 03:31:59 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(EngineCore_0 pid=1440043) INFO 09-02 03:31:59 [core.py:648] Waiting for init message from front-end.
(EngineCore_0 pid=1440043) INFO 09-02 03:31:59 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
(EngineCore_0 pid=1440043) WARNING 09-02 03:31:59 [registry.py:478] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
(EngineCore_0 pid=1440043) WARNING 09-02 03:31:59 [registry.py:478] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
(EngineCore_0 pid=1440043) WARNING 09-02 03:31:59 [registry.py:478] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
(EngineCore_0 pid=1440043) WARNING 09-02 03:31:59 [registry.py:478] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
(EngineCore_0 pid=1440043) WARNING 09-02 03:31:59 [registry.py:478] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3:CustomDeepseekV3ForCausalLM.
(EngineCore_0 pid=1440043) WARNING 09-02 03:31:59 [registry.py:478] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
(EngineCore_0 pid=1440043) WARNING 09-02 03:31:59 [registry.py:478] Model architecture Qwen3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3:CustomQwen3ForCausalLM.
(EngineCore_0 pid=1440043) INFO 09-02 03:31:59 [core.py:75] Initializing a V1 LLM engine (v0.9.1) with config: model='LLM-Research/Meta-Llama-3.1-8B-Instruct', speculative_config=SpeculativeConfig(method='eagle3', model='/root/.cache/modelscope/hub/models/vllm-ascend/EAGLE3-LLaMA3.1-Instruct-8B', num_spec_tokens=2), tokenizer='LLM-Research/Meta-Llama-3.1-8B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=128, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=True, kv_cache_dtype=auto, device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=LLM-Research/Meta-Llama-3.1-8B-Instruct, enable_prefix_caching=True, chunked_prefill_enabled=True, use_async_output_proc=False, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":null,"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":0,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"pass_config":{},"max_capture_size":0,"local_cache_dir":null}
INFO 09-02 03:32:09 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 09-02 03:32:09 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 09-02 03:32:09 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 09-02 03:32:09 [__init__.py:232] Platform plugin ascend is activated
WARNING 09-02 03:32:10 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
[rank0]:[W902 03:32:12.046387634 ProcessGroupGloo.cpp:727] Warning: Unable to resolve hostname to a (local) address. Using the loopback address as fallback. Manually set the network interface to bind to with GLOO_SOCKET_IFNAME. (function operator())
(EngineCore_0 pid=1440043) INFO 09-02 03:32:12 [parallel_state.py:1134] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
(EngineCore_0 pid=1440043) INFO 09-02 03:32:12 [model_runner_v1.py:2282] Starting to load model LLM-Research/Meta-Llama-3.1-8B-Instruct...
(EngineCore_0 pid=1440043) Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3.1-8B-Instruct
(EngineCore_0 pid=1440043) 2025-09-02 03:32:14,223 - modelscope - INFO - Target directory already exists, skipping creation.
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:00<00:01,  1.84it/s]
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:01<00:01,  1.56it/s]
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:01<00:00,  2.02it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:02<00:00,  1.95it/s]
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:02<00:00,  1.90it/s]
(EngineCore_0 pid=1440043) 
(EngineCore_0 pid=1440043) INFO 09-02 03:32:16 [default_loader.py:267] Loading weights took 2.31 seconds
(EngineCore_0 pid=1440043) INFO 09-02 03:32:16 [model_runner_v1.py:2298] Loading drafter model...
Loading pt checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading pt checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  2.33it/s]
Loading pt checkpoint shards: 100% Completed | 1/1 [00:00<00:00,  2.33it/s]
(EngineCore_0 pid=1440043) 
(EngineCore_0 pid=1440043) INFO 09-02 03:32:17 [default_loader.py:267] Loading weights took 0.60 seconds
(EngineCore_0 pid=1440043) INFO 09-02 03:32:17 [eagle_proposer_v1.py:332] The EAGLE head shares the same vocab embedding with the target model.
(EngineCore_0 pid=1440043) INFO 09-02 03:32:17 [model_runner_v1.py:2312] Loading model weights took 15.7847 GB
(EngineCore_0 pid=1440043) INFO 09-02 03:32:19 [worker_v1.py:190] Available memory: 34184553369, total memory: 65464696832
(EngineCore_0 pid=1440043) INFO 09-02 03:32:19 [kv_cache_utils.py:850] GPU KV cache size: 252,800 tokens
(EngineCore_0 pid=1440043) INFO 09-02 03:32:19 [kv_cache_utils.py:854] Maximum concurrency for 128 tokens per request: 1975.00x
(EngineCore_0 pid=1440043) INFO 09-02 03:32:19 [core.py:217] init engine (profile, create kv cache, warmup model) took 1.80 seconds
(EngineCore_0 pid=1440043) Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3.1-8B-Instruct
(EngineCore_0 pid=1440043) 2025-09-02 03:32:20,972 - modelscope - INFO - Target directory already exists, skipping creation.
(EngineCore_0 pid=1440043) INFO 09-02 03:32:21 [platform.py:144] Compilation disabled, using eager mode by default
(EngineCore_0 pid=1440043) WARNING 09-02 03:32:21 [platform.py:162] compilation_config.level = CompilationLevel.NO_COMPILATION is set, Setting CUDAGraphMode to NONE
INFO 09-02 03:32:21 [llm.py:285] Supported_tasks: ['generate']
INFO 09-02 03:32:21 [__init__.py:36] No IOProcessor plugins requested by the model
Adding requests: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 77.28it/s]
Processed prompts:   0%|                                                                                                              | 0/1 [00:00<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s](EngineCore_0 pid=1440043) WARNING 09-02 03:32:21 [cudagraph_dispatcher.py:102] cudagraph dispatching keys are not initialized. No cudagraph will be used.
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [dump_input.py:69] Dumping input data for V1 LLM engine (v0.9.1) with config: model='LLM-Research/Meta-Llama-3.1-8B-Instruct', speculative_config=SpeculativeConfig(method='eagle3', model='/root/.cache/modelscope/hub/models/vllm-ascend/EAGLE3-LLaMA3.1-Instruct-8B', num_spec_tokens=2), tokenizer='LLM-Research/Meta-Llama-3.1-8B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=128, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=True, kv_cache_dtype=auto, device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=LLM-Research/Meta-Llama-3.1-8B-Instruct, enable_prefix_caching=True, chunked_prefill_enabled=True, use_async_output_proc=False, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":null,"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":0,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"pass_config":{},"max_capture_size":0,"local_cache_dir":null}, 
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [dump_input.py:76] Dumping scheduler output for model execution: SchedulerOutput(scheduled_new_reqs=[], scheduled_cached_reqs=CachedRequestData(req_ids=['0'], resumed_from_preemption=[false], new_token_ids=[], new_block_ids=[null], num_computed_tokens=[38]), num_scheduled_tokens={0: 3}, total_num_scheduled_tokens=3, scheduled_spec_decode_tokens={0: [912, 1005]}, scheduled_encoder_inputs={}, num_common_prefix_blocks=[1], finished_req_ids=[], free_encoder_mm_hashes=[], structured_output_request_ids={}, grammar_bitmask=null, kv_connector_metadata=null)
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714] EngineCore encountered a fatal error.
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714] Traceback (most recent call last):
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]   File "/home/vllm/vllm/v1/engine/core.py", line 705, in run_engine_core
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]     engine_core.run_busy_loop()
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]   File "/home/vllm/vllm/v1/engine/core.py", line 732, in run_busy_loop
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]     self._process_engine_step()
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]   File "/home/vllm/vllm/v1/engine/core.py", line 758, in _process_engine_step
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]     outputs, model_executed = self.step_fn()
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]                               ^^^^^^^^^^^^^^
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]   File "/home/vllm/vllm/v1/engine/core.py", line 291, in step
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]     model_output = self.execute_model_with_error_logging(
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]   File "/home/vllm/vllm/v1/engine/core.py", line 277, in execute_model_with_error_logging
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]     raise err
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]   File "/home/vllm/vllm/v1/engine/core.py", line 268, in execute_model_with_error_logging
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]     return model_fn(scheduler_output)
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]            ^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]   File "/home/vllm/vllm/v1/executor/abstract.py", line 93, in execute_model
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]     output = self.collective_rpc("execute_model",
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]   File "/home/vllm/vllm/executor/uniproc_executor.py", line 58, in collective_rpc
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]     answer = run_method(self.driver_worker, method, args, kwargs)
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]   File "/home/vllm/vllm/utils/__init__.py", line 3045, in run_method
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]     return func(*args, **kwargs)
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]   File "/home/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 205, in execute_model
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]     output = self.model_runner.execute_model(scheduler_output,
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]     return func(*args, **kwargs)
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]   File "/home/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1862, in execute_model
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]     self._draft_token_ids = self.propose_draft_token_ids(
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]   File "/home/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1523, in propose_draft_token_ids
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]     draft_token_ids = self._generate_eagle3_token_ids(
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]   File "/home/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2692, in _generate_eagle3_token_ids
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]     draft_token_ids = self.drafter.propose(
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]                       ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]   File "/home/vllm-ascend/vllm_ascend/worker/eagle_proposer_v1.py", line 166, in propose
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]     sample_hidden_states = last_hidden_states[last_token_indices]
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]                            ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714] RuntimeError: checkUceErrAndRepair:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:200 NPU error, error code is 507899
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714] [ERROR] 2025-09-02-03:32:24 (PID:1440043, Device:0, RankID:-1) ERR00100 PTA call acl api failed
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714] [Error]: An internal error occurs in the Driver module. 
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]         Rectify the fault based on the error information in the ascend log.
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714] EZ9999: Inner Error!
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714] EZ9999: [PID: 1440043] 2025-09-02-03:32:24.130.271 The error from device(chipId:0, dieId:0), serial number is 3, there is an exception of fftsplus aicore error, core id is 2, error code = 0x800000, dump info: pc start: 0x124000cd0280, current: 0x124000cd10d8, vec error info: 0, mte error info: 0x41030000ed, ifu error info: 0x719fb20d89900, ccu error info: 0x4694fd483906733d, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c100340080.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:303]
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]         TraceBack (most recent call last):
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]        The extend info: errcode:(0x800000, 0, 0) errorStr: The DDR address of the MTE instruction is out of range. fixp_error0 info: 0x30000ed, fixp_error1 info: 0x41, fsmId:0, tslot:3, thread:0, ctxid:0, blk:12, sublk:0, subErrType:4.[FUNC:ProcessStarsCoreErrorInfo][FILE:device_error_core_proc.cc][LINE:322]
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]        Kernel task happen error, retCode=0x26, [aicore exception].[FUNC:PreCheckTaskErr][FILE:davinci_kernel_task.cc][LINE:1539]
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]        AICORE Kernel task happen error, retCode=0x26.[FUNC:GetError][FILE:stream.cc][LINE:1183]
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]        [AIC_INFO] after execute:args print end[FUNC:GetError][FILE:stream.cc][LINE:1183]
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]        [AIC_INFO] after execute:mixCtx print end[FUNC:GetError][FILE:stream.cc][LINE:1183]
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]        Aicore kernel execute failed, device_id=0, stream_id=2, report_stream_id=2, task_id=4637, flip_num=0, fault kernel_name=paged_attention_mask_33_mix_aic, fault kernel info ext=none, program id=295, hash=11792324042040180237.[FUNC:GetError][FILE:stream.cc][LINE:1183]
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]        rtStreamSynchronize execute failed, reason=[device mem error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]        synchronize stream failed, runtime result = 507053[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]        rtGetMemUceInfo execute failed, reason=[driver error:internal error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714]        [Call][Rts]call rts api [rtGetMemUceInfo] failed, retCode is 507899[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(EngineCore_0 pid=1440043) ERROR 09-02 03:32:24 [core.py:714] 
Traceback (most recent call last):
  File "/home/vllm-ascend/./examples/test_spec_decode_eagle.py", line 44, in <module>
    main()
  File "/home/vllm-ascend/./examples/test_spec_decode_eagle.py", line 37, in main
    outputs = llm.generate(prompts, sampling_params=sampling_params)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vllm/vllm/entrypoints/llm.py", line 386, in generate
    outputs = self._run_engine(use_tqdm=use_tqdm)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vllm/vllm/entrypoints/llm.py", line 1499, in _run_engine
    step_outputs = self.llm_engine.step()
                   ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vllm/vllm/v1/engine/llm_engine.py", line 241, in step
    outputs = self.engine_core.get_output()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/vllm/vllm/v1/engine/core_client.py", line 668, in get_output
    raise self._format_exception(outputs) from None
vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
[ERROR] 2025-09-02-03:32:24 (PID:1439433, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
Processed prompts:   0%|                                                                                                              | 0/1 [00:08<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s]
root@liteserver-for-vllm-ascend-00001:/home/vllm-ascend# /usr/local/python3.11.13/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
```

