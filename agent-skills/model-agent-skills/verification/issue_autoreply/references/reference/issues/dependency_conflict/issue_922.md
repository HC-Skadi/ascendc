# Issue #922: [Bug]: 官方vllm-ascend0.7.3镜像环境上安装mindie_turbo2.0.rc1在调用Qwen2.5-VL-7B时报错

## 基本信息

- **编号**: #922
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/922
- **创建时间**: 2025-05-22T02:39:26Z
- **关闭时间**: 2026-01-04T02:27:53Z
- **更新时间**: 2026-01-04T02:27:53Z
- **提交者**: @hjjjk
- **评论数**: 10

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>拉取镜像指令`</summary>

```text
docker pull quay.io/ascend/vllm-ascend@sha256:711b1dea10dcde4fa2f752456c1c8897421deee0ba620f1163a52a0601c96fce
```

</details>


### 🐛 Describe the bug

我的代码是：
```
import gc
import os
os.environ["VLLM_USE_V1"]="0"

import time
import torch
from transformers import AutoProcessor
from vllm import LLM, SamplingParams
from qwen_vl_utils import process_vision_info

from vllm.distributed.parallel_state import (destroy_distributed_environment,
                                             destroy_model_parallel)

MODEL_PATH = "/cache/Qwen2.5-VL-7B-Instruct"
llm = LLM(
    model=MODEL_PATH,
    max_model_len=16840,
    tensor_parallel_size=4,
    distributed_executor_backend="mp",
    limit_mm_per_prompt={"image": 1}
)

sampling_params = SamplingParams(
    max_tokens=512,
    temperature=0.6,
    top_p=0.95,
    top_k=40
)

image_messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "/cache/TestProject/meituan_003/9.jpg",
                "min_pixels": 224 * 224,
                "max_pixels": 12800 * 28 * 28,
            },
            {"type": "text", "text": "请根据图片中的内容，描述该图片中页面的功能"},
        ],
    },
]

messages = image_messages

processor = AutoProcessor.from_pretrained(MODEL_PATH)
prompt = processor.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)

image_inputs, _, _ = process_vision_info(messages, return_video_kwargs=True)

mm_data = {}
if image_inputs is not None:
    mm_data["image"] = image_inputs

llm_inputs = {
    "prompt": prompt,
    "multi_modal_data": mm_data,
}

tick = time.time()
outputs = llm.generate([llm_inputs], sampling_params=sampling_params)
tock = time.time()
generated_text = outputs[0].outputs[0].text

