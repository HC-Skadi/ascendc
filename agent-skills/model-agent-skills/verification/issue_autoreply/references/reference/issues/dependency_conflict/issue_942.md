# Issue #942: [Bug]: stateless_init_process_group is invalid on NPUs

## 基本信息

- **编号**: #942
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/942
- **创建时间**: 2025-05-24T07:35:39Z
- **关闭时间**: 2025-06-23T02:26:50Z
- **更新时间**: 2025-06-23T02:26:50Z
- **提交者**: @janelu9
- **评论数**: 3

## 标签

bug

## 问题描述

### Your current environment

```
PyTorch version: 2.5.1
Is debug build: False

OS: Ubuntu 22.04.5 LTS (aarch64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 4.0.0
Libc version: glibc-2.35

Python version: 3.10.17 (main, Apr 30 2025, 16:00:31) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-4.19.90-89.11.v2401.ky10.aarch64-aarch64-with-glibc2.35

CPU:
Architecture:                       aarch64
CPU op-mode(s):                     64-bit
Byte Order:                         Little Endian
CPU(s):                             192
On-line CPU(s) list:                0-191
Vendor ID:                          HiSilicon
BIOS Vendor ID:                     HiSilicon
Model name:                         Kunpeng-920
BIOS Model name:                    HUAWEI Kunpeng 920 5250
Model:                              0
Thread(s) per core:                 1
Core(s) per socket:                 48
Socket(s):                          4
Stepping:                           0x1
Frequency boost:                    disabled
CPU max MHz:                        2600.0000
CPU min MHz:                        200.0000
BogoMIPS:                           200.00
Flags:                              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma dcpop asimddp asimdfhm ssbs
L1d cache:                          12 MiB (192 instances)
L1i cache:                          12 MiB (192 instances)
L2 cache:                           96 MiB (192 instances)
L3 cache:                           192 MiB (8 instances)
NUMA node(s):                       8
NUMA node0 CPU(s):                  0-23
NUMA node1 CPU(s):                  24-47
NUMA node2 CPU(s):                  48-71
NUMA node3 CPU(s):                  72-95
NUMA node4 CPU(s):                  96-119
NUMA node5 CPU(s):                  120-143
NUMA node6 CPU(s):                  144-167
NUMA node7 CPU(s):                  168-191
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit:        Not affected
Vulnerability L1tf:                 Not affected
Vulnerability Mds:                  Not affected
Vulnerability Meltdown:             Not affected
Vulnerability Mmio stale data:      Not affected
Vulnerability Retbleed:             Not affected
Vulnerability Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:           Mitigation; __user pointer sanitization
Vulnerability Spectre v2:           Not affected
Vulnerability Srbds:                Not affected
Vulnerability Tsx async abort:      Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] pyzmq==26.4.0
[pip3] torch==2.5.1
[pip3] torch-npu==2.5.1
[pip3] torchvision==0.20.1
[pip3] transformers==4.51.3
[conda] Could not collect
vLLM Version: 0.8.5.post1
vLLM Ascend Version: 0.8.5rc1

ENV Variables:
ATB_OPSRUNNER_KERNEL_CACHE_TILING_SIZE=10240
ATB_OPSRUNNER_KERNEL_CACHE_LOCAL_COUNT=1
ATB_STREAM_SYNC_EVERY_RUNNER_ENABLE=0
ATB_OPSRUNNER_SETUP_CACHE_ENABLE=1
ATB_WORKSPACE_MEM_ALLOC_GLOBAL=0
ATB_DEVICE_TILING_BUFFER_BLOCK_NUM=32
ATB_STREAM_SYNC_EVERY_KERNEL_ENABLE=0
ATB_OPSRUNNER_KERNEL_CACHE_GLOABL_COUNT=5
ATB_HOME_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0
ASCEND_TOOLKIT_HOME=/usr/local/Ascend/ascend-toolkit/latest
ATB_COMPARE_TILING_EVERY_KERNEL=0
ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
LD_LIBRARY_PATH=/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_0/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/lib:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/examples:/usr/local/Ascend/nnal/atb/latest/atb/cxx_abi_1/tests/atbopstest:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling:/usr/local/Ascend/driver/lib64/common/:/usr/local/Ascend/driver/lib64/driver/:
ASCEND_AICPU_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_OPSRUNNER_KERNEL_CACHE_TYPE=3
ATB_RUNNER_POOL_SIZE=64
ATB_STREAM_SYNC_EVERY_OPERATION_ENABLE=0
ASCEND_HOME_PATH=/usr/local/Ascend/ascend-toolkit/latest
ATB_MATMUL_SHUFFLE_K_ENABLE=1
ATB_LAUNCH_KERNEL_WITH_TILING=1
ATB_WORKSPACE_MEM_ALLOC_ALG_TYPE=1
ATB_HOST_TILING_BUFFER_BLOCK_NUM=128
ATB_SHARE_MEMORY_NAME_SUFFIX=
TORCH_DEVICE_BACKEND_AUTOLOAD=1
PYTORCH_NVML_BASED_CUDA_CHECK=1
TORCHINDUCTOR_COMPILE_THREADS=1


NPU:
+------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0.3                 Version: 24.1.0.3                                             |
+---------------------------+---------------+----------------------------------------------------+
| NPU   Name                | Health        | Power(W)    Temp(C)           Hugepages-Usage(page)|
| Chip                      | Bus-Id        | AICore(%)   Memory-Usage(MB)  HBM-Usage(MB)        |
+===========================+===============+====================================================+
| 0     910B3               | OK            | 98.1        41                0    / 0             |
| 0                         | 0000:C1:00.0  | 0           0    / 0          3389 / 65536         |
+===========================+===============+====================================================+
| 1     910B3               | OK            | 93.6        40                0    / 0             |
| 0                         | 0000:C2:00.0  | 0           0    / 0          3380 / 65536         |
+===========================+===============+====================================================+
| 2     910B3               | OK            | 86.6        39                0    / 0             |
| 0                         | 0000:81:00.0  | 0           0    / 0          3379 / 65536         |
+===========================+===============+====================================================+
| 3     910B3               | OK            | 96.2        43                0    / 0             |
| 0                         | 0000:82:00.0  | 0           0    / 0          3380 / 65536         |
+===========================+===============+====================================================+
| 4     910B3               | OK            | 96.5        45                0    / 0             |
| 0                         | 0000:01:00.0  | 0           0    / 0          3378 / 65536         |
+===========================+===============+====================================================+
| 5     910B3               | OK            | 97.4        46                0    / 0             |
| 0                         | 0000:02:00.0  | 0           0    / 0          3381 / 65536         |
+===========================+===============+====================================================+
| 6     910B3               | OK            | 100.0       45                0    / 0             |
| 0                         | 0000:41:00.0  | 0           0    / 0          3380 / 65536         |
+===========================+===============+====================================================+
| 7     910B3               | OK            | 94.8        45                0    / 0             |
| 0                         | 0000:42:00.0  | 0           0    / 0          3379 / 65536         |
+===========================+===============+====================================================+
+---------------------------+---------------+----------------------------------------------------+
| NPU     Chip              | Process id    | Process name             | Process memory(MB)      |
+===========================+===============+====================================================+
| No running processes found in NPU 0                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 1                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 2                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 3                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 4                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 5                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 6                                                            |
+===========================+===============+====================================================+
| No running processes found in NPU 7                                                            |
+===========================+===============+====================================================+

CANN:
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux

```

