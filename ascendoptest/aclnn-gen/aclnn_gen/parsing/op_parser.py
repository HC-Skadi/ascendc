# aclnn_gen/parsing/op_parser.py
import json
from aclnn_gen.utils.helpers import camel_to_snake

class OperatorDefinition:
    """A structured container for operator information parsed from JSON."""
    def __init__(self, json_data: list):
        if not isinstance(json_data, list) or not json_data:
            raise ValueError("Invalid JSON format: expected a non-empty list.")

        op_info = json_data[0]

        self.op_name = op_info['op']
        self.op_name_snake = camel_to_snake(self.op_name)
        self.aclnn_func_name = f"aclnn{self.op_name}"

        self.inputs = op_info.get('input_desc', [])
        self.outputs = op_info.get('output_desc', [])
        self.attrs = op_info.get('attr', [])

        # Identify dynamic (ListTensor) inputs and outputs
        self.dynamic_inputs = [inp['name'] for inp in self.inputs if inp.get('param_type') == 'dynamic']
        self.dynamic_outputs = [out['name'] for out in self.outputs if out.get('param_type') == 'dynamic']

        # Pre-calculate names for convenience (exclude dynamic — their count is case-dependent)
        non_dynamic_inputs = [inp for inp in self.inputs if inp.get('param_type') != 'dynamic']
        non_dynamic_outputs = [out for out in self.outputs if out.get('param_type') != 'dynamic']
        self.tensor_names = [f"input{inp['name'].capitalize()}" for inp in non_dynamic_inputs] + \
                            [f"output{out['name'].capitalize()}" for out in non_dynamic_outputs]
        self.device_addr_names = [f"{name}DeviceAddr" for name in self.tensor_names]

    @classmethod
    def from_file(cls, filepath: str):
        """Creates an instance by reading a JSON file."""
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            return cls(data)
        except (json.JSONDecodeError, IOError) as e:
            raise RuntimeError(f"Failed to read or parse JSON file '{filepath}': {e}") from e