import os
from output_parse.output_desc import OutputDesc
output_list = []

def parse_output_desc(output_desc,case_name, case_path, op_name, timestamp):
    name = output_desc.get("name")
    format = output_desc.get("format")
    data_type = output_desc.get("data_type")
    param_type = output_desc.get("param_type")
    shape = output_desc.get("shape")
    data_path = output_desc.get("data_path")

    if data_path is None or len(data_path) == 0:
        data_path = "op_test/{}_{}_{}/output/{}.bin".format(op_name.lower() ,case_name.lower(), timestamp,name)
    golden_path = output_desc.get("golden_path")

    if golden_path is None or len(golden_path) == 0:
        golden_path = "op_test/{}_{}_{}/output/golden_{}.bin".format(op_name.lower() ,case_name.lower(), timestamp,name)
    if case_path and len(case_path.strip()) > 0:
        golden_path = os.path.join(case_path, golden_path)
        data_path = os.path.join(case_path, data_path)
    err_threshold = output_desc.get("err_threshold")
    output_list.append(OutputDesc(name, format, data_type, param_type, shape, data_path, golden_path, err_threshold))

def parse_output_desc_list(output_desc_list,case_name, case_path, op_name, timestamp):
    
    for output_desc in output_desc_list:
        parse_output_desc(output_desc,case_name, case_path, op_name, timestamp)
