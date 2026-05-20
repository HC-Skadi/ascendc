import argparse
import os
import shutil
import json
import re
from datetime import datetime
import csv
from typing import List, Dict, Union
import platform
import subprocess
import configparser
import numpy as np
import importlib.util
from ml_dtypes import bfloat16

parser = argparse.ArgumentParser()

# ir json
parser.add_argument("-i", "--ir_json", type=str, 
                    help="path of ir json")
# case json
parser.add_argument("-c", "--case_json", type=str, 
                    help="path of case json")

# aclnn dir
parser.add_argument("-a", "--aclnn_dir", type=str, default="aclnn_op", 
                    help="name of aclnn project")

# # aclnn dir
# parser.add_argument("-b", "--test_bck", type=str, default="test", 
#                     help="Backup of test data")
# msprof dir
parser.add_argument("-d", "--msprof_dir", type=str,
                    help="name of msprof out dir")

parser.add_argument("-e", "--error_num", type=int, default=10,
                    help="print error results num")
                
# test case name
parser.add_argument("-n", "--case_name", type=str,
                    help="test case name")

# test case result
parser.add_argument("-r", "--result", type=str, default="result.csv",
                    help="result csv file name")

# test case result
parser.add_argument("-k", "--kernel_name", type=str,
                    help="kernel name")

parser.add_argument("--msprof", action="store_true",
                    help="enable msprof")

parser.add_argument("--op", action="store_true", 
                    help="msprof op or msprof --application")

parser.add_argument("--sim", action="store_true", 
                    help="enable simulator")

parser.add_argument("--build", action="store_true", 
                    help="build aclnn project, default is False, if config while gen aclnn project and build exe")

# custom operator package path
parser.add_argument("--op-path", type=str, default="/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/prelu_nn/op_api",
                    help="path to the custom operator package directory")

# operator type
parser.add_argument("--op-type", type=str, default="custom", choices=["custom", "builtin"],
                    help="type of the operator: 'custom' or 'builtin' (default: custom)")

args = parser.parse_args()


# where is the current script
current_script_path = os.path.abspath(__file__)
# where is the current dir
current_dir_path = os.path.dirname(current_script_path)
os.system("echo case_name,name,data_path,golden_path,compare_result > {}".format(args.result))

# 根据CANN的set_env.sh内配置的ASCEND_TOOLKIT_HOME来自动设置DDK_PATH和NPU_HOST_LIB环境变量，如果未source set_env.sh则需要用户自己手动设置DDK_PATH和NPU_HOST_LIB
if os.getenv("ASCEND_TOOLKIT_HOME") is None:
    print("env of CANN is not set, please source set_env.sh first")
    # exit(1)  此处应该退出，但用户可以手动设置DDK_PATH和NPU_HOST_LIB环境变量，所以不退出
else:
    os.environ["DDK_PATH"] = os.getenv("ASCEND_TOOLKIT_HOME")
    arch = platform.machine() 
    system_name = platform.system().lower() 
    os.environ["NPU_HOST_LIB"] =  os.getenv("ASCEND_TOOLKIT_HOME") + f"/lib64"

def get_aclnn_gen_version():
    try:
        result = subprocess.run(
            'pip list --format=freeze 2>/dev/null | grep "^aclnn-gen"',
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        output = result.stdout.decode("utf-8").strip()
        return output.split("==", maxsplit=1)[1] if output else None
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError) as e:
        return "0.0.1"

