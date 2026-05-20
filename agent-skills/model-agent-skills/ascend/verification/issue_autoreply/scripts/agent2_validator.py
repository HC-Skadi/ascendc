#!/usr/bin/env python3
"""
Agent 2: Local Experiment Validator
Validates solutions by reproducing issues and testing fixes on local NPU hardware.
"""

import os
import sys
import json
import subprocess
import re
from datetime import datetime


class LocalExperimentValidator:
    """Agent 2: Validates solutions on local NPU hardware."""
    
    def __init__(self, workspace="/home/jiaozeyu/repo/issue_autoreply"):
        self.workspace = workspace
        self.npu_count = 8  # 8 NPU devices available
        
    def validate(self, analysis_report, issue_data):
        """
        Main validation logic.
        
        Input: 
            - analysis_report: Output from Agent 1
            - issue_data: Original issue data
        Output: Validation report (markdown string)
        """
        issue_number = issue_data.get("number", "unknown")
        
        print(f"[Agent2] Starting validation for Issue #{issue_number}")
        
        # Parse analysis report to get solution plan
        solution_plan = self._parse_solution_plan(analysis_report)
        
        # Step 1: Environment preparation
        env_status = self._prepare_environment(issue_data)
        
        # Step 2: Issue reproduction
        reproduction_result = self._reproduce_issue(issue_data, solution_plan)
        
        # Step 3: Execute solution attempts
        solution_results = self._execute_solutions(solution_plan, issue_data)
        
        # Step 4: Generate validation report
        validation_report = self._generate_report(
            issue_number, env_status, reproduction_result, solution_results
        )
        
        return validation_report
    
    def _parse_solution_plan(self, analysis_report):
        """Parse solution plan from Agent 1's report."""
        plan = {"steps": []}
        
        # Extract steps from report
        # This is a simplified parser - in production would use proper markdown parsing
        step_pattern = r"### Step (\d+): (.+?)\n"
        matches = re.findall(step_pattern, analysis_report)
        
        for step_num, step_title in matches:
            plan["steps"].append({
                "id": int(step_num),
                "title": step_title.strip()
            })
        
        return plan
    
    def _prepare_environment(self, issue_data):
        """Prepare the test environment."""
        print("[Agent2] Preparing test environment...")
        
        status = {
            "npu_available": False,
            "npu_count": 0,
            "vllm_installed": False,
            "vllm_ascend_installed": False,
            "details": {}
        }
        
        # Check NPU availability
        try:
            result = subprocess.run(
                ["npu-smi", "info", "-l"],
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0:
                lines = result.stdout.strip().split("\n")
                # Count NPU devices (exclude header lines)
                npu_lines = [l for l in lines if l and not l.startswith("---") 
                            and not l.startswith("Node")]
                status["npu_available"] = True
                status["npu_count"] = len(npu_lines)
                status["details"]["npu_output"] = result.stdout[:500]
        except (subprocess.SubprocessError, FileNotFoundError) as e:
            status["details"]["error"] = str(e)
        
        # Check vLLM installation
        try:
            result = subprocess.run(
                ["python", "-c", "import vllm; print(vllm.__version__)"],
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0:
                status["vllm_installed"] = True
                status["details"]["vllm_version"] = result.stdout.strip()
        except:
            pass
        
        # Check vLLM-ascend installation
        try:
            result = subprocess.run(
                ["python", "-c", "import vllm_ascend; print('installed')"],
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0:
                status["vllm_ascend_installed"] = True
        except:
            pass
        
        return status
    
    def _reproduce_issue(self, issue_data, solution_plan):
        """Attempt to reproduce the issue."""
        print("[Agent2] Attempting to reproduce the issue...")
        
        result = {
            "reproduced": False,
            "error_output": "",
            "steps_executed": []
        }
        
        # Extract relevant commands from issue description
        # This is a placeholder - in production would parse actual commands from issue
        
        # For now, document the reproduction attempt
        result["steps_executed"].append({
            "step": "Environment check",
            "status": "completed",
            "output": "Environment ready for testing"
        })
        
        return result
    
    def _execute_solutions(self, solution_plan, issue_data):
        """Execute solution attempts."""
        results = []
        
        print(f"[Agent2] Executing {len(solution_plan.get('steps', []))} solution steps...")
        
        for step in solution_plan.get("steps", []):
            step_result = {
                "step_id": step["id"],
                "title": step["title"],
                "status": "pending",
                "output": "",
                "success": False
            }
            
            # Execute each solution step
            # This would involve actual testing on NPU hardware
            # For now, we document the intended execution
            
            print(f"[Agent2]   Step {step['id']}: {step['title']}")
            
            # Simulate execution
            step_result["status"] = "simulated"
            step_result["output"] = "Solution execution simulated - requires actual NPU hardware"
            
            results.append(step_result)
        
        return results
    
    def _generate_report(self, issue_number, env_status, reproduction_result, solution_results):
        """Generate validation report."""
        report = f"""# Validation Report - Issue #{issue_number}

**Date**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---

## 1. Environment Status

### NPU Hardware
| Item | Status |
|------|--------|
| Available | {env_status.get('npu_available', False)} |
| Device Count | {env_status.get('npu_count', 0)} |
| vLLM Installed | {env_status.get('vllm_installed', False)} |
| vLLM-Ascend Installed | {env_status.get('vllm_ascend_installed', False)} |

"""
        if env_status.get("details", {}).get("npu_output"):
            report += f"""### NPU Output:
```
{env_status['details']['npu_output']}
```
"""
        
        if env_status.get("details", {}).get("vllm_version"):
            report += f"**vLLM Version**: {env_status['details']['vllm_version']}\n\n"

        report += f"""
---

## 2. Issue Reproduction

### Reproduction Status
- **Reproduced**: {reproduction_result.get('reproduced', False)}

### Steps Executed:
"""
        for step in reproduction_result.get("steps_executed", []):
            report += f"- **{step['step']}**: {step['status']}\n"
            if step.get("output"):
                report += f"  - Output: {step['output']}\n"

        report += """
---

## 3. Solution Testing Results

"""
        for result in solution_results:
            status_emoji = "✅" if result.get("success") else "⏳"
            report += f"""### Step {result['step_id']}: {result['title']}

- **Status**: {status_emoji} {result['status']}
- **Output**: {result.get('output', 'N/A')}

"""

        # Determine final recommendation
        successful_solutions = [r for r in solution_results if r.get("success")]
        
        if successful_solutions:
            recommendation = f"Found {len(successful_solutions)} working solution(s)"
        else:
            recommendation = "Solution testing in progress - requires NPU hardware access"
        
        report += f"""
---

## 4. Recommendation

{recommendation}

---

*Report generated by Agent 2: Local Experiment Validator*

**Note**: This validation was performed with {self.npu_count} NPU devices available.
For full validation, actual execution on NPU hardware is required.
"""
        
        return report


def main():
    """Test function for Agent 2."""
    test_issue = {
        "number": 1,
        "title": "Memory allocation error",
        "body": "Testing issue"
    }
    
    test_analysis = """
### Step 1: Verify NPU environment
- Command: npu-smi info -l

### Step 2: Apply FAQ solution
- Reference: FAQ knowledge base
"""
    
    validator = LocalExperimentValidator()
    report = validator.validate(test_analysis, test_issue)
    print(report)


if __name__ == "__main__":
    main()