# Issue #4621: [Installation]: 安装vllm-ascend0.11.0rc1报错

## 基本信息

- **编号**: #4621
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4621
- **创建时间**: 2025-12-02T06:36:32Z
- **关闭时间**: 2025-12-16T06:13:41Z
- **更新时间**: 2025-12-16T06:13:41Z
- **提交者**: @Guozhong23
- **评论数**: 4

## 标签

installation

## 问题描述

### Your current environment

A+X的A2
+------------------------------------------------------------------------------------------------+
| npu-smi 25.0.rc1.1               Version: 25.0.rc1.1                                           |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B2C              | OK            | 88.3        34                0    / 0             |
| 0                         | 0000:5A:00.0  | 0           0    / 0          3406 / 65536         |
+===========================+===============+====================================================+

cann包版本：
package_name=Ascend-cann-toolkit
version=8.3.RC2
innerversion=V100R001C23SPC002B210
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=x86_64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.3.RC2/x86_64-linux

当前环境中的依赖包：
Package                           Version                                   Editable project location
--------------------------------- ----------------------------------------- ---------------------------
absl-py                           2.3.1
aiofiles                          24.1.0
aiohappyeyeballs                  2.6.1
aiohttp                           3.12.15
aiosignal                         1.4.0
annotated-types                   0.7.0
anyio                             4.10.0
asc_opc_tool                      0.1.0
astor                             0.8.1
attrs                             25.3.0
auto_tune                         0.1.0
blake3                            1.0.6
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
fastapi                           0.116.2
fastapi-cli                       0.0.12
fastapi-cloud-cli                 0.2.0
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
huggingface-hub                   0.35.0
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
llm_datadist_v1                   0.0.1
llvmlite                          0.45.0
lm-format-enforcer                0.11.3
markdown-it-py                    4.0.0
MarkupSafe                        3.0.2
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
numba                             0.62.0
numpy                             1.26.4
op_compile_tool                   0.1.0
op_gen                            0.1
op_test_frame                     0.1
opc_tool                          0.1.0
openai                            1.108.0
openai-harmony                    0.0.4
opencv-python-headless            4.11.0.86
outlines_core                     0.2.11
packaging                         25.0
pandas                            2.3.3
pandas-stubs                      2.3.2.250926
partial-json-parser               0.2.1.1.post6
pathlib2                          2.3.7.post1
pillow                            11.3.0
pip                               25.3
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
python-dateutil                   2.9.0.post0
python-dotenv                     1.1.1
python-json-logger                3.3.0
python-multipart                  0.0.20
pytz                              2025.2
PyYAML                            6.0.2
pyzmq                             27.1.0
Quart                             0.20.0
ray                               2.49.1
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
sentry-sdk                        2.38.0
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
tokenizers                        0.22.0
torch                             2.7.1+cpu
torch_npu                         2.7.1
torchvision                       0.22.1+cpu
tqdm                              4.67.1
transformers                      4.56.1
triton-ascend                     3.2.0.dev20250916
typer                             0.17.4
types-pytz                        2025.2.0.20251108
typing_extensions                 4.15.0
typing-inspection                 0.4.1
tzdata                            2025.2
urllib3                           2.5.0
uvicorn                           0.35.0
uvloop                            0.21.0
vllm                              0.11.1rc6.dev0+g2918c1b49.d20251127.empty /vllm-workspace/vllm
vllm-ascend                       0.11.0rc1.dev356+ge98543267.d20251202     /vllm-workspace/vllm-ascend
watchfiles                        1.1.0
websockets                        15.0.1
Werkzeug                          3.1.3
wheel                             0.45.1
wsproto                           1.2.0
xgrammar                          0.1.23
yarl                              1.20.1


### How you are installing vllm and vllm-ascend

下列两个安装指令可以成功安装vllm-ascend，但是无法使能图模式：
“pip install -e . --no-deps --no-build-isolation”
“pip install -e . --no-build-isolation”

