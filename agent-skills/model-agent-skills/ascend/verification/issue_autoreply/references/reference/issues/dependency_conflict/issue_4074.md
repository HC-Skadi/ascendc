# Issue #4074: [Bug]: v0.11.0rc0部署qwen3-vl-8b时崩溃 （310P）

## 基本信息

- **编号**: #4074
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4074
- **创建时间**: 2025-11-10T01:37:53Z
- **关闭时间**: 2025-12-23T12:10:27Z
- **更新时间**: 2025-12-23T12:10:27Z
- **提交者**: @fuyao66
- **评论数**: 5

## 标签

bug; 310p

## 问题描述

### Your current environment

硬件环境：

<img width="738" height="272" alt="Image" src="https://github.com/user-attachments/assets/9cccf0d7-2953-4ac0-b645-4008bc2b5b86" />

软件环境：vllm-ascend:v0.11.0rc0-310p
Package                           Version           Editable project location
--------------------------------- ----------------- ---------------------------
absl-py                           2.3.1
aiofiles                          24.1.0
aiohappyeyeballs                  2.6.1
aiohttp                           3.12.15
aiosignal                         1.4.0
annotated-types                   0.7.0
anyio                             4.11.0
astor                             0.8.1
attrs                             25.3.0
auto_tune                         0.1.0
blake3                            1.0.7
blinker                           1.9.0
cachetools                        6.2.0
cbor2                             5.7.0
certifi                           2025.7.14
cffi                              1.17.1
charset-normalizer                3.4.2
click                             8.3.0
cloudpickle                       3.1.1
cmake                             4.1.0
compressed-tensors                0.11.0
Cython                            3.1.2
dataflow                          0.0.1
decorator                         5.2.1
depyf                             0.19.0
dill                              0.4.0
diskcache                         5.6.3
distro                            1.9.0
dnspython                         2.8.0
einops                            0.8.1
email-validator                   2.3.0
fastapi                           0.118.0
fastapi-cli                       0.0.13
fastapi-cloud-cli                 0.2.1
filelock                          3.19.1
Flask                             3.1.2
frozendict                        2.4.6
frozenlist                        1.7.0
fsspec                            2025.9.0
gguf                              0.17.1
h11                               0.16.0
h2                                4.3.0
hccl                              0.1.0
hccl_parser                       0.1
hf-xet                            1.1.10
hpack                             4.1.0
httpcore                          1.0.9
httptools                         0.6.4
httpx                             0.28.1
huggingface-hub                   0.35.3
Hypercorn                         0.17.3
hyperframe                        6.1.0
idna                              3.10
interegular                       0.3.3
itsdangerous                      2.2.0
Jinja2                            3.1.6
jiter                             0.11.0
jsonschema                        4.25.1
jsonschema-specifications         2025.9.1
lark                              1.2.2
llguidance                        0.7.30
llm_datadist                      0.0.1
llvmlite                          0.45.0
lm-format-enforcer                0.11.3
markdown-it-py                    4.0.0
MarkupSafe                        3.0.3
mdurl                             0.1.2
mistral_common                    1.8.5
modelscope                        1.30.0
mpmath                            1.3.0
msgpack                           1.1.1
msgspec                           0.19.0
msobjdump                         0.1.0
multidict                         6.6.4
networkx                          3.5
ninja                             1.13.0
numba                             0.62.1
numpy                             1.26.4
op_compile_tool                   0.1.0
op_gen                            0.1
op_test_frame                     0.1
opc_tool                          0.1.0
openai                            1.109.1
openai-harmony                    0.0.4
opencv-python-headless            4.12.0.88
outlines_core                     0.2.11
packaging                         25.0
partial-json-parser               0.2.1.1.post6
pathlib2                          2.3.7.post1
pillow                            11.3.0
pip                               25.1.1
priority                          2.0.0
prometheus_client                 0.23.1
prometheus-fastapi-instrumentator 7.1.0
propcache                         0.3.2
protobuf                          6.32.1
psutil                            7.0.0
py-cpuinfo                        9.0.0
pybase64                          1.4.2
pybind11                          3.0.1
pycountry                         24.6.1
pycparser                         2.22
pydantic                          2.11.9
pydantic_core                     2.33.2
pydantic-extra-types              2.10.5
Pygments                          2.19.2
python-dotenv                     1.1.1
python-json-logger                3.3.0
python-multipart                  0.0.20
PyYAML                            6.0.2
pyzmq                             27.1.0
Quart                             0.20.0
ray                               2.49.2
referencing                       0.36.2
regex                             2025.9.18
requests                          2.32.4
rich                              14.1.0
rich-toolkit                      0.15.1
rignore                           0.6.4
rpds-py                           0.27.1
safetensors                       0.6.2
schedule_search                   0.0.1
scipy                             1.15.3
sentencepiece                     0.2.1
sentry-sdk                        2.39.0
setproctitle                      1.3.7
setuptools                        65.5.0
setuptools-scm                    9.2.0
shellingham                       1.5.4
show_kernel_debug_data            0.1.0
six                               1.17.0
sniffio                           1.3.1
soundfile                         0.13.1
soxr                              1.0.0
starlette                         0.48.0
sympy                             1.14.0
te                                0.4.0
tiktoken                          0.11.0
tokenizers                        0.22.1
torch                             2.7.1+cpu
torch_npu                         2.7.1.dev20250724
torchvision                       0.22.1
tqdm                              4.67.1
transformers                      4.57.1
typer                             0.19.2
typing_extensions                 4.15.0
typing-inspection                 0.4.1
urllib3                           2.5.0
uvicorn                           0.37.0
uvloop                            0.21.0
vllm                              0.11.0rc3+empty   /vllm-workspace/vllm
vllm_ascend                       0.11.0rc0         /vllm-workspace/vllm-ascend
watchfiles                        1.1.0
websockets                        15.0.1
Werkzeug                          3.1.3
wheel                             0.45.1
wsproto                           1.2.0
xgrammar                          0.1.25
yarl                              1.20.1

