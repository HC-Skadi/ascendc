# Issue #5993: [Bug]: 双机 A2 800 (64Gx8) vllm-ascend:v0.13.0rc1 部署 DeepSeek-V3.1-w8a8-mtp-QuaRot 失败

## 基本信息

- **编号**: #5993
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/5993
- **创建时间**: 2026-01-19T06:12:45Z
- **关闭时间**: 2026-01-20T03:35:18Z
- **更新时间**: 2026-01-23T06:22:43Z
- **提交者**: @shilongx
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment



#### 一、基本信息
```text
=== 操作系统信息 ===                                  
NAME="openEuler"                                     
VERSION="22.03 LTS"                                                                                       
=== 内核与架构 ===                                                                          
Linux worker-25 5.10.0-60.18.0.50.oe2203.aarch64 #1 SMP Wed Mar 30 02:43:08 UTC 2022 aarch64 aarch64 aarch64 GNU/Linux 

=== CPU 信息 ===                                                                           
Architecture:                    aarch64                                                   
CPU(s):                          192       

=== 华为服务器型号 ===                                                                      
 Product Name          : Atlas 800 9000 A2

模型参数来源：https://modelscope.cn/models/Eco-Tech/DeepSeek-V3.1-w8a8-mtp-QuaRot
```

#### 二、操作记录
##### （1）两个节点的容器启动命令
```bash
export IMAGE=quay.io/ascend/vllm-ascend:v0.13.0rc1
export NAME=DeepSeek-V3.1-w8a8-mtp-QuaRot

sudo docker run --rm \
--name $NAME \
--net=host \
--shm-size=1g \
--device /dev/davinci0 \
--device /dev/davinci1 \
--device /dev/davinci2 \
--device /dev/davinci3 \
--device /dev/davinci4 \
--device /dev/davinci5 \
--device /dev/davinci6 \
--device /dev/davinci7 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/Ascend/driver/tools/hccn_tool:/usr/local/Ascend/driver/tools/hccn_tool \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /data/models/DeepSeek-V3.1-w8a8-mtp-QuaRot:/data/models/DeepSeek-V3.1-w8a8-mtp-QuaRot:ro \
-p 18034:8000 \
-d $IMAGE bash -c "tail -f /dev/null"
```
##### （2）两个节点的容器内的运行命令
Node0
```bash
nic_name="bond0.150"
local_ip="xxx.xxx.xxx.3"
node0_ip="xxx.xxx.xxx.3"

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export HCCL_BUFFSIZE=200
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export VLLM_ASCEND_ENABLE_MLAPO=1
export VLLM_ASCEND_BALANCE_SCHEDULING=1
export HCCL_INTRA_PCIE_ENABLE=1
export HCCL_INTRA_ROCE_ENABLE=0

vllm serve /data/models/DeepSeek-V3.1-w8a8-mtp-QuaRot \
--host 0.0.0.0 \
--port 8000 \
--data-parallel-size 4 \
--data-parallel-size-local 2 \
--data-parallel-address $node0_ip \
--data-parallel-rpc-port 13389 \
--tensor-parallel-size 4 \
--quantization ascend \
--seed 1024 \
--served-model-name deepseek_v3 \
--enable-expert-parallel \
--async-scheduling \
--max-num-seqs 16 \
--max-model-len 16384 \
--max-num-batched-tokens 4096 \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.92 \
--speculative-config '{"num_speculative_tokens": 3, "method": "mtp"}' \
--compilation-config '{"cudagraph_capture_sizes":[4,16,32,48,64], "cudagraph_mode": "FULL_DECODE_ONLY"}'
```
Node1
```bash
nic_name="bond0.150"
local_ip="xxx.xxx.xxx.4"
node0_ip="xxx.xxx.xxx.3" # same as the local_IP address in node 0

export HCCL_IF_IP=$local_ip
export GLOO_SOCKET_IFNAME=$nic_name
export TP_SOCKET_IFNAME=$nic_name
export HCCL_SOCKET_IFNAME=$nic_name
export OMP_PROC_BIND=false
export OMP_NUM_THREADS=1
export HCCL_BUFFSIZE=200
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
export VLLM_ASCEND_ENABLE_MLAPO=1
export VLLM_ASCEND_BALANCE_SCHEDULING=1
export HCCL_INTRA_PCIE_ENABLE=1
export HCCL_INTRA_ROCE_ENABLE=0

vllm serve /data/models/DeepSeek-V3.1-w8a8-mtp-QuaRot \
--host 0.0.0.0 \
--port 8000 \
--headless \
--data-parallel-size 4 \
--data-parallel-size-local 2 \
--data-parallel-start-rank 2 \
--data-parallel-address $node0_ip \
--data-parallel-rpc-port 13389 \
--tensor-parallel-size 4 \
--quantization ascend \
--seed 1024 \
--served-model-name deepseek_v3 \
--enable-expert-parallel \
--async-scheduling \
--max-num-seqs 16 \
--max-model-len 16384 \
--max-num-batched-tokens 4096 \
--trust-remote-code \
--no-enable-prefix-caching \
--gpu-memory-utilization 0.92 \
--speculative-config '{"num_speculative_tokens": 3, "method": "mtp"}' \
--compilation-config '{"cudagraph_capture_sizes":[4,16,32,48,64], "cudagraph_mode": "FULL_DECODE_ONLY"}'
```



