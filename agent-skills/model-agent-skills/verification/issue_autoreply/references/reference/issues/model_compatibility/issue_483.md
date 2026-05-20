# Issue #483: [Usage]: How to Offline Inference on Multi node？

## 基本信息

- **编号**: #483
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/483
- **创建时间**: 2025-04-08T07:57:23Z
- **关闭时间**: 2025-12-08T08:02:21Z
- **更新时间**: 2025-12-08T08:02:21Z
- **提交者**: @gakkiyomi
- **评论数**: 4

## 标签

help wanted

## 问题描述

### Your current environment

How to Offline Inference on Multi node？
I can't found in docs
https://vllm-ascend.readthedocs.io/en/latest/tutorials/multi_node.html

I want support Offline Inference on Multi node in my code
~~~python
@ModelLoader.register(ModelType.QWEN2INSTRUCT)
class Qwen2InstructModel(BaseLlmModel):
    def __init__(
        self,
        model_path: str,
        device: str,
        gpu_index: int = 0,
        tensor_parallel_size: int = 1,
    ):
        self.model_path = model_path
        """
        vllm加载不需要经过base_model初始化 使用了CUDA_VISIBLE_DEVICES 或者NPU_VISIBLE_DEVICES设置显卡index
        """
        # super().__init__(model_path, device, gpu_index)
        logger.info(
            f"Qwen2Model loading, model_path: {model_path},tensor_parallel_size: {tensor_parallel_size},gpu_memory_utilization: {AppSettings.modelservice.gpu_memory_utilization}"
        )
        engine_args = AsyncEngineArgs(
            model=self.model_path,
            trust_remote_code=True,
            gpu_memory_utilization=AppSettings.modelservice.gpu_memory_utilization,
            tensor_parallel_size=tensor_parallel_size,
            max_model_len=5000,
        )
        self.llm_engine = AsyncLLMEngine.from_engine_args(engine_args)
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_path, trust_remote_code=True
        )
~~~

