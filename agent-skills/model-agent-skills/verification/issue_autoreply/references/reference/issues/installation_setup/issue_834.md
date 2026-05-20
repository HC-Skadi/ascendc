# Issue #834: [Installation]: failed to run demo after installation

## 基本信息

- **编号**: #834
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/834
- **创建时间**: 2025-05-13T11:24:19Z
- **关闭时间**: 2025-05-13T11:34:38Z
- **更新时间**: 2025-05-13T11:34:39Z
- **提交者**: @Minamoto25
- **评论数**: 1

## 标签

installation

## 问题描述

### Current environment

```text
$ npu-smi info
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.rc1                 Version: 24.1.rc1                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 97.6        52                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3525 / 65536         |
+===========================+===============+=============================
cat /data/8.1/ascend-toolkit/latest/aarch64-linux/ascend_toolkit_install.info 
package_name=Ascend-cann-toolkit
version=8.1.RC1.alpha001
innerversion=V100R001C21B071
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/data/8.1/ascend-toolkit/8.1.RC1.alpha001/aarch64-linux
```


### How you are installing vllm and vllm-ascend
```
# Install vllm-project/vllm from pypi
pip install vllm==0.8.5.post1

# Install vllm-project/vllm-ascend from pypi.
 CFLAGS="-march=armv8.2-a+dotprod+fp16" CXXFLAGS="-march=armv8.2-a+dotprod+fp16" pip install vllm-ascend
```

