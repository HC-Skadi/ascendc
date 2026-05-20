# Issue #1713: [Bug]: deepseek双机推理报错

## 基本信息

- **编号**: #1713
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1713
- **创建时间**: 2025-07-10T02:20:21Z
- **关闭时间**: 2025-11-11T13:13:36Z
- **更新时间**: 2025-11-11T13:15:20Z
- **提交者**: @uhuuh
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>deepseek v3 双机推理报错</summary>

```text
按照官网教程，pip方式配置环境，起deepseek v3 双机推理

启动命令，配置文件，报错调用栈如下所示
```

</details>



### 🐛 Describe the bug

```
port_num=6390

python -m vllm.entrypoints.openai.api_server \
       --model="/home/ds/r1_w8a8_ckpt_ffn_concat" \
       --trust-remote-code \
       --distributed_executor_backend "ray" \
       --tensor-parallel-size 8 \
       --pipeline-parallel-size 2 \
       --disable-frontend-multiprocessing \
       --port ${port_num}
```

```
{
    "architectures": [
        "DeepseekV3ForCausalLM"
    ],
    "attention_bias": false,
    "attention_dropout": 0.0,
    "auto_map": {
        "AutoConfig": "configuration_deepseek.DeepseekV3Config",
        "AutoModel": "modeling_deepseek.DeepseekV3Model",
        "AutoModelForCausalLM": "modeling_deepseek.DeepseekV3ForCausalLM"
    },
    "aux_loss_alpha": 0.001,
    "bos_token_id": 0,
    "eos_token_id": 1,
    "ep_size": 1,
    "first_k_dense_replace": 3,
    "hidden_act": "silu",
    "hidden_size": 7168,
    "initializer_range": 0.02,
    "intermediate_size": 18432,
    "kv_lora_rank": 512,
    "max_position_embeddings": 163840,
    "model_type": "deepseek_v3",
    "moe_intermediate_size": 2048,
    "moe_layer_freq": 1,
    "n_group": 8,
    "n_routed_experts": 256,
    "n_shared_experts": 1,
    "norm_topk_prob": true,
    "num_attention_heads": 128,
    "num_experts_per_tok": 8,
    "num_hidden_layers": 4,
    "num_key_value_heads": 128,
    "num_nextn_predict_layers": 1,
    "pad_token_id": 128815,
    "pretraining_tp": 1,
    "q_lora_rank": 1536,
    "qk_nope_head_dim": 128,
    "qk_rope_head_dim": 64,
    "rms_norm_eps": 1e-06,
    "rope_scaling": {
        "beta_fast": 32,
        "beta_slow": 1,
        "factor": 40,
        "mscale": 1.0,
        "mscale_all_dim": 1.0,
        "original_max_position_embeddings": 4096,
        "type": "yarn"
    },
    "rope_theta": 10000,
    "routed_scaling_factor": 2.5,
    "scoring_func": "sigmoid",
    "seq_aux": true,
    "tie_word_embeddings": false,
    "topk_group": 4,
    "topk_method": "noaux_tc",
    "torch_dtype": "bfloat16",
    "transformers_version": "4.48.1",
    "unsloth_fixed": true,
    "use_cache": true,
    "v_head_dim": 128,
    "vocab_size": 129280,
    "quantize": "w8a8_dynamic",
    "quantization_config": {},
    "mla_quantize": "w8a8",
    "quantization_config": {
	    "activation_scheme": "dynamic",
	    "fmt": "e4m3",
	    "quant_method": "fp8",
	    "weight_block_size": [
	      128,
	      128
	    ]
  }
}
```


