# Issue #5144: [Bug]: v0.11.0 fp16推理结果出现“!!!!”

## 基本信息

- **编号**: #5144
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5144
- **创建时间**: 2025-12-18T02:15:25Z
- **关闭时间**: 2025-12-25T01:16:11Z
- **更新时间**: 2025-12-25T01:16:11Z
- **提交者**: @glowwormX
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.7.1+cpu
Is debug build: False

OS: Huawei Cloud EulerOS 2.0 (aarch64) (aarch64)
GCC version: (conda-forge gcc 13.1.0-0) 13.1.0
Clang version: Could not collect
CMake version: version 4.0.3
Libc version: glibc-2.34

Python version: 3.10.18 | packaged by conda-forge | (main, Jun  4 2025, 14:39:45) [GCC 13.3.0] (64-bit runtime)
Python platform: Linux-4.19.90-vhulk2211.3.0.h1543.eulerosv2r10.aarch64-aarch64-with-glibc2.34

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          192
On-line CPU(s) list:             0-191
Vendor ID:                       HiSilicon
Model name:                      Kunpeng-920
Model:                           0
Thread(s) per core:              1
Core(s) per cluster:             48
Socket(s):                       -
Cluster(s):                      4
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
[pip3] gpytorch==1.14.2
[pip3] numpy==1.26.4
[pip3] pyzmq==27.0.1
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1.post1
[pip3] torchaudio==2.7.0
[pip3] torchdata==0.11.0
[pip3] torchprofile==0.0.4
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] gpytorch                                    1.14.2           pypi_0                pypi
[conda] numpy                                       1.26.4           py310hcbab775_0       conda-forge
[conda] pyzmq                                       27.0.1           pypi_0                pypi
[conda] torch                                       2.7.1+cpu        pypi_0                pypi
[conda] torch-npu                                   2.7.1.post1      pypi_0                pypi
[conda] torchaudio                                  2.7.0            pypi_0                pypi
[conda] torchdata                                   0.11.0           pypi_0                pypi
[conda] torchprofile                                0.0.4            pypi_0                pypi
[conda] torchvision                                 0.22.1           pypi_0                pypi
[conda] transformers                                4.57.1           pypi_0                pypi
vLLM Version: 0.11.0
vLLM Ascend Version: 0.11.0

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=5,7
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/home/ma-user/work/dataset/openLLM_wulan_obs/env_config/cann8.3.rc1/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/home/ma-user/work/dataset/openLLM_wulan_obs/env_config/cann8.3.rc1/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/home/ma-user/work/dataset/openLLM_wulan_obs/env_config/cann8.3.rc1/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/home/ma-user/work/dataset/openLLM_wulan_obs/env_config/cann8.3.rc1/nnal/atb/latest/atb/cxx_abi_0/lib:/home/ma-user/work/dataset/openLLM_wulan_obs/env_config/cann8.3.rc1/nnal/atb/latest/atb/cxx_abi_0/examples:/home/ma-user/work/dataset/openLLM_wulan_obs/env_config/cann8.3.rc1/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/home/ma-user/work/dataset/openLLM_wulan_obs/env_config/cann8.3.rc1/ascend-toolkit/latest/tools/aml/lib64:/home/ma-user/work/dataset/openLLM_wulan_obs/env_config/cann8.3.rc1/ascend-toolkit/latest/tools/aml/lib64/plugin:/home/ma-user/work/dataset/openLLM_wulan_obs/env_config/cann8.3.rc1/ascend-toolkit/latest/lib64:/home/ma-user/work/dataset/openLLM_wulan_obs/env_config/cann8.3.rc1/ascend-toolkit/latest/lib64/plugin/opskernel:/home/ma-user/work/dataset/openLLM_wulan_obs/env_config/cann8.3.rc1/ascend-toolkit/latest/lib64/plugin/nnengine:/home/ma-user/work/dataset/openLLM_wulan_obs/env_config/cann8.3.rc1/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/toolbox/latest/Ascend-DMI/lib64:/usr/lib/aarch64-linux-gnu/hdf5/serial:/usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/compiler/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/:/usr/local/seccomponent/lib/:/usr/local/seccomponent/lib/openssl/:/usr/local/mindspore-lite/mindspore-lite-2.3.0rc3-linux-aarch64/tools/converter/lib:/usr/local/mindspore-lite/mindspore-lite-2.3.0rc3-linux-aarch64/runtime/lib:/usr/local/mindspore-lite/mindspore-lite-2.3.0rc3-linux-aarch64/runtime/third_party/dnnl:/usr/lib64:/home/ma-user/anaconda3/envs/PyTorch-2.1.0/lib
ASCEND_AICPU_PATH=/home/ma-user/work/dataset/openLLM_wulan_obs/env_config/cann8.3.rc1/ascend-toolkit/latest
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/home/ma-user/work/dataset/openLLM_wulan_obs/env_config/cann8.3.rc1/ascend-toolkit/latest
ASCEND_AUTOML_PATH=/usr/local/Ascend/ascend-toolkit/latest/tools
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0.3                 Version: 24.1.0.3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 5     910B1               | OK            | 97.0        49                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          59499/ 65536         |
+===========================+===============+====================================================+
| 7     910B1               | OK            | 94.4        50                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3422 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 5       0                 | 2865645       | VLLMEngineCor            | 56131                   |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.0.RC1
innerversion=V100R001C17SPC001B240
compatible_version=[V100R001C15,V100R001C18],[V100R001C30],[V100R001C13],[V100R003C11],[V100R001C29],[V100R001C10]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.RC1/aarch64-linux
```

</details>


### 🐛 Describe the bug

起初在verl训练时发现了问题，[verl_issues](https://github.com/volcengine/verl/issues/4200)，后面单独跑了vllm-ascend同样会出现

vllm启动脚本：
```
pkill -f -9 'VLLM'

