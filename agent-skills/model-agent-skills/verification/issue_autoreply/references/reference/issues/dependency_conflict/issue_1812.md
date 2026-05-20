# Issue #1812: [Bug]: VLLM ascend v0.9.2.rc1-310p with lora run exteremely slow

## 基本信息

- **编号**: #1812
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1812
- **创建时间**: 2025-07-15T08:57:29Z
- **关闭时间**: 2025-08-19T02:35:58Z
- **更新时间**: 2025-08-19T02:35:58Z
- **提交者**: @AlphaINF
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

Here is the command I use:
```
# 设置镜像版本
export IMAGE=quay.io/ascend/vllm-ascend:v0.9.2rc1-310p

# 启动容器并在后台运行vLLM服务
docker run --rm \
        --name qwen3-8b \
        --device /dev/davinci1 \
        --device /dev/davinci_manager \
        --device /dev/devmm_svm \
        --device /dev/hisi_hdc \
        -v /usr/local/dcmi:/usr/local/dcmi \
        -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
        -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
        -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
        -v /etc/ascend_install.info:/etc/ascend_install.info \
        -v /root/.cache:/root/.cache \
        -v /home/HwHiAiUser/models:/models \
        -v /root/myb/vllm-ascend:/workspace \
        -v /root/myb/mindie2_test/Qwen3-8B/qwen8b_wxey:/root/myb/mindie2_test/Qwen3-8B/qwen8b_wxey \
        -e OMP_NUM_THREADS=48 \
        -e VLLM_USE_V1=1 \
        -p 8000:8000 \
        $IMAGE \
        vllm serve --model="/models/Qwen3-8B" \
            --host 0.0.0.0 \
            --port 8000 \
            --max-num-seqs 32 \
            --max-seq-len-to-capture 32768 \
            --max-model-len 32768 \
            --served-model-name "qwen8b" \
            --enable-prefix-caching \
            --enable-reasoning \
            --reasoning-parser qwen3 \
            --enable-lora \
            --lora-modules qwen8b_wxey=/root/myb/mindie2_test/Qwen3-8B/qwen8b_wxey \
            --enforce-eager \
            --dtype float16 \
            --disable-custom-all-reduce \
            --compilation-config '{"custom_ops":["none", "+rms_norm", "+rotary_embedding"]}'
```

### 🐛 Describe the bug



I run it on Altas 300I duo.
When it run on base model, it can reach 9token/s, however, when i using the lora, it will slow down to 2token/s.
similar like this problem https://github.com/vllm-project/vllm-ascend/pull/1591
I know opening the eager mode can speed up, however the 300I duo can't using this method.

how to solve the problem?
