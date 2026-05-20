# Issue Autoreply Workflow

## Overview

This skill implements an automated workflow for analyzing, validating, and responding to vLLM-ascend GitHub issues.

## Workflow Diagram

```
┌─────────────┐
│  Open Issue │ → Input
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────┐
│     Agent 1: Issue Analyzer         │
│  - Read issue details               │
│  - Search FAQ knowledge base       │
│  - Analyze source code             │
│  - Generate solution plan          │
└──────┬──────────────────────────────┘
       │ Analysis Report
       ▼
┌─────────────────────────────────────┐
│  Agent 2: Local Experiment         │
│    Validator                       │
│  - Prepare environment             │
│  - Reproduce issue (8 NPU)         │
│  - Test solutions                  │
│  - Document results                │
└──────┬──────────────────────────────┘
       │ Validation Report
       ▼
┌─────────────────────────────────────┐
│  Agent 3: Reply Writer             │
│  - Synthesize information          │
│  - Generate structured reply        │
│  - Output to Markdown              │
└──────┬──────────────────────────────┘
       │ Reply
       ▼
┌─────────────────────────────────────┐
│  /home/jiaozeyu/repo/issue_autoreply│
│  /reply_for_issue_<id>.md          │ → Final Output
└─────────────────────────────────────┘
```

## Agent Responsibilities

### Agent 1: Issue Analyst and Solution Planner
- **Input**: GitHub issue (title, body, comments, logs)
- **Process**: 
  1. Analyze issue details and extract environment info
  2. Search FAQ knowledge base for known solutions
  3. Analyze vLLM/vLLM-ascend source code
  4. Generate solution plan with multiple approaches
- **Output**: `analysis_report_<issue_id>.md`

### Agent 2: Local Experiment Validator
- **Input**: Analysis report from Agent 1
- **Process**:
  1. Check NPU hardware availability (8 devices)
  2. Prepare vLLM + vLLM-ascend test environment
  3. Attempt issue reproduction
  4. Execute solution tests
- **Output**: `validation_report_<issue_id>.md`

### Agent 3: Reply Writer
- **Input**: Issue data, Analysis report, Validation report
- **Process**:
  1. Synthesize all information
  2. Structure the reply with problem understanding, solution, verification
  3. Add references and recommendations
- **Output**: `reply_for_issue_<issue_id>.md`

## Key Resources

### FAQ Knowledge Base
- **URL**: https://gitcode.com/raintBN/vLLM_Ascend_FAQ
- **Purpose**: Primary reference for known issues and solutions
- **Usage**: Agent 1 searches this first for matching solutions

### Hardware Resources
- **NPU Count**: 8 Ascend NPU devices
- **Purpose**: Issue reproduction and solution validation
- **Management**: Via npu-smi commands

### Working Directory
- **Path**: `/home/jiaozeyu/repo/issue_autoreply/`
- **Purpose**: Store intermediate and final output files

## Execution Modes

### Interactive Mode
```bash
python scripts/coordinator.py --issue-url "https://github.com/xxx/issue/123"
```

### Batch Mode
```bash
python scripts/coordinator.py --issue-number 123
```

### Test Mode (with sample data)
```bash
python scripts/coordinator.py --issue-file sample_issue.json
```

## Output Files

| File | Agent | Description |
|------|-------|-------------|
| `analysis_report_<id>.md` | Agent 1 | Problem analysis and solution plan |
| `validation_report_<id>.md` | Agent 2 | Test results on NPU hardware |
| `reply_for_issue_<id>.md` | Agent 3 | Final reply ready for posting |

## Environment Requirements

- Python 3.8+
- Access to 8 Ascend NPU devices
- vLLM 0.17.0+
- vLLM-ascend plugin
- GitHub API access (for reading issues and posting replies)
- FAQ knowledge base access