---
name: ascend-skills-eval
description: "昇腾技能评测器 - Ascend技能自动优化器。基于skills-eval的自主实验循环，专门评估昇腾相关Skills的结构质量和实际效果，通过真实NPU硬件测试验证改进，只保留真正有提升的修改。当测试昇腾相关skills时，自动调用本地NPU设备（通过npu-smi info查看）。适用于：优化Ascend相关skill、评估昇腾技能质量、skill评分、技能进化、ascend skill review。使用场景包括：优化所有昇腾skills、评估某个昇腾skill、对比有无skill的输出差异、生成可视化成卡等。"
---

# Ascend Skills Eval (昇腾技能评测)

> 借鉴 Karpathy autoresearch 的自主实验循环，对昇腾相关 Skills 进行持续优化。
> 核心理念：**评估 → 改进 → NPU实测验证 → 人类确认 → 保留或回滚 → 生成成果卡片**
> 与通用skills-eval的区别：**测试昇腾skills时使用真实NPU硬件进行效果验证**

---

## 与通用skills-eval的核心区别

| 方面 | skills-eval | ascend-skills-eval |
|:---|:---|:---|
| 优化范围 | 所有skills | 昇腾相关skills（名称含ascend/npu/昇腾） |
| 效果验证 | 子agent测试 | **昇腾skills用真实NPU硬件测试** |
| NPU检测 | 不涉及 | 通过`npu-smi info`检测可用设备 |
| 评估重点 | 通用结构 | **昇腾生态适配性** |

---

## 设计哲学

autoresearch 的精髓：
1. **单一可编辑资产** — 每次只改一个 SKILL.md
2. **双重评估** — 结构评分（静态分析）+ 效果验证（NPU实测或子agent测试）
3. **棘轮机制** — 只保留改进，自动回滚退步
4. **独立评分** — 评分用子agent，避免「自己改自己评」的偏差
5. **人在回路** — 每个skill优化完后暂停，用户确认再继续
6. **NPU优先** — 昇腾skills的效果验证必须用真实NPU硬件

---

## NPU环境检测

### Phase 0: NPU环境预检（每次评估前必须执行）

```bash
# 检查NPU状态
npu-smi info

# 检查可用设备数量
npu-smi info | grep "Ascend" | wc -l

# 检查CANN版本（如果需要）
python3 -c "import torch_npu; print(torch_npu.__version__)" 2>/dev/null || echo "torch_npu not available"
```

**NPU可用性判断：**
- `npu-smi info` 显示设备 → NPU可用，昇腾skills效果验证用真实硬件
- 无设备或错误 → 降级为子agent测试（无法真机验证时）

---

## 评估 Rubric（9维度，总分100）

### 结构维度（60分）— 静态分析

| # | 维度 | 权重 | 评分标准 |
|---|------|------|---------|
| 1 | **Frontmatter质量** | 8 | name规范、description包含做什么+何时用+触发词、≤1024字符 |
| 2 | **工作流清晰度** | 15 | 步骤明确可执行、有序号、每步有明确输入/输出 |
| 3 | **边界条件覆盖** | 10 | 处理异常情况、有fallback路径、错误恢复 |
| 4 | **检查点设计** | 7 | 关键决策前有用户确认、防止自主失控 |
| 5 | **指令具体性** | 15 | 不模糊、有具体参数/格式/示例、可直接执行 |
| 6 | **资源整合度** | 5 | references/scripts/assets引用正确、路径可达 |

### 效果维度（40分）— 需要实测

| # | 维度 | 权重 | 评分标准 |
|---|------|------|---------|
| 7 | **整体架构** | 15 | 结构层次清晰、不冗余不遗漏、与昇腾生态一致 |
| 8 | **昇腾适配性** | 10 | skill是否涉及NPU/Ascend相关操作，指令是否正确调用NPU工具 |
| 9 | **实测表现** | 15 | 用测试prompt跑一遍，输出质量是否符合skill宣称的能力 |

### 评分规则
- 维度1-8：每个维度打 1-10 分，乘以权重得到该维度得分
- 维度9（实测表现）：跑2-3个测试prompt
  - **昇腾相关skill**：用真实NPU硬件验证（如果npu-smi可用）
  - **非昇腾skill**：用子agent测试
