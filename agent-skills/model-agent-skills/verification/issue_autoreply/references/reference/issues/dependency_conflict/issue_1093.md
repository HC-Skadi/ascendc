# Issue #1093: [Bug]: 使用trl进行GRPO训练出现RuntimeError

## 基本信息

- **编号**: #1093
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1093
- **创建时间**: 2025-06-05T18:01:59Z
- **关闭时间**: 2025-06-16T07:10:51Z
- **更新时间**: 2025-06-16T07:10:51Z
- **提交者**: @SolarWindRider
- **评论数**: 1

## 标签

bug; module:rl

## 问题描述

###  current environment

<details>
<summary> The output of `python collect_env.py`</summary>

```text
(PyTorch-2.1.0) [ma-user work]$python collect_env.py
/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch_npu/utils/collect_env.py:58: UserWarning: Warning: The /usr/local/Ascend/ascend-toolkit/latest owner does not match the current owner.
  warnings.warn(f"Warning: The {path} owner does not match the current owner.")
/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/torch_npu/utils/collect_env.py:58: UserWarning: Warning: The /usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux/ascend_toolkit_install.info owner does not match the current owner.
  warnings.warn(f"Warning: The {path} owner does not match the current owner.")
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Huawei Cloud EulerOS 2.0 (aarch64) (aarch64)
GCC version: (GCC) 10.3.1
Clang version: Could not collect
CMake version: version 4.0.2
Libc version: glibc-2.34

Python version: 3.9.10 | packaged by conda-forge | (main, Feb  1 2022, 21:53:27)  [GCC 9.4.0] (64-bit runtime)
Python platform: Linux-5.10.0-182.0.0.95.r2220_156.hce2.aarch64-aarch64-with-glibc2.34

CPU:
Architecture:                         aarch64
CPU op-mode(s):                       64-bit
Byte Order:                           Little Endian
CPU(s):                               320
On-line CPU(s) list:                  0-319
Vendor ID:                            HiSilicon
Model:                                0
Thread(s) per core:                   2
Core(s) per cluster:                  80
Socket(s):                            -
Cluster(s):                           2
Stepping:                             0x0
Frequency boost:                      disabled
CPU max MHz:                          3000.0000
CPU min MHz:                          400.0000
BogoMIPS:                             200.00
Flags:                                fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs sb paca pacg dcpodp flagm2 frint svei8mm svef32mm svef64mm svebf16 i8mm bf16 dgh rng ecv
L1d cache:                            10 MiB (160 instances)
L1i cache:                            10 MiB (160 instances)
L2 cache:                             200 MiB (160 instances)
L3 cache:                             280 MiB (4 instances)
NUMA node(s):                         4
NUMA node0 CPU(s):                    0-79
NUMA node1 CPU(s):                    80-159
NUMA node2 CPU(s):                    160-239
NUMA node3 CPU(s):                    240-319
Vulnerability Gather data sampling:   Not affected
Vulnerability Itlb multihit:          Not affected
Vulnerability L1tf:                   Not affected
Vulnerability Mds:                    Not affected
Vulnerability Meltdown:               Not affected
Vulnerability Mmio stale data:        Not affected
Vulnerability Reg file data sampling: Not affected
Vulnerability Retbleed:               Not affected
Vulnerability Spec rstack overflow:   Not affected
Vulnerability Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:             Mitigation; __user pointer sanitization
Vulnerability Spectre v2:             Not affected
Vulnerability Srbds:                  Not affected
Vulnerability Tsx async abort:        Not affected

Versions of relevant libraries:
[pip3] gpytorch==1.12
[pip3] modelarts-pytorch-model-server==1.0.6
[pip3] mypy-extensions==1.0.0
[pip3] numpy==1.26.4
[pip3] onnx==1.17.0
[pip3] onnxconverter-common==1.14.0
[pip3] onnxruntime==1.15.1
[pip3] optree==0.14.0
[pip3] pyzmq==26.2.1
[pip3] skl2onnx==1.18.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torchaudio==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.52.4
[pip3] transformers-stream-generator==0.0.5
[conda] gpytorch                  1.12                      <pip>
[conda] modelarts-pytorch-model-server 1.0.6                     <pip>
[conda] numpy                     1.26.4                    <pip>
[conda] optree                    0.14.0                    <pip>
[conda] pyzmq                     26.2.1                    <pip>
[conda] torch                     2.5.1                     <pip>
[conda] torch-npu                 2.5.1                     <pip>
[conda] torchaudio                2.5.1                     <pip>
[conda] torchvision               0.20.1                    <pip>
[conda] transformers              4.52.4                    <pip>
[conda] transformers-stream-generator 0.0.5                     <pip>
vLLM Version: 0.7.3
vLLM Ascend Version: 0.7.3.post1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=6,7,0,1,2,3,4,5
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/toolbox/latest/Ascend-DMI/lib64:/usr/lib/aarch64-linux-gnu/hdf5/serial:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/:/usr/local/seccomponent/lib/:/usr/local/seccomponent/lib/openssl/:/usr/local/mindspore-lite/mindspore-lite-2.4.10-linux-aarch64/tools/converter/lib:/usr/local/mindspore-lite/mindspore-lite-2.4.10-linux-aarch64/runtime/lib:/usr/local/mindspore-lite/mindspore-lite-2.4.10-linux-aarch64/runtime/third_party/dnnl
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ASCEND_AUTOML_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc3.3               Version: 24.1.rc3.3                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 169.7       41                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          3422 / 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           40                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          3204 / 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 173.6       43                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          3429 / 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           42                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          3195 / 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 187.0       43                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3416 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           42                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          3204 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 175.2       41                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3417 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           43                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          3204 / 65536         |
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

CANN:
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux`
```

</details>


### 🐛 Describe the bug

trl==0.18.1
使用下面代码启动GRPO训练：

```python
# train_grpo.py
from datasets import load_dataset
from trl import GRPOConfig, GRPOTrainer