def extract_cases_with_result(
    original_json_path: str,
    target_case_name: str,
    # output_json_path: str,
    result_csv_path: str
) -> List[Dict]:
    """
    从原始JSON测试用例文件中提取指定case_name的用例，并关联result.csv中的路径信息后保存
    
    参数:
        original_json_path (str): 原始JSON测试用例文件路径
        target_case_name (str): 需要提取的目标用例名称
        result_csv_path (str): 结果CSV文件路径（包含路径信息）
    
    返回:
        List[Dict]: 提取并填充路径后的用例列表
    """

    try:
        # -------------------- 步骤1：读取并解析原始JSON用例 --------------------
        with open(original_json_path, 'r', encoding='utf-8') as f:
            original_cases: List[Dict] = json.load(f)
        
        if not isinstance(original_cases, list):
            raise ValueError("Original JSON data format error: top level should be a list")
        
        # 提取目标用例（支持重复case_name）
        extracted_cases = [
            case for case in original_cases 
            if case.get('case_name') == target_case_name
        ]
        if not extracted_cases:
            print(f"Warning: No case with case_name '{target_case_name}' found in the original JSON")
            return []

        # -------------------- 步骤2：读取并校验result.csv数据（增强空值容错） --------------------
        required_columns = {'case_name', 'name', 'data_path', 'golden_path', 'compare_result'}
        csv_records = []
        
        with open(result_csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            # 校验CSV表头是否完整（适配新的name字段）
            if not required_columns.issubset(reader.fieldnames or []):
                missing = required_columns - set(reader.fieldnames or [])
                raise ValueError(f"CSV file is missing required columns: {missing}. Please check the file format (must include: {required_columns})")
            
            for row_num, row in enumerate(reader, 2):  # 行号从2开始（表头占第1行）
                # 过滤非目标用例的记录
                if row.get('case_name') != target_case_name:
                    continue
                
                # 清洗关键字段（增强空值容错：使用get+默认空字符串）
                param_name = row.get('name', '').strip()  # 避免name字段缺失
                data_path = row.get('data_path', '').strip()  # 避免data_path为None
                golden_path = row.get('golden_path', '').strip()  # 避免golden_path为None
                
                csv_records.append({
                    'param_name': param_name,
                    'data_path': data_path,
                    'golden_path': golden_path
                })
        
        if not csv_records:
            print(f"Warning: No records with case_name '{target_case_name}' found in result.csv")
            return extracted_cases  # 返回未修改的原始用例

        output_json_path = None
        # -------------------- 步骤3：路径信息填充（严格隔离input/output处理） --------------------
        for case in extracted_cases:
            
            # -------------------- 处理输入参数（仅data_path，完全忽略golden_path） --------------------
            input_params = {p['name']: p for p in case.get('input_desc', [])}  # 按name建立索引
            for csv_record in csv_records:
                param_name = csv_record['param_name']
                if param_name not in input_params:
                    continue  # 跳过输出参数或无匹配的输入参数

                input_param = input_params[param_name]
                # 仅更新输入参数的data_path（输入参数无golden_path字段）
                if csv_record['data_path']:  # 仅当CSV中data_path非空时覆盖
                    # # 备份输入bin文件
                    # cmd = "cp {} {}".format(csv_record['data_path'],os.path.join(os.path.dirname(output_json_path),"input"))
                    # os.system(cmd)
                    # 备份ir文件
                    output_json_path = os.path.join(os.path.dirname(os.path.dirname(csv_record['data_path'])),args.case_name+".json")
                    os.system("cp {} {}".format(args.ir_json,os.path.dirname(output_json_path)))
                    input_param['data_path'] = csv_record['data_path']
                    # if csv_record['data_path'] is None or not os.path.exists(csv_record['data_path']) or len(csv_record['data_path']) == 0:
                    #     input_param['data_path'] = csv_record['data_path']
                    

            # -------------------- 处理输出参数（data_path + golden_path） --------------------
            output_params = {p['name']: p for p in case.get('output_desc', [])}  # 按name建立索引
            for csv_record in csv_records:
                param_name = csv_record['param_name']
                if param_name not in output_params:
                    continue  # 跳过输入参数或无匹配的输出参数
                
                output_param = output_params[param_name]
                # 更新输出参数的data_path（实际输出路径）
                if csv_record['data_path']:
                    # 备份实际输出文件
                    # os.system("cp {} {}".format(csv_record['data_path'],os.path.join(os.path.dirname(output_json_path),"output")))
                    # output_param['data_path'] = os.path.join(os.path.dirname(output_json_path),"output",os.path.basename(csv_record['data_path']))
                    output_param['data_path'] = csv_record['data_path']
                    # 防止算子只有输出时找不到output_json_path
                    output_json_path = os.path.join(os.path.dirname(os.path.dirname(csv_record['data_path'])),args.case_name+".json")
                # 更新输出参数的golden_path（预期结果路径）
                if csv_record['golden_path']:  # 仅当CSV中golden_path非空时覆盖
                    # # 备份golden文件
                    # os.system("cp {} {}".format(csv_record['golden_path'],os.path.join(os.path.dirname(output_json_path),"output")))
                    # output_param['golden_path'] = os.path.join(os.path.dirname(output_json_path),"output",os.path.basename(csv_record['golden_path']))
                    output_param['golden_path'] = csv_record['golden_path']
                    

        # -------------------- 步骤4：写入结果文件 --------------------
        with open(output_json_path, 'w', encoding='utf-8') as f:
            json.dump(
                extracted_cases, 
                f, 
                indent=4,
                ensure_ascii=False,
                sort_keys=False
            )
        return extracted_cases
    
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {str(e)}")
    except json.JSONDecodeError:
        raise ValueError(f"JSON parsing failed. Please check the file format: {original_json_path}")
    except csv.Error as e:
        raise ValueError(f"CSV parsing failed: {str(e)} (please check the file encoding or delimiter)")
    except Exception as e:
        raise RuntimeError(f"An unknown error occurred during processing: {str(e)}")

# 校验输入顺序是否一致
def check_order(desc_list, ir_desc_list):
    case_required = []
    ir_required = []
    ir_dynamic = set()

    for desc in ir_desc_list:
        if desc.get("param_type") == "required":
            ir_required.append(desc.get("name"))
        elif desc.get("param_type") == "dynamic":
            ir_dynamic.add(desc.get("name"))
    for desc in desc_list:
        if desc.get("param_type") == "required":
            case_required.append(desc.get("name"))

    missing_elements = set(ir_required) - set(case_required)
    if len(missing_elements) > 0:
        print("The following required params are missing in the case file: {}".format(missing_elements))
        return False

    # Validate dynamic params
    for dyn_name in ir_dynamic:
        has_any = False
        for desc in desc_list:
            case_name = desc.get("name", "")
            if case_name.startswith(dyn_name) and case_name[len(dyn_name):].isdigit():
                has_any = True
                break
        if not has_any:
            print("Dynamic param '{}' requires at least '{}0' in the case file.".format(dyn_name, dyn_name))
            return False

    # Non-dynamic order check
    case_non_dynamic = [d for d in desc_list if d.get("param_type") != "dynamic"]
    ir_non_dynamic = [d for d in ir_desc_list if d.get("param_type") != "dynamic"]

    if len(case_non_dynamic) > len(ir_non_dynamic):
        print("The number of non-dynamic params in the case file is greater than that in the ir file, {} > {}.".format(
            len(case_non_dynamic), len(ir_non_dynamic)))
        return False
    for i in range(len(case_non_dynamic)):
        if i >= len(ir_non_dynamic):
            print("The param {name} does not exist in the IR.".format(name=case_non_dynamic[i].get("name")))
            return False
        in_ir = False
        for j in range(i, len(ir_non_dynamic)):
            if case_non_dynamic[i].get("name") == ir_non_dynamic[j].get("name"):
                in_ir = True
        if not in_ir:
            print("The param {name} does not exist in the IR.".format(name=case_non_dynamic[i].get("name")))
            return False
    return True


def get_exe_name():
    try:
        with open(args.aclnn_dir+"/CMakeLists.txt", 'r', encoding='utf-8') as f:  # 按需调整编码（如 gbk）
            for line in f:
                if "add_executable" in line:
                    exe_name = line.split("(")[1]
                    return exe_name.strip()
    except Exception:
        print("CMakeLists.txt not found in the specified directory. check IR.json.")
        return None

def run_test(current_timestamp, kernel_name, case_tmp):
    if kernel_name is not None:
        kernel_name = kernel_name.strip()
    print("start run case",args.case_name)
    # gen input
    cmd = "python -B {} -i {} -c {} -n {} -t {} -r {}".format(os.path.join(current_dir_path, "data_gen/data_gen.py"), args.ir_json, args.case_json, args.case_name, current_timestamp,args.result)
    os.system(cmd)
    all_output_shape = compute_out_shape(case_tmp, current_timestamp)
    # gen golden output
    cmd = "python -B {} -i {} -c {} -n {} -t {}".format(os.path.join(current_dir_path, "golden/golden_gen.py"), args.ir_json, args.case_json, args.case_name, current_timestamp)
    os.system(cmd)

    # run aclnn exe
    exe_name = get_exe_name()
    if exe_name is None or os.path.exists(args.aclnn_dir+"/build/"+exe_name) is False:
        print("get aclnn exe failed, check IR.json, make sure it's right.")
        return
    exe_path = os.path.join(args.aclnn_dir, "build", exe_name)
    if not os.path.isabs(exe_path):
        exe_path = "./{}".format(exe_path)
    msprof_dir_name = None
    if args.msprof:
        if args.op:
            if args.sim:
                if args.msprof_dir:
                    msprof_dir_name = args.msprof_dir+"/"+"{}_{}".format(args.case_name, current_timestamp)
                else:
                    msprof_dir_name = "{}_{}_msprof_op_simulator".format(args.case_name, current_timestamp)
                cmd = "msprof op simulator --kernel-name={} --output={} {} --case_name {} --timestamp {} ".format(kernel_name, msprof_dir_name, exe_path, args.case_name, current_timestamp)
            else:
                if args.msprof_dir:
                    msprof_dir_name = args.msprof_dir+"/"+"{}_{}".format(args.case_name, current_timestamp)
                else:
                    msprof_dir_name = "{}_{}_msprof_op".format(args.case_name, current_timestamp)

                cmd = "msprof op --warm-up=5 --kernel-name={} --output={} {}  --case_name {} --timestamp {} ".format(kernel_name, msprof_dir_name, exe_path,  args.case_name, current_timestamp)
        else:
            if args.msprof_dir:
                msprof_dir_name = args.msprof_dir+"/"+"{}_{}".format(args.case_name, current_timestamp)
            else:
                msprof_dir_name = "{}_{}_msprof_application".format(args.case_name, current_timestamp)
            cmd = "msprof --application=\"{} --case_name {} --timestamp {} \" --output={}".format(exe_path, args.case_name, current_timestamp, msprof_dir_name)
    else:
        cmd = "{} --case_name {} --timestamp {} ".format(exe_path, args.case_name, current_timestamp)
    
    if all_output_shape is not None and len(all_output_shape) > 0:
        cmd += " --output_shapes {}".format("\""+str(all_output_shape)+"\"")

    os.system(cmd)

    # compare output
    cmd = "python -B {} -i {} -c {} -n {} -t {} -r{} -e {}".format(os.path.join(current_dir_path, "compare/data_compare.py"), args.ir_json, args.case_json, args.case_name, current_timestamp,args.result, args.error_num)
    os.system(cmd)

    extract_cases_with_result(original_json_path=args.case_json, target_case_name=args.case_name, result_csv_path=args.result)
    print("end run case",args.case_name)


def get_setup_cfg_version(setup_cfg_path):
    config = configparser.ConfigParser()
    if not os.path.exists(setup_cfg_path):
        print(f"setup.cfg not found at: {setup_cfg_path}")
        return "0.0.1"
    config.read(setup_cfg_path, encoding="utf-8")
    try:
        version = config.get("metadata", "version").strip()
        return version
    except configparser.NoSectionError:
        print("setup.cfg is missing the [metadata] section")
        return "0.0.1"
    except configparser.NoOptionError:
        print("the [metadata] section in setup.cfg is missing the 'version' option")
        return "0.0.1"


def compute_out_shape(case, timestamp):
    output_desc_list = case.get("output_desc")
    attr_list = []
    all_output_shape = {}

    # Load and group inputs
    dynamic_groups = {}
    regular_inputs = []

    for input_desc in case.get("input_desc"):
        input_path = input_desc.get("data_path")
        name = input_desc.get("name")
        param_type = input_desc.get("param_type", "required")

        if input_path is None or len(input_path) == 0:
            input_path = "op_test/{}_{}_{}/input/{}.bin".format(
                case.get("op_name").lower(), case.get("case_name").lower(), timestamp, name)

        if case.get("case_path") and len(case.get("case_path").strip()) > 0:
            input_path = os.path.join(case.get("case_path"), input_path)

        input_type = input_desc.get("data_type")
        if input_type == "float":
            input_type = "float32"
        elif input_type == "bf16":
            input_type = "bfloat16"

        input_data = np.fromfile(input_path, input_type)
        input_data = input_data.reshape(input_desc.get("shape"))

        if param_type == "dynamic":
            m = re.match(r'^(.+?)(\d+)$', name)
            if m:
                proto_name = m.group(1)
                idx = int(m.group(2))
                if proto_name not in dynamic_groups:
                    dynamic_groups[proto_name] = []
                dynamic_groups[proto_name].append((idx, input_data))
        else:
            regular_inputs.append(input_data)

    # Build input_list preserving order
    input_list = []
    seen_dynamic = set()
    regular_idx = 0
    for input_desc in case.get("input_desc"):
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
                    input_list.append([data for _, data in group])
        else:
            if regular_idx < len(regular_inputs):
                input_list.append(regular_inputs[regular_idx])
                regular_idx += 1

    for attr in case.get("attr_desc"):
        attr_list.append(attr.get("value"))

    for desc in output_desc_list:
        if desc.get("shape_depend") is not None:
            shape_depend = desc.get("shape_depend")
            expect_func_path = shape_depend.split(":")[0]
            func_name = shape_depend.split(":")[1]
            try:
                module_name = "custom_module"
                spec = importlib.util.spec_from_file_location(module_name, expect_func_path)
                custom_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(custom_module)
                custom_func = getattr(custom_module, func_name)

                if len(attr_list) == 0 and len(input_list) > 0:
                    output_shape_list = custom_func(*input_list)
                elif len(attr_list) > 0 and len(input_list) == 0:
                    output_shape_list = custom_func(*attr_list)
                elif len(attr_list) > 0 and len(input_list) > 0:
                    output_shape_list = custom_func(*input_list, *attr_list)
                all_output_shape[desc.get("name")] = output_shape_list
            except Exception as e:
                print(f"compute shape fail, {case.get('case_name')} use default shape, error info :", e)
                return None
    return all_output_shape



if __name__ == "__main__":
    current_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # check ir and case 
    if not args.ir_json or not args.case_json:
        parser.print_help()
        exit(1)
    # check ir or case is exist
    if not os.path.exists(args.ir_json) or not os.path.exists(args.case_json):
        parser.print_help()
        exit(1)
    
    new_aclnn_gen_version = get_setup_cfg_version(os.path.join(current_dir_path, "aclnn-gen/setup.cfg"))
    aclnn_gen_version = get_aclnn_gen_version()

    if shutil.which("aclnngen") is None or (aclnn_gen_version != new_aclnn_gen_version):
        # build and install aclnngen
        os.system("cd {} && pip install -r requirements.txt && python -m build && pip uninstall aclnn-gen -y && pip install dist/*.whl --force-reinstall".format(os.path.join(current_dir_path, "aclnn-gen")))

    if not os.path.exists(args.aclnn_dir) or args.build or not os.path.exists(args.aclnn_dir+"/build/"+get_exe_name()):
         # gen aclnn project and build exe
        ir_json_path = os.path.abspath(args.ir_json)
        case_json_path = os.path.abspath(args.case_json)
        op_path_abs = os.path.abspath(args.op_path)

        aclnngen_cmd = f"aclnngen {ir_json_path} {case_json_path} -o {args.aclnn_dir} --op-path {op_path_abs} --op-type {args.op_type}"
        print(f"Executing: {aclnngen_cmd}")
        os.system(aclnngen_cmd)
        
        # build aclnn project
        os.system("cd {} && ./build_aclnn.sh".format(args.aclnn_dir))

    ir_input_desc_list = None
    ir_output_desc_list = None
    with open(args.ir_json, "r") as f:
        ir_list = json.load(f)
        for ir in ir_list:
            ir_input_desc_list = ir.get("input_desc")
            ir_output_desc_list = ir.get("output_desc")

    if args.case_name:
        with open(args.case_json, "r") as f:
            case_json = json.load(f)
            for case in case_json:
                if args.case_name == case.get("case_name"):
                    #添加输入输出顺序校验
                    input_desc_list = case.get("input_desc")
                    output_desc_list = case.get("output_desc")
                    input_check_result = check_order(input_desc_list, ir_input_desc_list)
                    output_check_resutl =  check_order(output_desc_list, ir_output_desc_list)
                    if input_check_result and output_check_resutl:
                        # just test one case
                        kernel_name = args.kernel_name
                        if kernel_name is None:
                            kernel_name = case.get("op_name")
                        run_test(current_timestamp, kernel_name, case)
                    else:
                        print("case {} input or output desc check failed".format(args.case_name))

    else:
        # get case name
        with open(args.case_json, "r") as f:
            case_json = json.load(f)
            for case in case_json:
                #添加输入输出顺序校验
                args.case_name = case.get("case_name")
                input_desc_list = case.get("input_desc")
                output_desc_list = case.get("output_desc")
                input_check_result = check_order(input_desc_list, ir_input_desc_list)
                output_check_resutl =  check_order(output_desc_list, ir_output_desc_list)
                if input_check_result and output_check_resutl:
                    # just test one case
                    kernel_name = args.kernel_name
                    if kernel_name is None:
                        kernel_name = case.get("op_name")
                    run_test(current_timestamp, kernel_name, case)
                else:
                    print("case {} input or output desc check failed".format(args.case_name))
    
  
