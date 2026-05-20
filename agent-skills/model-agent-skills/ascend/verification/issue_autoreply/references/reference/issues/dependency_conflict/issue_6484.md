# Issue #6484: [Bug]: vllm-ascend离线推理方式运行qwen_2.5_7b模型报错

## 基本信息

- **编号**: #6484
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6484
- **创建时间**: 2026-02-02T06:40:53Z
- **关闭时间**: 2026-02-02T07:21:04Z
- **更新时间**: 2026-02-02T07:21:04Z
- **提交者**: @rocks-sudo
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

qwen2.5 -7b量化模型，用vllm-ascend跑报错KeyError: 'model.embed_tokens.weight'。在h800+vllm上跑正常，配置如下
llm_model = LLM(
    model="xxxx/quantized_model_awq_quant4",
    quantization="awq",
    dtype="float16",
    tensor_parallel_size=1,
    trust_remote_code=True,
    distributed_executor_backend="mp",
    max_num_batched_tokens=32000,
    max_model_len=17000,
    enable_prefix_caching=True,
    gpu_memory_utilization=0.9,
)

报错信息：
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597] WorkerProc failed to start.
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597] Traceback (most recent call last):
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]   File "/usr/local/miniconda3/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 571, in worker_main
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]     worker = WorkerProc(*args, **kwargs)
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]   File "/usr/local/miniconda3/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 437, in __init__
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]     self.worker.load_model()
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]   File "/usr/local/miniconda3/lib/python3.10/site-packages/vllm_ascend/worker/worker_v1.py", line 291, in load_model
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]     self.model_runner.load_model()
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]   File "/usr/local/miniconda3/lib/python3.10/site-packages/vllm_ascend/worker/model_runner_v1.py", line 2630, in load_model
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]     self.model = get_model(vllm_config=self.vllm_config)
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]   File "/usr/local/miniconda3/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 119, in get_model
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]     return loader.load_model(vllm_config=vllm_config,
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]   File "/usr/local/miniconda3/lib/python3.10/site-packages/vllm/model_executor/model_loader/base_loader.py", line 45, in load_model
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]     model = initialize_model(vllm_config=vllm_config,
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]   File "/usr/local/miniconda3/lib/python3.10/site-packages/vllm/model_executor/model_loader/utils.py", line 63, in initialize_model
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]     return model_class(vllm_config=vllm_config, prefix=prefix)
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]   File "/usr/local/miniconda3/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 468, in __init__
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]     self.model = Qwen2Model(vllm_config=vllm_config,
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]   File "/usr/local/miniconda3/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 201, in __init__
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]   File "/usr/local/miniconda3/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 308, in __init__
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]     self.embed_tokens = VocabParallelEmbedding(
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]   File "/usr/local/miniconda3/lib/python3.10/site-packages/vllm_ascend/ops/vocab_parallel_embedding.py", line 81, in __init__
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]     quant_method = quant_config.get_quant_method(self, prefix=prefix)
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]   File "/usr/local/miniconda3/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 120, in get_quant_method
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]     if self.is_layer_skipped_ascend(prefix,
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]   File "/usr/local/miniconda3/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 152, in is_layer_skipped_ascend
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597]     is_skipped = self.quant_description[prefix + '.weight'] == "FLOAT"
(EngineCore_DP0 pid=235945) (Worker pid=235952) ERROR 01-31 14:26:22 [multiproc_executor.py:597] KeyError: 'model.embed_tokens.weight'
(EngineCore_DP0 pid=235945) ERROR 01-31 14:26:23 [core.py:708] EngineCore failed to start.
(EngineCore_DP0 pid=235945) ERROR 01-31 14:26:23 [core.py:708] Traceback (most recent call last):
(EngineCore_DP0 pid=235945) ERROR 01-31 14:26:23 [core.py:708]   File "/usr/local/miniconda3/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 699, in run_engine_core

### 🐛 Describe the bug

vllm-ascend离线推理方式运行qwen_2.5_7b模型报错，KeyError: 'model.embed_tokens.weight'。在h800+vllm上跑正常
