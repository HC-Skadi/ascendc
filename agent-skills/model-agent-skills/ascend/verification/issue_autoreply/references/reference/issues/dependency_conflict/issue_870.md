# Issue #870: [Usage]: con't start vllm offline with NPUs by ray used in RLHF

## 基本信息

- **编号**: #870
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/870
- **创建时间**: 2025-05-15T09:08:29Z
- **关闭时间**: 2025-05-22T22:43:12Z
- **更新时间**: 2025-05-22T22:43:12Z
- **提交者**: @janelu9
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

```text
class vLLM(LLM):
    def __init__(self, *args, **kwargs):
        os.environ.pop("CUDA_VISIBLE_DEVICES", None)
        os.environ.pop("ASCEND_RT_VISIBLE_DEVICES", None)
        super().__init__(*args, **kwargs)
        
def init_vllm(address,
              model,
              gpu_memory_utilization=0.5,
              tensor_parallel_size=1,
              pipeline_parallel_size=1,
              gpus=1,
              max_num_batched_tokens=1024,
              max_model_len=1024):
    from ray.util.placement_group import placement_group
    from ray.util.scheduling_strategies import PlacementGroupSchedulingStrategy
    
    ray.init(address=address,ignore_reinit_error=True)
    if hasattr(torch,'npu'):
        pg = placement_group([{"NPU": 1, "CPU": 0}]*gpus)
    else:
        pg = placement_group([{"GPU": 1, "CPU": 0}]*gpus)
    ray.get(pg.ready())

    vllm_actor = ray.remote(
        num_cpus=0,
        num_gpus=0,
        scheduling_strategy=PlacementGroupSchedulingStrategy(
            placement_group=pg,
            placement_group_capture_child_tasks=True,
        ),
    )(vLLM).options(name="llm",namespace="vllm", lifetime="detached").remote(
        model=model,
        enforce_eager=True,
        worker_extension_cls="rlhf_utils.WorkerExtension",
        tensor_parallel_size=tensor_parallel_size,
        pipeline_parallel_size=pipeline_parallel_size,
        distributed_executor_backend="ray",
        gpu_memory_utilization=gpu_memory_utilization,
        max_num_batched_tokens=max_num_batched_tokens,
        max_model_len=max_model_len,
    )
    ray.get(vllm_actor.collective_rpc.remote("report_device_id"))
    return vllm_actor
```
```
[Error] The device is unavailable.
```
![image](https://github.com/user-attachments/assets/8e8279d7-891d-43d2-955d-d22d4c3f3b7b)

```rlhf_utils.py``` can be achived here. https://docs.vllm.ai/en/latest/getting_started/examples/rlhf_utils.html
``` vllm serve Qwen2.5-7B``` could run successful!


