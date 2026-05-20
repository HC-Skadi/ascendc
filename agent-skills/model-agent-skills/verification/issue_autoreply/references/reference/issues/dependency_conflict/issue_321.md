# Issue #321: [Bug]:离线推理没问题，在线推理感叹号

## 基本信息

- **编号**: #321
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/321
- **创建时间**: 2025-03-13T05:25:36Z
- **关闭时间**: 2025-03-31T15:57:30Z
- **更新时间**: 2025-03-31T15:57:30Z
- **提交者**: @huowang-li
- **评论数**: 6

## 标签

bug

## 问题描述

### Your current environment


quay.io/ascend/vllm-ascend:v0.7.3-dev使用该镜像
离线推理启动方式：
docker run \
--name test1 \
--device /dev/davinci0 \
--device /dev/davinci1 \
--device /dev/davinci2 \
--device /dev/davinci3 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-p 7862:7862 \
-e VLLM_USE_MODELSCOPE=True \
-e PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256 \
-it vllm1 bash
服务启动方式
docker run \
--name test2 \
--device /dev/davinci0 \
--device /dev/davinci1 \
--device /dev/davinci2 \
--device /dev/davinci3 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-p 7862:7862 \
-e VLLM_USE_MODELSCOPE=True \
-e PYTORCH_NPU_ALLOC_CONF=max_split_size_mb:256 \
-it vllm1 \
python -m vllm.entrypoints.openai.api_server --model="Qwen" --tensor-parallel-size 4 --enable-auto-tool-choice --tool-call-parser hermes --max-model-len 32768 --port 7862


### 🐛 Describe the bug

模型：Qwen-32B-insturct
离线推理无异常，输入1W字 输出8000字
服务推理无限感叹号
import gc

import torch

from vllm import LLM, SamplingParams
from vllm.distributed.parallel_state import (destroy_distributed_environment,
                                             destroy_model_parallel)
prompts = [
    """
　　省略一万字...
   总结一下以上小说的内容是什么
""",
]

def clean_up():
    destroy_model_parallel()
    destroy_distributed_environment()
    gc.collect()
    torch.npu.empty_cache()

# Create a sampling params object.
sampling_params = SamplingParams(temperature=0.8, top_p=0.95,max_tokens=8192)
# Create an LLM.
llm = LLM(model="Qwen",          tensor_parallel_size=4,
          distributed_executor_backend="mp",
          max_model_len=30000)

# Generate texts from the prompts.
outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f" Generated text: {generated_text!r}")
del llm
clean_up()

