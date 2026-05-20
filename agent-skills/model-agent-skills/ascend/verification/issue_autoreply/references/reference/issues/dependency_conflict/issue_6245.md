# Issue #6245: [Bug]: A3单机混部 vLLM0.13.0RC2镜像 部署DSV3.2报错

## 基本信息

- **编号**: #6245
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6245
- **创建时间**: 2026-01-26T03:01:05Z
- **关闭时间**: 2026-01-29T02:55:15Z
- **更新时间**: 2026-01-29T02:56:27Z
- **提交者**: @qxh84189941
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
[root@localhost hundsun]# python collect_env.py
Collecting environment information...
PyTorch version: 2.8.0+cpu
Is debug build: False

OS: openEuler 24.03 (LTS-SP2) (aarch64)
GCC version: (GCC) 12.3.1 (openEuler 12.3.1-99.oe2403sp2)
Clang version: 17.0.6 ( 17.0.6-45.oe2403sp2)
CMake version: version 4.2.1
Libc version: glibc-2.38

Python version: 3.11.14 (main, Jan 21 2026, 07:05:42) [GCC 12.3.1 (openEuler 12.3.1-99.oe2403sp2)] (64-bit runtime)
Python platform: Linux-5.10.0-296.0.0.199.oe2203sp4.aarch64-aarch64-with-glibc2.38

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             640
On-line CPU(s) list:                0-639
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         -
BIOS Model name:                    Kunpeng 920 7280Z To be filled by O.E.M. CPU @ 2.9GHz
BIOS CPU family:                    280
Model:                              0
Thread(s) per core:                 2
Core(s) per socket:                 80
Socket(s):                          4
Stepping:                           0x0
Frequency boost:                    disabled
CPU(s) scaling MHz:                 100%
CPU max MHz:                        2900.0000
CPU min MHz:                        400.0000
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs sb dcpodp flagm2 frint svei8mm svef32mm svef64mm svebf16 i8mm bf16 dgh rng ecv
L1d cache:                          20 MiB (320 instances)
L1i cache:                          20 MiB (320 instances)
L2 cache:                           400 MiB (320 instances)
L3 cache:                           560 MiB (8 instances)
NUMA node(s):                       8
NUMA node0 CPU(s):                  0-79
NUMA node1 CPU(s):                  80-159
NUMA node2 CPU(s):                  160-239
NUMA node3 CPU(s):                  240-319
NUMA node4 CPU(s):                  320-399
NUMA node5 CPU(s):                  400-479
NUMA node6 CPU(s):                  480-559
NUMA node7 CPU(s):                  560-639
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec rstack overflow: Not affected
Vulnerability Spec store bypass:    Not affected
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0.post1
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.6
[conda] Could not collect
vLLM Version: 0.13.0
vLLM Ascend Version: 0.13.0rc2

ENV Variables:
ASCEND_TOOLKIT_LATEST_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_AGGREGATE_ENABLE=1
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
VLLM_NIXL_ABORT_REQUEST_TIMEOUT=300000
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/cann-8.5.0
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/cann-8.5.0/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/cann-8.5.0/lib64:/usr/local/Ascend/cann-8.5.0/lib64/plugin/opskernel:/usr/local/Ascend/cann-8.5.0/lib64/plugin/nnengine:/usr/local/Ascend/cann-8.5.0/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/cann-8.5.0/tools/aml/lib64:/usr/local/Ascend/cann-8.5.0/tools/aml/lib64/plugin:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/cann-8.5.0
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/cann-8.5.0
ASCEND_TRANSPORT_PRINT=1
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ASCEND_A3_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 25.3.rc1.2               Version: 25.3.rc1.2                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 166.4       43                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          3158 / 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           43                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          2882 / 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 162.6       43                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          3151 / 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           41                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          2879 / 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 177.6       47                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3154 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           48                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          2881 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 170.5       45                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3140 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           47                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          2892 / 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 163.0       41                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          3141 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           40                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          2890 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 161.1       44                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          3153 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           42                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          2879 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 156.4       45                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          3153 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           46                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          2880 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 174.4       47                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          3139 / 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           47                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          2890 / 65536         |
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

