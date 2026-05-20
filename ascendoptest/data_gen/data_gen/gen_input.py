import sys
import os
from data_gen.data_generation import generate_data
from data_gen.data_generation import generate_data_tensor_list

from input_parse.input_parse import input_list
from input_parse.input_parse import parse_input_desc_list

def gen_input(input_desc_list, ir_input_desc_list, case_name, case_path, timestamp, op_name, result_path):
    parse_input_desc_list(input_desc_list, ir_input_desc_list, case_name,case_path, timestamp, op_name)
    for input_desc in input_list:
        if input_desc.param_type in ("required", "optional", "dynamic"):
            abspath =generate_data(input_desc)
            os.system("echo '{}, {}, {},,' >> {}".format(case_name, input_desc.name,abspath,result_path))
        else:
            abspath = generate_data_tensor_list(input_desc)
            os.system("echo '{}, {}, {},,' >> {}".format(case_name, input_desc.name,abspath,result_path))
    input_list.clear()