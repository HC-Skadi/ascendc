import argparse
import json
import csv
import pandas as pd
from pathlib import Path
import os

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--custom_dir", type=str, 
                    help="path of custom prof dir")
parser.add_argument("-b", "--built_in_dir", type=str, 
                    help="path of built-in prof dir")
parser.add_argument("-d", "--out_dir", type=str, 
                    help="path of output dir")
parser.add_argument("-f", "--case_file", type=str, 
                    help="path of case json")
args = parser.parse_args()


def json_to_single_csv_table(json_data, case_name, block_dim, time_use, target="custom", profile_case_dir=""):
    data = {}
    data["target"] = target
    data["case_name"] = case_name
    data["profile_case_dir"] = profile_case_dir
    data["block_dim"] = block_dim
    data["time_use"] = time_use    
    input_list = json_data.get("input_desc")
    for index in range(len(input_list)):
        data["input_"+str(index)+"_name"]= [input_list[index].get("name")]
        data["input_"+str(index)+"_format"]= [input_list[index].get("format")]
        data["input_"+str(index)+"_type"]= [input_list[index].get("data_type")]
        data["input_"+str(index)+"_shape"]= [str(input_list[index].get("shape"))]
        value_range = str(input_list[index].get("value_range"))
        if value_range == "None":
            value_range = [[0,1]]
        data["input_"+str(index)+"_value_range"]= [value_range]
    output_list = json_data.get("output_desc")
    for index in range(len(output_list)):
        data["output_"+str(index)+"_name"]= [output_list[index].get("name")]
        data["output_"+str(index)+"_type"]= [output_list[index].get("data_type")]
        data["output_"+str(index)+"_shape"]= [str(output_list[index].get("shape"))]
        data["output_"+str(index)+"_format"]= [output_list[index].get("format")]
    attr_list = json_data.get("attr_desc", [])
    for index in range(len(attr_list)):
        data["attr_"+str(index)+"_name"]= [attr_list[index].get("name")]
        data["attr_"+str(index)+"_type"]= [attr_list[index].get("type")]
        data["attr_"+str(index)+"_value"]= [attr_list[index].get("value")]
    return pd.DataFrame(data)


def extract_profile_case_dir(file_path, case_name):
    path_obj = Path(file_path).resolve()
    for part in path_obj.parts:
        if part == case_name or part.startswith(case_name + "_"):
            return part
    return None


def get_latest_prof_path(case_name, prof_dir):
    candidates = []
    for root, dirs, files in os.walk(prof_dir):
        current_prof_path = os.path.join(root, "OpBasicInfo.csv")
        if not os.path.isfile(current_prof_path):
            continue
        profile_case_dir = extract_profile_case_dir(current_prof_path, case_name)
        if profile_case_dir is None:
            continue
        candidates.append((profile_case_dir, current_prof_path))
    if not candidates:
        return None, None
    # 目录名自带时间戳后缀，直接按字典序取最新一轮即可。
    profile_case_dir, current_prof_path = max(candidates, key=lambda item: item[0])
    return profile_case_dir, current_prof_path

def get_prof(case_name, case ,prof_dir, target="custom"):
    pd_list = []
    profile_case_dir, current_prof_path = get_latest_prof_path(case_name, prof_dir)
    if current_prof_path is None:
        return pd_list
    with open(current_prof_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            time_use = row['Task Duration(us)']
            block_dim = row['Block Dim']
            pd_data = json_to_single_csv_table(
                case,
                case_name,
                block_dim,
                time_use,
                target,
                profile_case_dir=profile_case_dir,
            )
            pd_list.append(pd_data)
    return pd_list

custom_dir = args.custom_dir
built_in_dir = args.built_in_dir
out_dir = args.out_dir
all_pd_list = []

with open(args.case_file, "r") as f:
    case_json = json.load(f)
    for case in case_json:
        case_name =  case.get("case_name")
        if custom_dir:
            all_pd_list.extend(get_prof(case_name,case, custom_dir, target="custom"))
        if built_in_dir:
            all_pd_list.extend(get_prof(case_name,case, built_in_dir, target="built-in"))
if len(all_pd_list) == 0:
    print("No prof data found")
    exit(1)

merged_df = pd.concat(all_pd_list, ignore_index=True)
os.system(f"mkdir -p {out_dir}")
if out_dir is None:
    out_dir = os.path.abspath(".")
merged_df.to_csv(os.path.join(out_dir, "all_prof.csv"), index=False)