CANN:
package_name=Ascend-cann-toolkit
version=8.5.0
innerversion=V100R001C25SPC001B232
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/cann-8.5.0
[root@localhost hundsun]#

```

</details>


### 🐛 Describe the bug

```sh
export HCCL_OP_EXPANSION_MODE="AIV"
export LD_PRELOAD=/usr/lib64/libjemalloc.so.2:$LD_PRELOAD
source /usr/local/Ascend/ascend-toolkit/set_env.sh
source /usr/local/Ascend/nnal/atb/set_env.sh



export OMP_PROC_BIND=false
export OMP_NUM_THREADS=10
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export VLLM_USE_V1=1
export HCCL_BUFFSIZE=1024

export ASCEND_AGGREGATE_ENABLE=1
export ASCEND_TRANSPORT_PRINT=1
export ACL_OP_INIT_MODE=1
export ASCEND_A3_ENABLE=1
export VLLM_NIXL_ABORT_REQUEST_TIMEOUT=300000
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
export VLLM_ASCEND_ENABLE_MLAPO=1
export VLLM_ASCEND_ENABLE_FLASHCOMM1=0

vllm serve /home/models/DeepSeek-V3.2-W8A8 \
    --host 0.0.0.0 \
    --port 8000 \
    -dp 2 \
    -tp 8 \
    --seed 1024 \
    --quantization ascend \
    --enable-expert-parallel \
    --trust-remote-code \
    --no-enable-prefix-caching \
    --gpu-memory-utilization 0.92 \
    --served-model-name dsv3 \
    --speculative-config '{"num_speculative_tokens": 2, "method":"deepseek_mtp"}' \
    --compilation-config '{"cudagraph_mode":"FULL_DECODE_ONLY", "cudagraph_capture_sizes":[3,6,12,18,24,30,36,42,48]}' \
    --max-model-len 40000 \
    --max-num-batched-tokens 9000 \
    --max-num-seqs 16 \
    --tokenizer-mode deepseek_v32 \
    --reasoning-parser deepseek_v3 \
    2>&1 | tee pd_p.log
