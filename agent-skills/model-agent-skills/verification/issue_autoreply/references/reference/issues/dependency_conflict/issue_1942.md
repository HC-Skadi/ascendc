# Issue #1942: [Bug]: LLM-Research/Molmo-7B-D-0924 failed to start in graph mode due to no module named 'tensorflow'

## 基本信息

- **编号**: #1942
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1942
- **创建时间**: 2025-07-23T02:02:45Z
- **关闭时间**: 2025-11-11T10:56:53Z
- **更新时间**: 2025-11-11T10:56:53Z
- **提交者**: @zhangxinyuehfad
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

v0.9.2rc1 iamge:
```
vllm serve LLM-Research/Molmo-7B-D-0924 --trust_remote_code &
```


### 🐛 Describe the bug

bug:
```
Encountered exception while importing tensorflow: No module named 'tensorflow'
ERROR 07-23 01:52:56 [core.py:586] EngineCore failed to start.
ERROR 07-23 01:52:56 [core.py:586] Traceback (most recent call last):
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/core.py", line 577, in run_engine_core
ERROR 07-23 01:52:56 [core.py:586]     engine_core = EngineCoreProc(*args, **kwargs)
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/core.py", line 404, in __init__
ERROR 07-23 01:52:56 [core.py:586]     super().__init__(vllm_config, executor_class, log_stats,
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/engine/core.py", line 75, in __init__
ERROR 07-23 01:52:56 [core.py:586]     self.model_executor = executor_class(vllm_config)
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/executor/executor_base.py", line 53, in __init__
ERROR 07-23 01:52:56 [core.py:586]     self._init_executor()
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/executor/uniproc_executor.py", line 47, in _init_executor
ERROR 07-23 01:52:56 [core.py:586]     self.collective_rpc("init_device")
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/executor/uniproc_executor.py", line 57, in collective_rpc
ERROR 07-23 01:52:56 [core.py:586]     answer = run_method(self.driver_worker, method, args, kwargs)
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/utils/__init__.py", line 2736, in run_method
ERROR 07-23 01:52:56 [core.py:586]     return func(*args, **kwargs)
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/worker/worker_base.py", line 606, in init_device
ERROR 07-23 01:52:56 [core.py:586]     self.worker.init_device()  # type: ignore
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-ascend/vllm_ascend/worker/worker_v1.py", line 136, in init_device
ERROR 07-23 01:52:56 [core.py:586]     self.model_runner = NPUModelRunner(self.vllm_config, device)
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 173, in __init__
ERROR 07-23 01:52:56 [core.py:586]     self.max_num_encoder_input_tokens, self.encoder_cache_size = compute_encoder_budget(
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/core/encoder_cache_manager.py", line 199, in compute_encoder_budget
ERROR 07-23 01:52:56 [core.py:586]     ) = _compute_encoder_budget_multimodal(
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/v1/core/encoder_cache_manager.py", line 229, in _compute_encoder_budget_multimodal
ERROR 07-23 01:52:56 [core.py:586]     .get_max_tokens_per_item_by_nonzero_modality(model_config)
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/multimodal/registry.py", line 158, in get_max_tokens_per_item_by_nonzero_modality
ERROR 07-23 01:52:56 [core.py:586]     self.get_max_tokens_per_item_by_modality(model_config).items()
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/multimodal/registry.py", line 132, in get_max_tokens_per_item_by_modality
ERROR 07-23 01:52:56 [core.py:586]     return profiler.get_mm_max_tokens(
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/multimodal/profiling.py", line 282, in get_mm_max_tokens
ERROR 07-23 01:52:56 [core.py:586]     mm_inputs = self._get_dummy_mm_inputs(seq_len, mm_counts)
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/multimodal/profiling.py", line 170, in _get_dummy_mm_inputs
ERROR 07-23 01:52:56 [core.py:586]     processor_inputs = factory.get_dummy_processor_inputs(
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/multimodal/profiling.py", line 93, in get_dummy_processor_inputs
ERROR 07-23 01:52:56 [core.py:586]     dummy_mm_data = self.get_dummy_mm_data(seq_len, mm_counts)
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/model_executor/models/molmo.py", line 1229, in get_dummy_mm_data
ERROR 07-23 01:52:56 [core.py:586]     self.info.get_image_size_with_most_features()
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/model_executor/models/molmo.py", line 1193, in get_image_size_with_most_features
ERROR 07-23 01:52:56 [core.py:586]     processor = self.get_hf_processor()
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/model_executor/models/molmo.py", line 1162, in get_hf_processor
ERROR 07-23 01:52:56 [core.py:586]     processor = self.ctx.get_hf_processor(**kwargs)
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/inputs/registry.py", line 138, in get_hf_processor
ERROR 07-23 01:52:56 [core.py:586]     return super().get_hf_processor(
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/inputs/registry.py", line 96, in get_hf_processor
ERROR 07-23 01:52:56 [core.py:586]     return cached_processor_from_config(
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/transformers_utils/processor.py", line 110, in cached_processor_from_config
ERROR 07-23 01:52:56 [core.py:586]     return cached_get_processor(
ERROR 07-23 01:52:56 [core.py:586]   File "/__w/vllm-benchmarks/vllm-benchmarks/vllm-empty/vllm/transformers_utils/processor.py", line 72, in get_processor
ERROR 07-23 01:52:56 [core.py:586]     processor = processor_factory.from_pretrained(
ERROR 07-23 01:52:56 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/modelscope/utils/hf_util/patcher.py", line 177, in patch_pretrained_model_name_or_path
ERROR 07-23 01:52:56 [core.py:586]     return cls._from_pretrained_origin.__func__(cls, model_dir,
ERROR 07-23 01:52:56 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/transformers/models/auto/processing_auto.py", line 375, in from_pretrained
ERROR 07-23 01:52:56 [core.py:586]     return processor_class.from_pretrained(
ERROR 07-23 01:52:56 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/transformers/processing_utils.py", line 1306, in from_pretrained
ERROR 07-23 01:52:56 [core.py:586]     args = cls._get_arguments_from_pretrained(pretrained_model_name_or_path, **kwargs)
ERROR 07-23 01:52:56 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/transformers/processing_utils.py", line 1365, in _get_arguments_from_pretrained
ERROR 07-23 01:52:56 [core.py:586]     args.append(attribute_class.from_pretrained(pretrained_model_name_or_path, **kwargs))
ERROR 07-23 01:52:56 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/modelscope/utils/hf_util/patcher.py", line 177, in patch_pretrained_model_name_or_path
ERROR 07-23 01:52:56 [core.py:586]     return cls._from_pretrained_origin.__func__(cls, model_dir,
ERROR 07-23 01:52:56 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/transformers/models/auto/image_processing_auto.py", line 575, in from_pretrained
ERROR 07-23 01:52:56 [core.py:586]     image_processor_class = get_class_from_dynamic_module(class_ref, pretrained_model_name_or_path, **kwargs)
ERROR 07-23 01:52:56 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/transformers/dynamic_module_utils.py", line 570, in get_class_from_dynamic_module
ERROR 07-23 01:52:56 [core.py:586]     final_module = get_cached_module_file(
ERROR 07-23 01:52:56 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/transformers/dynamic_module_utils.py", line 393, in get_cached_module_file
ERROR 07-23 01:52:56 [core.py:586]     modules_needed = check_imports(resolved_module_file)
ERROR 07-23 01:52:56 [core.py:586]   File "/usr/local/python3.10.17/lib/python3.10/site-packages/transformers/dynamic_module_utils.py", line 225, in check_imports
ERROR 07-23 01:52:56 [core.py:586]     raise ImportError(
ERROR 07-23 01:52:56 [core.py:586] ImportError: This modeling file requires the following packages that were not found in your environment: tensorflow. Run `pip install tensorflow`

```
