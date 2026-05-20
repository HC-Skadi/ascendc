# Issue #382: [Bug]: Qwen2.5 VL failed

## 基本信息

- **编号**: #382
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/382
- **创建时间**: 2025-03-24T09:13:14Z
- **关闭时间**: 2025-03-25T07:27:21Z
- **更新时间**: 2025-03-25T07:29:36Z
- **提交者**: @zxy-111122
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

/home/ma-user/python3.10/lib/python3.10/site-packages/torch_npu/utils/collect_env.py:58: UserWarning: Warning: The /usr/local/Ascend/ascend-toolkit/latest owner does not match the current owner.
  warnings.warn(f"Warning: The {path} owner does not match the current owner.")
/home/ma-user/python3.10/lib/python3.10/site-packages/torch_npu/utils/collect_env.py:58: UserWarning: Warning: The /usr/local/Ascend/ascend-toolkit/8.0.RC2/aarch64-linux/ascend_toolkit_install.info owner does not match the current owner.
  warnings.warn(f"Warning: The {path} owner does not match the current owner.")
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: EulerOS 2.0 (SP10) (aarch64)
GCC version: (GCC) 7.3.0
Clang version: Could not collect
CMake version: version 3.16.5
Libc version: glibc-2.28

Python version: 3.10.4 (main, Mar 24 2025, 09:38:57) [GCC 7.3.0] (64-bit runtime)
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
[pip3] pyzmq==26.3.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250308
[pip3] torchaudio==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.49.0.dev0
[conda] modelarts-pytorch-model-server-arm 1.0.6                     <pip>
[conda] numpy                     1.22.0                    <pip>
[conda] pyzmq                     26.0.3                    <pip>
[conda] torch                     2.1.0                     <pip>
[conda] torch-npu                 2.1.0.post6.dev20240716           <pip>
[conda] torchvision               0.16.0                    <pip>
vLLM Version: 0.7.3
vLLM Ascend Version: 0.7.3rc1

ENV Variables:
ASCEND_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ASCEND_RUNTIME_OPTIONS=
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/home/ma-user/python3.10/lib/python3.10/site-packages/cv2/../../lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/toolbox/latest/Ascend-DMI/lib64:/usr/lib/aarch64-linux-gnu/hdf5/serial:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/:/usr/local/seccomponent/lib/:/usr/local/seccomponent/lib/openssl/:/usr/local/mindspore-lite/mindspore-lite-2.3.0-linux-aarch64/tools/converter/lib:/usr/local/mindspore-lite/mindspore-lite-2.3.0-linux-aarch64/runtime/lib:/usr/local/mindspore-lite/mindspore-lite-2.3.0-linux-aarch64/runtime/third_party/dnnl
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_AUTOML_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools
TORCH_DEVICE_BACKEND_AUTOLOAD=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc3                 Version: 24.1.rc3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B1               | OK            | 101.0       49                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          7324 / 65536         |
+===========================+===============+====================================================+
| 1     910B1               | OK            | 98.4        47                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          7311 / 65536         |
+===========================+===============+====================================================+
| 2     910B1               | OK            | 101.4       49                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3384 / 65536         |
+===========================+===============+====================================================+
| 3     910B1               | OK            | 95.0        47                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3377 / 65536         |
+===========================+===============+====================================================+
| 4     910B1               | OK            | 97.0        48                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3379 / 65536         |
+===========================+===============+====================================================+
| 5     910B1               | OK            | 97.1        47                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3379 / 65536         |
+===========================+===============+====================================================+
| 6     910B1               | OK            | 102.5       48                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3378 / 65536         |
+===========================+===============+====================================================+
| 7     910B1               | OK            | 96.4        47                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3378 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 919717        | python                   | 3969                    |
+===========================+===============+====================================================+
| 1       0                 | 920633        | python                   | 3969                    |
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
path=/home/ma-user/ascend-toolkit/8.0.0/aarch64-linux

### 🐛 Describe the bug

**sample code**