### 🐛 Describe the bug

部署日志：
nohup: ignoring input
INFO 11-10 01:23:32 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 11-10 01:23:32 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 11-10 01:23:32 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 11-10 01:23:32 [__init__.py:207] Platform plugin ascend is activated
WARNING 11-10 01:23:37 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 11-10 01:23:37 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 11-10 01:23:37 [registry.py:581] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 11-10 01:23:37 [registry.py:581] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 11-10 01:23:37 [registry.py:581] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 11-10 01:23:37 [registry.py:581] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 11-10 01:23:37 [registry.py:581] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 11-10 01:23:37 [registry.py:581] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 11-10 01:23:37 [registry.py:581] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 11-10 01:23:37 [registry.py:581] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 11-10 01:23:37 [registry.py:581] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
[1;36m(APIServer pid=4635)[0;0m INFO 11-10 01:23:37 [api_server.py:1839] vLLM API server version 0.11.0rc3
[1;36m(APIServer pid=4635)[0;0m INFO 11-10 01:23:37 [utils.py:233] non-default args: {'model_tag': '/home/models/Qwen3-VL-8B-Instruct', 'port': 22333, 'model': '/home/models/Qwen3-VL-8B-Instruct', 'dtype': 'float16', 'max_model_len': 14000, 'enforce_eager': True, 'served_model_name': ['Qwen3-VL-8B'], 'tensor_parallel_size': 2}
[1;36m(APIServer pid=4635)[0;0m INFO 11-10 01:23:52 [model.py:547] Resolved architecture: Qwen3VLForConditionalGeneration
[1;36m(APIServer pid=4635)[0;0m `torch_dtype` is deprecated! Use `dtype` instead!
[1;36m(APIServer pid=4635)[0;0m WARNING 11-10 01:23:52 [model.py:1733] Casting torch.bfloat16 to torch.float16.
[1;36m(APIServer pid=4635)[0;0m INFO 11-10 01:23:52 [model.py:1510] Using max model len 14000
[1;36m(APIServer pid=4635)[0;0m INFO 11-10 01:23:53 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=2048.
[1;36m(APIServer pid=4635)[0;0m INFO 11-10 01:23:53 [__init__.py:381] Cudagraph is disabled under eager mode
[1;36m(APIServer pid=4635)[0;0m INFO 11-10 01:23:53 [platform.py:141] Non-MLA LLMs forcibly disable the chunked prefill feature,as the performance of operators supporting this feature functionality is currently suboptimal.
[1;36m(APIServer pid=4635)[0;0m INFO 11-10 01:23:53 [platform.py:179] Compilation disabled, using eager mode by default
INFO 11-10 01:24:02 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 11-10 01:24:02 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 11-10 01:24:02 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 11-10 01:24:02 [__init__.py:207] Platform plugin ascend is activated
WARNING 11-10 01:24:07 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
[1;36m(EngineCore_DP0 pid=5263)[0;0m INFO 11-10 01:24:07 [core.py:644] Waiting for init message from front-end.
[1;36m(EngineCore_DP0 pid=5263)[0;0m INFO 11-10 01:24:07 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
[1;36m(EngineCore_DP0 pid=5263)[0;0m WARNING 11-10 01:24:07 [registry.py:581] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
[1;36m(EngineCore_DP0 pid=5263)[0;0m WARNING 11-10 01:24:07 [registry.py:581] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
[1;36m(EngineCore_DP0 pid=5263)[0;0m WARNING 11-10 01:24:07 [registry.py:581] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
[1;36m(EngineCore_DP0 pid=5263)[0;0m WARNING 11-10 01:24:07 [registry.py:581] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
[1;36m(EngineCore_DP0 pid=5263)[0;0m WARNING 11-10 01:24:07 [registry.py:581] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
[1;36m(EngineCore_DP0 pid=5263)[0;0m WARNING 11-10 01:24:07 [registry.py:581] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
[1;36m(EngineCore_DP0 pid=5263)[0;0m WARNING 11-10 01:24:07 [registry.py:581] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
[1;36m(EngineCore_DP0 pid=5263)[0;0m WARNING 11-10 01:24:07 [registry.py:581] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
[1;36m(EngineCore_DP0 pid=5263)[0;0m WARNING 11-10 01:24:07 [registry.py:581] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
[1;36m(EngineCore_DP0 pid=5263)[0;0m INFO 11-10 01:24:07 [core.py:77] Initializing a V1 LLM engine (v0.11.0rc3) with config: model='/home/models/Qwen3-VL-8B-Instruct', speculative_config=None, tokenizer='/home/models/Qwen3-VL-8B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=14000, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=True, quantization=None, enforce_eager=True, kv_cache_dtype=auto, device_config=npu, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen3-VL-8B, enable_prefix_caching=True, chunked_prefill_enabled=True, pooler_config=None, compilation_config={"level":0,"debug_dump_path":"","cache_dir":"","backend":"","custom_ops":[],"splitting_ops":null,"use_inductor":true,"compile_sizes":[],"inductor_compile_config":{"enable_auto_functionalized_v2":false},"inductor_passes":{},"cudagraph_mode":0,"use_cudagraph":true,"cudagraph_num_of_warmups":1,"cudagraph_capture_sizes":[],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"use_inductor_graph_partition":false,"pass_config":{},"max_capture_size":0,"local_cache_dir":null}
[1;36m(EngineCore_DP0 pid=5263)[0;0m WARNING 11-10 01:24:07 [multiproc_executor.py:720] Reducing Torch parallelism from 128 threads to 1 to avoid unnecessary CPU contention. Set OMP_NUM_THREADS in the external environment to tune this value as needed.
[1;36m(EngineCore_DP0 pid=5263)[0;0m INFO 11-10 01:24:07 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0, 1], buffer_handle=(2, 16777216, 10, 'psm_42e5906f'), local_subscribe_addr='ipc:///tmp/ee1d4621-b4f7-4470-a3fd-029caf776431', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 11-10 01:24:15 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 11-10 01:24:15 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 11-10 01:24:15 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 11-10 01:24:15 [__init__.py:207] Platform plugin ascend is activated
INFO 11-10 01:24:15 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 11-10 01:24:15 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 11-10 01:24:15 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 11-10 01:24:15 [__init__.py:207] Platform plugin ascend is activated
WARNING 11-10 01:24:20 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 11-10 01:24:20 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 11-10 01:24:20 [registry.py:581] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 11-10 01:24:20 [registry.py:581] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 11-10 01:24:20 [registry.py:581] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 11-10 01:24:20 [registry.py:581] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 11-10 01:24:20 [registry.py:581] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 11-10 01:24:20 [registry.py:581] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 11-10 01:24:20 [registry.py:581] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 11-10 01:24:20 [registry.py:581] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 11-10 01:24:20 [registry.py:581] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
WARNING 11-10 01:24:20 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 11-10 01:24:20 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 11-10 01:24:20 [registry.py:581] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 11-10 01:24:20 [registry.py:581] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 11-10 01:24:20 [registry.py:581] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 11-10 01:24:20 [registry.py:581] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 11-10 01:24:20 [registry.py:581] Model architecture DeepseekV2ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV2ForCausalLM.
WARNING 11-10 01:24:20 [registry.py:581] Model architecture DeepseekV3ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v2:CustomDeepseekV3ForCausalLM.
WARNING 11-10 01:24:20 [registry.py:581] Model architecture DeepSeekMTPModel is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_mtp:CustomDeepSeekMTP.
WARNING 11-10 01:24:20 [registry.py:581] Model architecture Qwen3MoeForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_moe:CustomQwen3MoeForCausalLM.
WARNING 11-10 01:24:20 [registry.py:581] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
INFO 11-10 01:24:33 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 11-10 01:24:33 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 11-10 01:24:33 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 11-10 01:24:33 [__init__.py:207] Platform plugin ascend is activated
INFO 11-10 01:24:33 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 11-10 01:24:33 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 11-10 01:24:33 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 11-10 01:24:33 [__init__.py:207] Platform plugin ascend is activated
WARNING 11-10 01:24:38 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 11-10 01:24:38 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
INFO 11-10 01:24:40 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_fd4c7e4f'), local_subscribe_addr='ipc:///tmp/8c83382f-dd13-405f-bad7-eb85b798927a', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 11-10 01:24:41 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_2275956b'), local_subscribe_addr='ipc:///tmp/737a36f4-fcdc-4596-a3a6-e35ba5e47969', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 11-10 01:24:42 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[1], buffer_handle=(1, 4194304, 6, 'psm_fd9f02e0'), local_subscribe_addr='ipc:///tmp/c267b2a4-362c-4e21-977f-67e3b0577980', remote_subscribe_addr=None, remote_addr_ipv6=False)
INFO 11-10 01:24:42 [parallel_state.py:1208] rank 1 in world size 2 is assigned as DP rank 0, PP rank 0, TP rank 1, EP rank 1
INFO 11-10 01:24:42 [parallel_state.py:1208] rank 0 in world size 2 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0
[1;36m(Worker_TP0 pid=5536)[0;0m INFO 11-10 01:24:44 [model_runner_v1.py:2627] Starting to load model /home/models/Qwen3-VL-8B-Instruct...
[1;36m(Worker_TP1 pid=5537)[0;0m INFO 11-10 01:24:44 [model_runner_v1.py:2627] Starting to load model /home/models/Qwen3-VL-8B-Instruct...
[1;36m(Worker_TP0 pid=5536)[0;0m 
Loading safetensors checkpoint shards:   0% Completed | 0/4 [00:00<?, ?it/s]
[1;36m(Worker_TP0 pid=5536)[0;0m 
Loading safetensors checkpoint shards:  25% Completed | 1/4 [00:03<00:10,  3.35s/it]
[1;36m(Worker_TP0 pid=5536)[0;0m 
Loading safetensors checkpoint shards:  50% Completed | 2/4 [00:07<00:07,  3.67s/it]
[1;36m(Worker_TP0 pid=5536)[0;0m 
Loading safetensors checkpoint shards:  75% Completed | 3/4 [00:09<00:03,  3.03s/it]
[1;36m(Worker_TP1 pid=5537)[0;0m INFO 11-10 01:24:58 [default_loader.py:267] Loading weights took 12.60 seconds
[1;36m(Worker_TP0 pid=5536)[0;0m 
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:13<00:00,  3.21s/it]
[1;36m(Worker_TP0 pid=5536)[0;0m 
Loading safetensors checkpoint shards: 100% Completed | 4/4 [00:13<00:00,  3.25s/it]
[1;36m(Worker_TP0 pid=5536)[0;0m 
[1;36m(Worker_TP0 pid=5536)[0;0m INFO 11-10 01:24:59 [default_loader.py:267] Loading weights took 13.11 seconds
[1;36m(Worker_TP1 pid=5537)[0;0m INFO 11-10 01:24:59 [model_runner_v1.py:2661] Loading model weights took 8.5003 GB
[1;36m(Worker_TP0 pid=5536)[0;0m INFO 11-10 01:25:00 [model_runner_v1.py:2661] Loading model weights took 8.5003 GB
[1;36m(Worker_TP0 pid=5536)[0;0m INFO 11-10 01:25:10 [worker_v1.py:234] Available memory: 29540439244, total memory: 46431260672
[1;36m(Worker_TP1 pid=5537)[0;0m INFO 11-10 01:25:11 [worker_v1.py:234] Available memory: 29297150361, total memory: 45816029184
[1;36m(EngineCore_DP0 pid=5263)[0;0m INFO 11-10 01:25:11 [kv_cache_utils.py:1087] GPU KV cache size: 400,640 tokens
[1;36m(EngineCore_DP0 pid=5263)[0;0m INFO 11-10 01:25:11 [kv_cache_utils.py:1091] Maximum concurrency for 14,000 tokens per request: 28.45x
[1;36m(EngineCore_DP0 pid=5263)[0;0m INFO 11-10 01:25:11 [kv_cache_utils.py:1087] GPU KV cache size: 397,312 tokens
[1;36m(EngineCore_DP0 pid=5263)[0;0m INFO 11-10 01:25:11 [kv_cache_utils.py:1091] Maximum concurrency for 14,000 tokens per request: 28.22x
[rank0]:[W1110 01:25:11.636919866 compiler_depend.ts:62] Warning: Cannot create tensor with NZ format while dim < 2, tensor will be created with ND format. (function operator())
[rank1]:[W1110 01:25:11.637762572 compiler_depend.ts:62] Warning: Cannot create tensor with NZ format while dim < 2, tensor will be created with ND format. (function operator())
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] WorkerProc hit an exception.
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] Traceback (most recent call last):
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]     output = func(*args, **kwargs)
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 254, in initialize_from_config
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]     self.worker.initialize_from_config(kv_cache_config)  # type: ignore
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 336, in initialize_from_config
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]     self.model_runner.initialize_kv_cache(kv_cache_config)
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2709, in initialize_kv_cache
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]     kv_caches = self.initialize_kv_cache_tensors(kv_cache_config)
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3045, in initialize_kv_cache_tensors
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]     v_cache = self._convert_torch_format(v_cache)
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2673, in _convert_torch_format
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]     tensor = torch_npu.npu_format_cast(tensor, ACL_FORMAT)
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]     return self._op(*args, **(kwargs or {}))
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] RuntimeError: npuSynchronizeDevice:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:508 NPU function error: AclrtSynchronizeDeviceWithTimeout, error code is 507013
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] [ERROR] 2025-11-10-01:25:12 (PID:5536, Device:0, RankID:-1) ERR00100 PTA call acl api failed
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] [Error]: System Direct Memory Access (DMA) hardware execution error. 
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]         Rectify the fault based on the error information in the ascend log.
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] EL0004: [PID: 5536] 2025-11-10-01:25:11.770.501 Failed to allocate memory.
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]         Possible Cause: Available memory is insufficient.
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]         Solution: Close applications not in use.
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]         TraceBack (most recent call last):
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]         alloc device memory failed, runtime result = 207001[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]         The error from device(6), serial number is 11. there is a sdma error, sdma channel is 0, the channel exist the following problems: The SMMU returns a Terminate error during page table translation.. the value of CQE status is 2. the description of CQE status: When the SQE translates a page table, the SMMU returns a Terminate error.it's config include: setting1=0xc000000880e0000, setting2=0xff009000ff004c, setting3=0, sq base addr=0x800d00001004c000[FUNC:ProcessSdmaErrorInfo][FILE:device_error_proc.cc][LINE:779]
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]         Memory async copy failed, device_id=0, stream_id=37, task_id=3172, flip_num=0, copy_type=2, memcpy_type=0, copy_data_type=0, length=820510720[FUNC:GetError][FILE:stream.cc][LINE:1183]
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]         rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]         wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] 
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] 
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] DEVICE[0] PID[5536]: 
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] EXCEPTION STREAM:
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]   Exception info:TGID=3458349, model id=65535, stream id=37, stream phase=SCHEDULE
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]   Message info[0]:RTS_HWTS: hwts sdma error, slot_id=5, stream_id=37
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]     Other info[0]:time=2025-11-10-09:25:11.620.206, function=int_process_hwts_sdma_error, line=1381, error code=0x20b
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] Traceback (most recent call last):
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]     output = func(*args, **kwargs)
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]   File "/vllm-workspace/vllm/vllm/worker/worker_base.py", line 254, in initialize_from_config
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]     self.worker.initialize_from_config(kv_cache_config)  # type: ignore
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 336, in initialize_from_config
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]     self.model_runner.initialize_kv_cache(kv_cache_config)
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2709, in initialize_kv_cache
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]     kv_caches = self.initialize_kv_cache_tensors(kv_cache_config)
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 3045, in initialize_kv_cache_tensors
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]     v_cache = self._convert_torch_format(v_cache)
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2673, in _convert_torch_format
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]     tensor = torch_npu.npu_format_cast(tensor, ACL_FORMAT)
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/_ops.py", line 1158, in __call__
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]     return self._op(*args, **(kwargs or {}))
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] RuntimeError: npuSynchronizeDevice:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:508 NPU function error: AclrtSynchronizeDeviceWithTimeout, error code is 507013
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] [ERROR] 2025-11-10-01:25:12 (PID:5536, Device:0, RankID:-1) ERR00100 PTA call acl api failed
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] [Error]: System Direct Memory Access (DMA) hardware execution error. 
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]         Rectify the fault based on the error information in the ascend log.
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] EL0004: [PID: 5536] 2025-11-10-01:25:11.770.501 Failed to allocate memory.
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]         Possible Cause: Available memory is insufficient.
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]         Solution: Close applications not in use.
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]         TraceBack (most recent call last):
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]         alloc device memory failed, runtime result = 207001[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]         The error from device(6), serial number is 11. there is a sdma error, sdma channel is 0, the channel exist the following problems: The SMMU returns a Terminate error during page table translation.. the value of CQE status is 2. the description of CQE status: When the SQE translates a page table, the SMMU returns a Terminate error.it's config include: setting1=0xc000000880e0000, setting2=0xff009000ff004c, setting3=0, sq base addr=0x800d00001004c000[FUNC:ProcessSdmaErrorInfo][FILE:device_error_proc.cc][LINE:779]
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]         Memory async copy failed, device_id=0, stream_id=37, task_id=3172, flip_num=0, copy_type=2, memcpy_type=0, copy_data_type=0, length=820510720[FUNC:GetError][FILE:stream.cc][LINE:1183]
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]         rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]         wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] 
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] 
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] DEVICE[0] PID[5536]: 
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] EXCEPTION STREAM:
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]   Exception info:TGID=3458349, model id=65535, stream id=37, stream phase=SCHEDULE
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]   Message info[0]:RTS_HWTS: hwts sdma error, slot_id=5, stream_id=37
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671]     Other info[0]:time=2025-11-10-09:25:11.620.206, function=int_process_hwts_sdma_error, line=1381, error code=0x20b
[1;36m(Worker_TP0 pid=5536)[0;0m ERROR 11-10 01:25:12 [multiproc_executor.py:671] 
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708] EngineCore failed to start.
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708] Traceback (most recent call last):
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]     engine_core = EngineCoreProc(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]     super().__init__(vllm_config, executor_class, log_stats,
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 92, in __init__
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]     self._initialize_kv_caches(vllm_config)
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 207, in _initialize_kv_caches
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]     self.model_executor.initialize_from_config(kv_cache_configs)
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 73, in initialize_from_config
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]     self.collective_rpc("initialize_from_config",
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 264, in collective_rpc
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]     result = get_response(w, dequeue_timeout,
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 248, in get_response
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]     raise RuntimeError(
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708] RuntimeError: Worker failed with error 'npuSynchronizeDevice:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:508 NPU function error: AclrtSynchronizeDeviceWithTimeout, error code is 507013
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708] [ERROR] 2025-11-10-01:25:12 (PID:5536, Device:0, RankID:-1) ERR00100 PTA call acl api failed
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708] [Error]: System Direct Memory Access (DMA) hardware execution error. 
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]         Rectify the fault based on the error information in the ascend log.
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708] EL0004: [PID: 5536] 2025-11-10-01:25:11.770.501 Failed to allocate memory.
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]         Possible Cause: Available memory is insufficient.
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]         Solution: Close applications not in use.
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]         TraceBack (most recent call last):
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]         alloc device memory failed, runtime result = 207001[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]         The error from device(6), serial number is 11. there is a sdma error, sdma channel is 0, the channel exist the following problems: The SMMU returns a Terminate error during page table translation.. the value of CQE status is 2. the description of CQE status: When the SQE translates a page table, the SMMU returns a Terminate error.it's config include: setting1=0xc000000880e0000, setting2=0xff009000ff004c, setting3=0, sq base addr=0x800d00001004c000[FUNC:ProcessSdmaErrorInfo][FILE:device_error_proc.cc][LINE:779]
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]         Memory async copy failed, device_id=0, stream_id=37, task_id=3172, flip_num=0, copy_type=2, memcpy_type=0, copy_data_type=0, length=820510720[FUNC:GetError][FILE:stream.cc][LINE:1183]
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]         rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]         wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708] 
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708] 
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708] DEVICE[0] PID[5536]: 
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708] EXCEPTION STREAM:
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]   Exception info:TGID=3458349, model id=65535, stream id=37, stream phase=SCHEDULE
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]   Message info[0]:RTS_HWTS: hwts sdma error, slot_id=5, stream_id=37
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:12 [core.py:708]     Other info[0]:time=2025-11-10-09:25:11.620.206, function=int_process_hwts_sdma_error, line=1381, error code=0x20b', please check the stack trace above for the root cause
[W1110 01:25:13.659282289 compiler_depend.ts:528] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 5536] 2025-11-10-01:25:13.679.177 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeUsedDevices)
[W1110 01:25:13.661755307 compiler_depend.ts:510] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 5536] 2025-11-10-01:25:13.682.191 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W1110 01:25:13.663521490 compiler_depend.ts:227] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 5536] 2025-11-10-01:25:13.684.115 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
[W1110 01:25:14.013531448 compiler_depend.ts:528] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 5537] 2025-11-10-01:25:14.033.335 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeUsedDevices)
[W1110 01:25:14.015985956 compiler_depend.ts:510] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 5537] 2025-11-10-01:25:14.036.173 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W1110 01:25:14.017974841 compiler_depend.ts:227] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 5537] 2025-11-10-01:25:14.038.284 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
[W1110 01:25:14.019787574 compiler_depend.ts:510] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 5537] 2025-11-10-01:25:14.040.203 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W1110 01:25:14.021668917 compiler_depend.ts:227] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 5537] 2025-11-10-01:25:14.042.067 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
[W1110 01:25:15.421441188 compiler_depend.ts:510] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 5536] 2025-11-10-01:25:15.441.804 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function npuSynchronizeDevice)
[W1110 01:25:15.423192881 compiler_depend.ts:227] Warning: NPU warning, error code is 507013[Error]: 
[Error]: System Direct Memory Access (DMA) hardware execution error. 
        Rectify the fault based on the error information in the ascend log.
