class OutputDesc:
    def __init__(self, name, format, data_type, param_type, shape, data_path, golden_path, err_threshold):
        self.name = name
        self.format = format
        self.data_type = data_type
        self.param_type = param_type
        self.shape = shape
        self.data_path = data_path
        self.golden_path = golden_path
        self.err_threshold = err_threshold