# Issue #2723: [Usage]: vllm-ascned运行deepseek-v3.1-w8a8做response_format请求服务崩溃

## 基本信息

- **编号**: #2723
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/2723
- **创建时间**: 2025-09-03T07:57:47Z
- **关闭时间**: 2025-12-15T08:29:20Z
- **更新时间**: 2025-12-15T08:29:20Z
- **提交者**: @chenzhenyu1993
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

910B2*8 * 2  25.2.0
cat /usr/local/Ascend/ascend-toolkit/latest/"$(uname -i)"-linux/ascend_toolkit_install.info
package_name=Ascend-cann-toolkit
version=8.2.RC1
innerversion=V100R001C22SPC001B231
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21],[V100R001C23]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.2.RC1/aarch64-linux


### How would you like to use vllm on ascend

curl --location 'http://127.0.0.1:8025/v1/chat/completions' \
--header 'Content-Type: application/json' \
--data '{
  "model": "deepseek_v3.1",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful math tutor. Guide the user through the solution step by step."
    },
    {
      "role": "user",
      "content": "how can I solve 8x + 7 = -23"
    }
  ],
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "math_reasoning",
      "schema": {
        "type": "object",
        "properties": {
          "steps": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "explanation": { "type": "string" },
                "output": { "type": "string" }
              },
              "required": ["explanation", "output"],
              "additionalProperties": false
            }
          },
          "final_answer": { "type": "string" }
        },
        "required": ["steps", "final_answer"],
        "additionalProperties": false
      },
      "strict": true
    }
  }
}'
希望以上请求可以正常运行但是出现以下报错最终服务崩溃

INFO 09-03 07:50:59 [logger.py:41] Received request chatcmpl-b3678bb5415c4440b811f5d3598e1323: prompt: '<｜begin▁of▁sentence｜>You are a helpful math tutor. Guide the user through the solution step by step.<｜User｜>how can I solve 8x + 7 = -23<｜Assistant｜></think>', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.6, top_p=0.95, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=32734, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=GuidedDecodingParams(json={'type': 'object', 'properties': {'steps': {'type': 'array', 'items': {'type': 'object', 'properties': {'explanation': {'type': 'string'}, 'output': {'type': 'string'}}, 'required': ['explanation', 'output'], 'additionalProperties': False}}, 'final_answer': {'type': 'string'}}, 'required': ['steps', 'final_answer'], 'additionalProperties': False}, regex=None, choice=None, grammar=None, json_object=None, backend=None, backend_was_auto=False, disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, whitespace_pattern=None, structural_tag=None), extra_args=None), prompt_token_ids: None, prompt_embeds shape: None, lora_request: None.
INFO 09-03 07:50:59 [async_llm.py:269] Added request chatcmpl-b3678bb5415c4440b811f5d3598e1323.
(EngineCore_0 pid=280674) ERROR 09-03 07:51:00 [core.py:634] EngineCore encountered a fatal error.
(EngineCore_0 pid=280674) ERROR 09-03 07:51:00 [core.py:634] Traceback (most recent call last):
(EngineCore_0 pid=280674) ERROR 09-03 07:51:00 [core.py:634]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 625, in run_engine_core
(EngineCore_0 pid=280674) ERROR 09-03 07:51:00 [core.py:634]     engine_core.run_busy_loop()
(EngineCore_0 pid=280674) ERROR 09-03 07:51:00 [core.py:634]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 968, in run_busy_loop
(EngineCore_0 pid=280674) ERROR 09-03 07:51:00 [core.py:634]     executed = self._process_engine_step()
(EngineCore_0 pid=280674) ERROR 09-03 07:51:00 [core.py:634]                ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=280674) ERROR 09-03 07:51:00 [core.py:634]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 677, in _process_engine_step
(EngineCore_0 pid=280674) ERROR 09-03 07:51:00 [core.py:634]     outputs, model_executed = self.step_fn()
(EngineCore_0 pid=280674) ERROR 09-03 07:51:00 [core.py:634]                               ^^^^^^^^^^^^^^
(EngineCore_0 pid=280674) ERROR 09-03 07:51:00 [core.py:634]   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 266, in step
(EngineCore_0 pid=280674) ERROR 09-03 07:51:00 [core.py:634]     scheduler_output = self.scheduler.schedule()
(EngineCore_0 pid=280674) ERROR 09-03 07:51:00 [core.py:634]                        ^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_0 pid=280674) ERROR 09-03 07:51:00 [core.py:634]   File "/vllm-workspace/vllm-ascend/vllm_ascend/core/scheduler.py", line 216, in schedule
(EngineCore_0 pid=280674) ERROR 09-03 07:51:00 [core.py:634]     raise RuntimeError(f"Invalid request status: {request.status}")
(EngineCore_0 pid=280674) ERROR 09-03 07:51:00 [core.py:634] RuntimeError: Invalid request status: WAITING_FOR_FSM
ERROR 09-03 07:51:00 [async_llm.py:416] AsyncLLM output_handler failed.
ERROR 09-03 07:51:00 [async_llm.py:416] Traceback (most recent call last):
ERROR 09-03 07:51:00 [async_llm.py:416]   File "/vllm-workspace/vllm/vllm/v1/engine/async_llm.py", line 375, in output_handler
ERROR 09-03 07:51:00 [async_llm.py:416]     outputs = await engine_core.get_output_async()
ERROR 09-03 07:51:00 [async_llm.py:416]               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ERROR 09-03 07:51:00 [async_llm.py:416]   File "/vllm-workspace/vllm/vllm/v1/engine/core_client.py", line 751, in get_output_async
ERROR 09-03 07:51:00 [async_llm.py:416]     raise self._format_exception(outputs) from None
ERROR 09-03 07:51:00 [async_llm.py:416] vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue. See stack trace (above) for the root cause.
INFO 09-03 07:51:00 [async_llm.py:342] Request chatcmpl-b3678bb5415c4440b811f5d3598e1323 failed (engine dead).
INFO:     117.68.88.127:52690 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [280402]
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
[ERROR] TBE Subprocess[task_distribute] raise error[], main process disappeared!
/usr/local/python3.11.13/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 124 leaked semaphore objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '
/usr/local/python3.11.13/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 6 leaked shared_memory objects to clean up at shutdown
  warnings.warn('resource_tracker: There appear to be %d '


