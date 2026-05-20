# Issue #178: [Usage] vllm-ascend doesn't work with vllm = 0.6.0

## 基本信息

- **编号**: #178
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/178
- **创建时间**: 2025-02-26T09:05:46Z
- **关闭时间**: 2025-02-27T15:19:50Z
- **更新时间**: 2025-02-27T15:19:50Z
- **提交者**: @Jial5588
- **评论数**: 3

## 标签

question

## 问题描述

### Your current environment

```text
vllm = 0.6.0
```


### How would you like to use vllm on ascend

I want to run inference of a [https://modelscope.cn/models/Qwen/Qwen2.5-3B](put link here). I don't know how to integrate it with vllm.

请问使用vLLM在NPU 加载模型权重的时候报错了，报错信息如下：
   File "/opt/huawei/miniconda3/lib/python3.10/site-packages/wise_inference_engine/mindie/model_executor/model_loader/loader.py", line 86, in load_model
     model.load_weights(model_config.model, model_config.revision)
   File "/opt/huawei/miniconda3/lib/python3.10/site-packages/wise_inference_engine/mindie/model_executor/models/utils/modellink_base.py", line 168, in load_weights
     self.atb_model = self.model_cls(self.config, weights)
   File "/usr/local/atb-models/atb_llm/models/qwen2/flash_causal_qwen2.py", line 27, in __init__
     self.lm_head = load_column_multi(
   File "/usr/local/atb-models/atb_llm/utils/layers/__init__.py", line 38, in load_column_multi
    weight = weights.get_multi_weights_col(prefixes, quantize=quantize, dim=0, gqa_size=head_size)
   File "/usr/local/atb-models/atb_llm/utils/weights.py", line 515, in get_multi_weights_col
     w = [self.get_sharded(f"{p}.weight", dim=0, gqa_size=gqa_size) for p in prefixes]
   File "/usr/local/atb-models/atb_llm/utils/weights.py", line 515, in <listcomp>
     w = [self.get_sharded(f"{p}.weight", dim=0, gqa_size=gqa_size) for p in prefixes]
   File "/usr/local/atb-models/atb_llm/utils/weights.py", line 203, in get_sharded
     slice_ = self._get_slice(tensor_name)
   File "/usr/local/atb-models/atb_llm/utils/weights.py", line 561, in _get_slice
     filename, tensor_name = self.get_filename(tensor_name)
  File "/usr/local/atb-models/atb_llm/utils/weights.py", line 80, in get_filename
     raise AssertionError(f"weight {tensor_name} does not exist")
 AssertionError: weight lm_head.weight does not exist

模型是Qwen2.5-3B模型，其中的config.json里也已经设置好了"tie_word_embeddings": true, 请问是什么原因呢？