print(generated_text)
print(f"elapsed {tock - tick}s")
```

报的错是

```
INFO 05-21 11:55:37 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-21 11:55:37 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
INFO 05-21 11:55:37 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-21 11:55:37 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-21 11:55:37 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-21 11:55:37 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-21 11:55:37 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-21 11:55:37 [__init__.py:44] plugin ascend loaded.
INFO 05-21 11:55:37 [__init__.py:230] Platform plugin ascend is activated
WARNING 05-21 11:55:39 [_custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 05-21 11:55:41 [__init__.py:30] Available plugins for group vllm.general_plugins:
INFO 05-21 11:55:41 [__init__.py:32] name=ascend_enhanced_model, value=vllm_ascend:register_model
INFO 05-21 11:55:41 [__init__.py:34] all available plugins for group vllm.general_plugins will be loaded.
INFO 05-21 11:55:41 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-21 11:55:41 [__init__.py:44] plugin ascend_enhanced_model loaded.
WARNING 05-21 11:55:43 [registry.py:389] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 05-21 11:55:43 [registry.py:389] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 05-21 11:55:43 [registry.py:389] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 05-21 11:55:43 [registry.py:389] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 05-21 11:55:43 [registry.py:389] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
INFO 05-21 11:55:58 [config.py:717] This model supports multiple tasks: {'embed', 'reward', 'classify', 'generate', 'score'}. Defaulting to 'generate'.
INFO 05-21 11:55:58 [arg_utils.py:1669] npu is experimental on VLLM_USE_V1=1. Falling back to V0 Engine.
INFO 05-21 11:55:58 [config.py:1804] Disabled the custom all-reduce kernel because it is not supported on current platform.
WARNING 05-21 11:55:58 [platform.py:136] NPU compilation support pending. Will be available in future CANN and torch_npu releases. NPU graph mode is currently experimental and disabled by default. You can just adopt additional_config={'enable_graph_mode': True} to serve deepseek models with NPU graph mode on vllm-ascend with V0 engine.
INFO 05-21 11:55:58 [platform.py:144] Compilation disabled, using eager mode by default
INFO 05-21 11:55:58 [llm_engine.py:240] Initializing a V0 LLM engine (v0.8.5.post1) with config: model='/cache/Qwen2.5-VL-7B-Instruct', speculative_config=None, tokenizer='/cache/Qwen2.5-VL-7B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=16840, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=None, served_model_name=/cache/Qwen2.5-VL-7B-Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=None, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"level":0,"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"max_capture_size":256}, use_cached_outputs=False,
WARNING 05-21 11:55:59 [multiproc_worker_utils.py:306] Reducing Torch parallelism from 192 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this value as needed.
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m INFO 05-21 11:55:59 [multiproc_worker_utils.py:225] Worker ready; awaiting tasks
^[[1;36m(VllmWorkerProcess pid=113917)^[[0;0m INFO 05-21 11:55:59 [multiproc_worker_utils.py:225] Worker ready; awaiting tasks
WARNING 05-21 11:55:59 [utils.py:566] The environment variable HOST_IP is deprecated and ignored, as it is often used by Docker and other software to interact with the container's network stack. Please use VLLM_HOST_IP instead to set the IP address for vLLM processes to communicate with each other.
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m INFO 05-21 11:55:59 [multiproc_worker_utils.py:225] Worker ready; awaiting tasks
WARNING 05-21 11:55:59 [utils.py:2522] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffdb8f5a6b0>
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m WARNING 05-21 11:55:59 [utils.py:2522] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffe7fd882e0>
^[[1;36m(VllmWorkerProcess pid=113917)^[[0;0m WARNING 05-21 11:55:59 [utils.py:2522] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffe7fd88b20>
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m WARNING 05-21 11:55:59 [utils.py:2522] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffdb9054d30>
INFO 05-21 11:55:59 [utils.py:52] MindIE Turbo is installed. vLLM inference will be accelerated with MindIE Turbo.
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m INFO 05-21 11:55:59 [utils.py:52] MindIE Turbo is installed. vLLM inference will be accelerated with MindIE Turbo.
^[[1;36m(VllmWorkerProcess pid=113917)^[[0;0m INFO 05-21 11:55:59 [utils.py:52] MindIE Turbo is installed. vLLM inference will be accelerated with MindIE Turbo.
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m INFO 05-21 11:55:59 [utils.py:52] MindIE Turbo is installed. vLLM inference will be accelerated with MindIE Turbo.
INFO 05-21 11:56:06 [shm_broadcast.py:266] vLLM message queue communication handle: Handle(local_reader_ranks=[1, 2, 3], buffer_handle=(3, 4194304, 6, 'psm_6f1e1ae0'), local_subscribe_addr='ipc:///tmp/978ab6f9-23d2-4246-a3a6-43310a37dc92', remote_subscribe_addr=None, remote_addr_ipv6=False)
^[[1;36m(VllmWorkerProcess pid=113917)^[[0;0m INFO 05-21 11:56:06 [parallel_state.py:1004] rank 2 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 2
INFO 05-21 11:56:06 [parallel_state.py:1004] rank 0 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 0
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m INFO 05-21 11:56:06 [parallel_state.py:1004] rank 1 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 1
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m INFO 05-21 11:56:06 [parallel_state.py:1004] rank 3 in world size 4 is assigned as DP rank 0, PP rank 0, TP rank 3
INFO 05-21 11:56:06 [model_runner.py:953] Starting to load model /cache/Qwen2.5-VL-7B-Instruct...
^[[1;36m(VllmWorkerProcess pid=113917)^[[0;0m INFO 05-21 11:56:06 [model_runner.py:953] Starting to load model /cache/Qwen2.5-VL-7B-Instruct...
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m INFO 05-21 11:56:06 [model_runner.py:953] Starting to load model /cache/Qwen2.5-VL-7B-Instruct...
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m INFO 05-21 11:56:06 [model_runner.py:953] Starting to load model /cache/Qwen2.5-VL-7B-Instruct...
INFO 05-21 11:56:07 [config.py:3614] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
WARNING 05-21 11:56:07 [platform.py:136] NPU compilation support pending. Will be available in future CANN and torch_npu releases. NPU graph mode is currently experimental and disabled by default. You can just adopt additional_config={'enable_graph_mode': True} to serve deepseek models with NPU graph mode on vllm-ascend with V0 engine.
INFO 05-21 11:56:07 [platform.py:144] Compilation disabled, using eager mode by default
^[[1;36m(VllmWorkerProcess pid=113917)^[[0;0m INFO 05-21 11:56:07 [config.py:3614] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
^[[1;36m(VllmWorkerProcess pid=113917)^[[0;0m WARNING 05-21 11:56:07 [platform.py:136] NPU compilation support pending. Will be available in future CANN and torch_npu releases. NPU graph mode is currently experimental and disabled by default. You can just adopt additional_config={'enable_graph_mode': True} to serve deepseek models with NPU graph mode on vllm-ascend with V0 engine.
^[[1;36m(VllmWorkerProcess pid=113917)^[[0;0m INFO 05-21 11:56:07 [platform.py:144] Compilation disabled, using eager mode by default
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m INFO 05-21 11:56:07 [config.py:3614] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m WARNING 05-21 11:56:07 [platform.py:136] NPU compilation support pending. Will be available in future CANN and torch_npu releases. NPU graph mode is currently experimental and disabled by default. You can just adopt additional_config={'enable_graph_mode': True} to serve deepseek models with NPU graph mode on vllm-ascend with V0 engine.
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m INFO 05-21 11:56:07 [platform.py:144] Compilation disabled, using eager mode by default
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m INFO 05-21 11:56:07 [config.py:3614] cudagraph sizes specified by model runner [1, 2, 4, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256] is overridden by config [256, 128, 2, 1, 4, 136, 8, 144, 16, 152, 24, 160, 32, 168, 40, 176, 48, 184, 56, 192, 64, 200, 72, 208, 80, 216, 88, 120, 224, 96, 232, 104, 240, 112, 248]
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m WARNING 05-21 11:56:07 [platform.py:136] NPU compilation support pending. Will be available in future CANN and torch_npu releases. NPU graph mode is currently experimental and disabled by default. You can just adopt additional_config={'enable_graph_mode': True} to serve deepseek models with NPU graph mode on vllm-ascend with V0 engine.
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m INFO 05-21 11:56:07 [platform.py:144] Compilation disabled, using eager mode by default
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238] Traceback (most recent call last):^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     self.model_runner.load_model()^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/home/ma-user/.local/lib/python3.10/site-packages/mindie_turbo/adaptor/vllm/weight_utils.py", line 94, in postprocess_loading^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     func(self)^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 955, in load_model^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 455, in load_model^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     loaded_weights = model.load_weights(^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 1126, in load_weights^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 261, in load_weights^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     autoloaded_weights = set(self._load_module("", self.module, weights))^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 213, in _load_module^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     for child_prefix, child_weights in self._groupby_prefix(weights):^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 103, in _groupby_prefix^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     for prefix, group in itertools.groupby(weights_by_parts,^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 100, in <genexpr>^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     weights_by_parts = ((weight_name.split(".", 1), weight_data)^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 63, in <genexpr>^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     return ((out_name, data) for name, data in weights^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 431, in get_all_weights^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     yield from self._get_weights_iterator(primary_weights)^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 379, in _get_weights_iterator^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     weights_iterator = safetensors_weights_iterator(^M
^[[1;36m(VllmWorkerProcess pid=113915)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238] TypeError: wrapper_weights_iterator.<locals>._safetensors_weights_iterator() takes 1 positional argument but 2 were given

^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method load_model.^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238] Traceback (most recent call last):^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/executor/multiproc_worker_utils.py", line 232, in _run_worker_process^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     output = run_method(worker, method, args, kwargs)^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     return func(*args, **kwargs)^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 235, in load_model^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     self.model_runner.load_model()^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/home/ma-user/.local/lib/python3.10/site-packages/mindie_turbo/adaptor/vllm/weight_utils.py", line 94, in postprocess_loading^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     func(self)^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 955, in load_model^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     self.model = get_model(vllm_config=self.vllm_config)^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 14, in get_model^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     return loader.load_model(vllm_config=vllm_config)^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 455, in load_model^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     loaded_weights = model.load_weights(^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen2_5_vl.py", line 1126, in load_weights^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 261, in load_weights^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     autoloaded_weights = set(self._load_module("", self.module, weights))^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 213, in _load_module^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     for child_prefix, child_weights in self._groupby_prefix(weights):^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 103, in _groupby_prefix^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     for prefix, group in itertools.groupby(weights_by_parts,^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 100, in <genexpr>^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     weights_by_parts = ((weight_name.split(".", 1), weight_data)^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/models/utils.py", line 63, in <genexpr>^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     return ((out_name, data) for name, data in weights^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 431, in get_all_weights^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     yield from self._get_weights_iterator(primary_weights)^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/loader.py", line 379, in _get_weights_iterator^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238]     weights_iterator = safetensors_weights_iterator(^M
^[[1;36m(VllmWorkerProcess pid=113919)^[[0;0m ERROR 05-21 11:56:08 [multiproc_worker_utils.py:238] TypeError: wrapper_weights_iterator.<locals>._safetensors_weights_iterator() takes 1 positional argument but 2 were given
[ERROR] 2025-05-21-11:56:09 (PID:113031, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
INFO 05-21 11:56:11 [multiproc_worker_utils.py:137] Terminating local vLLM worker processes
```
