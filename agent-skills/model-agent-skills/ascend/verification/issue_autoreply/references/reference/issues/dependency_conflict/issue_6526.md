# Issue #6526: [Bug]: vllm-ascend v0.14.0rc1-310p 部署Qwen3-coder-30B报错

## 基本信息

- **编号**: #6526
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6526
- **创建时间**: 2026-02-04T03:31:14Z
- **关闭时间**: 2026-02-04T03:33:57Z
- **更新时间**: 2026-02-04T03:33:57Z
- **提交者**: @lin807095501
- **评论数**: 0

## 标签

bug

## 问题描述

### Your current environment

我使用的镜像是vllm-ascend v0.14.0rc1-310p的arm64版本，启动docker的指令是：
docker run -it -d --net=host --shm-size=200g --name vllm-qwen-coder -w /home \
            --device /dev/davinci4\
           --device /dev/davinci5\
           --device /dev/davinci6\
           --device /dev/davinci7\
           --device /dev/davinci_manager\
           --device /dev/hisi_hdc\
           --device /dev/devmm_svm\
           -v /usr/local/Ascend/driver:/usr/local/Ascend/driver:ro\
           -v /usr/local/dcmi:/usr/local/dcmi:ro\
           -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi:ro\
           -v /usr/local/sbin/:/usr/local/sbin:ro\
           -v /datadir/Qwen3-Coder-30B-A3B-Instruct:/root/work/Qwen3-Coder-30B-A3B-Instruct:rw \
           a14bc3fdeb2d bash
执行vllm serve报错信息如下，前面的都是正常执行，但出现了一个WARNING 02-03 07:19:44 [camem.py:66] Failed to import vllm_ascend_C:/vllm-workspace/vllm-ascend/vllm_ascend/vllm_ascend_C.cpython-311-aarch64-linux-gnu.so: undefined symbol: _ZN9pp_matmul17GetPpMatmulTilingERKNS_10MatMulInfoERKNS_12HardwareInfoERjRNS_18PpMatmulTilingDataE. Sleep mode will be disabled. 
之后是正常执行，但在加载权重之后就开始报错了
Loading safetensors checkpoint shards:   0% Completed | 0/16 [00:00<?, ?it/s]

