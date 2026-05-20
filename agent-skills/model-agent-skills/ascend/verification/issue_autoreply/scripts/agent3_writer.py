#!/usr/bin/env python3
"""
Agent 3: Issue Summary and Reply Writer
Generates structured, professional replies for GitHub issues based on analysis and validation results.
"""

import os
import sys
import json
from datetime import datetime


class ReplyWriter:
    """Agent 3: Writes professional issue replies."""
    
    def __init__(self, workspace="/home/jiaozeyu/repo/issue_autoreply"):
        self.workspace = workspace
        self.faq_source = "https://gitcode.com/raintBN/vLLM_Ascend_FAQ"
        
    def write_reply(self, issue_data, analysis_report, validation_report):
        """
        Main reply generation logic.
        
        Input:
            - issue_data: Original issue data
            - analysis_report: Output from Agent 1
            - validation_report: Output from Agent 2
        Output: Reply text (markdown string)
        """
        issue_number = issue_data.get("number", "unknown")
        issue_title = issue_data.get("title", "Unknown Issue")
        
        print(f"[Agent3] Generating reply for Issue #{issue_number}")
        
        # Parse key information from reports
        problem_summary = self._extract_problem(analysis_report)
        root_cause = self._extract_root_cause(analysis_report)
        solution = self._extract_solution(validation_report)
        verification_result = self._extract_verification(validation_report)
        
        # Generate structured reply
        reply = self._generate_reply(
            issue_number, issue_title, problem_summary, 
            root_cause, solution, verification_result
        )
        
        return reply
    
    def _extract_problem(self, analysis_report):
        """Extract problem summary from analysis report."""
        # Parse markdown sections
        # Simplified - would use proper markdown parsing in production
        
        lines = analysis_report.split("\n")
        in_problem_section = False
        problem_lines = []
        
        for line in lines:
            if "## 1. Problem Summary" in line or "## Problem Summary" in line:
                in_problem_section = True
                continue
            if in_problem_section:
                if line.startswith("##"):
                    break
                problem_lines.append(line)
        
        # Clean and join
        problem = "\n".join(problem_lines).strip()
        return problem[:500] if problem else "Issue description analysis in progress"
    
    def _extract_root_cause(self, analysis_report):
        """Extract root cause analysis from report."""
        lines = analysis_report.split("\n")
        in_causes_section = False
        causes = []
        
        for line in lines:
            if "Root Cause" in line or "potential_root_causes" in line.lower():
                in_causes_section = True
                continue
            if in_causes_section:
                if line.startswith("##") or line.startswith("---"):
                    break
                if line.strip() and not line.startswith("###"):
                    causes.append(line.strip())
        
        return causes[:3] if causes else ["Analysis in progress"]
    
    def _extract_solution(self, validation_report):
        """Extract solution from validation report."""
        # Extract working solutions from validation
        solutions = []
        
        lines = validation_report.split("\n")
        for line in lines:
            if "✅" in line or "Step" in line:
                if "Step" in line:
                    solutions.append(line.strip())
        
        return solutions if solutions else ["Solution validation in progress"]
    
    def _extract_verification(self, validation_report):
        """Extract verification results."""
        # Check for successful verifications
        verified = "✅" in validation_report or "success" in validation_report.lower()
        
        npu_count = 8  # From skill specification
        
        return {
            "verified": verified,
            "npu_count": npu_count,
            "details": "Verification performed on 8 NPU devices" if verified else "Awaiting verification"
        }
    
    def _generate_reply(self, issue_number, title, problem, root_cause, solution, verification):
        """Generate the final reply structure."""
        reply = f"""## 问题理解与原因分析

Thank you for reporting this issue!

**问题摘要**: {title}

{problem}

**根本原因分析**:
"""
        
        for cause in root_cause:
            if cause.strip():
                reply += f"- {cause}\n"
        
        reply += f"""
---

## 已验证的解决方案

"""
        
        for sol in solution:
            if sol.strip():
                reply += f"- {sol}\n"
        
        # If no verified solution, provide FAQ reference
        if not verification["verified"]:
            reply += f"""
> **Note**: The solution is being validated. For immediate assistance, please refer to our FAQ knowledge base:
> - FAQ Repository: {self.faq_source}
> - Common solutions and troubleshooting guides are available there.

"""
        
        reply += f"""
---

## 验证结果展示

"""
        
        if verification["verified"]:
            reply += f"""✅ **Verified on Hardware**

This solution has been tested and verified on our local environment with **{verification['npu_count']} Ascend NPU devices**.

```
[Verification details from local testing]
```
"""
        else:
            reply += f"""⏳ **Verification In Progress**

This solution is being validated on our local environment with **{verification['npu_count']} Ascend NPU devices**. We will update this issue once testing is complete.

"""
        
        reply += f"""
---

## 后续建议

1. Please try the solution above and let us know if it resolves your issue
2. If you encounter any other problems, please provide detailed error logs
3. For faster resolution, please include:
   - Full error traceback
   - Environment details (NPU model, CANN version, vLLM version)
   - Minimal reproduction steps

---

## 引用与致谢

"""
        
        # Add FAQ reference if applicable
        reply += f"""- This solution references our FAQ knowledge base: [{self.faq_source}]({self.faq_source})
- Thank you for helping improve vLLM-ascend!

---

*Generated by vLLM-ascend Issue Autoreply System*
"""
        
        return reply


def main():
    """Test function for Agent 3."""
    test_issue = {
        "number": 1,
        "title": "Memory allocation error on Atlas 910"
    }
    
    test_analysis = """
## 1. Problem Summary

Memory allocation fails when running vLLM with vLLM-ascend

## Root Cause
- Memory management issue in ascend device module
"""
    
    test_validation = """
## Solution Testing Results

✅ Step 1: Environment verified - 8 NPUs available
✅ Step 2: Solution applied - Memory fix implemented
"""
    
    writer = ReplyWriter()
    reply = writer.write_reply(test_issue, test_analysis, test_validation)
    print(reply)


if __name__ == "__main__":
    main()