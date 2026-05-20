# Issue #1382: [Bug]: longterm test failed due to RuntimeError: value cannot be converted to type at::Half without overflow

## 基本信息

- **编号**: #1382
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1382
- **创建时间**: 2025-06-24T00:24:33Z
- **关闭时间**: 2025-07-13T16:01:19Z
- **更新时间**: 2025-07-13T16:01:53Z
- **提交者**: @Yikun
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment



```
FAILED tests/e2e/long_term/spec_decode_v0/e2e/test_eagle_correctness.py::test_eagle_e2e_greedy_correctness[1-1-128-test_llm_kwargs0-baseline_llm_kwargs0-per_test_common_llm_kwargs0-common_llm_kwargs0] - requests.exceptions.ReadTimeout: (ReadTimeoutError("HTTPSConnectionPool(host='hf-mirror.com', port=443): Read timed out. (read timeout=10)"), '(Request ID: 3a48bb60-7902-4a44-bec7-6acbe77bf584)')

// ... ...

FAILED tests/e2e/long_term/spec_decode_v0/e2e/test_ngram_correctness.py::test_ngram_disable_queue[1-32-5-test_llm_kwargs0-baseline_llm_kwargs0-per_test_common_llm_kwargs0-common_llm_kwargs0] - RuntimeError: value cannot be converted to type at::Half without overflow
FAILED tests/e2e/long_term/spec_decode_v0/e2e/test_ngram_correctness.py::test_ngram_disable_queue[1-32-5-test_llm_kwargs1-baseline_llm_kwargs0-per_test_common_llm_kwargs0-common_llm_kwargs0] - RuntimeError: value cannot be converted to type at::Half without overflow
FAILED tests/e2e/long_term/spec_decode_v0/e2e/test_ngram_correctness.py::test_ngram_scorer[1-32-1-test_llm_kwargs0-baseline_llm_kwargs0-per_test_common_llm_kwargs0-common_llm_kwargs0] - RuntimeError: value cannot be converted to type at::Half without overflow
FAILED tests/e2e/long_term/spec_decode_v0/e2e/test_ngram_correctness.py::test_ngram_scorer[1-32-5-test_llm_kwargs0-baseline_llm_kwargs0-per_test_common_llm_kwargs0-common_llm_kwargs0] - RuntimeError: value cannot be converted to type at::Half without overflow
```

### 🐛 Describe the bug

https://github.com/vllm-project/vllm-ascend/actions/runs/15837115956/job/44642861026

```
tests/e2e/long_term/spec_decode_v0/e2e/test_ngram_correctness.py:397: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
tests/e2e/long_term/spec_decode_v0/e2e/conftest.py:174: in run_equality_correctness_test
    with vllm_runner(**org_args) as vllm_model:
tests/conftest.py:91: in __init__
    self.model = LLM(
vllm-empty/vllm/entrypoints/llm.py:263: in __init__
    self.llm_engine = LLMEngine.from_engine_args(
vllm-empty/vllm/engine/llm_engine.py:501: in from_engine_args
    return engine_cls.from_vllm_config(
vllm-empty/vllm/engine/llm_engine.py:477: in from_vllm_config
    return cls(
vllm-empty/vllm/engine/llm_engine.py:268: in __init__
    self._initialize_kv_caches()
vllm-empty/vllm/engine/llm_engine.py:413: in _initialize_kv_caches
    self.model_executor.determine_num_available_blocks())
vllm-empty/vllm/executor/executor_base.py:104: in determine_num_available_blocks
    results = self.collective_rpc("determine_num_available_blocks")
vllm-empty/vllm/executor/uniproc_executor.py:57: in collective_rpc
    answer = run_method(self.driver_worker, method, args, kwargs)
vllm-empty/vllm/utils.py:2687: in run_method
    return func(*args, **kwargs)
/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py:116: in decorate_context
    return func(*args, **kwargs)
vllm_ascend/worker/worker.py:288: in determine_num_available_blocks
    self.model_runner.profile_run()
/usr/local/python3.10.17/lib/python3.10/site-packages/torch/utils/_contextlib.py:116: in decorate_context
    return func(*args, **kwargs)
vllm_ascend/worker/model_runner.py:1195: in profile_run
    model_input = self.prepare_model_input(
vllm_ascend/worker/model_runner.py:1299: in prepare_model_input
    model_input = self._prepare_model_input_tensors(
vllm_ascend/worker/model_runner.py:1106: in _prepare_model_input_tensors
    builder = self._builder_cls(weakref.proxy(self), finished_requests_ids)
vllm_ascend/worker/model_runner.py:429: in __init__
    self.attn_metadata_builder = self.attn_backend.make_metadata_builder(
vllm_ascend/attention/attention.py:216: in make_metadata_builder
    return cls.get_builder_cls()(*args, **kwargs)
vllm_ascend/attention/attention.py:527: in __init__
    AscendMetadataBuilder._attn_mask_builder = AttentionMaskBuilder.initialize_from_len(
vllm_ascend/attention/attention.py:78: in initialize_from_len
    return cls(generate_attn_mask(max_seq_len, dtype, mask_value))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

max_seq_len = 128, dtype = torch.float16, mask_value = -3.4028234663852886e+38

    def generate_attn_mask(max_seq_len: int, dtype=torch.float16, mask_value=None):
        # Construct lower triangle matrix.
        mask_flag = torch.tril(
            torch.ones((max_seq_len, max_seq_len),
                       dtype=torch.bool)).view(max_seq_len, max_seq_len)
        # Create upper triangle matrix used to mark mask positions.
        mask_flag = ~mask_flag
        # Currently for fp16 dtype, the mask value should be set to -inf.
        # TODO: Eliminate this part in the future.
        if mask_value is None:
            if dtype == torch.float16:
                mask_value = torch.finfo(torch.float32).min
            else:
                mask_value = 1
>       attn_mask = torch.masked_fill(torch.zeros(size=(max_seq_len, max_seq_len)),
                                      mask_flag, mask_value).to(dtype)
E       RuntimeError: value cannot be converted to type at::Half without overflow

vllm_ascend/attention/attention.py:61: RuntimeError
```
