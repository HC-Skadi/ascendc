# Issue #976: [Bug]: Qwen 2.5 VL 多卡ViT qkv部分权重为0导致精度异常

## 基本信息

- **编号**: #976
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/976
- **创建时间**: 2025-05-27T12:24:46Z
- **关闭时间**: 2025-05-29T12:43:56Z
- **更新时间**: 2025-05-29T12:43:56Z
- **提交者**: @404805854
- **评论数**: 5

## 标签

bug

## 问题描述

### Your current environment

各组件版本如下

|组件|版本|
|:--|:--|
|npu-smi|23.0.5|
|vllm|0.8.5.post1|
|vllm-ascend|0.8.5rc1|
|transformers|4.52.2|
|torch|2.6.0|
|torch-npu|2.6.0rc1|
|EulerOS|2.0|
|CANN|8.1.RC1|

使用8 * 910B1部署Qwen2.5-VL-72B-Instruct

测试确定在qwen2_5_vl.py/AscendQwen2_5_VisionAttention/forward中
x, _ = self.qkv(x)
操作处与8 * V100的结果完全不同，我打印了一下qkv.weight以及qkv.bias，发现两个权重后面全是0

测试7B模型单卡权重正常，4卡存在同样问题

### 🐛 Describe the bug

```shell
model=./models/Qwen2.5-VL-72B-Instruct

export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7

vllm serve \
        $model \
        --dtype float16 \
        --max_model_len 10240 \
        --enforce-eager \
        --enable-auto-tool-choice \
        --tool-call-parser hermes \
        --tensor_parallel_size 8 \
        --gpu_memory_utilization 0.95 \
        --limit-mm-per-prompt image=4
```

### 补充说明

 - 每张卡单独运行7B模型结果正常，应该非硬件问题
 - 回退版本到0.7.3rc2可以正常推理，但是vit的输出误差在1e-4级别，LM的logits的误差在1e-2级别。影响体现在temperature为0的时候，客户端收到的结果不完全相同，引入resample的话两者有结果相同的时候
