# aclnn_gen/aclnngen.py
import sys
import os
import argparse

from aclnn_gen.parsing.op_parser import OperatorDefinition
from aclnn_gen.parsing.case_parser import CaseParser 
from aclnn_gen.generation.project_generator import ProjectGenerator

def main():
    """
    Parses command-line arguments and orchestrates the generation of a complete,
    multi-case test project.
    """
    # Create the top-level parser
    parser = argparse.ArgumentParser(
        prog="aclnngen",
        description="A tool to generate a unified Ascend CANN (ACLNN) C++ test project from a prototype and a case file.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""\
Example Usage:
  aclnngen <operator_prototype.json> <test_cases.json> -o <output_dir> --op-path <path_to_custom_op_pkg>

This command reads the operator definition and all test cases, then generates a single,
comprehensive project that can run any of the specified test cases.
"""
    )
    
    # --- Positional Arguments ---
    parser.add_argument(
        "prototype_file",
        help="Path to the operator prototype JSON file, which defines the operator's interface."
    )
    parser.add_argument(
        "case_file",
        help="Path to the test cases JSON file, which contains a list of all test case configurations."
    )

    # --- Optional Arguments ---
    parser.add_argument(
        "-o", "--output_dir",
        default=".",
        help="The directory where the new project folder will be created. \n"
             "(Default: current directory)"
    )
    parser.add_argument(
        "--op-path",
        default="/home/ma-user/Ascend/ascend-toolkit/latest/opp/vendors/customize/op_api",
        help="Path to the custom operator package directory."
    )
    parser.add_argument(
        "--op-type",
        default="custom",
        help="Type of the operator: 'custom' or 'builtin'. (Default: custom)",
        choices=["custom", "builtin"]
    )

    args = parser.parse_args()

    try:
        # --- Main Workflow ---
        print("--- Generating Unified Multi-Case Test Project ---")
        
        # 1. Parse the operator prototype file (optional, can be merged into case parser if redundant)
        # For now, we assume it might contain info not in the case file.
        print(f"Parsing operator prototype from: {args.prototype_file}")
        op_def = OperatorDefinition.from_file(args.prototype_file)

        # 2. Parse all test cases from the case file
        print(f"Parsing all test cases from: {args.case_file}")
        # The CaseParser will load all cases into a list of RunConfiguration objects.
        all_run_configs = CaseParser.from_file(args.case_file, op_def)

        # 3. Instantiate the ProjectGenerator with all necessary information
        # The project generator will now need both op_def and the list of run_configs.
        project_gen = ProjectGenerator(op_def, all_run_configs, args.op_path, args.op_type)
        
        # 4. Generate the entire project
        project_gen.generate(args.output_dir)

    except (RuntimeError, ValueError, KeyError) as e:
        print(f"\nAn error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()