[0;36m(Worker_TP0 pid=273)[0;0m Loading safetensors checkpoint shards:   6% Completed | 1/16 [00:01<00:22,  1.50s/it]

[0;36m(Worker_TP0 pid=273)[0;0m Loading safetensors checkpoint shards:  12% Completed | 2/16 [00:03<00:21,  1.50s/it]

[0;36m(Worker_TP0 pid=273)[0;0m Loading safetensors checkpoint shards:  19% Completed | 3/16 [00:04<00:19,  1.48s/it]

[0;36m(Worker_TP0 pid=273)[0;0m Loading safetensors checkpoint shards:  25% Completed | 4/16 [00:05<00:17,  1.44s/it]

[0;36m(Worker_TP0 pid=273)[0;0m Loading safetensors checkpoint shards:  31% Completed | 5/16 [00:07<00:15,  1.45s/it]

[0;36m(Worker_TP0 pid=273)[0;0m Loading safetensors checkpoint shards:  38% Completed | 6/16 [00:08<00:14,  1.46s/it]

[0;36m(Worker_TP0 pid=273)[0;0m Loading safetensors checkpoint shards:  44% Completed | 7/16 [00:10<00:13,  1.48s/it]

[0;36m(Worker_TP0 pid=273)[0;0m Loading safetensors checkpoint shards:  50% Completed | 8/16 [00:11<00:11,  1.48s/it]

[0;36m(Worker_TP0 pid=273)[0;0m Loading safetensors checkpoint shards:  56% Completed | 9/16 [00:12<00:07,  1.12s/it]

[0;36m(Worker_TP0 pid=273)[0;0m Loading safetensors checkpoint shards:  62% Completed | 10/16 [00:13<00:07,  1.22s/it]

[0;36m(Worker_TP0 pid=273)[0;0m Loading safetensors checkpoint shards:  69% Completed | 11/16 [00:15<00:06,  1.29s/it]

[0;36m(Worker_TP0 pid=273)[0;0m Loading safetensors checkpoint shards:  75% Completed | 12/16 [00:16<00:05,  1.35s/it]

[0;36m(Worker_TP0 pid=273)[0;0m Loading safetensors checkpoint shards:  81% Completed | 13/16 [00:17<00:04,  1.39s/it]

[0;36m(Worker_TP0 pid=273)[0;0m Loading safetensors checkpoint shards:  88% Completed | 14/16 [00:19<00:02,  1.46s/it]

[0;36m(Worker_TP0 pid=273)[0;0m Loading safetensors checkpoint shards:  94% Completed | 15/16 [00:21<00:01,  1.47s/it]

[0;36m(Worker_TP0 pid=273)[0;0m Loading safetensors checkpoint shards: 100% Completed | 16/16 [00:22<00:00,  1.48s/it]

[0;36m(Worker_TP0 pid=273)[0;0m Loading safetensors checkpoint shards: 100% Completed | 16/16 [00:22<00:00,  1.41s/it]

[0;36m(Worker_TP0 pid=273)[0;0m 

[0;36m(Worker_TP0 pid=273)[0;0m INFO 02-03 07:20:39 [default_loader.py:291] Loading weights took 22.58 seconds

[0;36m(Worker_TP2 pid=275)[0;0m INFO 02-03 07:20:39 [model_runner_v1.py:2205] Loading model weights took 14.2651 GB

[0;36m(Worker_TP0 pid=273)[0;0m INFO 02-03 07:20:40 [model_runner_v1.py:2205] Loading model weights took 14.2651 GB

[0;36m(Worker_TP3 pid=276)[0;0m INFO 02-03 07:20:40 [model_runner_v1.py:2205] Loading model weights took 14.2651 GB

[0;36m(Worker_TP1 pid=274)[0;0m INFO 02-03 07:20:41 [model_runner_v1.py:2205] Loading model weights took 14.2651 GB

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822] WorkerProc hit an exception.

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822] Traceback (most recent call last):

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 817, in worker_busy_loop

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]     output = func(*args, **kwargs)

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]              ^^^^^^^^^^^^^^^^^^^^^

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]     return func(*args, **kwargs)

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 262, in determine_available_memory

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]     self.model_runner.profile_run()

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2176, in profile_run

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]     super().profile_run()

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/v1/worker/gpu_model_runner.py", line 4743, in profile_run

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]     hidden_states, last_hidden_states = self._dummy_run(

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]                                         ^^^^^^^^^^^^^^^^

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]     return func(*args, **kwargs)

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2118, in _dummy_run

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]     hidden_states = self._generate_dummy_run_hidden_states(

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1905, in _generate_dummy_run_hidden_states

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]     hidden_states = self.model(input_ids=input_ids,

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]     return self._call_impl(*args, **kwargs)

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]     return forward_call(*args, **kwargs)

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 735, in forward

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]     hidden_states = self.model(

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]                     ^^^^^^^^^^^

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 390, in __call__

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]     return self.forward(*args, **kwargs)

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]   File "/vllm-workspace/vllm/vllm/model_executor/models/qwen3_moe.py", line 456, in forward

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]     hidden_states, residual = layer(positions, hidden_states, residual)

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]     return self._call_impl(*args, **kwargs)

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]     return forward_call(*args, **kwargs)

[0;36m(Worker_TP0 pid=273)[0;0m ERROR 02-03 07:20:41 [multiproc_executor.py:822]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
后面是类似的报错，中间夹带AttributeError: '_OpNamespace' '_C_ascend' object has no attribute 'moe_gating_top_k'

请问我应该如何解决这个BUG

### 🐛 Describe the bug

1
