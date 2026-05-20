# Issue #4546: [Bug]: DP parallel + TP > 1 offline inference failed: address already in use

## 基本信息

- **编号**: #4546
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4546
- **创建时间**: 2025-11-28T11:27:53Z
- **关闭时间**: 2025-12-03T09:07:52Z
- **更新时间**: 2025-12-03T09:07:52Z
- **提交者**: @leo-pony
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
vllm 0.11.2 + vllm ascend
```

</details>


### 🐛 Describe the bug

[Bug]: DP parallel + TP > 1 offline inference failed: port already in use.

Reproduce scrip:
```
    python examples/offline_data_parallel_vllm.py \
            --model="Qwen/Qwen3-0.6B" \
            --dp-size=2 \
            --tp-size=2 \
            --disable-expert-parallel
```
Error information:
```
ERROR 11-28 11:22:27 [multiproc_executor.py:743] WorkerProc failed to start.
ERROR 11-28 11:22:27 [multiproc_executor.py:743] Traceback (most recent call last):
ERROR 11-28 11:22:27 [multiproc_executor.py:743]   File "/data_mnj/code/fork_repo/vllm_mnj/vllm/vllm/v1/executor/multiproc_executor.py", line 715, in worker_main
ERROR 11-28 11:22:27 [multiproc_executor.py:743]     worker = WorkerProc(*args, **kwargs)
ERROR 11-28 11:22:27 [multiproc_executor.py:743]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 11-28 11:22:27 [multiproc_executor.py:743]   File "/data_mnj/code/fork_repo/vllm_mnj/vllm/vllm/v1/executor/multiproc_executor.py", line 546, in __init__
ERROR 11-28 11:22:27 [multiproc_executor.py:743]     self.worker.init_device()
ERROR 11-28 11:22:27 [multiproc_executor.py:743]   File "/data_mnj/code/fork_repo/vllm_mnj/vllm/vllm/v1/worker/worker_base.py", line 324, in init_device
ERROR 11-28 11:22:27 [multiproc_executor.py:743]     self.worker.init_device()  # type: ignore
ERROR 11-28 11:22:27 [multiproc_executor.py:743]     ^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 11-28 11:22:27 [multiproc_executor.py:743]   File "/data_mnj/code/fork_repo/wxy/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 235, in init_device
ERROR 11-28 11:22:27 [multiproc_executor.py:743]     self.device = self._init_device()
ERROR 11-28 11:22:27 [multiproc_executor.py:743]                   ^^^^^^^^^^^^^^^^^^^
ERROR 11-28 11:22:27 [multiproc_executor.py:743]   File "/data_mnj/code/fork_repo/wxy/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 226, in _init_device
ERROR 11-28 11:22:27 [multiproc_executor.py:743]     self._init_worker_distributed_environment()
ERROR 11-28 11:22:27 [multiproc_executor.py:743]   File "/data_mnj/code/fork_repo/wxy/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 413, in _init_worker_distributed_environment
ERROR 11-28 11:22:27 [multiproc_executor.py:743]     init_distributed_environment(self.parallel_config.world_size,
ERROR 11-28 11:22:27 [multiproc_executor.py:743]   File "/data_mnj/code/fork_repo/vllm_mnj/vllm/vllm/distributed/parallel_state.py", line 1285, in init_distributed_environment
ERROR 11-28 11:22:27 [multiproc_executor.py:743]     torch.distributed.init_process_group(
ERROR 11-28 11:22:27 [multiproc_executor.py:743]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/c10d_logger.py", line 81, in wrapper
ERROR 11-28 11:22:27 [multiproc_executor.py:743]     return func(*args, **kwargs)
ERROR 11-28 11:22:27 [multiproc_executor.py:743]            ^^^^^^^^^^^^^^^^^^^^^
ERROR 11-28 11:22:27 [multiproc_executor.py:743]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/c10d_logger.py", line 95, in wrapper
ERROR 11-28 11:22:27 [multiproc_executor.py:743]     func_return = func(*args, **kwargs)
ERROR 11-28 11:22:27 [multiproc_executor.py:743]                   ^^^^^^^^^^^^^^^^^^^^^
ERROR 11-28 11:22:27 [multiproc_executor.py:743]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/distributed_c10d.py", line 1710, in init_process_group
ERROR 11-28 11:22:27 [multiproc_executor.py:743]     store, rank, world_size = next(rendezvous_iterator)
ERROR 11-28 11:22:27 [multiproc_executor.py:743]                               ^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 11-28 11:22:27 [multiproc_executor.py:743]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/rendezvous.py", line 230, in _tcp_rendezvous_handler
ERROR 11-28 11:22:27 [multiproc_executor.py:743]     store = _create_c10d_store(
ERROR 11-28 11:22:27 [multiproc_executor.py:743]             ^^^^^^^^^^^^^^^^^^^
ERROR 11-28 11:22:27 [multiproc_executor.py:743]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/rendezvous.py", line 198, in _create_c10d_store
ERROR 11-28 11:22:27 [multiproc_executor.py:743]     return TCPStore(
ERROR 11-28 11:22:27 [multiproc_executor.py:743]            ^^^^^^^^^
ERROR 11-28 11:22:27 [multiproc_executor.py:743] torch.distributed.DistNetworkError: The server socket has failed to listen on any local network address. port: 56065, useIpv6: false, code: -98, name: EADDRINUSE, message: address already in use
```
