import importlib.util
import os
import re
import numpy as np
from ml_dtypes import bfloat16


def compute(case_desc, timestamp):
    expect_func = case_desc.expect_func
    expect_func_list = expect_func.split(":")
    if len(expect_func_list) < 2:
        return None
    expect_func_path = expect_func_list[0]
    func_name = expect_func_list[1]
    module_name = "custom_module"

    try:
        spec = importlib.util.spec_from_file_location(module_name, expect_func_path)
        custom_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(custom_module)
    except Exception as e:
        print(f"load {expect_func_path} fail, {case_desc.case_name} use default golden bin, error info :", e)
        return None

    try:
        custom_func = getattr(custom_module, func_name)
    except AttributeError as e:
        print(f"load {expect_func_path} fail, {case_desc.case_name} use default golden bin, error info :", e)
        return None

    # Load all input data and track dynamic grouping
    dynamic_groups = {}  # proto_name -> [(index, data)]
    regular_inputs = []  # list of (original_index, data) for non-dynamic inputs

    for i, input_desc in enumerate(case_desc.input_desc_list):
        input_path = input_desc.get("data_path")
        name = input_desc.get("name")
        param_type = input_desc.get("param_type", "required")

        if input_path is None or len(input_path) == 0:
            input_path = "op_test/{}_{}_{}/input/{}.bin".format(
                case_desc.op_name.lower(), case_desc.case_name.lower(), timestamp, name)

        if case_desc.case_path and len(case_desc.case_path.strip()) > 0:
            input_path = os.path.join(case_desc.case_path, input_path)

        input_type = input_desc.get("data_type")
        if input_type == "float":
            input_type = "float32"
        elif input_type == "bf16":
            input_type = "bfloat16"

        input_data = np.fromfile(input_path, input_type)
        try:
            input_data = input_data.reshape(input_desc.get("shape"))
        except Exception as e:
            print(f"reshape {input_path} fail, Please verify whether the shape of the input file is consistent with the shape specified in the test case file.")
            return None

        if param_type == "dynamic":
            m = re.match(r'^(.+?)(\d+)$', name)
            if m:
                proto_name = m.group(1)
                idx = int(m.group(2))
                if proto_name not in dynamic_groups:
                    dynamic_groups[proto_name] = []
                dynamic_groups[proto_name].append((idx, input_data))
            else:
                regular_inputs.append((i, input_data))
        else:
            regular_inputs.append((i, input_data))

    # Build input_list preserving order: dynamic groups as lists, regular inputs individually
    # For expect_func compatibility: unpack dynamic groups so each tensor is a separate argument
    input_list = []
    seen_dynamic = set()
    regular_idx = 0

    for input_desc in case_desc.input_desc_list:
        name = input_desc.get("name")
        param_type = input_desc.get("param_type", "required")
        if param_type == "dynamic":
            m = re.match(r'^(.+?)(\d+)$', name)
            if m:
                proto_name = m.group(1)
                if proto_name not in seen_dynamic:
                    seen_dynamic.add(proto_name)
                    group = dynamic_groups[proto_name]
                    group.sort(key=lambda t: t[0])
                    for _, data in group:
                        input_list.append(data)
        else:
            if regular_idx < len(regular_inputs):
                input_list.append(regular_inputs[regular_idx][1])
                regular_idx += 1

    if case_desc.attr_list is None:
        case_desc.attr_list = []

    attr_list = []
    for attr in case_desc.attr_list:
        attr_list.append(attr.get("value"))

    if len(attr_list) == 0 and len(input_list) > 0:
        output_list = custom_func(*input_list)
    elif len(attr_list) > 0 and len(input_list) == 0:
        output_list = custom_func(*attr_list)
    elif len(attr_list) > 0 and len(input_list) > 0:
        output_list = custom_func(*input_list, *attr_list)
    else:
        print(f"case: {case_desc.case_name} input and output is empty, use default golden bin")
        return None
    return output_list
