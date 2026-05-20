import os
from input_parse.input_desc import InputDesc
input_list=[]

def parse_input_desc(input_desc, case_name, case_path, timestamp, op_name):
    name = input_desc.get("name")
    format = input_desc.get("format")
    data_type = input_desc.get("data_type")
    param_type = input_desc.get("param_type")
    shape = input_desc.get("shape")
    if shape is None or len(shape) == 0:
        shape = [1] # 标量输入
    data_path = input_desc.get("data_path")
    # 如果路径未设置，使用默认路径
    if data_path is None or len(data_path) == 0:
        data_path = "op_test/{}_{}_{}/input/{}.bin".format(op_name.lower() ,case_name.lower(), timestamp,name)
    # 如果路径不存在，拼接路径
    if case_path and len(case_path.strip()) > 0 :
        data_path = os.path.join(case_path, data_path)
    value_range = input_desc.get("value_range")
    if value_range is None:
        value_range = [0, 1] # 默认值范围

    if len(value_range) == 1:
        value_range = [value_range[0], value_range[0]] # 单值范围，扩展为[min, max]
    elif len(value_range) > 2:
        value_range = [value_range[0], value_range[1]] # 异常情况，取前两个值作为随机范围，保持[min, max]
    input_list.append(InputDesc(name, format, data_type, param_type, shape, data_path, value_range))

# 校验输入顺序是否一致
def check_input_desc_order(input_desc_list, ir_input_desc_list):
    case_required_inputs = []
    ir_required_inputs = []
    ir_dynamic_inputs = set()

    for input_desc in ir_input_desc_list:
        if input_desc.get("param_type") == "required":
            ir_required_inputs.append(input_desc.get("name"))
        elif input_desc.get("param_type") == "dynamic":
            ir_dynamic_inputs.add(input_desc.get("name"))

    for input_desc in input_desc_list:
        name = input_desc.get("name")
        param_type = input_desc.get("param_type")
        if param_type == "required":
            case_required_inputs.append(name)

    # Validate required inputs
    missing_elements = set(ir_required_inputs) - set(case_required_inputs)
    if len(missing_elements) > 0:
        print("The following required inputs are missing in the case file: {}".format(missing_elements))
        return False

    # Validate dynamic inputs: for each ir dynamic input 'x', at least 'x0' must exist in case
    for dyn_name in ir_dynamic_inputs:
        has_any = False
        for input_desc in input_desc_list:
            case_name = input_desc.get("name", "")
            if case_name.startswith(dyn_name) and case_name[len(dyn_name):].isdigit():
                has_any = True
                break
        if not has_any:
            print("Dynamic input '{}' requires at least '{}0' in the case file.".format(dyn_name, dyn_name))
            return False

    # For non-dynamic entries, check order
    case_non_dynamic = [d for d in input_desc_list if d.get("param_type") != "dynamic"]
    ir_non_dynamic = [d for d in ir_input_desc_list if d.get("param_type") != "dynamic"]

    if len(case_non_dynamic) > len(ir_non_dynamic):
        print("The number of non-dynamic inputs in the case file is greater than that in the ir file, {} > {}.".format(
            len(case_non_dynamic), len(ir_non_dynamic)))
        return False
    for i in range(len(case_non_dynamic)):
        if i >= len(ir_non_dynamic):
            print("The input {name} does not exist in the IR.".format(name=case_non_dynamic[i].get("name")))
            return False
        in_ir = False
        for j in range(i, len(ir_non_dynamic)):
            if case_non_dynamic[i].get("name") == ir_non_dynamic[j].get("name"):
                in_ir = True
        if not in_ir:
            print("The input {name} does not exist in the IR.".format(name=case_non_dynamic[i].get("name")))
            return False
    return True



def parse_input_desc_list(input_desc_list, ir_input_desc_list, case_name,case_path, timestamp, op_name):
    if not check_input_desc_order(input_desc_list, ir_input_desc_list):
        return
    for input_desc in input_desc_list:
        parse_input_desc(input_desc, case_name, case_path, timestamp, op_name)
