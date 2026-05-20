# Issue #405: [Bug]: 运行时报错，多进程tp=4，单个设备使用时，一个python程序成功运行，一个python程序失败，端口和ip占用冲突导致

## 基本信息

- **编号**: #405
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/405
- **创建时间**: 2025-03-27T03:55:26Z
- **关闭时间**: 2025-05-14T02:52:01Z
- **更新时间**: 2025-05-14T02:52:02Z
- **提交者**: @chenchao9999
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
错误信息
[rank0]: RuntimeError: createHCCLComm:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:1479 HCCL function error: HcclGetRootInfo(&hcclID), error code is 11
[rank0]: [ERROR] 2025-03-26-17:01:03 (PID:159, Device:0, RankID:-1) ERR02200 DIST call hccl api failed.
[rank0]: EJ0003: [PID: 159] 2025-03-26-17:01:02.816.428 Failed to bind the IP port. Reason: The IP address and port have been bound already.
[rank0]:         TraceBack (most recent call last):
[rank0]:         host nic listen start failed, port[60000], return[11][FUNC:StartListenSocket][FILE:network_manager.cc][LINE:1163]

是否有环境变量可以设置这个？或者其的方法解决。
</details>


### 🐛 Describe the bug

llm = LLM(model=DEFAULT_CKPT_PATH, tensor_parallel_size=4, max_model_len=8192, max_num_seqs=256)

外部启用多个python程序。