- **总分 = Σ(维度分 × 权重) / 10**，满分100
- 改进后总分必须 **严格高于** 改进前才保留

### 关于「实测表现」维度

这是与纯结构评分最大的区别。评分方式：

1. 为每个skill设计2-3个**典型用户prompt**（不是边缘case，是最常见的使用场景）
2. 昇腾相关skills的验证：
   - 首先检查NPU环境：`npu-smi info`
   - 如果NPU可用，用真实硬件运行skill中的关键命令
   - 如果NPU不可用，降级为子agent对比测试
3. 非昇腾skills的验证：
   - 用子agent执行：一个带skill跑，一个不带skill跑（baseline）
4. 对比输出质量，从以下角度打分：
   - 输出是否完成了用户意图？
   - 相比不带skill的baseline，质量提升明显吗？
   - 有没有skill引入的负面影响（过度冗余、跑偏、格式奇怪）？

如果无法跑子agent（时间/资源限制），可以退化为「干跑验证」：读完skill后模拟一个典型prompt的执行思路，判断流程是否合理。但要在results.tsv中标注 `dry_run`。

---

## 自主优化循环

### Phase 0: 初始化

```
1. 确认优化范围：
   - 昇腾相关skills → 扫描 skills目录，筛选名称含ascend/npu/昇腾的skill
   - 指定skills → 用户指定列表
2. 检查NPU环境：npu-smi info
3. 创建 git 分支：auto-optimize/YYYYMMDD-HHMM
4. 初始化 results.tsv（如不存在）
5. 读取现有 results.tsv 了解历史优化记录
```

### Phase 0.5: 测试Prompt设计

在评估之前，为每个skill设计测试prompt。这步很关键——没有测试prompt，「实测表现」维度就打不了分。

```
for each skill:
  1. 读取 SKILL.md，理解它做什么
  2. 设计2-3个测试prompt，覆盖：
     - 最典型的使用场景（happy path）
     - 一个稍复杂或有歧义的场景
     - 昇腾skills：包含NPU操作相关prompt
  3. 保存到 skill目录/test-prompts.json：
     [
       {"id": 1, "prompt": "用户会说的话", "expected": "期望输出的简短描述"},
       {"id": 2, "prompt": "...", "expected": "..."}
     ]
```

展示所有测试prompt给用户，**确认后再进入评估**。测试prompt的质量决定了优化方向是否正确。

### Phase 1: 基线评估（Baseline）

```
for each skill in 优化范围:

  # 结构评分（主agent可以做）
  1. 读取 SKILL.md 全文
  2. 按维度1-8逐项打分（附简短理由）

  # 效果评分（用子agent做，独立于主agent）
  3. 判断skill是否昇腾相关
  4. 对每个测试prompt，spawn子agent：
     - with_skill: 带着SKILL.md执行测试prompt
     - baseline: 不带skill执行同一prompt
  5. 如果是昇腾skill且NPU可用：
     - 尝试在NPU上运行skill中的关键命令
     - 记录实际执行结果
  6. 对比两组输出，打维度9的分

  # 汇总
  7. 计算加权总分
  8. 记录到 results.tsv
```

**如果子agent不可用**（超时、环境限制），维度9用干跑验证打分，标注 `dry_run`。不要因为跑不了测试就跳过这个维度——哪怕是模拟推演也比完全不看效果好。

基线评估完成后，展示评分卡：

```
┌──────────────────────────┬───────┬──────────────┬──────────────┐
│ Skill                    │ Score │ 结构短板      │ 效果短板      │
├──────────────────────────┼───────┼──────────────┼──────────────┤
│ ascend-npu-verifier      │ 78    │ 边界条件      │ NPU实测通过  │
│ ascend-model-scanner     │ 72    │ 指令具体性    │ baseline持平  │
├──────────────────────────┼───────┼──────────────┼──────────────┤
│ 平均                     │ 75    │              │              │
└──────────────────────────┴───────┴──────────────┴──────────────┘
```

**暂停等用户确认，再进入优化循环。**

### Phase 2: 优化循环

