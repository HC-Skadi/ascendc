# Issue #5812: [Bug]: 部署W8A8模型异常 layers.0.mlp.gate_up_proj.deq_scale

**类型**: Issue

## 问题背景
### Your current environment

硬件：华为910B3 * 4，欧拉系统。部署全精度的版本是可以的，但是W8A8会报错


vllm-ascend版本：v0.13.0rc1、v0.11.0（错误一样）

模型地址（vllm-ascend官方文档推荐地址）：https://www.modelscope.cn/models/vllm-ascend/Qwen3-8B-W8A8

模型文件夹：
```text

]root@DS-01 Qwen3-8B-W8A8]# ll

total 11G

-rw-r--r-- 1 root root 786 Jan 11 16:46 config.json

-rw-r--r-- 1 root root 73 Jan 11 16:46 configuration.json

-rw-r--r-- 1 root root 239 Jan 11 16:46 generation_config.json

-rw-r--r-- 1 root root 96K Jan 11 16:46 quant_model_description.json

-rw-r--r-- 1 root root 11G Jan 11 16:55 quant_model_weight_w8a8.safetensors

-rw-r--r-- 1 root root 1.4K Jan 11 16:46 README.md

-rw-r--r-- 1 root root 9.5K Jan 11 16:46 tokenizer_config.json

-rw-r--r-- 1 root root 11M Jan 11 16:46 tokenizer.json
```

<details>
<summary>The output of `python collect_env.py`</summary>

```text
[root@DS-01 0.13.0]# docker exec -it c8a bash -c "python -m vllm.collect_env"
Collecting environment information...
==============================
        System Inf

## 基本信息
- **编号**: #5812
- **作者**: impptg
- **创建时间**: 2026-01-12T09:58:42Z
- **关闭时间**: 2026-01-12T10:02:51Z
- **标签**: bug

## 涉及版本
- vLLM: 未知

## 链接
- [查看原Issue](https://github.com/vllm-project/vllm-ascend/issues/5812)
