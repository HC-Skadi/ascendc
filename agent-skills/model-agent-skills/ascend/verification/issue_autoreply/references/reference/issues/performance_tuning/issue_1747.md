# Issue #1747: [Usage]: 出现ImportError: cannot import name 'PoolingParams' from 'vllm' (unknown location)

## 基本信息

- **编号**: #1747
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1747
- **创建时间**: 2025-07-11T08:09:53Z
- **关闭时间**: 2025-07-18T00:35:48Z
- **更新时间**: 2025-07-18T00:35:48Z
- **提交者**: @Schweizliu
- **评论数**: 3

## 标签

无

## 问题描述

### Your current environment

<details>
<summary>910B4 八卡32G </summary>

```text
vllm-ascend:090rc2镜像 vllm:main hdk 24.1.1 cann8.1.rc1
启动命令：
VLLM_USE_V1=1 python -m vllm.entrypoints.openai.api_server --model /home/Qwen2.5-VL-7B/ --tensor-parallel-size 4 --block-size=128 --max-num-seqs=32 --max-model-len=16384 --host 127.17.0.1 --port 8080 --trust-remote-code --gpu-memory-utilization=0.96 --served-model-name="qwen2.5-vl-7b"
其中vllm仓库无法git clone，

参考这里的步骤
https://github.com/vllm-project/vllm-ascend/blob/57664f07724404d5ca45835442968e0e97d9aa5d/benchmarks/scripts/run-performance-benchmarks.sh#L274
将vllm main仓下载到本地上传到/vllm-worksapce/vllm-ascend/benchmarks下 

执行性能测试bash benchmarks/scripts/run-performance-benchmarks.sh
出现
<img width="1883" height="889" alt="Image" src="https://github.com/user-attachments/assets/2da33c1b-4301-4986-b99d-023e1b989aa0" />
```

</details>

https://github.com/vllm-project/vllm官方仓无090rc2tags
该问题是否是vllm-ascend090rc2与vllm main版本不匹配导致的，应该使用vllm哪个版本仓


### How would you like to use vllm on ascend

我希望在090rc2上可以正常进行benchmark性能测试