```

报错信息如下：
```
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/compilation/piecewise_backend.py", line 178, in __call__
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     return range_entry.runnable(*args)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/_inductor/compile_fx.py", line 2474, in wrapper
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     return pytree.tree_unflatten(compiled_fn(*args, **kwargs), spec)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/_dynamo/eval_frame.py", line 929, in _fn
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     return fn(*args, **kwargs)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/_functorch/aot_autograd.py", line 1241, in forward
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     return compiled_fn(full_args)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py", line 384, in runtime_wrapper
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     all_outs = call_func_at_runtime_with_args(
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/utils.py", line 126, in call_func_at_runtime_with_args
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     out = normalize_as_list(f(args))
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]                             ^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py", line 750, in inner_fn
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     outs = compiled_fn(args)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/runtime_wrappers.py", line 556, in wrapper
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     return compiled_fn(runtime_args)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/_functorch/_aot_autograd/utils.py", line 100, in g
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     return f(*args)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]            ^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/fx/graph_module.py", line 848, in call_wrapped
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     return self._wrapped_call(self, *args, **kwargs)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/fx/graph_module.py", line 424, in __call__
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     raise e
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/fx/graph_module.py", line 411, in __call__
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     return super(self.cls, obj).__call__(*args, **kwargs)  # type: ignore[misc]
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     return self._call_impl(*args, **kwargs)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1784, in _call_impl
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     return forward_call(*args, **kwargs)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "<eval_with_key>.13 from /usr/local/python3.11.14/lib/python3.11/site-packages/torch/fx/experimental/proxy_tensor.py:1301 in wrapped", line 21, in forward
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     auto_functionalized_v2 = torch.ops.higher_order.auto_functionalized_v2(torch.ops.vllm.mla_forward.default, hidden_states = add_44, need_gather_q_kv = False, layer_name = 'model.layers.0.self_attn', _output_base_index = 0, _output_alias = True, _all_bases = [empty]);  add_44 = empty = None
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/_higher_order_ops/auto_functionalize.py", line 401, in __call__
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     return super().__call__(_mutable_op, **kwargs)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/_ops.py", line 524, in __call__
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     return wrapper()
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]            ^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/_ops.py", line 520, in wrapper
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     return self.dispatch(
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/_ops.py", line 380, in dispatch
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     return kernel(*args, **kwargs)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/_higher_order_ops/auto_functionalize.py", line 856, in auto_functionalized_v2_dense
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     out = call_op(
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]           ^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/_higher_order_ops/utils.py", line 1017, in call_op
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     return op(*args, **kwargs)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/torch/_ops.py", line 829, in __call__
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     return self._op(*args, **kwargs)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/mla.py", line 164, in mla_forward
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     self.mla_attn.impl.forward(self.mla_attn.layer_name, hidden_states,
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/sfa_v1.py", line 771, in forward
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     q, k = self.indexer_select_pre_process(
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/attention/sfa_v1.py", line 940, in indexer_select_pre_process
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     q, k = rope_forward_triton(q,
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/ops/triton/rope.py", line 187, in rope_forward_triton
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     _triton_rope[(n_row, )](
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/triton/runtime/jit.py", line 353, in <lambda>
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     return lambda *args, **kwargs: self.run(grid=grid, warmup=False, *args, **kwargs)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/triton/runtime/jit.py", line 696, in run
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     kernel._init_handles()
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/triton/compiler/compiler.py", line 424, in _init_handles
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     self.run = driver.active.launcher_cls(self.src, self.metadata)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/triton/backends/ascend/driver.py", line 127, in __init__
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     so_launcher_path = make_npu_launcher_stub(header_src, wrapper_src, metadata.debug)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/triton/backends/ascend/driver.py", line 279, in make_npu_launcher_stub
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     so_path = _build_npu_ext(name, header_path, src_path, kernel_launcher=kernel_launcher_type, precompile=True)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/site-packages/triton/backends/ascend/utils.py", line 413, in _build_npu_ext
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     raise RuntimeError(f"Failed to compile {src_path}, error: {result.stderr}")
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] RuntimeError: Failed to compile /tmp/tmphxcyl__n/launcher_cxx11abi1.cxx, error: In file included from <built-in>:1:
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] In file included from /root/.triton/cache/dp_5hWqtjuyyrcwp8NOg07sKOjLwY_A0fQPUzPpDpl8/precompiled.h:38:
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpCommand.h:5:
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpParamMaker.h:7:
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/interface/AclOpCompileInterface.h:146:55: error: use of undeclared identifier 'aclOpExecutor'; did you mean 'aclopExecute'?
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   146 | ACL_FUNC_VISIBILITY  aclError AclDestroyAclOpExecutor(aclOpExecutor *executor);
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]       |                                                       ^~~~~~~~~~~~~
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]       |                                                       aclopExecute
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] /usr/local/Ascend/cann-8.5.0/include/acl/acl_op.h:267:30: note: 'aclopExecute' declared here
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   267 | ACL_FUNC_VISIBILITY aclError aclopExecute(const char *opType,
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]       |                              ^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] In file included from <built-in>:1:
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] In file included from /root/.triton/cache/dp_5hWqtjuyyrcwp8NOg07sKOjLwY_A0fQPUzPpDpl8/precompiled.h:38:
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpCommand.h:5:
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpParamMaker.h:7:
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/interface/AclOpCompileInterface.h:146:70: error: use of undeclared identifier 'executor'
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   146 | ACL_FUNC_VISIBILITY  aclError AclDestroyAclOpExecutor(aclOpExecutor *executor);
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]       |                                                                      ^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] 2 errors generated.
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] During handling of the above exception, another exception occurred:
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] Traceback (most recent call last):
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     output = func(*args, **kwargs)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 406, in compile_or_warm_up_model
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     self.model_runner.capture_model()
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3049, in capture_model
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     with _torch_cuda_wrapper(), _replace_gpu_model_runner_function_wrapper(
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/usr/local/python3.11.14/lib/python3.11/contextlib.py", line 158, in __exit__
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     self.gen.throw(typ, value, traceback)
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3114, in _torch_cuda_wrapper
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]     raise RuntimeError(f"NPUModelRunner init failed, error is {e}")
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] RuntimeError: NPUModelRunner init failed, error is Failed to compile /tmp/tmphxcyl__n/launcher_cxx11abi1.cxx, error: In file included from <built-in>:1:
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] In file included from /root/.triton/cache/dp_5hWqtjuyyrcwp8NOg07sKOjLwY_A0fQPUzPpDpl8/precompiled.h:38:
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpCommand.h:5:
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpParamMaker.h:7:
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/interface/AclOpCompileInterface.h:146:55: error: use of undeclared identifier 'aclOpExecutor'; did you mean 'aclopExecute'?
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   146 | ACL_FUNC_VISIBILITY  aclError AclDestroyAclOpExecutor(aclOpExecutor *executor);
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]       |                                                       ^~~~~~~~~~~~~
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]       |                                                       aclopExecute
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] /usr/local/Ascend/cann-8.5.0/include/acl/acl_op.h:267:30: note: 'aclopExecute' declared here
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   267 | ACL_FUNC_VISIBILITY aclError aclopExecute(const char *opType,
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]       |                              ^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] In file included from <built-in>:1:
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] In file included from /root/.triton/cache/dp_5hWqtjuyyrcwp8NOg07sKOjLwY_A0fQPUzPpDpl8/precompiled.h:38:
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpCommand.h:5:
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpParamMaker.h:7:
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/interface/AclOpCompileInterface.h:146:70: error: use of undeclared identifier 'executor'
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]   146 | ACL_FUNC_VISIBILITY  aclError AclDestroyAclOpExecutor(aclOpExecutor *executor);
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]       |                                                                      ^
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824] 2 errors generated.
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]
(Worker_DP1_TP0_EP8 pid=86026) ERROR 01-26 10:28:18 [multiproc_executor.py:824]
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68] EngineCore failed to start.
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68] Traceback (most recent call last):
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_core.py", line 55, in run_engine_core
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 1159, in __init__
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]     super().__init__(
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 637, in __init__
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]     super().__init__(
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 109, in __init__
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]     num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches(
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 256, in _initialize_kv_caches
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]     self.model_executor.initialize_from_config(kv_cache_configs)
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 116, in initialize_from_config
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]     self.collective_rpc("compile_or_warm_up_model")
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 359, in collective_rpc
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]     return aggregate(get_response())
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]                      ^^^^^^^^^^^^^^
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 342, in get_response
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]     raise RuntimeError(
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68] RuntimeError: Worker failed with error 'NPUModelRunner init failed, error is Failed to compile /tmp/tmphxcyl__n/launcher_cxx11abi1.cxx, error: In file included from <built-in>:1:
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68] In file included from /root/.triton/cache/dp_5hWqtjuyyrcwp8NOg07sKOjLwY_A0fQPUzPpDpl8/precompiled.h:38:
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68] In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpCommand.h:5:
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68] In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpParamMaker.h:7:
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68] /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/interface/AclOpCompileInterface.h:146:55: error: use of undeclared identifier 'aclOpExecutor'; did you mean 'aclopExecute'?
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]   146 | ACL_FUNC_VISIBILITY  aclError AclDestroyAclOpExecutor(aclOpExecutor *executor);
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]       |                                                       ^~~~~~~~~~~~~
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]       |                                                       aclopExecute
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68] /usr/local/Ascend/cann-8.5.0/include/acl/acl_op.h:267:30: note: 'aclopExecute' declared here
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]   267 | ACL_FUNC_VISIBILITY aclError aclopExecute(const char *opType,
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]       |                              ^
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68] In file included from <built-in>:1:
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68] In file included from /root/.triton/cache/dp_5hWqtjuyyrcwp8NOg07sKOjLwY_A0fQPUzPpDpl8/precompiled.h:38:
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68] In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpCommand.h:5:
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68] In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpParamMaker.h:7:
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68] /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/interface/AclOpCompileInterface.h:146:70: error: use of undeclared identifier 'executor'
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]   146 | ACL_FUNC_VISIBILITY  aclError AclDestroyAclOpExecutor(aclOpExecutor *executor);
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68]       |                                                                      ^
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68] 2 errors generated.
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:18 [patch_core.py:68] ', please check the stack trace above for the root cause
(EngineCore_DP0 pid=85932) ERROR 01-26 10:28:26 [multiproc_executor.py:231] Worker proc VllmWorker-0 died unexpectedly, shutting down executor.
(EngineCore_DP0 pid=85932) Process EngineCore_DP0:
(EngineCore_DP0 pid=85932) Traceback (most recent call last):
(EngineCore_DP0 pid=85932)   File "/usr/local/python3.11.14/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=85932)     self.run()
(EngineCore_DP0 pid=85932)   File "/usr/local/python3.11.14/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=85932)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=85932)   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_core.py", line 72, in run_engine_core
(EngineCore_DP0 pid=85932)     raise e
(EngineCore_DP0 pid=85932)   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_core.py", line 55, in run_engine_core
(EngineCore_DP0 pid=85932)     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=85932)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=85932)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 1159, in __init__
(EngineCore_DP0 pid=85932)     super().__init__(
(EngineCore_DP0 pid=85932)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 637, in __init__
(EngineCore_DP0 pid=85932)     super().__init__(
(EngineCore_DP0 pid=85932)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 109, in __init__
(EngineCore_DP0 pid=85932)     num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches(
(EngineCore_DP0 pid=85932)                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=85932)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 256, in _initialize_kv_caches
(EngineCore_DP0 pid=85932)     self.model_executor.initialize_from_config(kv_cache_configs)
(EngineCore_DP0 pid=85932)   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 116, in initialize_from_config
(EngineCore_DP0 pid=85932)     self.collective_rpc("compile_or_warm_up_model")
(EngineCore_DP0 pid=85932)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 359, in collective_rpc
(EngineCore_DP0 pid=85932)     return aggregate(get_response())
(EngineCore_DP0 pid=85932)                      ^^^^^^^^^^^^^^
(EngineCore_DP0 pid=85932)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 342, in get_response
(EngineCore_DP0 pid=85932)     raise RuntimeError(
(EngineCore_DP0 pid=85932) RuntimeError: Worker failed with error 'NPUModelRunner init failed, error is Failed to compile /tmp/tmp92w2nbtm/launcher_cxx11abi1.cxx, error: In file included from <built-in>:1:
(EngineCore_DP0 pid=85932) In file included from /root/.triton/cache/dp_5hWqtjuyyrcwp8NOg07sKOjLwY_A0fQPUzPpDpl8/precompiled.h:38:
(EngineCore_DP0 pid=85932) In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpCommand.h:5:
(EngineCore_DP0 pid=85932) In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpParamMaker.h:7:
(EngineCore_DP0 pid=85932) /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/interface/AclOpCompileInterface.h:146:55: error: use of undeclared identifier 'aclOpExecutor'; did you mean 'aclopExecute'?
(EngineCore_DP0 pid=85932)   146 | ACL_FUNC_VISIBILITY  aclError AclDestroyAclOpExecutor(aclOpExecutor *executor);
(EngineCore_DP0 pid=85932)       |                                                       ^~~~~~~~~~~~~
(EngineCore_DP0 pid=85932)       |                                                       aclopExecute
(EngineCore_DP0 pid=85932) /usr/local/Ascend/cann-8.5.0/include/acl/acl_op.h:267:30: note: 'aclopExecute' declared here
(EngineCore_DP0 pid=85932)   267 | ACL_FUNC_VISIBILITY aclError aclopExecute(const char *opType,
(EngineCore_DP0 pid=85932)       |                              ^
(EngineCore_DP0 pid=85932) In file included from <built-in>:1:
(EngineCore_DP0 pid=85932) In file included from /root/.triton/cache/dp_5hWqtjuyyrcwp8NOg07sKOjLwY_A0fQPUzPpDpl8/precompiled.h:38:
(EngineCore_DP0 pid=85932) In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpCommand.h:5:
(EngineCore_DP0 pid=85932) In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpParamMaker.h:7:
(EngineCore_DP0 pid=85932) /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/interface/AclOpCompileInterface.h:146:70: error: use of undeclared identifier 'executor'
(EngineCore_DP0 pid=85932)   146 | ACL_FUNC_VISIBILITY  aclError AclDestroyAclOpExecutor(aclOpExecutor *executor);
(EngineCore_DP0 pid=85932)       |                                                                      ^
(EngineCore_DP0 pid=85932) 2 errors generated.
(EngineCore_DP0 pid=85932) ', please check the stack trace above for the root cause
(EngineCore_DP1 pid=85985) ERROR 01-26 10:28:27 [multiproc_executor.py:231] Worker proc VllmWorker-0 died unexpectedly, shutting down executor.
(EngineCore_DP1 pid=85985) Process EngineCore_DP1:
(EngineCore_DP1 pid=85985) Traceback (most recent call last):
(EngineCore_DP1 pid=85985)   File "/usr/local/python3.11.14/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP1 pid=85985)     self.run()
(EngineCore_DP1 pid=85985)   File "/usr/local/python3.11.14/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_DP1 pid=85985)     self._target(*self._args, **self._kwargs)
(EngineCore_DP1 pid=85985)   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_core.py", line 72, in run_engine_core
(EngineCore_DP1 pid=85985)     raise e
(EngineCore_DP1 pid=85985)   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_core.py", line 55, in run_engine_core
(EngineCore_DP1 pid=85985)     engine_core = DPEngineCoreProc(*args, **kwargs)
(EngineCore_DP1 pid=85985)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP1 pid=85985)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 1159, in __init__
(EngineCore_DP1 pid=85985)     super().__init__(
(EngineCore_DP1 pid=85985)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 637, in __init__
(EngineCore_DP1 pid=85985)     super().__init__(
(EngineCore_DP1 pid=85985)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 109, in __init__
(EngineCore_DP1 pid=85985)     num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches(
(EngineCore_DP1 pid=85985)                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP1 pid=85985)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 256, in _initialize_kv_caches
(EngineCore_DP1 pid=85985)     self.model_executor.initialize_from_config(kv_cache_configs)
(EngineCore_DP1 pid=85985)   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 116, in initialize_from_config
(EngineCore_DP1 pid=85985)     self.collective_rpc("compile_or_warm_up_model")
(EngineCore_DP1 pid=85985)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 359, in collective_rpc
(EngineCore_DP1 pid=85985)     return aggregate(get_response())
(EngineCore_DP1 pid=85985)                      ^^^^^^^^^^^^^^
(EngineCore_DP1 pid=85985)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 342, in get_response
(EngineCore_DP1 pid=85985)     raise RuntimeError(
(EngineCore_DP1 pid=85985) RuntimeError: Worker failed with error 'NPUModelRunner init failed, error is Failed to compile /tmp/tmphxcyl__n/launcher_cxx11abi1.cxx, error: In file included from <built-in>:1:
(EngineCore_DP1 pid=85985) In file included from /root/.triton/cache/dp_5hWqtjuyyrcwp8NOg07sKOjLwY_A0fQPUzPpDpl8/precompiled.h:38:
(EngineCore_DP1 pid=85985) In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpCommand.h:5:
(EngineCore_DP1 pid=85985) In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpParamMaker.h:7:
(EngineCore_DP1 pid=85985) /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/interface/AclOpCompileInterface.h:146:55: error: use of undeclared identifier 'aclOpExecutor'; did you mean 'aclopExecute'?
(EngineCore_DP1 pid=85985)   146 | ACL_FUNC_VISIBILITY  aclError AclDestroyAclOpExecutor(aclOpExecutor *executor);
(EngineCore_DP1 pid=85985)       |                                                       ^~~~~~~~~~~~~
(EngineCore_DP1 pid=85985)       |                                                       aclopExecute
(EngineCore_DP1 pid=85985) /usr/local/Ascend/cann-8.5.0/include/acl/acl_op.h:267:30: note: 'aclopExecute' declared here
(EngineCore_DP1 pid=85985)   267 | ACL_FUNC_VISIBILITY aclError aclopExecute(const char *opType,
(EngineCore_DP1 pid=85985)       |                              ^
(EngineCore_DP1 pid=85985) In file included from <built-in>:1:
(EngineCore_DP1 pid=85985) In file included from /root/.triton/cache/dp_5hWqtjuyyrcwp8NOg07sKOjLwY_A0fQPUzPpDpl8/precompiled.h:38:
(EngineCore_DP1 pid=85985) In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpCommand.h:5:
(EngineCore_DP1 pid=85985) In file included from /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/OpParamMaker.h:7:
(EngineCore_DP1 pid=85985) /usr/local/python3.11.14/lib/python3.11/site-packages/torch_npu/include/torch_npu/csrc/framework/interface/AclOpCompileInterface.h:146:70: error: use of undeclared identifier 'executor'
(EngineCore_DP1 pid=85985)   146 | ACL_FUNC_VISIBILITY  aclError AclDestroyAclOpExecutor(aclOpExecutor *executor);
(EngineCore_DP1 pid=85985)       |                                                                      ^
(EngineCore_DP1 pid=85985) 2 errors generated.
(EngineCore_DP1 pid=85985) ', please check the stack trace above for the root cause
(APIServer pid=85820) Traceback (most recent call last):
(APIServer pid=85820)   File "/usr/local/python3.11.14/bin/vllm", line 7, in <module>
(APIServer pid=85820)     sys.exit(main())
(APIServer pid=85820)              ^^^^^^
(APIServer pid=85820)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 73, in main
(APIServer pid=85820)     args.dispatch_function(args)
(APIServer pid=85820)   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 60, in cmd
(APIServer pid=85820)     uvloop.run(run_server(args))
(APIServer pid=85820)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/uvloop/__init__.py", line 92, in run
(APIServer pid=85820)     return runner.run(wrapper())
(APIServer pid=85820)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=85820)   File "/usr/local/python3.11.14/lib/python3.11/asyncio/runners.py", line 118, in run
(APIServer pid=85820)     return self._loop.run_until_complete(task)
(APIServer pid=85820)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=85820)   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
(APIServer pid=85820)   File "/usr/local/python3.11.14/lib/python3.11/site-packages/uvloop/__init__.py", line 48, in wrapper
(APIServer pid=85820)     return await main
(APIServer pid=85820)            ^^^^^^^^^^
(APIServer pid=85820)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1398, in run_server
(APIServer pid=85820)     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
(APIServer pid=85820)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1417, in run_server_worker
(APIServer pid=85820)     async with build_async_engine_client(
(APIServer pid=85820)   File "/usr/local/python3.11.14/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=85820)     return await anext(self.gen)
(APIServer pid=85820)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=85820)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 172, in build_async_engine_client
(APIServer pid=85820)     async with build_async_engine_client_from_engine_args(
(APIServer pid=85820)   File "/usr/local/python3.11.14/lib/python3.11/contextlib.py", line 210, in __aenter__
(APIServer pid=85820)     return await anext(self.gen)
(APIServer pid=85820)            ^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=85820)   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 213, in build_async_engine_client_from_engine_args
(APIServer pid=85820)     async_llm = AsyncLLM.from_vllm_config(
(APIServer pid=85820)                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=85820)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 215, in from_vllm_config
(APIServer pid=85820)     return cls(
(APIServer pid=85820)            ^^^^
(APIServer pid=85820)   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 134, in __init__
(APIServer pid=85820)     self.engine_core = EngineCoreClient.make_async_mp_client(
(APIServer pid=85820)                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=85820)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 120, in make_async_mp_client
(APIServer pid=85820)     return DPLBAsyncMPClient(*client_args)
(APIServer pid=85820)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(APIServer pid=85820)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 1192, in __init__
(APIServer pid=85820)     super().__init__(
(APIServer pid=85820)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 1033, in __init__
(APIServer pid=85820)     super().__init__(
(APIServer pid=85820)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 820, in __init__
(APIServer pid=85820)     super().__init__(
(APIServer pid=85820)   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 477, in __init__
(APIServer pid=85820)     with launch_core_engines(vllm_config, executor_class, log_stats) as (
(APIServer pid=85820)   File "/usr/local/python3.11.14/lib/python3.11/contextlib.py", line 144, in __exit__
(APIServer pid=85820)     next(self.gen)
(APIServer pid=85820)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 903, in launch_core_engines
(APIServer pid=85820)     wait_for_engine_startup(
(APIServer pid=85820)   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 960, in wait_for_engine_startup
(APIServer pid=85820)     raise RuntimeError(
(APIServer pid=85820) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
(APIServer pid=85820) [ERROR] 2026-01-26-10:28:29 (PID:85820, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```