source /home/ma-user/work/dataset/openLLM_wulan_obs/env_config/cann8.3.rc1/ascend-toolkit/set_env.sh
source /home/ma-user/work/dataset/openLLM_wulan_obs/env_config/cann8.3.rc1/nnal/atb/set_env.sh
source /cache/verl_1118_env_main_py310_vllm_v11_release_unpack/bin/activate
set -x
pip list|grep vllm
pip list|grep torch
python -c "import platform, torch, torch_npu, transformers; print('Python:', platform.python_version()); print('PyTorch:', torch.__version__); print('PyTorch_npu:', torch_npu.__version__) ; print('CANN:', torch.version.cann); print('transformers:', transformers.__version__)"

export VLLM_ASCEND_ENABLE_NZ=0
export VLLM_USE_V1=1

vllm serve /home/ma-user/work/dataset/openLLM_wulan/DeepSeek/DeepSeek_R1_Distill_Qwen_1_5B --dtype float16 --max_model_len 9216 --max_num_seqs 1024 --gpu_memory_utilization 0.9 --tensor_parallel_size 1 --seed 0

export VLLM_ASCEND_ENABLE_NZ=0
export VLLM_USE_V1=1

vllm serve /home/ma-user/work/dataset/openLLM_wulan/DeepSeek/DeepSeek_R1_Distill_Qwen_1_5B --dtype float16 --max_model_len 9216 --max_num_seqs 1024 --gpu_memory_utilization 0.9 --tensor_parallel_size 1 --seed 0
```
重新source了cann环境，打印了相关版本：
```
+ pip list
+ grep vllm
vllm                                     0.11.0+empty
vllm-ascend                              0.11.0
+ pip list
+ grep torch
gpytorch                                 1.14.2
torch                                    2.7.1+cpu
torch_npu                                2.7.1.post1
torchaudio                               2.7.0
torchdata                                0.11.0
torchprofile                             0.0.4
torchvision                              0.22.1
+ python -c 'import platform, torch, torch_npu, transformers; print('\''Python:'\'', platform.python_version()); print('\''PyTorch:'\'', torch.__version__); print('\''PyTorch_npu:'\'', torch_npu.__version__) ; print('\''CANN:'\'', torch.version.cann); print('\''transformers:'\'', transformers.__version__)'
Python: 3.10.18
PyTorch: 2.7.1+cpu
PyTorch_npu: 2.7.1.post1
CANN: 8.3.RC1
transformers: 4.57.1
```

请求：
```
for ((i=1; i<=2; i++))
do
    curl -w "总耗时: %{time_total}秒\n" http://localhost:8000/v1/completions     -H "Content-Type: application/json"     -d '{
        "model": "/home/ma-user/work/dataset/openLLM_wulan/DeepSeek/DeepSeek_R1_Distill_Qwen_1_5B",
        "prompt": "<｜begin▁of▁sentence｜><｜User｜>Let $a,b,c$ be the roots of $x^3-9x^2+11x-1=0$, and let $s=\\sqrt{a}+\\sqrt{b}+\\sqrt{c}$.  Find $s^4-18s^2-8s$. Please reason step by step, and put your final answer within \\boxed{}.\n<｜Assistant｜><think>\n",
        "max_tokens": "64",
        "top_p": "1",
        "top_k": "-1",
        "temperature": "1.0"
    }' &
done
```

输出：
```
{"id":"cmpl-1e6c93a2bb014386a065b5f4f7375c79","object":"text_completion","created":1766024046,"model":"/home/ma-user/work/dataset/openLLM_wulan/DeepSeek/DeepSeek_R1_Distill_Qwen_1_5B","choices":[{"index":0,"text":"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!","logprobs":null,"finish_reason":"length","stop_reason":null,"token_ids":null,"prompt_logprobs":null,"prompt_token_ids":null}],"service_tier":null,"system_fingerprint":null,"usage":{"prompt_tokens":86,"total_tokens":150,"completion_tokens":64,"prompt_tokens_details":null},"kv_transfer_params":null}总耗时: 1.099893秒
{"id":"cmpl-6b08b71800924b888846e16efb590c7a","object":"text_completion","created":1766024046,"model":"/home/ma-user/work/dataset/openLLM_wulan/DeepSeek/DeepSeek_R1_Distill_Qwen_1_5B","choices":[{"index":0,"text":"Okay, so I've got this problem here where I need to find the value of \\( s^4 - 18s^2 - 8s \\) where \\( s = \\sqrt{a} + \\sqrt{b} + \\sqrt{c} \\) and \\( a, b, c","logprobs":null,"finish_reason":"length","stop_reason":null,"token_ids":null,"prompt_logprobs":null,"prompt_token_ids":null}],"service_tier":null,"system_fingerprint":null,"usage":{"prompt_tokens":86,"total_tokens":150,"completion_tokens":64,"prompt_tokens_details":null},"kv_transfer_params":null}总耗时: 1.115041秒
```

奇怪的是并发时永远都是第一个请求出现"!!!"
