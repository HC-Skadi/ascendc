# Ascend Model Verifier

## Skill Metadata

- **Skill Name**: Ascend Model Verifier
- **Version**: 1.0.0
- **Category**: DevOps / AI Infrastructure
- **Target Platform**: Huawei Ascend NPU
- **Skill Path**: `/home/jiaozeyu/agent/skills/Ascend_Model_Verifier`

## Skill Goal

自动、持续地发现、验证、归档开源大模型在华为昇腾NPU上的适配情况，构建一个可运行的昇腾模型生态知识库。

## Core Design Principles

采用多Agent协作、解耦架构。每个Agent负责单一职责，通过文件系统（特定路径下的脚本、列表、结果文件夹）和状态（如文件存在与否）进行通信与协同。

## Environment Requirements

- **Hardware**: Huawei Ascend NPU (910B/310B series)
- **vLLM Version**: 0.17.0
- **vLLM-Ascend Plugin**: 0.17.0
- **Python**: 3.8+
- **Dependencies**: 
  - `modelscope`
  - `huggingface_hub`
  - `requests`
  - `beautifulsoup4`

## Directory Structure

```
Ascend_Model_Verifier/
├── SKILL.md                          # 本技能定义文件
├── scripts/                          # 各Agent所需脚本
│   ├── crawler_huggingface.py        # Agent1: HF爬虫
│   ├── crawler_modelscope.py         # Agent1: ModelScope爬虫
│   ├── merge_model_lists.py          # Agent1: 列表合并
│   ├── download_model.py             # Agent2: 模型下载
│   ├── run_vllm_benchmark.py         # Agent3: vLLM验证
│   ├── check_npu_status.py           # Agent3: NPU状态检查
│   ├── generate_adaptation_guide.py  # Agent4: 适配指南生成
│   ├── generate_error_log.py         # Agent4: 错误日志生成
│   ├── archive_and_upload.py         # Agent5: 归档上传
│   └── coordinator.py                # 总协调器
├── reference/                        # 参考文档
│   ├── features.md                   # 功能特性文档
│   ├── deployment.md                 # 部署指南
│   ├── models.md                     # 模型部署示例
│   ├── quantization.md              # 量化指南
│   ├── troubleshooting.md            # 故障排除
│   └── faq.md                       # 常见问题
├── results/                          # 验证结果目录
│   └── <model_name>/                # 各模型结果
└── downloaded_models/                # 下载的模型权重
```

## Agent Architecture

### Agent1: Hot Model Retriever (热点模型检索器)

**职责**: 从HuggingFace和ModelScope平台爬取最新的热点模型列表。

### Agent2: Model Filter & Downloader (模型筛选与下载器)

**职责**: 从热点列表中筛选可验证的模型，并下载第一个待验证的模型。

**筛选规则**:
- 过滤参数总量 > 300B 的模型
- 跳过已处理的模型

### Agent3: Ascend NPU Validator (昇腾NPU验证器)

**职责**: 在华为昇腾设备上使用vLLM进行基准测试验证。

### Agent4: Result Checker & Doc Generator (结果校验与文档生成器)

**职责**: 根据验证结果生成适配指南或错误日志。

### Agent5: Archiver & Uploader (归档上传器)

**职责**: 将单个模型的完整验证结果归档并上传至代码仓库。

## 执行方式

```bash
# 单次运行
python scripts/coordinator.py --once

# 持续运行
python scripts/coordinator.py --continuous
```

## 标记文件协议

| 标记文件 | 创建者 | 含义 |
|---------|-------|------|
| `download.complete` | Agent2 | 模型下载完成 |
| `validation.complete` | Agent3 | 验证完成 |
| `documentation.complete` | Agent4 | 文档生成完成 |
