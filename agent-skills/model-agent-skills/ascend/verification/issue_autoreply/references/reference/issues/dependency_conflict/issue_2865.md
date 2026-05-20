# Issue #2865: [Bug]: accuract test failed due to unexpected keyword argument 'prompt_token_ids'

## 基本信息

- **编号**: #2865
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2865
- **创建时间**: 2025-09-10T15:53:40Z
- **关闭时间**: 2025-09-11T10:39:04Z
- **更新时间**: 2025-12-27T06:13:48Z
- **提交者**: @Yikun
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

https://github.com/vllm-project/vllm-ascend/actions/runs/17617228019/job/50053429133?pr=2864

### 🐛 Describe the bug

```
=================================== FAILURES ===================================
_______________ test_lm_eval_correctness_param[config_filename0] _______________

config_filename = PosixPath('/__w/vllm-ascend/vllm-ascend/tests/e2e/models/configs/Qwen3-8B-Base.yaml')
tp_size = '1', report_dir = './benchmarks/accuracy'
env_config = EnvConfig(vllm_version='0.1.dev1', vllm_commit='b8a9307', vllm_ascend_version='refs/pull/2864/merge', vllm_ascend_commit='f890241', cann_version='8.2.RC1', torch_version='2.7.1', torch_npu_version='2.7.1.dev20250724')

    def test_lm_eval_correctness_param(config_filename, tp_size, report_dir,
                                       env_config):
        eval_config = yaml.safe_load(config_filename.read_text(encoding="utf-8"))
        model_args = build_model_args(eval_config, tp_size)
        success = True
        report_data: dict[str, list[dict]] = {"rows": []}
    
        eval_params = {
            "model": eval_config.get("model", "vllm"),
            "model_args": model_args,
            "tasks": [task["name"] for task in eval_config["tasks"]],
            "apply_chat_template": eval_config.get("apply_chat_template", True),
            "fewshot_as_multiturn": eval_config.get("fewshot_as_multiturn", True),
            "limit": eval_config.get("limit", None),
            "batch_size": "auto",
        }
        for s in ["num_fewshot", "fewshot_as_multiturn", "apply_chat_template"]:
            val = eval_config.get(s, None)
            if val is not None:
                eval_params[s] = val
    
        print("Eval Parameters:")
        print(eval_params)
    
>       results = lm_eval.simple_evaluate(**eval_params)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/e2e/models/test_lm_eval_correctness.py:123: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/python3.11.13/lib/python3.11/site-packages/lm_eval/utils.py:422: in _wrapper
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
/usr/local/python3.11.13/lib/python3.11/site-packages/lm_eval/evaluator.py:308: in simple_evaluate
    results = evaluate(
/usr/local/python3.11.13/lib/python3.11/site-packages/lm_eval/utils.py:422: in _wrapper
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
/usr/local/python3.11.13/lib/python3.11/site-packages/lm_eval/evaluator.py:528: in evaluate
    resps = getattr(lm, reqtype)(cloned_reqs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/python3.11.13/lib/python3.11/site-packages/lm_eval/api/model.py:382: in loglikelihood
    return self._loglikelihood_tokens(new_reqs, disable_tqdm=disable_tqdm)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/python3.11.13/lib/python3.11/site-packages/lm_eval/models/vllm_causallms.py:473: in _loglikelihood_tokens
    outputs = self._model_generate(requests=inputs, generate=False)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <lm_eval.models.vllm_causallms.VLLM object at 0xfffdd0333b10>
requests = [[151644, 8948, 198, 87752, 105196, 101888, ...], [151644, 8948, 198, 87752, 105196, 101888, ...], [151644, 8948, 198,...6, 101888, ...], [151644, 8948, 198, 87752, 105196, 101888, ...], [151644, 8948, 198, 87752, 105196, 101888, ...], ...]
generate = False, max_tokens = None, stop = None, kwargs = {}

    def _model_generate(
        self,
        requests: List[List[int]] = None,
        generate: bool = False,
        max_tokens: int = None,
        stop: Optional[List[str]] = None,
        **kwargs,
    ):
        if generate:
            kwargs = self.modify_gen_kwargs(kwargs)
            sampling_params = SamplingParams(max_tokens=max_tokens, stop=stop, **kwargs)
        else:
            sampling_params = SamplingParams(
                temperature=0, prompt_logprobs=1, max_tokens=1, detokenize=False
            )
        if self.data_parallel_size > 1:
            # vLLM hangs if resources are set in ray.remote
            # also seems to only work with decorator and not with ray.remote() fn
            # see https://github.com/vllm-project/vllm/issues/973
            @ray.remote
            def run_inference_one_model(
                model_args: dict,
                sampling_params: SamplingParams,
                requests: List[List[int]],
                lora_request: LoRARequest,
            ):
                llm = LLM(**model_args)
                return llm.generate(

```
