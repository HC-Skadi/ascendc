# Issue #5399: [Bug]: RuntimeError: bIndex is out of range: 3068 in vllm-ascend_main when deploying DeepSeek-V3.2 under high concurrency

## 基本信息

- **编号**: #5399
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5399
- **创建时间**: 2025-12-26T09:05:51Z
- **关闭时间**: 2026-01-26T02:12:19Z
- **更新时间**: 2026-01-26T02:12:20Z
- **提交者**: @tan-lei
- **评论数**: 10

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Version: vllm-ascend_main branch
Model: DeepSeek-V3.2

+------------------------------------------------------------------------------------------------+
| npu-smi 25.2.0                   Version: 25.2.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2               | OK            | 87.6        32                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3411 / 65536         |
+===========================+===============+====================================================+
| 1     910B2               | OK            | 87.5        32                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3411 / 65536         |
+===========================+===============+====================================================+
| 2     910B2               | OK            | 92.3        32                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3411 / 65536         |
+===========================+===============+====================================================+
| 3     910B2               | OK            | 92.3        32                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3411 / 65536         |
+===========================+===============+====================================================+
| 4     910B2               | OK            | 87.2        32                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3413 / 65536         |
+===========================+===============+====================================================+
| 5     910B2               | OK            | 93.4        32                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3413 / 65536         |
+===========================+===============+====================================================+
| 6     910B2               | OK            | 91.2        31                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3412 / 65536         |
+===========================+===============+====================================================+
| 7     910B2               | OK            | 92.0        32                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3412 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
+===========================+===============+====================================================+
```

</details>


### 🐛 Describe the bug

When deploying the DeepSeek-V3.2 model using the vllm-ascend_main branch in a high concurrency scenario (10 concurrent inference requests), the engine throws a RuntimeError with the message bIndex is out of range: 3068.

**script**
```
#!/bin/sh

nic_name="eno0"
local_ip=$(hostname -I | awk '{print $1}')
node0_ip=$MASTER_ADDR

export MODEL_NAME=DeepSeek-V3.2

export MODEL_DIR=/mnt/nvme0n1/model/DeepSeek-V3.2-w8a8-mtp-QuaRot

export VLLM_IMG=vllm-ascend_main.sif

export HCCL_OP_EXPANSION_MODE="AIV"
export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export HCCL_BUFFSIZE=200
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export VLLM_ASCEND_ENABLE_MLAPO=1
export HCCL_INTRA_PCIE_ENABLE=1
export HCCL_INTRA_ROCE_ENABLE=0


apptainer instance start --no-home --writable-tmpfs \
        -B /usr/local/sbin:/usr/local/sbin \
        -B /usr/local/Ascend/driver:/usr/local/Ascend/driver \
        -B $MODEL_DIR:/model \
        $VLLM_IMG app-instance

if [ $SLURM_NODEID == 0 ]; then
  apptainer exec instance://app-instance \
        vllm serve \
        /model \
        --served-model-name "$MODEL_NAME" \
        --host 0.0.0.0 \
        --port 11025 \
        --data-parallel-size 4 \
        --data-parallel-size-local 2 \
        --data-parallel-address $node0_ip \
        --data-parallel-rpc-port 13389 \
        --tensor-parallel-size 4 \
        --quantization ascend \
        --seed 1024 \
        --enable-expert-parallel \
        --max-num-seqs 20 \
        --max-model-len 16384 \
        --max-num-batched-tokens 4096 \
        --trust-remote-code \
        --no-enable-prefix-caching \
        --gpu-memory-utilization 0.94
fi

if [ $SLURM_NODEID == 1 ]; then
  apptainer exec instance://app-instance \
        vllm serve \
        /model \
        --served-model-name "$MODEL_NAME" \
        --host 0.0.0.0 \
        --port 11025 \
        --headless \
        --data-parallel-size 4 \
        --data-parallel-size-local 2 \
        --data-parallel-start-rank 2 \
        --data-parallel-address $node0_ip \
        --data-parallel-rpc-port 13389 \
        --tensor-parallel-size 4 \
        --quantization ascend \
        --seed 1024 \
        --enable-expert-parallel \
        --max-num-seqs 20 \
        --max-model-len 16384 \
        --max-num-batched-tokens 4096 \
        --trust-remote-code \
        --no-enable-prefix-caching \
        --gpu-memory-utilization 0.94
