# Issue #2984: [Bug]: deepseekv3 startup error

## 基本信息

- **编号**: #2984
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2984
- **创建时间**: 2025-09-17T08:57:15Z
- **关闭时间**: 2025-11-13T08:15:44Z
- **更新时间**: 2025-11-13T08:15:44Z
- **提交者**: @sleepy-dev-bin
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

I used docker: quay.io/ascend/vllm-ascend:v0.9.1

### 🐛 Describe the bug

**used 4x910B3**
**model weights:** https://modelscope.cn/models/deepseek-ai/DeepSeek-V3
**start scripts:**

> **node1:**

#!/bin/sh
nic_name="xxxx"
local_ip=$(ifconfig $nic_name | grep inet | grep -v inet6 | awk '{print $2}')
echo $local_ip
export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=100
export HCCL_BUFFSIZE=1024

```
vllm serve DeepSeek-V3 \
        --host 0.0.0.0 \
        --port 8004 \
        --data-parallel-size 4 \
        --data-parallel-size-local 1 \
        --data-parallel-start-rank 0 \
        --data-parallel-address $local_ip \
        --data-parallel-rpc-port 13389 \
        --tensor-parallel-size 8 \
        --seed 1024 \
        --served-model-name Deepseek-V3 \
        --enable-expert-parallel \
        --max-num-seqs 16 \
        --max-model-len 4096 \
        --quantization ascend \
        --max-num-batched-tokens 4096 \
        --trust-remote-code \
        --no-enable-prefix-caching \
        --gpu-memory-utilization 0.9 \
        --additional-config '{"ascend_scheduler_config":{"enabled":true},"torchair_graph_config":{"enabled":true}}'

```

> **node2:**
```
#!/bin/sh
nic_name="enp67s0f5"
local_ip=$(ifconfig $nic_name | grep inet | grep -v inet6 | awk '{print $2}')
echo $local_ip
export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=100
export HCCL_BUFFSIZE=1024

vllm serve /data/deepseekv3/models/DeepSeek-V3 \
        --host 0.0.0.0 \
        --port 8004 \
        --headless \
        --data-parallel-size 4 \
        --data-parallel-size-local 1 \
        --data-parallel-start-rank 1 \
        --data-parallel-address 192.168.0.1 \
        --data-parallel-rpc-port 13389 \
        --tensor-parallel-size 8 \
        --seed 1024 \
        --served-model-name Deepseek-V3 \
        --enable-expert-parallel \
        --max-num-seqs 16 \
        --max-model-len 4096 \
        --quantization ascend \
        --max-num-batched-tokens 4096 \
        --trust-remote-code \
        --no-enable-prefix-caching \
        --gpu-memory-utilization 0.9 \
        --additional-config '{"ascend_scheduler_config":{"enabled":true},"torchair_graph_config":{"enabled":true}}'`
```
node3 and node4 just need to change --data-parallel-start-rank to 2, 3.

**errors:**
 ```
(VllmWorker rank=5 pid=14564) INFO 09-17 08:35:31 [model_runner_v1.py:1897] Starting to load model DeepSeek-V3...
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492] WorkerProc failed to start.
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492] Traceback (most recent call last):
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 466, in worker_main
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]     worker = WorkerProc(*args, **kwargs)
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 363, in __init__
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]     self.worker.load_model()
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 238, in load_model
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]     self.model_runner.load_model()
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1900, in load_model
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]     self.model = get_model(vllm_config=self.vllm_config)
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/__init__.py", line 59, in get_model
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]     return loader.load_model(vllm_config=vllm_config,
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/base_loader.py", line 38, in load_model
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]     model = initialize_model(vllm_config=vllm_config,
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]   File "/vllm-workspace/vllm/vllm/model_executor/model_loader/utils.py", line 62, in initialize_model
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]     return model_class(vllm_config=vllm_config, prefix=prefix)
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 833, in __init__
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]     self.model = CustomDeepseekV2Model(vllm_config=vllm_config,
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]   File "/vllm-workspace/vllm-ascend/vllm_ascend/models/deepseek_v2.py", line 751, in __init__
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]     self.embed_tokens = VocabParallelEmbedding(
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]                         ^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]   File "/vllm-workspace/vllm/vllm/model_executor/layers/vocab_parallel_embedding.py", line 234, in __init__
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]     quant_method = quant_config.get_quant_method(self, prefix=prefix)
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 110, in get_quant_method
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]     if self.is_layer_skipped_ascend(prefix,
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]   File "/vllm-workspace/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 143, in is_layer_skipped_ascend
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]     is_skipped = self.quant_description[prefix + '.weight'] == "FLOAT"
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492]                  ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
(VllmWorker rank=0 pid=14559) ERROR 09-17 08:35:32 [multiproc_executor.py:492] KeyError: 'model.embed_tokens.weight'
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515] EngineCore failed to start.
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515] Traceback (most recent call last):
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 504, in run_engine_core
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515]     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 764, in __init__
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515]     super().__init__(vllm_config, on_head_node, handshake_address,
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 390, in __init__
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 76, in __init__
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515]     self.model_executor = executor_class(vllm_config)
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 53, in __init__
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515]     self._init_executor()
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 98, in _init_executor
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515]     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 427, in wait_for_ready
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515]     raise e from None
(EngineCore_1 pid=14480) ERROR 09-17 08:35:36 [core.py:515] Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
(EngineCore_1 pid=14480) Process EngineCore_1:
(EngineCore_1 pid=14480) Traceback (most recent call last):
(EngineCore_1 pid=14480)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_1 pid=14480)     self.run()
(EngineCore_1 pid=14480)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_1 pid=14480)     self._target(*self._args, **self._kwargs)
(EngineCore_1 pid=14480)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 519, in run_engine_core
(EngineCore_1 pid=14480)     raise e
(EngineCore_1 pid=14480)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 504, in run_engine_core
(EngineCore_1 pid=14480)     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_1 pid=14480)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_1 pid=14480)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 764, in __init__
(EngineCore_1 pid=14480)     super().__init__(vllm_config, on_head_node, handshake_address,
(EngineCore_1 pid=14480)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 390, in __init__
(EngineCore_1 pid=14480)     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_1 pid=14480)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 76, in __init__
(EngineCore_1 pid=14480)     self.model_executor = executor_class(vllm_config)
(EngineCore_1 pid=14480)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_1 pid=14480)   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 53, in __init__
(EngineCore_1 pid=14480)     self._init_executor()
(EngineCore_1 pid=14480)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 98, in _init_executor
(EngineCore_1 pid=14480)     self.workers = WorkerProc.wait_for_ready(unready_workers)
(EngineCore_1 pid=14480)                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_1 pid=14480)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 427, in wait_for_ready
(EngineCore_1 pid=14480)     raise e from None
(EngineCore_1 pid=14480) Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.
```

If using vllm-ascend, ascend quantization must be employed; the source model cannot be used directly.？