```
from transformers import AutoProcessor
from vllm import LLM, SamplingParams
from qwen_vl_utils import process_vision_info

MODEL_PATH = "/home/ma-user/work/dataset/checkpointsulan/Qwen2_5_VL_3B_Instruct"

llm = LLM(
    model=MODEL_PATH,
    tensor_parallel_size=2,
    trust_remote_code=True,
    max_num_seqs=8
)

sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=256)

image_messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "1929087646.jpg",
                "min_pixels": 224 * 224,
                "max_pixels": 1280 * 28 * 28,
            },
            {"type": "text", "text": "Please describe it"},
        ],
    },
]

# Here we use video messages as a demonstration
messages = image_messages

processor = AutoProcessor.from_pretrained(MODEL_PATH)
prompt = processor.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
image_inputs, video_inputs = process_vision_info(messages)

mm_data = {}
if image_inputs is not None:
    mm_data["image"] = image_inputs
if video_inputs is not None:
    mm_data["video"] = video_inputs

llm_inputs = {
    "prompt": prompt,
    "multi_modal_data": mm_data
}

outputs = llm.generate([llm_inputs], sampling_params=sampling_params)
generated_text = outputs[0].outputs[0].text

print(generated_text)
```

**and I tried only text on qwen2.5vl, it failed too.**
```
from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The future of AI is",
]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
# The first run will take about 3-5 mins (10 MB/s) to download models
llm = LLM(model="/home/ma-user/work/dataset/checkpointsulan/Qwen2_5_VL_3B_Instruct",
            tensor_parallel_size=2,
            distributed_executor_backend="mp",
            trust_remote_code=True)

outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

**It stucked here**
(PyTorch-2.1.0) [ma-user vllm]$python test.py 
INFO 03-24 17:02:27 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 03-24 17:02:27 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 03-24 17:02:27 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 03-24 17:02:27 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-24 17:02:27 __init__.py:44] plugin ascend loaded.
INFO 03-24 17:02:27 __init__.py:198] Platform plugin ascend is activated
INFO 03-24 17:02:27 __init__.py:30] Available plugins for group vllm.general_plugins:
INFO 03-24 17:02:27 __init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 03-24 17:02:27 __init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 03-24 17:02:27 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 03-24 17:02:27 __init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 03-24 17:02:27 _custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 03-24 17:02:28 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 03-24 17:02:29 registry.py:351] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:CustomQwen2VLForConditionalGeneration.
INFO 03-24 17:02:40 config.py:549] This model supports multiple tasks: {'generate', 'score', 'embed', 'reward', 'classify'}. Defaulting to 'generate'.
WARNING 03-24 17:02:40 arg_utils.py:1197] The model has a long context length (128000). This may cause OOM errors during the initial memory profiling phase, or result in low performance due to small KV cache space. Consider setting --max-model-len to a smaller value.
INFO 03-24 17:02:40 llm_engine.py:234] Initializing a V0 LLM engine (v0.7.3) with config: model='/home/ma-user/work/dataset/checkpointsulan/Qwen2_5_VL_3B_Instruct', speculative_config=None, tokenizer='/home/ma-user/work/dataset/checkpointsulan/Qwen2_5_VL_3B_Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=128000, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=/home/ma-user/work/dataset/checkpointsulan/Qwen2_5_VL_3B_Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=False, 
WARNING 03-24 17:02:40 multiproc_worker_utils.py:300] Reducing Torch parallelism from 192 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this value as needed.
WARNING 03-24 17:02:40 utils.py:447] The environment variable HOST_IP is deprecated and ignored, as it is often used by Docker and other software tointeract with the container's network stack. Please use VLLM_HOST_IP instead to set the IP address for vLLM processes to communicate with each other.
(VllmWorkerProcess pid=920633) INFO 03-24 17:02:40 multiproc_worker_utils.py:229] Worker ready; awaiting tasks
/home/ma-user/python3.10/lib/python3.10/site-packages/torch_npu/contrib/transfer_to_npu.py:292: ImportWarning: 
    *************************************************************************************************************
    The torch.Tensor.cuda and torch.nn.Module.cuda are replaced with torch.Tensor.npu and torch.nn.Module.npu now..
    The torch.cuda.DoubleTensor is replaced with torch.npu.FloatTensor cause the double type is not supported now..
    The backend in torch.distributed.init_process_group set to hccl now..
    The torch.cuda.* and torch.cuda.amp.* are replaced with torch.npu.* and torch.npu.amp.* now..
    The device parameters have been replaced with npu in the function below:
    torch.logspace, torch.randint, torch.hann_window, torch.rand, torch.full_like, torch.ones_like, torch.rand_like, torch.randperm, torch.arange, torch.frombuffer, torch.normal, torch._empty_per_channel_affine_quantized, torch.empty_strided, torch.empty_like, torch.scalar_tensor, torch.tril_indices, torch.bartlett_window, torch.ones, torch.sparse_coo_tensor, torch.randn, torch.kaiser_window, torch.tensor, torch.triu_indices, torch.as_tensor, torch.zeros, torch.randint_like, torch.full, torch.eye, torch._sparse_csr_tensor_unsafe, torch.empty, torch._sparse_coo_tensor_unsafe, torch.blackman_window, torch.zeros_like, torch.range, torch.sparse_csr_tensor, torch.randn_like, torch.from_file, torch._cudnn_init_dropout_state, torch._empty_affine_quantized, torch.linspace, torch.hamming_window, torch.empty_quantized, torch._pin_memory, torch.autocast, torch.load, torch.Generator, torch.set_default_device, torch.Tensor.new_empty, torch.Tensor.new_empty_strided, torch.Tensor.new_full, torch.Tensor.new_ones, torch.Tensor.new_tensor, torch.Tensor.new_zeros, torch.Tensor.to, torch.Tensor.pin_memory, torch.nn.Module.to, torch.nn.Module.to_empty
    *************************************************************************************************************
    
  warnings.warn(msg, ImportWarning)
(VllmWorkerProcess pid=920633) /home/ma-user/python3.10/lib/python3.10/site-packages/torch_npu/contrib/transfer_to_npu.py:292: ImportWarning: 
(VllmWorkerProcess pid=920633)     *************************************************************************************************************
(VllmWorkerProcess pid=920633)     The torch.Tensor.cuda and torch.nn.Module.cuda are replaced with torch.Tensor.npu and torch.nn.Module.npu now..
(VllmWorkerProcess pid=920633)     The torch.cuda.DoubleTensor is replaced with torch.npu.FloatTensor cause the double type is not supported now..
(VllmWorkerProcess pid=920633)     The backend in torch.distributed.init_process_group set to hccl now..
(VllmWorkerProcess pid=920633)     The torch.cuda.* and torch.cuda.amp.* are replaced with torch.npu.* and torch.npu.amp.* now..
(VllmWorkerProcess pid=920633)     The device parameters have been replaced with npu in the function below:
(VllmWorkerProcess pid=920633)     torch.logspace, torch.randint, torch.hann_window, torch.rand, torch.full_like, torch.ones_like, torch.rand_like, torch.randperm, torch.arange, torch.frombuffer, torch.normal, torch._empty_per_channel_affine_quantized, torch.empty_strided, torch.empty_like, torch.scalar_tensor, torch.tril_indices, torch.bartlett_window, torch.ones, torch.sparse_coo_tensor, torch.randn, torch.kaiser_window, torch.tensor, torch.triu_indices, torch.as_tensor, torch.zeros, torch.randint_like, torch.full, torch.eye, torch._sparse_csr_tensor_unsafe, torch.empty, torch._sparse_coo_tensor_unsafe, torch.blackman_window, torch.zeros_like, torch.range, torch.sparse_csr_tensor, torch.randn_like, torch.from_file, torch._cudnn_init_dropout_state, torch._empty_affine_quantized, torch.linspace, torch.hamming_window, torch.empty_quantized, torch._pin_memory, torch.autocast, torch.load, torch.Generator, torch.set_default_device, torch.Tensor.new_empty, torch.Tensor.new_empty_strided, torch.Tensor.new_full, torch.Tensor.new_ones, torch.Tensor.new_tensor, torch.Tensor.new_zeros, torch.Tensor.to, torch.Tensor.pin_memory, torch.nn.Module.to, torch.nn.Module.to_empty
(VllmWorkerProcess pid=920633)     *************************************************************************************************************
(VllmWorkerProcess pid=920633)     
(VllmWorkerProcess pid=920633)   warnings.warn(msg, ImportWarning)
(VllmWorkerProcess pid=920633) /home/ma-user/python3.10/lib/python3.10/site-packages/torch_npu/contrib/transfer_to_npu.py:247: RuntimeWarning: torch.jit.script and torch.jit.script_method will be disabled by transfer_to_npu, which currently does not support them, if you need to enable them, please do not use transfer_to_npu.
/home/ma-user/python3.10/lib/python3.10/site-packages/torch_npu/contrib/transfer_to_npu.py:247: RuntimeWarning: torch.jit.script and torch.jit.script_method will be disabled by transfer_to_npu, which currently does not support them, if you need to enable them, please do not use transfer_to_npu.
  warnings.warn(msg, RuntimeWarning)
(VllmWorkerProcess pid=920633)   warnings.warn(msg, RuntimeWarning)
WARNING 03-24 17:02:40 utils.py:2262] Methods add_lora,add_prompt_adapter,cache_config,compilation_config,current_platform,list_loras,list_prompt_adapters,load_config,pin_lora,pin_prompt_adapter,remove_lora,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffd1d4106a0>
(VllmWorkerProcess pid=920633) WARNING 03-24 17:02:40 utils.py:2262] Methods add_lora,add_prompt_adapter,cache_config,compilation_config,current_platform,list_loras,list_prompt_adapters,load_config,pin_lora,pin_prompt_adapter,remove_lora,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffd1d410550>
INFO 03-24 17:02:46 shm_broadcast.py:258] vLLM message queue communication handle: Handle(connect_ip='127.0.0.1', local_reader_ranks=[1], buffer_handle=(1, 4194304, 6, 'psm_60c6417e'), local_subscribe_port=44435, remote_subscribe_port=None)
(VllmWorkerProcess pid=920633) INFO 03-24 17:02:46 config.py:3054] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
INFO 03-24 17:02:46 config.py:3054] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
Loading safetensors checkpoint shards:   0% Completed | 0/2 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  50% Completed | 1/2 [00:04<00:04,  4.29s/it]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:08<00:00,  4.31s/it]
Loading safetensors checkpoint shards: 100% Completed | 2/2 [00:08<00:00,  4.31s/it]

Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.48, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
(VllmWorkerProcess pid=920633) Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.48, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
(VllmWorkerProcess pid=920633) It looks like you are trying to rescale already rescaled images. If the input images have pixel values between 0 and 1, set `do_rescale=False` to avoid rescaling them again.
It looks like you are trying to rescale already rescaled images. If the input images have pixel values between 0 and 1, set `do_rescale=False` to avoid rescaling them again.
./home/ma-user/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_5_vl.py:622: UserWarning: current tensor is running as_strided, don't perform inplace operations on the returned value. If you encounter this warning and have precision issues, you can try torch.npu.config.allow_internal_format = False to resolve precision issues. (Triggered internally at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:123.)
  hidden_states = hidden_states[window_index, :, :]
(VllmWorkerProcess pid=920633) /home/ma-user/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_5_vl.py:622: UserWarning: current tensor is running as_strided, don't perform inplace operations on the returned value. If you encounter this warning and have precision issues, you can try torch.npu.config.allow_internal_format = False to resolve precision issues. (Triggered internally at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:123.)
(VllmWorkerProcess pid=920633)   hidden_states = hidden_states[window_index, :, :]

**and finally got this**
[rank1]:[E324 13:00:25.428029551 compiler_depend.ts:574] [Rank 1] Watchdog caught collective operation timeout: WorkHCCL(SeqNum=196, OpType=ALLREDUCE, Timeout(ms)=3600000) ran for 3600185 milliseconds before timing out.
[rank1]:[E324 13:00:25.428092542 compiler_depend.ts:628] Some HCCL operations have failed or timed out. Due to the asynchronous nature of ASCEND kernels, subsequent NPU operations might run on corrupted/incomplete data.
[rank1]:[E324 13:00:25.428107952 compiler_depend.ts:634] To avoid data inconsistency, we are taking the entire process down.
[rank1]:[E324 13:00:25.429344265 compiler_depend.ts:1020] [Rank 1] HCCL watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkHCCL(SeqNum=196, OpType=ALLREDUCE, Timeout(ms)=3600000) ran for 3600185 milliseconds before timing out.
terminate called after throwing an instance of 'std::runtime_error'
  what():  [Rank 1] HCCL watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkHCCL(SeqNum=196, OpType=ALLREDUCE, Timeout(ms)=3600000) ran for 3600185 milliseconds before timing out.
[rank0]:[E324 13:00:25.236600964 compiler_depend.ts:574] [Rank 0] Watchdog caught collective operation timeout: WorkHCCL(SeqNum=196, OpType=ALLREDUCE, Timeout(ms)=3600000) ran for 3600993 milliseconds before timing out.
[rank0]:[E324 13:00:25.236660334 compiler_depend.ts:628] Some HCCL operations have failed or timed out. Due to the asynchronous nature of ASCEND kernels, subsequent NPU operations might run on corrupted/incomplete data.
[rank0]:[E324 13:00:25.236673554 compiler_depend.ts:634] To avoid data inconsistency, we are taking the entire process down.
[rank0]:[E324 13:00:25.236891287 compiler_depend.ts:1020] [Rank 0] HCCL watchdog thread terminated with exception: [Rank 0] Watchdog caught collective operation timeout: WorkHCCL(SeqNum=196, OpType=ALLREDUCE, Timeout(ms)=3600000) ran for 3600993 milliseconds before timing out.
terminate called after throwing an instance of 'std::runtime_error'
  what():  [Rank 0] HCCL watchdog thread terminated with exception: [Rank 0] Watchdog caught collective operation timeout: WorkHCCL(SeqNum=196, OpType=ALLREDUCE, Timeout(ms)=3600000) ran for 3600993 milliseconds before timing out.
Process ForkServerProcess-1:6:
Process ForkServerProcess-1:4:
Process ForkServerProcess-1:5:
Process ForkServerProcess-1:9:
Process ForkServerProcess-1:3:
Process ForkServerProcess-1:8:
Process ForkServerProcess-1:2:
Process ForkServerProcess-1:7:
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 65, in wrapper
    raise exp
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 62, in wrapper
    func(*args, **kwargs)
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 262, in task_distribute
    key, func_name, detail = resource_proxy[TASK_QUEUE].get()
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 65, in wrapper
    raise exp
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 65, in wrapper
    raise exp
Traceback (most recent call last):
  File "<string>", line 2, in get
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 65, in wrapper
    raise exp
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 62, in wrapper
    func(*args, **kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 65, in wrapper
    raise exp
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 62, in wrapper
    func(*args, **kwargs)
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/managers.py", line 818, in _callmethod
    kind, result = conn.recv()
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 65, in wrapper
    raise exp
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 62, in wrapper
    func(*args, **kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 262, in task_distribute
    key, func_name, detail = resource_proxy[TASK_QUEUE].get()
Traceback (most recent call last):
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 62, in wrapper
    func(*args, **kwargs)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 262, in task_distribute
    key, func_name, detail = resource_proxy[TASK_QUEUE].get()
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/connection.py", line 255, in recv
    buf = self._recv_bytes()
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 62, in wrapper
    func(*args, **kwargs)
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 262, in task_distribute
    key, func_name, detail = resource_proxy[TASK_QUEUE].get()
  File "<string>", line 2, in get
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 262, in task_distribute
    key, func_name, detail = resource_proxy[TASK_QUEUE].get()
  File "<string>", line 2, in get
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/connection.py", line 419, in _recv_bytes
    buf = self._recv(4)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 262, in task_distribute
    key, func_name, detail = resource_proxy[TASK_QUEUE].get()
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "<string>", line 2, in get
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/process.py", line 315, in _bootstrap
    self.run()
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/managers.py", line 818, in _callmethod
    kind, result = conn.recv()
  File "<string>", line 2, in get
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/managers.py", line 818, in _callmethod
    kind, result = conn.recv()
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/connection.py", line 388, in _recv
    raise EOFError
  File "<string>", line 2, in get
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 65, in wrapper
    raise exp
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/managers.py", line 818, in _callmethod
    kind, result = conn.recv()
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/connection.py", line 255, in recv
    buf = self._recv_bytes()
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/managers.py", line 818, in _callmethod
    kind, result = conn.recv()
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/connection.py", line 255, in recv
    buf = self._recv_bytes()
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/managers.py", line 818, in _callmethod
    kind, result = conn.recv()
EOFError
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 62, in wrapper
    func(*args, **kwargs)
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/connection.py", line 255, in recv
    buf = self._recv_bytes()
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 65, in wrapper
    raise exp
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/connection.py", line 419, in _recv_bytes
    buf = self._recv(4)
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/connection.py", line 255, in recv
    buf = self._recv_bytes()
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/connection.py", line 419, in _recv_bytes
    buf = self._recv(4)
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/connection.py", line 255, in recv
    buf = self._recv_bytes()
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 262, in task_distribute
    key, func_name, detail = resource_proxy[TASK_QUEUE].get()
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/connection.py", line 419, in _recv_bytes
    buf = self._recv(4)
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 62, in wrapper
    func(*args, **kwargs)
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/connection.py", line 388, in _recv
    raise EOFError
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/connection.py", line 419, in _recv_bytes
    buf = self._recv(4)
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/connection.py", line 388, in _recv
    raise EOFError
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/connection.py", line 419, in _recv_bytes
    buf = self._recv(4)
  File "<string>", line 2, in get
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/connection.py", line 388, in _recv
    raise EOFError
  File "/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/repository_manager/route.py", line 262, in task_distribute
    key, func_name, detail = resource_proxy[TASK_QUEUE].get()
  File "/home/ma-user/python3.10/lib/python3.10/multiprocessing/connection.py", line 388, in _recv
    raise EOFError
EOFError

**Any idea? THX**
