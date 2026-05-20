# Issue #1138: [Usage]: Serving DeepSeek-R1-Distill-Qwen-32B on vllm-ascend

## 基本信息

- **编号**: #1138
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1138
- **创建时间**: 2025-06-09T10:15:12Z
- **关闭时间**: 2025-06-10T04:20:27Z
- **更新时间**: 2025-06-10T04:20:27Z
- **提交者**: @JohanLi233
- **评论数**: 1

## 标签

无

## 问题描述

### Your current environment

<img width="540" alt="Image" src="https://github.com/user-attachments/assets/2e3278e9-191c-4795-bcac-fc8701aafd8e" />

### How would you like to use vllm on ascend


<p>Low NPU utilisation (&lt;15 % AI Core) and limited throughput when serving <strong>DeepSeek-R1-Distill-Qwen-32B</strong> with <code inline="">vllm-ascend v0.8.5rc1</code></p>
<hr>

<img width="1724" alt="Image" src="https://github.com/user-attachments/assets/3f9c74a8-b65e-43eb-a505-87c4c48c269c" />

<img width="1727" alt="Image" src="https://github.com/user-attachments/assets/2adeac89-f17c-4943-823d-c29457cdddbc" />

<h3><strong>Environment</strong></h3>

Item | Value
-- | --
Container image | quay.io/ascend/vllm-ascend:v0.8.5rc1
Model | DeepSeek-R1-Distill-Qwen-32B (HF format, offline)
Hardware | 8 × Ascend 910B
Host OS | ubuntu 24.04
Driver / firmware | 25.0.rc1.1 / 7.7.0.1.231

## Command to reproduce
``` bash
# model path
export MODEL_DIR=$HOME/DeepSeek-R1-Distill-Qwen-32B

# launch on 4 NPUs
docker run -d \
  --name vllm-ascend \
  --restart unless-stopped \
  $(printf -- '--device /dev/davinci%d ' {0..3}) \
  --device /dev/davinci_manager \
  --device /dev/devmm_svm \
  --device /dev/hisi_hdc \
  -v /usr/local/dcmi:/usr/local/dcmi \
  -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
  -v /usr/local/Ascend/driver/lib64:/usr/local/Ascend/driver/lib64 \
  -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
  -v /etc/ascend_install.info:/etc/ascend_install.info \
  -v ~/.cache:/root/.cache \
  -v $MODEL_DIR:/workspace/model \
  -e ASCEND_RT_VISIBLE_DEVICES=0,1,2,3 \
  -e HF_HUB_OFFLINE=1 \
  -e OMP_NUM_THREADS=192 \
  -p 8000:8000 \
  quay.io/ascend/vllm-ascend:v0.8.5rc1 \
  vllm serve /workspace/model \
    --tensor-parallel-size 4 \
    --enable-reasoning \
    --dtype bfloat16 \
    --reasoning-parser deepseek_r1 \
    --gpu-memory-utilization 0.98 \
    --max-num-seqs 1024
```

</body></html>

<hr>
<h3><strong>Questions / help needed</strong></h3>
<ol>
<li>
<p>Do additional flags (e.g. <code inline="">--block-size</code>, <code inline="">--max-num-seqs</code>) need tuning for this model?</p>
</li>
<li>
<p>Anything obvious in my run command that would cap sequence concurrency at 6?</p>
</li>
<li>
<p>Any guidance on profiling to understand the low AI Core utilisation?</p>
</li>
</ol>
<p>Thanks in advance for any pointers—happy to provide more logs or experiment with patches.</p></body></html>
