# Issue #16: 在运行 vLLM 的 benchmark_latency.py 时，出现 NotImplementedError: 'vllm::all_reduce' 错误

## 基本信息

- **编号**: #16
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/16
- **创建时间**: 2025-02-06T15:04:14Z
- **关闭时间**: 2025-02-10T02:36:09Z
- **更新时间**: 2025-02-11T13:25:46Z
- **提交者**: @imsatoshi
- **评论数**: 2

## 标签

无

## 问题描述

---

### **Issue Description**
在运行 vLLM 的 `benchmark_latency.py` 时，出现 `NotImplementedError: 'vllm::all_reduce'` 错误，且日志提示该算子不支持 NPU 后端，回退到 CPU 执行导致失败。

### **Environment**
- **操作系统**:  openeuler24.03-lts
- **硬件**: Ascend NPU
- **PyTorch 版本**:   2.5.1rc
- **vLLM 版本**:  0.1.dev1+gc786e75.empty

### **复现步骤**

 运行 benchmark 脚本：
   ```bash
   python benchmarks/benchmark_latency.py 

python benchmark_latency.py \
  --model /path/to/Qwen2.5-Coder-32B-Instruct \
  --tensor-parallel-size 2 \
  --input-len 1024 \
  --output-len 20 \
  --batch-size 4

   ```

### **错误日志（关键部分）**
```
[ERROR] 未实现的操作符错误：
NotImplementedError: Could not run 'vllm::all_reduce' with arguments from the 'CPU' backend.

[警告] NPU 支持问题：
Warning: CAUTION: The operator 'vllm::all_reduce' is not currently supported on the NPU backend and will fall back to run on the CPU.

[关键堆栈跟踪]:
File "/data01/vllm-ascend/vllm_ascend/worker.py", line 220, in determine_num_available_blocks
    self.model_runner.profile_run()
File "/data01/vllm-ascend/vllm_ascend/model_runner.py", line 1386, in profile_run
    self.execute_model(model_input, kv_caches, intermediate_tensors)
File "/usr/local/lib/python3.11/site-packages/vllm/distributed/parallel_state.py", line 357, in all_reduce
    return torch.ops.vllm.all_reduce(input_, group_name=self.unique_name)
```

### **预期行为**
`vllm::all_reduce` 算子应在 NPU/GPU 上正常运行，成功完成分布式计算。

### **可能原因**
1. **NPU 算子未适配**: vLLM 的 `all_reduce` 算子未实现 NPU 后端支持。
2. **设备映射错误**: 程序未正确识别 NPU 设备，回退到 CPU 执行。
3. **分支兼容性问题**: 使用的 `vllm-ascend` 分支可能存在与主分支的兼容性问题。

