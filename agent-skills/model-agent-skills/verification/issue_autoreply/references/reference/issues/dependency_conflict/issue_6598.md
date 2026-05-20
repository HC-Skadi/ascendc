# Issue #6598: [Bug]: A2双机， GLM-4.7模型，使用全图模式推理报错

## 基本信息

- **编号**: #6598
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/6598
- **创建时间**: 2026-02-06T09:13:05Z
- **关闭时间**: 2026-02-26T05:40:15Z
- **更新时间**: 2026-02-26T05:40:15Z
- **提交者**: @Edkamoni
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

<details>
报错截图：
<img width="1877" height="70" alt="Image" src="https://github.com/user-attachments/assets/ef8ca8d1-00c9-4d76-bbc5-f12ae82d3370" />

docker镜像：quay.io/ascend/vllm-ascend:v0.14.0rc1
vllm：release/0.14.0
vllm-ascend commit: d1dcdfc4084825d2d8f6ff39f1e69767e5f88c40
A2双机拉起服务正常，推理报错，报错内容如图

</details>


### 🐛 Describe the bug

vllm serve /xxxxx/GLM-4.7 \
  --host 0.0.0.0 \
  --port 8004 \
  --data-parallel-size 2 \
  --data-parallel-size-local 1 \
  --data-parallel-address $HCCL_IF_IP \
  --data-parallel-rpc-port 13389 \
  --tensor-parallel-size 8 \
  --enable-expert-parallel \
  --seed 1024 \
  --served-model-name glm \
  --max-model-len 32768 \
  --max-num-batched-tokens 16384 \
  --max-num-seqs 16 \
  --async-scheduling \
  --quantization ascend \
  --trust-remote-code \
  --gpu-memory-utilization 0.9 \
  --speculative-config '{"num_speculative_tokens": 3, "model":"/xxxxx/GLM-4.7", "method":"mtp"}' \
  --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}' \
  --additional-config '{"ascend_compilation_config": {"fuse_qknorm_rope": true}, "ascend_fusion_config": {"fusion_ops_gmmswigluquant": false}}'

