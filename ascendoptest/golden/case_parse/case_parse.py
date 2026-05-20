
from case_parse.case_desc import CaseDesc


def parse_case_desc(case_desc):
    case_name = case_desc.get("case_name")
    op_name = case_desc.get("op_name")
    expect_func = case_desc.get("expect_func")
    input_desc_list = case_desc.get("input_desc")
    output_desc_list = case_desc.get("output_desc")
    attr_list = case_desc.get("attr_desc")
    case_path = case_desc.get("case_path")
    return CaseDesc(case_name, op_name, case_path, expect_func, input_desc_list, output_desc_list,attr_list)
