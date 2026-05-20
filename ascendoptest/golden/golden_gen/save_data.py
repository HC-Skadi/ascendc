from case_parse.case_parse import parse_case_desc
from golden_gen.compute import compute
from pathlib import Path
import os

def save_data_list(data_list, data_path_list):
    if data_list is None:
        print("golden data is None")
        return
    if len(data_list) != len(data_path_list):
        print("expect output num: ", len(data_list), "!= actual output num: ", len(data_path_list))
        return 
    for data, data_path in zip(data_list, data_path_list):
        file_path = Path(data_path)
        dir_path = file_path.parent
        if not dir_path.exists():
            dir_path.mkdir(parents=True)
        if os.path.exists(data_path):
            print("golden data already exists: ", os.path.abspath(data_path))
        else:
            data.tofile(data_path)
            print("gen golden data to: ", os.path.abspath(data_path))

def save_data(case, timestamp):
    case_desc = parse_case_desc(case)
    output_list = compute(case_desc, timestamp)
    output_path_list = []
    for output in case_desc.output_desc_list:
        golden_path = output.get("golden_path")
        name = output.get("name")
        if golden_path is None or len(golden_path) == 0:
           golden_path = "op_test/{}_{}_{}/output/golden_{}.bin".format(case_desc.op_name.lower() ,case_desc.case_name.lower(), timestamp,name)
        if case_desc.case_path and len(case_desc.case_path.strip()) > 0:
            golden_path = os.path.join(case_desc.case_path, golden_path)
        output_path_list.append(golden_path)

    save_data_list(output_list, output_path_list)
    