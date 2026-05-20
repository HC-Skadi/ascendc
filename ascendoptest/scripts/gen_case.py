import argparse
import sys
import importlib
from pathlib import Path
import copy
import numpy as np
import math
import json
import os
import re

parser = argparse.ArgumentParser()
# ir json
parser.add_argument("-i", "--ir_json", type=str, required=True,
                    help="path of ir json")
parser.add_argument("-c", "--constraint_condition", type=str,
                    help="file path of constraint condition py")
parser.add_argument("-f", "--constraint_condition_func", type=str, default="constraint_condition",
                    help="function name of constraint condition py")
parser.add_argument("-o", "--out_json", type=str, default="case.json",
                    help="path of out case json")
parser.add_argument("-n", "--num", type=int, default=1,
                    help="Generate a specified number of cases")
parser.add_argument("-b", "--gen_broadcast", type=bool, default=False,
                    help="whether to generate broadcast case")

parser.add_argument("-d", "--dim", type=int, choices=range(1, 9),
                    help="dim of case, default is all dim")
args = parser.parse_args()


def constraint_condition(case, constraint_condition_module, constraint_condition_func):
    if constraint_condition_module is None:
        return True
    try:
        constraint_condition_func = getattr(constraint_condition_module, constraint_condition_func)
    except AttributeError:
        print(f"constraint_condition_func {constraint_condition_func} not found in {constraint_condition_file}")
        return False
    return constraint_condition_func(case)


def gen_unaligned_case(case, dim=None, min_dim_value=1, max_dim_value1=129, max_dim_value2=10000, check_align=False,
                       broadcast=False):
    '''
    生成shape内元素乘积乘元素类型占用字节数为非32倍数的用例
    :param case: 输入用例
    :param dim: 用例维度，默认None表示任意维度
    :param min_dim_value: 用例维度最小值，默认1
    :param max_dim_value1: 用例维度前n-2维最大值，默认129
    :param max_dim_value2: 用例维度最后两维最大值，默认10000
    :param check_align: 是否检查对齐，默认False不检查
    :param broadcast: 是否生成广播用例，默认False不生成
    :return: 生成的随机用例
    '''
    dim_pro = np.random.rand()

    if dim is None or dim == 0:
        # 当dim为None时，默认允许shape为1~8维度,较大概率生成1~4维用例
        if dim_pro > 0.9:
            dim = np.random.randint(6, 9)
        elif dim_pro > 0.8:
            dim = np.random.randint(5, 7)
        else:
            dim = np.random.randint(1, 5)
    # 随机生成dim个维度的shape
    shape = []
    # max_dim_value2 = max_dim_value2 // dim # 防止出现极大值
    for i in range(dim):
        if i < dim - 2:  # 前面的维度（非最后两维）
            shape.append(np.random.randint(min_dim_value, max_dim_value1))
        else:  # 最后两维
            shape.append(np.random.randint(min_dim_value, max_dim_value2))
    # 设置max_allowed最大为float类型时2G的数据量
    max_allowed = 2 * 1024 * 1024 * 1024 / 4
    try_unaligned = 0
    while math.prod(shape) > max_allowed or (
            check_align and (math.prod(shape) * 4 % 32 == 0)):  # 确保shape内元素乘积乘元素类型占用字节数为非32倍数, 如果要支持double类型非对齐，应修改为*8
        shape = []
        try_unaligned += 1
        for i in range(dim):
            if i < dim - 2:
                shape.append(np.random.randint(min_dim_value, max_dim_value1))
            else:  # 最后两维
                shape.append(np.random.randint(min_dim_value, max_dim_value2))
        if try_unaligned > 100:# 最多尝试100次, 仍未生成符合要求的shape, 则随机生成小shape
            shape= []
            for i in range(dim): 
                shape.append(np.random.randint(2, dim))
            break

    # 修改case内的input_desc和output_desc的shape字段
    for desc in case["input_desc"] + case["output_desc"]:
        desc["shape"] = shape.copy()  # 关键：避免所有desc共享同一shape列表

    if broadcast:
        if len(case["input_desc"]) > 1:
            # 随机选一个输入desc
            selected_input_idx = np.random.randint(0, len(case["input_desc"]))
            selected_input = case["input_desc"][selected_input_idx]

            # 找到该输入shape中的非1维度索引
            non_one_dims = [i for i, size in enumerate(selected_input["shape"]) if size != 1]

            if non_one_dims:
                # 随机选一个非1维度，改为1
                change_dim = np.random.choice(non_one_dims)
                old_val = selected_input["shape"][change_dim]
                selected_input["shape"][change_dim] = 1

    return case


