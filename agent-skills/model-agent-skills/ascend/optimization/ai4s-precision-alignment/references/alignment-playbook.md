# 对齐执行手册

## 目录

1. 对比约束
2. 基线来源确认
3. 训练精度对齐
4. 推理精度对齐
5. 如何理解偏差模式
6. 报告与结论约束

## 对比约束

在比较任何数值之前，先固定对比约束。

至少记录以下项目：

- 模型仓库、分支和 commit
- checkpoint 路径或权重转换步骤
- 数据集版本和具体 split
- seed 与数据顺序控制方式
- batch size、梯度累积和等效全局 batch size
- 精度模式，例如 `fp32`、`fp16`、`bf16`
- 优化器、scheduler、warmup 和 loss scaling
- 分布式拓扑和 reduction 行为
- 指标定义与聚合方式

任何缺失项都可能是精度不一致的来源。

## 基线来源确认

在进入训练或推理对齐前，先确认基线来自哪里。

优先级如下：

1. 官方 README、官方示例、官方 benchmark 或官方文档
2. 用户提供的 GPU 真实运行结果

执行顺序必须是：

1. 先检查官方资料中是否已有可直接比较的标准结果
2. 只有官方资料不足时，才向用户确认 GPU 基线来源
3. 在前两步都没有完成前，不要先写或运行精度对比脚本
4. 不要因为本地 CPU 路径容易跑通，就默认做 CPU vs NPU

如果用户已经提供本地目录，先读取 `references/baseline-bundle-spec.md`，并运行：

```bash
python scripts/scan_baseline_bundle.py /path/to/bundle
```

## 训练精度对齐

### 第一步：确认训练基线

- 官方训练日志、官方收敛曲线或官方指标存在时，优先使用这些结果。
- 官方训练基线不存在时，先询问用户 GPU 训练结果来源。
- 不要先写 CPU 训练对比脚本，再回头确认基线来源。

### 第二步：收集可比较日志

收集相同训练窗口内的基线日志和昇腾日志。优先保证 step 或 epoch 数一致，以及日志打印频率一致。

如果用户给的是目录而不是单个日志文件，先运行：

```bash
python scripts/scan_baseline_bundle.py /path/to/bundle --expect training
```

然后优先使用 `scripts/compare_loss.py`：

```bash
python scripts/compare_loss.py baseline.log ascend.log
python scripts/compare_loss.py baseline.log ascend.log --metric loss --metric val_loss
python scripts/compare_loss.py baseline.log ascend.log --export-csv-dir out
```

### 第三步：比较稳定信号

按以下顺序比较：

1. 最终 `val_loss` 或 `test_loss`
2. 最终训练 `loss`
3. 整体趋势是否一致
4. 波动性和尖峰情况

阈值应在比较前声明。没有项目阈值时，只能把结果写成“在当前比较条件下观察到的差异”，不要事后改阈值再直接写成“全部通过”。

### 第四步：定位失配类型

根据偏差模式决定下一步排查方向。

- 从第一步就开始漂移：
  优先检查预处理、随机性、checkpoint 加载、未支持算子以及 dtype 提升或截断。
- 前期一致，后期逐渐偏离：
  优先检查优化器状态、梯度缩放、reduction 语义、scheduler 触发时机以及累积边界。
- 训练 loss 接近，但验证 loss 偏离：
  优先检查 eval mode、dropout 是否关闭、预处理、标签处理与指标聚合逻辑。

## 推理精度对齐

### 第一步：找到官方基线

先检查模型 README、官方示例、benchmark 表格或源码注释。

优先级建议如下：

1. 官方给出的确定性样例及精确输出
2. 官方 benchmark 指标和固定评测脚本
3. 同项目历史可信运行结果

如果官方已经给出示例值，就直接比较 NPU 输出与官方值。不要因为当前有本地 PyTorch 模型，就改成 CPU 对比。

### 第二步：官方基线不足时，询问用户 GPU 基线

只有在官方基线不足时，才向用户确认 GPU 结果来源。此时读取 `references/baseline-policy.md`。

### 第三步：固定完整推理约束

在比较输出前，固定以下全部条件：

- checkpoint 与权重转换方式
- tokenizer 或特征提取器
- 输入归一化和 padding
- prompt 模板或 system prompt
- 采样与解码参数
- 后处理与阈值逻辑
- batch shape 与动态 shape 设置

### 第四步：分两层比较

先比较任务级指标，再比较同一输入集上的逐样本输出。

优先使用：

```bash
python scripts/compare_inference.py gpu/metrics.json ascend/metrics.json
python scripts/compare_inference.py gpu/predictions.jsonl ascend/predictions.jsonl
python scripts/compare_inference.py gpu/ ascend/
```

如果官方只提供样例输出，最终报告必须限制在“样例级推理对齐”范围，不能直接宣称整个模型已完成对齐。

## 如何理解偏差模式

- 数值有轻微漂移，但任务指标一致：
  通常停留在指标层即可，不一定要做 dump。
- 只有长序列场景下指标漂移：
  优先缩小到 token range、attention mask 或 decode step。
- 某一类 layer 开始漂移，而更早层一致：
  优先怀疑第一处漂移附近的算子、融合 kernel、layout 变换或 dtype 边界。
- 只有转换后的 checkpoint 出问题：
  重新检查 key 映射、转置规则、缺失 buffer 以及默认 dtype 变化。

## 报告与结论约束

最终输出必须明确写出：

- 基线来源
- 是否为官方基线、用户 GPU 基线，还是仅 CPU 调试结果
- 比较覆盖范围
- 使用的阈值以及阈值是在比较前还是比较后确定的
- 哪些结论是证据支持的，哪些只是合理推测

禁止以下写法：

- “CPU vs NPU 通过，因此模型已经完成精度对齐”
- “样例输出对齐，因此整个模型训练和推理都完成对齐”
- “先在 1e-4 下 mismatch，再改成 2e-4 后直接写全部 match”，但不解释阈值依据

可选外部工具：

- loss 曲线可视化工具：
  `https://github.com/CurryRice233/TrainingLogParser`
