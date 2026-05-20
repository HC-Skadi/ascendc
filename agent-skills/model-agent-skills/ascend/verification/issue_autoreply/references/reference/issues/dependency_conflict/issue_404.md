# Issue #404: [Bug]: MultiNode offline inference failed

## 基本信息

- **编号**: #404
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/404
- **创建时间**: 2025-03-27T03:42:24Z
- **关闭时间**: 2025-05-14T02:51:13Z
- **更新时间**: 2025-05-14T02:51:14Z
- **提交者**: @zxy-111122
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

<details>
cann8beta1 torch 2.5.1

</details>


### 🐛 Describe the bug

**Here is my code**

```
llm = LLM(
    model="/home/ma-user/work/dataset/checkpointsulan/Qwen2_5_VL_3B_Instruct",
    tensor_parallel_size=2,
    max_model_len=2048,
    dtype="bfloat16",
    gpu_memory_utilization=0.7,
    trust_remote_code=True,
    enforce_eager=False,
    distributed_executor_backend="ray",
)
```

**Failure**
```
[rank0]: Traceback (most recent call last):
[rank0]:   File "/home/ma-user/work/dataset/checkpointsulan/vllm/test_qwen2_5_vl.py", line 34, in <module>
[rank0]:     llm = LLM(
[rank0]:   File "/home/ma-user/python3.10/lib/python3.10/site-packages/vllm/utils.py", line 1022, in inner
[rank0]:     return fn(*args, **kwargs)
[rank0]:   File "/home/ma-user/python3.10/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 242, in __init__
[rank0]:     self.llm_engine = self.engine_class.from_engine_args(
[rank0]:   File "/home/ma-user/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 489, in from_engine_args
[rank0]:     engine = cls(
[rank0]:   File "/home/ma-user/python3.10/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 273, in __init__
[rank0]:     self.model_executor = executor_class(vllm_config=vllm_config, )
[rank0]:   File "/home/ma-user/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 271, in __init__
[rank0]:     super().__init__(*args, **kwargs)
[rank0]:   File "/home/ma-user/python3.10/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 52, in __init__
[rank0]:     self._init_executor()
[rank0]:   File "/home/ma-user/python3.10/lib/python3.10/site-packages/vllm/executor/ray_distributed_executor.py", line 93, in _init_executor
[rank0]:     self.output_decoder = msgspec.msgpack.Decoder(
[rank0]: TypeError: Type '<function Generator at 0xfffdc5ba7910>' is not supported
[ERROR] 2025-03-27-11:25:51 (PID:1779168, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
/home/ma-user/python3.10/lib/python3.10/subprocess.py:1067: ResourceWarning: subprocess 1780392 is still running
  _warn("subprocess %s is still running" % self.pid,
```

Multinode inference has to be conducted in "ray" distributed_backend? It failed as above, so could you give an example of multinode offline inference?
Everything works well except the multinode ray distributed backend.
