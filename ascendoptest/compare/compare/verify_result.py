import os
from compare.compare import compare
from output_parse.output_parse import parse_output_desc_list
from output_parse.output_parse import output_list

def write_result(result, case_name, output_desc, result_path, case_path, op_name, timestamp):
    if not os.path.exists(result_path):
        return
    compare_result = "pass"
    if result == False:
        compare_result = "fail"
    with open(result_path, "a+") as f:
        f.write(case_name+", "+output_desc.name+", "+output_desc.data_path+", "+output_desc.golden_path+","+ compare_result +"\n")
        f.close()
def verify_output_list(output_desc_list, case_name, result_path, case_path, op_name, timestamp , show_err_num=10):
    parse_output_desc_list(output_desc_list,case_name, case_path, op_name, timestamp)
    for output_desc in output_list:
        result = compare(output_desc, case_name, show_err_num)
        result_color_num = "31" 
        if result == True:
            result_color_num = "32"
        write_result(result, case_name, output_desc, result_path, case_path, op_name, timestamp)
        print("\033[{}m*\033[0m".format(result_color_num)*60)
        print("\033[{}m*\033[0m".format(result_color_num)*60)
        print(f"run case {case_name} result:\n")
        cmd = "echo \033[{}m$(grep -m 1 '' {})\033[0m ".format(result_color_num, result_path)
        # print(cmd)
        os.system(cmd)
        cmd = "echo \033[{}m$(grep -r {} {})\033[0m ".format(result_color_num, case_name, result_path)
        # print(cmd)
        os.system(cmd)
        print("\033[{}m*\033[0m".format(result_color_num)*60)
        print("\033[{}m*\033[0m".format(result_color_num)*60)
    output_list.clear()