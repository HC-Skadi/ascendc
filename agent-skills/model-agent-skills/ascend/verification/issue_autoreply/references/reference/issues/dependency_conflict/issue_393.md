# Issue #393: [Bug]: RuntimeError: setup failed!

## 基本信息

- **编号**: #393
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/393
- **创建时间**: 2025-03-25T12:14:49Z
- **关闭时间**: 2025-05-14T02:53:42Z
- **更新时间**: 2025-05-14T02:53:43Z
- **提交者**: @ShuhangChen1207
- **评论数**: 8

## 标签

bug

## 问题描述

### Your current environment

absl-py                           2.1.0
accelerate                        1.5.2
addict                            2.4.0
aiofiles                          23.2.1
aiohappyeyeballs                  2.6.1
aiohttp                           3.11.14
aiosignal                         1.3.2
airportsdata                      20250224
aliyun-python-sdk-core            2.16.0
aliyun-python-sdk-kms             2.16.5
annotated-types                   0.7.0
antlr4-python3-runtime            4.13.2
anyio                             4.9.0
astor                             0.8.1
async-timeout                     5.0.1
attrdict                          2.0.1
attrs                             25.1.0
auto_tune                         0.1.0
binpacking                        1.5.2
blake3                            1.0.4
certifi                           2025.1.31
cffi                              1.17.1
charset-normalizer                3.4.1
click                             8.1.8
cloudpickle                       3.1.1
compressed-tensors                0.9.1
contourpy                         1.3.1
cpm-kernels                       1.0.11
crcmod                            1.7
cryptography                      44.0.2
cycler                            0.12.1
Cython                            3.0.12
dacite                            1.9.2
dataflow                          0.0.1
datasets                          3.2.0
decorator                         5.1.1
deepspeed                         0.14.5
depyf                             0.18.0
dill                              0.3.8
diskcache                         5.6.3
distro                            1.9.0
dnspython                         2.7.0
einops                            0.8.1
email_validator                   2.2.0
exceptiongroup                    1.2.2
fastapi                           0.115.12
fastapi-cli                       0.0.7
ffmpy                             0.5.0
filelock                          3.18.0
fonttools                         4.56.0
frozenlist                        1.5.0
fsspec                            2024.9.0
future                            1.0.0
gguf                              0.10.0
gradio                            5.23.0
gradio_client                     1.8.0
groovy                            0.1.2
grpcio                            1.71.0
h11                               0.14.0
hccl                              0.1.0
hccl_parser                       0.1
hjson                             3.1.0
httpcore                          1.0.7
httptools                         0.6.4
httpx                             0.28.1
huggingface-hub                   0.29.3
idna                              3.10
importlib_metadata                8.6.1
interegular                       0.3.3
jieba                             0.42.1
Jinja2                            3.1.6
jiter                             0.9.0
jmespath                          0.10.0
joblib                            1.4.2
jsonschema                        4.23.0
jsonschema-specifications         2024.10.1
kiwisolver                        1.4.8
lark                              1.2.2
latex2sympy2_extended             1.10.1
llm_datadist                      0.0.1
llvmlite                          0.43.0
lm-format-enforcer                0.10.11
Markdown                          3.7
markdown-it-py                    3.0.0
MarkupSafe                        3.0.2
math-verify                       0.7.0
matplotlib                        3.10.1
mdurl                             0.1.2
mistral_common                    1.5.4
ml_dtypes                         0.5.1
modelscope                        1.24.0
mpmath                            1.3.0
ms_swift                          3.2.1
msgspec                           0.19.0
msobjdump                         0.1.0
multidict                         6.2.0
multiprocess                      0.70.16
nest-asyncio                      1.6.0
networkx                          3.4.2
ninja                             1.11.1.4
nltk                              3.9.1
numba                             0.60.0
numpy                             1.26.4
nvidia-ml-py                      12.570.86
op_compile_tool                   0.1.0
op_gen                            0.1
op_test_frame                     0.1
opc_tool                          0.1.0
openai                            1.68.2
opencv-python-headless            4.11.0.86
orjson                            3.10.16
oss2                              2.19.1
outlines                          0.1.11
outlines_core                     0.1.26
packaging                         24.2
pandas                            2.2.3
partial-json-parser               0.2.1.1.post5
pathlib2                          2.3.7.post1
peft                              0.14.0
pillow                            11.1.0
pip                               25.0.1
prometheus_client                 0.21.1
prometheus-fastapi-instrumentator 7.1.0
propcache                         0.3.0
protobuf                          3.20.0
psutil                            7.0.0
py-cpuinfo                        9.0.0
pyarrow                           19.0.1
pycountry                         24.6.1
pycparser                         2.22
pycryptodome                      3.22.0
pydantic                          2.10.6
pydantic_core                     2.27.2
pydub                             0.25.1
Pygments                          2.19.1
pyparsing                         3.2.2
python-dateutil                   2.9.0.post0
python-dotenv                     1.0.1
python-multipart                  0.0.20
pytz                              2025.1
PyYAML                            6.0.2
pyzmq                             26.3.0
referencing                       0.36.2
regex                             2024.11.6
requests                          2.32.3
rich                              13.9.4
rich-toolkit                      0.13.2
rouge                             1.0.1
rpds-py                           0.23.1
ruff                              0.11.2
safehttpx                         0.1.6
safetensors                       0.5.3
schedule_search                   0.0.1
scipy                             1.15.2
semantic-version                  2.10.0
sentencepiece                     0.2.0
setuptools                        69.5.1
setuptools-scm                    8.2.0
shellingham                       1.5.4
show_kernel_debug_data            0.1.0
simplejson                        3.20.1
six                               1.17.0
sniffio                           1.3.1
sortedcontainers                  2.4.0
starlette                         0.46.1
sympy                             1.13.1
te                                0.4.0
tensorboard                       2.19.0
tensorboard-data-server           0.7.2
tiktoken                          0.9.0
tokenizers                        0.21.1
tomli                             2.2.1
tomlkit                           0.13.2
torch                             2.5.1
torch-npu                         2.5.1.dev20250308
torchaudio                        2.5.1
torchvision                       0.20.1
tornado                           6.4.2
tqdm                              4.67.1
transformers                      4.50.0
transformers-stream-generator     0.0.5
trl                               0.16.0
typer                             0.15.2
typing_extensions                 4.12.2
tzdata                            2025.2
urllib3                           2.3.0
uvicorn                           0.34.0
uvloop                            0.21.0
vllm                              0.7.3
vllm_ascend                       0.7.3rc1
watchfiles                        1.0.4
websockets                        15.0.1
Werkzeug                          3.1.3
xxhash                            3.5.0
yarl                              1.18.3
zipp                              3.21.0
zstandard                         0.23.0

