# Issue #4135: [Bug]: 现在用0.11.0rc1版本镜像部署qwen3-next部署是成功了，问答时直接崩溃了。

## 基本信息

- **编号**: #4135
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/4135
- **创建时间**: 2025-11-12T02:58:38Z
- **关闭时间**: 2025-11-19T03:47:12Z
- **更新时间**: 2025-12-01T02:38:38Z
- **提交者**: @watch-Ultra
- **评论数**: 23

## 标签

bug; qwen3-next

## 问题描述

### Your current environment

[<details>](

[qwen3-next部署成功后问答崩溃了.txt](https://github.com/user-attachments/files/23490993/qwen3-next.txt)

)
<summary>The output of `python collect_env.py`</summary>

```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

部署命令行是 sudo docker run -d   --name Qwen3-Next-80B-A3B-Instruct   -p 8866:8000  --restart always  --shm-size=1g   --device /dev/davinci_manager   --device /dev/hisi_hdc   --device /dev/devmm_svm   --device /dev/davinci0   --device /dev/davinci1   --device /dev/davinci2   --device /dev/davinci3   -v /usr/local/dcmi:/usr/local/dcmi   -v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi   -v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/   -v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info   -v /etc/ascend_install.info:/etc/ascend_install.info   -v /data/peak/Qwen3-Next-80B-A3B-Instruct:/root/models/Qwen3-Next-80B-A3B-Instruct  --entrypoint "vllm"   vllm-ascend:v0.11.0rc1   serve /root/models/Qwen3-Next-80B-A3B-Instruct         --served-model-name Qwen3-Next-80B-A3B-Instruct    --tensor-parallel-size 4         --port 8000  --gpu-memory-utilization 0.7 --enforce-eager    
