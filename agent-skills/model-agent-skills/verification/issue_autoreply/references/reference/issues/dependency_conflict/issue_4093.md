# Issue #4093: [Bug]: DeepSeek-V3.1-W8A8 MTP inference failure

## 基本信息

- **编号**: #4093
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4093
- **创建时间**: 2025-11-10T09:47:30Z
- **关闭时间**: 2025-11-14T06:41:34Z
- **更新时间**: 2025-11-17T02:58:14Z
- **提交者**: @wxsIcey
- **评论数**: 1

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

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.1.2
Libc version: glibc-2.35

Python version: 3.11.14 (main, Oct 21 2025, 18:24:34) [GCC 11.2.0] (64-bit runtime)
Python platform: Linux-5.10.0-182.0.0.95.r1941_123.hce2.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                         aarch64
CPU op-mode(s):                       64-bit
Byte Order:                           Little Endian
CPU(s):                               320
On-line CPU(s) list:                  0-319
Vendor ID:                            HiSilicon
BIOS Vendor ID:                       HiSilicon
BIOS Model name:                      Kunpeng 920 7285Z
Model:                                0
Thread(s) per core:                   1
Core(s) per socket:                   80
Socket(s):                            4
Stepping:                             0x0
Frequency boost:                      disabled
CPU max MHz:                          3000.0000
CPU min MHz:                          400.0000
BogoMIPS:                             200.00
Flags:                                fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm ssbs sb paca pacg dcpodp flagm2 frint svei8mm svef32mm svef64mm svebf16 i8mm bf16 dgh rng ecv
L1d cache:                            20 MiB (320 instances)
L1i cache:                            20 MiB (320 instances)
L2 cache:                             400 MiB (320 instances)
L3 cache:                             560 MiB (8 instances)
NUMA node(s):                         8
NUMA node0 CPU(s):                    0-39
NUMA node1 CPU(s):                    40-79
NUMA node2 CPU(s):                    80-119
NUMA node3 CPU(s):                    120-159
NUMA node4 CPU(s):                    160-199
NUMA node5 CPU(s):                    200-239
NUMA node6 CPU(s):                    240-279
NUMA node7 CPU(s):                    280-319
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
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.7.1+cpu
[pip3] torch_npu==2.7.1
[pip3] torchvision==0.22.1
[pip3] transformers==4.57.1
[conda] numpy                                1.26.4                              pypi_0           pypi
[conda] pyzmq                                27.1.0                              pypi_0           pypi
[conda] torch                                2.7.1+cpu                           pypi_0           pypi
[conda] torch-npu                            2.7.1                               pypi_0           pypi
[conda] torchvision                          0.22.1                              pypi_0           pypi
[conda] transformers                         4.57.1                              pypi_0           pypi
vLLM Version: 0.10.2rc3.dev1319+g074475541 (git sha: 074475541)
vLLM Ascend Version: 0.11.0rc1.dev188+g3db53d117 (git sha: 3db53d117)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ASCEND_RT_VISIBLE_DEVICES=5,6,7,8
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
VLLM_USE_MODELSCOPE=True
PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc3.7               Version: 24.1.rc3.7                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip  Phy-ID              | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     Ascend910           | OK            | 181.4       36                0    / 0             |
| 0     0                   | 0000:9D:00.0  | 0           0    / 0          3447 / 65536         |
+------------------------------------------------------------------------------------------------+
| 0     Ascend910           | OK            | -           36                0    / 0             |
| 1     1                   | 0000:9F:00.0  | 0           0    / 0          3188 / 65536         |
+===========================+===============+====================================================+
| 1     Ascend910           | OK            | 184.3       35                0    / 0             |
| 0     2                   | 0000:99:00.0  | 0           0    / 0          3423 / 65536         |
+------------------------------------------------------------------------------------------------+
| 1     Ascend910           | OK            | -           36                0    / 0             |
| 1     3                   | 0000:9B:00.0  | 0           0    / 0          3205 / 65536         |
+===========================+===============+====================================================+
| 2     Ascend910           | OK            | 183.8       37                0    / 0             |
| 0     4                   | 0000:95:00.0  | 0           0    / 0          3424 / 65536         |
+------------------------------------------------------------------------------------------------+
| 2     Ascend910           | OK            | -           37                0    / 0             |
| 1     5                   | 0000:97:00.0  | 0           0    / 0          3201 / 65536         |
+===========================+===============+====================================================+
| 3     Ascend910           | OK            | 194.6       36                0    / 0             |
| 0     6                   | 0000:91:00.0  | 0           0    / 0          3426 / 65536         |
+------------------------------------------------------------------------------------------------+
| 3     Ascend910           | OK            | -           39                0    / 0             |
| 1     7                   | 0000:93:00.0  | 0           0    / 0          3209 / 65536         |
+===========================+===============+====================================================+
| 4     Ascend910           | OK            | 182.3       37                0    / 0             |
| 0     8                   | 0000:8D:00.0  | 0           0    / 0          3427 / 65536         |
+------------------------------------------------------------------------------------------------+
| 4     Ascend910           | OK            | -           37                0    / 0             |
| 1     9                   | 0000:8F:00.0  | 0           0    / 0          3203 / 65536         |
+===========================+===============+====================================================+
| 5     Ascend910           | OK            | 184.1       36                0    / 0             |
| 0     10                  | 0000:89:00.0  | 0           0    / 0          3417 / 65536         |
+------------------------------------------------------------------------------------------------+
| 5     Ascend910           | OK            | -           36                0    / 0             |
| 1     11                  | 0000:8B:00.0  | 0           0    / 0          3204 / 65536         |
+===========================+===============+====================================================+
| 6     Ascend910           | OK            | 192.3       37                0    / 0             |
| 0     12                  | 0000:85:00.0  | 0           0    / 0          3432 / 65536         |
+------------------------------------------------------------------------------------------------+
| 6     Ascend910           | OK            | -           37                0    / 0             |
| 1     13                  | 0000:87:00.0  | 0           0    / 0          3198 / 65536         |
+===========================+===============+====================================================+
| 7     Ascend910           | OK            | 186.9       37                0    / 0             |
| 0     14                  | 0000:81:00.0  | 0           0    / 0          3403 / 65536         |
+------------------------------------------------------------------------------------------------+
| 7     Ascend910           | OK            | -           36                0    / 0             |
| 1     15                  | 0000:83:00.0  | 0           0    / 0          3199 / 65536         |
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
version=8.3.RC1
innerversion=V100R001C23SPC001B235
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC1/aarch64-linux
```

</details>


### 🐛 Describe the bug

```python
os.environ["VLLM_USE_MODELSCOPE"] = "True"
os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"
os.environ["HCCL_BUFFSIZE"] = "1024"

def main():
    prompts = [
        "窗前明月光，",
        "The president of the United States is Mr.",
        "The capital of France is",
        "The future of AI is",
        "感时花溅泪，",
        "家书抵万金啥意思？",
        "plz tell me a story: ",
    ]
    # Create a sampling params object.
    sampling_params = SamplingParams(max_tokens=100, temperature=0.6, top_k=40, top_p=0.95)
    
    speculative_config = {
        "method": "deepseek_mtp",
        "num_speculative_tokens": 1,
    }
    
    # Create an LLM.
    llm = LLM(model="/root/.cache/modelscope/hub/models/vllm-ascend/DeepSeek-V3.1-W8A8",
              enforce_eager=True,
              tensor_parallel_size=16,
              enable_expert_parallel=True,
              trust_remote_code=True,
              max_model_len=1024,
              quantization="ascend",
              gpu_memory_utilization=0.9,
              speculative_config=speculative_config,
              
              )

    # Generate texts from the prompts.
    outputs = llm.generate(prompts, sampling_params)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```
```text
WARNING 11-09 08:03:18 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(Worker_TP4_EP4 pid=1011809) INFO 11-09 08:03:18 [model_runner_v1.py:2659] Loading drafter model...
(Worker_TP3_EP3 pid=1011445) INFO 11-09 08:03:18 [model_runner_v1.py:2659] Loading drafter model...
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597] WorkerProc failed to start.
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597] Traceback (most recent call last):
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]   File "/home/wxs/vllm/vllm/v1/executor/multiproc_executor.py", line 571, in worker_main
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]     worker = WorkerProc(*args, **kwargs)
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]   File "/home/wxs/vllm/vllm/v1/executor/multiproc_executor.py", line 437, in __init__
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]     self.worker.load_model()
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]   File "/home/wxs/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 307, in load_model
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]     self.model_runner.load_model()
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]   File "/home/wxs/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2660, in load_model
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]     self.drafter.load_model(self.model)
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]   File "/home/wxs/vllm-ascend/vllm_ascend/spec_decode/mtp_proposer.py", line 92, in load_model
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]     self.model = DeepSeekMTP(
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]                  ^^^^^^^^^^^^
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]   File "/home/wxs/vllm/vllm/compilation/decorators.py", line 201, in __init__
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]     old_init(self, vllm_config=vllm_config, prefix=prefix, **kwargs)
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]   File "/home/wxs/vllm-ascend/vllm_ascend/patch/worker/patch_deepseek_mtp.py", line 49, in __init__
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]     super().__init__(vllm_config=vllm_config, prefix=prefix)
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]   File "/home/wxs/vllm/vllm/model_executor/models/deepseek_mtp.py", line 153, in __init__
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]     self.model = DeepSeekMultiTokenPredictor(vllm_config=vllm_config,
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]   File "/home/wxs/vllm/vllm/model_executor/models/deepseek_mtp.py", line 103, in __init__
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]     self.layers = torch.nn.ModuleDict({
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]                                       ^
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]   File "/home/wxs/vllm/vllm/model_executor/models/deepseek_mtp.py", line 105, in <dictcomp>
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]     DeepSeekMultiTokenPredictorLayer(vllm_config,
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]   File "/home/wxs/vllm-ascend/vllm_ascend/patch/worker/patch_deepseek_mtp.py", line 86, in predictor_init
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]     self.shared_head = SharedHead(config=config,
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]                        ^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]   File "/home/wxs/vllm-ascend/vllm_ascend/patch/worker/patch_deepseek_mtp.py", line 62, in __init__
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]     self.head = ParallelLMHead(
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]                 ^^^^^^^^^^^^^^^
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]   File "/home/wxs/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py", line 183, in __init__
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]     AscendVocabParallelEmbedding.__init__(self, num_embeddings,
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]   File "/home/wxs/vllm-ascend/vllm_ascend/ops/vocab_parallel_embedding.py", line 81, in __init__
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]     quant_method = quant_config.get_quant_method(self, prefix=prefix)
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]   File "/home/wxs/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 129, in get_quant_method
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]     if self.is_layer_skipped_ascend(prefix,
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]   File "/home/wxs/vllm-ascend/vllm_ascend/quantization/quant_config.py", line 161, in is_layer_skipped_ascend
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]     is_skipped = self.quant_description[prefix + '.weight'] == "FLOAT"
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597]                  ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
(Worker_TP12_EP12 pid=1014347) ERROR 11-09 08:03:19 [multiproc_executor.py:597] KeyError: 'model.layers.61.head.weight'
```
