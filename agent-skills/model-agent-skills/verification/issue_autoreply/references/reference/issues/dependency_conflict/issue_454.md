# Issue #454: [Bug]: rtGetDeviceIndexByPhyId execute failed when runing TP4DP2 on a single node with V1

## 基本信息

- **编号**: #454
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/454
- **创建时间**: 2025-04-01T08:55:27Z
- **关闭时间**: 2025-07-12T17:19:21Z
- **更新时间**: 2025-07-12T17:19:21Z
- **提交者**: @yangqinj
- **评论数**: 8

## 标签

bug

## 问题描述

### Your current environment

Version of main package:

vllm: main branch with commit 726efc6a320ad9a4ef0b0378b40abbd0561ea394 with extra modification for ascend
vllm-ascend: main branch with commit https://github.com/vllm-project/vllm-ascend/commit/b1557abab6534af830f1555f262332aba2bf6e51 with extra modification to adapt to vllm main branch
torch：2.5.1
torch-npu: 2.5.1.dev20250320


### 🐛 Describe the bug

vllm implements data parallel by creating number of data-parallel-size EngineCore instances and setting `CUDA_VISIBLE_DEVICES` for each instance. If deploy service on a single node with `tensor-parallel-size=4` and `data-parallel-size=2` arguments, then vllm will create 2 EngineCores and `EngineCore_0` will see `0,1,2,3` and `EngineCore_1` will see `4,5,6,7`.

To adap to ascend npu, I add the following code to set `ASCEND_RT_VISIBLE_DEVICES` for each EngineCore instance:
```python
diff --git a/vllm/platforms/interface.py b/vllm/platforms/interface.py
--- a/vllm/platforms/interface.py
+++ b/vllm/platforms/interface.py
@@ -379,6 +379,16 @@ class Platform:
         """
         return False

+    @classmethod
+    def device_id_to_physical_device_id(cls, device_id: int) -> int:
+        import os
+        if cls.device_control_env_var in os.environ:
+            device_ids = os.environ[cls.device_control_env_var].split(",")
+            physical_device_id = device_ids[device_id]
+            return int(physical_device_id)
+        else:
+            return device_id
+

 class UnspecifiedPlatform(Platform):
     _enum = PlatformEnum.UNSPECIFIED

diff --git a/vllm/v1/engine/core.py b/vllm/v1/engine/core.py
--- a/vllm/v1/engine/core.py
+++ b/vllm/v1/engine/core.py
@@ -534,6 +534,13 @@ class DPEngineCoreProc(EngineCoreProc):
                 str(device_id_to_physical_device_id(i))
                 for i in range(local_dp_rank * tp_size, (local_dp_rank + 1) *
                                tp_size))
+        else:
+            from vllm.platforms import current_platform
+            tp_size = vllm_config.parallel_config.tensor_parallel_size
+            os.environ[current_platform.device_control_env_var] = ",".join(
+                str(current_platform.device_id_to_physical_device_id(i))
+                for i in range(local_dp_rank * tp_size, (local_dp_rank + 1) *
+                               tp_size))

         self.dp_group = vllm_config.parallel_config.stateless_init_dp_group()

```

And I check the `ASCEND_RT_VISIBLE_DEVICES` env variable is right:
```bash
[1;36m(EngineCore_1 pid=97610)[0;0m INFO 04-01 08:03:21 [core.py:547] +++ ASCEND_RT_VISIBLE_DEVICES: 4,5,6,7
[1;36m(EngineCore_0 pid=97609)[0;0m INFO 04-01 08:03:21 [core.py:547] +++ ASCEND_RT_VISIBLE_DEVICES: 0,1,2,3
```

