#!/usr/bin/env python3
"""
Agent 1: Issue Analyst and Solution Planner
Analyzes GitHub issues, searches FAQ knowledge base, and generates analysis reports.
"""

import os
import sys
import json
import re
from datetime import datetime

# FAQ Knowledge Base URL
FAQ_BASE_URL = "https://gitcode.com/raintBN/vLLM_Ascend_FAQ"


class IssueAnalyzer:
    """Agent 1: Analyzes issues and generates solution plans."""
    
    def __init__(self, workspace="/home/jiaozeyu/repo/issue_autoreply"):
        self.workspace = workspace
        self.faq_cache_path = os.path.join(workspace, "faq_cache")
        
    def analyze(self, issue_data):
        """
        Main analysis logic.
        
        Input: issue_data (dict with title, body, comments, labels, etc.)
        Output: Analysis report (markdown string)
        """
        # Extract key information from issue
        title = issue_data.get("title", "")
        body = issue_data.get("body", "")
        issue_number = issue_data.get("number", "unknown")
        labels = issue_data.get("labels", [])
        comments = issue_data.get("comments", [])
        
        print(f"[Agent1] Analyzing Issue #{issue_number}: {title}")
        
        # Step 1: Extract environment and problem information
        env_info = self._extract_environment_info(body, comments)
        problem_summary = self._extract_problem_summary(body, comments)
        
        # Step 2: Search FAQ knowledge base (simulated for now)
        faq_matches = self._search_faq(problem_summary, env_info)
        
        # Step 3: Analyze related source code
        source_analysis = self._analyze_source_code(problem_summary, env_info)
        
        # Step 4: Generate solution plan
        solution_plan = self._generate_solution_plan(
            problem_summary, env_info, faq_matches, source_analysis
        )
        
        # Step 5: Compile analysis report
        report = self._generate_report(
            issue_number, title, problem_summary, env_info, 
            faq_matches, source_analysis, solution_plan
        )
        
        return report
    
    def _extract_environment_info(self, body, comments):
        """Extract environment information from issue."""
        info = {
            "npu_model": None,
            "driver_version": None,
            "vllm_version": None,
            "vllm_ascend_version": None,
            "model_name": None,
            "error_messages": []
        }
        
        # Combine body and comments for searching
        all_text = body + "\n" + "\n".join([c.get("body", "") for c in comments])
        
        # Extract NPU model
        npu_match = re.search(r"(Atlas|910|310)[\s_-]?([A-Z0-9]+)", all_text, re.IGNORECASE)
        if npu_match:
            info["npu_model"] = npu_match.group(0)
        
        # Extract driver/CANN version
        driver_match = re.search(r"(CANN|driver)[\s_-]?([0-9.]+)", all_text, re.IGNORECASE)
        if driver_match:
            info["driver_version"] = driver_match.group(0)
        
        # Extract vLLM version
        vllm_match = re.search(r"vLLM[\s_-]?([0-9.]+)", all_text, re.IGNORECASE)
        if vllm_match:
            info["vllm_version"] = vllm_match.group(0)
        
        # Extract model name
        model_match = re.search(r"(?:model|Model)[\s:]*([A-Za-z0-9_-]+)", all_text)
        if model_match:
            info["model_name"] = model_match.group(1)
        
        # Extract error messages
        error_patterns = [
            r"(?:Error|Exception|Traceback|CRITICAL|FATAL)[:\s]+(.+)",
            r"RuntimeError[:\s]+(.+)",
            r"OSError[:\s]+(.+)"
        ]
        for pattern in error_patterns:
            matches = re.findall(pattern, all_text, re.IGNORECASE | re.MULTILINE)
            info["error_messages"].extend(matches[:5])  # Limit to 5 errors
        
        return info
    
    def _extract_problem_summary(self, body, comments):
        """Extract problem summary from issue."""
        # Extract first substantial paragraph as problem description
        paragraphs = body.split("\n\n")
        for p in paragraphs:
            if len(p) > 50 and "```" not in p[:100]:  # Skip code blocks
                return p.strip()[:500]  # Limit length
        
        return body[:500] if body else "No description provided"
    
    def _search_faq(self, problem_summary, env_info):
        """Search FAQ knowledge base for relevant solutions."""
        # This would integrate with the FAQ repository
        # For now, return placeholder structure
        
        matches = []
        
        # Keywords to search in FAQ
        keywords = []
        if env_info.get("error_messages"):
            keywords.extend(env_info["error_messages"][0].split()[:3])
        keywords.extend(problem_summary.split()[:5])
        
        # Simulated FAQ search
        print(f"[Agent1] Searching FAQ with keywords: {keywords}")
        
        # Note: In production, this would query https://gitcode.com/raintBN/vLLM_Ascend_FAQ
        # For now, we document the search intent
        matches.append({
            "source": FAQ_BASE_URL,
            "keywords_used": keywords,
            "status": "search_required",
            "note": "Manual FAQ search or API integration needed"
        })
        
        return matches
    
    def _analyze_source_code(self, problem_summary, env_info):
        """Analyze related source code."""
        # Placeholder for source code analysis
        # In production, this would search vLLM and vLLM-ascend source code
        
        analysis = {
            "relevant_modules": [],
            "potential_root_causes": [],
            "code_patterns": []
        }
        
        # Analyze error messages for code patterns
        if env_info.get("error_messages"):
            for err in env_info["error_messages"]:
                # Look for common vLLM-ascend error patterns
                if "memory" in err.lower():
                    analysis["potential_root_causes"].append("Memory allocation/deallocation issue")
                    analysis["relevant_modules"].append("vllm/device/ascend")
                if "kernel" in err.lower():
                    analysis["potential_root_causes"].append("Kernel execution error")
                    analysis["relevant_modules"].append("vllm/kernel")
        
        return analysis
    
    def _generate_solution_plan(self, problem_summary, env_info, faq_matches, source_analysis):
        """Generate solution plan with multiple approaches."""
        plan = {
            "steps": [],
            "priority_order": []
        }
        
        # Generate steps based on analysis
        steps = []
        
        # Step 1: Environment verification
        if env_info.get("npu_model"):
            steps.append({
                "id": 1,
                "action": "Verify NPU environment",
                "details": f"Check {env_info['npu_model']} availability and health status",
                "command": "npu-smi info -l"
            })
        
        # Step 2: FAQ solution attempt
        if faq_matches:
            steps.append({
                "id": 2,
                "action": "Apply FAQ solution",
                "details": "Try solutions from FAQ knowledge base",
                "reference": faq_matches[0].get("source", "FAQ")
            })
        
        # Step 3: Code fix (if identified)
        if source_analysis.get("relevant_modules"):
            steps.append({
                "id": 3,
                "action": "Apply source code fix",
                "details": f"Fix identified issues in {', '.join(source_analysis['relevant_modules'])}",
                "modules": source_analysis["relevant_modules"]
            })
        
        # Step 4: Configuration adjustment
        steps.append({
            "id": 4,
            "action": "Adjust vLLM configuration",
            "details": "Try different runtime configurations",
            "options": ["--tensor-parallel-size", "--trust-remote-code", "--dtype"]
        })
        
        plan["steps"] = steps
        plan["priority_order"] = [s["id"] for s in steps]
        
        return plan
    
    def _generate_report(self, issue_number, title, problem_summary, env_info, 
                         faq_matches, source_analysis, solution_plan):
        """Generate the final analysis report."""
        report = f"""# Issue Analysis Report - #{issue_number}

**Title**: {title}
**Date**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---

## 1. Problem Summary

{problem_summary}

---

## 2. Environment Information

| Item | Value |
|------|-------|
| NPU Model | {env_info.get('npu_model', 'Not specified')} |
| Driver/CANN Version | {env_info.get('driver_version', 'Not specified')} |
| vLLM Version | {env_info.get('vllm_version', 'Not specified')} |
| vLLM-Ascend Version | {env_info.get('vllm_ascend_version', 'Not specified')} |
| Model Name | {env_info.get('model_name', 'Not specified')} |

### Error Messages Found:
"""
        for i, err in enumerate(env_info.get("error_messages", []), 1):
            report += f"{i}. `{err}`\n"
        
        report += f"""
---

## 3. FAQ Knowledge Base Search

**Reference**: {FAQ_BASE_URL}

"""
        for i, match in enumerate(faq_matches, 1):
            report += f"""### Match {i}:
- **Source**: {match.get('source', 'Unknown')}
- **Keywords**: {', '.join(match.get('keywords_used', []))}
- **Status**: {match.get('status', 'unknown')}
- **Note**: {match.get('note', 'N/A')}

"""
        
        report += f"""
---

## 4. Source Code Analysis

### Relevant Modules:
"""
        for module in source_analysis.get("relevant_modules", []):
            report += f"- `{module}`\n"
        
        report += """
### Potential Root Causes:
"""
        for cause in source_analysis.get("potential_root_causes", []):
            report += f"- {cause}\n"
        
        report += """
---

## 5. Solution Plan

"""
        for step in solution_plan.get("steps", []):
            report += f"""### Step {step['id']}: {step['action']}

- **Description**: {step.get('details', 'N/A')}
"""
            if "command" in step:
                report += f"- **Command**: `{step['command']}`\n"
            if "reference" in step:
                report += f"- **Reference**: {step['reference']}\n"
            if "modules" in step:
                report += f"- **Modules**: {', '.join(step['modules'])}\n"
            if "options" in step:
                report += f"- **Options**: {', '.join(step['options'])}\n"
            report += "\n"
        
        report += f"""
---

## 6. Next Steps for Agent 2

Agent 2 should:
1. Attempt to reproduce the issue using the environment details provided
2. Execute the solution plan steps in priority order
3. Document test results for each step
4. Identify the working solution

---

*Report generated by Agent 1: Issue Analyst and Solution Planner*
"""
        
        return report


def main():
    """Test function for Agent 1."""
    # Sample issue data for testing
    test_issue = {
        "number": 1,
        "title": "Memory allocation error on Atlas 910",
        "body": "When running vLLM with vLLM-ascend on Atlas 910, memory allocation fails...",
        "labels": ["bug", "memory"],
        "comments": [
            {"body": "Can you provide the vLLM version?"}
        ]
    }
    
    analyzer = IssueAnalyzer()
    report = analyzer.analyze(test_issue)
    print(report)


if __name__ == "__main__":
    main()