### 🐛 Describe the bug

```
import torch
import torch_npu
from torch_npu.contrib import transfer_to_npu
import multiprocessing as mp
from vllm.distributed.device_communicators.pynccl import PyNcclCommunicator

def stateless_init_process_group(master_address, master_port, rank, world_size, device):
    from vllm.distributed.device_communicators.pynccl import PyNcclCommunicator
    from vllm.distributed.utils import StatelessProcessGroup
    pg = StatelessProcessGroup.create(
        host=master_address,
        port=master_port,
        rank=rank,
        world_size=world_size
    )
    pynccl = PyNcclCommunicator(pg, device=device)
    return pynccl

def worker(rank, world_size, master_address, master_port):
    # 设置 CUDA 设备 (假设单机多卡)
    torch.cuda.set_device(f"cuda:{rank % torch.cuda.device_count()}")
    
    # 初始化自定义进程组
    pynccl = stateless_init_process_group(
        master_address=master_address,
        master_port=master_port,
        rank=rank,
        world_size=world_size,
        device=f"cuda:{rank % torch.cuda.device_count()}"
    )
    
    # 测试张量
    if rank == 0:
        # Rank 0 发送全1张量
        send_tensor = torch.ones(4, 4, device="cuda")
        print(f"[Rank {rank}] Sending: {send_tensor}")
        pynccl.broadcast(send_tensor, src=0)
    else:
        # Rank 1 接收并验证
        recv_tensor = torch.empty(4, 4, device="cuda")
        pynccl.broadcast(recv_tensor, src=0)
        print(f"[Rank {rank}] Received: {recv_tensor}")
        assert torch.allclose(recv_tensor, torch.ones(4, 4, device="cuda")), "Data mismatch!"

if __name__ == "__main__":
    # 配置参数
    master_address = "127.0.0.1"  # 本地测试用回环地址
    master_port = 29500           # 确保端口未被占用
    world_size = 2
    
    # 启动两个进程 (模拟两个节点)
    processes = []
    for rank in range(world_size):
        p = mp.Process(
            target=worker,
            args=(rank, world_size, master_address, master_port)
        )
        p.start()
        processes.append(p)
    
    # 等待所有进程完成
    for p in processes:
        p.join()
    
    print("Test passed!")
```

```
[Rank 1] Received: tensor([[0., 0., 0., 0.],
        [0., 0., 0., 0.],
        [0., 0., 0., 0.],
        [0., 0., 0., 0.]], device='npu:1')
[Rank 0] Sending: tensor([[1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.]], device='npu:0')
/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py:108: ResourceWarning: unclosed <                                                      socket.socket fd=89, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>
  self._target(*self._args, **self._kwargs)
Process Process-2:
Traceback (most recent call last):
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 314, in _bootstra                                                      p
    self.run()
  File "/usr/local/python3.10.17/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/mnt/test.py", line 42, in worker
    assert torch.allclose(recv_tensor, torch.ones(4, 4, device="cuda")), "Data mismatch!"
AssertionError: Data mismatch!
```

Do we have any other alternative methods?