fi
```


**log**
```
 (Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824] WorkerProc hit an exception.
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824] Traceback (most recent call last):
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     output = func(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/worker/worker_base.py", line 369, in execute_model
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 308, in execute_model
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     output = self.model_runner.execute_model(scheduler_output,
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1427, in execute_model
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     hidden_states = self._generate_process_reqs_hidden_states(
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1147, in _generate_process_reqs_hidden_states
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     hidden_states = self.model(
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]                     ^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self._call_impl(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return forward_call(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/model_executor/models/deepseek_v2.py", line 1463, in forward
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     hidden_states = self.model(
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]                     ^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 439, in __call__
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return TorchCompileWithNoGuardsWrapper.__call__(self, *args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/compilation/wrapper.py", line 223, in __call__
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self._call_with_optional_nvtx_range(
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/compilation/wrapper.py", line 109, in _call_with_optional_nvtx_range
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return callable_fn(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/worker/patch_deepseek.py", line 10, in forward
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     def forward(
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 929, in _fn
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return fn(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/compilation/caching.py", line 54, in __call__
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self.optimized_call(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 848, in call_wrapped
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self._wrapped_call(self, *args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 424, in __call__
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     raise e
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 411, in __call__
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self._call_impl(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return forward_call(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "<eval_with_key>.124", line 327, in forward
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     submod_1 = self.submod_1(getitem, s72, getitem_1);  getitem = submod_1 = None
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 848, in call_wrapped
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self._wrapped_call(self, *args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 424, in __call__
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     raise e
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 411, in __call__
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self._call_impl(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return forward_call(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "<eval_with_key>.2", line 5, in forward
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     mla_forward = torch.ops.vllm.mla_forward(x, False, output_1, 'model.layers.0.self_attn');  x = output_1 = mla_forward = None
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1243, in __call__
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self._op(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/mla.py", line 166, in mla_forward
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     self.mla_attn.impl.forward(self.mla_attn.layer_name, hidden_states,
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/sfa_v1.py", line 774, in forward
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     hidden_states, ql_nope, q_pe, q_c = self._sfa_preprocess_decode(
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/sfa_v1.py", line 708, in _sfa_preprocess_decode
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     torch.ops._C_ascend.mla_preprocess(
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1243, in __call__
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self._op(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824] RuntimeError: bIndex is out of range: 3068
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824] Traceback (most recent call last):
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     output = func(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/worker/worker_base.py", line 369, in execute_model
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self.worker.execute_model(scheduler_output, *args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 308, in execute_model
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     output = self.model_runner.execute_model(scheduler_output,
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1427, in execute_model
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     hidden_states = self._generate_process_reqs_hidden_states(
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 1147, in _generate_process_reqs_hidden_states
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     hidden_states = self.model(
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]                     ^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self._call_impl(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return forward_call(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/model_executor/models/deepseek_v2.py", line 1463, in forward
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     hidden_states = self.model(
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]                     ^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 439, in __call__
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return TorchCompileWithNoGuardsWrapper.__call__(self, *args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/compilation/wrapper.py", line 223, in __call__
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self._call_with_optional_nvtx_range(
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/compilation/wrapper.py", line 109, in _call_with_optional_nvtx_range
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return callable_fn(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/worker/patch_deepseek.py", line 10, in forward
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     def forward(
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 929, in _fn
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return fn(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/compilation/caching.py", line 54, in __call__
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self.optimized_call(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 848, in call_wrapped
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self._wrapped_call(self, *args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 424, in __call__
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     raise e
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 411, in __call__
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self._call_impl(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return forward_call(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "<eval_with_key>.124", line 327, in forward
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     submod_1 = self.submod_1(getitem, s72, getitem_1);  getitem = submod_1 = None
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 848, in call_wrapped
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self._wrapped_call(self, *args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 424, in __call__
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     raise e
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/fx/graph_module.py", line 411, in __call__
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self._call_impl(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return forward_call(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "<eval_with_key>.2", line 5, in forward
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     mla_forward = torch.ops.vllm.mla_forward(x, False, output_1, 'model.layers.0.self_attn');  x = output_1 = mla_forward = None
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1243, in __call__
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self._op(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/mla.py", line 166, in mla_forward
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     self.mla_attn.impl.forward(self.mla_attn.layer_name, hidden_states,
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/sfa_v1.py", line 774, in forward
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     hidden_states, ql_nope, q_pe, q_c = self._sfa_preprocess_decode(
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/sfa_v1.py", line 708, in _sfa_preprocess_decode
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     torch.ops._C_ascend.mla_preprocess(
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1243, in __call__
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]     return self._op(*args, **kwargs)
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824] RuntimeError: bIndex is out of range: 3068
(Worker_DP3_TP1_EP13 pid=72) ERROR 12-26 16:50:20 [multiproc_executor.py:824] 
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868] EngineCore encountered a fatal error.
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868] Traceback (most recent call last):
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 859, in run_engine_core
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]     engine_core.run_busy_loop()
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 1248, in run_busy_loop
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]     executed = self._process_engine_step()
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 919, in _process_engine_step
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]     outputs, model_executed = self.step_fn()
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]                               ^^^^^^^^^^^^^^
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 351, in step
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]     model_output = future.result()
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]                    ^^^^^^^^^^^^^^^
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 80, in result
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]     return super().result()
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]            ^^^^^^^^^^^^^^^^
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]   File "/usr/local/python3.11.13/lib/python3.11/concurrent/futures/_base.py", line 449, in result
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]     return self.__get_result()
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]            ^^^^^^^^^^^^^^^^^^^
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]   File "/usr/local/python3.11.13/lib/python3.11/concurrent/futures/_base.py", line 401, in __get_result
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]     raise self._exception
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 84, in wait_for_response
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]     response = self.aggregate(get_response())
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]                               ^^^^^^^^^^^^^^
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 342, in get_response
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868]     raise RuntimeError(
(EngineCore_DP3 pid=40) ERROR 12-26 16:50:20 [core.py:868] RuntimeError: Worker failed with error 'bIndex is out of range: 3068', please check the stack trace above for the root cause
```
