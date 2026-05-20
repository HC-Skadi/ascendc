# msprobe Dump 指南

## 使用目的

只有在 loss、任务指标或样例输出层面已经确认存在真实不一致时，才使用本指南。不要在配置层面问题还没排除前，直接进入全量 dump。

## 先看官方文档

不同版本工具的命令格式、参数名和支持流程都可能变化。如果本地没有所需文档，先加载 `web-access` 查看 Ascend 官方精度工具文档，再写命令。

不要只看单页，要从整套文档入手。用户给出的这个锚点可以作为入口：

- `https://gitcode.com/Ascend/mstt/blob/tag_MindStudio_8.2.RC1.B020_001/debug/accuracy_tools/msprobe/docs/05.data_dump_PyTorch.md#25-%E6%8E%A8%E7%90%86%E6%A8%A1%E5%9E%8B%E9%87%87%E9%9B%86%E6%8C%87%E5%AE%9Atoken_range`

同时查看相邻文档，确保流程与实际安装版本一致。

## 采集前准备

尽量缩小复现范围：

- 单卡
- 单进程
- 固定 seed
- 最小 batch size
- 最小样本量
- 稳定输入 shape
- 对生成式模型固定 decode 设置

固定能够稳定暴露问题的样本或 token 窗口。

## 需要采集什么

只采集能定位第一处漂移所需的最小证据：

- 输入 tensor
- 最终输出或 logits
- 靠近可疑 layer 的关键中间 tensor
- tensor 元数据：dtype、shape、layout、scale、device
- 运行元数据：代码版本、checkpoint、命令、环境版本

对于序列模型或生成式模型，优先固定 `token_range` 或某一个 decoding step，不要一上来 dump 全序列。

## 定位策略

采用逐步收缩范围的方式，不要一开始就全量 dump。

1. 先确认固定样本上的最终输出确实不同。
2. 比较最后一个 block 或最后一个关键中间 tensor。
3. 逐步向前回溯，直到找到最后一个仍然一致的点。
4. 将问题缩小到第一处漂移的 block、算子或 layout 变换位置。

这种近似二分的定位方式通常比全层 dump 更快，也更容易得到可行动证据。

## Manifest 要求

写一份 manifest，保证基线与昇腾侧产物可以准确配对。至少记录：

- 样本标识
- dump 范围
- layer 或 token range
- 文件名和目录
- 命令行
- 版本与环境变量

## 常见错误

- 比较了不同样本或顺序不一致的数据
- 忘记固定随机种子
- dump 了动态 shape，却没有记录实际 shape
- 比较的是不同后处理阶段的 tensor
- 没有记录 dtype 转换或 scale 状态
- 一开始 scope 太大，导致结果不可操作
