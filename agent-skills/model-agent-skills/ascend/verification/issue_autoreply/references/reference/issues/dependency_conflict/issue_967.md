# Issue #967: [Bug]: qwen2.5-omni-3b服务启动报错

## 基本信息

- **编号**: #967
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/967
- **创建时间**: 2025-05-27T03:11:23Z
- **关闭时间**: 2025-07-12T16:21:24Z
- **更新时间**: 2025-07-12T16:21:24Z
- **提交者**: @heavenrain99
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

硬件：910b3
软件：
torch:2.5.1
torch-npu:2.5.1
cann: 8.1.rc1
vllm && vllm-npu:0.8.5.post1

### 🐛 Describe the bug

服务运行命令： vllm serve qwen2.5-omni-3B 
报错信息：
```
File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 278, in __init__

    self._initialize_kv_caches()

  File "/vllm-workspace/vllm/vllm/engine/llm_engine.py", line 422, in _initialize_kv_caches

    self.model_executor.determine_num_available_blocks())

  File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 103, in determine_num_available_blocks

    results = self.collective_rpc("determine_num_available_blocks")

  File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 56, in collective_rpc

    answer = run_method(self.driver_worker, method, args, kwargs)

  File "/vllm-workspace/vllm/vllm/utils.py", line 2456, in run_method

    return func(*args, **kwargs)

  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context

    return func(*args, **kwargs)

  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 283, in determine_num_available_blocks

    self.model_runner.profile_run()

  File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context

    return func(*args, **kwargs)

  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1138, in profile_run

    model_input = self.prepare_model_input(

  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1242, in prepare_model_input

    model_input = self._prepare_model_input_tensors(

  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 1052, in _prepare_model_input_tensors

    builder.add_seq_group(seq_group_metadata)

  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 487, in add_seq_group

    per_seq_group_fn(inter_data, seq_group_metadata)

  File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner.py", line 819, in _compute_multi_modal_input

    MRotaryEmbedding.get_input_positions(

  File "/vllm-workspace/vllm/vllm/model_executor/layers/rotary_embedding.py", line 1024, in get_input_positions

    cls.get_input_positions_tensor(

  File "/vllm-workspace/vllm/vllm/model_executor/layers/rotary_embedding.py", line 1053, in get_input_positions_tensor

    return cls._omni_get_input_positions_tensor(

  File "/vllm-workspace/vllm/vllm/model_executor/layers/rotary_embedding.py", line 1256, in _omni_get_input_positions_tensor

    assert audio_seqlens is not None
```
