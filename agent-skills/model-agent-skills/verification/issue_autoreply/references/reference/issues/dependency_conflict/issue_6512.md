# Issue #6512: [Bug]: vllm ascend 0.13.0rc1 + mooncake + Qwen3-Embedding-8B执行vllm bench测试的时候会卡住

## 基本信息

- **编号**: #6512
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6512
- **创建时间**: 2026-02-03T12:07:47Z
- **关闭时间**: 2026-02-24T11:25:28Z
- **更新时间**: 2026-02-24T11:25:28Z
- **提交者**: @GoMarck
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
PyTorch version: 2.8.0+cpu
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0
Clang version: Could not collect
CMake version: version 4.2.1
Libc version: glibc-2.35

Python version: 3.11.13 (main, Nov 20 2025, 16:02:27) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.15.0-25-generic-aarch64-with-glibc2.35

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Byte Order:                      Little Endian
CPU(s):                          256
On-line CPU(s) list:             0-255
Vendor ID:                       HiSilicon
Model name:                      Kunpeng-920
Model:                           0
Thread(s) per core:              1
Core(s) per socket:              64
Socket(s):                       4
Stepping:                        0x1
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       16 MiB (256 instances)
L1i cache:                       16 MiB (256 instances)
L2 cache:                        128 MiB (256 instances)
L3 cache:                        256 MiB (8 instances)
NUMA node(s):                    8
NUMA node0 CPU(s):               0-31
NUMA node1 CPU(s):               32-63
NUMA node2 CPU(s):               64-95
NUMA node3 CPU(s):               96-127
NUMA node4 CPU(s):               128-159
NUMA node5 CPU(s):               160-191
NUMA node6 CPU(s):               192-223
NUMA node7 CPU(s):               224-255
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.1.0
[pip3] torch==2.8.0+cpu
[pip3] torch_npu==2.8.0
[pip3] torchvision==0.23.0
[pip3] transformers==4.57.3
[conda] Could not collect
vLLM Version: 0.13.0
vLLM Ascend Version: 0.13.0rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=1
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/lib:/workspace/Mooncake/build/mooncake-store/src:/workspace/Mooncake/build/mooncake-common/src:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/workspace/Mooncake/build/mooncake-store/src:/workspace/Mooncake/build/mooncake-common/src:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/workspace/Mooncake/build/mooncake-store/src:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
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
| npu-smi 25.2.0                   Version: 25.2.0                                               |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 97.9        34                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3408 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 89.5        32                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3408 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 92.3        32                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          41052/ 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 92.4        32                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3390 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 95.6        37                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3403 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 97.2        38                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3400 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 91.0        36                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3401 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 95.4        37                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3400 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| 2       0                 | 1333928       |                          | 37709                   |
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
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/aarch64-linux
```

</details>


### 🐛 Describe the bug

基本环境信息：
- 910B A2容器环境
- vllm ascend 镜像版本：quay.io/ascend/vllm-ascend:v0.13.0rc1
- 模型版本：[Qwen3-Embedding-8B](https://modelscope.cn/models/Qwen/Qwen3-Embedding-8B)
- mooncake版本：0.3.7.post2

容器拉起命令：
```bash
export MODEL_PATH="/mnt/cephfs"
docker run \
    --name "vllm_qwen32b" \
    --privileged \
    -itu root \
    -d \
    --net=host \
    --device=/dev/davinci0:/dev/davinci0 \
    --device=/dev/davinci1:/dev/davinci1 \
    --device=/dev/davinci2:/dev/davinci2 \
    --device=/dev/davinci3:/dev/davinci3 \
    --device=/dev/davinci4:/dev/davinci4 \
    --device=/dev/davinci5:/dev/davinci5 \
    --device=/dev/davinci6:/dev/davinci6 \
    --device=/dev/davinci7:/dev/davinci7 \
    --device=/dev/davinci_manager:/dev/davinci_manager \
    --device=/dev/devmm_svm:/dev/devmm_svm \
    --device=/dev/hisi_hdc:/dev/hisi_hdc \
    -v /usr/local/dcmi:/usr/local/dcmi \
    -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
    -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
    -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
    -v /usr/bin/hccn_tool:/usr/bin/hccn_tool \
    -v /etc/ascend_install.info:/etc/ascend_install.info \
    -v /root/.cache:/root/.cache \
    -v ${MODEL_PATH}:${MODEL_PATH} \
    -it quay.io/ascend/vllm-ascend:v0.13.0rc1 bash
```

部署命令如下：
- 启动Mooncake Master: 
  ```bash
  mooncake_master \
    --rpc_port 19491 \
    --enable_http_metadata_server=true \
    --http_metadata_server_host=https://192.168.1.1 \
    --http_metadata_server_port=8088 \
    --metrics_port 18488 \
    --rpc_thread_num 8 \
    --eviction_ratio 0.05 \
    --eviction_high_watermark_ratio 0.8 \
    > "/tmp/mooncake_master.log" 2>&1 &
  ```
- 启动vllm:
  ```bash
  export HCCL_OP_EXPANSION_MODE="AIV"
  export PYTORCH_NPU_ALLOC_CONF="expandable_segments:True"
  export CPU_AFFINITY_CONF=2
  export TASK_QUEUE_ENABLE=2
  export ATB_OPERATION_EXECUTE_ASYNC=2
  export VLLM_ASCEND_ENABLE_NZ=2
  export VLLM_USE_V1=1
  export ASCEND_RT_VISIBLE_DEVICES=2
  export PYTHONHASHSEED=0
  export ACL_OP_INIT_MODE=1
  export ASCEND_BUFFER_POOL=4:8
  export ASCEND_CONNECT_TIMEOUT=10000
  export ASCEND_TRANSFER_TIMEOUT=10000
  export MOONCAKE_CONFIG_PATH="/root/mooncake.json"
  export MC_LOG_DIR="/tmp"

  # profiling
  export VLLM_TORCH_PROFILER_WITH_STACK=0
  export VLLM_TORCH_PROFILER_DIR="./profiling"
  
  vllm serve /mnt/cephfs/models/Qwen3-Embedding-8B \
      --runner pooling \
      --served-model-name "Qwen3-Embedding" \
      --host 0.0.0.0 \
      --port 8087 \
      --max-model-len 1280 \
      --max-num-seqs 16 \
      --max-num-batched-tokens 4096 \
      --gpu-memory-utilization 0.6 \
      --enable-prefix-caching \
      --async-scheduling \
      --trust-remote-code \
      --enforce-eager \
      --additional-config '{"enable_cpu_binding":true}' \
      --kv-transfer-config '{
          "kv_connector": "AscendStoreConnector",
          "kv_role": "kv_both",
          "kv_connector_extra_config": {
              "lookup_rpc_port":"1",
              "backend": "mooncake"
          }
    }'  > /tmp/vllm.log 2>&1 &
  ```
- mooncake.json
  ```json
  {
      "metadata_server": "P2PHANDSHAKE",
      "protocol": "ascend",
      "device_name": "",
      "master_server_address": "192.168.1.1:19491",
      "global_segment_size": "200GB"
  }
  ```

部署最终成功，运行benchmark测试命令如下：

```bash
vllm bench serve \
    --backend openai-embeddings \
    --endpoint /v1/embeddings \
    --dataset-name custom \
    --dataset-path 9000.jsonl \
    --trust-remote-code \
    --host 192.168.1.1 \
    --port 8087 \
    --model  /mnt/cephfs/models/Qwen3-Embedding-8B \
    --served-model-name Qwen3-Embedding \
    --num-prompts 9000 \
    --max-concurrency 10 \
    --metric-percentiles "50,90,99" \
    --save-result 
```

现象：
在运行到第382个请求之后请求卡住，进度条不再继续往下执行：

```text
INFO 02-03 09:11:55 [__init__.py:43] Available plugins for group vllm.platform_plugins:
INFO 02-03 09:11:55 [__init__.py:45] - ascend -> vllm_ascend:register
INFO 02-03 09:11:55 [__init__.py:48] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 02-03 09:11:55 [__init__.py:217] Platform plugin ascend is activated
INFO 02-03 09:11:55 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available.
INFO 02-03 09:12:01 [__init__.py:108] Registered model loader `<class 'vllm_ascend.model_loader.netloader.netloader.ModelNetLoaderElastic'>` with load format `netloader`
Namespace(subparser='bench', bench_type='serve', dispatch_function=<function BenchmarkServingSubcommand.cmd at 0xffff1e97ec00>, seed=0, num_prompts=9000, dataset_name='custom', no_stream=False, dataset_path='9000.jsonl', no_oversample=False, skip_chat_template=False, disable_shuffle=False, custom_output_len=256, spec_bench_output_len=256, spec_bench_category=None, sonnet_input_len=550, sonnet_output_len=150, sonnet_prefix_len=200, sharegpt_output_len=None, blazedit_min_distance=0.0, blazedit_max_distance=1.0, random_input_len=1024, random_output_len=128, random_range_ratio=0.0, random_prefix_len=0, random_batch_size=1, no_reranker=False, random_mm_base_items_per_request=1, random_mm_num_mm_items_range_ratio=0.0, random_mm_limit_mm_per_prompt={'image': 255, 'video': 1}, random_mm_bucket_config={(256, 256, 1): 0.5, (720, 1280, 1): 0.5, (720, 1280, 16): 0.0}, hf_subset=None, hf_split=None, hf_name=None, hf_output_len=None, prefix_repetition_prefix_len=256, prefix_repetition_suffix_len=256, prefix_repetition_num_prefixes=10, prefix_repetition_output_len=128, label=None, backend='openai-embeddings', base_url=None, host='192.168.1.1', port=8087, endpoint='/v1/embeddings', header=None, max_concurrency=10, model='/mnt/cephfs/models/Qwen3-Embedding-8B', tokenizer=None, tokenizer_mode='auto', use_beam_search=False, logprobs=None, request_rate=inf, burstiness=1.0, trust_remote_code=True, disable_tqdm=False, num_warmups=0, profile=False, save_result=False, save_detailed=False, append_result=False, metadata=None, result_dir=None, result_filename=None, ignore_eos=False, percentile_metrics=None, metric_percentiles='50,90,99', goodput=None, request_id_prefix='bench-5964d374-', top_p=None, top_k=None, min_p=None, temperature=None, frequency_penalty=None, presence_penalty=None, repetition_penalty=None, common_prefix_len=None, served_model_name='Qwen3-Embedding', lora_modules=None, ramp_up_strategy=None, ramp_up_start_rps=None, ramp_up_end_rps=None, ready_check_timeout_sec=600, extra_body=None)
Starting initial single prompt test run...
Waiting for endpoint to become up in 600 seconds
 |                                                                                                                                                                           | 00:02 elapsed, 213:16:38 remaining
