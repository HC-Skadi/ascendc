# aclnn_gen/config/mappings.py

# ==============================================================================
# 1. MAPPING FOR TENSOR DATA TYPES
# Maps JSON type strings (including aliases) to ACL and C++ types.
# ==============================================================================

# Mapping from JSON Type String to aclDataType Enum
JSON_TO_ACL_DTYPE = {
    # --- Standard Floating-Point Types ---
    "float32": "aclDataType::ACL_FLOAT",
    "fp32": "aclDataType::ACL_FLOAT",       # Alias
    "float": "aclDataType::ACL_FLOAT",        # Alias
    "float16": "aclDataType::ACL_FLOAT16",
    "fp16": "aclDataType::ACL_FLOAT16",      # Alias
    "half": "aclDataType::ACL_FLOAT16",       # Alias
    "double": "aclDataType::ACL_DOUBLE",
    "bf16": "aclDataType::ACL_BF16",
    "bfloat16": "aclDataType::ACL_BF16", # Alias

    # --- Standard Integer Types ---
    "int8": "aclDataType::ACL_INT8",
    "int16": "aclDataType::ACL_INT16",
    "int32": "aclDataType::ACL_INT32",
    "int64": "aclDataType::ACL_INT64",
    "uint8": "aclDataType::ACL_UINT8",
    "uint16": "aclDataType::ACL_UINT16",
    "uint32": "aclDataType::ACL_UINT32",
    "uint64": "aclDataType::ACL_UINT64",

    # --- Quantized Types ---
    "qint8": "aclDataType::ACL_QINT8",
    "qint16": "aclDataType::ACL_QINT16",
    "qint32": "aclDataType::ACL_QINT32",
    "quint8": "aclDataType::ACL_QUINT8",
    "quint16": "aclDataType::ACL_QUINT16",
    "quint32": "aclDataType::ACL_QUINT32",

    # --- Other Types ---
    "bool": "aclDataType::ACL_BOOL",
    "complex64": "aclDataType::ACL_COMPLEX64",
    "complex128": "aclDataType::ACL_COMPLEX128",
    "string": "aclDataType::ACL_STRING", # For string tensors, not attributes
}

# Mapping from JSON Type String to C++ Type (for std::vector<T>)
JSON_TO_CPP_TYPE = {
    # --- Standard Floating-Point Types ---
    "float32": "float",
    "fp32": "float",
    "float": "float",
    "float16": "aclFloat16",
    "fp16": "aclFloat16",
    "half": "aclFloat16",
    "double": "double",
    "bf16": "int16_t",
    "bfloat16": "int16_t",

    # --- Standard Integer Types ---
    "int8": "int8_t",
    "int16": "int16_t",
    "int32": "int32_t",
    "int64": "int64_t",
    "uint8": "uint8_t",
    "uint16": "uint16_t",
    "uint32": "uint32_t",
    "uint64": "uint64_t",

    # --- Quantized Types (Stored as base integer types on host) ---
    "qint8": "int8_t",
    "qint16": "int16_t",
    "qint32": "int32_t",
    "quint8": "uint8_t",
    "quint16": "uint16_t",
    "quint32": "uint32_t",

    # --- Other Types ---
    "bool": "uint8_t",
    "complex64": "std::complex<float>",
    "complex128": "std::complex<double>",
    "string": "std::string", # For host-side representation of string tensors
}

# ==============================================================================
#  Mapping from JSON Type String to C++ Type (for sizeof(T))
#  This should represent the raw storage type for accurate memory calculation.
# ==============================================================================
JSON_TO_SIZEOF_TYPE = {
    # --- Standard Floating-Point Types ---
    "float32": "float", "fp32": "float", "float": "float",
    "float16": "uint16_t", "fp16": "uint16_t", "half": "uint16_t",
    "double": "double",
    "bf16": "uint16_t", "bfloat16": "uint16_t", # Stored as 2 bytes

    # --- Standard Integer Types ---
    "int8": "int8_t",
    "int16": "int16_t",
    "int32": "int32_t",
    "int64": "int64_t",
    "uint8": "uint8_t",
    "uint16": "uint16_t",
    "uint32": "uint32_t",
    "uint64": "uint64_t",

    # --- Quantized Types ---
    "qint8": "int8_t",
    "qint16": "int16_t",
    "qint32": "int32_t",
    "quint8": "uint8_t",
    "quint16": "uint16_t",
    "quint32": "uint32_t",

    # --- Other Types ---
    "bool": "uint8_t",
    "complex64": "std::complex<float>",
    "complex128": "std::complex<double>",
}


# ==============================================================================
# 2. MAPPING FOR OPERATOR ATTRIBUTES
# ==============================================================================
JSON_ATTR_TO_CPP_TYPE = {
    "string": "std::string",
    "int": "int64_t",
    "float": "float",
    "bool": "bool",
    "type": "aclDataType", # An attribute can also be a type

    # Scalar types (host-side representation is the same as simple types)
    "scalar_int": "int64_t",
    "scalar_float": "float",
    "scalar_bool": "bool",
    
    # List types
    "list_int": "std::vector<int64_t>",
    "list_float": "std::vector<float>",
    "list_bool": "std::vector<bool>",
    "list_string": "std::vector<std::string>",
}

# ==============================================================================
# 3. MAPPING FOR ACL OBJECT CREATION/DESTRUCTION
# Centralizes logic for converting host C++ types to ACL C-style objects.
# ==============================================================================

# --- Mappings for aclScalar ---
# Maps scalar JSON type to the required aclDataType for aclCreateScalar
SCALAR_ATTR_TO_ACL_DTYPE = {
    'scalar_int': 'aclDataType::ACL_INT64',
    'scalar_float': 'aclDataType::ACL_FLOAT',
    'scalar_bool': 'aclDataType::ACL_BOOL',
}

# --- Mappings for acl...Array ---
# Defines the C++ type of the corresponding ACL array pointer
LIST_ATTR_TO_ACL_ARRAY_TYPE = {
    'list_int': 'aclIntArray*',
    'list_float': 'aclFloatArray*',
    'list_bool': 'aclBoolArray*',
}

# Defines the ACL function used to create the array
LIST_ATTR_TO_ACL_CREATE_FUNC = {
    'list_int': 'aclCreateIntArray',
    'list_float': 'aclCreateFloatArray',
    'list_bool': 'aclCreateBoolArray',
}
# Defines the ACL function used to destroy the array
LIST_ATTR_TO_ACL_DESTROY_FUNC = {
    'list_int': 'aclDestroyIntArray',
    'list_float': 'aclDestroyFloatArray',
    'list_bool': 'aclDestroyBoolArray',
}

# ==============================================================================
# 4. MAPPING FOR COLLECTION DATA TYPES
# This allows expanding a collection name like "numbertype" into a list of
# concrete types. This logic is no longer used by the main generator but kept
# for potential future use or for other tools that might use this config.
# If you are sure it won't be needed, this section can also be removed.
# ==============================================================================
_DT_TO_JSON_TYPE = {
    "DT_FLOAT": "float32",
    "DT_FLOAT16": "float16",
    "DT_HALF": "float16", # Alias for float16
    "DT_Bfp16": "bf16",
    "DT_DOUBLE": "double",
    "DT_INT8": "int8",
    "DT_INT16": "int16",
    "DT_INT32": "int32",
    "DT_INT64": "int64",
    "DT_UINT8": "uint8",
    "DT_UINT16": "uint16",
    "DT_UINT32": "uint32",
    "DT_UINT64": "uint64",
    "DT_QINT8": "qint8",
    "DT_QINT16": "qint16",
    "DT_QINT32": "qint32",
    "DT_QUINT8": "quint8",
    "DT_QUINT16": "quint16",
    "DT_BOOL": "bool",
    "DT_COMPLEX64": "complex64",
    "DT_COMPLEX128": "complex128",
    "DT_STRING": "string",
}

def _parse_collection_string(dt_string: str) -> list:
    """Helper to parse a 'DT_FLOAT, DT_INT8, ...' string into a list of json types."""
    dt_types = [dt.strip() for dt in dt_string.split(',')]
    json_types = [_DT_TO_JSON_TYPE.get(dt) for dt in dt_types if dt in _DT_TO_JSON_TYPE]
    # Remove duplicates while preserving order
    unique_json_types = sorted(list(set(json_types)), key=json_types.index)
    return unique_json_types

# This logic is currently not used by the primary aclnngen workflow but kept for reference
COLLECTION_TYPE_EXPANSION = {
    "numbertype": _parse_collection_string("DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT8, DT_INT16, DT_INT32,DT_INT64, DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_QINT8,DT_QUINT8, DT_COMPLEX64, DT_COMPLEX128, DT_QINT32"),
    "realnumbertype": _parse_collection_string("DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64"),
    "quantizedtype": _parse_collection_string("DT_QINT8, DT_QUINT8, DT_QINT16, DT_QUINT16, DT_QINT32"),
    "BasicType": _parse_collection_string("DT_FLOAT, DT_DOUBLE, DT_INT32, DT_UINT8, DT_INT16, DT_INT8, DT_COMPLEX64, DT_INT64, DT_QINT8, DT_QUINT8, DT_QINT32, DT_QINT16, DT_QUINT16, DT_UINT16, DT_COMPLEX128, DT_FLOAT16, DT_UINT32, DT_UINT64"),
    "IndexNumberType": _parse_collection_string("DT_INT32, DT_INT64"),
}