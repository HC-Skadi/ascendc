# Issue #145: [Bug]: MRotaryEmbedding.get_input_positions() got an unexpected keyword argument 'image_token_id'

## 基本信息

- **编号**: #145
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/145
- **创建时间**: 2025-02-23T13:39:44Z
- **关闭时间**: 2025-04-09T16:14:03Z
- **更新时间**: 2025-04-09T16:14:04Z
- **提交者**: @SHYuanBest
- **评论数**: 6

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

```
INFO 02-23 21:38:32 __init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 02-23 21:38:32 __init__.py:32] name=ascend, value=vllm_ascend:register
INFO 02-23 21:38:32 __init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 02-23 21:38:32 __init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 02-23 21:38:32 __init__.py:44] plugin ascend loaded.
INFO 02-23 21:38:32 __init__.py:198] Platform plugin ascend is activated
INFO 02-23 21:38:40 config.py:560] This model supports multiple tasks: {'embed', 'score', 'classify', 'generate', 'reward'}. Defaulting to 'generate'.
INFO 02-23 21:38:40 llm_engine.py:234] Initializing a V0 LLM engine (v0.7.4.dev51+g5a2ba16f) with config: model='/work/share/checkpoint/ysh/Qwen2.5-VL-7B-Instruct', speculative_config=None, tokenizer='/work/share/checkpoint/ysh/Qwen2.5-VL-7B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=/work/share/checkpoint/ysh/Qwen2.5-VL-7B-Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=False, chunked_prefill_enabled=False, use_async_output_proc=True, disable_mm_preprocessor_cache=False, mm_processor_kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[8,4,2,1],"max_capture_size":8}, use_cached_outputs=False, 
INFO 02-23 21:38:41 importing.py:16] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 02-23 21:38:41 utils.py:2298] Methods add_lora,add_prompt_adapter,cache_config,compilation_config,current_platform,list_loras,list_prompt_adapters,load_config,pin_lora,pin_prompt_adapter,remove_lora,remove_prompt_adapter not implemented in <vllm_ascend.worker.NPUWorker object at 0xfffcaccabc40>
INFO 02-23 21:38:46 parallel_state.py:948] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0
WARNING 02-23 21:38:46 _custom_ops.py:21] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 02-23 21:38:46 config.py:3127] cudagraph sizes specified by model runner [1, 2, 4, 8] is overridden by config [8, 1, 2, 4]
Loading safetensors checkpoint shards:   0% Completed | 0/5 [00:00<?, ?it/s]
Loading safetensors checkpoint shards:  20% Completed | 1/5 [00:00<00:00,  4.21it/s]
Loading safetensors checkpoint shards:  40% Completed | 2/5 [00:00<00:00,  4.45it/s]
Loading safetensors checkpoint shards:  60% Completed | 3/5 [00:00<00:00,  4.50it/s]
Loading safetensors checkpoint shards:  80% Completed | 4/5 [00:00<00:00,  4.53it/s]
Loading safetensors checkpoint shards: 100% Completed | 5/5 [00:00<00:00,  5.19it/s]

Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.48, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
Computed max_num_seqs (min(5, 5120 // 32768)) to be less than 1. Setting it to the minimum value of 1.
It looks like you are trying to rescale already rescaled images. If the input images have pixel values between 0 and 1, set `do_rescale=False` to avoid rescaling them again.
WARNING 02-23 21:38:55 profiling.py:196] The context length (5120) of the model is too short to hold the multi-modal embeddings in the worst case (32768 tokens in total, out of which {'image': 16384, 'video': 16384} are reserved for multi-modal embeddings). This may cause certain multi-modal inputs to fail during inference, even when the input text is short. To avoid this, you should increase `max_model_len`, reduce `max_num_seqs`, and/or reduce `mm_counts`.
INFO 02-23 21:39:03 executor_base.py:111] # npu blocks: 35511, # CPU blocks: 4681
INFO 02-23 21:39:03 executor_base.py:116] Maximum concurrency for 4096 tokens per request: 138.71x
INFO 02-23 21:39:03 llm_engine.py:436] init engine (profile, create kv cache, warmup model) took 15.18 seconds
Processed prompts:   0%|                                                                                  | 0/1 [00:00<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s][rank0]: Traceback (most recent call last):
[rank0]:   File "/work/share/projects/ysh/ConsisID-X/vllm_code/test_mllm.py", line 54, in <module>
[rank0]:     outputs = llm.generate(inputs, sampling_params=sampling_params)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/utils.py", line 1080, in inner
[rank0]:     return fn(*args, **kwargs)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py", line 470, in generate
[rank0]:     outputs = self._run_engine(use_tqdm=use_tqdm)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py", line 1377, in _run_engine
[rank0]:     step_outputs = self.llm_engine.step()
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 1391, in step
[rank0]:     outputs = self.model_executor.execute_model(
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/executor/executor_base.py", line 139, in execute_model
[rank0]:     output = self.collective_rpc("execute_model",
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
[rank0]:     answer = run_method(self.driver_worker, method, args, kwargs)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/utils.py", line 2232, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/worker/worker_base.py", line 394, in execute_model
[rank0]:     inputs = self.prepare_input(execute_model_req)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/worker/worker_base.py", line 379, in prepare_input
[rank0]:     return self._get_driver_input_and_broadcast(execute_model_req)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/vllm/worker/worker_base.py", line 341, in _get_driver_input_and_broadcast
[rank0]:     self.model_runner.prepare_model_input(
[rank0]:   File "/work/share/projects/ysh/0_local_env/vllm-ascend/vllm_ascend/model_runner.py", line 1063, in prepare_model_input
[rank0]:     model_input = self._prepare_model_input_tensors(
[rank0]:   File "/work/share/projects/ysh/0_local_env/vllm-ascend/vllm_ascend/model_runner.py", line 885, in _prepare_model_input_tensors
[rank0]:     builder.add_seq_group(seq_group_metadata)
[rank0]:   File "/work/share/projects/ysh/0_local_env/vllm-ascend/vllm_ascend/model_runner.py", line 446, in add_seq_group
[rank0]:     per_seq_group_fn(inter_data, seq_group_metadata)
[rank0]:   File "/work/share/projects/ysh/0_local_env/vllm-ascend/vllm_ascend/model_runner.py", line 722, in _compute_multi_modal_input
[rank0]:     MRotaryEmbedding.get_input_positions(
[rank0]: TypeError: MRotaryEmbedding.get_input_positions() got an unexpected keyword argument 'image_token_id'
[ERROR] 2025-02-23-21:39:09 (PID:360549, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```

```
from argparse import Namespace
from typing import List, NamedTuple, Optional

from PIL.Image import Image
from transformers import AutoProcessor, AutoTokenizer

from vllm import LLM, SamplingParams
from vllm.multimodal.utils import fetch_image
from vllm.utils import FlexibleArgumentParser
from qwen_vl_utils import process_vision_info

model_name = Qwen/Qwen2.5-VL-7B-Instruct"

llm = LLM(
    model=model_name,
    max_model_len=32768 if process_vision_info is None else 4096,
    max_num_seqs=5,
    limit_mm_per_prompt={"image": 1},
)
processor = AutoProcessor.from_pretrained(model_name)

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg",
            },
            {"type": "text", "text": "Describe this image."},
        ],
    }
]
prompt = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
image_data, _ = process_vision_info(messages)

stop_token_ids = None

sampling_params = SamplingParams(temperature=0.0,
                                 max_tokens=128,
                                 stop_token_ids=stop_token_ids)

inputs = {
        "prompt": prompt,
        "multi_modal_data": {
            "image": image_data
        },
    }

outputs = llm.generate(inputs, sampling_params=sampling_params)

for o in outputs:
    generated_text = o.outputs[0].text
    print(generated_text)
```
