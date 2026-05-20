# Issue #2077: [Installation]: VLLM Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 using --pipeline-parallel-size 2

## 基本信息

- **编号**: #2077
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2077
- **创建时间**: 2025-07-29T05:24:34Z
- **关闭时间**: 2025-08-14T20:03:22Z
- **更新时间**: 2025-09-09T08:37:09Z
- **提交者**: @isnuryusuf
- **评论数**: 2

## 标签

installation

## 问题描述

### Your current environment

Env:
1Server with 8GPU, configure kubernetes and Run LeaderWorkerSet API (LWS)
Replica set to 2
each POD have 4 GPU H200, total 8GPU, ray cluster show 8GPU and 2Node

VLLM Config:
```
          - bash /vllm-workspace/examples/online_serving/multi-node-serving.sh leader
            --ray_cluster_size=$(LWS_GROUP_SIZE); python3 -m vllm.entrypoints.openai.api_server
            --host 0.0.0.0 --port 8080 --served-model-name qwen-coder --tool-call-parser
            qwen3_coder --model /models/Qwen3-Coder-480B-A35B-Instruct-FP8 --download-dir
            /models --api-key xxxxxxxxxxxxxxxxx
            --enable-auto-tool-choice --enable-chunked-prefill --enable-prefix-caching
            --enable-expert-parallel --tensor-parallel-size 4 --gpu-memory-utilization
            0.95 --max-model-len 262144 --pipeline-parallel-size 2 --enable-expert-parallel
```

during startup we found error bellow, when removed `--pipeline-parallel-size 2` we can start the POD, but looks like the GPU utilization only 4 GPU

question: did the model can be devided into multiple neural network ?

```
2025-07-29T12:19:19.333962774+07:00 stdout F (RayWorkerWrapper pid=549) INFO 07-28 22:19:18 [gpu_model_runner.py:1875] Loading model from scratch...
2025-07-29T12:19:19.333966385+07:00 stdout F (RayWorkerWrapper pid=549) INFO 07-28 22:19:18 [cuda.py:290] Using Flash Attention backend on V1 engine.
2025-07-29T12:19:19.333970143+07:00 stdout F (RayWorkerWrapper pid=549) WARNING 07-28 22:19:18 [fp8.py:535] CutlassBlockScaledGroupedGemm not supported on the current platform.
2025-07-29T12:19:19.333973773+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632] EngineCore failed to start.
2025-07-29T12:19:19.333978309+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632] Traceback (most recent call last):
2025-07-29T12:19:19.333985278+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]   File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 623, in run_engine_core
2025-07-29T12:19:19.333989299+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]     engine_core = EngineCoreProc(*args, **kwargs)
2025-07-29T12:19:19.333992405+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-29T12:19:19.333995969+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]   File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 441, in __init__
2025-07-29T12:19:19.333999405+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]     super().__init__(vllm_config, executor_class, log_stats,
2025-07-29T12:19:19.333892453+07:00 stderr F Process EngineCore_0:
2025-07-29T12:19:19.334003049+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]   File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 77, in __init__
2025-07-29T12:19:19.334020336+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]     self.model_executor = executor_class(vllm_config)
2025-07-29T12:19:19.334023161+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-07-29T12:19:19.334025736+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]   File "/usr/local/lib/python3.12/dist-packages/vllm/executor/executor_base.py", line 263, in __init__
2025-07-29T12:19:19.334028665+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]     super().__init__(*args, **kwargs)
2025-07-29T12:19:19.33403102+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]   File "/usr/local/lib/python3.12/dist-packages/vllm/executor/executor_base.py", line 53, in __init__
2025-07-29T12:19:19.334045825+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]     self._init_executor()
2025-07-29T12:19:19.334048821+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]   File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/ray_distributed_executor.py", line 47, in _init_executor
2025-07-29T12:19:19.334051287+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]     super()._init_executor()
2025-07-29T12:19:19.334053467+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]   File "/usr/local/lib/python3.12/dist-packages/vllm/executor/ray_distributed_executor.py", line 107, in _init_executor
2025-07-29T12:19:19.334055727+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]     self._init_workers_ray(placement_group)
2025-07-29T12:19:19.334057867+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]   File "/usr/local/lib/python3.12/dist-packages/vllm/executor/ray_distributed_executor.py", line 378, in _init_workers_ray
2025-07-29T12:19:19.334060334+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]     self._run_workers("load_model",
2025-07-29T12:19:19.3340717+07:00 stdout F ERROR 07-28 22:19:19 [core.py:632]   File "/usr/local/lib/python3.12/dist-packages/vllm/executor/ray_distributed_executor.py", line 503, in _run_workers

```


### How you are installing vllm and vllm-ascend

```sh
pip install -vvv vllm vllm-ascend
```

