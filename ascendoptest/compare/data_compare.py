import sys
import json
import os
import argparse
from compare.verify_result import verify_output_list

parser = argparse.ArgumentParser()
# ir json
parser.add_argument("-i", "--ir_json", type=str, 
                    help="path of ir json")
# case json
parser.add_argument("-c", "--case_json", type=str, 
                    help="path of case json")

parser.add_argument("-e", "--error_num", type=int, default=10,
                    help="print error results num")

# timestamp
parser.add_argument("-t", "--timestamp", type=str, default="0",
                    help="name of msprof out dir")
                
# test case name
parser.add_argument("-n", "--case_name", type=str,default=None, 
                    help="test case name")

# test case name
parser.add_argument("-r", "--result", type=str, default="result.csv",
                    help="result csv file name")
args = parser.parse_args()

if __name__ == "__main__":
    if not args.ir_json or not args.case_json or not args.timestamp:
        parser.print_help()
        exit(1)
    if not os.path.exists(args.ir_json) or not os.path.exists(args.case_json):
        parser.print_help()
        exit(1)
    
    ir_json = args.ir_json
    case_json = args.case_json
    case_name = args.case_name
    timestamp = args.timestamp
    result_path = args.result
    error_num = args.error_num
 
    with open(case_json, "r") as f:
        case_list = json.load(f)
        for case in case_list:
            output_desc_list = case.get("output_desc")
            case_path = case.get("case_path")
            op_name = case.get("op_name")
            if case_name:
                if case_name == case.get("case_name"):
                    verify_output_list(output_desc_list,case_name, result_path, case_path, op_name, timestamp, error_num)
            else:
                case_name = case.get("case_name")
                verify_output_list(output_desc_list,case_name, result_path, case_path, op_name, timestamp, error_num)
                case_name = None
