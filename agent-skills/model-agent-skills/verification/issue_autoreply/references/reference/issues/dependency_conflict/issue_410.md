# Issue #410: [Bug]: 4卡部署推理Qwen2.5-32B模型卡住

## 基本信息

- **编号**: #410
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/410
- **创建时间**: 2025-03-27T09:20:03Z
- **关闭时间**: 2025-04-10T01:56:21Z
- **更新时间**: 2025-04-10T01:56:21Z
- **提交者**: @gakkiyomi
- **评论数**: 6

## 标签

bug

## 问题描述

### Your current environment

同样的代码Qwen2.5-7B是可以部署并运行推理的
NPU资源  4张910B4  
使用vllm:v0.4.2 + vllm_npu:0.4.2

### 🐛 Describe the bug

同样的代码Qwen2.5-7B是可以部署并运行推理的
配置 4张910B4  
下面是部署Qwen2.5-7B的显存占用
![Image](https://github.com/user-attachments/assets/171d4434-ad5b-450f-8a39-90e1efa10d65)

~~~python
import logging

from transformers import AutoTokenizer, Conversation
from vllm import SamplingParams, AsyncLLMEngine, AsyncEngineArgs

from common.context_vars import context_traceid
from .base_llm_model import BaseLlmModel, History
from .loader import ModelLoader
from ..enums import ModelType
from ..params import VllmModelParams

logger = logging.getLogger(__name__)


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
            f"Qwen2Model loading, model_path: {model_path},tensor_parallel_size: {tensor_parallel_size}"
        )
        engine_args = AsyncEngineArgs(
            model=self.model_path,
            trust_remote_code=True,
            gpu_memory_utilization=0.98,
            tensor_parallel_size=tensor_parallel_size,
            max_model_len=5000,
        )
        self.llm_engine = AsyncLLMEngine.from_engine_args(engine_args)
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_path, trust_remote_code=True
        )
~~~
在部署Qwen2.5-32B的模型时会卡住
![Image](https://github.com/user-attachments/assets/ab3886ce-1fce-4973-bae4-fb787ff93c91)
可以看到读写阻塞了

![Image](https://github.com/user-attachments/assets/d8c5ea4b-0563-49d2-800f-30f17365e906)
NPU显存占用也一直上不去
![Image](https://github.com/user-attachments/assets/8940a04a-c582-4373-9a24-b95356410412)
