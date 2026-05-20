# Issue #1470: TypeError: Qwen2_5_VLProcessor.__init__() got multiple values for argument 'image_processor'

## 基本信息

- **编号**: #1470
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1470
- **创建时间**: 2025-06-27T01:27:23Z
- **关闭时间**: 2025-09-10T11:02:33Z
- **更新时间**: 2025-09-10T11:02:33Z
- **提交者**: @Yikun
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

https://github.com/vllm-project/vllm-ascend/actions/runs/15909593074/job/44873297165
https://github.com/vllm-project/vllm-ascend/actions/runs/15909658129/job/44873510059

### 🐛 Describe the bug

```
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 519, in run_engine_core
    raise e
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 506, in run_engine_core
    engine_core = EngineCoreProc(*args, **kwargs)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 390, in __init__
    super().__init__(vllm_config, executor_class, log_stats,
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/engine/core.py", line 76, in __init__
    self.model_executor = executor_class(vllm_config)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/executor/executor_base.py", line 53, in __init__
    self._init_executor()
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/executor/uniproc_executor.py", line 47, in _init_executor
    self.collective_rpc("init_device")
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/executor/uniproc_executor.py", line 57, in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/utils.py", line 2671, in run_method
    return func(*args, **kwargs)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/worker/worker_base.py", line 606, in init_device
    self.worker.init_device()  # type: ignore
  File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 127, in init_device
    self.model_runner = NPUModelRunner(self.vllm_config, device)
  File "/__w/vllm-ascend/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 152, in __init__
    self.max_num_encoder_input_tokens, self.encoder_cache_size = compute_encoder_budget(
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/core/encoder_cache_manager.py", line 95, in compute_encoder_budget
    ) = _compute_encoder_budget_multimodal(
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/v1/core/encoder_cache_manager.py", line 125, in _compute_encoder_budget_multimodal
    .get_max_tokens_per_item_by_nonzero_modality(model_config)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/multimodal/registry.py", line 158, in get_max_tokens_per_item_by_nonzero_modality
    self.get_max_tokens_per_item_by_modality(model_config).items()
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/multimodal/registry.py", line 132, in get_max_tokens_per_item_by_modality
    return profiler.get_mm_max_tokens(
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/multimodal/profiling.py", line 256, in get_mm_max_tokens
    mm_inputs = self._get_dummy_mm_inputs(seq_len, mm_counts)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/multimodal/profiling.py", line 166, in _get_dummy_mm_inputs
    processor_inputs = factory.get_dummy_processor_inputs(
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/multimodal/profiling.py", line 91, in get_dummy_processor_inputs
    dummy_text = self.get_dummy_text(mm_counts)
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen2_vl.py", line 973, in get_dummy_text
    hf_processor = self.info.get_hf_processor()
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/model_executor/models/qwen2_5_vl.py", line 795, in get_hf_processor
    return self.ctx.get_hf_processor(
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/inputs/registry.py", line 131, in get_hf_processor
    return super().get_hf_processor(
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/inputs/registry.py", line 94, in get_hf_processor
    return cached_processor_from_config(
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/transformers_utils/processor.py", line 110, in cached_processor_from_config
    return cached_get_processor(
  File "/__w/vllm-ascend/vllm-ascend/vllm-empty/vllm/transformers_utils/processor.py", line 72, in get_processor
    processor = processor_factory.from_pretrained(
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/transformers/processing_utils.py", line 1304, in from_pretrained
    return cls.from_args_and_dict(args, processor_dict, **kwargs)
  File "/usr/local/python3.10.17/lib/python3.10/site-packages/transformers/processing_utils.py", line 1105, in from_args_and_dict
    processor = cls(*args, **valid_kwargs)
TypeError: Qwen2_5_VLProcessor.__init__() got multiple values for argument 'image_processor'
```
