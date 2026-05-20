# Issue #2176: [Bug]:Ascend310P3 encountered an exception while running seed-x

## 基本信息

- **编号**: #2176
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2176
- **创建时间**: 2025-08-02T06:06:19Z
- **关闭时间**: 2025-08-05T01:42:43Z
- **更新时间**: 2025-08-05T01:44:21Z
- **提交者**: @shaojun0
- **评论数**: 2

## 标签

bug

## 问题描述

### current environment

#### sysinfo
| key                  | value         |
| -------------------- | ------------- |
| docker image    | vllm-ascend:v0.9.2rc1-310p        |
| NPU                  | ascend 310p*1 |
| model                  | Seed-X-PPO-7B |
#### docker compose
```yaml
services:
  seed-x-1:
    image: quay.nju.edu.cn/ascend/vllm-ascend:v0.9.2rc1-310p
    container_name: seed-x-1
    devices:
      - "/dev/davinci1"
      - "/dev/davinci_manager"
      - "/dev/devmm_svm"
      - "/dev/hisi_hdc"
    volumes:
      - "/usr/local/dcmi:/usr/local/dcmi"
      - "/usr/local/bin/npu-smi:/usr/local/bin/npu-smi"
      - "/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64"
      - "/usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info"
      - "/etc/ascend_install.info:/etc/ascend_install.info"
      - "./models:/data/models"
      - "/root/.cache:/root/.cache"
    command: ["python3","-m","vllm.entrypoints.openai.api_server","--max_model_len","4096","--dtype","float16","--served-model-name","seed-x","--model","/data/models/Seed-X-PPO-7B"]
```

