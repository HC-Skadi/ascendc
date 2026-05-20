# Issue #1059: [Bug][CI Failure]: AttributeError: `ParallelConfig` object has no attribute `expert_parallel_size`

## 基本信息

- **编号**: #1059
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1059
- **创建时间**: 2025-06-04T03:28:23Z
- **关闭时间**: 2025-06-09T15:03:12Z
- **更新时间**: 2025-06-10T01:33:10Z
- **提交者**: @shen-shanshan
- **评论数**: 1

## 标签

bug; help wanted

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

Run vllm-ascend long term test in CI, get this error:

```bash
self = <vllm_ascend.worker.worker.NPUWorker object at 0xfffb03085cf0>
vllm_config = VllmConfig(model_config=ModelConfig(model='wemaster/deepseek_mtp_main_random_bf16', task='draft', tokenizer='wemaster/...":0,"local_cache_dir":null}, kv_transfer_config=None, kv_events_config=None, additional_config={}, instance_id='fc6e4')
rank = 0, distributed_init_method = 'tcp://10.0.0.107:40471', local_rank = 0
backend = 'hccl'

    def _init_worker_distributed_environment(
            self,
            vllm_config: VllmConfig,
            rank: int,
            distributed_init_method: Optional[str] = None,
            local_rank: int = -1,
            backend: str = "hccl") -> None:
        """Initialize the distributed environment."""
        parallel_config = self.parallel_config
        set_custom_all_reduce(not parallel_config.disable_custom_all_reduce)
        init_distributed_environment(parallel_config.world_size, rank,
                                     distributed_init_method, local_rank,
                                     backend)
        ensure_model_parallel_initialized(
            parallel_config.tensor_parallel_size,
            parallel_config.pipeline_parallel_size)
        init_ascend_model_parallel(
>           parallel_config.expert_parallel_size,
            parallel_config.expert_tensor_parallel_size,
            parallel_config.world_size,
        )
E       AttributeError: 'ParallelConfig' object has no attribute 'expert_parallel_size'. Did you mean: 'tensor_parallel_size'?

vllm_ascend/worker/worker.py:545: AttributeError
```

There is no `expert_parallel_size` attribute in latest `main` of vllm.

Help wanted to sync these changes with vllm upstream.
