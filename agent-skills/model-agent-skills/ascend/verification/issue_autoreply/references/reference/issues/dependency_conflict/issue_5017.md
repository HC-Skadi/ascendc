# Issue #5017: [Bug]: conv3d not supported

## 基本信息

- **编号**: #5017
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5017
- **创建时间**: 2025-12-15T06:24:46Z
- **关闭时间**: 2025-12-16T00:34:47Z
- **更新时间**: 2025-12-16T00:34:47Z
- **提交者**: @andy19966212-cloud
- **评论数**: 1

## 标签

bug; 310p

## 问题描述

### Your current environment

<details>
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

<img width="2903" height="1780" alt="Image" src="https://github.com/user-attachments/assets/0b827b19-083f-47b7-b29d-1daae0fb096d" />

300I DUO vllm-ascend 0.10.0 镜像部署Qwen3-VL，推理图像时存在不支持的算子conv3d