But when run into the `broadcast` funciton in `naive_multicast` for `fused_moe`, `rtGetDeviceIndexByPhyId execute failed` error is raised:
```bash
[1;36m(VllmWorker rank=0 pid=97890)[0;0m INFO 04-01 08:04:30 [layer.py:860] +++ naive_multicast rank: 0 ranks: [0, 4] world_size: 2 local_rank: 0 rank in group: 0 dp_rank： 0 
[1;36m(VllmWorker rank=0 pid=97890)[0;0m INFO 04-01 08:04:30 [parallel_state.py:346] +++ broadcast rank: 0 ranks: [0, 4] src: 0 src in ranks: 0 device_group: hccl device_group.rank: 0
[1;36m(VllmWorker rank=2 pid=97997)[0;0m INFO 04-01 08:04:31 [layer.py:860] +++ naive_multicast rank: 2 ranks: [2, 6] world_size: 2 local_rank: 2 rank in group: 0 dp_rank： 0 
[1;36m(VllmWorker rank=2 pid=97997)[0;0m INFO 04-01 08:04:31 [parallel_state.py:346] +++ broadcast rank: 2 ranks: [2, 6] src: 0 src in ranks: 2 device_group: hccl device_group.rank: 0
[1;36m(VllmWorker rank=3 pid=98490)[0;0m INFO 04-01 08:04:31 [layer.py:860] +++ naive_multicast rank: 3 ranks: [3, 7] world_size: 2 local_rank: 3 rank in group: 0 dp_rank： 0 
[1;36m(VllmWorker rank=3 pid=98490)[0;0m INFO 04-01 08:04:31 [parallel_state.py:346] +++ broadcast rank: 3 ranks: [3, 7] src: 0 src in ranks: 3 device_group: hccl device_group.rank: 0
[1;36m(VllmWorker rank=1 pid=97934)[0;0m INFO 04-01 08:04:31 [layer.py:860] +++ naive_multicast rank: 1 ranks: [1, 5] world_size: 2 local_rank: 1 rank in group: 0 dp_rank： 0 
[1;36m(VllmWorker rank=1 pid=97934)[0;0m INFO 04-01 08:04:31 [parallel_state.py:346] +++ broadcast rank: 1 ranks: [1, 5] src: 0 src in ranks: 1 device_group: hccl device_group.rank: 0
[1;36m(VllmWorker rank=1 pid=97920)[0;0m INFO 04-01 08:04:31 [layer.py:860] +++ naive_multicast rank: 5 ranks: [1, 5] world_size: 2 local_rank: 1 rank in group: 1 dp_rank： 1 
[1;36m(VllmWorker rank=1 pid=97920)[0;0m INFO 04-01 08:04:31 [parallel_state.py:346] +++ broadcast rank: 5 ranks: [1, 5] src: 0 src in ranks: 1 device_group: hccl device_group.rank: 1
[1;36m(VllmWorker rank=2 pid=97980)[0;0m INFO 04-01 08:04:31 [layer.py:860] +++ naive_multicast rank: 6 ranks: [2, 6] world_size: 2 local_rank: 2 rank in group: 1 dp_rank： 1 
[1;36m(VllmWorker rank=2 pid=97980)[0;0m INFO 04-01 08:04:31 [parallel_state.py:346] +++ broadcast rank: 6 ranks: [2, 6] src: 0 src in ranks: 2 device_group: hccl device_group.rank: 1
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383] WorkerProc hit an exception: %s
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383] Traceback (most recent call last):
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 376, in worker_busy_loop
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     output = func(*args, **kwargs)
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker_v1.py", line 171, in determine_available_memory
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     self.model_runner.profile_run()
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner_v1.py", line 717, in profile_run
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     hidden_states = self._dummy_run(self.max_num_tokens)
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     return func(*args, **kwargs)
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner_v1.py", line 683, in _dummy_run
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     hidden_states = model(input_ids=input_ids,
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     return self._call_impl(*args, **kwargs)
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     return forward_call(*args, **kwargs)
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_moe.py", line 413, in forward
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     hidden_states = self.model(input_ids, positions, intermediate_tensors,
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 172, in __call__
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     return self.forward(*args, **kwargs)
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_moe.py", line 371, in forward
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     hidden_states, residual = layer(positions, hidden_states, residual)
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     return self._call_impl(*args, **kwargs)
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     return forward_call(*args, **kwargs)
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_moe.py", line 317, in forward
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     hidden_states = self.mlp(hidden_states)
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     return self._call_impl(*args, **kwargs)
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     return forward_call(*args, **kwargs)
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2_moe.py", line 154, in forward
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     final_hidden_states = self.experts(hidden_states=hidden_states,
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     return self._call_impl(*args, **kwargs)
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     return forward_call(*args, **kwargs)
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/layer.py", line 881, in forward
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     return torch.ops.vllm.moe_forward(hidden_states, router_logits,
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     return self._op(*args, **(kwargs or {}))
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/layer.py", line 1010, in moe_forward
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     return self.forward_impl(hidden_states, router_logits)
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/layer.py", line 892, in forward_impl
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     hidden_states = self.naive_multicast(hidden_states,
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/fused_moe/layer.py", line 871, in naive_multicast
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     get_dp_group().broadcast(buffer[start:end, :], idx)
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/distributed/parallel_state.py", line 358, in broadcast
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     torch.distributed.broadcast(input_,
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/distributed/c10d_logger.py", line 83, in wrapper
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     return func(*args, **kwargs)
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 2421, in broadcast
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]     work = group.broadcast([tensor], opts)
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383] RuntimeError: create_config:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:102 HCCL function error: hcclCommInitRootInfoConfig(numRanks, &rootInfo, rank, config, &(comm->hcclComm_)), error code is 15
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383] [ERROR] 2025-04-01-08:04:31 (PID:97934, Device:1, RankID:-1) ERR02200 DIST call hccl api failed.
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383] EE9999: Inner Error!
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383] EE9999: [PID: 97934] 2025-04-01-08:04:31.591.683 get error: phyid:5 realDeviceId:5 is err:0x7010003[FUNC:GetDeviceIndexByPhyId][FILE:api_error.cc][LINE:1918]
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]         TraceBack (most recent call last):
[1;36m(VllmWorker rank=1 pid=97934)[0;0m ERROR 04-01 08:04:31 [multiproc_executor.py:383]        rtGetDeviceIndexByPhyId execute failed, reason=[device id error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
...

# same exception are raised for all devices
```

