# aclnn_gen/parsing/case_parser.py
import json
import os
import re
from aclnn_gen.parsing.op_parser import OperatorDefinition
from aclnn_gen.config import mappings

class CaseParser:
    """
    Parses a test case JSON file, processes each case by resolving paths,
    handling default values, and pre-formatting values for code generation.
    """
    def __init__(self, raw_cases: list, op_def: OperatorDefinition):
        self.raw_cases = raw_cases
        self.op_def = op_def
        self.processed_cases = self._process_all()

    @classmethod
    def from_file(cls, case_filepath: str, op_def: OperatorDefinition):
        try:
            with open(case_filepath, 'r') as f:
                raw_cases = json.load(f)
            parser_instance = cls(raw_cases, op_def)
            return parser_instance.processed_cases
        except (json.JSONDecodeError, IOError) as e:
            raise RuntimeError(f"Failed to read or parse case file '{case_filepath}': {e}") from e

    def _process_all(self) -> list:
        return [self._process_single_case(case) for case in self.raw_cases]

    @staticmethod
    def _group_dynamic_entries(desc_list, dynamic_names, desc_key="input_desc"):
        """
        Groups numbered entries (e.g. x0, x1, x2) belonging to dynamic proto names (e.g. x).
        Returns (remaining_descs, dynamic_groups) where:
        - remaining_descs: entries that are NOT part of any dynamic group
        - dynamic_groups: dict mapping proto_name -> {proto_name, tensors: [...], count: N}
        """
        if not dynamic_names:
            return desc_list, {}

        dynamic_groups = {}
        remaining = []
        grouped_indices = set()

        for dyn_name in dynamic_names:
            pattern = re.compile(r'^' + re.escape(dyn_name) + r'(\d+)$')
            group_tensors = []
            for i, desc in enumerate(desc_list):
                m = pattern.match(desc.get('name', ''))
                if m:
                    idx = int(m.group(1))
                    group_tensors.append((idx, desc))
                    grouped_indices.add(i)
            # Sort by index
            group_tensors.sort(key=lambda t: t[0])
            if group_tensors:
                dynamic_groups[dyn_name] = {
                    "proto_name": dyn_name,
                    "tensors": [t[1] for t in group_tensors],
                    "count": len(group_tensors)
                }

        for i, desc in enumerate(desc_list):
            if i not in grouped_indices:
                remaining.append(desc)

        return remaining, dynamic_groups

    def _process_single_case(self, raw_case: dict) -> dict:
        # 1. Determine the base path for this case
        if raw_case.get("case_path"):
            base_path = os.path.abspath(raw_case["case_path"])
        else:
            base_path = os.getcwd()
        raw_case['resolved_base_path'] = base_path

        # 2. Process paths for all inputs and outputs
        for inp in raw_case.get("input_desc", []):
            self._resolve_path(inp, path_key="data_path")
        for outp in raw_case.get("output_desc", []):
            self._resolve_path(outp, path_key="data_path")
            self._resolve_path(outp, path_key="golden_path")

        # 3. Group dynamic inputs and outputs
        remaining_inputs, dynamic_input_groups = self._group_dynamic_entries(
            raw_case.get('input_desc', []),
            self.op_def.dynamic_inputs,
            desc_key="input_desc"
        )
        remaining_outputs, dynamic_output_groups = self._group_dynamic_entries(
            raw_case.get('output_desc', []),
            self.op_def.dynamic_outputs,
            desc_key="output_desc"
        )
        raw_case['input_desc'] = remaining_inputs
        raw_case['dynamic_input_groups'] = dynamic_input_groups
        raw_case['output_desc'] = remaining_outputs
        raw_case['dynamic_output_groups'] = dynamic_output_groups

        # 4. Process attributes and pre-format their values
        proto_attrs_map = {p['name']: p for p in self.op_def.attrs}
        case_attrs_map = {c['name']: c for c in raw_case.get('attr_desc', [])}

        processed_attrs = []
        for name, proto_attr in proto_attrs_map.items():
            value = case_attrs_map.get(name, {}).get('value', proto_attr.get('default_value'))
            attr_type_lower = proto_attr['type'].lower()

            value_str = ""
            if attr_type_lower.startswith("list_"):
                if not value:
                    value_str = "{}"
                else:
                    value_str = str(value).replace('[', '{').replace(']', '}')
            elif attr_type_lower == 'string':
                value_str = f'"{value}"'
            elif attr_type_lower == 'bool':
                value_str = str(value).lower()
            else:
                value_str = str(value)

            processed_attrs.append({
                "name": name,
                "type": attr_type_lower,
                "cpp_type": mappings.JSON_ATTR_TO_CPP_TYPE.get(attr_type_lower, "/*_unknown_attr_type_*/"),
                "value_str": value_str
            })

        raw_case['attr_desc'] = processed_attrs
        return raw_case

    def _resolve_path(self, tensor_desc: dict, path_key: str = "data_path"):
        user_path = tensor_desc.get(path_key)
        if not user_path:
            filename = f"golden_{tensor_desc['name']}.bin" if path_key == "golden_path" else f"{tensor_desc['name']}.bin"
            tensor_desc[path_key] = filename
            tensor_desc[f"{path_key}_is_default"] = True
        else:
            tensor_desc[f"{path_key}_is_default"] = False
