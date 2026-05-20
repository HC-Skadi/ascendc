# Issue #4502: [Bug]: 如果在初始化同步engine之前使用过torch_npu的某些方法，会导致engine初始化失败

## 基本信息

- **编号**: #4502
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4502
- **创建时间**: 2025-11-27T08:27:31Z
- **关闭时间**: 2025-12-08T07:56:56Z
- **更新时间**: 2025-12-08T07:56:56Z
- **提交者**: @myhloli
- **评论数**: 6

## 标签

bug

## 问题描述

### Your current environment

```
root@PJ910000110006:/workspace# python test.py 
memory: 60.96875
INFO 11-27 08:18:52 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 11-27 08:18:52 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 11-27 08:18:52 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 11-27 08:18:52 [__init__.py:207] Platform plugin ascend is activated
WARNING 11-27 08:18:59 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 11-27 08:18:59 [registry.py:582] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 11-27 08:18:59 [registry.py:582] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 11-27 08:18:59 [registry.py:582] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 11-27 08:18:59 [registry.py:582] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 11-27 08:18:59 [registry.py:582] Model architecture Qwen2_5OmniModel is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_omni_thinker:AscendQwen2_5OmniThinkerForConditionalGeneration.
WARNING 11-27 08:18:59 [registry.py:582] Model architecture DeepseekV32ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3_2:CustomDeepseekV3ForCausalLM.
WARNING 11-27 08:18:59 [registry.py:582] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
INFO 11-27 08:18:59 [utils.py:233] non-default args: {'disable_log_stats': True, 'logits_processors': [<class 'mineru_vl_utils.logits_processor.vllm_v1_no_repeat_ngram.VllmV1NoRepeatNGramLogitsProcessor'>], 'model': 'opendatalab/MinerU2.5-2509-1.2B'}
INFO 11-27 08:18:59 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/opendatalab/MinerU2.5-2509-1.2B
2025-11-27 08:19:00,773 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/opendatalab/MinerU2.5-2509-1.2B
2025-11-27 08:19:02,028 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/opendatalab/MinerU2.5-2509-1.2B
2025-11-27 08:19:03,047 - modelscope - INFO - Target directory already exists, skipping creation.
INFO 11-27 08:19:03 [model.py:547] Resolved architecture: Qwen2VLForConditionalGeneration
`torch_dtype` is deprecated! Use `dtype` instead!
INFO 11-27 08:19:03 [model.py:1510] Using max model len 16384
INFO 11-27 08:19:03 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=8192.
INFO 11-27 08:19:03 [platform.py:213] PIECEWISE compilation enabled on NPU. use_inductor not supported - using only ACL Graph mode
INFO 11-27 08:19:03 [utils.py:441] Calculated maximum supported batch sizes for ACL graph: 72
WARNING 11-27 08:19:03 [utils.py:444] Currently, communication is performed using FFTS+ method, which reduces the number of available streams and, as a result, limits the range of runtime shapes that can be handled. To both improve communication performance and increase the number of supported shapes, set HCCL_OP_EXPANSION_MODE=AIV.
INFO 11-27 08:19:03 [utils.py:474] No adjustment needed for ACL graph batch sizes: Qwen2VLForConditionalGeneration model (layers: 24) with 67 sizes
WARNING 11-27 08:19:03 [platform.py:275] If chunked prefill or prefix caching is enabled, block size must be set to 128.
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/opendatalab/MinerU2.5-2509-1.2B
2025-11-27 08:19:04,620 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/opendatalab/MinerU2.5-2509-1.2B
2025-11-27 08:19:06,251 - modelscope - INFO - Target directory already exists, skipping creation.
Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/opendatalab/MinerU2.5-2509-1.2B
2025-11-27 08:19:07,342 - modelscope - INFO - Target directory already exists, skipping creation.
(EngineCore_DP0 pid=14421) INFO 11-27 08:19:07 [core.py:644] Waiting for init message from front-end.
(EngineCore_DP0 pid=14421) INFO 11-27 08:19:07 [core.py:77] Initializing a V1 LLM engine (v0.11.0) with config: model='opendatalab/MinerU2.5-2509-1.2B', speculative_config=None, tokenizer='opendatalab/MinerU2.5-2509-1.2B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=16384, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=npu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=opendatalab/MinerU2.5-2509-1.2B, enable_prefix_caching=True, chunked_prefill_enabled=True, pooler_config=None, compilation_config={"level":3,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":["all"],"splitting_ops":["vllm.unified_attention","vllm.unified_attention_with_output","vllm.mamba_mixer2","vllm.mamba_mixer","vllm.short_conv","vllm.linear_attention","vllm.plamo2_mamba_mixer","vllm.gdn_attention","vllm.sparse_attn_indexer","vllm.unified_ascend_attention_with_output","vllm.mla_forward"],"use_inductor":false,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":1,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[512,504,496,488,480,472,464,456,448,440,432,424,416,408,400,392,384,376,368,360,352,344,336,328,320,312,304,296,288,280,272,264,256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"use_inductor_graph_partition":false,"pass_config":{},"max_capture_size":512,"local_cache_dir":null}
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708] EngineCore failed to start.
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708] Traceback (most recent call last):
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 83, in __init__
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]     self._init_executor()
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 53, in _init_executor
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]     self.collective_rpc("init_worker", args=([kwargs], ))
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 83, in collective_rpc
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]     return [run_method(self.driver_worker, method, args, kwargs)]
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 3122, in run_method
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]     return func(*args, **kwargs)
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 248, in init_worker
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]     self.worker = worker_class(**kwargs)
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]                   ^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 92, in __init__
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]     init_ascend_soc_version()
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]   File "/vllm-workspace/vllm-ascend/vllm_ascend/utils.py", line 623, in init_ascend_soc_version
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]     soc_version = torch_npu.npu.get_soc_version()
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/npu/_backends.py", line 97, in get_soc_version
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]     torch_npu.npu._lazy_init()
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/npu/__init__.py", line 247, in _lazy_init
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708]     raise RuntimeError(
(EngineCore_DP0 pid=14421) ERROR 11-27 08:19:08 [core.py:708] RuntimeError: Cannot re-initialize NPU in forked subprocess. To use NPU with multiprocessing, you must use the 'spawn' start method
(EngineCore_DP0 pid=14421) Process EngineCore_DP0:
(EngineCore_DP0 pid=14421) Traceback (most recent call last):
(EngineCore_DP0 pid=14421)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
(EngineCore_DP0 pid=14421)     self.run()
(EngineCore_DP0 pid=14421)   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
(EngineCore_DP0 pid=14421)     self._target(*self._args, **self._kwargs)
(EngineCore_DP0 pid=14421)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 712, in run_engine_core
(EngineCore_DP0 pid=14421)     raise e
(EngineCore_DP0 pid=14421)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
(EngineCore_DP0 pid=14421)     engine_core = EngineCoreProc(*args, **kwargs)
(EngineCore_DP0 pid=14421)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=14421)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
(EngineCore_DP0 pid=14421)     super().__init__(vllm_config, executor_class, log_stats,
(EngineCore_DP0 pid=14421)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 83, in __init__
(EngineCore_DP0 pid=14421)     self.model_executor = executor_class(vllm_config)
(EngineCore_DP0 pid=14421)                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=14421)   File "/vllm-workspace/vllm/vllm/executor/executor_base.py", line 54, in __init__
(EngineCore_DP0 pid=14421)     self._init_executor()
(EngineCore_DP0 pid=14421)   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 53, in _init_executor
(EngineCore_DP0 pid=14421)     self.collective_rpc("init_worker", args=([kwargs], ))
(EngineCore_DP0 pid=14421)   File "/vllm-workspace/vllm/vllm/executor/uniproc_executor.py", line 83, in collective_rpc
(EngineCore_DP0 pid=14421)     return [run_method(self.driver_worker, method, args, kwargs)]
(EngineCore_DP0 pid=14421)             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=14421)   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 3122, in run_method
(EngineCore_DP0 pid=14421)     return func(*args, **kwargs)
(EngineCore_DP0 pid=14421)            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=14421)   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 248, in init_worker
(EngineCore_DP0 pid=14421)     self.worker = worker_class(**kwargs)
(EngineCore_DP0 pid=14421)                   ^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=14421)   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 92, in __init__
(EngineCore_DP0 pid=14421)     init_ascend_soc_version()
(EngineCore_DP0 pid=14421)   File "/vllm-workspace/vllm-ascend/vllm_ascend/utils.py", line 623, in init_ascend_soc_version
(EngineCore_DP0 pid=14421)     soc_version = torch_npu.npu.get_soc_version()
(EngineCore_DP0 pid=14421)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP0 pid=14421)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/npu/_backends.py", line 97, in get_soc_version
(EngineCore_DP0 pid=14421)     torch_npu.npu._lazy_init()
(EngineCore_DP0 pid=14421)   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/npu/__init__.py", line 247, in _lazy_init
(EngineCore_DP0 pid=14421)     raise RuntimeError(
(EngineCore_DP0 pid=14421) RuntimeError: Cannot re-initialize NPU in forked subprocess. To use NPU with multiprocessing, you must use the 'spawn' start method
Traceback (most recent call last):
  File "/workspace/test.py", line 12, in <module>
    llm = LLM(
          ^^^^
  File "/vllm-workspace/vllm/vllm/entrypoints/llm.py", line 297, in __init__
    self.llm_engine = LLMEngine.from_engine_args(
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/engine/llm_engine.py", line 177, in from_engine_args
    return cls(vllm_config=vllm_config,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/engine/llm_engine.py", line 114, in __init__
    self.engine_core = EngineCoreClient.make_client(
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 80, in make_client
    return SyncMPClient(vllm_config, executor_class, log_stats)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 602, in __init__
    super().__init__(
  File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 448, in __init__
    with launch_core_engines(vllm_config, executor_class,
  File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 144, in __exit__
    next(self.gen)
  File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 732, in launch_core_engines
    wait_for_engine_startup(
  File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 785, in wait_for_engine_startup
    raise RuntimeError("Engine core initialization failed. "
RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
```

### 🐛 Describe the bug

```bash
pip install mineru_vl_utils
```

```python
import torch
import torch_npu
if torch_npu.npu.is_available():
    print(f"memory: {torch_npu.npu.get_device_properties('npu').total_memory / (1024 ** 3)}GB")

from vllm import LLM
from PIL import Image
from mineru_vl_utils import MinerUClient
from mineru_vl_utils import MinerULogitsProcessor  # if vllm>=0.10.1

llm = LLM(
    model="opendatalab/MinerU2.5-2509-1.2B",
    logits_processors=[MinerULogitsProcessor]  # if vllm>=0.10.1
)

client = MinerUClient(
    backend="vllm-engine",
    vllm_llm=llm
)

image = Image.open("./test.jpeg")
extracted_blocks = client.two_step_extract(image)
print(extracted_blocks)
```
