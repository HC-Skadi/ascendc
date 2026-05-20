# Issue #1751: [Bug]: V1 pipeline parallel failed with ray backend

## 基本信息

- **编号**: #1751
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1751
- **创建时间**: 2025-07-11T09:22:11Z
- **关闭时间**: 2025-07-23T06:52:53Z
- **更新时间**: 2025-07-23T06:52:53Z
- **提交者**: @MengqingCao
- **评论数**: 1

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

#### Repoduction script

```python
import pytest

from tests.conftest import VllmRunner, example_prompts

MODELS = [
    "Qwen/Qwen3-0.6B-Base",
]

TENSOR_PARALLELS = [1]
PIPELINE_PARALLELS = [2]

@pytest.mark.parametrize("model", MODELS)
@pytest.mark.parametrize("tp_size", TENSOR_PARALLELS)
@pytest.mark.parametrize("pp_size", PIPELINE_PARALLELS)
@pytest.mark.parametrize("distributed_executor_backend", ["mp", "ray"])
def test_models(example_prompts, model: str, tp_size: int, pp_size: int, distributed_executor_backend: str) -> None:
    with VllmRunner(model,
                    tensor_parallel_size=tp_size,
                    pipeline_parallel_size=pp_size,
                    enforce_eager=True,
                    gpu_memory_utilization=0.7,
                    distributed_executor_backend=distributed_executor_backend) as vllm_model:
        vllm_model.generate_greedy(example_prompts, 64)

```

#### Error log