用户确认后，按基线分数从低到高排序，先优化最弱的。

```
for each skill:
  round = 0
  while round < MAX_ROUNDS (默认3):
    round += 1

    # Step 1: 诊断
    找出得分最低的维度（结构或效果都算）

    # Step 2: 提出改进方案
    针对最低维度，生成1个具体改进方案：
      - 改什么（具体段落/行）
      - 为什么改（对应rubric哪条）
      - 预期提升多少分

    # Step 3: 执行改进
    编辑 SKILL.md
    git add + commit（message: "optimize {skill}: {改进摘要}"）

    # Step 4: 重新评估
    - 结构维度：主agent重新打分
    - 效果维度：spawn独立子agent重跑测试prompt（关键！不能自己评自己）
    - 如果是昇腾skill且之前有NPU实测：重新在NPU上验证

    # Step 5: 决策
    if 新总分 > 旧总分:
      status = "keep"，更新旧总分
    else:
      status = "revert"
      git revert HEAD（创建新commit回滚，不用reset --hard）
      记录失败尝试到 results.tsv
      break  # 该skill到瓶颈，跳到下一个

    # Step 6: 日志
    results.tsv 追加行

  # === 每个skill优化完后的人类检查点 ===
  展示该skill的改动摘要：
    - git diff（改前 vs 改后）
    - 分数变化（哪些维度提升/下降）
    - 测试prompt输出对比（如果跑过的话）
    - NPU实测结果（如果是昇腾skill）
  等用户确认 OK 再继续下一个skill。
  如果用户说"不好"，回滚到该skill的优化前版本。
```

### Phase 2.5: 探索性重写（可选）

当 hill-climbing 连续2个skill都在 round 1 就 break（涨不动）时，提议一次「探索性重写」：

```
1. 选一个瓶颈skill
2. git stash 保存当前最优版本
3. 从头重写SKILL.md（不是微调，是重新组织结构和表达方式）
4. 重新评估
5. if 重写版 > stash版: 采用重写版
   else: git stash pop 恢复
```

这解决了 hill-climbing 的局部最优问题——有时候需要「先拆后建」才能突破瓶颈。
**必须征得用户同意后才执行。**

### Phase 3: 汇总报告

```
## 优化报告

### 总览
- 优化skills数：N（均为昇腾相关）
- 总实验次数：M
- 保留改进：X（Y%）
- 回滚次数：Z
- NPU实测验证：A次
- 子agent测试：B次
- 干跑验证：C次

### NPU环境
- 可用设备：{npu-smi info输出}
- 实测skills：{list}

### 分数变化
┌──────────────────────────┬────────┬────────┬────────┐
│ Skill                    │ Before │ After  │ Δ      │
├──────────────────────────┼────────┼────────┼────────┤
│ ascend-npu-verifier      │ 78     │ 87     │ +9     │
│ ascend-model-scanner      │ 72     │ 83     │ +11    │
├──────────────────────────┼────────┼────────┼────────┤
│ 平均                     │ 75     │ 85     │ +10    │
└──────────────────────────┴────────┴────────┴────────┘

### 主要改进
1. [skill-A] 补充了昇腾NPU调用逻辑，测试输出质量提升明显
2. [skill-B] 重组了workflow结构，baseline对比优势增大
```

---

## results.tsv 格式

```tsv
timestamp	commit	skill	old_score	new_score	status	dimension	note	eval_mode	npu_verified
2026-03-31T10:00	baseline	ascend-npu-verifier	-	78	baseline	-	初始评估	full_test	true
2026-03-31T10:05	a1b2c3d	ascend-npu-verifier	78	84	keep	边界条件	补充fallback	full_test	true
2026-03-31T10:10	b2c3d4e	ascend-npu-verifier	84	82	revert	指令具体性	过度细化	dry_run	false
```

新增列：
- `eval_mode`：full_test（子agent测试）、npu_test（NPU实测）、dry_run（模拟推演）
- `npu_verified`：true/false - 是否经过真实NPU验证

文件位置：`.claude/skills/ascend-skills-eval/results.tsv`

---

## 优化策略库

按优先级排序，每轮只做最高优先级的一个：

