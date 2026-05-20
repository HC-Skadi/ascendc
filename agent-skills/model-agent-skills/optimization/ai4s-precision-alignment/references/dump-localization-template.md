# Dump 定位模板

## 使用目的

当训练或推理层面的比较已经确认存在真实差异时，用本模板组织 dump 采集和首漂移定位，避免无边界全量 dump。

## 采集前确认

- GPU 基线来源已确认
- 昇腾侧结果已确认
- 已缩小到最小可复现样本
- 已固定 seed、batch size、shape 与 decode 参数
- 已确认要比较的是同一输入、同一阶段、同一后处理边界

## 推荐目录

```text
dump/
  gpu/
    manifest.json
    tensors/
  ascend/
    manifest.json
    tensors/
  compare/
    notes.md
```

`manifest.json` 可参考 `assets/templates/dump-manifest.example.json`。

## 首漂移定位步骤

1. 固定一个最小样本或固定 `token_range`
2. 先确认最终输出确实不同
3. 对比最后一个关键 block 的输出
4. 如果最后一个关键 block 已不同，继续向前回溯
5. 找到最后一个相同点和第一个不同点
6. 将问题缩小到 block、算子、layout 变换或 dtype 边界

## 必须记录的字段

- 模型名与版本
- 样本标识
- token range 或 step
- dump 范围
- 输入输出文件路径
- 运行命令
- 关键环境变量
- 框架、驱动、固件、工具版本

## 输出模板

可以按以下格式返回：

```text
问题范围：
  第一个不一致位置：
  最后一个一致位置：

证据：
  GPU 文件：
  Ascend 文件：
  对比命令：

高概率原因：
  1.
  2.

下一步：
  1.
  2.
```

## 升级条件

只有在推理输出或任务指标已经明确失配，而且不能通过配置差异解释时，才进入本模板。