听从建议，使用下列指令安装vllm-ascend，但是安装失败：
“pip install -e .”
报错如下：

  Given no hashes to check 0 links for project 'torch': discarding no candidates
  INFO: pip is looking at multiple versions of torch-npu to determine which version is compatible with other requirements. This could take a while.
  Will try a different candidate, due to conflict:
      The user requested torch==2.7.1
      torch-npu 2.7.1 depends on torch==2.7.1+cpu
  ERROR: Cannot install torch-npu==2.7.1 and torch==2.7.1 because these package versions have conflicting dependencies.

  The conflict is caused by:
      The user requested torch==2.7.1
      torch-npu 2.7.1 depends on torch==2.7.1+cpu

  Additionally, some packages in these conflicts have no matching distributions available for your environment:
      torch

  To fix this you could try to:
  1. loosen the range of package versions you've specified
  2. remove package versions to allow pip to attempt to solve the dependency conflict

  ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts
  Exception information:
  Traceback (most recent call last):
    File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/resolver.py", line 99, in resolve
      result = self._result = resolver.resolve(
                              ^^^^^^^^^^^^^^^^^
    File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_vendor/resolvelib/resolvers/resolution.py", line 601, in resolve
      state = resolution.resolve(requirements, max_rounds=max_rounds)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_vendor/resolvelib/resolvers/resolution.py", line 542, in resolve
      raise ResolutionImpossible(self.state.backtrack_causes)
  pip._vendor.resolvelib.resolvers.exceptions.ResolutionImpossible: [RequirementInformation(requirement=SpecifierRequirement('torch==2.7.1'), parent=None), RequirementInformation(requirement=SpecifierRequirement('torch==2.7.1+cpu'), parent=LinkCandidate('https://files.pythonhosted.org/packages/b4/2b/eaf823aec1e273cd5826e0ba3351510d292a14508467b14d6c467c4fbc3c/torch_npu-2.7.1-cp311-cp311-manylinux_2_28_x86_64.whl (from https://pypi.org/simple/torch-npu/)'))]

  The above exception was the direct cause of the following exception:

  Traceback (most recent call last):
    File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/cli/base_command.py", line 107, in _run_wrapper
      status = _inner_run()
               ^^^^^^^^^^^^
    File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/cli/base_command.py", line 98, in _inner_run
      return self.run(options, args)
             ^^^^^^^^^^^^^^^^^^^^^^^
    File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/cli/req_command.py", line 85, in wrapper
      return func(self, options, args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/commands/install.py", line 388, in run
      requirement_set = resolver.resolve(
                        ^^^^^^^^^^^^^^^^^
    File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/resolver.py", line 108, in resolve
      raise error from e
  pip._internal.exceptions.DistributionNotFound: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts
  Removed build tracker: '/tmp/pip-build-tracker-lx33qk6l'
  error: subprocess-exited-with-error

  × installing build dependencies did not run successfully.
  │ exit code: 1
  ╰─> No available output.

  note: This error originates from a subprocess, and is likely not a problem with pip.
  full command: /usr/local/python3.11.13/bin/python3.11 /usr/local/python3.11.13/lib/python3.11/site-packages/pip/__pip-runner__.py install --ignore-installed --no-user --prefix /tmp/pip-build-env-40crz8av/overlay --no-warn-script-location --disable-pip-version-check --no-compile --target '' -vv --no-binary :none: --only-binary :none: -i https://pypi.org/simple -- 'cmake>=3.26' decorator einops 'numpy<2.0.0' packaging pip pybind11 pyyaml scipy pandas pandas-stubs 'setuptools>=64' 'setuptools-scm>=8' torch-npu==2.7.1 torch==2.7.1 torchvision wheel msgpack quart numba 'opencv-python-headless<=4.11.0.86'
  cwd: [inherit]
  Installing build dependencies ... error
Remote version of pip: 25.3
Local version of pip:  25.3
Was pip installed by pip? True
ERROR: Failed to build 'file:///vllm-workspace/vllm-ascend' when installing build dependencies
Exception information:
Traceback (most recent call last):
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/candidates.py", line 238, in _prepare
    dist = self._prepare_distribution()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/candidates.py", line 353, in _prepare_distribution
    return self._factory.preparer.prepare_editable_requirement(self._ireq)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/operations/prepare.py", line 714, in prepare_editable_requirement
    dist = _get_prepared_distribution(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/operations/prepare.py", line 77, in _get_prepared_distribution
    abstract_dist.prepare_distribution_metadata(
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/distributions/sdist.py", line 48, in prepare_distribution_metadata
    self._prepare_build_backend(build_env_installer)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/distributions/sdist.py", line 82, in _prepare_build_backend
    self.req.build_env.install_requirements(
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/build_env.py", line 386, in install_requirements
    self.installer.install(requirements, prefix, kind=kind, for_req=for_req)
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/build_env.py", line 240, in install
    call_subprocess(
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/utils/subprocess.py", line 212, in call_subprocess
    raise error
pip._internal.exceptions.InstallationSubprocessError: installing build dependencies exited with 1

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/cli/base_command.py", line 107, in _run_wrapper
    status = _inner_run()
             ^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/cli/base_command.py", line 98, in _inner_run
    return self.run(options, args)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/cli/req_command.py", line 85, in wrapper
    return func(self, options, args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/commands/install.py", line 388, in run
    requirement_set = resolver.resolve(
                      ^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/resolver.py", line 79, in resolve
    collected = self.factory.collect_root_requirements(root_reqs)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/factory.py", line 538, in collect_root_requirements
    reqs = list(
           ^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/factory.py", line 494, in _make_requirements_from_install_req
    cand = self._make_base_candidate_from_link(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/factory.py", line 205, in _make_base_candidate_from_link
    self._editable_candidate_cache[link] = EditableCandidate(
                                           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/candidates.py", line 343, in __init__
    super().__init__(
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/candidates.py", line 161, in __init__
    self.dist = self._prepare()
                ^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/pip/_internal/resolution/resolvelib/candidates.py", line 254, in _prepare
    raise FailedToPrepareCandidate(
pip._internal.exceptions.FailedToPrepareCandidate: Failed to build 'file:///vllm-workspace/vllm-ascend' when installing build dependencies
Removed file:///vllm-workspace/vllm-ascend from build tracker '/tmp/pip-build-tracker-lx33qk6l'
Removed build tracker: '/tmp/pip-build-tracker-lx33qk6l'

[install_error.log](https://github.com/user-attachments/files/23874187/install_error.log)