```bash
tests/e2e/multicard/test_pipeline_parallel.py::test_models[ray-2-1-/home/xxx/cache/modelscope/models/Qwen/Qwen3-0___6B-Base] INFO 07-11 09:56:54 [config.py:841] This model supports multiple tasks: {'embed', 'reward', 'generate', 'classify'}. Defaulting to 'generate'.
WARNING 07-11 09:56:54 [config.py:3371] Casting torch.bfloat16 to torch.float16.
INFO 07-11 09:56:54 [config.py:1472] Using max model len 1024
INFO 07-11 09:56:54 [config.py:2285] Chunked prefill is enabled with max_num_batched_tokens=8192.
INFO 07-11 09:56:54 [platform.py:161] Compilation disabled, using eager mode by default
WARNING 07-11 09:56:54 [platform.py:200] If prefix caching is enabled, block size must be set to 128.
huggingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks...
To disable this warning, you can either:
        - Avoid using `tokenizers` before the fork if possible
        - Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false)
INFO 07-11 09:56:55 [core.py:526] Waiting for init message from front-end.
INFO 07-11 09:56:55 [core.py:69] Initializing a V1 LLM engine (v0.9.2.dev301+g3c545c0c3) with config: model='/home/xxx/cache/modelscope/models/Qwen/Qwen3-0___6B-Base', speculative_config=None, tokenizer='/home/xxx/cache/modelscope/models/Qwen/Qwen3-0___6B-Base', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=1024, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=2, disable_custom_all_reduce=True, quantization=None, enforce_eager=True, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=/home/xxx/cache/modelscope/models/Qwen/Qwen3-0___6B-Base, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=True, chunked_prefill_enabled=True, use_async_output_proc=False, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":[],"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{},"inductor_passes":{},"use_cudagraph":true,"cudagraph_num_of_warmups":0,"cudagraph_capture_sizes":[],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"max_capture_size":0,"local_cache_dir":null}
2025-07-11 09:56:58,027 INFO worker.py:1917 -- Started a local Ray instance.
INFO 07-11 09:56:59 [ray_utils.py:334] No current placement group found. Creating a new placement group.
INFO 07-11 09:57:00 [ray_distributed_executor.py:177] use_ray_spmd_worker: True
(pid=20612) INFO 07-11 09:57:09 [__init__.py:39] Available plugins for group vllm.platform_plugins:
(pid=20612) INFO 07-11 09:57:09 [__init__.py:41] - ascend -> vllm_ascend:register
(pid=20612) INFO 07-11 09:57:09 [__init__.py:41] - ascend -> vllm_ascend:register
(pid=20612) INFO 07-11 09:57:09 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
(pid=20612) INFO 07-11 09:57:09 [__init__.py:235] Platform plugin ascend is activated
(pid=20612) WARNING 07-11 09:57:10 [_custom_ops.py:20] Failed to import from vllm._C with ImportError('libnuma.so.1: cannot open shared object file: No such file or directory')
INFO 07-11 09:57:11 [ray_distributed_executor.py:353] non_carry_over_env_vars from config: set()
INFO 07-11 09:57:11 [ray_distributed_executor.py:355] Copying the following environment variables to workers: ['LD_LIBRARY_PATH', 'VLLM_USE_RAY_SPMD_WORKER', 'VLLM_USE_RAY_COMPILED_DAG', 'VLLM_USE_V1']
INFO 07-11 09:57:11 [ray_distributed_executor.py:358] If certain env vars should NOT be copied to workers, add them to /home/xxx/.config/vllm/ray_non_carry_over_env_vars.json file
(RayWorkerWrapper pid=20612) WARNING 07-11 09:57:11 [__init__.py:733] Overwriting environment variable ASCEND_RT_VISIBLE_DEVICES from '1' to '0,1'
(RayWorkerWrapper pid=20612) INFO 07-11 09:57:13 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
(RayWorkerWrapper pid=20612) WARNING 07-11 09:57:13 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
(RayWorkerWrapper pid=20612) WARNING 07-11 09:57:13 [registry.py:413] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
(RayWorkerWrapper pid=20612) WARNING 07-11 09:57:13 [registry.py:413] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
(RayWorkerWrapper pid=20612) WARNING 07-11 09:57:13 [registry.py:413] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
(RayWorkerWrapper pid=20612) WARNING 07-11 09:57:13 [registry.py:413] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
(RayWorkerWrapper pid=20612) WARNING 07-11 09:57:13 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
(RayWorkerWrapper pid=20612) INFO 07-11 09:57:19 [parallel_state.py:1076] rank 1 in world size 2 is assigned as DP rank 0, PP rank 1, TP rank 0, EP rank 0
(pid=20614) INFO 07-11 09:57:09 [__init__.py:39] Available plugins for group vllm.platform_plugins:
(pid=20614) INFO 07-11 09:57:09 [__init__.py:41] - ascend -> vllm_ascend:register [repeated 2x across cluster] (Ray deduplicates logs by default. Set RAY_DEDUP_LOGS=0 to disable log deduplication, or see https://docs.ray.io/en/master/ray-observability/user-guides/configure-logging.html#log-deduplication for more options.)
(pid=20614) INFO 07-11 09:57:09 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
(pid=20614) INFO 07-11 09:57:09 [__init__.py:235] Platform plugin ascend is activated
(pid=20614) WARNING 07-11 09:57:11 [_custom_ops.py:20] Failed to import from vllm._C with ImportError('libnuma.so.1: cannot open shared object file: No such file or directory')
(RayWorkerWrapper pid=20614) WARNING 07-11 09:57:11 [__init__.py:733] Overwriting environment variable ASCEND_RT_VISIBLE_DEVICES from '0' to '0,1'
(RayWorkerWrapper pid=20614) INFO 07-11 09:57:13 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
(RayWorkerWrapper pid=20614) WARNING 07-11 09:57:13 [registry.py:413] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
(RayWorkerWrapper pid=20614) WARNING 07-11 09:57:13 [registry.py:413] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM. [repeated 5x across cluster]
(RayWorkerWrapper pid=20612) INFO 07-11 09:57:19 [model_runner_v1.py:1745] Starting to load model /home/xxx/cache/modelscope/models/Qwen/Qwen3-0___6B-Base...
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
(RayWorkerWrapper pid=20612) INFO 07-11 09:57:22 [default_loader.py:272] Loading weights took 1.68 seconds
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:01<00:00,  1.80s/it]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:01<00:00,  1.80s/it]
(RayWorkerWrapper pid=20614) 
(RayWorkerWrapper pid=20612) INFO 07-11 09:57:23 [model_runner_v1.py:1777] Loading model weights took 0.7079 GB
(RayWorkerWrapper pid=20614) INFO 07-11 09:57:33 [worker_v1.py:181] Available memory: 44070370406, total memory: 65464696832
(RayWorkerWrapper pid=20614) INFO 07-11 09:57:19 [parallel_state.py:1076] rank 0 in world size 2 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
(RayWorkerWrapper pid=20614) INFO 07-11 09:57:19 [model_runner_v1.py:1745] Starting to load model /home/xxx/cache/modelscope/models/Qwen/Qwen3-0___6B-Base...
(RayWorkerWrapper pid=20614) INFO 07-11 09:57:22 [default_loader.py:272] Loading weights took 1.86 seconds
(RayWorkerWrapper pid=20614) INFO 07-11 09:57:23 [model_runner_v1.py:1777] Loading model weights took 0.7079 GB
INFO 07-11 09:57:34 [kv_cache_utils.py:716] GPU KV cache size: 768,512 tokens
INFO 07-11 09:57:34 [kv_cache_utils.py:720] Maximum concurrency for 1,024 tokens per request: 750.50x
INFO 07-11 09:57:34 [kv_cache_utils.py:716] GPU KV cache size: 769,536 tokens
INFO 07-11 09:57:34 [kv_cache_utils.py:720] Maximum concurrency for 1,024 tokens per request: 751.50x
INFO 07-11 09:57:34 [core.py:172] init engine (profile, create kv cache, warmup model) took 10.84 seconds
INFO 07-11 09:57:34 [core.py:129] Batch queue is enabled with size 2
INFO 07-11 09:57:34 [platform.py:161] Compilation disabled, using eager mode by default
Adding requests: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 8/8 [00:00<00:00, 1153.47it/s]
Processed prompts:   0%|                                                                      | 0/8 [00:00<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s]INFO 07-11 09:57:34 [ray_distributed_executor.py:569] RAY_CGRAPH_get_timeout is set to 300
INFO 07-11 09:57:34 [ray_distributed_executor.py:571] VLLM_USE_RAY_COMPILED_DAG_CHANNEL_TYPE = auto
INFO 07-11 09:57:34 [ray_distributed_executor.py:573] VLLM_USE_RAY_COMPILED_DAG_OVERLAP_COMM = False
(RayWorkerWrapper pid=20614) [rank0]:[W711 09:57:36.315174395 compiler_depend.ts:164] Warning: Warning: Device do not support double dtype now, dtype cast repalce with float. (function operator())
2025-07-11 09:57:36,281 INFO compiled_dag_node.py:2157 -- Tearing down compiled DAG
2025-07-11 09:57:36,283 INFO compiled_dag_node.py:2162 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, a605e09def975470504f1fae01000000)
2025-07-11 09:57:36,283 INFO compiled_dag_node.py:2162 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, 4ecf7d28520f52919b8db63101000000)
ERROR 07-11 09:57:36 [core.py:588] EngineCore encountered a fatal error.
ERROR 07-11 09:57:36 [core.py:588] Traceback (most recent call last):
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/code/vllm-cpu/vllm/vllm/v1/engine/core.py", line 579, in run_engine_core
ERROR 07-11 09:57:36 [core.py:588]     engine_core.run_busy_loop()
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/code/vllm-cpu/vllm/vllm/v1/engine/core.py", line 606, in run_busy_loop
ERROR 07-11 09:57:36 [core.py:588]     self._process_engine_step()
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/code/vllm-cpu/vllm/vllm/v1/engine/core.py", line 631, in _process_engine_step
ERROR 07-11 09:57:36 [core.py:588]     outputs, model_executed = self.step_fn()
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/code/vllm-cpu/vllm/vllm/v1/engine/core.py", line 283, in step_with_batch_queue
ERROR 07-11 09:57:36 [core.py:588]     model_output = future.result()
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/code/vllm-cpu/vllm/vllm/v1/executor/ray_distributed_executor.py", line 25, in result
ERROR 07-11 09:57:36 [core.py:588]     return self.ref.get()
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/experimental/compiled_dag_ref.py", line 145, in get
ERROR 07-11 09:57:36 [core.py:588]     raise execution_error from None
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/experimental/compiled_dag_ref.py", line 136, in get
ERROR 07-11 09:57:36 [core.py:588]     ray.get(actor_execution_loop_refs, timeout=10)
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/_private/auto_init_hook.py", line 22, in auto_init_wrapper
ERROR 07-11 09:57:36 [core.py:588]     return fn(*args, **kwargs)
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/_private/client_mode_hook.py", line 104, in wrapper
ERROR 07-11 09:57:36 [core.py:588]     return func(*args, **kwargs)
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/_private/worker.py", line 2849, in get
ERROR 07-11 09:57:36 [core.py:588]     values, debugger_breakpoint = worker.get_objects(object_refs, timeout=timeout)
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/_private/worker.py", line 937, in get_objects
ERROR 07-11 09:57:36 [core.py:588]     raise value.as_instanceof_cause()
ERROR 07-11 09:57:36 [core.py:588] ray.exceptions.RayTaskError(TypeError): ray::RayWorkerWrapper.__ray_call__() (pid=20614, ip=192.168.144.2, actor_id=a605e09def975470504f1fae01000000, repr=<vllm.executor.ray_utils.RayWorkerWrapper object at 0xfff55f5b1c90>)
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/cloudpickle/cloudpickle.py", line 1479, in dumps
ERROR 07-11 09:57:36 [core.py:588]     cp.dump(obj)
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/cloudpickle/cloudpickle.py", line 1245, in dump
ERROR 07-11 09:57:36 [core.py:588]     return super().dump(obj)
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/experimental/channel/torch_tensor_type.py", line 121, in serialize
ERROR 07-11 09:57:36 [core.py:588]     return ctx.serialization_context.serialize_tensor(t)
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/experimental/channel/serialization_context.py", line 105, in serialize_tensor
ERROR 07-11 09:57:36 [core.py:588]     return self.serialize_to_numpy_or_scalar(tensor)
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/experimental/channel/serialization_context.py", line 133, in serialize_to_numpy_or_scalar
ERROR 07-11 09:57:36 [core.py:588]     return (tensor.view(torch.uint8).numpy(), tensor.dtype, tensor_device_type)
ERROR 07-11 09:57:36 [core.py:588] TypeError: can't convert npu:0 device type tensor to numpy. Use Tensor.cpu() to copy the tensor to host memory first.
ERROR 07-11 09:57:36 [core.py:588] 
ERROR 07-11 09:57:36 [core.py:588] The above exception was the direct cause of the following exception:
ERROR 07-11 09:57:36 [core.py:588] 
ERROR 07-11 09:57:36 [core.py:588] ray::RayWorkerWrapper.__ray_call__() (pid=20614, ip=192.168.144.2, actor_id=a605e09def975470504f1fae01000000, repr=<vllm.executor.ray_utils.RayWorkerWrapper object at 0xfff55f5b1c90>)
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/actor.py", line 1745, in __ray_call__
ERROR 07-11 09:57:36 [core.py:588]     return fn(self, *args, **kwargs)
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/dag/compiled_dag_node.py", line 253, in do_exec_tasks
ERROR 07-11 09:57:36 [core.py:588]     done = tasks[operation.exec_task_idx].exec_operation(
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/dag/compiled_dag_node.py", line 786, in exec_operation
ERROR 07-11 09:57:36 [core.py:588]     return self._write()
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/dag/compiled_dag_node.py", line 751, in _write
ERROR 07-11 09:57:36 [core.py:588]     self.output_writer.write(output_val)
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/experimental/channel/common.py", line 617, in write
ERROR 07-11 09:57:36 [core.py:588]     channel.write(val_i, timeout)
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/experimental/channel/shared_memory_channel.py", line 772, in write
ERROR 07-11 09:57:36 [core.py:588]     channel.write(value, timeout)
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/experimental/channel/shared_memory_channel.py", line 597, in write
ERROR 07-11 09:57:36 [core.py:588]     self._buffers[self._next_write_index].write(value, timeout)
ERROR 07-11 09:57:36 [core.py:588]   File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/experimental/channel/shared_memory_channel.py", line 456, in write
ERROR 07-11 09:57:36 [core.py:588]     raise TypeError(msg) from e
ERROR 07-11 09:57:36 [core.py:588] TypeError: Could not serialize the put value (SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=0,prompt_token_ids=[85, 4086, 44, 374, 264, 1550, 42747, 628, 323, 4938, 72816, 44378, 323, 13480, 4712, 369, 444, 10994, 82, 624],mm_inputs=[],mm_hashes=[],mm_positions=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=64, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([1],),num_computed_tokens=0,lora_request=None)], scheduled_cached_reqs=CachedRequestData(req_ids=[], resumed_from_preemption=[], new_token_ids=[], new_block_ids=[], num_computed_tokens=[]), num_scheduled_tokens={'0': 20}, total_num_scheduled_tokens=20, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={}, num_common_prefix_blocks=[1], finished_req_ids=set(), free_encoder_input_ids=[], structured_output_request_ids={}, grammar_bitmask=None, kv_connector_metadata=None), IntermediateTensors(tensors={'hidden_states': tensor([[ 0.0142, -0.0137,  0.0033,  ...,  0.0062,  0.0052,  0.0045],
ERROR 07-11 09:57:36 [core.py:588]         [ 0.3826, -0.4673, -0.2744,  ...,  0.2869,  0.1188,  0.0718],
ERROR 07-11 09:57:36 [core.py:588]         [ 0.4016, -0.5796,  0.0168,  ..., -0.1387,  0.0813,  0.1603],
ERROR 07-11 09:57:36 [core.py:588]         ...,
ERROR 07-11 09:57:36 [core.py:588]         [ 0.1327, -0.1063, -0.0959,  ..., -0.8140,  0.4983, -0.5146],
ERROR 07-11 09:57:36 [core.py:588]         [-0.0643, -0.2620,  0.0656,  ..., -1.1348,  0.4729, -0.1216],
ERROR 07-11 09:57:36 [core.py:588]         [ 0.1147, -0.3320, -0.3613,  ...,  0.2942,  0.0243,  0.3521]],
ERROR 07-11 09:57:36 [core.py:588]        device='npu:0', dtype=torch.float16), 'residual': tensor([[ 2.1828e+01,  3.9100e+02, -2.0977e+00,  ..., -1.0469e+00,
ERROR 07-11 09:57:36 [core.py:588]          -3.3516e+00, -3.3828e+00],
ERROR 07-11 09:57:36 [core.py:588]         [ 1.9727e+00,  6.9648e+00,  4.7754e-01,  ...,  1.3428e-02,
ERROR 07-11 09:57:36 [core.py:588]          -6.6211e-01, -4.1528e-01],
ERROR 07-11 09:57:36 [core.py:588]         [ 2.3398e+00,  7.2227e+00, -3.2129e-01,  ...,  6.1133e-01,
ERROR 07-11 09:57:36 [core.py:588]           2.0752e-03,  2.7466e-01],
ERROR 07-11 09:57:36 [core.py:588]         ...,
ERROR 07-11 09:57:36 [core.py:588]         [ 1.3359e+00,  7.1602e+00, -3.7793e-01,  ..., -2.7002e-01,
ERROR 07-11 09:57:36 [core.py:588]           1.3281e-01,  1.1250e+00],
ERROR 07-11 09:57:36 [core.py:588]         [-8.4717e-02,  4.5938e+00, -7.8564e-01,  ...,  3.3789e-01,
ERROR 07-11 09:57:36 [core.py:588]           1.9043e-02,  5.2393e-01],
ERROR 07-11 09:57:36 [core.py:588]         [ 3.6816e+00,  5.0352e+00, -3.6743e-02,  ..., -1.0449e-01,
ERROR 07-11 09:57:36 [core.py:588]          -2.0703e-01,  5.0977e-01]], device='npu:0', dtype=torch.float16)})):
ERROR 07-11 09:57:36 [core.py:588] ================================================================================
ERROR 07-11 09:57:36 [core.py:588] Checking Serializability of (SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=0,prompt_token_ids=[85, 4086, 44, 374, 264, 1550, 42747, 628, 323, 4938, 72816, 44378, 323, 13480, 4712, 369, 444, 10994, 82, 624],mm_inputs=[],mm_hashes=[],mm_positions=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=64, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([1],),num_computed_tokens=0,lora_request=None)], scheduled_cached_reqs=CachedRequestData(req_ids=[], resumed_from_preemption=[], new_token_ids=[], new_block_ids=[], num_computed_tokens=[]), num_scheduled_tokens={'0': 20}, total_num_scheduled_tokens=20, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={}, num_common_prefix_blocks=[1], finished_req_ids=set(), free_encoder_input_ids=[], structured_output_request_ids={}, grammar_bitmask=None, kv_connector_metadata=None), IntermediateTensors(tensors={'hidden_states': tensor([[ 0.0142, -0.0137,  0.0033,  ...,  0.0062,  0.0052,  0.0045],
ERROR 07-11 09:57:36 [core.py:588]         [ 0.3826, -0.4673, -0.2744,  ...,  0.2869,  0.1188,  0.0718],
ERROR 07-11 09:57:36 [core.py:588]         [ 0.4016, -0.5796,  0.0168,  ..., -0.1387,  0.0813,  0.1603],
ERROR 07-11 09:57:36 [core.py:588]         ...,
ERROR 07-11 09:57:36 [core.py:588]         [ 0.1327, -0.1063, -0.0959,  ..., -0.8140,  0.4983, -0.5146],
ERROR 07-11 09:57:36 [core.py:588]         [-0.0643, -0.2620,  0.0656,  ..., -1.1348,  0.4729, -0.1216],
ERROR 07-11 09:57:36 [core.py:588]         [ 0.1147, -0.3320, -0.3613,  ...,  0.2942,  0.0243,  0.3521]],
ERROR 07-11 09:57:36 [core.py:588]        device='npu:0', dtype=torch.float16), 'residual': tensor([[ 2.1828e+01,  3.9100e+02, -2.0977e+00,  ..., -1.0469e+00,
ERROR 07-11 09:57:36 [core.py:588]          -3.3516e+00, -3.3828e+00],
ERROR 07-11 09:57:36 [core.py:588]         [ 1.9727e+00,  6.9648e+00,  4.7754e-01,  ...,  1.3428e-02,
ERROR 07-11 09:57:36 [core.py:588]          -6.6211e-01, -4.1528e-01],
ERROR 07-11 09:57:36 [core.py:588]         [ 2.3398e+00,  7.2227e+00, -3.2129e-01,  ...,  6.1133e-01,
ERROR 07-11 09:57:36 [core.py:588]           2.0752e-03,  2.7466e-01],
ERROR 07-11 09:57:36 [core.py:588]         ...,
ERROR 07-11 09:57:36 [core.py:588]         [ 1.3359e+00,  7.1602e+00, -3.7793e-01,  ..., -2.7002e-01,
ERROR 07-11 09:57:36 [core.py:588]           1.3281e-01,  1.1250e+00],
ERROR 07-11 09:57:36 [core.py:588]         [-8.4717e-02,  4.5938e+00, -7.8564e-01,  ...,  3.3789e-01,
ERROR 07-11 09:57:36 [core.py:588]           1.9043e-02,  5.2393e-01],
ERROR 07-11 09:57:36 [core.py:588]         [ 3.6816e+00,  5.0352e+00, -3.6743e-02,  ..., -1.0449e-01,
ERROR 07-11 09:57:36 [core.py:588]          -2.0703e-01,  5.0977e-01]], device='npu:0', dtype=torch.float16)}))
ERROR 07-11 09:57:36 [core.py:588] ================================================================================
ERROR 07-11 09:57:36 [core.py:588] !!! FAIL serialization: can't convert npu:0 device type tensor to numpy. Use Tensor.cpu() to copy the tensor to host memory first.
ERROR 07-11 09:57:36 [core.py:588] WARNING: Did not find non-serializable object in (SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=0,prompt_token_ids=[85, 4086, 44, 374, 264, 1550, 42747, 628, 323, 4938, 72816, 44378, 323, 13480, 4712, 369, 444, 10994, 82, 624],mm_inputs=[],mm_hashes=[],mm_positions=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=64, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([1],),num_computed_tokens=0,lora_request=None)], scheduled_cached_reqs=CachedRequestData(req_ids=[], resumed_from_preemption=[], new_token_ids=[], new_block_ids=[], num_computed_tokens=[]), num_scheduled_tokens={'0': 20}, total_num_scheduled_tokens=20, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={}, num_common_prefix_blocks=[1], finished_req_ids=set(), free_encoder_input_ids=[], structured_output_request_ids={}, grammar_bitmask=None, kv_connector_metadata=None), IntermediateTensors(tensors={'hidden_states': tensor([[ 0.0142, -0.0137,  0.0033,  ...,  0.0062,  0.0052,  0.0045],
ERROR 07-11 09:57:36 [core.py:588]         [ 0.3826, -0.4673, -0.2744,  ...,  0.2869,  0.1188,  0.0718],
ERROR 07-11 09:57:36 [core.py:588]         [ 0.4016, -0.5796,  0.0168,  ..., -0.1387,  0.0813,  0.1603],
ERROR 07-11 09:57:36 [core.py:588]         ...,
ERROR 07-11 09:57:36 [core.py:588]         [ 0.1327, -0.1063, -0.0959,  ..., -0.8140,  0.4983, -0.5146],
ERROR 07-11 09:57:36 [core.py:588]         [-0.0643, -0.2620,  0.0656,  ..., -1.1348,  0.4729, -0.1216],
ERROR 07-11 09:57:36 [core.py:588]         [ 0.1147, -0.3320, -0.3613,  ...,  0.2942,  0.0243,  0.3521]],
ERROR 07-11 09:57:36 [core.py:588]        device='npu:0', dtype=torch.float16), 'residual': tensor([[ 2.1828e+01,  3.9100e+02, -2.0977e+00,  ..., -1.0469e+00,
ERROR 07-11 09:57:36 [core.py:588]          -3.3516e+00, -3.3828e+00],
ERROR 07-11 09:57:36 [core.py:588]         [ 1.9727e+00,  6.9648e+00,  4.7754e-01,  ...,  1.3428e-02,
ERROR 07-11 09:57:36 [core.py:588]          -6.6211e-01, -4.1528e-01],
ERROR 07-11 09:57:36 [core.py:588]         [ 2.3398e+00,  7.2227e+00, -3.2129e-01,  ...,  6.1133e-01,
ERROR 07-11 09:57:36 [core.py:588]           2.0752e-03,  2.7466e-01],
ERROR 07-11 09:57:36 [core.py:588]         ...,
ERROR 07-11 09:57:36 [core.py:588]         [ 1.3359e+00,  7.1602e+00, -3.7793e-01,  ..., -2.7002e-01,
ERROR 07-11 09:57:36 [core.py:588]           1.3281e-01,  1.1250e+00],
ERROR 07-11 09:57:36 [core.py:588]         [-8.4717e-02,  4.5938e+00, -7.8564e-01,  ...,  3.3789e-01,
ERROR 07-11 09:57:36 [core.py:588]           1.9043e-02,  5.2393e-01],
ERROR 07-11 09:57:36 [core.py:588]         [ 3.6816e+00,  5.0352e+00, -3.6743e-02,  ..., -1.0449e-01,
ERROR 07-11 09:57:36 [core.py:588]          -2.0703e-01,  5.0977e-01]], device='npu:0', dtype=torch.float16)})). This may be an oversight.
ERROR 07-11 09:57:36 [core.py:588] ================================================================================
ERROR 07-11 09:57:36 [core.py:588] Variable: 
ERROR 07-11 09:57:36 [core.py:588] 
ERROR 07-11 09:57:36 [core.py:588]      FailTuple((SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=0,prompt_token_ids=[85, 4086, 44, 374, 264, 1550, 42747, 628, 323, 4938, 72816, 44378, 323, 13480, 4712, 369, 444, 10994, 82, 624],mm_inputs=[],mm_hashes=[],mm_positions=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=64, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([1],),num_computed_tokens=0,lora_request=None)], scheduled_cached_reqs=CachedRequestData(req_ids=[], resumed_from_preemption=[], new_token_ids=[], new_block_ids=[], num_computed_tokens=[]), num_scheduled_tokens={'0': 20}, total_num_scheduled_tokens=20, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={}, num_common_prefix_blocks=[1], finished_req_ids=set(), free_encoder_input_ids=[], structured_output_request_ids={}, grammar_bitmask=None, kv_connector_metadata=None), IntermediateTensors(tensors={'hidden_states': tensor([[ 0.0142, -0.0137,  0.0033,  ...,  0.0062,  0.0052,  0.0045],
ERROR 07-11 09:57:36 [core.py:588]         [ 0.3826, -0.4673, -0.2744,  ...,  0.2869,  0.1188,  0.0718],
ERROR 07-11 09:57:36 [core.py:588]         [ 0.4016, -0.5796,  0.0168,  ..., -0.1387,  0.0813,  0.1603],
ERROR 07-11 09:57:36 [core.py:588]         ...,
ERROR 07-11 09:57:36 [core.py:588]         [ 0.1327, -0.1063, -0.0959,  ..., -0.8140,  0.4983, -0.5146],
ERROR 07-11 09:57:36 [core.py:588]         [-0.0643, -0.2620,  0.0656,  ..., -1.1348,  0.4729, -0.1216],
ERROR 07-11 09:57:36 [core.py:588]         [ 0.1147, -0.3320, -0.3613,  ...,  0.2942,  0.0243,  0.3521]],
ERROR 07-11 09:57:36 [core.py:588]        device='npu:0', dtype=torch.float16), 'residual': tensor([[ 2.1828e+01,  3.9100e+02, -2.0977e+00,  ..., -1.0469e+00,
ERROR 07-11 09:57:36 [core.py:588]          -3.3516e+00, -3.3828e+00],
ERROR 07-11 09:57:36 [core.py:588]         [ 1.9727e+00,  6.9648e+00,  4.7754e-01,  ...,  1.3428e-02,
ERROR 07-11 09:57:36 [core.py:588]          -6.6211e-01, -4.1528e-01],
ERROR 07-11 09:57:36 [core.py:588]         [ 2.3398e+00,  7.2227e+00, -3.2129e-01,  ...,  6.1133e-01,
ERROR 07-11 09:57:36 [core.py:588]           2.0752e-03,  2.7466e-01],
ERROR 07-11 09:57:36 [core.py:588]         ...,
ERROR 07-11 09:57:36 [core.py:588]         [ 1.3359e+00,  7.1602e+00, -3.7793e-01,  ..., -2.7002e-01,
ERROR 07-11 09:57:36 [core.py:588]           1.3281e-01,  1.1250e+00],
ERROR 07-11 09:57:36 [core.py:588]         [-8.4717e-02,  4.5938e+00, -7.8564e-01,  ...,  3.3789e-01,
ERROR 07-11 09:57:36 [core.py:588]           1.9043e-02,  5.2393e-01],
ERROR 07-11 09:57:36 [core.py:588]         [ 3.6816e+00,  5.0352e+00, -3.6743e-02,  ..., -1.0449e-01,
ERROR 07-11 09:57:36 [core.py:588]          -2.0703e-01,  5.0977e-01]], device='npu:0', dtype=torch.float16)})) [obj=(SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=0,prompt_token_ids=[85, 4086, 44, 374, 264, 1550, 42747, 628, 323, 4938, 72816, 44378, 323, 13480, 4712, 369, 444, 10994, 82, 624],mm_inputs=[],mm_hashes=[],mm_positions=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=64, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([1],),num_computed_tokens=0,lora_request=None)], scheduled_cached_reqs=CachedRequestData(req_ids=[], resumed_from_preemption=[], new_token_ids=[], new_block_ids=[], num_computed_tokens=[]), num_scheduled_tokens={'0': 20}, total_num_scheduled_tokens=20, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={}, num_common_prefix_blocks=[1], finished_req_ids=set(), free_encoder_input_ids=[], structured_output_request_ids={}, grammar_bitmask=None, kv_connector_metadata=None), IntermediateTensors(tensors={'hidden_states': tensor([[ 0.0142, -0.0137,  0.0033,  ...,  0.0062,  0.0052,  0.0045],
ERROR 07-11 09:57:36 [core.py:588]         [ 0.3826, -0.4673, -0.2744,  ...,  0.2869,  0.1188,  0.0718],
ERROR 07-11 09:57:36 [core.py:588]         [ 0.4016, -0.5796,  0.0168,  ..., -0.1387,  0.0813,  0.1603],
ERROR 07-11 09:57:36 [core.py:588]         ...,
ERROR 07-11 09:57:36 [core.py:588]         [ 0.1327, -0.1063, -0.0959,  ..., -0.8140,  0.4983, -0.5146],
ERROR 07-11 09:57:36 [core.py:588]         [-0.0643, -0.2620,  0.0656,  ..., -1.1348,  0.4729, -0.1216],
ERROR 07-11 09:57:36 [core.py:588]         [ 0.1147, -0.3320, -0.3613,  ...,  0.2942,  0.0243,  0.3521]],
ERROR 07-11 09:57:36 [core.py:588]        device='npu:0', dtype=torch.float16), 'residual': tensor([[ 2.1828e+01,  3.9100e+02, -2.0977e+00,  ..., -1.0469e+00,
ERROR 07-11 09:57:36 [core.py:588]          -3.3516e+00, -3.3828e+00],
ERROR 07-11 09:57:36 [core.py:588]         [ 1.9727e+00,  6.9648e+00,  4.7754e-01,  ...,  1.3428e-02,
ERROR 07-11 09:57:36 [core.py:588]          -6.6211e-01, -4.1528e-01],
ERROR 07-11 09:57:36 [core.py:588]         [ 2.3398e+00,  7.2227e+00, -3.2129e-01,  ...,  6.1133e-01,
ERROR 07-11 09:57:36 [core.py:588]           2.0752e-03,  2.7466e-01],
ERROR 07-11 09:57:36 [core.py:588]         ...,
ERROR 07-11 09:57:36 [core.py:588]         [ 1.3359e+00,  7.1602e+00, -3.7793e-01,  ..., -2.7002e-01,
ERROR 07-11 09:57:36 [core.py:588]           1.3281e-01,  1.1250e+00],
ERROR 07-11 09:57:36 [core.py:588]         [-8.4717e-02,  4.5938e+00, -7.8564e-01,  ...,  3.3789e-01,
ERROR 07-11 09:57:36 [core.py:588]           1.9043e-02,  5.2393e-01],
ERROR 07-11 09:57:36 [core.py:588]         [ 3.6816e+00,  5.0352e+00, -3.6743e-02,  ..., -1.0449e-01,
ERROR 07-11 09:57:36 [core.py:588]          -2.0703e-01,  5.0977e-01]], device='npu:0', dtype=torch.float16)})), parent=None])
ERROR 07-11 09:57:36 [core.py:588] 
ERROR 07-11 09:57:36 [core.py:588] was found to be non-serializable. There may be multiple other undetected variables that were non-serializable. 
ERROR 07-11 09:57:36 [core.py:588] Consider either removing the instantiation/imports of these variables or moving the instantiation into the scope of the function/class. 
ERROR 07-11 09:57:36 [core.py:588] ================================================================================
ERROR 07-11 09:57:36 [core.py:588] Check https://docs.ray.io/en/master/ray-core/objects/serialization.html#troubleshooting for more information.
ERROR 07-11 09:57:36 [core.py:588] If you have any suggestions on how to improve this error message, please reach out to the Ray developers on github.com/ray-project/ray/issues/
ERROR 07-11 09:57:36 [core.py:588] ================================================================================
INFO 07-11 09:57:36 [ray_distributed_executor.py:128] Shutting down Ray distributed executor. If you see error log from logging.cc regarding SIGTERM received, please ignore because this is the expected termination process in Ray.
2025-07-11 09:57:36,292 INFO compiled_dag_node.py:2184 -- Waiting for worker tasks to exit
2025-07-11 09:57:36,293 INFO compiled_dag_node.py:2187 -- Teardown complete
Process EngineCore_0:
Traceback (most recent call last):
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/home/xxx/code/vllm-cpu/vllm/vllm/v1/engine/core.py", line 590, in run_engine_core
    raise e
  File "/home/xxx/code/vllm-cpu/vllm/vllm/v1/engine/core.py", line 579, in run_engine_core
    engine_core.run_busy_loop()
  File "/home/xxx/code/vllm-cpu/vllm/vllm/v1/engine/core.py", line 606, in run_busy_loop
    self._process_engine_step()
  File "/home/xxx/code/vllm-cpu/vllm/vllm/v1/engine/core.py", line 631, in _process_engine_step
    outputs, model_executed = self.step_fn()
  File "/home/xxx/code/vllm-cpu/vllm/vllm/v1/engine/core.py", line 283, in step_with_batch_queue
    model_output = future.result()
  File "/home/xxx/code/vllm-cpu/vllm/vllm/v1/executor/ray_distributed_executor.py", line 25, in result
    return self.ref.get()
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/experimental/compiled_dag_ref.py", line 145, in get
    raise execution_error from None
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/experimental/compiled_dag_ref.py", line 136, in get
    ray.get(actor_execution_loop_refs, timeout=10)
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/_private/auto_init_hook.py", line 22, in auto_init_wrapper
    return fn(*args, **kwargs)
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/_private/client_mode_hook.py", line 104, in wrapper
    return func(*args, **kwargs)
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/_private/worker.py", line 2849, in get
    values, debugger_breakpoint = worker.get_objects(object_refs, timeout=timeout)
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/_private/worker.py", line 937, in get_objects
    raise value.as_instanceof_cause()
ray.exceptions.RayTaskError(TypeError): ray::RayWorkerWrapper.__ray_call__() (pid=20614, ip=192.168.144.2, actor_id=a605e09def975470504f1fae01000000, repr=<vllm.executor.ray_utils.RayWorkerWrapper object at 0xfff55f5b1c90>)
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/cloudpickle/cloudpickle.py", line 1479, in dumps
    cp.dump(obj)
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/cloudpickle/cloudpickle.py", line 1245, in dump
    return super().dump(obj)
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/experimental/channel/torch_tensor_type.py", line 121, in serialize
    return ctx.serialization_context.serialize_tensor(t)
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/experimental/channel/serialization_context.py", line 105, in serialize_tensor
    return self.serialize_to_numpy_or_scalar(tensor)
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/experimental/channel/serialization_context.py", line 133, in serialize_to_numpy_or_scalar
    return (tensor.view(torch.uint8).numpy(), tensor.dtype, tensor_device_type)
TypeError: can't convert npu:0 device type tensor to numpy. Use Tensor.cpu() to copy the tensor to host memory first.

The above exception was the direct cause of the following exception:

ray::RayWorkerWrapper.__ray_call__() (pid=20614, ip=192.168.144.2, actor_id=a605e09def975470504f1fae01000000, repr=<vllm.executor.ray_utils.RayWorkerWrapper object at 0xfff55f5b1c90>)
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/actor.py", line 1745, in __ray_call__
    return fn(self, *args, **kwargs)
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/dag/compiled_dag_node.py", line 253, in do_exec_tasks
    done = tasks[operation.exec_task_idx].exec_operation(
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/dag/compiled_dag_node.py", line 786, in exec_operation
    return self._write()
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/dag/compiled_dag_node.py", line 751, in _write
    self.output_writer.write(output_val)
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/experimental/channel/common.py", line 617, in write
    channel.write(val_i, timeout)
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/experimental/channel/shared_memory_channel.py", line 772, in write
    channel.write(value, timeout)
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/experimental/channel/shared_memory_channel.py", line 597, in write
    self._buffers[self._next_write_index].write(value, timeout)
  File "/home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/ray/experimental/channel/shared_memory_channel.py", line 456, in write
    raise TypeError(msg) from e
TypeError: Could not serialize the put value (SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=0,prompt_token_ids=[85, 4086, 44, 374, 264, 1550, 42747, 628, 323, 4938, 72816, 44378, 323, 13480, 4712, 369, 444, 10994, 82, 624],mm_inputs=[],mm_hashes=[],mm_positions=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=64, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([1],),num_computed_tokens=0,lora_request=None)], scheduled_cached_reqs=CachedRequestData(req_ids=[], resumed_from_preemption=[], new_token_ids=[], new_block_ids=[], num_computed_tokens=[]), num_scheduled_tokens={'0': 20}, total_num_scheduled_tokens=20, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={}, num_common_prefix_blocks=[1], finished_req_ids=set(), free_encoder_input_ids=[], structured_output_request_ids={}, grammar_bitmask=None, kv_connector_metadata=None), IntermediateTensors(tensors={'hidden_states': tensor([[ 0.0142, -0.0137,  0.0033,  ...,  0.0062,  0.0052,  0.0045],
        [ 0.3826, -0.4673, -0.2744,  ...,  0.2869,  0.1188,  0.0718],
        [ 0.4016, -0.5796,  0.0168,  ..., -0.1387,  0.0813,  0.1603],
        ...,
        [ 0.1327, -0.1063, -0.0959,  ..., -0.8140,  0.4983, -0.5146],
        [-0.0643, -0.2620,  0.0656,  ..., -1.1348,  0.4729, -0.1216],
        [ 0.1147, -0.3320, -0.3613,  ...,  0.2942,  0.0243,  0.3521]],
       device='npu:0', dtype=torch.float16), 'residual': tensor([[ 2.1828e+01,  3.9100e+02, -2.0977e+00,  ..., -1.0469e+00,
         -3.3516e+00, -3.3828e+00],
        [ 1.9727e+00,  6.9648e+00,  4.7754e-01,  ...,  1.3428e-02,
         -6.6211e-01, -4.1528e-01],
        [ 2.3398e+00,  7.2227e+00, -3.2129e-01,  ...,  6.1133e-01,
          2.0752e-03,  2.7466e-01],
        ...,
        [ 1.3359e+00,  7.1602e+00, -3.7793e-01,  ..., -2.7002e-01,
          1.3281e-01,  1.1250e+00],
        [-8.4717e-02,  4.5938e+00, -7.8564e-01,  ...,  3.3789e-01,
          1.9043e-02,  5.2393e-01],
        [ 3.6816e+00,  5.0352e+00, -3.6743e-02,  ..., -1.0449e-01,
         -2.0703e-01,  5.0977e-01]], device='npu:0', dtype=torch.float16)})):
================================================================================
Checking Serializability of (SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=0,prompt_token_ids=[85, 4086, 44, 374, 264, 1550, 42747, 628, 323, 4938, 72816, 44378, 323, 13480, 4712, 369, 444, 10994, 82, 624],mm_inputs=[],mm_hashes=[],mm_positions=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=64, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([1],),num_computed_tokens=0,lora_request=None)], scheduled_cached_reqs=CachedRequestData(req_ids=[], resumed_from_preemption=[], new_token_ids=[], new_block_ids=[], num_computed_tokens=[]), num_scheduled_tokens={'0': 20}, total_num_scheduled_tokens=20, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={}, num_common_prefix_blocks=[1], finished_req_ids=set(), free_encoder_input_ids=[], structured_output_request_ids={}, grammar_bitmask=None, kv_connector_metadata=None), IntermediateTensors(tensors={'hidden_states': tensor([[ 0.0142, -0.0137,  0.0033,  ...,  0.0062,  0.0052,  0.0045],
        [ 0.3826, -0.4673, -0.2744,  ...,  0.2869,  0.1188,  0.0718],
        [ 0.4016, -0.5796,  0.0168,  ..., -0.1387,  0.0813,  0.1603],
        ...,
        [ 0.1327, -0.1063, -0.0959,  ..., -0.8140,  0.4983, -0.5146],
        [-0.0643, -0.2620,  0.0656,  ..., -1.1348,  0.4729, -0.1216],
        [ 0.1147, -0.3320, -0.3613,  ...,  0.2942,  0.0243,  0.3521]],
       device='npu:0', dtype=torch.float16), 'residual': tensor([[ 2.1828e+01,  3.9100e+02, -2.0977e+00,  ..., -1.0469e+00,
         -3.3516e+00, -3.3828e+00],
        [ 1.9727e+00,  6.9648e+00,  4.7754e-01,  ...,  1.3428e-02,
         -6.6211e-01, -4.1528e-01],
        [ 2.3398e+00,  7.2227e+00, -3.2129e-01,  ...,  6.1133e-01,
          2.0752e-03,  2.7466e-01],
        ...,
        [ 1.3359e+00,  7.1602e+00, -3.7793e-01,  ..., -2.7002e-01,
          1.3281e-01,  1.1250e+00],
        [-8.4717e-02,  4.5938e+00, -7.8564e-01,  ...,  3.3789e-01,
          1.9043e-02,  5.2393e-01],
        [ 3.6816e+00,  5.0352e+00, -3.6743e-02,  ..., -1.0449e-01,
         -2.0703e-01,  5.0977e-01]], device='npu:0', dtype=torch.float16)}))
================================================================================
!!! FAIL serialization: can't convert npu:0 device type tensor to numpy. Use Tensor.cpu() to copy the tensor to host memory first.
WARNING: Did not find non-serializable object in (SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=0,prompt_token_ids=[85, 4086, 44, 374, 264, 1550, 42747, 628, 323, 4938, 72816, 44378, 323, 13480, 4712, 369, 444, 10994, 82, 624],mm_inputs=[],mm_hashes=[],mm_positions=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=64, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([1],),num_computed_tokens=0,lora_request=None)], scheduled_cached_reqs=CachedRequestData(req_ids=[], resumed_from_preemption=[], new_token_ids=[], new_block_ids=[], num_computed_tokens=[]), num_scheduled_tokens={'0': 20}, total_num_scheduled_tokens=20, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={}, num_common_prefix_blocks=[1], finished_req_ids=set(), free_encoder_input_ids=[], structured_output_request_ids={}, grammar_bitmask=None, kv_connector_metadata=None), IntermediateTensors(tensors={'hidden_states': tensor([[ 0.0142, -0.0137,  0.0033,  ...,  0.0062,  0.0052,  0.0045],
        [ 0.3826, -0.4673, -0.2744,  ...,  0.2869,  0.1188,  0.0718],
        [ 0.4016, -0.5796,  0.0168,  ..., -0.1387,  0.0813,  0.1603],
        ...,
        [ 0.1327, -0.1063, -0.0959,  ..., -0.8140,  0.4983, -0.5146],
        [-0.0643, -0.2620,  0.0656,  ..., -1.1348,  0.4729, -0.1216],
        [ 0.1147, -0.3320, -0.3613,  ...,  0.2942,  0.0243,  0.3521]],
       device='npu:0', dtype=torch.float16), 'residual': tensor([[ 2.1828e+01,  3.9100e+02, -2.0977e+00,  ..., -1.0469e+00,
         -3.3516e+00, -3.3828e+00],
        [ 1.9727e+00,  6.9648e+00,  4.7754e-01,  ...,  1.3428e-02,
         -6.6211e-01, -4.1528e-01],
        [ 2.3398e+00,  7.2227e+00, -3.2129e-01,  ...,  6.1133e-01,
          2.0752e-03,  2.7466e-01],
        ...,
        [ 1.3359e+00,  7.1602e+00, -3.7793e-01,  ..., -2.7002e-01,
          1.3281e-01,  1.1250e+00],
        [-8.4717e-02,  4.5938e+00, -7.8564e-01,  ...,  3.3789e-01,
          1.9043e-02,  5.2393e-01],
        [ 3.6816e+00,  5.0352e+00, -3.6743e-02,  ..., -1.0449e-01,
         -2.0703e-01,  5.0977e-01]], device='npu:0', dtype=torch.float16)})). This may be an oversight.
================================================================================
Variable: 

        FailTuple((SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=0,prompt_token_ids=[85, 4086, 44, 374, 264, 1550, 42747, 628, 323, 4938, 72816, 44378, 323, 13480, 4712, 369, 444, 10994, 82, 624],mm_inputs=[],mm_hashes=[],mm_positions=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=64, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([1],),num_computed_tokens=0,lora_request=None)], scheduled_cached_reqs=CachedRequestData(req_ids=[], resumed_from_preemption=[], new_token_ids=[], new_block_ids=[], num_computed_tokens=[]), num_scheduled_tokens={'0': 20}, total_num_scheduled_tokens=20, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={}, num_common_prefix_blocks=[1], finished_req_ids=set(), free_encoder_input_ids=[], structured_output_request_ids={}, grammar_bitmask=None, kv_connector_metadata=None), IntermediateTensors(tensors={'hidden_states': tensor([[ 0.0142, -0.0137,  0.0033,  ...,  0.0062,  0.0052,  0.0045],
        [ 0.3826, -0.4673, -0.2744,  ...,  0.2869,  0.1188,  0.0718],
        [ 0.4016, -0.5796,  0.0168,  ..., -0.1387,  0.0813,  0.1603],
        ...,
        [ 0.1327, -0.1063, -0.0959,  ..., -0.8140,  0.4983, -0.5146],
        [-0.0643, -0.2620,  0.0656,  ..., -1.1348,  0.4729, -0.1216],
        [ 0.1147, -0.3320, -0.3613,  ...,  0.2942,  0.0243,  0.3521]],
       device='npu:0', dtype=torch.float16), 'residual': tensor([[ 2.1828e+01,  3.9100e+02, -2.0977e+00,  ..., -1.0469e+00,
         -3.3516e+00, -3.3828e+00],
        [ 1.9727e+00,  6.9648e+00,  4.7754e-01,  ...,  1.3428e-02,
         -6.6211e-01, -4.1528e-01],
        [ 2.3398e+00,  7.2227e+00, -3.2129e-01,  ...,  6.1133e-01,
          2.0752e-03,  2.7466e-01],
        ...,
        [ 1.3359e+00,  7.1602e+00, -3.7793e-01,  ..., -2.7002e-01,
          1.3281e-01,  1.1250e+00],
        [-8.4717e-02,  4.5938e+00, -7.8564e-01,  ...,  3.3789e-01,
          1.9043e-02,  5.2393e-01],
        [ 3.6816e+00,  5.0352e+00, -3.6743e-02,  ..., -1.0449e-01,
         -2.0703e-01,  5.0977e-01]], device='npu:0', dtype=torch.float16)})) [obj=(SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=0,prompt_token_ids=[85, 4086, 44, 374, 264, 1550, 42747, 628, 323, 4938, 72816, 44378, 323, 13480, 4712, 369, 444, 10994, 82, 624],mm_inputs=[],mm_hashes=[],mm_positions=[],sampling_params=SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=64, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None),block_ids=([1],),num_computed_tokens=0,lora_request=None)], scheduled_cached_reqs=CachedRequestData(req_ids=[], resumed_from_preemption=[], new_token_ids=[], new_block_ids=[], num_computed_tokens=[]), num_scheduled_tokens={'0': 20}, total_num_scheduled_tokens=20, scheduled_spec_decode_tokens={}, scheduled_encoder_inputs={}, num_common_prefix_blocks=[1], finished_req_ids=set(), free_encoder_input_ids=[], structured_output_request_ids={}, grammar_bitmask=None, kv_connector_metadata=None), IntermediateTensors(tensors={'hidden_states': tensor([[ 0.0142, -0.0137,  0.0033,  ...,  0.0062,  0.0052,  0.0045],
        [ 0.3826, -0.4673, -0.2744,  ...,  0.2869,  0.1188,  0.0718],
        [ 0.4016, -0.5796,  0.0168,  ..., -0.1387,  0.0813,  0.1603],
        ...,
        [ 0.1327, -0.1063, -0.0959,  ..., -0.8140,  0.4983, -0.5146],
        [-0.0643, -0.2620,  0.0656,  ..., -1.1348,  0.4729, -0.1216],
        [ 0.1147, -0.3320, -0.3613,  ...,  0.2942,  0.0243,  0.3521]],
       device='npu:0', dtype=torch.float16), 'residual': tensor([[ 2.1828e+01,  3.9100e+02, -2.0977e+00,  ..., -1.0469e+00,
         -3.3516e+00, -3.3828e+00],
        [ 1.9727e+00,  6.9648e+00,  4.7754e-01,  ...,  1.3428e-02,
         -6.6211e-01, -4.1528e-01],
        [ 2.3398e+00,  7.2227e+00, -3.2129e-01,  ...,  6.1133e-01,
          2.0752e-03,  2.7466e-01],
        ...,
        [ 1.3359e+00,  7.1602e+00, -3.7793e-01,  ..., -2.7002e-01,
          1.3281e-01,  1.1250e+00],
        [-8.4717e-02,  4.5938e+00, -7.8564e-01,  ...,  3.3789e-01,
          1.9043e-02,  5.2393e-01],
        [ 3.6816e+00,  5.0352e+00, -3.6743e-02,  ..., -1.0449e-01,
         -2.0703e-01,  5.0977e-01]], device='npu:0', dtype=torch.float16)})), parent=None])

was found to be non-serializable. There may be multiple other undetected variables that were non-serializable. 
Consider either removing the instantiation/imports of these variables or moving the instantiation into the scope of the function/class. 
================================================================================
Check https://docs.ray.io/en/master/ray-core/objects/serialization.html#troubleshooting for more information.
If you have any suggestions on how to improve this error message, please reach out to the Ray developers on github.com/ray-project/ray/issues/
================================================================================
FAILED

=============================================================================== FAILURES ===============================================================================
____________________________________________ test_models[ray-2-1-/home/xxx/cache/modelscope/models/Qwen/Qwen3-0___6B-Base] _____________________________________________

example_prompts = ['vLLM is a high-throughput and memory-efficient inference and serving engine for LLMs.\n', 'Briefly describe the majo...me.\n', 'Analyze the impact of the COVID-19 pandemic on global economic structures and future business models.\n', ...]
model = '/home/xxx/cache/modelscope/models/Qwen/Qwen3-0___6B-Base', tp_size = 1, pp_size = 2, distributed_executor_backend = 'ray'

>   ???

tests/e2e/multicard/test_pipeline_parallel.py:45: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
tests/conftest.py:251: in generate_greedy
    outputs = self.generate(prompts,
tests/conftest.py:166: in generate
    req_outputs = self.model.generate(inputs,
../vllm-cpu/vllm/vllm/utils/__init__.py:1292: in inner
    return fn(*args, **kwargs)
../vllm-cpu/vllm/vllm/entrypoints/llm.py:510: in generate
    outputs = self._run_engine(use_tqdm=use_tqdm)
../vllm-cpu/vllm/vllm/entrypoints/llm.py:1570: in _run_engine
    step_outputs = self.llm_engine.step()
../vllm-cpu/vllm/vllm/v1/engine/llm_engine.py:237: in step
    outputs = self.engine_core.get_output()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <vllm.v1.engine.core_client.SyncMPClient object at 0xfffcc98aece0>

    def get_output(self) -> EngineCoreOutputs:
        # If an exception arises in process_outputs_socket task,
        # it is forwarded to the outputs_queue so we can raise it
        # from this (run_output_handler) task to shut down the server.
        outputs = self.outputs_queue.get()
        if isinstance(outputs, Exception):
>           raise self._format_exception(outputs) from None
E           vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.

../vllm-cpu/vllm/vllm/v1/engine/core_client.py:571: EngineDeadError
=========================================================================== warnings summary ===========================================================================
../../miniconda3/envs/atb/lib/python3.10/site-packages/torch_npu/dynamo/torchair/__init__.py:8
  /home/xxx/miniconda3/envs/atb/lib/python3.10/site-packages/torch_npu/dynamo/torchair/__init__.py:8: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
    import pkg_resources

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================================= short test summary info ========================================================================
FAILED tests/e2e/multicard/test_pipeline_parallel.py::test_models[ray-2-1-/home/xxx/cache/modelscope/models/Qwen/Qwen3-0___6B-Base] - vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
========================================================== 1 failed, 1 passed, 1 warning in 97.83s (0:01:37) ===========================================================
Processed prompts:   0%|          | 0/8 [00:04<?, ?it/s, est. speed input: 0.00 toks/s, output: 0.00 toks/s]  
```
