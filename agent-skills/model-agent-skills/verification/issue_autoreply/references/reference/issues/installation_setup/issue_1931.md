# Issue #1931: [Installation]: pybind cmake

## 基本信息

- **编号**: #1931
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1931
- **创建时间**: 2025-07-22T07:39:25Z
- **关闭时间**: 2025-07-28T03:20:59Z
- **更新时间**: 2025-07-28T03:20:59Z
- **提交者**: @NivinaNull
- **评论数**: 2

## 标签

installation

## 问题描述

### Your current environment

```text
npu-dirver : 24.1.rc2.1
CANN docker: 8.1.rc1-310p-ubuntu22.04-py3.10
torch-npu:2.5.1
python:3.10
cmake:4.0.3
pybind:3.0.0
```


### How you are installing vllm and vllm-ascend

```sh
pip install  vllm-ascend 
```
got the following error
'''Collecting vllm-ascend==0.8.5.rc1
  Downloading https://mirrors.aliyun.com/pypi/packages/a1/b1/a279964fc53e7059b1ae93981118e676dfebbf09177b709f9189b2fd1e99/vllm_ascend-0.8.5rc1.tar.gz (536 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.0/536.0 kB 1.2 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: cmake>=3.26 in /usr/local/python3.10.17/lib/python3.10/site-packages (from vllm-ascend==0.8.5.rc1) (4.0.3)
Requirement already satisfied: decorator in /usr/local/python3.10.17/lib/python3.10/site-packages (from vllm-ascend==0.8.5.rc1) (5.2.1)
Requirement already satisfied: numpy<2.0.0 in /usr/local/python3.10.17/lib/python3.10/site-packages (from vllm-ascend==0.8.5.rc1) (1.26.4)
Requirement already satisfied: packaging in /usr/local/python3.10.17/lib/python3.10/site-packages (from vllm-ascend==0.8.5.rc1) (25.0)
Requirement already satisfied: pip in /usr/local/python3.10.17/lib/python3.10/site-packages (from vllm-ascend==0.8.5.rc1) (25.1.1)
Requirement already satisfied: pybind11 in /usr/local/python3.10.17/lib/python3.10/site-packages (from vllm-ascend==0.8.5.rc1) (3.0.0)
Requirement already satisfied: pyyaml in /usr/local/python3.10.17/lib/python3.10/site-packages (from vllm-ascend==0.8.5.rc1) (6.0.2)
Requirement already satisfied: scipy in /usr/local/python3.10.17/lib/python3.10/site-packages (from vllm-ascend==0.8.5.rc1) (1.15.3)
Requirement already satisfied: setuptools>=64 in /usr/local/python3.10.17/lib/python3.10/site-packages (from vllm-ascend==0.8.5.rc1) (80.9.0)
Collecting setuptools-scm>=8 (from vllm-ascend==0.8.5.rc1)
  Using cached https://mirrors.aliyun.com/pypi/packages/ab/ac/8f96ba9b4cfe3e4ea201f23f4f97165862395e9331a424ed325ae37024a8/setuptools_scm-8.3.1-py3-none-any.whl (43 kB)
Requirement already satisfied: torch-npu==2.5.1 in /usr/local/python3.10.17/lib/python3.10/site-packages (from vllm-ascend==0.8.5.rc1) (2.5.1)
Requirement already satisfied: torch>=2.5.1 in /usr/local/python3.10.17/lib/python3.10/site-packages (from vllm-ascend==0.8.5.rc1) (2.5.1)
Requirement already satisfied: torchvision<0.21.0 in /usr/local/python3.10.17/lib/python3.10/site-packages (from vllm-ascend==0.8.5.rc1) (0.20.1)
Requirement already satisfied: wheel in /usr/local/python3.10.17/lib/python3.10/site-packages (from vllm-ascend==0.8.5.rc1) (0.45.1)
Requirement already satisfied: msgpack in /usr/local/python3.10.17/lib/python3.10/site-packages (from vllm-ascend==0.8.5.rc1) (1.1.1)
Collecting quart (from vllm-ascend==0.8.5.rc1)
  Downloading https://mirrors.aliyun.com/pypi/packages/7e/e9/cc28f21f52913adf333f653b9e0a3bf9cb223f5083a26422968ba73edd8d/quart-0.20.0-py3-none-any.whl (77 kB)
Requirement already satisfied: filelock in /usr/local/python3.10.17/lib/python3.10/site-packages (from torch>=2.5.1->vllm-ascend==0.8.5.rc1) (3.18.0)
Requirement already satisfied: typing-extensions>=4.8.0 in /usr/local/python3.10.17/lib/python3.10/site-packages (from torch>=2.5.1->vllm-ascend==0.8.5.rc1) (4.14.1)
Requirement already satisfied: networkx in /usr/local/python3.10.17/lib/python3.10/site-packages (from torch>=2.5.1->vllm-ascend==0.8.5.rc1) (3.4.2)
Requirement already satisfied: jinja2 in /usr/local/python3.10.17/lib/python3.10/site-packages (from torch>=2.5.1->vllm-ascend==0.8.5.rc1) (3.1.6)
Requirement already satisfied: fsspec in /usr/local/python3.10.17/lib/python3.10/site-packages (from torch>=2.5.1->vllm-ascend==0.8.5.rc1) (2024.12.0)
Requirement already satisfied: sympy==1.13.1 in /usr/local/python3.10.17/lib/python3.10/site-packages (from torch>=2.5.1->vllm-ascend==0.8.5.rc1) (1.13.1)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/python3.10.17/lib/python3.10/site-packages (from sympy==1.13.1->torch>=2.5.1->vllm-ascend==0.8.5.rc1) (1.3.0)
Requirement already satisfied: pillow!=8.3.*,>=5.3.0 in /usr/local/python3.10.17/lib/python3.10/site-packages (from torchvision<0.21.0->vllm-ascend==0.8.5.rc1) (11.3.0)
Collecting tomli>=1 (from setuptools-scm>=8->vllm-ascend==0.8.5.rc1)
  Using cached https://mirrors.aliyun.com/pypi/packages/6e/c2/61d3e0f47e2b74ef40a68b9e6ad5984f6241a942f7cd3bbfbdbd03861ea9/tomli-2.2.1-py3-none-any.whl (14 kB)
Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/python3.10.17/lib/python3.10/site-packages (from jinja2->torch>=2.5.1->vllm-ascend==0.8.5.rc1) (3.0.2)
Collecting aiofiles (from quart->vllm-ascend==0.8.5.rc1)
  Downloading https://mirrors.aliyun.com/pypi/packages/a5/45/30bb92d442636f570cb5651bc661f52b610e2eec3f891a5dc3a4c3667db0/aiofiles-24.1.0-py3-none-any.whl (15 kB)
Collecting blinker>=1.6 (from quart->vllm-ascend==0.8.5.rc1)
  Downloading https://mirrors.aliyun.com/pypi/packages/10/cb/f2ad4230dc2eb1a74edf38f1a38b9b52277f75bef262d8908e60d957e13c/blinker-1.9.0-py3-none-any.whl (8.5 kB)
Requirement already satisfied: click>=8.0 in /usr/local/python3.10.17/lib/python3.10/site-packages (from quart->vllm-ascend==0.8.5.rc1) (8.2.1)
Collecting flask>=3.0 (from quart->vllm-ascend==0.8.5.rc1)
  Downloading https://mirrors.aliyun.com/pypi/packages/3d/68/9d4508e893976286d2ead7f8f571314af6c2037af34853a30fd769c02e9d/flask-3.1.1-py3-none-any.whl (103 kB)
Collecting hypercorn>=0.11.2 (from quart->vllm-ascend==0.8.5.rc1)
  Downloading https://mirrors.aliyun.com/pypi/packages/0e/3b/dfa13a8d96aa24e40ea74a975a9906cfdc2ab2f4e3b498862a57052f04eb/hypercorn-0.17.3-py3-none-any.whl (61 kB)
Collecting itsdangerous (from quart->vllm-ascend==0.8.5.rc1)
  Downloading https://mirrors.aliyun.com/pypi/packages/04/96/92447566d16df59b2a776c0fb82dbc4d9e07cd95062562af01e408583fc4/itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Collecting werkzeug>=3.0 (from quart->vllm-ascend==0.8.5.rc1)
  Downloading https://mirrors.aliyun.com/pypi/packages/52/24/ab44c871b0f07f491e5d2ad12c9bd7358e527510618cb1b803a88e986db1/werkzeug-3.1.3-py3-none-any.whl (224 kB)
Collecting exceptiongroup>=1.1.0 (from hypercorn>=0.11.2->quart->vllm-ascend==0.8.5.rc1)
  Downloading https://mirrors.aliyun.com/pypi/packages/36/f4/c6e662dade71f56cd2f3735141b265c3c79293c109549c1e6933b0651ffc/exceptiongroup-1.3.0-py3-none-any.whl (16 kB)
Collecting h11 (from hypercorn>=0.11.2->quart->vllm-ascend==0.8.5.rc1)
  Downloading https://mirrors.aliyun.com/pypi/packages/04/4b/29cac41a4d98d144bf5f6d33995617b185d14b22401f75ca86f384e87ff1/h11-0.16.0-py3-none-any.whl (37 kB)
Collecting h2>=3.1.0 (from hypercorn>=0.11.2->quart->vllm-ascend==0.8.5.rc1)
  Downloading https://mirrors.aliyun.com/pypi/packages/d0/9e/984486f2d0a0bd2b024bf4bc1c62688fcafa9e61991f041fb0e2def4a982/h2-4.2.0-py3-none-any.whl (60 kB)
Collecting priority (from hypercorn>=0.11.2->quart->vllm-ascend==0.8.5.rc1)
  Downloading https://mirrors.aliyun.com/pypi/packages/5e/5f/82c8074f7e84978129347c2c6ec8b6c59f3584ff1a20bc3c940a3e061790/priority-2.0.0-py3-none-any.whl (8.9 kB)
Collecting taskgroup (from hypercorn>=0.11.2->quart->vllm-ascend==0.8.5.rc1)
  Downloading https://mirrors.aliyun.com/pypi/packages/d1/b1/74babcc824a57904e919f3af16d86c08b524c0691504baf038ef2d7f655c/taskgroup-0.2.2-py2.py3-none-any.whl (14 kB)
Collecting wsproto>=0.14.0 (from hypercorn>=0.11.2->quart->vllm-ascend==0.8.5.rc1)
  Downloading https://mirrors.aliyun.com/pypi/packages/78/58/e860788190eba3bcce367f74d29c4675466ce8dddfba85f7827588416f01/wsproto-1.2.0-py3-none-any.whl (24 kB)
Collecting hyperframe<7,>=6.1 (from h2>=3.1.0->hypercorn>=0.11.2->quart->vllm-ascend==0.8.5.rc1)
  Downloading https://mirrors.aliyun.com/pypi/packages/48/30/47d0bf6072f7252e6521f3447ccfa40b421b6824517f82854703d0f5a98b/hyperframe-6.1.0-py3-none-any.whl (13 kB)
Collecting hpack<5,>=4.1 (from h2>=3.1.0->hypercorn>=0.11.2->quart->vllm-ascend==0.8.5.rc1)
  Downloading https://mirrors.aliyun.com/pypi/packages/07/c6/80c95b1b2b94682a72cbdbfb85b81ae2daffa4291fbfa1b1464502ede10d/hpack-4.1.0-py3-none-any.whl (34 kB)
Building wheels for collected packages: vllm-ascend
  Building wheel for vllm-ascend (pyproject.toml) ... error
  error: subprocess-exited-with-error
  
  × Building wheel for vllm-ascend (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [180 lines of output]
      /tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/dist.py:759: SetuptoolsDeprecationWarning: License classifiers are deprecated.
      !!
      
              ********************************************************************************
              Please consider removing the following classifiers in favor of a SPDX license expression:
      
              License :: OSI Approved :: Apache Software License
      
              See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
              ********************************************************************************
      
      !!
        self._finalize_license_expression()
      running bdist_wheel
      running build
      running build_py
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend
      copying vllm_ascend/envs.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend
      copying vllm_ascend/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend
      copying vllm_ascend/_version.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend
      copying vllm_ascend/platform.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend
      copying vllm_ascend/utils.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/quantization
      copying vllm_ascend/quantization/w8a8.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/quantization
      copying vllm_ascend/quantization/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/quantization
      copying vllm_ascend/quantization/func_wrapper.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/quantization
      copying vllm_ascend/quantization/w8a8_dynamic.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/quantization
      copying vllm_ascend/quantization/quant_config.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/quantization
      copying vllm_ascend/quantization/quantizer.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/quantization
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/attention
      copying vllm_ascend/attention/mla_v1.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/attention
      copying vllm_ascend/attention/attention_v1.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/attention
      copying vllm_ascend/attention/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/attention
      copying vllm_ascend/attention/attention.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/attention
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/distributed
      copying vllm_ascend/distributed/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/distributed
      copying vllm_ascend/distributed/communicator.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/distributed
      copying vllm_ascend/distributed/parallel_state.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/distributed
      copying vllm_ascend/distributed/llmdatadist_connector.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/distributed
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/models
      copying vllm_ascend/models/deepseek_mtp.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/models
      copying vllm_ascend/models/qwen2_vl.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/models
      copying vllm_ascend/models/qwen2_5_vl.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/models
      copying vllm_ascend/models/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/models
      copying vllm_ascend/models/deepseek_v2.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/models
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/device_allocator
      copying vllm_ascend/device_allocator/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/device_allocator
      copying vllm_ascend/device_allocator/camem.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/device_allocator
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/ops
      copying vllm_ascend/ops/rotary_embedding.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/ops
      copying vllm_ascend/ops/activation.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/ops
      copying vllm_ascend/ops/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/ops
      copying vllm_ascend/ops/fused_moe.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/ops
      copying vllm_ascend/ops/cache.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/ops
      copying vllm_ascend/ops/common_fused_moe.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/ops
      copying vllm_ascend/ops/layernorm.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/ops
      copying vllm_ascend/ops/vocab_parallel_embedding.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/ops
      copying vllm_ascend/ops/attention.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/ops
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/patch
      copying vllm_ascend/patch/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/patch
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/core
      copying vllm_ascend/core/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/core
      copying vllm_ascend/core/scheduler.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/core
      copying vllm_ascend/core/schedule_config.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/core
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/lora
      copying vllm_ascend/lora/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/lora
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/worker
      copying vllm_ascend/worker/model_runner.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/worker
      copying vllm_ascend/worker/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/worker
      copying vllm_ascend/worker/multi_step_worker.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/worker
      copying vllm_ascend/worker/draft_model_runner.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/worker
      copying vllm_ascend/worker/pooling_model_runner.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/worker
      copying vllm_ascend/worker/multi_step_runner.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/worker
      copying vllm_ascend/worker/cache_engine.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/worker
      copying vllm_ascend/worker/model_runner_v1.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/worker
      copying vllm_ascend/worker/worker_v1.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/worker
      copying vllm_ascend/worker/worker.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/worker
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/distributed/device_communicators
      copying vllm_ascend/distributed/device_communicators/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/distributed/device_communicators
      copying vllm_ascend/distributed/device_communicators/pyhccl_wrapper.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/distributed/device_communicators
      copying vllm_ascend/distributed/device_communicators/pyhccl.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/distributed/device_communicators
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/distributed/kv_transfer
      copying vllm_ascend/distributed/kv_transfer/simple_connector.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/distributed/kv_transfer
      copying vllm_ascend/distributed/kv_transfer/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/distributed/kv_transfer
      copying vllm_ascend/distributed/kv_transfer/utils.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/distributed/kv_transfer
      copying vllm_ascend/distributed/kv_transfer/simple_pipe.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/distributed/kv_transfer
      copying vllm_ascend/distributed/kv_transfer/simple_buffer.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/distributed/kv_transfer
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/platform
      copying vllm_ascend/patch/platform/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/platform
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/worker
      copying vllm_ascend/patch/worker/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/worker
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/platform/patch_0_8_5
      copying vllm_ascend/patch/platform/patch_0_8_5/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/platform/patch_0_8_5
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/platform/patch_main
      copying vllm_ascend/patch/platform/patch_main/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/platform/patch_main
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/platform/patch_common
      copying vllm_ascend/patch/platform/patch_common/patch_distributed.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/platform/patch_common
      copying vllm_ascend/patch/platform/patch_common/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/platform/patch_common
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/worker/patch_0_8_5
      copying vllm_ascend/patch/worker/patch_0_8_5/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/worker/patch_0_8_5
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/worker/patch_main
      copying vllm_ascend/patch/worker/patch_main/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/worker/patch_main
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/worker/patch_common
      copying vllm_ascend/patch/worker/patch_common/patch_spec_decode_worker.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/worker/patch_common
      copying vllm_ascend/patch/worker/patch_common/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/worker/patch_common
      copying vllm_ascend/patch/worker/patch_common/patch_multi_step_worker.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/worker/patch_common
      copying vllm_ascend/patch/worker/patch_common/patch_minicpm.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/worker/patch_common
      copying vllm_ascend/patch/worker/patch_common/patch_metrics.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/patch/worker/patch_common
      creating build/lib.linux-aarch64-cpython-310/vllm_ascend/lora/punica_wrapper
      copying vllm_ascend/lora/punica_wrapper/__init__.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/lora/punica_wrapper
      copying vllm_ascend/lora/punica_wrapper/punica_npu.py -> build/lib.linux-aarch64-cpython-310/vllm_ascend/lora/punica_wrapper
      running build_ext
      Found existing ASCEND_HOME_PATH: /usr/local/Ascend/ascend-toolkit/latest
      Found existing PYTHON_EXECUTABLE: /usr/local/python3.10.17/bin/python3.10
      Found existing PYTHON_INCLUDE_PATH: /usr/local/python3.10.17/include/python3.10
      usage: __main__.py [-h] [--version] [--includes] [--cmakedir] [--pkgconfigdir]
                         [--extension-suffix]
      __main__.py: error: unrecognized arguments: --cmake
      Traceback (most recent call last):
        File "<string>", line 153, in configure
        File "/usr/local/python3.10.17/lib/python3.10/subprocess.py", line 421, in check_output
          return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
        File "/usr/local/python3.10.17/lib/python3.10/subprocess.py", line 526, in run
          raise CalledProcessError(retcode, process.args,
      subprocess.CalledProcessError: Command '['/usr/local/python3.10.17/bin/python3.10', '-m', 'pybind11', '--cmake']' returned non-zero exit status 2.
      
      During handling of the above exception, another exception occurred:
      
      Traceback (most recent call last):
        File "/usr/local/python3.10.17/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 389, in <module>
          main()
        File "/usr/local/python3.10.17/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 373, in main
          json_out["return_val"] = hook(**hook_input["kwargs"])
        File "/usr/local/python3.10.17/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 280, in build_wheel
          return _build_backend().build_wheel(
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 435, in build_wheel
          return _build(['bdist_wheel', '--dist-info-dir', str(metadata_directory)])
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 423, in _build
          return self._build_with_temp_dir(
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 404, in _build_with_temp_dir
          self.run_setup()
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 317, in run_setup
          exec(code, locals())
        File "<string>", line 331, in <module>
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/__init__.py", line 115, in setup
          return distutils.core.setup(**attrs)
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/_distutils/core.py", line 186, in setup
          return run_commands(dist)
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/_distutils/core.py", line 202, in run_commands
          dist.run_commands()
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 1002, in run_commands
          self.run_command(cmd)
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/dist.py", line 1102, in run_command
          super().run_command(command)
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 1021, in run_command
          cmd_obj.run()
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/command/bdist_wheel.py", line 370, in run
          self.run_command("build")
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/_distutils/cmd.py", line 357, in run_command
          self.distribution.run_command(command)
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/dist.py", line 1102, in run_command
          super().run_command(command)
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 1021, in run_command
          cmd_obj.run()
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/_distutils/command/build.py", line 135, in run
          self.run_command(cmd_name)
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/_distutils/cmd.py", line 357, in run_command
          self.distribution.run_command(command)
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/dist.py", line 1102, in run_command
          super().run_command(command)
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/_distutils/dist.py", line 1021, in run_command
          cmd_obj.run()
        File "<string>", line 269, in run
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/command/build_ext.py", line 96, in run
          _build_ext.run(self)
        File "/tmp/pip-build-env-l3dko3co/overlay/lib/python3.10/site-packages/setuptools/_distutils/command/build_ext.py", line 368, in run
          self.build_extensions()
        File "<string>", line 229, in build_extensions
        File "<string>", line 158, in configure
      RuntimeError: CMake configuration failed: Command '['/usr/local/python3.10.17/bin/python3.10', '-m', 'pybind11', '--cmake']' returned non-zero exit status 2.
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for vllm-ascend
Failed to build vllm-ascend
ERROR: Failed to build installable wheels for some pyproject.toml based projects (vllm-ascend)'''
