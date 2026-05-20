# vLLM Ascend 故障排除指南

> 本文档提供常见问题的诊断和解决方案
> 来源: https://docs.vllm.ai/projects/ascend/en/latest/

## 常见错误及解决方案

### 1. NPU 不可用

#### 症状
```
RuntimeError: NPU not found
```

#### 诊断步骤

```bash
# 检查NPU驱动
npu-smi info

# 检查NPU设备
npu-smi -l

# 查看驱动版本
npu-smi -v
```

#### 解决方案

1. **确认驱动安装**:
```bash
# 安装昇腾驱动
# 参考: https://www.hiascend.com/
```

2. **设置环境变量**:
```bash
export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3
```

3. **检查设备权限**:
```bash
ls -la /dev/npu*
# 如无权限,添加用户组
sudo usermod -a -G npu $USER
```

### 2. 内存不足 (OOM)

#### 症状
```
RuntimeError: NPU out of memory
```

#### 诊断步骤

```bash
# 检查NPU内存使用
npu-smi info -q -d memory
```

#### 解决方案

1. **减少最大序列长度**:
```python
llm = LLM(
    model=model_path,
    max_model_len=2048  # 减小此值
)
```

2. **降低内存利用率**:
```bash
vllm serve ... --gpu-memory-utilization 0.8
```

3. **启用内存优化**:
```bash
export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True
```

4. **使用量化模型**:
```bash
# 使用W4A8量化模型
--quantization ascend
```

5. **增加张量并行度**:
```bash
--tensor-parallel-size 4
```

### 3. 导入错误

#### 症状
```
ImportError: No module named 'vllm'
ModuleNotFoundError: No module named 'torch_npu'
```

#### 解决方案

1. **安装vLLM**:
```bash
pip install vllm==0.17.0
pip install vllm-ascend==0.17.0
```

2. **检查Python环境**:
```python
import sys
print(sys.executable)
print(sys.path)
```

3. **验证CANN安装**:
```bash
source /usr/local/Ascend/ascend-toolkit/set_env.sh
python -c "import torch; print(torch.__version__)"
```

### 4. 模型加载失败

#### 症状
```
OSError: Model not found
ValueError: Invalid model_id
```

#### 解决方案

1. **确认模型路径**:
```bash
ls -la /path/to/your/model
```

2. **下载模型**:
```bash
# 使用ModelScope
export VLLM_USE_MODELSCOPE=true
vllm serve modelscope.cn/xxx/xxx

# 使用HuggingFace
huggingface-cli download org/model-name
```

3. **检查模型格式**:
```bash
# 确认必要文件存在
ls config.json tokenizer.json
```

### 5. 量化错误

#### 症状
```
ValueError: Quantization not supported
RuntimeError: Model is not quantized
```

#### 解决方案

1. **确认量化安装**:
```bash
pip list | grep ascend
```

2. **使用正确量化参数**:
```python
llm = LLM(
    model=quantized_model_path,
    quantization="ascend"  # 必须指定
)
```

3. **使用量化版模型**:
```bash
# 使用已量化模型
vllm serve vllm-ascend/Qwen3-8B-w4a8
```

### 6. 推理超时

#### 症状
```
TimeoutError: Inference timeout
```

#### 解决方案

1. **增加超时时间**:
```bash
export VLLM_EXECUTE_MODEL_TIMEOUT_SECONDS=30000
export VLLM_RPC_TIMEOUT=3600000
```

2. **检查NPU资源占用**:
```bash
npu-smi info
```

3. **减少批处理大小**:
```bash
--max-num-batched-tokens 1024
```

### 7. 多节点通信错误

#### 症状
```
RuntimeError: HCCL communication error
```

#### 解决方案

1. **检查网络配置**:
```bash
# 确认网络连通性
ping other_node_ip

# 检查端口
nc -zv other_node_ip 8000
```

2. **配置网络环境变量**:
```bash
export HCCL_IF_IP=192.168.1.1
export GLOO_SOCKET_IFNAME=eth0
export TP_SOCKET_IFNAME=eth0
```

3. **检查防火墙**:
```bash
sudo ufw status
sudo firewall-cmd --list-ports
```

## 性能问题

### 推理速度慢

#### 诊断

1. **检查GPU利用率**:
```bash
npu-smi info -q -d utilization
```

2. **分析性能瓶颈**:
```bash
# 启用profiler
vllm serve ... --profiler-config '{"profiler": "torch"}'
```

#### 优化建议

1. **启用CUDA Graph**:
```bash
--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}'
```

2. **启用异步调度**:
```bash
--async-scheduling
```

3. **使用量化**:
```bash
--quantization ascend
```

4. **启用前缀缓存**:
```bash
--enable-prefix-caching
```

### 内存泄漏

#### 诊断

```python
import torch
print(torch.npu.memory_allocated())
print(torch.npu.memory_reserved())
```

#### 解决方案

```python
# 正确清理
del llm
gc.collect()
torch.npu.empty_cache()
```

## 调试技巧

### 1. 启用详细日志

```bash
export VLLM_LOGGING_LEVEL=DEBUG
vllm serve ...
```

### 2. 使用CPU测试

```bash
# 设置SOC_VERSION
export SOC_VERSION="ascend910b1"
python -c "import vllm; print(vllm.__version__)"
```

### 3. 检查依赖版本

```bash
pip list | grep -E "torch|npu|vllm"
python -c "import torch; print(torch.__version__)"
python -c "import torch_npu; print(torch_npu.__version__)"
python -c "import vllm; print(vllm.__version__)"
```

### 4. 验证环境

```python
import torch
import torch_npu
import vllm

print(f"PyTorch: {torch.__version__}")
print(f"CUDA Available: {torch.cuda.is_available()}")
print(f"NPU Available: {torch.npu.is_available()}")
print(f"vLLM: {vllm.__version__}")
```

## 日志位置

### vLLM日志

```bash
# 默认日志
~/.vllm/logs/

# 查看日志
ls -la ~/.vllm/logs/
cat ~/.vllm/logs/vllm.log
```

### NPU日志

```bash
# CANN日志
/var/log/ascend-secure/

# NPU驱动日志
dmesg | grep -i npu
```

## 获取帮助

### 1. 查看官方文档

- [vLLM Ascend 文档](https://docs.vllm.ai/projects/ascend/en/latest/)
- [华为昇腾文档](https://www.hiascend.com/)

### 2. GitHub Issues

如遇无法解决的问题,请提交Issue:
- https://github.com/vllm-project/vllm-ascend/issues

### 3. 社区支持

- 加入vLLM Discord
- 访问华为昇腾社区

---

*本文档由 Ascend Model Verifier 自动整理*
*最后更新: 2025-03-18*
