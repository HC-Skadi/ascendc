# Issue #1578: [Bug]: Distributed model serving deployed with LWS on Kubernetes failed

## 基本信息

- **编号**: #1578
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1578
- **创建时间**: 2025-07-02T04:01:54Z
- **关闭时间**: 2025-12-31T02:33:38Z
- **更新时间**: 2025-12-31T02:33:38Z
- **提交者**: @CageW
- **评论数**: 4

## 标签

bug; 310p

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
WARNING 07-02 11:41:37 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 07-02 11:41:38 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-02 11:41:38 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-02 11:41:38 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-02 11:41:38 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-02 11:41:42 [_custom_ops.py:22] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
Collecting environment information...
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.3
Libc version: glibc-2.35

Python version: 3.10.17 (main, May 27 2025, 01:33:16) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-5.10.134-16.3.al8.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                    aarch64
CPU op-mode(s):                  64-bit
Address sizes:                   48 bits physical, 48 bits virtual
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
Frequency boost:                 disabled
CPU max MHz:                     2600.0000
CPU min MHz:                     200.0000
BogoMIPS:                        200.00
Flags:                           fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                       12 MiB (192 instances)
L1i cache:                       12 MiB (192 instances)
L2 cache:                        96 MiB (192 instances)
L3 cache:                        192 MiB (8 instances)
NUMA node(s):                    1
NUMA node0 CPU(s):               0-191
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Mmio stale data:   Not affected
Vulnerability Retbleed:          Not affected
Vulnerability Spec store bypass: Not affected
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==27.0.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1.post1.dev20250619
[pip3] torchvision==0.20.1
[pip3] transformers==4.52.4
[conda] Could not collect
vLLM Version: 0.9.1
vLLM Ascend Version: 0.1.dev1+g0e43813 (git sha: 0e43813)

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ASCEND_VISIBLE_DEVICES=0
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ASCEND_RUNTIME_OPTIONS=
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc1                 Version: 24.1.rc1                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 94.6        40                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3439 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| 0       0                 | 1904          | python3                  | 101                     |
| 0       0                 | 2044          | python3                  | 99                      |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux
```

</details>


### 🐛 Describe the bug

Deployed distributed task with LWS, here is my yaml configuration file:
```yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    annotation: cannotbenull
    leaderworkerset.sigs.k8s.io/size: "2"
  creationTimestamp: "2025-07-02T03:15:36Z"
  generateName: os-xxx-
  labels:
    apps.kubernetes.io/pod-index: "0"
    controller-revision-hash: os-xxx
    leaderworkerset.sigs.k8s.io/group-index: "0"
    leaderworkerset.sigs.k8s.io/group-key: xxx
    leaderworkerset.sigs.k8s.io/name: os-xxxx
    leaderworkerset.sigs.k8s.io/template-revision-hash: xxx
    leaderworkerset.sigs.k8s.io/worker-index: "0"
    role: leader
    statefulset.kubernetes.io/pod-name: os-xxxx-0
  name: os-xxxx-0
  namespace: xxx
  ownerReferences:
  - apiVersion: apps/v1
    blockOwnerDeletion: true
    controller: true
    kind: StatefulSet
    name: os-xxxx
    uid: xxx
  resourceVersion: "8163147"
  uid: xxx
spec:
  containers:
  - command:
    - sh
    - -c
    - /lws/code/ray_init.sh leader --ray_cluster_size=$(LWS_GROUP_SIZE); vllm serve
      /models/Qwen2.5-7B-Instruct  --trust-remote-code  --disable-log-requests   --served_model_name
      Qwen2.5-7B-Instruct  --host 0.0.0.0 --port 8000  --tensor-parallel-size=2
    env:
    - name: LWS_LEADER_ADDRESS
      value: os-xxxxx
    - name: LWS_GROUP_SIZE
      value: "2"
    image: quay.io/ascend/vllm-ascend:v0.9.1rc1-310p-lws
    imagePullPolicy: IfNotPresent
    name: leaderworkerset
    ports:
    - containerPort: 8000
      protocol: TCP
    readinessProbe:
      failureThreshold: 3
      initialDelaySeconds: 10
      periodSeconds: 5
      successThreshold: 1
      tcpSocket:
        port: 8000
      timeoutSeconds: 1
    resources:
      limits:
        cpu: "16"
        huawei.com/Ascend910: "1"
        memory: 32Gi
      requests:
        cpu: "16"
        huawei.com/Ascend910: "1"
        memory: 32Gi
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /models/Qwen2.5-7B-Instruct
      name:pvc-os-xxxxxxxx
    - mountPath: /dev/shm
      name: dshm
    - mountPath: /etc/localtime
      name: localtime
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-brjcz
      readOnly: true
  dnsPolicy: ClusterFirst
  enableServiceLinks: true
  preemptionPolicy: PreemptLowerPriority
  priority: 0
  restartPolicy: Always
  schedulerName: default-scheduler
  securityContext: {}
  serviceAccount: default
  serviceAccountName: default
  subdomain: os-xxxxxxx
  terminationGracePeriodSeconds: 30
  tolerations:
  - effect: NoExecute
    key: node.kubernetes.io/not-ready
    operator: Exists
    tolerationSeconds: 300
  - effect: NoExecute
    key: node.kubernetes.io/unreachable
    operator: Exists
    tolerationSeconds: 300
  volumes:
  - name: pvc-os-xxxxxxxx
    persistentVolumeClaim:
      claimName: pvc-os-xxxxxxxx
  - emptyDir:
      medium: Memory
      sizeLimit: 16Gi
    name: dshm
  - hostPath:
      path: /etc/localtime
      type: File
    name: localtime
  - name: kube-api-access-brjcz
    projected:
      defaultMode: 420
      sources:
      - serviceAccountToken:
          expirationSeconds: 3607
          path: token
      - configMap:
          items:
          - key: ca.crt
            path: ca.crt
          name: kube-root-ca.crt
      - downwardAPI:
          items:
          - fieldRef:
              apiVersion: v1
              fieldPath: metadata.namespace
            path: namespace