### 🐛 Describe the bug

{'loss': 3.14e-06, 'grad_norm': 0.00347595, 'learning_rate': 3e-08, 'train_speed(iter/s)': 0.028684, 'completion_length': 74.35416985, 'response_clip_ratio': 0.0, 'rewards/MathFormat': 0.0, 'reward': 0.0, 'reward_std': 0.0, 'kl': 0.00330734, 'clip_ratio': 0.0, 'epoch': 0.0, 'global_step/max_steps': '5/8724', 'percentage': '0.06%', 'elapsed_time': '2m 25s', 'remaining_time': '2d 22h 37m 44s'}
Train:   0%|                                                                                                                                                         | 5/8724 [02:25<69:44:50, 28.80s/it]mki_log log dir:/root/atb/log exist
[rank0]: Traceback (most recent call last):
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/swift/cli/rlhf.py", line 5, in <module>
[rank0]:     rlhf_main()
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/swift/llm/train/rlhf.py", line 96, in rlhf_main
[rank0]:     return SwiftRLHF(args).main()
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/swift/llm/base.py", line 47, in main
[rank0]:     result = self.run()
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/swift/llm/train/sft.py", line 142, in run
[rank0]:     return self.train(trainer)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/swift/llm/train/sft.py", line 204, in train
[rank0]:     trainer.train(trainer.args.resume_from_checkpoint)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/swift/trainers/mixin.py", line 288, in train
[rank0]:     res = super().train(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/transformers/trainer.py", line 2245, in train
[rank0]:     return inner_training_loop(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/transformers/trainer.py", line 2556, in _inner_training_loop
[rank0]:     tr_loss_step = self.training_step(model, inputs, num_items_in_batch)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/transformers/trainer.py", line 3712, in training_step
[rank0]:     inputs = self._prepare_inputs(inputs)
[rank0]:   File "/workspace/trl/extras/profiling.py", line 87, in wrapper
[rank0]:     return func(self, *args, **kwargs)
[rank0]:   File "/workspace/trl/trainer/grpo_trainer.py", line 692, in _prepare_inputs
[rank0]:     inputs = self._generate_and_score_completions(inputs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/swift/trainers/rlhf_trainer/grpo_trainer.py", line 700, in _generate_and_score_completions
[rank0]:     inputs, outputs = self._fast_infer(inputs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/swift/trainers/rlhf_trainer/grpo_trainer.py", line 659, in _fast_infer
[rank0]:     outputs = self.engine.infer(_input_slice, self.request_config, use_tqdm=False)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/swift/llm/infer/infer_engine/vllm_engine.py", line 422, in infer
[rank0]:     step_outputs = self.engine.step()
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 1391, in step
[rank0]:     outputs = self.model_executor.execute_model(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 139, in execute_model
[rank0]:     output = self.collective_rpc("execute_model",
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc
[rank0]:     answer = run_method(self.driver_worker, method, args, kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 2196, in run_method
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 420, in execute_model
[rank0]:     output = self.model_runner.execute_model(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/worker/model_runner.py", line 1140, in execute_model
[rank0]:     hidden_or_intermediate_states = model_executable(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 486, in forward
[rank0]:     hidden_states = self.model(input_ids, positions, kv_caches,
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/compilation/decorators.py", line 172, in __call__
[rank0]:     return self.forward(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 348, in forward
[rank0]:     hidden_states, residual = layer(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 247, in forward
[rank0]:     hidden_states = self.self_attn(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 179, in forward
[rank0]:     attn_output = self.attn(q, k, v, kv_cache, attn_metadata)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
[rank0]:     return self._call_impl(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
[rank0]:     return forward_call(*args, **kwargs)
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm/attention/layer.py", line 198, in forward
[rank0]:     return self.impl.forward(self, query, key, value,
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/vllm_ascend/attention.py", line 869, in forward
[rank0]:     torch_npu._npu_flash_attention_qlens(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/torch/_ops.py", line 1116, in __call__
[rank0]:     return self._op(*args, **(kwargs or {}))
[rank0]: RuntimeError: setup failed!
