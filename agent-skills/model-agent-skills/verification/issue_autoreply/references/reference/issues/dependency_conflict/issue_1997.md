# Issue #1997: [Bug]:  Run Kimi-K2 instruct with vllm ascend 0.9.1-dev

## 基本信息

- **编号**: #1997
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1997
- **创建时间**: 2025-07-24T12:27:58Z
- **关闭时间**: 2025-08-11T03:14:10Z
- **更新时间**: 2025-08-11T03:14:10Z
- **提交者**: @erluchen
- **评论数**: 4

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

As you know, Kimi k2 instruct‘s quant method is fb8 which is not not supported for ascend currently.
we can check it in config.json as belows:
```
  "quantization_config": {
    "activation_scheme": "dynamic",
    "fmt": "e4m3",
    "quant_method": "fp8",
    "weight_block_size": [
      128,
      128
    ]
  }
```
So before starting the test, I need to invert quantize the model weights to BF16.

My test environment uses 8 Atlas 800T, a total of 64 NPU cards, and a hybrid deployment mode. 
Actually, the vllm ascend version I tested initially was V0.9.2 rc1, but after a lot of trouble, I found that there was a problem, and some of the problems were internal known problems that were fixed in the 0.9.1 -dev version, so I used the 0.9.1-dev branch. 

Now I will list the settings and problems I encountered during the testing process below. 

1. I need remove the field named "quantization_conifg" in config.json;
2. Because torchair graph mode in vllm ascend is only support DeekSeep and Pangu currently, so when i run vllm serve, I need to use eager mode by setting --enforce-eager and disable torchair;
3. Set VLLM_USE_V1=1, because it's not default setting, it needs to be done manually.
4. The third-party dependency package "blobfile" needs to be installed, otherwise, the service will not start. 
5. The most important thing is to modify the is_deepseek_mala method in the config file and add the model type of kimi_k2, otherwise, the service will report an error and fail to start.