输出：

 Generated text: '《全职艺术家》是一部描述主角林渊穿越到一个名为蓝星的平行时空，并利用系统和自身才能征服世界的网络小说。在这个充满艺术氛围的世界里，林渊继承了一个生命垂危的原主的身体，决定要在有限的生命里，通过艺术改变自己和家人的命运。小说以文艺系统为核心，林渊通过系统获得音乐、文学等方面的知识和技能，努力提升个人声望以获得治疗和改变命运的机会。同时，他也在寻找实现自己和家人梦想的方法，特别是利用新人季等机会展示自己的音乐才华。\n\n故事主要通过林渊与同学简易、夏繁的互动以及与经纪人赵钰的交流，展示了主角为实现梦想所作出的努力和克服困难的过程。其中涉及了林渊对自己前世记忆的探索、对未来的期待，以及与现实世界的竞争。通过《生如夏花》这首歌，林渊开始尝试将自己的创作推向市场，希望能够获得认可。\n\n\n### 主要内容：\n1. **穿越和背景设定**：林渊穿越到名为蓝星的平行时空，继承一个身患绝症的原主的身体，决定要在有限的时间里通过艺术改变命运。\n2. **文艺系统**：系统绑定后，林渊获得了各类艺术技能和声望提升的机会。系统还提供了新手任务和奖励。\n3. **人际关系**：林渊与小学同学简易、夏繁保持深厚友谊，并从他们那里得知新人季的机会。\n4. **经纪人赵珏**：林渊与经纪人的关系，试图通过她获取歌曲发行的机会。经纪人赵珏因为新人季的业绩压力，愿意帮助林渊一次。\n5. **新人季**：每年十一月的新人季是各大娱乐公司推出新人的重要机会，林渊希望能借此机会发布自己的歌曲。\n6. **任务和奖励**：系统触发新手任务，要求林渊在学院考试中取得好成绩，并给出相应奖励。\n\n\n小说通过这些情节，展现了主角在艺术领域的奋斗与成长，以及如何利用系统力量在残酷的娱乐圈竞争中脱颖而出。\n\n\n### 关键情节总结：\n- **穿越与设定**：林渊穿越到蓝星，拥有一个文艺系统。\n- **系统任务**：林渊接受系统任务，目标是通过专业课考试取得好成绩。\n- **经纪人合作**：林渊与经纪人赵珏合作，尝试通过公司渠道发布歌曲。\n- **新人季机会**：林渊打算利用新人季的机会发布歌曲，迈出成功的第一步。\n\n\n小说通过这些情节展现了主角在面对绝症、家庭负担以及竞争压力时的坚强和毅力。通过艺术，林渊希望能够改变自己和家人的命运。\n\n\n### 下一步发展：\n接下来，林渊可能继续与系统互动，完成更多任务，提升自己的声望，同时努力发布自己的歌曲，参与新人季比赛，期望获得成功并得到治疗。同时，他也会继续与身边的朋友和家人互动，展现自己的艺术才华，为未来铺路。\n\n\n### 结论：\n《全职艺术家》是一部融合了穿越、系统、娱乐圈竞争以及艺术成长元素的小说，通过主角林渊的故事，展现了个人在逆境中不断努力、实现梦想的过程。\n\n\n### 推荐理由：\n本作不仅有精彩的故事情节和人物塑造，还提供了许多艺术领域的背景知识和文化细节，使读者在享受故事的同时，也能感受到艺术的魅力。\n\n\n### 感想：\n小说通过主人公在艺术领域的努力，展现了对梦想的坚持和不懈追求。同时，对系统设定的巧妙运用，让故事更具有吸引力。\n\n\n### 展望：\n随着故事的发展，林渊将面临更多的挑战和机遇，他如何利用自己的才华和系统资源，在艺术领域取得更大的成功，令人期待。\n\n\n希望以上总结和分析对您有所帮助。如果您有其他问题或需要进一步的信息，请随时提问。\n\n\n### 最后：\n《全职艺术家》是一部关于梦想、奋斗和成长的小说，它不仅提供了一个充满希望的故事，还激发了读者对艺术的兴趣和对生活的热爱。\n\n\n### 结尾：\n通过林渊的努力，我们可以看到，即使面对绝症和生活压力，只要拥有坚定的信念和持续的努力，梦想总是有可能实现的。\n\n\n### 感谢：\n感谢您阅读本篇小说的概要和分析，希望它能为您带来愉快的阅读体验。\n\n\n如果您有任何问题或需要更多信息，请随时提问。祝您阅读愉快！\n\n\n### 结束语：\n林渊的故事还在继续，他能否在新人季获得成功？让我们拭目以待。\n\n\n### 再见：\n期待您下次的阅读和交流。祝您一切顺利！\n\n\n### 附注：\n如果需要进一步的分析或其他相关信息，欢迎随时联系。\n\n\n### 最后提醒：\n《全职艺术家》是一部值得阅读的作品，它不仅提供了娱乐，还有启发意义。\n\n\n感谢您的关注和支持！\n\n\n祝好！\n\n\n###'


服务推理：
        stream = client.chat.completions.create(
            model="Qwen",
            messages=messages,
            tools=tools,
            stream=True,
            temperature=temperature,
            top_p=0.8,
            max_tokens=1500
        )
算上模板，输入tokens约3000字，输出1500字
推理结果无限感叹号！！！！！