```
[rank0]: Traceback (most recent call last):
[rank0]:   File "<frozen runpy>", line 198, in _run_module_as_main
[rank0]:   File "<frozen runpy>", line 88, in _run_code
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 1387, in <module>
[rank0]:     uvloop.run(run_server(args))
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/uvloop/__init__.py", line 105, in run
[rank0]:     return runner.run(wrapper())
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/lib64/python3.11/asyncio/runners.py", line 118, in run
[rank0]:     return self._loop.run_until_complete(task)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
[rank0]:     return await main
[rank0]:            ^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 1323, in run_server
[rank0]:     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 1343, in run_server_worker
[rank0]:     async with build_async_engine_client(args, client_config) as engine_client:
[rank0]:   File "/usr/lib64/python3.11/contextlib.py", line 204, in __aenter__
[rank0]:     return await anext(self.gen)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 155, in build_async_engine_client
[rank0]:     async with build_async_engine_client_from_engine_args(
[rank0]:   File "/usr/lib64/python3.11/contextlib.py", line 204, in __aenter__
[rank0]:     return await anext(self.gen)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 213, in build_async_engine_client_from_engine_args
[rank0]:     engine_client = AsyncLLMEngine.from_vllm_config(
[rank0]:                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 628, in from_vllm_config
[rank0]:     return cls(
[rank0]:            ^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 583, in __init__
[rank0]: (raylet, ip=96.13.20.32) [2025-07-09 17:31:56,030 E 42912 42956] (raylet) file_system_monitor.cc:116: /tmp/ray/session_2025-07-09_16-52-46_486747_79577 is over 95% full, available space: 22.7539 GB; capacity: 3445.35 GB. Object creation will fail if spilling is required.
[rank0]:     self.engine = self._engine_class(*args, **kwargs)
[rank0]:                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 266, in __init__
[rank0]:     super().__init__(*args, **kwargs)
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/engine/llm_engine.py", line 265, in __init__
[rank0]:     self.model_executor = executor_class(vllm_config=vllm_config)
[rank0]:                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/executor/executor_base.py", line 287, in __init__
[rank0]:     super().__init__(*args, **kwargs)
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/executor/executor_base.py", line 53, in __init__
[rank0]:     self._init_executor()
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/executor/ray_distributed_executor.py", line 115, in _init_executor
[rank0]:     self._init_workers_ray(placement_group)
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/executor/ray_distributed_executor.py", line 397, in _init_workers_ray
[rank0]:     self._run_workers("load_model",
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/executor/ray_distributed_executor.py", line 517, in _run_workers
[rank0]:     self.driver_worker.execute_method(sent_method, *args, **kwargs)
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/worker/worker_base.py", line 623, in execute_method
[rank0]:     raise e
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/worker/worker_base.py", line 614, in execute_method
[rank0]:     return run_method(self, method, args, kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/utils.py", line 2671, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/worker/worker.py", line 240, in load_model
[rank0]:     self.model_runner.load_model()
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/worker/model_runner.py", line 997, in load_model
[rank0]:     self.model = get_model(vllm_config=self.vllm_config)
[rank0]:                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/model_executor/model_loader/__init__.py", line 59, in get_model
[rank0]:     return loader.load_model(vllm_config=vllm_config,
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/model_executor/model_loader/base_loader.py", line 38, in load_model
[rank0]:     model = initialize_model(vllm_config=vllm_config,
[rank0]:             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/model_executor/model_loader/utils.py", line 62, in initialize_model
[rank0]:     return model_class(vllm_config=vllm_config, prefix=prefix)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/models/deepseek_v2.py", line 730, in __init__
[rank0]:     self.model = CustomDeepseekV2Model(vllm_config=vllm_config,
[rank0]:                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/models/deepseek_v2.py", line 656, in __init__
[rank0]:     self.start_layer, self.end_layer, self.layers = make_layers(
[rank0]:                                                     ^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/model_executor/models/utils.py", line 626, in make_layers
[rank0]:     [PPMissingLayer() for _ in range(start_layer)] + [
[rank0]:                                                      ^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/model_executor/models/utils.py", line 627, in <listcomp>
[rank0]:     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
[rank0]:                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/models/deepseek_v2.py", line 658, in <lambda>
[rank0]:     lambda prefix: CustomDeepseekV2DecoderLayer(
[rank0]:                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/models/deepseek_v2.py", line 532, in __init__
[rank0]:     self.self_attn = attn_cls(
[rank0]:                      ^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/models/deepseek_v2.py", line 369, in __init__
[rank0]:     self.q_a_proj = ReplicatedLinear(self.hidden_size,
[rank0]:                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/model_executor/layers/linear.py", line 280, in __init__
[rank0]:     super().__init__(input_size,
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm/model_executor/layers/linear.py", line 243, in __init__
[rank0]:     self.quant_method = quant_config.get_quant_method(self,
[rank0]:                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/quantization/quant_config.py", line 92, in get_quant_method
[rank0]:     if self.is_layer_skipped_ascend(prefix,
[rank0]:        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/usr/local/lib64/python3.11/site-packages/vllm_ascend/quantization/quant_config.py", line 136, in is_layer_skipped_ascend
[rank0]:     is_skipped = self.quant_description[prefix + '.weight'] == "FLOAT"
[rank0]:                  ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
[rank0]: KeyError: 'model.layers.0.self_attn.q_a_proj.weight'
```