EH9999: Inner Error!
        rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
EH9999: [PID: 5536] 2025-11-10-01:25:15.443.837 wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        TraceBack (most recent call last):
 (function empty_cache)
[1;36m(EngineCore_DP0 pid=5263)[0;0m ERROR 11-10 01:25:24 [multiproc_executor.py:154] Worker proc VllmWorker-0 died unexpectedly, shutting down executor.
[1;36m(EngineCore_DP0 pid=5263)[0;0m Process EngineCore_DP0:
[1;36m(EngineCore_DP0 pid=5263)[0;0m Traceback (most recent call last):
[1;36m(EngineCore_DP0 pid=5263)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap
[1;36m(EngineCore_DP0 pid=5263)[0;0m     self.run()
[1;36m(EngineCore_DP0 pid=5263)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/process.py", line 108, in run
[1;36m(EngineCore_DP0 pid=5263)[0;0m     self._target(*self._args, **self._kwargs)
[1;36m(EngineCore_DP0 pid=5263)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 712, in run_engine_core
[1;36m(EngineCore_DP0 pid=5263)[0;0m     raise e
[1;36m(EngineCore_DP0 pid=5263)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 699, in run_engine_core
[1;36m(EngineCore_DP0 pid=5263)[0;0m     engine_core = EngineCoreProc(*args, **kwargs)
[1;36m(EngineCore_DP0 pid=5263)[0;0m                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(EngineCore_DP0 pid=5263)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 498, in __init__
[1;36m(EngineCore_DP0 pid=5263)[0;0m     super().__init__(vllm_config, executor_class, log_stats,
[1;36m(EngineCore_DP0 pid=5263)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 92, in __init__
[1;36m(EngineCore_DP0 pid=5263)[0;0m     self._initialize_kv_caches(vllm_config)
[1;36m(EngineCore_DP0 pid=5263)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 207, in _initialize_kv_caches
[1;36m(EngineCore_DP0 pid=5263)[0;0m     self.model_executor.initialize_from_config(kv_cache_configs)
[1;36m(EngineCore_DP0 pid=5263)[0;0m   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 73, in initialize_from_config
[1;36m(EngineCore_DP0 pid=5263)[0;0m     self.collective_rpc("initialize_from_config",
[1;36m(EngineCore_DP0 pid=5263)[0;0m   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 264, in collective_rpc
[1;36m(EngineCore_DP0 pid=5263)[0;0m     result = get_response(w, dequeue_timeout,
[1;36m(EngineCore_DP0 pid=5263)[0;0m              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(EngineCore_DP0 pid=5263)[0;0m   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 248, in get_response
[1;36m(EngineCore_DP0 pid=5263)[0;0m     raise RuntimeError(
[1;36m(EngineCore_DP0 pid=5263)[0;0m RuntimeError: Worker failed with error 'npuSynchronizeDevice:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:508 NPU function error: AclrtSynchronizeDeviceWithTimeout, error code is 507013
[1;36m(EngineCore_DP0 pid=5263)[0;0m [ERROR] 2025-11-10-01:25:12 (PID:5536, Device:0, RankID:-1) ERR00100 PTA call acl api failed
[1;36m(EngineCore_DP0 pid=5263)[0;0m [Error]: System Direct Memory Access (DMA) hardware execution error. 
[1;36m(EngineCore_DP0 pid=5263)[0;0m         Rectify the fault based on the error information in the ascend log.
[1;36m(EngineCore_DP0 pid=5263)[0;0m EL0004: [PID: 5536] 2025-11-10-01:25:11.770.501 Failed to allocate memory.
[1;36m(EngineCore_DP0 pid=5263)[0;0m         Possible Cause: Available memory is insufficient.
[1;36m(EngineCore_DP0 pid=5263)[0;0m         Solution: Close applications not in use.
[1;36m(EngineCore_DP0 pid=5263)[0;0m         TraceBack (most recent call last):
[1;36m(EngineCore_DP0 pid=5263)[0;0m         alloc device memory failed, runtime result = 207001[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
[1;36m(EngineCore_DP0 pid=5263)[0;0m         The error from device(6), serial number is 11. there is a sdma error, sdma channel is 0, the channel exist the following problems: The SMMU returns a Terminate error during page table translation.. the value of CQE status is 2. the description of CQE status: When the SQE translates a page table, the SMMU returns a Terminate error.it's config include: setting1=0xc000000880e0000, setting2=0xff009000ff004c, setting3=0, sq base addr=0x800d00001004c000[FUNC:ProcessSdmaErrorInfo][FILE:device_error_proc.cc][LINE:779]
[1;36m(EngineCore_DP0 pid=5263)[0;0m         Memory async copy failed, device_id=0, stream_id=37, task_id=3172, flip_num=0, copy_type=2, memcpy_type=0, copy_data_type=0, length=820510720[FUNC:GetError][FILE:stream.cc][LINE:1183]
[1;36m(EngineCore_DP0 pid=5263)[0;0m         rtDeviceSynchronizeWithTimeout execute failed, reason=[sdma copy error][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:53]
[1;36m(EngineCore_DP0 pid=5263)[0;0m         wait for compute device to finish failed, runtime result = 507013.[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
[1;36m(EngineCore_DP0 pid=5263)[0;0m 
[1;36m(EngineCore_DP0 pid=5263)[0;0m 
[1;36m(EngineCore_DP0 pid=5263)[0;0m DEVICE[0] PID[5536]: 
[1;36m(EngineCore_DP0 pid=5263)[0;0m EXCEPTION STREAM:
[1;36m(EngineCore_DP0 pid=5263)[0;0m   Exception info:TGID=3458349, model id=65535, stream id=37, stream phase=SCHEDULE
[1;36m(EngineCore_DP0 pid=5263)[0;0m   Message info[0]:RTS_HWTS: hwts sdma error, slot_id=5, stream_id=37
[1;36m(EngineCore_DP0 pid=5263)[0;0m     Other info[0]:time=2025-11-10-09:25:11.620.206, function=int_process_hwts_sdma_error, line=1381, error code=0x20b', please check the stack trace above for the root cause
[1;36m(APIServer pid=4635)[0;0m Traceback (most recent call last):
[1;36m(APIServer pid=4635)[0;0m   File "/usr/local/python3.11.13/bin/vllm", line 8, in <module>
[1;36m(APIServer pid=4635)[0;0m     sys.exit(main())
[1;36m(APIServer pid=4635)[0;0m              ^^^^^^
[1;36m(APIServer pid=4635)[0;0m   File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 54, in main
[1;36m(APIServer pid=4635)[0;0m     args.dispatch_function(args)
[1;36m(APIServer pid=4635)[0;0m   File "/vllm-workspace/vllm/vllm/entrypoints/cli/serve.py", line 57, in cmd
[1;36m(APIServer pid=4635)[0;0m     uvloop.run(run_server(args))
[1;36m(APIServer pid=4635)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 105, in run
[1;36m(APIServer pid=4635)[0;0m     return runner.run(wrapper())
[1;36m(APIServer pid=4635)[0;0m            ^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=4635)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
[1;36m(APIServer pid=4635)[0;0m     return self._loop.run_until_complete(task)
[1;36m(APIServer pid=4635)[0;0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=4635)[0;0m   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
[1;36m(APIServer pid=4635)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/site-packages/uvloop/__init__.py", line 61, in wrapper
[1;36m(APIServer pid=4635)[0;0m     return await main
[1;36m(APIServer pid=4635)[0;0m            ^^^^^^^^^^
[1;36m(APIServer pid=4635)[0;0m   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1884, in run_server
[1;36m(APIServer pid=4635)[0;0m     await run_server_worker(listen_address, sock, args, **uvicorn_kwargs)
[1;36m(APIServer pid=4635)[0;0m   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 1902, in run_server_worker
[1;36m(APIServer pid=4635)[0;0m     async with build_async_engine_client(
[1;36m(APIServer pid=4635)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
[1;36m(APIServer pid=4635)[0;0m     return await anext(self.gen)
[1;36m(APIServer pid=4635)[0;0m            ^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=4635)[0;0m   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 180, in build_async_engine_client
[1;36m(APIServer pid=4635)[0;0m     async with build_async_engine_client_from_engine_args(
[1;36m(APIServer pid=4635)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 210, in __aenter__
[1;36m(APIServer pid=4635)[0;0m     return await anext(self.gen)
[1;36m(APIServer pid=4635)[0;0m            ^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=4635)[0;0m   File "/vllm-workspace/vllm/vllm/entrypoints/openai/api_server.py", line 225, in build_async_engine_client_from_engine_args
[1;36m(APIServer pid=4635)[0;0m     async_llm = AsyncLLM.from_vllm_config(
[1;36m(APIServer pid=4635)[0;0m                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=4635)[0;0m   File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 1571, in inner
[1;36m(APIServer pid=4635)[0;0m     return fn(*args, **kwargs)
[1;36m(APIServer pid=4635)[0;0m            ^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=4635)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 207, in from_vllm_config
[1;36m(APIServer pid=4635)[0;0m     return cls(
[1;36m(APIServer pid=4635)[0;0m            ^^^^
[1;36m(APIServer pid=4635)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 134, in __init__
[1;36m(APIServer pid=4635)[0;0m     self.engine_core = EngineCoreClient.make_async_mp_client(
[1;36m(APIServer pid=4635)[0;0m                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=4635)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 102, in make_async_mp_client
[1;36m(APIServer pid=4635)[0;0m     return AsyncMPClient(*client_args)
[1;36m(APIServer pid=4635)[0;0m            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
[1;36m(APIServer pid=4635)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 769, in __init__
[1;36m(APIServer pid=4635)[0;0m     super().__init__(
[1;36m(APIServer pid=4635)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 448, in __init__
[1;36m(APIServer pid=4635)[0;0m     with launch_core_engines(vllm_config, executor_class,
[1;36m(APIServer pid=4635)[0;0m   File "/usr/local/python3.11.13/lib/python3.11/contextlib.py", line 144, in __exit__
[1;36m(APIServer pid=4635)[0;0m     next(self.gen)
[1;36m(APIServer pid=4635)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 732, in launch_core_engines
[1;36m(APIServer pid=4635)[0;0m     wait_for_engine_startup(
[1;36m(APIServer pid=4635)[0;0m   File "/vllm-workspace/vllm/vllm/v1/engine/utils.py", line 785, in wait_for_engine_startup
[1;36m(APIServer pid=4635)[0;0m     raise RuntimeError("Engine core initialization failed. "
[1;36m(APIServer pid=4635)[0;0m RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}
[1;36m(APIServer pid=4635)[0;0m [ERROR] 2025-11-10-01:25:26 (PID:4635, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception

