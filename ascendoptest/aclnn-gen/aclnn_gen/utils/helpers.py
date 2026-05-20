# aclnn_gen/utils/helpers.py
import re

def camel_to_snake(name: str) -> str:
    """
    Converts a CamelCase string to snake_case, handling various formats.
    
    Examples:
        "TriuCustom" -> "triu_custom"
        "Add"        -> "add"
        "RMSNorm"    -> "rms_norm"
        "MyOpV2"     -> "my_op_v2"
    """
    # 1. 在小写字母或数字与大写字母之间插入下划线。
    #    e.g., "MyOpV2" -> "My_Op_V2", "TriuCustom" -> "Triu_Custom"
    s1 = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name)
    
    # 2. 在大写字母与大写字母+小写字母之间插入下划线。
    #    e.g., "RMSNorm" -> "RMS_Norm"
    s2 = re.sub(r'([A-Z])([A-Z][a-z])', r'\1_\2', s1)
    
    # 3. 将整个字符串转换为小写。
    return s2.lower()