### 🐛 Describe the bug
```shell

INFO 08-02 05:45:49 [parallel_state.py:1076] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0

INFO 08-02 05:45:50 [model_runner_v1.py:1745] Starting to load model /data/models/Seed-X-PPO-7B...

Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]

Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:01<00:00,  1.92s/it]

Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:01<00:00,  1.92s/it]



INFO 08-02 05:45:52 [default_loader.py:272] Loading weights took 1.94 seconds

INFO 08-02 05:45:53 [model_runner_v1.py:1777] Loading model weights took 14.0046 GB

INFO 08-02 05:46:07 [backends.py:508] Using cache directory: /root/.cache/vllm/torch_compile_cache/24ae571172/rank_0_0/backbone for vLLM's torch.compile

INFO 08-02 05:46:07 [backends.py:519] Dynamo bytecode transform time: 6.94 s

INFO 08-02 05:46:09 [backends.py:193] Compiling a graph for general shape takes 1.60 s

.INFO 08-02 05:46:15 [monitor.py:34] torch.compile takes 8.54 s in total

INFO 08-02 05:46:16 [worker_v1.py:181] Available memory: 24180219801, total memory: 45816029184

INFO 08-02 05:46:16 [kv_cache_utils.py:716] GPU KV cache size: 184,448 tokens

INFO 08-02 05:46:16 [kv_cache_utils.py:720] Maximum concurrency for 4,096 tokens per request: 45.03x

ERROR 08-02 05:46:18 [core.py:586] EngineCore failed to start.

ERROR 08-02 05:46:18 [core.py:586] Traceback (most recent call last):

ERROR 08-02 05:46:18 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 577, in run_engine_core

ERROR 08-02 05:46:18 [core.py:586]     engine_core = EngineCoreProc(*args, **kwargs)

ERROR 08-02 05:46:18 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 404, in __init__

ERROR 08-02 05:46:18 [core.py:586]     super().__init__(vllm_config, executor_class, log_stats,

ERROR 08-02 05:46:18 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 82, in __init__

ERROR 08-02 05:46:18 [core.py:586]     self._initialize_kv_caches(vllm_config)

ERROR 08-02 05:46:18 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 169, in _initialize_kv_caches

ERROR 08-02 05:46:18 [core.py:586]     self.model_executor.initialize_from_config(kv_cache_configs)

ERROR 08-02 05:46:18 [core.py:586]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 66, in initialize_from_config

ERROR 08-02 05:46:18 [core.py:586]     self.collective_rpc("compile_or_warm_up_model")

ERROR 08-02 05:46:18 [core.py:586]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 57, in collective_rpc

ERROR 08-02 05:46:18 [core.py:586]     answer = run_method(self.driver_worker, method, args, kwargs)

ERROR 08-02 05:46:18 [core.py:586]   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 2736, in run_method

ERROR 08-02 05:46:18 [core.py:586]     return func(*args, **kwargs)

ERROR 08-02 05:46:18 [core.py:586]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 253, in compile_or_warm_up_model

ERROR 08-02 05:46:18 [core.py:586]     self.model_runner.capture_model()

ERROR 08-02 05:46:18 [core.py:586]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2064, in capture_model

ERROR 08-02 05:46:18 [core.py:586]     self._dummy_run(num_tokens)

ERROR 08-02 05:46:18 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context

ERROR 08-02 05:46:18 [core.py:586]     return func(*args, **kwargs)

ERROR 08-02 05:46:18 [core.py:586]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1663, in _dummy_run

ERROR 08-02 05:46:18 [core.py:586]     hidden_states = model(

ERROR 08-02 05:46:18 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl

ERROR 08-02 05:46:18 [core.py:586]     return self._call_impl(*args, **kwargs)

ERROR 08-02 05:46:18 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl

ERROR 08-02 05:46:18 [core.py:586]     return forward_call(*args, **kwargs)

ERROR 08-02 05:46:18 [core.py:586]   File "/vllm-workspace/vllm/vllm/model_executor/models/llama.py", line 581, in forward

ERROR 08-02 05:46:18 [core.py:586]     model_output = self.model(input_ids, positions, intermediate_tensors,

ERROR 08-02 05:46:18 [core.py:586]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 246, in __call__

ERROR 08-02 05:46:18 [core.py:586]     model_output = self.forward(*args, **kwargs)

ERROR 08-02 05:46:18 [core.py:586]   File "/vllm-workspace/vllm/vllm/model_executor/models/llama.py", line 368, in forward

ERROR 08-02 05:46:18 [core.py:586]     def forward(

ERROR 08-02 05:46:18 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl

ERROR 08-02 05:46:18 [core.py:586]     return self._call_impl(*args, **kwargs)

ERROR 08-02 05:46:18 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl

ERROR 08-02 05:46:18 [core.py:586]     return forward_call(*args, **kwargs)

ERROR 08-02 05:46:18 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/_dynamo/eval_frame.py", line 632, in _fn

ERROR 08-02 05:46:18 [core.py:586]     return fn(*args, **kwargs)

ERROR 08-02 05:46:18 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/fx/graph_module.py", line 784, in call_wrapped

ERROR 08-02 05:46:18 [core.py:586]     return self._wrapped_call(self, *args, **kwargs)

ERROR 08-02 05:46:18 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/fx/graph_module.py", line 361, in __call__

ERROR 08-02 05:46:18 [core.py:586]     raise e

ERROR 08-02 05:46:18 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/fx/graph_module.py", line 348, in __call__

ERROR 08-02 05:46:18 [core.py:586]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]

ERROR 08-02 05:46:18 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl

ERROR 08-02 05:46:18 [core.py:586]     return self._call_impl(*args, **kwargs)

ERROR 08-02 05:46:18 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl

ERROR 08-02 05:46:18 [core.py:586]     return forward_call(*args, **kwargs)

ERROR 08-02 05:46:18 [core.py:586]   File "<eval_with_key>.66", line 202, in forward

ERROR 08-02 05:46:18 [core.py:586]     submod_0 = self.submod_0(l_input_ids_, s0, l_self_modules_embed_tokens_parameters_weight_, l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_, l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_, l_positions_, s1, l_self_modules_layers_modules_0_modules_self_attn_modules_rotary_emb_buffers_cos_sin_cache_);  l_input_ids_ = l_self_modules_embed_tokens_parameters_weight_ = l_self_modules_layers_modules_0_modules_input_layernorm_parameters_weight_ = l_self_modules_layers_modules_0_modules_self_attn_modules_qkv_proj_parameters_weight_ = None

ERROR 08-02 05:46:18 [core.py:586]   File "/vllm-workspace/vllm-ascend/vllm_ascend/compilation/piecewise_backend.py", line 192, in __call__

ERROR 08-02 05:46:18 [core.py:586]     with torch.npu.graph(aclgraph, pool=self.graph_pool):

ERROR 08-02 05:46:18 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/npu/graphs.py", line 310, in __enter__

ERROR 08-02 05:46:18 [core.py:586]     self.npu_graph.capture_begin(

ERROR 08-02 05:46:18 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/npu/graphs.py", line 210, in capture_begin

ERROR 08-02 05:46:18 [core.py:586]     super().capture_begin(pool=pool, capture_error_mode=capture_error_mode)

ERROR 08-02 05:46:18 [core.py:586] RuntimeError: status == aclmdlRICaptureStatus::ACL_MODEL_RI_CAPTURE_STATUS_ACTIVE INTERNAL ASSERT FAILED at "build/CMakeFiles/torch_npu.dir/compiler_depend.ts":162, please report a bug to PyTorch.
```