dataset = load_dataset("trl-lib/tldr", split="train", cache_dir="/home/ma-user/work/DownLoads/Dataset/trl-lib/tldr")


# Define the reward function, which rewards completions that are close to 20 characters
def reward_len(completions, **kwargs):
    return [-abs(20 - len(completion)) for completion in completions]


model_name = "Qwen/Qwen2.5-0.5B-Instruct"

training_args = GRPOConfig(output_dir="Qwen2-0.5B-GRPO", logging_steps=10)
trainer = GRPOTrainer(
    model=f"/home/ma-user/work/DownLoads/Models/{model_name}",
    reward_funcs=reward_len,
    args=training_args,
    train_dataset=dataset,
)
trainer.train()

```
报错信息为：No module named 'vllm_ascend.distributed.device_communicators'
```
Traceback (most recent call last):
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/trl/import_utils.py", line 144, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 850, in exec_module
  File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/trl/trainer/grpo_trainer.py", line 50, in <module>
    from ..extras.vllm_client import VLLMClient
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/trl/extras/vllm_client.py", line 38, in <module>
    from vllm_ascend.distributed.device_communicators.pyhccl import PyHcclCommunicator as PyNcclCommunicator
ModuleNotFoundError: No module named 'vllm_ascend.distributed.device_communicators'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/ma-user/work/playground/aaa.py", line 3, in <module>
    from trl import GRPOConfig, GRPOTrainer
  File "<frozen importlib._bootstrap>", line 1055, in _handle_fromlist
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/trl/import_utils.py", line 135, in __getattr__
    value = getattr(module, name)
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/trl/import_utils.py", line 134, in __getattr__
    module = self._get_module(self._class_to_module[name])
  File "/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib/python3.9/site-packages/trl/import_utils.py", line 146, in _get_module
    raise RuntimeError(
RuntimeError: Failed to import trl.trainer.grpo_trainer because of the following error (look up to see its traceback):
No module named 'vllm_ascend.distributed.device_communicators'
[ERROR] 2025-06-06-01:09:45 (PID:716148, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```