You can check from the log that ranks of each data parallel group are right:
```bash
$ grep -rn "+++ naive_multicast" log_service_tp_dp
284:(VllmWorker rank=0 pid=97890) INFO 04-01 08:04:30 [layer.py:860] +++ naive_multicast rank: 0 ranks: [0, 4] world_size: 2 local_rank: 0 rank in group: 0 dp_rank： 0
286:(VllmWorker rank=2 pid=97997) INFO 04-01 08:04:31 [layer.py:860] +++ naive_multicast rank: 2 ranks: [2, 6] world_size: 2 local_rank: 2 rank in group: 0 dp_rank： 0
288:(VllmWorker rank=3 pid=98490) INFO 04-01 08:04:31 [layer.py:860] +++ naive_multicast rank: 3 ranks: [3, 7] world_size: 2 local_rank: 3 rank in group: 0 dp_rank： 0
290:(VllmWorker rank=1 pid=97934) INFO 04-01 08:04:31 [layer.py:860] +++ naive_multicast rank: 1 ranks: [1, 5] world_size: 2 local_rank: 1 rank in group: 0 dp_rank： 0
292:(VllmWorker rank=1 pid=97920) INFO 04-01 08:04:31 [layer.py:860] +++ naive_multicast rank: 5 ranks: [1, 5] world_size: 2 local_rank: 1 rank in group: 1 dp_rank： 1
294:(VllmWorker rank=2 pid=97980) INFO 04-01 08:04:31 [layer.py:860] +++ naive_multicast rank: 6 ranks: [2, 6] world_size: 2 local_rank: 2 rank in group: 1 dp_rank： 1
418:(VllmWorker rank=3 pid=98477) INFO 04-01 08:04:31 [layer.py:860] +++ naive_multicast rank: 7 ranks: [3, 7] world_size: 2 local_rank: 3 rank in group: 1 dp_rank： 1
664:(VllmWorker rank=0 pid=97893) INFO 04-01 08:04:31 [layer.py:860] +++ naive_multicast rank: 4 ranks: [0, 4] world_size: 2 local_rank: 0 rank in group: 1 dp_rank： 1
```



