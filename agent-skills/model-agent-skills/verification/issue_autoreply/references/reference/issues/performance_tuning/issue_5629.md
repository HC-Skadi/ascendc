# Issue #5629: [Usage]: 双八卡910B节点部署DeepSeek-V3.1-Terminus-w8a8-mtp-QuaRot报错

## 基本信息

- **编号**: #5629
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5629
- **创建时间**: 2026-01-06T03:32:44Z
- **关闭时间**: 2026-01-06T08:54:58Z
- **更新时间**: 2026-01-06T08:54:58Z
- **提交者**: @StormMapleleaf
- **评论数**: 2

## 标签

无

## 问题描述

### Your current environment

```
export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export HCCL_BUFFSIZE=200
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export VLLM_ASCEND_ENABLE_MLAPO=1
export VLLM_ASCEND_BALANCE_SCHEDULING=1
export HCCL_INTRA_PCIE_ENABLE=1
export HCCL_INTRA_ROCE_ENABLE=0

vllm serve /root/.cache/DeepSeek-V3.1-Terminus-w8a8-mtp-QuaRot \
--host 0.0.0.0 \
--port 8004 \
--data-parallel-size 4 \
--data-parallel-size-local 2 \
--data-parallel-address $node0_ip \
--data-parallel-rpc-port 13389 \
--tensor-parallel-size 4 \
--quantization ascend \
--seed 1024 \
--served-model-name DeepSeek-V3.1-Terminus \
--enable-expert-parallel \
--async-scheduling \
--max-num-seqs 64 \
--max-model-len 16384 \
--max-num-batched-tokens 16384 \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.92 \
--speculative-config '{"num_speculative_tokens": 3, "method": "mtp"}' \
--compilation-config '{"cudagraph_capture_sizes":[4,16,32,48,64], "cudagraph_mode": "FULL_DECODE_ONLY"}'
```

