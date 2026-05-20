# Issue #573: [Bug]: call aclnnSwiGlu failed,  Get path and read binary_info_config.json failed

## 基本信息

- **编号**: #573
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/573
- **创建时间**: 2025-04-18T08:40:21Z
- **关闭时间**: 2025-05-14T05:26:08Z
- **更新时间**: 2025-05-14T05:26:08Z
- **提交者**: @xdfai4x
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>call aclnnSwiGlu failed,  Get path and read binary_info_config.json failed</summary>
environment:
```sh
root@c25c6825ad8e:/workspace# npu-smi info
+------------------------------------------------------------------------------------------------+
| npu-smi 23.0.rc2                 Version: 23.0.rc2                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B                | OK            | 69.4        35                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           1452 / 15137      1    / 32768         |
+===========================+===============+====================================================+
| 1     910B                | OK            | 66.4        37                0    / 0             |
| 0                         | 0000:81:00.0  | 0           1824 / 15137      0    / 32768         |
+===========================+===============+====================================================+
| 2     910B                | OK            | 69.9        37                0    / 0             |
| 0                         | 0000:41:00.0  | 0           1857 / 15137      0    / 32768         |
+===========================+===============+====================================================+
| 3     910B                | OK            | 66.8        36                0    / 0             |
| 0                         | 0000:01:00.0  | 0           2624 / 15039      0    / 32768         |
+===========================+===============+====================================================+
| 4     910B                | OK            | 69.9        35                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           1273 / 15137      0    / 32768         |
+===========================+===============+====================================================+
| 5     910B                | OK            | 67.1        36                0    / 0             |
| 0                         | 0000:82:00.0  | 0           2021 / 15137      0    / 32768         |
+===========================+===============+====================================================+
| 6     910B                | OK            | 69.9        36                0    / 0             |
| 0                         | 0000:42:00.0  | 0           1761 / 15137      0    / 32768         |
+===========================+===============+====================================================+
| 7     910B                | OK            | 67.4        35                0    / 0             |
| 0                         | 0000:02:00.0  | 0           2413 / 15039      0    / 32768         |
+===========================+===============+====================================================+
```
```sh
# Update DEVICE according to your device (/dev/davinci[0-7])
export DEVICE=/dev/davinci0
# Update the vllm-ascend image
export IMAGE=quay.io/ascend/vllm-ascend:v0.7.3rc2

docker run --rm \
--name vllm-ascend \
--device $DEVICE \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
--privileged=true \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-p 8000:8000 \
-it $IMAGE bash
```

</details>


### 🐛 Describe the bug

docker run failed with the following error:
issue: 
```
ERROR 04-18 08:22:17 engine.py:400] call aclnnSwiGlu failed, detail:EZ1001: [PID: 426] 2025-04-18-08:22:17.195.330 Get path and read binary_info_config.json failed, please check if the opp_kernel package is installed!
ERROR 04-18 08:22:17 engine.py:400]         TraceBack (most recent call last):
ERROR 04-18 08:22:17 engine.py:400]         Check NnopbaseCollecterWork(binCollecter.get()) failed
ERROR 04-18 08:22:17 engine.py:400]         Assert ((NnopbaseInit()) == 0) failed
ERROR 04-18 08:22:17 engine.py:400]         Check NnopbaseCreateExecutorSpace(&executorSpace) failed
ERROR 04-18 08:22:17 engine.py:400]
ERROR 04-18 08:22:17 engine.py:400] [ERROR] 2025-04-18-08:22:17 (PID:426, Device:0, RankID:-1) ERR01100 OPS call acl api failed
ERROR 04-18 08:22:17 engine.py:400] Traceback (most recent call last):
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 391, in run_mp_engine
ERROR 04-18 08:22:17 engine.py:400]     engine = MQLLMEngine.from_engine_args(engine_args=engine_args,
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 124, in from_engine_args
ERROR 04-18 08:22:17 engine.py:400]     return cls(ipc_path=ipc_path,
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 76, in __init__
ERROR 04-18 08:22:17 engine.py:400]     self.engine = LLMEngine(*args, **kwargs)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 276, in __init__
ERROR 04-18 08:22:17 engine.py:400]     self._initialize_kv_caches()
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 421, in _initialize_kv_caches
ERROR 04-18 08:22:17 engine.py:400]     self.model_executor.determine_num_available_blocks())
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 102, in determine_num_available_blocks
ERROR 04-18 08:22:17 engine.py:400]     results = self.collective_rpc("determine_num_available_blocks")
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
ERROR 04-18 08:22:17 engine.py:400]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
ERROR 04-18 08:22:17 engine.py:400]     return func(*args, **kwargs)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 04-18 08:22:17 engine.py:400]     return func(*args, **kwargs)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 227, in determine_num_available_blocks
ERROR 04-18 08:22:17 engine.py:400]     self.model_runner.profile_run()
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 04-18 08:22:17 engine.py:400]     return func(*args, **kwargs)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1366, in profile_run
ERROR 04-18 08:22:17 engine.py:400]     self.execute_model(model_input, kv_caches, intermediate_tensors)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
ERROR 04-18 08:22:17 engine.py:400]     return func(*args, **kwargs)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1146, in execute_model
ERROR 04-18 08:22:17 engine.py:400]     hidden_or_intermediate_states = model_executable(
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 04-18 08:22:17 engine.py:400]     return self._call_impl(*args, **kwargs)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 04-18 08:22:17 engine.py:400]     return forward_call(*args, **kwargs)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 486, in forward
ERROR 04-18 08:22:17 engine.py:400]     hidden_states = self.model(input_ids, positions, kv_caches,
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 172, in __call__
ERROR 04-18 08:22:17 engine.py:400]     return self.forward(*args, **kwargs)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 348, in forward
ERROR 04-18 08:22:17 engine.py:400]     hidden_states, residual = layer(
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 04-18 08:22:17 engine.py:400]     return self._call_impl(*args, **kwargs)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 04-18 08:22:17 engine.py:400]     return forward_call(*args, **kwargs)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 257, in forward
ERROR 04-18 08:22:17 engine.py:400]     hidden_states = self.mlp(hidden_states)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 04-18 08:22:17 engine.py:400]     return self._call_impl(*args, **kwargs)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 04-18 08:22:17 engine.py:400]     return forward_call(*args, **kwargs)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 96, in forward
ERROR 04-18 08:22:17 engine.py:400]     x = self.act_fn(gate_up)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
ERROR 04-18 08:22:17 engine.py:400]     return self._call_impl(*args, **kwargs)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
ERROR 04-18 08:22:17 engine.py:400]     return forward_call(*args, **kwargs)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/custom_op.py", line 25, in forward
ERROR 04-18 08:22:17 engine.py:400]     return self._forward_method(*args, **kwargs)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/ops/activation.py", line 25, in silu_and_mul_forward_oot
ERROR 04-18 08:22:17 engine.py:400]     out = torch_npu.npu_swiglu(x)
ERROR 04-18 08:22:17 engine.py:400]   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
ERROR 04-18 08:22:17 engine.py:400]     return self._op(*args, **(kwargs or {}))
```
