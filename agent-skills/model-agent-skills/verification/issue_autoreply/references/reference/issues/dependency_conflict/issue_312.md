# Issue #312: [Bug]: AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'

## 基本信息

- **编号**: #312
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/312
- **创建时间**: 2025-03-12T07:54:02Z
- **关闭时间**: 2025-03-12T08:59:21Z
- **更新时间**: 2025-03-12T08:59:22Z
- **提交者**: @csw7777
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

使用镜像：quay.io/ascend/vllm-ascend   v0.7.3-dev 
环境：
```
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: Could not collect
Libc version: glibc-2.35

Python version: 3.10.15 (main, Nov 27 2024, 06:51:55) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-60.18.0.50.r865_35.hce2.aarch64-aarch64-with-glibc2.35
Is XNNPACK available: True

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       HiSilicon
BIOS Vendor ID:                  HiSilicon
Model name:                      Kunpeng-920
BIOS Model name:                 HUAWEI Kunpeng 920 5250
Model:                           0
Thread(s) per core:              1
Core(s) per socket:              48
Socket(s):                       4
Stepping:                        0x1
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       12 MiB (192 instances)
L1i cache:                       12 MiB (192 instances)
L2 cache:                        96 MiB (192 instances)
L3 cache:                        192 MiB (8 instances)
NUMA node(s):                    8
NUMA node0 CPU(s):               0-23
NUMA node1 CPU(s):               24-47
NUMA node2 CPU(s):               48-71
NUMA node3 CPU(s):               72-95
NUMA node4 CPU(s):               96-119
NUMA node5 CPU(s):               120-143
NUMA node6 CPU(s):               144-167
NUMA node7 CPU(s):               168-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Mmio stale data:   Not affected
Vulnerability Retbleed:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.2.1
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.dev20250308
[pip3] transformers==4.49.0
[conda] Could not collect
vLLM Version: 0.7.3
vLLM Build Flags:
ROCm: Disabled; Neuron: Disabled

ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_PROCESS_LOG_PATH=/home/log
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/python3.10/lib/python3.10/site-packages/cv2/../../lib64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
VLLM_HOST_IP=192.168.0.11
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
TORCH_DEVICE_BACKEND_AUTOLOAD=1
TORCHINDUCTOR_COMPILE_THREADS=1

NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0                   Version: 24.1.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B1               | OK            | 89.1        32                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3437 / 65536         |
+===========================+===============+====================================================+
| 1     910B1               | OK            | 90.0        33                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3378 / 65536         |
+===========================+===============+====================================================+
| 2     910B1               | OK            | 91.5        32                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3376 / 65536         |
+===========================+===============+====================================================+
| 3     910B1               | OK            | 91.3        32                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3377 / 65536         |
+===========================+===============+====================================================+
| 4     910B1               | OK            | 92.7        31                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3377 / 65536         |
+===========================+===============+====================================================+
| 5     910B1               | OK            | 93.0        33                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3376 / 65536         |
+===========================+===============+====================================================+
| 6     910B1               | OK            | 91.5        30                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3377 / 65536         |
+===========================+===============+====================================================+
| 7     910B1               | OK            | 91.1        32                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3380 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 641248        |                          | 113                     |
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
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux
```

### 🐛 Describe the bug