```
..(Worker_DP0_TP1_EP1 pid=37564) INFO 01-06 03:22:51 [model_runner_v1.py:2243] Loading model weights took 45.6571 GB
(Worker_DP0_TP3_EP3 pid=37642) INFO 01-06 03:22:53 [model_runner_v1.py:2243] Loading model weights took 45.6571 GB
...(Worker_DP0_TP0_EP0 pid=37552) INFO 01-06 03:22:55 [model_runner_v1.py:2243] Loading model weights took 45.6571 GB
(Worker_DP1_TP1_EP5 pid=37567) INFO 01-06 03:22:56 [model_runner_v1.py:2243] Loading model weights took 45.6571 GB
(Worker_DP1_TP0_EP4 pid=37553) INFO 01-06 03:22:57 [model_runner_v1.py:2243] Loading model weights took 45.6571 GB
(Worker_DP1_TP2_EP6 pid=37605) INFO 01-06 03:22:57 [model_runner_v1.py:2243] Loading model weights took 45.6571 GB
(Worker_DP1_TP3_EP7 pid=37645) INFO 01-06 03:22:57 [model_runner_v1.py:2243] Loading model weights took 45.6571 GB
(Worker_DP0_TP2_EP2 pid=37602) INFO 01-06 03:22:58 [model_runner_v1.py:2243] Loading model weights took 45.6571 GB
(Worker_DP1_TP3_EP7 pid=37645) [rank7]:E0106 03:23:01.677000 37645 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0] failed while attempting to run meta for npu.npu_quant_matmul.default
(Worker_DP1_TP3_EP7 pid=37645) [rank7]:E0106 03:23:01.677000 37645 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0] Traceback (most recent call last):
(Worker_DP1_TP3_EP7 pid=37645) [rank7]:E0106 03:23:01.677000 37645 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_subclasses/fake_tensor.py", line 2717, in _dispatch_impl
(Worker_DP1_TP3_EP7 pid=37645) [rank7]:E0106 03:23:01.677000 37645 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0]     r = func(*args, **kwargs)
(Worker_DP1_TP3_EP7 pid=37645) [rank7]:E0106 03:23:01.677000 37645 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0]         ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=37645) [rank7]:E0106 03:23:01.677000 37645 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 829, in __call__
(Worker_DP1_TP3_EP7 pid=37645) [rank7]:E0106 03:23:01.677000 37645 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0]     return self._op(*args, **kwargs)
(Worker_DP1_TP3_EP7 pid=37645) [rank7]:E0106 03:23:01.677000 37645 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=37645) [rank7]:E0106 03:23:01.677000 37645 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/op_plugin/meta/_meta_registrations.py", line 1934, in npu_quant_matmul_meta
(Worker_DP1_TP3_EP7 pid=37645) [rank7]:E0106 03:23:01.677000 37645 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0]     quant_matmul_scale_offset_out_check(scale, offset, pertoken_scale, output_dtype, is_a4w4)
(Worker_DP1_TP3_EP7 pid=37645) [rank7]:E0106 03:23:01.677000 37645 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/op_plugin/meta/_meta_registrations.py", line 1866, in quant_matmul_scale_offset_out_check
(Worker_DP1_TP3_EP7 pid=37645) [rank7]:E0106 03:23:01.677000 37645 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0]     torch._check(
(Worker_DP1_TP3_EP7 pid=37645) [rank7]:E0106 03:23:01.677000 37645 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/__init__.py", line 1684, in _check
(Worker_DP1_TP3_EP7 pid=37645) [rank7]:E0106 03:23:01.677000 37645 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0]     _check_with(RuntimeError, cond, message)
(Worker_DP1_TP3_EP7 pid=37645) [rank7]:E0106 03:23:01.677000 37645 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/__init__.py", line 1666, in _check_with
(Worker_DP1_TP3_EP7 pid=37645) [rank7]:E0106 03:23:01.677000 37645 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0]     raise error_type(message_evaluated)
(Worker_DP1_TP3_EP7 pid=37645) [rank7]:E0106 03:23:01.677000 37645 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0] RuntimeError: When output_dtype is float16 and pertoken_scale is not none, scale's dtype must be float32, but scale's dtype is torch.float16
(Worker_DP1_TP3_EP7 pid=37645) [rank7]:E0106 03:23:01.677000 37645 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0] [ERROR] 2026-01-06-03:23:01 (PID:37645, Device:3, RankID:7) ERR01002 OPS invalid type
(Worker_DP0_TP2_EP2 pid=37602) [rank2]:E0106 03:23:01.679000 37602 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0] failed while attempting to run meta for npu.npu_quant_matmul.default
(Worker_DP0_TP2_EP2 pid=37602) [rank2]:E0106 03:23:01.679000 37602 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0] Traceback (most recent call last):
(Worker_DP0_TP2_EP2 pid=37602) [rank2]:E0106 03:23:01.679000 37602 site-packages/torch/_subclasses/fake_tensor.py:2721] [0/0]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_subclasses/fake_tensor.py", line 2717, in _dispatch_impl

```
```
(Worker_DP1_TP3_EP7 pid=37645) ERROR 01-06 03:23:01 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_subclasses/fake_tensor.py", line 2717, in _dispatch_impl
(Worker_DP0_TP2_EP2 pid=37602) ERROR 01-06 03:23:01 [multiproc_executor.py:824]     return super().call_function(tx, args, kwargs)
(Worker_DP1_TP3_EP7 pid=37645) ERROR 01-06 03:23:01 [multiproc_executor.py:824]     r = func(*args, **kwargs)
(Worker_DP0_TP2_EP2 pid=37602) ERROR 01-06 03:23:01 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=37645) ERROR 01-06 03:23:01 [multiproc_executor.py:824]         ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP2_EP2 pid=37602) ERROR 01-06 03:23:01 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/variables/functions.py", line 293, in call_function
(Worker_DP1_TP3_EP7 pid=37645) ERROR 01-06 03:23:01 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 829, in __call__
(Worker_DP0_TP2_EP2 pid=37602) ERROR 01-06 03:23:01 [multiproc_executor.py:824]     return tx.inline_user_function_return(self, [*self.self_args(), *args], kwargs)
(Worker_DP1_TP3_EP7 pid=37645) ERROR 01-06 03:23:01 [multiproc_executor.py:824]     return self._op(*args, **kwargs)
(Worker_DP0_TP2_EP2 pid=37602) ERROR 01-06 03:23:01 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=37645) ERROR 01-06 03:23:01 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP0_TP2_EP2 pid=37602) ERROR 01-06 03:23:01 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/symbolic_convert.py", line 1210, in inline_user_function_return
(Worker_DP1_TP3_EP7 pid=37645) ERROR 01-06 03:23:01 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/op_plugin/meta/_meta_registrations.py", line 1934, in npu_quant_matmul_meta
(Worker_DP0_TP2_EP2 pid=37602) ERROR 01-06 03:23:01 [multiproc_executor.py:824]     return InliningInstructionTranslator.inline_call(self, fn, args, kwargs)
(Worker_DP1_TP3_EP7 pid=37645) ERROR 01-06 03:23:01 [multiproc_executor.py:824]     quant_matmul_scale_offset_out_check(scale, offset, pertoken_scale, output_dtype, is_a4w4)
(Worker_DP0_TP2_EP2 pid=37602) ERROR 01-06 03:23:01 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=37645) ERROR 01-06 03:23:01 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/op_plugin/meta/_meta_registrations.py", line 1866, in quant_matmul_scale_offset_out_check
(Worker_DP0_TP2_EP2 pid=37602) ERROR 01-06 03:23:01 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_dynamo/symbolic_convert.py", line 3698, in inline_call
(Worker_DP1_TP3_EP7 pid=37645) ERROR 01-06 03:23:01 [multiproc_executor.py:824]     torch._check(
(Worker_DP0_TP2_EP2 pid=37602) ERROR 01-06 03:23:01 [multiproc_executor.py:824]     return tracer.inline_call_()
(Worker_DP1_TP3_EP7 pid=37645) ERROR 01-06 03:23:01 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/__init__.py", line 1684, in _check
(Worker_DP0_TP2_EP2 pid=37602) ERROR 01-06 03:23:01 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=37645) ERROR 01-06 03:23:01 [multiproc_executor.py:824]     _check_with(RuntimeError, cond, message)
(Worker_DP0_TP2_EP2 pid=37602) ERROR 01-06 03:23:01 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/compilation/decorators.py", line 475, in patched_inline_call
(Worker_DP1_TP3_EP7 pid=37645) ERROR 01-06 03:23:01 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/__init__.py", line 1666, in _check_with
(Worker_DP0_TP2_EP2 pid=37602) ERROR 01-06 03:23:01 [multiproc_executor.py:824]     return inline_call(self_)
(Worker_DP1_TP3_EP7 pid=37645) ERROR 01-06 03:23:01 [multiproc_executor.py:824]     raise error_type(message_evaluated)
(Worker_DP0_TP2_EP2 pid=37602) ERROR 01-06 03:23:01 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP3_EP7 pid=37645) ERROR 01-06 03:23:01 [multiproc_executor.py:824] torch._dynamo.exc.TorchRuntimeError: Dynamo failed to run FX node with fake tensors: call_function npu.npu_quant_matmul(*(FakeTensor(..., device='npu:3', size=(s72, 7168), dtype=torch.int8), Parameter(FakeTensor(..., device='npu:3', size=(7168, 9216), dtype=torch.int8)), Parameter(FakeTensor(..., device='npu:3', size=(9216,), dtype=torch.float16))), **{'pertoken_scale': FakeTensor(..., device='npu:3', size=(s72,)), 'bias': None, 'output_dtype': torch.float16}): got RuntimeError("When output_dtype is float16 and pertoken_scale is not none, scale's dtype must be float32, but scale's dtype is torch.float16\n[ERROR] 2026-01-06-03:23:01 (PID:37645, Device:3, RankID:7) ERR01002 OPS invalid type")
```



### How would you like to use vllm on ascend

I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

