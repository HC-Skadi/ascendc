# Issue #765: [quantization]: how to quantization model `Qwen/Qwen3-235B-A22B`

## 基本信息

- **编号**: #765
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/765
- **创建时间**: 2025-05-06T10:14:18Z
- **关闭时间**: 2025-05-07T02:08:14Z
- **更新时间**: 2025-05-07T02:08:16Z
- **提交者**: @wanmei002
- **评论数**: 2

## 标签

documentation

## 问题描述

### 📚 The doc issue

i use [here](https://github.com/vllm-project/vllm-ascend/pull/580#issuecomment-2816747613) to quantization model, but error:
```bash
python3 quant_qwen.py --model_path $MODEL_PATH --save_directory $SAVE_PATH --calib_file ../common/boolq.jsonl --w_bit 8 --a_bit 8 --device_type npu --trust_remote_code True
2025-05-06 09:59:17,883 - msmodelslim-logger - WARNING - The current CANN version does not support importing the migration and migration_vit packages.
2025-05-06 09:59:17,899 - msmodelslim-logger - WARNING - The current CANN version does not support recall_window method.
2025-05-06 09:59:17,909 - msmodelslim-logger - WARNING - The current CANN version does not support LayerSelector quantile method.
2025-05-06 09:59:17,913 - msmodelslim-logger - INFO - write directory exists, write file to directory '/root/.cache/huggingface/hub/models--Qwen--Qwen3-235B-A22B-int8/'
Loading checkpoint shards: 100%|██████████████████████████████████████████████████████| 118/118 [05:15<00:00,  2.68s/it]
Traceback (most recent call last):
  File "/root/msit/msmodelslim/example/Qwen/quant_qwen.py", line 316, in <module>
    quantifier.convert(tokenized_calib_data, save_directory, args.disable_level, part_file_size=args.part_file_size, \
  File "/root/msit/msmodelslim/example/Qwen/quant_qwen.py", line 240, in convert
    calibrator = Calibrator(self.model, self.quant_config, calib_data=tokenized_data, disable_level=disable_level)
  File "/usr/local/python3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/usr/local/python3.10/lib/python3.10/site-packages/msmodelslim/pytorch/llm_ptq/llm_ptq_tools/quant_tools.py", line 160, in __init__
    self.rollback_names_process(model)
  File "/usr/local/python3.10/lib/python3.10/site-packages/msmodelslim/pytorch/llm_ptq/llm_ptq_tools/quant_tools.py", line 426, in rollback_names_process
    raise ValueError(f"`disable_names` has invalid key `{name}`, please check your model configurations.")
ValueError: `disable_names` has invalid key `model.layers.0.mlp.down_proj`, please check your model configurations.
[ERROR] 2025-05-06-10:06:30 (PID:16390, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```

### Suggest a potential alternative/fix

_No response_
