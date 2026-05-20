# Issue #4737: [Usage]: vllm-ascend 0.11.0rc2、0.11.0rc3镜像没有安装vllm bench的依赖，导致镜像无法在离线环境进行vllm bench测试

## 基本信息

- **编号**: #4737
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4737
- **创建时间**: 2025-12-05T03:51:07Z
- **关闭时间**: 2025-12-08T03:23:53Z
- **更新时间**: 2025-12-08T03:25:08Z
- **提交者**: @SakuraChaser
- **评论数**: 5

## 标签

无

## 问题描述

### Your current environment

```text
vllm-ascend:0.11.0rc2、0.11.0rc3，执行 vllm bench serve 报错
root@fc40334132ba:/home/dcn/work# vllm bench serve \
>   --backend vllm \
>   --model /models/Qwen3-32B-W8A8 \
>   --endpoint /v1/completions \
>   --dataset-name custom \
>   --dataset-path /home/dcn/datasets/hs_vllm/data.jsonl \
>   --max-concurrency 1000 \
>   --request-rate 1 \
>   --num-prompts 3
INFO 12-05 02:10:41 [__init__.py:36] Available plugins for group vllm.platform_plugins:
INFO 12-05 02:10:41 [__init__.py:38] - ascend -> vllm_ascend:register
INFO 12-05 02:10:41 [__init__.py:41] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load.
INFO 12-05 02:10:41 [__init__.py:207] Platform plugin ascend is activated
WARNING 12-05 02:10:46 [_custom_ops.py:20] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'")
WARNING 12-05 02:10:46 [registry.py:582] Model architecture Qwen2VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_vl:AscendQwen2VLForConditionalGeneration.
WARNING 12-05 02:10:46 [registry.py:582] Model architecture Qwen3VLMoeForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLMoeForConditionalGeneration.
WARNING 12-05 02:10:46 [registry.py:582] Model architecture Qwen3VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl_without_padding:AscendQwen3VLForConditionalGeneration.
WARNING 12-05 02:10:46 [registry.py:582] Model architecture Qwen2_5_VLForConditionalGeneration is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_vl:AscendQwen2_5_VLForConditionalGeneration.
WARNING 12-05 02:10:46 [registry.py:582] Model architecture Qwen2_5OmniModel is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen2_5_omni_thinker:AscendQwen2_5OmniThinkerForConditionalGeneration.
WARNING 12-05 02:10:46 [registry.py:582] Model architecture DeepseekV32ForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.deepseek_v3_2:CustomDeepseekV3ForCausalLM.
WARNING 12-05 02:10:46 [registry.py:582] Model architecture Qwen3NextForCausalLM is already registered, and will be overwritten by the new model class vllm_ascend.models.qwen3_next:CustomQwen3NextForCausalLM.
INFO 12-05 02:10:46 [importing.py:63] Triton not installed or not compatible; certain GPU-related functions will not be available.
Namespace(subparser='bench', bench_type='serve', dispatch_function=<function BenchmarkServingSubcommand.cmd at 0xfffce3de4180>, seed=0, num_prompts=3, dataset_name='custom', no_stream=False, dataset_path='/home/dcn/datasets/hs_vllm/data.jsonl', no_oversample=False, custom_output_len=256, custom_skip_chat_template=False, spec_bench_output_len=256, spec_bench_category=None, sonnet_input_len=550, sonnet_output_len=150, sonnet_prefix_len=200, sharegpt_output_len=None, blazedit_min_distance=0.0, blazedit_max_distance=1.0, random_input_len=1024, random_output_len=128, random_range_ratio=0.0, random_prefix_len=0, random_batch_size=1, random_mm_base_items_per_request=1, random_mm_num_mm_items_range_ratio=0.0, random_mm_limit_mm_per_prompt={'image': 255, 'video': 0}, random_mm_bucket_config={(256, 256, 1): 0.5, (720, 1280, 1): 0.5, (720, 1280, 16): 0.0}, hf_subset=None, hf_split=None, hf_name=None, hf_output_len=None, prefix_repetition_prefix_len=256, prefix_repetition_suffix_len=256, prefix_repetition_num_prefixes=10, prefix_repetition_output_len=128, label=None, backend='vllm', endpoint_type=None, base_url=None, host='127.0.0.1', port=8000, endpoint='/v1/completions', header=None, max_concurrency=1000, model='/models/Qwen3-32B-W8A8', tokenizer=None, use_beam_search=False, logprobs=None, request_rate=1.0, burstiness=1.0, trust_remote_code=False, disable_tqdm=False, profile=False, save_result=False, save_detailed=False, append_result=False, metadata=None, result_dir=None, result_filename=None, ignore_eos=False, percentile_metrics='ttft,tpot,itl', metric_percentiles='99', goodput=None, request_id_prefix='benchmark-serving', top_p=None, top_k=None, min_p=None, temperature=None, tokenizer_mode='auto', served_model_name=None, lora_modules=None, ramp_up_strategy=None, ramp_up_start_rps=None, ramp_up_end_rps=None, ready_check_timeout_sec=600)
Traceback (most recent call last):
  File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 2582, in __getattr__
    importlib.import_module(name)
  File "/usr/local/python3.11.13/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1140, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'pandas'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/python3.11.13/bin/vllm", line 7, in <module>
    sys.exit(main())
             ^^^^^^
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/main.py", line 54, in main
    args.dispatch_function(args)
  File "/vllm-workspace/vllm/vllm/entrypoints/cli/benchmark/serve.py", line 21, in cmd
    main(args)
  File "/vllm-workspace/vllm/vllm/benchmarks/serve.py", line 1164, in main
    return asyncio.run(main_async(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 190, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/benchmarks/serve.py", line 1227, in main_async
    input_requests = get_samples(args, tokenizer)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/benchmarks/datasets.py", line 1348, in get_samples
    dataset = CustomDataset(dataset_path=args.dataset_path)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/benchmarks/datasets.py", line 1597, in __init__
    self.load_data()
  File "/vllm-workspace/vllm/vllm/benchmarks/datasets.py", line 1612, in load_data
    jsonl_data = pd.read_json(path_or_buf=self.dataset_path,
                 ^^^^^^^^^^^^
  File "/vllm-workspace/vllm/vllm/utils/__init__.py", line 2587, in __getattr__
    raise ImportError(msg) from exc
ImportError: Please install vllm[bench] for bench support
[ERROR] 2025-12-05-02:10:47 (PID:1977, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```


### How would you like to use vllm on ascend

_No response_