启动命令（四节点）：
```
export head_node_ip=192.168.0.11
export plog_save_path=/home/log
export nic_name=enp67s0f0

export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export RAY_EXPERIMENTAL_NOSET_ASCEND_RT_VISIBLE_DEVICES=1
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
ray start --head --num-gpus=8 

export head_node_ip=192.168.0.11
export plog_save_path=/home/log
export VLLM_HOST_IP=$head_node_ip
export HCCL_CONNECT_TIMEOUT=12000
export ASCEND_PROCESS_LOG_PATH=$plog_save_path
export HCCL_IF_IP=$head_node_ip

if [ -d "{plog_save_path}" ]; then
    rm -rf {plog_save_path}
    echo ">>> remove {plog_save_path}"
fi

LOG_FILE="multinode_$(date +%Y%m%d_%H%M).log"
VLLM_TORCH_PROFILER_DIR=./vllm_profile
export OMP_NUM_THREADS=1
python -m vllm.entrypoints.openai.api_server  \
       --model="/home/model/deepseekr1" \
       --trust-remote-code \
       --enforce-eager \
       --max-model-len 16384 \
       --gpu_memory_utilization 0.98 \
       --distributed_executor_backend "ray" \
       --tensor_parallel_size=16 \
       --pipeline_parallel_size=2 \
       --disable-log-requests \
       --disable-log-stats \
       --disable-frontend-multiprocessing \
       --block-size 128 \
       --served-model-name="deepseekr1" \
       --dtype bfloat16 \
       --port 8000 
```
```
(NPURayWorkerWrapper pid=6830, ip=192.168.0.14) WARNING 03-12 07:42:27 utils.py:168] The model class DeepseekV3ForCausalLM has not defined `packed_modules_mapping`, this may lead to incorrect mapping of quantized or ignored modules
ERROR 03-12 07:42:27 worker_base.py:581] Error executing method 'load_model'. This might cause deadlock in distributed execution.
ERROR 03-12 07:42:27 worker_base.py:581] Traceback (most recent call last):
ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 573, in execute_method
ERROR 03-12 07:42:27 worker_base.py:581]     return run_method(target, method, args, kwargs)
ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
ERROR 03-12 07:42:27 worker_base.py:581]     return func(*args, **kwargs)
ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 179, in load_model
ERROR 03-12 07:42:27 worker_base.py:581]     self.model_runner.load_model()
ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 818, in load_model
ERROR 03-12 07:42:27 worker_base.py:581]     self.model = get_model(vllm_config=self.vllm_config)
ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
ERROR 03-12 07:42:27 worker_base.py:581]     return loader.load_model(vllm_config=vllm_config)
ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 406, in load_model
ERROR 03-12 07:42:27 worker_base.py:581]     model = _initialize_model(vllm_config=vllm_config)
ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 125, in _initialize_model
ERROR 03-12 07:42:27 worker_base.py:581]     return model_class(vllm_config=vllm_config, prefix=prefix)
ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 655, in __init__
ERROR 03-12 07:42:27 worker_base.py:581]     self.model = DeepseekV2Model(vllm_config=vllm_config,
ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 151, in __init__
ERROR 03-12 07:42:27 worker_base.py:581]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 589, in __init__
ERROR 03-12 07:42:27 worker_base.py:581]     self.start_layer, self.end_layer, self.layers = make_layers(
ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 557, in make_layers
ERROR 03-12 07:42:27 worker_base.py:581]     [PPMissingLayer() for _ in range(start_layer)] + [
ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 558, in <listcomp>
ERROR 03-12 07:42:27 worker_base.py:581]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 591, in <lambda>
ERROR 03-12 07:42:27 worker_base.py:581]     lambda prefix: DeepseekV2DecoderLayer(
ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 496, in __init__
ERROR 03-12 07:42:27 worker_base.py:581]     self.self_attn = attn_cls(
ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 374, in __init__
ERROR 03-12 07:42:27 worker_base.py:581]     self.q_a_proj = ReplicatedLinear(self.hidden_size,
ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 209, in __init__
ERROR 03-12 07:42:27 worker_base.py:581]     super().__init__(input_size,
ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 179, in __init__
ERROR 03-12 07:42:27 worker_base.py:581]     self.quant_method = quant_config.get_quant_method(self,
ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 89, in get_quant_method
ERROR 03-12 07:42:27 worker_base.py:581]     self.packed_modules_mapping):
ERROR 03-12 07:42:27 worker_base.py:581] AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581] Error executing method 'load_model'. This might cause deadlock in distributed execution.
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581] Traceback (most recent call last):
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 573, in execute_method
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]     return run_method(target, method, args, kwargs)
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]     return func(*args, **kwargs)
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 179, in load_model
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]     self.model_runner.load_model()
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 818, in load_model
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]     self.model = get_model(vllm_config=self.vllm_config)
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]     return loader.load_model(vllm_config=vllm_config)
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 406, in load_model
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]     model = _initialize_model(vllm_config=vllm_config)
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 125, in _initialize_model
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]     return model_class(vllm_config=vllm_config, prefix=prefix)
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 655, in __init__
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]     self.model = DeepseekV2Model(vllm_config=vllm_config,
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 151, in __init__
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 589, in __init__
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]     self.start_layer, self.end_layer, self.layers = make_layers(
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 557, in make_layers
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]     [PPMissingLayer() for _ in range(start_layer)] + [
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 558, in <listcomp>
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 591, in <lambda>
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]     lambda prefix: DeepseekV2DecoderLayer(
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 496, in __init__
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]     self.self_attn = attn_cls(
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 374, in __init__
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]     self.q_a_proj = ReplicatedLinear(self.hidden_size,
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 209, in __init__
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]     super().__init__(input_size,
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 179, in __init__
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]     self.quant_method = quant_config.get_quant_method(self,
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 89, in get_quant_method
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581]     self.packed_modules_mapping):
(NPURayWorkerWrapper pid=18142) ERROR 03-12 07:42:27 worker_base.py:581] AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'
[rank0]: Traceback (most recent call last):
[rank0]:   File "/usr/local/python3.10/lib/python3.10/runpy.py", line 196, in _run_module_as_main
[rank0]:     return _run_code(code, main_globals, None,
[rank0]:   File "/usr/local/python3.10/lib/python3.10/runpy.py", line 86, in _run_code
[rank0]:     exec(code, run_globals)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 991, in <module>
[rank0]:     uvloop.run(run_server(args))
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 82, in run
[rank0]:     return loop.run_until_complete(wrapper())
[rank0]:   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/uvloop/__init__.py", line 61, in wrapper
[rank0]:     return await main
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 947, in run_server
[rank0]:     async with build_async_engine_client(args) as engine_client:
[rank0]:   File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
[rank0]:     return await anext(self.gen)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 139, in build_async_engine_client
[rank0]:     async with build_async_engine_client_from_engine_args(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/contextlib.py", line 199, in __aenter__
[rank0]:     return await anext(self.gen)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/entrypoints/openai/api_server.py", line 163, in build_async_engine_client_from_engine_args
[rank0]:     engine_client = AsyncLLMEngine.from_engine_args(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 644, in from_engine_args
[rank0]:     engine = cls(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 594, in __init__
[rank0]:     self.engine = self._engine_class(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 267, in __init__
[rank0]:     super().__init__(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 273, in __init__
[rank0]:     self.model_executor = executor_class(vllm_config=vllm_config, )
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 271, in __init__
[rank0]:     super().__init__(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 52, in __init__
[rank0]:     self._init_executor()
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/ray_distributed_executor.py", line 90, in _init_executor
[rank0]:     self._init_workers_ray(placement_group)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/ray_distributed_executor.py", line 360, in _init_workers_ray
[rank0]:     self._run_workers("load_model",
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/ray_distributed_executor.py", line 480, in _run_workers
[rank0]:     self.driver_worker.execute_method(sent_method, *args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 582, in execute_method
[rank0]:     raise e
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 573, in execute_method
[rank0]:     return run_method(target, method, args, kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/worker.py", line 179, in load_model
[rank0]:     self.model_runner.load_model()
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 818, in load_model
[rank0]:     self.model = get_model(vllm_config=self.vllm_config)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/__init__.py", line 14, in get_model
[rank0]:     return loader.load_model(vllm_config=vllm_config)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 406, in load_model
[rank0]:     model = _initialize_model(vllm_config=vllm_config)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 125, in _initialize_model
[rank0]:     return model_class(vllm_config=vllm_config, prefix=prefix)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 655, in __init__
[rank0]:     self.model = DeepseekV2Model(vllm_config=vllm_config,
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 151, in __init__
[rank0]:     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 589, in __init__
[rank0]:     self.start_layer, self.end_layer, self.layers = make_layers(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 557, in make_layers
[rank0]:     [PPMissingLayer() for _ in range(start_layer)] + [
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/utils.py", line 558, in <listcomp>
[rank0]:     maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}"))
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 591, in <lambda>
[rank0]:     lambda prefix: DeepseekV2DecoderLayer(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 496, in __init__
[rank0]:     self.self_attn = attn_cls(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/deepseek_v2.py", line 374, in __init__
[rank0]:     self.q_a_proj = ReplicatedLinear(self.hidden_size,
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 209, in __init__
[rank0]:     super().__init__(input_size,
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/layers/linear.py", line 179, in __init__
[rank0]:     self.quant_method = quant_config.get_quant_method(self,
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/quantization/quant_config.py", line 89, in get_quant_method
[rank0]:     self.packed_modules_mapping):
[rank0]: AttributeError: 'AscendQuantConfig' object has no attribute 'packed_modules_mapping'
```