### P0: 效果问题（实测发现的）
- 测试输出偏离用户意图 → 检查skill是否有误导性指令
- 带skill比不带还差 → skill可能过度约束，考虑精简
- 输出格式不符合预期 → 补充明确的输出模板
- **昇腾skill特有**：NPU调用失败 → 检查device设置、memory配置、ASCEND_RT_VISIBLE_DEVICES

### P1: 昇腾适配性问题
- skill涉及NPU但指令缺失 → 补充npu-smi info检查、NPU设备选择逻辑
- NPU memory管理缺失 → 补充pkill vllm、gpu_memory_utilization设置
- 昇腾特定错误处理缺失 → 补充OOM处理、NPU不可用fallback

### P2: 结构性问题
- Frontmatter缺少触发词 → 补充中英文触发词
- 缺少Phase/Step结构 → 重组为线性流程
- 缺少用户确认检查点 → 在关键决策处插入

### P3: 具体性问题
- 步骤模糊（"处理图片"）→ 改为具体操作和参数
- 缺少输入/输出规格 → 补充格式、路径、示例
- 缺少异常处理 → 补充 "如果X失败，则Y"

### P4: 可读性问题
- 段落过长 → 拆分+用表格
- 重复描述 → 合并去重
- 缺少速查 → 添加TL;DR或决策树

---

## 异常与边界条件

流程假设环境理想，但实操常遇异常。以下预定义 fallback，保证优化过程不会「一跑就卡住」。

| 场景 | 触发条件 | 处理动作 |
|---|---|---|
| NPU不可用 | `npu-smi info` 无输出或错误 | 降级为子agent测试，标注npu_verified=false |
| NPU memory不足 | 部署时OOM | 记录错误，继续测试其他skills，事后分析 |
| 不在 git 仓库 | `git rev-parse` 失败 | 提示用户「建议 git init」；若拒绝，用 `cp SKILL.md SKILL.md.bak.YYYYMMDD-HHMM` 文件备份代替 revert |
| results.tsv 缺失 | 文件不存在 | 新建并写表头行（10列：含 eval_mode + npu_verified） |
| results.tsv 损坏 | 列数不匹配 / 非TSV | 备份为 `.bak.YYYYMMDD-HHMM` 后重建，告知用户 |
| 分支已存在 | `git checkout -b` 失败 | 分支名末尾加 `-2` / `-3`；第3次失败则切回现有分支并询问继续还是新起 |
| `git revert` 失败 | 冲突 / 工作树脏 | 先 `git stash`，重试；仍失败则从上一个 commit 的 SKILL.md 读出覆盖当前文件手动恢复 |
| MAX_ROUNDS 触顶（默认3） | 已跑3轮仍有短板 | 不强制 break，展示当前最弱维度问用户「继续加1轮 / 进入Phase 2.5 / 收工」 |
| 优化后超 150% 体积 | 新文件 > 原 × 1.5 | 拒绝提交，回到改进步骤精简（删冗余/合并重复），再评 |
| test-prompts.json 已存在 | 文件已在 skill 目录 | 默认复用并展示，问用户「复用 / 重写 / 追加」三选一 |
| SKILL.md 找不到 | 目录存在但无 SKILL.md | 该 skill 终止，results.tsv 记 `status=error`，继续下一个 |
| 分数计算规则 | 浮点精度漂移 | 总分保留 1 位小数，改进需严格 > 旧分（不靠四舍五入） |

**原则**：异常先告知用户，再按规则处理；绝不静默跳过或静默失败。

---

## 约束规则

1. **不改变skill的核心功能和用途** — 只优化"怎么写"和"怎么执行"，不改"做什么"
2. **不引入新依赖** — 不添加skill原本没有的scripts或references文件
3. **每轮只改一个维度** — 避免多个变更导致无法归因
4. **保持文件大小合理** — 优化后SKILL.md不应超过原始大小的150%
5. **尊重花叔风格** — 中文为主、简洁为上
6. **可回滚** — 所有改动在git分支上，用git revert而非reset --hard
7. **评分独立性** — 效果维度必须用子agent/NPU实测或至少干跑验证，不能在同一上下文里「改完直接评」
8. **昇腾优先** — 昇腾相关skills的效果验证必须优先尝试真实NPU硬件