# 根据每个input的data_type设置每个input的取值范围value_range，根据attr的type设置attr随机的value
def set_case_value_random(case, min_value=-100.0, min_value2=0, max_value=100):
    # 为每个input设置取值范围value_range
    for input_desc in case["input_desc"]:
        data_type = input_desc["data_type"]
        if "uint" in data_type:
            input_desc["value_range"] = [min_value2, max_value]
        elif data_type == "bool":
            input_desc["value_range"] = [0, 1]
        else:
            input_desc["value_range"] = [min_value, max_value]
        # 为每个attr设置取值范围value_range
    for attr in case["attr_desc"]:
        attr_type = attr["type"]
        if attr_type == "bool":
            attr["value"] = bool(np.random.choice([True, False]))
        elif attr_type == "string":
            attr["value"] = None
        elif "list_" in attr_type:
            attr["value"] = [np.random.randint(0, 1) for _ in range(5)]
        else:
            attr["value"] = np.random.randint(0, 1)

    return case


# 根据每个input的data_type设置每个input的取值范围value_range, 并确保该取值范围为对应类型的边界值
def set_case_value_boundary(case, maximum_value_boundary=False):
    """
    根据input的data_type设置取值范围value_range
    :param case: 包含input_desc的测试用例字典
    :param maximum_value_boundary: 是否设置为最大边界值，默认False为最小边界值
    :return: 修改后的case
    """
    uint_pattern = re.compile(r"^uint(\d+)$")  # 提取uint后的位数（如uint32→32）
    int_pattern = re.compile(r"^int(\d+)$")  # 提取int后的位数（如int16→16）

    for input_desc in case["input_desc"]:
        data_type = input_desc["data_type"]
        min_val, max_val = None, None

        # ---------------------- 1. 处理无符号整数（uintX） ----------------------
        uint_match = uint_pattern.match(data_type)
        if uint_match:
            bits = int(uint_match.group(1))
            min_val = 0
            max_val = (1 << bits) - 1

            # ---------------------- 2. 处理有符号整数（intX） ----------------------
        elif int_pattern.match(data_type):
            bits = int(int_pattern.match(data_type).group(1))
            min_val = -(1 << (bits - 1))
            max_val = (1 << (bits - 1)) - 1

        # ---------------------- 3. 处理其他常见类型 ----------------------
        else:
            # 可根据实际需求扩展更多类型
            type_lower = data_type.lower()
            if type_lower in ["float32", "float"]:
                min_val = -3.4028235e+38
                max_val = 3.4028235e+38
            elif type_lower == "float64":
                min_val = -1.7976931348623157e+308
                max_val = 1.7976931348623157e+308
            elif type_lower == "bool":
                min_val, max_val = 0, 1
            elif type_lower == "bfloat16":
                min_val = -3.4e+38  # 约等于-3.39e+38
                max_val = 3.4e+38  # 约等于3.39e+38
            elif type_lower == "float16":
                min_val = -65504
                max_val = 65504
            else:  # 其他类型，暂时默认取值范围为0
                min_val = 0
                max_val = 0

        if maximum_value_boundary:
            input_desc["value_range"] = [max_val, max_val]
        else:
            input_desc["value_range"] = [min_val, min_val]

    return case


def generate_case_with_independent_input(op_file_path):
    try:
        with open(op_file_path, 'r', encoding='utf-8') as f:
            op_data = json.load(f)
        target_op = op_data[0] if op_data else None
        if not target_op:
            print("Check the IR json to confirm that it contains the \"op\" field.")
            exit(1)

        op_name = target_op["op"]
        input_params = target_op["input_desc"]
        output_param = target_op["output_desc"]
        op_attrs = target_op.get("attr", [])

        input_configs = []
        for param in input_params:
            input_configs.append({
                "name": param["name"],
                "format_list": param.get("format", []),
                "type_list": param.get("type", []),
                "param_type": param.get("param_type", "required")
            })

        output_format_list = output_param[0].get("format", [])
        output_type_list = output_param[0].get("type", [])

        format_lengths = [len(cfg["format_list"]) for cfg in input_configs]
        if len(set(format_lengths)) != 1:
            print("Please verify whether the IR json content is correct. Input format list does not match.")
            exit(1)
        combo_count = format_lengths[0]

        if len(output_format_list) != combo_count or len(output_type_list) != combo_count:
            print(
                f"Error: The length of the output parameter list (format/type) ({len(output_format_list)}/{len(output_type_list)}) does not match the input (it should be {combo_count})")
            exit(1)
    except (FileNotFoundError, json.JSONDecodeError, KeyError, IndexError) as e:
        print(f"Please verify whether the IR json content is correct. {str(e)}")
        exit(1)

    final_cases = []
    for combo_idx in range(combo_count):
        case_name = f"Test_{str(combo_idx + 1).zfill(3)}"

        input_desc = []
        output_desc = []
        for cfg in input_configs:
            target_format = cfg["format_list"][combo_idx]
            target_dtype = cfg["type_list"][combo_idx]
            if cfg["param_type"] == "dynamic":
                # Generate 3 numbered entries for dynamic inputs
                default_dynamic_count = 3
                for di in range(default_dynamic_count):
                    param_attr = {
                        "format": target_format,
                        "data_type": target_dtype,
                        "param_type": "dynamic",
                        "shape": [],
                        "value_range": [],
                        "name": f"{cfg['name']}{di}",
                        "data_path": ""
                    }
                    input_desc.append(param_attr)
            else:
                param_attr = {
                    "format": target_format,
                    "data_type": target_dtype,
                    "param_type": "required",
                    "shape": [],
                    "value_range": [],
                    "name": cfg["name"],
                    "data_path": ""
                }
                input_desc.append(param_attr)
        for out_param in output_param:
            out_param_type = out_param.get("param_type", "required")
            if out_param_type == "dynamic":
                default_dynamic_count = 3
                for di in range(default_dynamic_count):
                    output_desc.append({
                        "format": output_format_list[combo_idx],
                        "data_type": output_type_list[combo_idx],
                        "param_type": "dynamic",
                        "shape": [],
                        "name": f"{out_param['name']}{di}",
                        "data_path": "",
                        "golden_path": "",
                        "err_threshold": []
                    })
            else:
                output_desc.append({
                    "format": output_format_list[combo_idx],
                    "data_type": output_type_list[combo_idx],
                    "param_type": "required",
                    "shape": [],
                    "name": out_param["name"],
                    "data_path": "",
                    "golden_path": "",
                    "err_threshold": []
                })
        attr_desc = []
        for attr in op_attrs:
            attr_info = {
                "name": attr["name"],
                "param_type": attr["param_type"],
                "type": attr["type"],
                "value": None
            }
            attr_desc.append(attr_info)
        case = {
            "case_name": case_name,
            "op_name": op_name,
            "case_path": "",
            "expect_func": "",
            "input_desc": input_desc,
            "output_desc": output_desc,
            "attr_desc": attr_desc
        }
        final_cases.append(case)

    return final_cases