测试用的python环境
```
Package                                  Version
---------------------------------------- -------------
absl-py                                  2.2.2
aiohappyeyeballs                         2.6.1
aiohttp                                  3.11.18
aiosignal                                1.3.2
airportsdata                             20250224
annotated-types                          0.7.0
anyio                                    4.9.0
ascendctools                             0.1.0
astor                                    0.8.1
async-timeout                            5.0.1
attrs                                    25.3.0
auto_tune                                0.1.0
blake3                                   1.0.4
cachetools                               5.5.2
certifi                                  2025.4.26
cffi                                     1.17.1
charset-normalizer                       3.4.2
click                                    8.1.8
cloudpickle                              3.1.1
cmake                                    4.0.2
compressed-tensors                       0.9.3
dataflow                                 0.0.1
datasets                                 3.6.0
decorator                                5.2.1
Deprecated                               1.2.18
depyf                                    0.18.0
dill                                     0.3.8
diskcache                                5.6.3
distro                                   1.9.0
dnspython                                2.7.0
einops                                   0.8.1
email_validator                          2.2.0
exceptiongroup                           1.3.0
fastapi                                  0.115.12
fastapi-cli                              0.0.7
filelock                                 3.18.0
frozenlist                               1.6.0
fsspec                                   2025.3.0
gguf                                     0.16.3
googleapis-common-protos                 1.70.0
grpcio                                   1.72.0
h11                                      0.16.0
hccl                                     0.1.0
hccl_parser                              0.1
hf-xet                                   1.1.1
httpcore                                 1.0.9
httptools                                0.6.4
httpx                                    0.28.1
huggingface-hub                          0.31.1
idna                                     3.10
importlib_metadata                       8.0.0
interegular                              0.3.3
Jinja2                                   3.1.6
jiter                                    0.9.0
jsonschema                               4.23.0
jsonschema-specifications                2025.4.1
lark                                     1.2.2
llguidance                               0.7.19
llm_datadist                             0.0.1
lm-format-enforcer                       0.10.11
markdown-it-py                           3.0.0
MarkupSafe                               3.0.2
mdurl                                    0.1.2
mistral_common                           1.5.4
mpmath                                   1.3.0
msgspec                                  0.19.0
msobjdump                                0.1.0
multidict                                6.4.3
multiprocess                             0.70.16
nest-asyncio                             1.6.0
networkx                                 3.2.1
ninja                                    1.11.1.4
npu-bridge                               1.15.0
npu-device                               0.1
numpy                                    1.26.4
op_compile_tool                          0.1.0
op_gen                                   0.1
op_test_frame                            0.1
opc_tool                                 0.1.0
openai                                   1.78.1
opencv-python-headless                   4.11.0.86
opentelemetry-api                        1.26.0
opentelemetry-exporter-otlp              1.26.0
opentelemetry-exporter-otlp-proto-common 1.26.0
opentelemetry-exporter-otlp-proto-grpc   1.26.0
opentelemetry-exporter-otlp-proto-http   1.26.0
opentelemetry-proto                      1.26.0
opentelemetry-sdk                        1.26.0
opentelemetry-semantic-conventions       0.47b0
opentelemetry-semantic-conventions-ai    0.4.8
outlines                                 0.1.11
outlines_core                            0.1.26
packaging                                25.0
pandas                                   2.2.3
partial-json-parser                      0.2.1.1.post5
pathlib2                                 2.3.7.post1
pillow                                   11.2.1
pip                                      25.1
prometheus_client                        0.21.1
prometheus-fastapi-instrumentator        7.1.0
propcache                                0.3.1
protobuf                                 4.25.7
psutil                                   7.0.0
py-cpuinfo                               9.0.0
pyarrow                                  20.0.0
pybind11                                 2.13.6
pycountry                                24.6.1
pycparser                                2.22
pydantic                                 2.11.4
pydantic_core                            2.33.2
Pygments                                 2.19.1
python-dateutil                          2.9.0.post0
python-dotenv                            1.1.0
python-json-logger                       3.3.0
python-multipart                         0.0.20
pytz                                     2025.2
PyYAML                                   6.0.2
pyzmq                                    26.4.0
referencing                              0.36.2
regex                                    2024.11.6
requests                                 2.32.3
rich                                     14.0.0
rich-toolkit                             0.14.6
rpds-py                                  0.24.0
safetensors                              0.5.3
schedule_search                          0.0.1
scipy                                    1.13.1
sentencepiece                            0.2.0
setuptools                               78.1.1
setuptools-scm                           8.3.1
shellingham                              1.5.4
show_kernel_debug_data                   0.1.0
six                                      1.17.0
sniffio                                  1.3.1
starlette                                0.46.2
sympy                                    1.13.1
te                                       0.4.0
tiktoken                                 0.9.0
tokenizers                               0.21.1
tomli                                    2.2.1
torch                                    2.5.1
torch-npu                                2.5.1
torchaudio                               2.6.0
torchvision                              0.20.1
tqdm                                     4.67.1
transformers                             4.51.3
typer                                    0.15.3
typing_extensions                        4.13.2
typing-inspection                        0.4.0
tzdata                                   2025.2
urllib3                                  2.4.0
uvicorn                                  0.34.2
uvloop                                   0.21.0
vllm                                     0.8.5.post1
vllm_ascend                              0.7.3
watchfiles                               1.0.5
websockets                               15.0.1
wheel                                    0.45.1
wrapt                                    1.17.2
xgrammar                                 0.1.18
xxhash                                   3.5.0
yarl                                     1.20.0
zipp                                     3.21.0
```
运行测试脚本时，import LLM出错，错误信息如下：
```
INFO 05-13 19:24:03 [importing.py:17] Triton not installed or not compatible; certain GPU-related functions will not be available.
WARNING 05-13 19:24:03 [importing.py:28] Triton is not installed. Using dummy decorators. Install it via `pip install triton` to enable kernelcompilation.
INFO 05-13 19:24:03 [importing.py:53] Triton module has been replaced with a placeholder.
INFO 05-13 19:24:04 [__init__.py:30] Available plugins for group vllm.platform_plugins:
INFO 05-13 19:24:04 [__init__.py:32] name=ascend, value=vllm_ascend:register
INFO 05-13 19:24:04 [__init__.py:34] all available plugins for group vllm.platform_plugins will be loaded.
INFO 05-13 19:24:04 [__init__.py:36] set environment variable VLLM_PLUGINS to control which plugins to load.
INFO 05-13 19:24:04 [__init__.py:44] plugin ascend loaded.
INFO 05-13 19:24:04 [__init__.py:230] Platform plugin ascend is activated
Traceback (most recent call last):
  File "/data/mjy/Cronus/cronus/test/tp-infer/demo.py", line 1, in <module>
    from vllm import LLM, SamplingParams
  File "/root/miniconda3/envs/cronus_vllm/lib/python3.9/site-packages/vllm/__init__.py", line 12, in <module>
    from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs
  File "/root/miniconda3/envs/cronus_vllm/lib/python3.9/site-packages/vllm/engine/arg_utils.py", line 18, in <module>
    from vllm.config import (BlockSize, CacheConfig, CacheDType, CompilationConfig,
  File "/root/miniconda3/envs/cronus_vllm/lib/python3.9/site-packages/vllm/config.py", line 30, in <module>
    from vllm.model_executor.layers.quantization import (QUANTIZATION_METHODS,
  File "/root/miniconda3/envs/cronus_vllm/lib/python3.9/site-packages/vllm/model_executor/__init__.py", line 3, in <module>
    from vllm.model_executor.parameter import (BasevLLMParameter,
  File "/root/miniconda3/envs/cronus_vllm/lib/python3.9/site-packages/vllm/model_executor/parameter.py", line 9, in <module>
    from vllm.distributed import get_tensor_model_parallel_rank
  File "/root/miniconda3/envs/cronus_vllm/lib/python3.9/site-packages/vllm/distributed/__init__.py", line 3, in <module>
    from .communication_op import *
  File "/root/miniconda3/envs/cronus_vllm/lib/python3.9/site-packages/vllm/distributed/communication_op.py", line 8, in <module>
    from .parallel_state import get_tp_group
  File "/root/miniconda3/envs/cronus_vllm/lib/python3.9/site-packages/vllm/distributed/parallel_state.py", line 149, in <module>
    from vllm.platforms import current_platform
  File "/root/miniconda3/envs/cronus_vllm/lib/python3.9/site-packages/vllm/platforms/__init__.py", line 271, in __getattr__
    _current_platform = resolve_obj_by_qualname(
  File "/root/miniconda3/envs/cronus_vllm/lib/python3.9/site-packages/vllm/utils.py", line 2087, in resolve_obj_by_qualname
    module = importlib.import_module(module_name)
  File "/root/miniconda3/envs/cronus_vllm/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "/root/miniconda3/envs/cronus_vllm/lib/python3.9/site-packages/vllm_ascend/platform.py", line 25, in <module>
    from vllm.config import CompilationLevel, VllmConfig
ImportError: cannot import name 'CompilationLevel' from partially initialized module 'vllm.config' (most likely due to a circular import) (/root/miniconda3/envs/cronus_vllm/lib/python3.9/site-packages/vllm/config.py)
[ERROR] 2025-05-13-19:24:04 (PID:2650070, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```