---

## 使用方式

### 全量优化（推荐首次使用）
```
用户："优化所有昇腾skills"
→ Phase 0-3 完整流程
→ 自动筛选昇腾相关skills进行评估和优化
```

### 单个优化
```
用户："优化 ascend-npu-verifier 这个skill"
→ 只对指定skill执行 Phase 0.5-2
```

### 仅评估不改
```
用户："评估所有昇腾skills的质量"
→ 只执行 Phase 0.5-1（设计测试prompt + 基线评估），不进入优化循环
```

### NPU实测验证
```
用户："用NPU实测验证 ascend-model-scanner"
→ 检查npu-smi可用性
→ 在真实NPU上运行skill中的关键命令
→ 记录实测结果到报告
```

### 查看历史
```
用户："看看昇腾skill优化历史"
→ 读取并展示 results.tsv（含npu_verified列）
```

---

## 设计灵感

> "You write the goals and constraints in program.md; let an agent generate and test code deltas indefinitely; keep only what measurably improves the objective."
> — Karpathy, autoresearch

本skill的对应关系：
- **program.md** → 本文件（评估rubric和约束规则）
- **train.py** → 每个待优化的SKILL.md
- **val_bpb** → 9维加权总分（含昇腾适配性和NPU实测）
- **git ratchet** → 只保留有改进的commit
- **test set** → 每个skill的test-prompts.json

区别：增加了昇腾适配性维度（维度8）和NPU实测验证，因为昇腾skills的实际效果与NPU硬件状态密切相关。

---

## 成果卡片生成（Result Card）

每个skill优化完成后（或全量汇总后），自动生成视觉成果卡片，截图保存为PNG。

### 卡片模板

模板位置：`templates/result-card.html`

### 生成流程

```
1. 复制 templates/result-card.html 到临时工作文件
2. 用编辑工具替换占位数据：
   - data-field="skill-name" → 实际skill名
   - data-field="score-before/after/delta" → 实际分数
   - 9个维度的 dim-bar-before/after width → 实际百分比
   - data-field="improvement-1/2/3" → 实际改进摘要
   - data-field="date" → 当前日期
   - data-field="npu-status" → NPU实测状态
3. 随机选择风格：swiss/terminal/newspaper 之一
4. 用 scripts/screenshot.mjs 截图（2x 高清，只截 .card 元素）
5. 提示用户查看成果卡片 PNG
```

### 何时生成

- **单skill卡片**：每个skill优化完成后，展示该skill的分数变化（含NPU实测结果）
- **总览卡片**：全部优化完成后（Phase 3），展示全局战绩（含NPU环境信息）

### 品牌元素

- 顶部：Ascend Skills Eval 品牌标识 + 日期
- 底部：「Train your Skills like you train your models — Now on Ascend」
- NPU环境badge：显示实测设备数量

---

## 资源文件速查

| 路径 | 用途 |
|---|---|
| `templates/result-card.html` | 3风格主模板（swiss/terminal/newspaper，hash切换） |
| `scripts/screenshot.mjs` | 2x 高清截图，只截 .card |
| `results.tsv` | 历次优化日志（11列含 eval_mode + npu_verified） |
| `{skill目录}/test-prompts.json` | 每个 skill 的测试 prompt 集（用于维度9实测） |

---

## 快速参考：昇腾Skill测试检查清单

当测试昇腾相关skills时，按以下顺序检查：

```
□ 1. NPU环境检查
   - npu-smi info 显示设备
   - torch_npu 可导入
   - CANN 版本兼容

□ 2. Skill加载检查
   - SKILL.md 格式正确
   - Frontmatter 完整（name + description）
   - 触发词覆盖常见场景

□ 3. 指令执行检查
   - NPU设备选择逻辑正确（ASCEND_RT_VISIBLE_DEVICES）
   - Memory管理设置合理（gpu_memory_utilization）
   - 错误处理包含OOM fallback

□ 4. 实际效果检查
   - 模型加载成功
   - 推理输出合理
   - 性能指标可接受

□ 5. 结果记录
   - 保存测试输出
   - 记录执行时间
   - 归档到results.tsv
```