if __name__ == "__main__":
    constraint_condition_file = args.constraint_condition
    constraint_condition_func = args.constraint_condition_func
    ir_json = args.ir_json
    out_json = args.out_json
    num = args.num
    dim = args.dim
    gen_broadcast = args.gen_broadcast

    # 至少生成1个用例
    if num is None or num < 1:
        print(f"num {num} is invalid, it should be greater than 0")
        exit(1)
    # 可以不设置，但设置时只能取1~8
    if dim is not None and dim < 1:
        print(f"dim {dim} is invalid, it should be greater than 0")
        exit(1)

    case_model = generate_case_with_independent_input(ir_json)  # 根据data_type和format生成用例模板

    if constraint_condition_file is not None:  # 加载约束文件
        if os.path.exists(constraint_condition_file):
            file_path = Path(constraint_condition_file)
            file_abs_path = file_path.resolve()
            folder_abs_path = file_abs_path.parent
            if folder_abs_path not in sys.path:
                sys.path.append(folder_abs_path)  # 添加到sys.path中
            try:
                constraint_condition_module = importlib.import_module(
                    file_path.stem)  # 加载constraint_condition_file所在文件夹下的模块
            except ImportError as e:
                print(f"Failed to load module:{e}")
                exit(1)

    # 根据模板生成num个用例
    final_cases = []
    for i in range(num):
        case_tmp = copy.deepcopy(case_model[i % len(case_model)])  # 这里需要Copy，否则会改变case_model中的值，导致最终生成的用例名有重复
        case_tmp["case_name"] = f"Test_{str(i + 1).zfill(3)}"
        r1 = np.random.rand()  # 生成的随机数，用于判断生成对齐或非对齐用例
        r2 = np.random.rand()  # 生成随机数，用于判断是否生成广播用例
        max_dim_value2 = 10000
        max_dim_value1 = 129
        if r2 >0.2:
            max_dim_value2 = 129
            max_dim_value1 = 30
        if r1 < 0.6:  # 60%概率非对齐样例
            case_tmp = gen_unaligned_case(case_tmp, dim, min_dim_value=2, max_dim_value1=max_dim_value1, max_dim_value2=max_dim_value2,check_align=True, broadcast=r2 < 0.1 and gen_broadcast)
        else:  # 40%概率一般随机样例, 一般随机样例也可能是非对齐样例
            case_tmp = gen_unaligned_case(case_tmp, dim, min_dim_value=2, max_dim_value1=max_dim_value1, max_dim_value2=max_dim_value2, broadcast=r2 < 0.1 and gen_broadcast)

        case_tmp = set_case_value_random(case_tmp)

        r3 = np.random.rand()  # 生成随机数，用于生成极限值数据
        if r3 < 0.1:  # 10%概率生成极限值数据
            case_tmp = set_case_value_boundary(case_tmp, maximum_value_boundary=r3 > 0.05)  # 5%生成上边界，95%生成下边界

        if constraint_condition_file is not None: 
            case_tmp = constraint_condition(case_tmp, constraint_condition_module,
                                            constraint_condition_func)  # 调用约束条件函数，修改用例使其满足约束
        final_cases.append(case_tmp)

    # 判断out_json所在目录是否存在，不存在则先创建目录
    out_json_dir = os.path.dirname(out_json)
    if out_json_dir and not os.path.exists(out_json_dir):
        os.makedirs(out_json_dir)

    # 保存到json文件
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(final_cases, f, ensure_ascii=False, indent=4)