Initial test run completed.
Starting main benchmark run...
Traffic request rate: inf
Burstiness factor: 1.0 (Poisson process)
Maximum request concurrency: 10
  4%|███████▏                                                                                                                                                                 | 382/9000 [00:37<05:48, 24.72it/s]
```

查看vllm的日志：

```text
[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-382-0, Total tokens 1182, kvpool hit tokens: 1024, need to load: 1024
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-383-0, Total tokens 1193, kvpool hit tokens: 1024, need to load: 0
^[[0;36m(EngineCore_DP0 pid=10773)^[[0;0m INFO 02-03 11:27:41 [pool_scheduler.py:85] Reqid: embd-bench-373bb790-385-0, Total tokens 1193, kvpool hit tokens: 1024, need to load: 1024
```
会大量打印以上日志，似乎一直在重复lookup阶段。


重试了两次，均为相同现象。


<details>
<summary>数据集生成脚本</summary>

```bash
def save_to_file(prompts, output_file):
    """Save generated prompts to a JSONL file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        for prompt in tqdm(prompts, desc="Writing to file"):
            data = {"prompt": prompt}
            json_line = json.dumps(data, ensure_ascii=False)
            f.write(json_line + '\n')

    logging.info(f"Successfully saved {len(prompts)} entries to {output_file}")


def main():
    # ==============================================================================
    # Configuration - Parts you need to modify
    # ==============================================================================
    config = {
        # Fill in your local model folder path or model name on Hugging Face here
        # For example: 'gpt2', './my_local_llama_model', 'Qwen/Qwen1.5-7B-Chat'
        'tokenizer_path': '/mnt/cephfs/models/Qwen3-Embedding-8B',
        'num_groups': 300,
        'num_prompts_per_group': 30,
        'prefix_length': 1 * 1024,  # Prefix token count
        'suffix_length': 100,  # Suffix token count
        'output_dir': '.',
        'output_file': '9000.jsonl',
        'seed': 42
    }

    # Set random seed
    random.seed(config['seed'])

    # ==============================================================================
    # Load generic tokenizer from specified path
    # ==============================================================================
    tokenizer_path = config['tokenizer_path']
    logging.info(f"Loading tokenizer from '{tokenizer_path}'...")
    try:
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_path, trust_remote_code=True)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
            logging.info("Tokenizer pad_token not set, has been set to eos_token.")

        logging.info("Tokenizer loaded successfully.")
    except Exception as e:
        logging.error(f"Error: Unable to load tokenizer from path '{tokenizer_path}'.")
        logging.error(
            f"Please confirm if the path is correct and if the folder contains files like " +
            "'tokenizer.json' or 'tokenizer_config.json'."
        )
        logging.error(f"Detailed error message: {e}")
        return

    os.makedirs(config['output_dir'], exist_ok=True)
    output_path = os.path.join(config['output_dir'], config['output_file'])
    total_prompts = config['num_groups'] * config['num_prompts_per_group']
    total_tokens = config['prefix_length'] + config['suffix_length']
    logging.info(f"Will generate a total of {total_prompts} entries, each with approximately {total_tokens} tokens.")
    logging.info(f"(Number of groups: {config['num_groups']}, Prompts per group: {config['num_prompts_per_group']})")
    prompts = gen_random_prompts(tokenizer, config['num_groups'], config['num_prompts_per_group'],
                                 config['prefix_length'], config['suffix_length'])
    save_to_file(prompts, output_path)


if __name__ == "__main__":
    main()
```
</details>
