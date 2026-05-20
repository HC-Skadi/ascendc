# Issue #5497: [Bug]: ImportError: cannot import name 'SamplingParams' from 'vllm' (unknown location)

## 基本信息

- **编号**: #5497
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5497
- **创建时间**: 2025-12-30T01:59:54Z
- **关闭时间**: 2025-12-30T12:25:55Z
- **更新时间**: 2025-12-30T12:26:07Z
- **提交者**: @Skyminers
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Collecting environment information...
Traceback (most recent call last):
  File "/home/xxx/collect_env.py", line 489, in <module>
    main()
  File "/home/xxx/collect_env.py", line 468, in main
    output = get_pretty_env_info()
             ^^^^^^^^^^^^^^^^^^^^^
  File "/home/xxx/collect_env.py", line 463, in get_pretty_env_info
    return pretty_str(get_env_info())
                      ^^^^^^^^^^^^^^
  File "/home/xxx/collect_env.py", line 352, in get_env_info
    vllm_version=get_vllm_version(),
                 ^^^^^^^^^^^^^^^^^^
  File "/home/xxx/collect_env.py", line 169, in get_vllm_version
    from vllm import __version__, __version_tuple__
ImportError: cannot import name '__version__' from 'vllm' (unknown location)
[ERROR] 2025-12-30-01:54:14 (PID:975, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```

</details>


### 🐛 Describe the bug

minimal output:
```
Traceback (most recent call last):
  File "/home/xxx/vllm/test.py", line 1, in <module>
    from vllm import LLM, SamplingParams
ImportError: cannot import name 'LLM' from 'vllm' (unknown location)
```

I am using the prebuild docker image: `docker pull quay.io/ascend/vllm-ascend:v0.13.0rc1-openeuler`.

According to the official documentation, I do not need to perform any environment setup steps at this time. I have tried `pip install vllm-ascend`:

```
[root@node1 vllm]# pip install vllm-ascend==0.13.0rc1
Requirement already satisfied: vllm-ascend==0.13.0rc1 in /usr/local/python3.11.13/lib/python3.11/site-packages (0.13.0rc1)
Requirement already satisfied: cmake>=3.26 in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (4.2.1)
Requirement already satisfied: decorator in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (5.2.1)
Requirement already satisfied: einops in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (0.8.1)
Requirement already satisfied: numpy<2.0.0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (1.26.4)
Requirement already satisfied: packaging in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (25.0)
Requirement already satisfied: pip in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (25.3)
Requirement already satisfied: pybind11 in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (3.0.1)
Requirement already satisfied: pyyaml in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (6.0.3)
Requirement already satisfied: scipy in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (1.15.3)
Requirement already satisfied: pandas in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (2.3.3)
Requirement already satisfied: setuptools>=64 in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (65.5.0)
Requirement already satisfied: setuptools-scm>=8 in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (9.2.2)
Requirement already satisfied: torch==2.8.0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (2.8.0+cpu)
Requirement already satisfied: torchvision in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (0.23.0)
Requirement already satisfied: wheel in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (0.45.1)
Requirement already satisfied: pandas-stubs in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (2.3.3.251219)
Requirement already satisfied: opencv-python-headless<=4.11.0.86 in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (4.11.0.86)
Requirement already satisfied: compressed_tensors>=0.11.0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (0.12.2)
Requirement already satisfied: msgpack in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (1.1.2)
Requirement already satisfied: quart in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (0.20.0)
Requirement already satisfied: numba in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (0.63.1)
Requirement already satisfied: torch-npu==2.8.0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (2.8.0)
Requirement already satisfied: transformers>=4.57.3 in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (4.57.3)
Requirement already satisfied: fastapi<0.124.0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from vllm-ascend==0.13.0rc1) (0.123.10)
Requirement already satisfied: filelock in /usr/local/python3.11.13/lib/python3.11/site-packages (from torch==2.8.0->vllm-ascend==0.13.0rc1) (3.20.1)
Requirement already satisfied: typing-extensions>=4.10.0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from torch==2.8.0->vllm-ascend==0.13.0rc1) (4.15.0)
Requirement already satisfied: sympy>=1.13.3 in /usr/local/python3.11.13/lib/python3.11/site-packages (from torch==2.8.0->vllm-ascend==0.13.0rc1) (1.14.0)
Requirement already satisfied: networkx in /usr/local/python3.11.13/lib/python3.11/site-packages (from torch==2.8.0->vllm-ascend==0.13.0rc1) (3.6.1)
Requirement already satisfied: jinja2 in /usr/local/python3.11.13/lib/python3.11/site-packages (from torch==2.8.0->vllm-ascend==0.13.0rc1) (3.1.6)
Requirement already satisfied: fsspec in /usr/local/python3.11.13/lib/python3.11/site-packages (from torch==2.8.0->vllm-ascend==0.13.0rc1) (2025.12.0)
Requirement already satisfied: starlette<0.51.0,>=0.40.0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from fastapi<0.124.0->vllm-ascend==0.13.0rc1) (0.50.0)
Requirement already satisfied: pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4 in /usr/local/python3.11.13/lib/python3.11/site-packages (from fastapi<0.124.0->vllm-ascend==0.13.0rc1) (2.12.5)
Requirement already satisfied: annotated-doc>=0.0.2 in /usr/local/python3.11.13/lib/python3.11/site-packages (from fastapi<0.124.0->vllm-ascend==0.13.0rc1) (0.0.4)
Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi<0.124.0->vllm-ascend==0.13.0rc1) (0.7.0)
Requirement already satisfied: pydantic-core==2.41.5 in /usr/local/python3.11.13/lib/python3.11/site-packages (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi<0.124.0->vllm-ascend==0.13.0rc1) (2.41.5)
Requirement already satisfied: typing-inspection>=0.4.2 in /usr/local/python3.11.13/lib/python3.11/site-packages (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi<0.124.0->vllm-ascend==0.13.0rc1) (0.4.2)
Requirement already satisfied: anyio<5,>=3.6.2 in /usr/local/python3.11.13/lib/python3.11/site-packages (from starlette<0.51.0,>=0.40.0->fastapi<0.124.0->vllm-ascend==0.13.0rc1) (4.12.0)
Requirement already satisfied: idna>=2.8 in /usr/local/python3.11.13/lib/python3.11/site-packages (from anyio<5,>=3.6.2->starlette<0.51.0,>=0.40.0->fastapi<0.124.0->vllm-ascend==0.13.0rc1) (3.11)
Requirement already satisfied: loguru in /usr/local/python3.11.13/lib/python3.11/site-packages (from compressed_tensors>=0.11.0->vllm-ascend==0.13.0rc1) (0.7.3)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from sympy>=1.13.3->torch==2.8.0->vllm-ascend==0.13.0rc1) (1.3.0)
Requirement already satisfied: huggingface-hub<1.0,>=0.34.0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from transformers>=4.57.3->vllm-ascend==0.13.0rc1) (0.36.0)
Requirement already satisfied: regex!=2019.12.17 in /usr/local/python3.11.13/lib/python3.11/site-packages (from transformers>=4.57.3->vllm-ascend==0.13.0rc1) (2025.11.3)
Requirement already satisfied: requests in /usr/local/python3.11.13/lib/python3.11/site-packages (from transformers>=4.57.3->vllm-ascend==0.13.0rc1) (2.32.5)
Requirement already satisfied: tokenizers<=0.23.0,>=0.22.0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from transformers>=4.57.3->vllm-ascend==0.13.0rc1) (0.22.1)
Requirement already satisfied: safetensors>=0.4.3 in /usr/local/python3.11.13/lib/python3.11/site-packages (from transformers>=4.57.3->vllm-ascend==0.13.0rc1) (0.7.0)
Requirement already satisfied: tqdm>=4.27 in /usr/local/python3.11.13/lib/python3.11/site-packages (from transformers>=4.57.3->vllm-ascend==0.13.0rc1) (4.67.1)
Requirement already satisfied: hf-xet<2.0.0,>=1.1.3 in /usr/local/python3.11.13/lib/python3.11/site-packages (from huggingface-hub<1.0,>=0.34.0->transformers>=4.57.3->vllm-ascend==0.13.0rc1) (1.2.0)
Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from jinja2->torch==2.8.0->vllm-ascend==0.13.0rc1) (3.0.3)
Requirement already satisfied: llvmlite<0.47,>=0.46.0dev0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from numba->vllm-ascend==0.13.0rc1) (0.46.0)
Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/python3.11.13/lib/python3.11/site-packages (from pandas->vllm-ascend==0.13.0rc1) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in /usr/local/python3.11.13/lib/python3.11/site-packages (from pandas->vllm-ascend==0.13.0rc1) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in /usr/local/python3.11.13/lib/python3.11/site-packages (from pandas->vllm-ascend==0.13.0rc1) (2025.3)
Requirement already satisfied: six>=1.5 in /usr/local/python3.11.13/lib/python3.11/site-packages (from python-dateutil>=2.8.2->pandas->vllm-ascend==0.13.0rc1) (1.17.0)
Requirement already satisfied: types-pytz>=2022.1.1 in /usr/local/python3.11.13/lib/python3.11/site-packages (from pandas-stubs->vllm-ascend==0.13.0rc1) (2025.2.0.20251108)
Requirement already satisfied: aiofiles in /usr/local/python3.11.13/lib/python3.11/site-packages (from quart->vllm-ascend==0.13.0rc1) (25.1.0)
Requirement already satisfied: blinker>=1.6 in /usr/local/python3.11.13/lib/python3.11/site-packages (from quart->vllm-ascend==0.13.0rc1) (1.9.0)
Requirement already satisfied: click>=8.0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from quart->vllm-ascend==0.13.0rc1) (8.3.1)
Requirement already satisfied: flask>=3.0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from quart->vllm-ascend==0.13.0rc1) (3.1.2)
Requirement already satisfied: hypercorn>=0.11.2 in /usr/local/python3.11.13/lib/python3.11/site-packages (from quart->vllm-ascend==0.13.0rc1) (0.18.0)
Requirement already satisfied: itsdangerous in /usr/local/python3.11.13/lib/python3.11/site-packages (from quart->vllm-ascend==0.13.0rc1) (2.2.0)
Requirement already satisfied: werkzeug>=3.0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from quart->vllm-ascend==0.13.0rc1) (3.1.4)
Requirement already satisfied: h11 in /usr/local/python3.11.13/lib/python3.11/site-packages (from hypercorn>=0.11.2->quart->vllm-ascend==0.13.0rc1) (0.16.0)
Requirement already satisfied: h2>=4.3.0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from hypercorn>=0.11.2->quart->vllm-ascend==0.13.0rc1) (4.3.0)
Requirement already satisfied: priority in /usr/local/python3.11.13/lib/python3.11/site-packages (from hypercorn>=0.11.2->quart->vllm-ascend==0.13.0rc1) (2.0.0)
Requirement already satisfied: wsproto>=0.14.0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from hypercorn>=0.11.2->quart->vllm-ascend==0.13.0rc1) (1.3.2)
Requirement already satisfied: hyperframe<7,>=6.1 in /usr/local/python3.11.13/lib/python3.11/site-packages (from h2>=4.3.0->hypercorn>=0.11.2->quart->vllm-ascend==0.13.0rc1) (6.1.0)
Requirement already satisfied: hpack<5,>=4.1 in /usr/local/python3.11.13/lib/python3.11/site-packages (from h2>=4.3.0->hypercorn>=0.11.2->quart->vllm-ascend==0.13.0rc1) (4.1.0)
Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/python3.11.13/lib/python3.11/site-packages (from requests->transformers>=4.57.3->vllm-ascend==0.13.0rc1) (3.4.4)
Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/python3.11.13/lib/python3.11/site-packages (from requests->transformers>=4.57.3->vllm-ascend==0.13.0rc1) (2.5.0)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/python3.11.13/lib/python3.11/site-packages (from requests->transformers>=4.57.3->vllm-ascend==0.13.0rc1) (2025.11.12)
Requirement already satisfied: pillow!=8.3.*,>=5.3.0 in /usr/local/python3.11.13/lib/python3.11/site-packages (from torchvision->vllm-ascend==0.13.0rc1) (12.0.0)
```

Everything should be OK but nothing worked.
