class CaseDesc:
    def __init__(self, case_name, op_name, case_path, expect_func, input_desc_list, output_desc_list, attr_list):
        self.case_name = case_name
        self.op_name = op_name
        self.case_path = case_path
        self.expect_func = expect_func
        self.input_desc_list = input_desc_list
        self.output_desc_list = output_desc_list
        self.attr_list = attr_list