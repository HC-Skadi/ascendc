class InputDesc:
    def __init__(self, name, format, data_type, param_type, shape, data_path, value_range):
        self.name = name
        self.format = format
        self.data_type = data_type
        self.param_type = param_type
        self.shape = shape
        self.data_path = data_path
        self.value_range = value_range