### 🐛 Describe the bug

#### 部分报错信息
```text
(Worker_DP3_TP0_EP12 pid=9196) INFO 01-19 05:52:13 [backends.py:643] Using cache directory: /root/.cache/vllm/torch_compile_cache/5a08503937/rank_0_3/backbone for vLLM's torch.compile
(Worker_DP3_TP0_EP12 pid=9196) INFO 01-19 05:52:13 [backends.py:703] Dynamo bytecode transform time: 7.64 s
(Worker_DP2_TP0_EP8 pid=9197) INFO 01-19 05:52:14 [backends.py:643] Using cache directory: /root/.cache/vllm/torch_compile_cache/5a08503937/rank_0_2/backbone for vLLM's torch.compile
(Worker_DP2_TP0_EP8 pid=9197) INFO 01-19 05:52:14 [backends.py:703] Dynamo bytecode transform time: 7.93 s
(Worker_DP2_TP0_EP8 pid=9197) INFO 01-19 05:52:35 [backends.py:278] Compiling a graph for compile range (1, 4096) takes 16.71 s
(Worker_DP3_TP0_EP12 pid=9196) INFO 01-19 05:52:35 [backends.py:278] Compiling a graph for compile range (1, 4096) takes 17.00 s
[rank9]:[E119 05:52:40.886041733 compiler_depend.ts:444] operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:161 NPU function error: call aclnnMoeDistributeDispatchV3 failed, error code is 561000
[ERROR] 2026-01-19-05:52:40 (PID:9208, Device:1, RankID:-1) ERR00100 PTA call acl api failed.
[PID: 9208] 2026-01-19-05:52:40.055.233 Allocation_Failure(EI0007): Failed to allocate resource[qp] with info [aicpu rank:9,localUserrank:9,localIpAddr: 100.97.1.26,deviceLogicId:1,send_cq_depth:32768]. Reason: Memory resources are exhausted.
        Possible Cause: Failed to allocate memory or the Notify register due to resource insufficiency.
        TraceBack (most recent call last):
        Transport init error. Reason: [Create][DestLink]Create Dest error! creakLink para:rank[9]-localUserrank[9]-localIpAddr[135.173.74.4], dst_rank[0]-remoteUserrank[0]-remote_ip_addr[135.173.74.3]
        Transport init error. Reason: [Create][DestLink]Create Dest error! creakLink para:rank[9]-localUserrank[9]-localIpAddr[135.173.74.4], dst_rank[1]-remoteUserrank[1]-remote_ip_addr[135.173.74.3]
        Transport init error. Reason: [Create][DestLink]Create Dest error! creakLink para:rank[9]-localUserrank[9]-localIpAddr[135.173.74.4], dst_rank[2]-remoteUserrank[2]-remote_ip_addr[135.173.74.3]
        Transport init error. Reason: [Create][DestLink]Create Dest error! creakLink para:rank[9]-localUserrank[9]-localIpAddr[135.173.74.4], dst_rank[3]-remoteUserrank[3]-remote_ip_addr[135.173.74.3]
        Transport init error. Reason: [Create][DestLink]Create Dest error! creakLink para:rank[9]-localUserrank[9]-localIpAddr[135.173.74.4], dst_rank[4]-remoteUserrank[4]-remote_ip_addr[135.173.74.3]
        Transport init error. Reason: [Create][DestLink]Create Dest error! creakLink para:rank[9]-localUserrank[9]-localIpAddr[135.173.74.4], dst_rank[5]-remoteUserrank[5]-remote_ip_addr[135.173.74.3]
        Transport init error. Reason: [Create][DestLink]Create Dest error! creakLink para:rank[9]-localUserrank[9]-localIpAddr[135.173.74.4], dst_rank[6]-remoteUserrank[6]-remote_ip_addr[135.173.74.3]
        Transport init error. Reason: [Create][DestLink]Create Dest error! creakLink para:rank[9]-localUserrank[9]-localIpAddr[135.173.74.4], dst_rank[7]-remoteUserrank[7]-remote_ip_addr[135.173.74.3]
        Nnopbase fails to invoke the HcclAllocComResourceByTiling function of the hccl module. ret = 4, comm = 0xfffec97318c0.
        Check nnopbase::NnopBaseHcclWrapper::GetInstance().HcclAllocComResourceByTiling(commHandle, stream, ((NnopbaseTilingData *)executor->args->tilingInfo.tilingData)->GetData(), &contextAddr) failed
        Check NnopbaseGetHcomResource(executor, stream) failed
        Check NnopbaseExecutorGetMc2Num(executor, stream, &argsAddr, &mc2Num) failed
        Check NnopbaseExecutorPrepareParamsExt(executor, stream) failed
        Check NnopbaseRunWithWorkspace(executor, stream, workspace, workspaceSize) failed

Exception raised from operator() at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:161 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xb0 (0xffff96ce48c0 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x68 (0xffff96c8c140 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: <unknown function> + 0x18aaac0 (0xffff8393aac0 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #3: <unknown function> + 0x29f0894 (0xffff84a80894 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #4: <unknown function> + 0x9cc700 (0xffff82a5c700 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0x9cd2dc (0xffff82a5d2dc in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0x9cb1f8 (0xffff82a5b1f8 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0xd29cc (0xffffa48c29cc in /lib/aarch64-linux-gnu/libstdc++.so.6)
frame #8: <unknown function> + 0x80398 (0xffffa4aa0398 in /lib/aarch64-linux-gnu/libc.so.6)
frame #9: <unknown function> + 0xe9e9c (0xffffa4b09e9c in /lib/aarch64-linux-gnu/libc.so.6)
```
```text
[rank15]:[E119 05:52:40.888371814 compiler_depend.ts:444] operator():build/CMakeFiles/torch_npu.dir/compiler_depend.ts:161 NPU function error: call aclnnMoeDistributeDispatchV3 failed, error code is 561000
[ERROR] 2026-01-19-05:52:40 (PID:9288, Device:3, RankID:-1) ERR00100 PTA call acl api failed.
[PID: 9288] 2026-01-19-05:52:40.052.351 Allocation_Failure(EI0007): Failed to allocate resource[qp] with info [aicpu rank:15,localUserrank:15,localIpAddr: 100.97.1.32,deviceLogicId:3,send_cq_depth:32768]. Reason: Memory resources are exhausted.
        Possible Cause: Failed to allocate memory or the Notify register due to resource insufficiency.
        TraceBack (most recent call last):
        Transport init error. Reason: [Create][DestLink]Create Dest error! creakLink para:rank[15]-localUserrank[15]-localIpAddr[135.173.74.4], dst_rank[1]-remoteUserrank[1]-remote_ip_addr[135.173.74.3]
        Transport init error. Reason: [Create][DestLink]Create Dest error! creakLink para:rank[15]-localUserrank[15]-localIpAddr[135.173.74.4], dst_rank[0]-remoteUserrank[0]-remote_ip_addr[135.173.74.3]
        Transport init error. Reason: [Create][DestLink]Create Dest error! creakLink para:rank[15]-localUserrank[15]-localIpAddr[135.173.74.4], dst_rank[2]-remoteUserrank[2]-remote_ip_addr[135.173.74.3]
        Transport init error. Reason: [Create][DestLink]Create Dest error! creakLink para:rank[15]-localUserrank[15]-localIpAddr[135.173.74.4], dst_rank[3]-remoteUserrank[3]-remote_ip_addr[135.173.74.3]
        Transport init error. Reason: [Create][DestLink]Create Dest error! creakLink para:rank[15]-localUserrank[15]-localIpAddr[135.173.74.4], dst_rank[4]-remoteUserrank[4]-remote_ip_addr[135.173.74.3]
        Transport init error. Reason: [Create][DestLink]Create Dest error! creakLink para:rank[15]-localUserrank[15]-localIpAddr[135.173.74.4], dst_rank[5]-remoteUserrank[5]-remote_ip_addr[135.173.74.3]
        Transport init error. Reason: [Create][DestLink]Create Dest error! creakLink para:rank[15]-localUserrank[15]-localIpAddr[135.173.74.4], dst_rank[6]-remoteUserrank[6]-remote_ip_addr[135.173.74.3]
        Transport init error. Reason: [Create][DestLink]Create Dest error! creakLink para:rank[15]-localUserrank[15]-localIpAddr[135.173.74.4], dst_rank[7]-remoteUserrank[7]-remote_ip_addr[135.173.74.3]
        Nnopbase fails to invoke the HcclAllocComResourceByTiling function of the hccl module. ret = 4, comm = 0xfffedefb18c0.
        Check nnopbase::NnopBaseHcclWrapper::GetInstance().HcclAllocComResourceByTiling(commHandle, stream, ((NnopbaseTilingData *)executor->args->tilingInfo.tilingData)->GetData(), &contextAddr) failed
        Check NnopbaseGetHcomResource(executor, stream) failed
        Check NnopbaseExecutorGetMc2Num(executor, stream, &argsAddr, &mc2Num) failed
        Check NnopbaseExecutorPrepareParamsExt(executor, stream) failed
        Check NnopbaseRunWithWorkspace(executor, stream, workspace, workspaceSize) failed

Exception raised from operator() at build/CMakeFiles/torch_npu.dir/compiler_depend.ts:161 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0xb0 (0xffffac5848c0 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) + 0x68 (0xffffac52c140 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch/lib/libc10.so)
frame #2: <unknown function> + 0x18aaac0 (0xffff991daac0 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #3: <unknown function> + 0x29f0894 (0xffff9a320894 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #4: <unknown function> + 0x9cc700 (0xffff982fc700 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0x9cd2dc (0xffff982fd2dc in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0x9cb1f8 (0xffff982fb1f8 in /usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0xd29cc (0xffffba1629cc in /lib/aarch64-linux-gnu/libstdc++.so.6)
frame #8: <unknown function> + 0x80398 (0xffffba340398 in /lib/aarch64-linux-gnu/libc.so.6)
frame #9: <unknown function> + 0xe9e9c (0xffffba3a9e9c in /lib/aarch64-linux-gnu/libc.so.6)

(Worker_DP2_TP0_EP8 pid=9197) INFO 01-19 05:52:40 [backends.py:703] Dynamo bytecode transform time: 0.44 s
(Worker_DP3_TP0_EP12 pid=9196) INFO 01-19 05:52:40 [backends.py:703] Dynamo bytecode transform time: 0.46 s
(Worker_DP2_TP0_EP8 pid=9197) INFO 01-19 05:52:41 [backends.py:278] Compiling a graph for compile range (1, 4096) takes 0.60 s
(Worker_DP3_TP0_EP12 pid=9196) INFO 01-19 05:52:41 [backends.py:278] Compiling a graph for compile range (1, 4096) takes 0.59 s
(Worker_DP2_TP0_EP8 pid=9197) INFO 01-19 05:52:54 [worker.py:283] Available memory: 0, total memory: 65464696832
(Worker_DP3_TP0_EP12 pid=9196) INFO 01-19 05:52:55 [worker.py:283] Available memory: 0, total memory: 65464696832
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824] WorkerProc hit an exception.
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824] Traceback (most recent call last):
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     output = func(*args, **kwargs)
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 254, in determine_available_memory
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     self.model_runner.profile_run()
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2206, in profile_run
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     self._dummy_run(mc2_tokens_capacity,
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2158, in _dummy_run
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     self.drafter.dummy_run(
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/mtp_proposer.py", line 236, in dummy_run
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     ) = self.runner._sync_metadata_across_dp(num_tokens, with_prefill)
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 470, in _sync_metadata_across_dp
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     dist.all_reduce(packed_tensor, group=get_dp_group().cpu_group)
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/c10d_logger.py", line 81, in wrapper
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/distributed_c10d.py", line 2931, in all_reduce
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     work.wait()
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824] RuntimeError: [/pytorch/third_party/gloo/gloo/transport/tcp/pair.cc:544] Connection closed by peer [135.173.74.3]:59824
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824] Traceback (most recent call last):
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     output = func(*args, **kwargs)
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 254, in determine_available_memory
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     self.model_runner.profile_run()
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2206, in profile_run
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     self._dummy_run(mc2_tokens_capacity,
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2158, in _dummy_run
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     self.drafter.dummy_run(
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/mtp_proposer.py", line 236, in dummy_run
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     ) = self.runner._sync_metadata_across_dp(num_tokens, with_prefill)
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 470, in _sync_metadata_across_dp
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     dist.all_reduce(packed_tensor, group=get_dp_group().cpu_group)
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/c10d_logger.py", line 81, in wrapper
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/distributed_c10d.py", line 2931, in all_reduce
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     work.wait()
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824] RuntimeError: [/pytorch/third_party/gloo/gloo/transport/tcp/pair.cc:544] Connection closed by peer [135.173.74.3]:59824
(Worker_DP2_TP3_EP11 pid=9291) ERROR 01-19 05:53:08 [multiproc_executor.py:824] 
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824] WorkerProc hit an exception.
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824] Traceback (most recent call last):
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     output = func(*args, **kwargs)
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 254, in determine_available_memory
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     self.model_runner.profile_run()
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2206, in profile_run
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     self._dummy_run(mc2_tokens_capacity,
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2158, in _dummy_run
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     self.drafter.dummy_run(
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/mtp_proposer.py", line 236, in dummy_run
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     ) = self.runner._sync_metadata_across_dp(num_tokens, with_prefill)
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 470, in _sync_metadata_across_dp
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     dist.all_reduce(packed_tensor, group=get_dp_group().cpu_group)
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/c10d_logger.py", line 81, in wrapper
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/distributed_c10d.py", line 2931, in all_reduce
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     work.wait()
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824] RuntimeError: [/pytorch/third_party/gloo/gloo/transport/tcp/pair.cc:544] Connection closed by peer [135.173.74.3]:8628
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824] Traceback (most recent call last):
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     output = func(*args, **kwargs)
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 254, in determine_available_memory
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     self.model_runner.profile_run()
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2206, in profile_run
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     self._dummy_run(mc2_tokens_capacity,
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2158, in _dummy_run
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     self.drafter.dummy_run(
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/mtp_proposer.py", line 236, in dummy_run
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     ) = self.runner._sync_metadata_across_dp(num_tokens, with_prefill)
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 470, in _sync_metadata_across_dp
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     dist.all_reduce(packed_tensor, group=get_dp_group().cpu_group)
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/c10d_logger.py", line 81, in wrapper
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/distributed_c10d.py", line 2931, in all_reduce
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824]     work.wait()
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824] RuntimeError: [/pytorch/third_party/gloo/gloo/transport/tcp/pair.cc:544] Connection closed by peer [135.173.74.3]:8628
(Worker_DP2_TP2_EP10 pid=9251) ERROR 01-19 05:53:08 [multiproc_executor.py:824] 
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824] WorkerProc hit an exception.
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824] Traceback (most recent call last):
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     output = func(*args, **kwargs)
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 254, in determine_available_memory
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     self.model_runner.profile_run()
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2206, in profile_run
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     self._dummy_run(mc2_tokens_capacity,
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2158, in _dummy_run
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     self.drafter.dummy_run(
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/mtp_proposer.py", line 236, in dummy_run
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     ) = self.runner._sync_metadata_across_dp(num_tokens, with_prefill)
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 470, in _sync_metadata_across_dp
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     dist.all_reduce(packed_tensor, group=get_dp_group().cpu_group)
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/c10d_logger.py", line 81, in wrapper
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/distributed_c10d.py", line 2931, in all_reduce
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     work.wait()
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824] RuntimeError: [/pytorch/third_party/gloo/gloo/transport/tcp/pair.cc:544] Connection closed by peer [135.173.74.3]:46499
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824] Traceback (most recent call last):
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     output = func(*args, **kwargs)
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]              ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/worker.py", line 254, in determine_available_memory
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     self.model_runner.profile_run()
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2206, in profile_run
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     self._dummy_run(mc2_tokens_capacity,
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2158, in _dummy_run
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     self.drafter.dummy_run(
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/spec_decode/mtp_proposer.py", line 236, in dummy_run
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     ) = self.runner._sync_metadata_across_dp(num_tokens, with_prefill)
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/vllm-workspace/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 470, in _sync_metadata_across_dp
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     dist.all_reduce(packed_tensor, group=get_dp_group().cpu_group)
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/c10d_logger.py", line 81, in wrapper
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     return func(*args, **kwargs)
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]            ^^^^^^^^^^^^^^^^^^^^^
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]   File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/distributed/distributed_c10d.py", line 2931, in all_reduce
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824]     work.wait()
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824] RuntimeError: [/pytorch/third_party/gloo/gloo/transport/tcp/pair.cc:544] Connection closed by peer [135.173.74.3]:46499
(Worker_DP2_TP1_EP9 pid=9208) ERROR 01-19 05:53:09 [multiproc_executor.py:824] 
(EngineCore_DP2 pid=9164) [2026-01-19 05:53:09] ERROR patch_balance_schedule.py:670: EngineCore failed to start.
(EngineCore_DP2 pid=9164) Traceback (most recent call last):
(EngineCore_DP2 pid=9164)   File "/vllm-workspace/vllm-ascend/vllm_ascend/patch/platform/patch_balance_schedule.py", line 657, in run_engine_core
(EngineCore_DP2 pid=9164)     engine_core = BalanceDPEngineCoreProc(*args, **kwargs)
(EngineCore_DP2 pid=9164)                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP2 pid=9164)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 1159, in __init__
(EngineCore_DP2 pid=9164)     super().__init__(
(EngineCore_DP2 pid=9164)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 637, in __init__
(EngineCore_DP2 pid=9164)     super().__init__(
(EngineCore_DP2 pid=9164)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 109, in __init__
(EngineCore_DP2 pid=9164)     num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches(
(EngineCore_DP2 pid=9164)                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP2 pid=9164)   File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 240, in _initialize_kv_caches
(EngineCore_DP2 pid=9164)     available_gpu_memory = self.model_executor.determine_available_memory()
(EngineCore_DP2 pid=9164)                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP2 pid=9164)   File "/vllm-workspace/vllm/vllm/v1/executor/abstract.py", line 126, in determine_available_memory
(EngineCore_DP2 pid=9164)     return self.collective_rpc("determine_available_memory")
(EngineCore_DP2 pid=9164)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore_DP2 pid=9164)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 359, in collective_rpc
(EngineCore_DP2 pid=9164)     return aggregate(get_response())
(EngineCore_DP2 pid=9164)                      ^^^^^^^^^^^^^^
(EngineCore_DP2 pid=9164)   File "/vllm-workspace/vllm/vllm/v1/executor/multiproc_executor.py", line 342, in get_response
(EngineCore_DP2 pid=9164)     raise RuntimeError(
(EngineCore_DP2 pid=9164) RuntimeError: Worker failed with error '[/pytorch/third_party/gloo/gloo/transport/tcp/pair.cc:544] Connection closed by peer [135.173.74.3]:46499', please check the stack trace above for the root cause
```
#### 详细报错日志

[Node0日志记录.log](https://github.com/user-attachments/files/24706429/Node0.log)
[Node1日志记录.log](https://github.com/user-attachments/files/24706430/Node1.log)
