#!/usr/bin/env python3
"""
Issue Autoreply Coordinator
Orchestrates the three-agent workflow for automatic issue analysis, validation, and response generation.
"""

import argparse
import os
import sys
import json
from datetime import datetime

# Add scripts directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agent1_analyzer import IssueAnalyzer
from agent2_validator import LocalExperimentValidator
from agent3_writer import ReplyWriter


class Coordinator:
    """Main coordinator for the issue autoreply workflow."""
    
    def __init__(self, workspace="/home/jiaozeyu/repo/issue_autoreply"):
        self.workspace = workspace
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
    def load_issue(self, issue_url=None, issue_number=None, issue_data=None):
        """Load issue data from various sources."""
        if issue_data:
            return issue_data
        elif issue_url:
            # TODO: Implement GitHub API integration
            # For now, expect a JSON file or direct input
            pass
        elif issue_number:
            # TODO: Implement GitHub API integration
            pass
        
        raise ValueError("Must provide one of: issue_url, issue_number, or issue_data")
    
    def run_workflow(self, issue_data):
        """Execute the three-agent workflow."""
        issue_id = issue_data.get("id", f"issue_{self.timestamp}")
        
        print(f"[Coordinator] Starting workflow for Issue #{issue_id}")
        
        # Step 1: Agent 1 - Issue Analysis and Planning
        print(f"[Coordinator] Step 1/3: Running Agent 1 - Issue Analyzer...")
        analyzer = IssueAnalyzer(workspace=self.workspace)
        analysis_report = analyzer.analyze(issue_data)
        
        # Save analysis report
        analysis_path = os.path.join(self.workspace, f"analysis_report_{issue_id}.md")
        with open(analysis_path, "w") as f:
            f.write(analysis_report)
        print(f"[Coordinator] Analysis report saved to: {analysis_path}")
        
        # Step 2: Agent 2 - Local Experiment Validation
        print(f"[Coordinator] Step 2/3: Running Agent 2 - Local Experiment Validator...")
        validator = LocalExperimentValidator(workspace=self.workspace)
        validation_report = validator.validate(analysis_report, issue_data)
        
        # Save validation report
        validation_path = os.path.join(self.workspace, f"validation_report_{issue_id}.md")
        with open(validation_path, "w") as f:
            f.write(validation_report)
        print(f"[Coordinator] Validation report saved to: {validation_path}")
        
        # Step 3: Agent 3 - Reply Writer
        print(f"[Coordinator] Step 3/3: Running Agent 3 - Reply Writer...")
        writer = ReplyWriter(workspace=self.workspace)
        reply = writer.write_reply(issue_data, analysis_report, validation_report)
        
        # Save reply
        reply_path = os.path.join(self.workspace, f"reply_for_issue_{issue_id}.md")
        with open(reply_path, "w") as f:
            f.write(reply)
        print(f"[Coordinator] Reply saved to: {reply_path}")
        
        print(f"[Coordinator] Workflow completed successfully!")
        
        return {
            "issue_id": issue_id,
            "analysis_report": analysis_path,
            "validation_report": validation_path,
            "reply": reply_path
        }


def main():
    parser = argparse.ArgumentParser(description="Issue Autoreply Coordinator")
    parser.add_argument("--issue-url", type=str, help="GitHub issue URL")
    parser.add_argument("--issue-number", type=int, help="GitHub issue number")
    parser.add_argument("--issue-file", type=str, help="Path to issue JSON file")
    parser.add_argument("--workspace", type=str, default="/home/jiaozeyu/repo/issue_autoreply", 
                       help="Working directory")
    
    args = parser.parse_args()
    
    # Initialize coordinator
    coordinator = Coordinator(workspace=args.workspace)
    
    # Load issue data
    issue_data = None
    if args.issue_file:
        with open(args.issue_file, "r") as f:
            issue_data = json.load(f)
    
    # Run workflow
    result = coordinator.run_workflow(issue_data)
    
    print("\n" + "="*60)
    print("Workflow Summary:")
    print(f"  Issue ID: {result['issue_id']}")
    print(f"  Analysis: {result['analysis_report']}")
    print(f"  Validation: {result['validation_report']}")
    print(f"  Reply: {result['reply']}")
    print("="*60)


if __name__ == "__main__":
    main()