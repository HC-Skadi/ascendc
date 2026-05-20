#BY|# issue_autoreply
#KM|
#KZ|## Skill Metadata
#RW|
#BV|- **Skill Name**: issue_autoreply
#RH|- **Version**: 1.0.0
#QB|- **Category**: DevOps / AI Infrastructure / Issue Management
#BW|- **Target Platform**: Huawei Ascend NPU, vLLM-ascend
#HK|- **Skill Path**: `/home/jiaozeyu/agent/skills/skills/issue_autoreply`
#SK|
#XZ|## Skill Goal
#TX|
#QB|构建一个能够自动分析、验证并回复 vLLM-ascend 项目中处于"开启(open)"状态 Issue 的智能体工作流。该技能将集成项目源码、历史 FAQ 知识库以及本地昇腾（Ascend）NPU 硬件资源，实现对 Issue 的智能诊断、实验复现、验证解决的全流程自动化，最终生成可直接用于回复 Issue 的、包含根本原因分析、解决方案及验证结果的结构化内容。
#BY|
#WQ|## Core Design Principles
#VP|
#NP|采用多Agent协作架构，三个Agent按顺序执行、紧密协作。通过文件系统（特定路径下的脚本、报告、日志）和状态进行通信与协同。每个Agent职责单一，通过工作流传递信息。
#KS|
#XM|## Environment Requirements
#YQ|
#NY|- **Hardware**: Huawei Ascend NPU (8x NPU devices)
#ZW|- **vLLM Version**: 0.17.0+
#MZ|- **vLLM-Ascend Plugin**: Compatible version
#HM|- **Python**: 3.8+
#VM|- **External Knowledge Base**: FAQ知识库 (https://gitcode.com/raintBN/vLLM_Ascend_FAQ)
#PK|- **GitHub Access**: For fetching and responding to issues
#ZM|
#BR|## External Knowledge Resources
#JQ|
#VX|### FAQ Knowledge Base
#TX|
#QP|必须将【FAQ知识库】（https://gitcode.com/raintBN/vLLM_Ascend_FAQ）的内容作为只读参考资源集成到技能中。该仓库是基于历史已关闭Issue总结的调试指南，将作为首要的问题分析与解决方案参考来源。
#KR|
#BH|## Directory Structure
#HQ|
#ZS|```
#RJ|issue_autoreply/
#QP|├── SKILL.md                          # 本技能定义文件
#KR|├── scripts/                          # 各Agent所需脚本
#XB|│   ├── agent1_analyzer.py           # Agent1: Issue分析与规划
#WP|│   ├── agent2_validator.py          # Agent2: 本地实验验证
#QZ|│   ├── agent3_writer.py            # Agent3: 回复撰写
#VM|│   └── coordinator.py                # 总协调器
#PT|├── reference/                        # 参考文档
#XV|│   ├── workflow.md                   # 工作流说明
#QY|│   ├── faq_integration.md           # FAQ集成指南
#KW|└── templates/                        # 模板文件
#ZN|    ├── analysis_report_template.md  # 分析报告模板
#BN|    ├── validation_report_template.md # 验证报告模板
#TY|    └── reply_template.md             # 回复模板
#YZ|```
#KR|
#BH|## Working Directory
#HQ|
#ZS|技能使用 `/home/jiaozeyu/repo/issue_autoreply/` 作为工作目录，用于存放中间分析报告、验证日志和最终生成的回复文件。
#WR|
#XT|## Agent Architecture
#KR|
#BV|### Agent 1: Issue 分析师与解决思路规划师
#QW|
#XP|**输入**: 一个指定的、处于"open"状态的 vllm-ascend Issue 详情（标题、描述、评论、日志、代码片段等）
#QT|
#NB|**处理逻辑**:
#SN|1. 深度分析：仔细阅读 Issue 描述，理解用户遇到的问题现象、报错信息、环境配置（如 NPU 型号、驱动版本、vLLM 与 vLLM-ascend 版本、模型名称等）
#MJ|2. 知识检索：优先并重点查询【FAQ知识库】。将当前 Issue 的关键词、错误信息与 FAQ 中的条目进行匹配，寻找已知的类似问题及其解决方案
#VM|3. 源码关联：结合 vLLM 及 vLLM-ascend 的源代码，分析问题可能出现的模块（如内核、调度、内存管理、模型适配层等）
#HM|4. 生成方案：综合以上分析，提出一个或多个具体的、可操作的解决思路或验证步骤
#PK|
#ZM|**输出**: 一份详细的分析报告与行动方案，作为下一个 Agent 的输入。报告应包括：
#BR|- 问题摘要
#JQ|- 与【FAQ知识库】的关联情况
#VX|- 初步判断的根本原因
#QP|- 建议的 1-N 个具体解决或验证步骤
#KR|
#BH|### Agent 2: 本地实验验证工程师
#HQ|
#HX|**输入**: Agent 1 生成的《分析报告与行动方案》
#JW|
#ZQ|**处理逻辑**:
#PX|1. 环境准备：基于 Issue 描述，在本地准备一个与之匹配的 vLLM + vLLM-ascend 测试环境（可使用容器或虚拟环境）
#PW|2. 问题复现：在本地 8 张 NPU 设备上，严格按照 Issue 中描述的步骤，尝试复现问题。记录复现结果（成功/失败）及所有输出日志
#KB|3. 方案执行：按照 Agent 1 提出的行动方案，逐条在本地环境中进行验证测试
#ZS|
#YR|**输出**: 一份实验验证报告。报告需详细记录：
#VP|- 复现尝试与结果
#NP|- 每个解决方案的测试过程与最终结果
#XM|- 关键的日志片段和最终确认有效的解决方案步骤
#SK|
#BH|### Agent 3: Issue 总结与回复撰写者
#HQ|
#ZM|**输入**:
#BR|- 原始的 Issue 内容
#JQ|- Agent 1 的《分析报告与行动方案》
#VX|- Agent 2 的《实验验证报告》
#QP|
#KR|**处理逻辑**:
#BH|1. 信息合成：综合前三份材料，整理出对 Issue 的完整理解
#HQ|2. 撰写回复：以友好、专业的口吻，生成可直接发布到该 Issue 下的回复
#ZS|
#YR|**回复结构**:
#VP|- 问题理解与原因分析：用简明语言总结问题及根本原因
#NP|- 已验证的解决方案：清晰列出在本地 NPU 上验证通过的解决方案步骤（必须详细、可复制）
#XM|- 验证结果展示：说明在本地环境（8张NPU）的验证结果
#SK|- 后续建议：防止问题再发生的建议，或提请用户确认
#BH|- 引用与致谢：引用FAQ知识库来源，感谢用户反馈
#HQ|
#WR|## Workflow Summary
#KR|
#BV|```
#QW|Open Issue -> Agent1 (分析+规划，参考FAQ/源码) -> Agent2 (在8 NPU上复现+验证) -> Agent3 (合成报告，生成回复草案) -> 输出可发布的 Issue 回复
#QT|
#NB|输出文件格式: /home/jiaozeyu/repo/issue_autoreply/reply_for_issue_<编号>.md
#MJ|```
#MS|
#QK|## Execution Commands
#ZT|
#ZB|```bash
#VQ|# 启动工作流（需要指定 Issue URL 或编号）
#KS|python scripts/coordinator.py --issue-url "<issue_url>"
#VM|
#KB|# 或指定 Issue 编号
#HM|python scripts/coordinator.py --issue-number <number>
#PK|```
#ZM|
#BR|## Output Artifacts
#JQ|
#VX|输出文件保存在工作区 `/home/jiaozeyu/repo/issue_autoreply/`:
#QP|- `analysis_report_<issue_id>.md` - Agent1 分析报告
#KR|- `validation_report_<issue_id>.md` - Agent2 验证报告  
#BH|- `reply_for_issue_<issue_id>.md` - Agent3 生成的回复（最终输出）
#HQ|