```
and the bug information is:
```bash
2025-07-01 22:44:21,057 INFO usage_lib.py:467 -- Usage stats collection is enabled by default without user confirmation because this terminal is detected to be non-interactive. To disable this, add `--disable-usage-stats` to the command that starts the cluster, or run the following command: `ray disable-usage-stats` before starting the cluster. See https://docs.ray.io/en/master/cluster/usage-stats.html for more details.
2025-07-01 22:44:21,058 INFO scripts.py:971 -- Local node IP: 172.26.1.141
2025-07-01 22:44:24,648 SUCC scripts.py:1007 -- --------------------
2025-07-01 22:44:24,649 SUCC scripts.py:1008 -- Ray runtime started.
2025-07-01 22:44:24,649 SUCC scripts.py:1009 -- --------------------
2025-07-01 22:44:24,649 INFO scripts.py:1011 -- Next steps
2025-07-01 22:44:24,649 INFO scripts.py:1014 -- To add another node to this Ray cluster, run
2025-07-01 22:44:24,649 INFO scripts.py:1017 --   ray start --address='172.26.1.141:6379'
2025-07-01 22:44:24,649 INFO scripts.py:1026 -- To connect to this Ray cluster:
2025-07-01 22:44:24,649 INFO scripts.py:1028 -- import ray
2025-07-01 22:44:24,649 INFO scripts.py:1029 -- ray.init()
2025-07-01 22:44:24,649 INFO scripts.py:1060 -- To terminate the Ray runtime, run
2025-07-01 22:44:24,649 INFO scripts.py:1061 --   ray stop
2025-07-01 22:44:24,649 INFO scripts.py:1064 -- To view the status of the cluster, use
2025-07-01 22:44:24,649 INFO scripts.py:1065 --   ray status
2025-07-01 22:44:26,055 INFO worker.py:1723 -- Connecting to existing Ray cluster at address: 172.26.1.141:6379...
2025-07-01 22:44:26,074 INFO worker.py:1917 -- Connected to Ray cluster.
All ray workers are active and the ray cluster is initialized successfully.
INFO 07-01 22:44:33 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-01 22:44:33 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 07-01 22:44:34 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-01 22:44:34 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-01 22:44:34 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-01 22:44:35 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-01 22:44:39 [_custom_ops.py:22] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 07-01 22:44:44 [registry.py:401] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 07-01 22:44:44 [registry.py:401] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 07-01 22:44:44 [registry.py:401] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 07-01 22:44:44 [registry.py:401] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 07-01 22:44:44 [registry.py:401] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 07-01 22:44:44 [registry.py:401] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
INFO 07-01 22:44:46 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 07-01 22:44:48 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 07-01 22:44:50 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 07-01 22:44:51 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 07-01 22:44:51 [api_server.py:1287] vLLM API server version 0.9.1
INFO 07-01 22:44:53 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 07-01 22:44:53 [cli_args.py:309] non-default args: {'host': '0.0.0.0', 'model': '/models/Qwen2.5-7B-Instruct', 'trust_remote_code': True, 'dtype': 'float32', 'max_model_len': 2048, 'enforce_eager': True, 'served_model_name': ['Qwen2.5-7B-Instruct'], 'pipeline_parallel_size': 2, 'disable_log_requests': True}
INFO 07-01 22:45:11 [config.py:823] This model supports multiple tasks: {'score', 'reward', 'generate', 'classify', 'embed'}. Defaulting to 'generate'.
INFO 07-01 22:45:11 [config.py:3265] Upcasting torch.bfloat16 to torch.float32.
WARNING 07-01 22:45:11 [arg_utils.py:1642] --dtype torch.float32 is not supported by the V1 Engine. Falling back to V0. 
INFO 07-01 22:45:11 [config.py:1946] Defaulting to use mp for distributed inference
INFO 07-01 22:45:11 [config.py:1980] Disabled the custom all-reduce kernel because it is not supported on current platform.
INFO 07-01 22:45:11 [platform.py:164] Compilation disabled, using eager mode by default
INFO 07-01 22:45:11 [llm_engine.py:230] Initializing a V0 LLM engine (v0.9.1) with config: model='/models/Qwen2.5-7B-Instruct', speculative_config=None, tokenizer='/models/Qwen2.5-7B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config={}, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float32, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=2, disable_custom_all_reduce=True, quantization=None, enforce_eager=True, kv_cache_dtype=auto,  device_config=npu, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen2.5-7B-Instruct, num_scheduler_steps=1, multi_step_stream_outputs=True, enable_prefix_caching=None, chunked_prefill_enabled=False, use_async_output_proc=False, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":[],"splitting_ops":[],"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{},"inductor_passes":{},"use_cudagraph":true,"cudagraph_num_of_warmups":0,"cudagraph_capture_sizes":[],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"max_capture_size":0,"local_cache_dir":null}, use_cached_outputs=False, 
WARNING 07-01 22:45:13 [multiproc_worker_utils.py:307] Reducing Torch parallelism from 192 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this value as needed.
WARNING 07-01 22:45:13 [utils.py:2737] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xfffde066d210>
WARNING 07-01 22:45:17 [env_override.py:17] NCCL_CUMEM_ENABLE is set to 0, skipping override. This may increase memory overhead with cudagraph+allreduce: https://github.com/NVIDIA/nccl/issues/1234
INFO 07-01 22:45:19 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 07-01 22:45:19 [importing.py:29] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernel compilation.
INFO 07-01 22:45:20 [__init__.py:39] Available plugins for group vllm.platform_plugins:
INFO 07-01 22:45:20 [__init__.py:41] - ascend -> vllm_ascend:register
INFO 07-01 22:45:20 [__init__.py:44] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 07-01 22:45:20 [__init__.py:235] Platform plugin ascend is activated
WARNING 07-01 22:45:24 [_custom_ops.py:22] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
(VllmWorkerProcess pid=1817) INFO 07-01 22:45:27 [multiproc_worker_utils.py:226] Worker ready; awaiting tasks
(VllmWorkerProcess pid=1817) WARNING 07-01 22:45:29 [registry.py:401] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
(VllmWorkerProcess pid=1817) WARNING 07-01 22:45:29 [registry.py:401] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
(VllmWorkerProcess pid=1817) WARNING 07-01 22:45:29 [registry.py:401] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
(VllmWorkerProcess pid=1817) WARNING 07-01 22:45:29 [registry.py:401] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
(VllmWorkerProcess pid=1817) WARNING 07-01 22:45:29 [registry.py:401] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
(VllmWorkerProcess pid=1817) WARNING 07-01 22:45:29 [registry.py:401] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
(VllmWorkerProcess pid=1817) WARNING 07-01 22:45:29 [utils.py:2737] Methods add_prompt_adapter,cache_config,compilation_config,current_platform,list_prompt_adapters,load_config,pin_prompt_adapter,remove_prompt_adapter not implemented in <vllm_ascend.worker.worker.NPUWorker object at 0xffff74fa1d50>
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239] Exception in worker VllmWorkerProcess while processing method init_device.
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239] Traceback (most recent call last):
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239]   File "/vllm-workspace/vllm/vllm/executor/multiproc_worker_utils.py", line 233, in _run_worker_process
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239]     output = run_method(worker, method, args, kwargs)
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239]   File "/vllm-workspace/vllm/vllm/utils.py", line 2671, in run_method
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239]     return func(*args, **kwargs)
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 606, in init_device
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239]     self.worker.init_device()  # type: ignore
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 216, in init_device
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239]     NPUPlatform.set_device(self.device)
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239]   File "/vllm-workspace/vllm-ascend/vllm_ascend/platform.py", line 97, in set_device
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239]     torch.npu.set_device(device)
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/torch_npu/npu/utils.py", line 80, in set_device
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239]     torch_npu._C._npu_setDevice(device_id)
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239] RuntimeError: Initialize:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:146 NPU function error: c10_npu::SetDevice(device_id_), error code is 107001
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239] [ERROR] 2025-07-01-22:45:31 (PID:1817, Device:0, RankID:-1) ERR00100 PTA call acl api failed
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239] [Error]: Invalid device ID.
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239]         Check whether the device ID is valid.
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239] EE1001: [PID: 1817] 2025-07-01-22:45:30.528.819 The argument is invalid.Reason: Set device failed, invalid device, set device=1, valid device range is [0, 1)
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239]         Solution: 1.Check the input parameter range of the function. 2.Check the function invocation relationship.
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239]         TraceBack (most recent call last):
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239]         rtSetDevice execute failed, reason=[device id error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239]         open device 1 failed, runtime result = 107001.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
(VllmWorkerProcess pid=1817) ERROR 07-01 22:45:31 [multiproc_worker_utils.py:239] 


```
