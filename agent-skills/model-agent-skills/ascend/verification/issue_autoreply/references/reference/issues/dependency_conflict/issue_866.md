# Issue #866: [Bug]: vllm 0.7.3 v1 engine do not support Baichuan model

## 基本信息

- **编号**: #866
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/866
- **创建时间**: 2025-05-15T06:50:11Z
- **关闭时间**: 2025-05-26T11:29:44Z
- **更新时间**: 2025-05-26T11:29:46Z
- **提交者**: @kevin-hongkai
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

<details>
<summary>vllm 0.7.3 do not support Baichuan model</summary>
enviroment:    vllm 0.7.3 cann8.1.rc1 torch2.5.1 torch-npu 2.5.1 ,  use the docs:  https://vllm-ascend.readthedocs.io/en/v0.7.3/installation.html  to run baichuan model
</details>


### 🐛 Describe the bug

1、enviroment:    vllm 0.7.3 cann8.1.rc1 torch2.5.1 torch-npu 2.5.1 ,  use the docs:  https://vllm-ascend.readthedocs.io/en/v0.7.3/installation.html  to run baichuan model

2、command: 
**export VLLM_USE_V1=1**
**export VLLM_WORKER_MULTIPROC_METHOD=spawn**
python3 vllm/benchmarks/benchmark_throughput.py --model baichuan-inc/Baichuan2-7B-Chat --input-len 512 --output-len 1 --tensor-parallel-size 1 --num-prompts 300 --disable-custom-all-reduce --trust-remote-code

3、result error:
CANN_VERSION : 8.1.RC1
opp/built-in/op_impl/ai_core/tbe/impl/dynamic/../ascendc/gather_v3/gather_v3_base.h:137
Assertion `(0 <= val && val < this->gxSize_)' Index 5330 out of range[0 4096)!

 AIV Kernel happen error, retCode=0x31.[FUNC:GetError][FILE:stream.cc][LINE:1119]
       Aicore kernel execute failed, device_id=2, stream_id=2, report_stream_id=2, task_id=96, flip_num=0, fault kernel_name=GatherV3_7869a97190b9b4d296d9414a005b954b_high_performance_10330, fault kernel info ext=none, 

4、vllm 0.8.5post1, vllm-ascend 0.8.5rc1 v1 engine can run baichuan model, hope the modify of  0.8.5rc1  can merge to 0.7.3
