# Issue #9: [RFC] V1 engine support

## 基本信息

- **编号**: #9
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/9
- **创建时间**: 2025-02-06T02:22:33Z
- **关闭时间**: 2025-03-28T04:01:19Z
- **更新时间**: 2025-03-28T04:01:20Z
- **提交者**: @wangxiyuan
- **评论数**: 1

## 标签

无

## 问题描述

Currently, ascend works on V0 engine only. This issue tracks the V1 engine support TODO list or known issue:

1. Users must add `__main__` check to their script when use V1, see https://docs.vllm.ai/en/latest/design/multiprocessing.html for detail, for example：
    V0:
    ```
    from vllm import LLM, SamplingParams
    
    prompts = ["Hello, my name is"]
    sampling_params = SamplingParams(max_tokens=100, temperature=0.0)
    llm = LLM(model="facebook/opt-125m")
    outputs = llm.generate(prompts, sampling_params)
    ```
    V1
    ```
    from vllm import LLM, SamplingParams
    
    if __name__ == "__main__":
        prompts = ["Hello, my name is"]
        sampling_params = SamplingParams(max_tokens=100, temperature=0.0)
        llm = LLM(model="facebook/opt-125m")
        outputs = llm.generate(prompts, sampling_params)
    ```
2. vllm V1 engin is hard-code to cuda, it need refactor. for example, it uses cudagraph only.
3. V1 runs with torch inductor by default.
    ```
    if envs.VLLM_USE_V1 and self.model_config is not None and \
        not self.model_config.enforce_eager:
        # NOTE(woosuk): Currently, we use inductor because the piecewise
        # CUDA graphs do not work properly with the custom CUDA kernels.
        # FIXME(woosuk): Disable inductor to reduce the compilation time
        # and avoid any potential issues with the inductor.
        self.compilation_config.custom_ops = ["none"]
        self.compilation_config.use_cudagraph = True
        self.compilation_config.use_inductor = True
        self.compilation_config.cudagraph_num_of_warmups = 1
        self.compilation_config.pass_config.enable_fusion = False
        self.compilation_config.pass_config.enable_reshape = False
        self.compilation_config.level = CompilationLevel.PIECEWISE
    ```
5. some new function need be added in vllm-ascend, for example `get_kv_cache_spec`
