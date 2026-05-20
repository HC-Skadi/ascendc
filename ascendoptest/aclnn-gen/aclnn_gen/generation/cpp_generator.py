# aclnn_gen/generation/cpp_generator.py
from aclnn_gen.parsing.op_parser import OperatorDefinition
from aclnn_gen.config import mappings
import textwrap
import os

class CppGenerator:
    """
    Generates a unified, multi-case C++ source file that supports both
    standard and inplace operators.
    """
    def __init__(self, op_def: OperatorDefinition, cases: list):
        self.op_def = op_def
        self.cases = cases
        # --- Pre-scan for required headers ---
        self.requires_complex_header = self._scan_for_complex_types()

    def _scan_for_complex_types(self) -> bool:
        """
        Scans all test cases to determine if the <complex> header is needed.
        """
        for case in self.cases:
            for desc in case.get('input_desc', []) + case.get('output_desc', []):
                if 'complex' in desc.get('data_type', '').lower():
                    return True
        return False

    def generate_code(self) -> str:
        """Generates the full C++ source code as a string."""
        case_functions = [self._generate_case_function(case) for case in self.cases]
        
        code_parts = [
            self._generate_headers(),
            self._generate_boilerplate(),
            *case_functions,
            self._generate_main_dispatcher(),
        ]
        return "\n\n".join(code_parts)
    
    # --- Methods for generating static parts of the file ---
    
    def _generate_headers(self) -> str:
        # --- Conditional include for <complex> ---
        complex_include = "#include <complex>" if self.requires_complex_header else ""
        return f"""#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <fstream>
#include <fcntl.h>
#include <cstring>
#include <map>
#include <regex>
{complex_include}

#include "acl/acl.h"
#include "aclnn_{self.op_def.op_name_snake}.h"

#define SUCCESS 0
#define FAILED 1

#define INFO_LOG(fmt, args...) fprintf(stdout, "[INFO]  " fmt "\\n", ##args)
#define WARN_LOG(fmt, args...) fprintf(stdout, "[WARN]  " fmt "\\n", ##args)
#define ERROR_LOG(fmt, args...) fprintf(stderr, "[ERROR]  " fmt "\\n", ##args)

#define CHECK_RET(cond, return_expr) \\
    do {{                             \\
        if (!(cond)) {{               \\
            return_expr;             \\
        }}                            \\
    }} while (0)

#define LOG_PRINT(message, ...)         \\
    do {{                                \\
        printf(message, ##__VA_ARGS__); \\
    }} while (0)
"""

    def _generate_boilerplate(self) -> str:
        return r'''
// --- Utility functions for file I/O and tensor creation ---

bool ReadFile(const std::string &filePath, size_t &fileSize, void *buffer, size_t bufferSize)
{
    std::ifstream file(filePath, std::ios::binary | std::ios::ate);
    if (!file.is_open()) {
        ERROR_LOG("Failed to open file: %s", filePath.c_str());
        return false;
    }

    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);
    
    fileSize = static_cast<size_t>(size);

    if (fileSize > bufferSize) {
        ERROR_LOG("File size (%zu) is larger than buffer size (%zu). If the use case file has been modified, please add '--build' in your command", fileSize, bufferSize);
        file.close();
        return false;
    }

    if (!file.read(static_cast<char *>(buffer), size)) {
        ERROR_LOG("Failed to read the entire file: %s", filePath.c_str());
        file.close();
        return false;
    }

    file.close();
    return true;
}


bool WriteFile(const std::string &filePath, const void *buffer, size_t size)
{
    if (buffer == nullptr) {
        ERROR_LOG("Write file failed, buffer is nullptr.");
        return false;
    }

    size_t lastSlash = filePath.find_last_of('/');
    if (lastSlash != std::string::npos) {
        std::string dirPath = filePath.substr(0, lastSlash);
        std::string cmd = "mkdir -p " + dirPath;
        int ret = system(cmd.c_str());
        if (ret != 0) {
            ERROR_LOG("Failed to create directory: %s", dirPath.c_str());
            return false;
        }
    }

    int fd = open(filePath.c_str(), O_RDWR | O_CREAT | O_TRUNC, S_IRUSR | S_IWRITE);
    if (fd < 0) {
        ERROR_LOG("Failed to open file: %s", filePath.c_str());
        return false;
    }

    const char *data = static_cast<const char *>(buffer);
    size_t bytesWritten = 0;
    const size_t chunkSize = 1024 * 1024 * 1024; // 1GB chunk size

    while (bytesWritten < size) {
        size_t bytesToWrite = std::min(chunkSize, size - bytesWritten);
        ssize_t writeResult = write(fd, data + bytesWritten, bytesToWrite);

        if (writeResult < 0) {
            ERROR_LOG("Write file failed with error.");
            close(fd);
            return false;
        }
        
        bytesWritten += static_cast<size_t>(writeResult);

        if (static_cast<size_t>(writeResult) != bytesToWrite) {
            ERROR_LOG("Partial write occurred. Wrote %zu of %zu bytes.", static_cast<size_t>(writeResult), bytesToWrite);
            break;
        }
    }

    close(fd);

    if (bytesWritten != size) {
        ERROR_LOG("Write file size mismatch. Expected %zu, but wrote %zu.", size, bytesWritten);
        return false;
    }

    return true;
}

int64_t GetShapeSize(const std::vector<int64_t> &shape)
{
    int64_t size = 1;
    for (auto dim : shape) {
        size *= dim;
    }
    return size;
}

int Init(int32_t deviceId, aclrtStream *stream)
{
    auto ret = aclInit(nullptr);
    CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclInit failed. ERROR: %d\n", ret); return FAILED);
    ret = aclrtSetDevice(deviceId);
    CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclrtSetDevice failed. ERROR: %d\n", ret); return FAILED);
    ret = aclrtCreateStream(stream);
    CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclrtCreateStream failed. ERROR: %d\n", ret); return FAILED);
    return SUCCESS;
}

template <typename T>
int CreateInputTensor(const std::vector<T> &hostData, const std::vector<int64_t> &shape, void **deviceAddr, aclDataType dataType, aclTensor **tensor)
{
    auto size = GetShapeSize(shape) * sizeof(T);
    auto ret = aclrtMalloc(deviceAddr, size, ACL_MEM_MALLOC_HUGE_FIRST);
    CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclrtMalloc failed. ERROR: %d\n", ret); return FAILED);
    
    ret = aclrtMemcpy(*deviceAddr, size, hostData.data(), size, ACL_MEMCPY_HOST_TO_DEVICE);
    CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclrtMemcpy failed. ERROR: %d\n", ret); return FAILED);
    
    *tensor = aclCreateTensor(shape.data(), shape.size(), dataType, nullptr, 0, ACL_FORMAT_ND, shape.data(), shape.size(), *deviceAddr);
    CHECK_RET(*tensor != nullptr, LOG_PRINT("aclCreateTensor failed.\n"); return FAILED);
    return SUCCESS;
}

int CreateOutputTensor(const std::vector<int64_t> &shape, size_t type_size, void **deviceAddr, aclDataType dataType, aclTensor **tensor)
{
    auto size = GetShapeSize(shape) * type_size;
    auto ret = aclrtMalloc(deviceAddr, size, ACL_MEM_MALLOC_HUGE_FIRST);
    CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclrtMalloc failed. ERROR: %d\n", ret); return FAILED);
    
    *tensor = aclCreateTensor(shape.data(), shape.size(), dataType, nullptr, 0, ACL_FORMAT_ND, shape.data(), shape.size(), *deviceAddr);
    CHECK_RET(*tensor != nullptr, LOG_PRINT("aclCreateTensor failed.\n"); return FAILED);
    return SUCCESS;
}

// --- Helper: Parse Python-style shape dict string: {'name': [(d1, d2)], ...} ---
std::map<std::string, std::vector<int64_t>> ParseOutputShapesStr(const std::string& input) {
    std::map<std::string, std::vector<int64_t>> shapeMap;
    if (input.empty()) return shapeMap;

    // Regex to match: 'name': [(dim1, dim2, ...)]
    std::regex re(R"('(\w+)':\s*\[\(([\d,\s]+)\)\])");
    std::sregex_iterator next(input.begin(), input.end(), re);
    std::sregex_iterator end;

    while (next != end) {
        std::smatch match = *next;
        std::string name = match[1].str();
        std::string dims_str = match[2].str();

        std::vector<int64_t> dims;
        std::regex num_re(R"(\d+)");
        std::sregex_iterator num_next(dims_str.begin(), dims_str.end(), num_re);
        std::sregex_iterator num_end;

        while (num_next != num_end) {
            dims.push_back(std::stoll(num_next->str()));
            num_next++;
        }
        shapeMap[name] = dims;
        next++;
    }
    return shapeMap;
}
'''
    
    def _generate_case_function(self, case: dict) -> str:
        """Generates a complete, self-contained C++ function for a single test case."""
        case_name = case['case_name']
        function_body = self._generate_case_body(case)
        
        indented_body = textwrap.indent(function_body, "    ")
        
        return f"int run_case_{case_name}(const std::string& timestamp, const std::map<std::string, std::vector<int64_t>>& outputShapes)\n{{\n{indented_body}\n}}"

    def _generate_case_body(self, case: dict) -> str:
        lines = ["auto ret = 0;"]
        
        # --- Input Classification ---
        case_tensor_inputs = [inp for inp in case.get('input_desc', []) if inp.get('shape')]
        case_scalar_inputs = [inp for inp in case.get('input_desc', []) if not inp.get('shape')]
        # Quick Lookup Maps
        proto_inputs_map = {p['name']: p for p in self.op_def.inputs}
        case_tensor_inputs_map = {c['name']: c for c in case_tensor_inputs}
        case_scalar_inputs_map = {c['name']: c for c in case_scalar_inputs}

        dynamic_input_groups = case.get('dynamic_input_groups', {})
        dynamic_output_groups = case.get('dynamic_output_groups', {})

        # Inplace Detection
        proto_input_names = set(proto_inputs_map.keys())
        proto_output_names = {p['name'] for p in self.op_def.outputs}
        dynamic_proto_names = set(self.op_def.dynamic_inputs) | set(self.op_def.dynamic_outputs)
        inplace_tensor_names = proto_input_names.intersection(proto_output_names)
        all_unique_tensor_names = (proto_input_names.union(proto_output_names)) - dynamic_proto_names
        is_fully_inplace = proto_output_names and (proto_output_names == proto_input_names)
        
        # --- 0. Initialization ---
        lines.append("\n// 0. INITIALIZATION")
        lines.append("int32_t deviceId = 0;")
        lines.append("aclrtStream stream;")
        lines.append("ret = Init(deviceId, &stream);")
        lines.append("CHECK_RET(ret == SUCCESS, return FAILED);")

        # --- 1. Declarations ---
        lines.append("\n// 1. DECLARATIONS")
        processed_attrs = case.get('attr_desc', [])
        if processed_attrs: lines.append("// Attributes")
        for attr in processed_attrs:
            lines.append(f"{attr['cpp_type']} {attr['name']} = {attr['value_str']};")
            attr_type = attr['type']
            if attr_type in mappings.SCALAR_ATTR_TO_ACL_DTYPE:
                lines.append(f"aclScalar* {attr['name']}Scalar = nullptr;")
            elif attr_type in mappings.LIST_ATTR_TO_ACL_ARRAY_TYPE:
                acl_array_type = mappings.LIST_ATTR_TO_ACL_ARRAY_TYPE[attr_type]
                lines.append(f"{acl_array_type} {attr['name']}Acl = nullptr;")
        
        lines.append("\n// Scalar Inputs")
        for s_inp in case_scalar_inputs:
            json_type = s_inp['data_type'].lower()
            cpp_type = mappings.JSON_TO_CPP_TYPE.get(json_type, "/*_err_*/")
            lines.append(f"{cpp_type} {s_inp['name']}Host; // Host variable for scalar input")
            lines.append(f"aclScalar* {s_inp['name']}Scalar = nullptr;")

        lines.append("\n// Tensor Pointers")
        for name in sorted(list(all_unique_tensor_names)):
            lines.append(f"void* {name}DeviceAddr = nullptr;")
            lines.append(f"aclTensor* {name}Tensor = nullptr;")
        lines.append("void* workspaceAddr = nullptr;")
        lines.append("uint64_t workspaceSize = 0;")

        if dynamic_input_groups or dynamic_output_groups:
            lines.append("\n// Dynamic (ListTensor) Pointers")
        for proto_name, group in dynamic_input_groups.items():
            for tensor_desc in group['tensors']:
                tname = tensor_desc['name']
                lines.append(f"void* {tname}DeviceAddr = nullptr;")
                lines.append(f"aclTensor* {tname}Tensor = nullptr;")
            lines.append(f"aclTensorList* {proto_name}TensorList = nullptr;")
        for proto_name, group in dynamic_output_groups.items():
            for tensor_desc in group['tensors']:
                tname = tensor_desc['name']
                lines.append(f"void* {tname}DeviceAddr = nullptr;")
                lines.append(f"aclTensor* {tname}Tensor = nullptr;")
            lines.append(f"aclTensorList* {proto_name}TensorList = nullptr;")

        # --- 2. PREPARATION & EXECUTION ---
        lines.append("\n// 2. PREPARATION & EXECUTION")
        lines.append(f"// Construct the default data path for this run using the timestamp")
        lines.append(f"std::string casePath = \"{case['resolved_base_path']}\";")
        lines.append(f"std::string defaultDataDir = casePath + \"/op_test/{case['op_name'].lower()}_{case['case_name'].lower()}_\" + timestamp;")
        
        lines.append("\n// Prepare ACL Objects from Attributes")
        for attr in processed_attrs:
            name = attr['name']
            attr_type = attr['type']
            if attr_type in mappings.SCALAR_ATTR_TO_ACL_DTYPE:
                acl_dtype = mappings.SCALAR_ATTR_TO_ACL_DTYPE[attr_type]
                lines.append(f"{name}Scalar = aclCreateScalar(&{name}, {acl_dtype});")
            elif attr_type in mappings.LIST_ATTR_TO_ACL_ARRAY_TYPE:
                create_func = mappings.LIST_ATTR_TO_ACL_CREATE_FUNC[attr_type]
                if attr_type == 'list_bool':
                    lines.append(f"{{ // Convert std::vector<bool> to a contiguous array for aclCreateBoolArray")
                    lines.append(f"    std::vector<uint8_t> {name}AsByte({name}.size());")
                    lines.append(f"    for(size_t i = 0; i < {name}.size(); ++i) {{ {name}AsByte[i] = static_cast<uint8_t>({name}[i]); }}")
                    lines.append(f"    {name}Acl = {create_func}(reinterpret_cast<const bool*>({name}AsByte.data()), {name}AsByte.size());")
                    lines.append(f"}}")
                else:
                    lines.append(f"{name}Acl = {create_func}({name}.data(), {name}.size());")

        lines.append("\n// Prepare Scalar Inputs")
        for s_inp in case_scalar_inputs:
            name = s_inp['name']
            json_type = s_inp['data_type'].lower()
            sizeof_type = mappings.JSON_TO_SIZEOF_TYPE.get(json_type, "/*_err_*/")
            acl_dtype = mappings.JSON_TO_ACL_DTYPE.get(json_type, "/*_err_*/")
            lines.append(f"{{ // Scope for scalar input '{name}'")
            lines.append(f"    std::string finalDataPath;")
            if s_inp.get('data_path_is_default', False):
                lines.append(f"    finalDataPath = defaultDataDir + \"/input/{s_inp['data_path']}\";")
            else:
                is_abs = os.path.isabs(s_inp['data_path'])
                lines.append(f"    finalDataPath = {'true' if is_abs else 'false'} ? \"{s_inp['data_path']}\" : casePath + \"/{s_inp['data_path']}\";")
            lines.append(f"    size_t {name}FileSize = 0;")
            lines.append(f"    ReadFile(finalDataPath, {name}FileSize, &{name}Host, sizeof({sizeof_type}));")
            lines.append(f"    {name}Scalar = aclCreateScalar(&{name}Host, {acl_dtype});")
            lines.append(f"}}")

        lines.append("\n// Prepare Tensor Inputs")
        for name, proto_input in proto_inputs_map.items():
            if name in case_tensor_inputs_map:
                conf = case_tensor_inputs_map[name]
                lines.append(f"{{ // Scope for input '{name}'")
                lines.append(f"    std::string finalDataPath;")
                if conf.get('data_path_is_default', False):
                    lines.append(f"    finalDataPath = defaultDataDir + \"/input/{conf['data_path']}\";")
                else:
                    is_abs = os.path.isabs(conf['data_path'])
                    lines.append(f"    finalDataPath = {'true' if is_abs else 'false'} ? \"{conf['data_path']}\" : casePath + \"/{conf['data_path']}\";")
                
                shape_str = str(conf['shape']).replace('[', '{').replace(']', '}')
                json_type = conf['data_type'].lower()
                cpp_type = mappings.JSON_TO_CPP_TYPE.get(json_type, "/*_err_*/")
                sizeof_type = mappings.JSON_TO_SIZEOF_TYPE.get(json_type, "/*_err_*/")
                acl_dtype = mappings.JSON_TO_ACL_DTYPE.get(json_type, "/*_err_*/")
                
                lines.append(f"    std::vector<int64_t> {name}Shape = {shape_str};")
                lines.append(f"    if (outputShapes.count(\"{name}\") > 0) {{")
                lines.append(f"        {name}Shape = outputShapes.at(\"{name}\");")
                lines.append(f"        INFO_LOG(\"Output Shape Override applied for input {name}\");")
                lines.append(f"    }}")

                lines.extend([
                    f"    size_t {name}Size = GetShapeSize({name}Shape);",
                    f"    std::vector<{cpp_type}> {name}HostData({name}Size);",
                    f"    size_t {name}FileSize = 0;",
                    f"    ReadFile(finalDataPath, {name}FileSize, {name}HostData.data(), {name}Size * sizeof({sizeof_type}));",
                    f"    ret = CreateInputTensor({name}HostData, {name}Shape, &{name}DeviceAddr, {acl_dtype}, &{name}Tensor);",
                    f"    CHECK_RET(ret == SUCCESS, return FAILED);",
                    f"}}"
                ])
            elif name in case_scalar_inputs_map:
                pass
            elif proto_input.get('param_type') == 'optional':
                lines.append(f"// Optional input '{name}' not provided, remains nullptr.")
            elif proto_input.get('param_type') == 'dynamic':
                pass  # Dynamic inputs are handled separately via dynamic_input_groups
            else:
                lines.append(f"// FATAL: Required input '{name}' not in case '{case['case_name']}'!")

        for proto_name, group in dynamic_input_groups.items():
            lines.append(f"\n// Prepare Dynamic Input ListTensor '{proto_name}'")
            for tensor_desc in group['tensors']:
                tname = tensor_desc['name']
                lines.append(f"{{ // Scope for dynamic input tensor '{tname}'")
                lines.append(f"    std::string finalDataPath;")
                if tensor_desc.get('data_path_is_default', False):
                    lines.append(f"    finalDataPath = defaultDataDir + \"/input/{tensor_desc['data_path']}\";")
                else:
                    is_abs = os.path.isabs(tensor_desc['data_path'])
                    lines.append(f"    finalDataPath = {'true' if is_abs else 'false'} ? \"{tensor_desc['data_path']}\" : casePath + \"/{tensor_desc['data_path']}\";")
                shape_str = str(tensor_desc['shape']).replace('[', '{').replace(']', '}')
                json_type = tensor_desc['data_type'].lower()
                cpp_type = mappings.JSON_TO_CPP_TYPE.get(json_type, "/*_err_*/")
                sizeof_type = mappings.JSON_TO_SIZEOF_TYPE.get(json_type, "/*_err_*/")
                acl_dtype = mappings.JSON_TO_ACL_DTYPE.get(json_type, "/*_err_*/")
                lines.append(f"    std::vector<int64_t> {tname}Shape = {shape_str};")
                lines.extend([
                    f"    size_t {tname}Size = GetShapeSize({tname}Shape);",
                    f"    std::vector<{cpp_type}> {tname}HostData({tname}Size);",
                    f"    size_t {tname}FileSize = 0;",
                    f"    ReadFile(finalDataPath, {tname}FileSize, {tname}HostData.data(), {tname}Size * sizeof({sizeof_type}));",
                    f"    ret = CreateInputTensor({tname}HostData, {tname}Shape, &{tname}DeviceAddr, {acl_dtype}, &{tname}Tensor);",
                    f"    CHECK_RET(ret == SUCCESS, return FAILED);",
                    f"}}"
                ])
            # Assemble TensorList
            tensor_names_arr = ", ".join([f"{td['name']}Tensor" for td in group['tensors']])
            count = group['count']
            lines.append(f"{{ // Create TensorList for '{proto_name}'")
            lines.append(f"    aclTensor* {proto_name}Tensors[] = {{{tensor_names_arr}}};")
            lines.append(f"    {proto_name}TensorList = aclCreateTensorList({proto_name}Tensors, {count});")
            lines.append(f"    CHECK_RET({proto_name}TensorList != nullptr, LOG_PRINT(\"aclCreateTensorList failed for {proto_name}.\\n\"); return FAILED);")
            lines.append(f"}}")

        lines.append("INFO_LOG(\"Input preparation success.\");")

        lines.append("\n// Prepare Outputs")
        for conf in case.get('output_desc', []):
            name = conf['name']
            if name in inplace_tensor_names:
                lines.append(f"// Output '{name}' is an inplace tensor, already created as input.")
                continue
            
            lines.append(f"{{ // Scope for output '{name}'")
            shape_str = str(conf['shape']).replace('[', '{').replace(']', '}')
            json_type = conf['data_type'].lower()
            sizeof_type = mappings.JSON_TO_SIZEOF_TYPE.get(json_type, "/*_err_*/")
            acl_dtype = mappings.JSON_TO_ACL_DTYPE.get(json_type, "/*_err_*/")
            
            lines.append(f"    std::vector<int64_t> {name}Shape = {shape_str};")
            lines.append(f"    if (outputShapes.count(\"{name}\") > 0) {{")
            lines.append(f"        {name}Shape = outputShapes.at(\"{name}\");")
            lines.append(f"        INFO_LOG(\"Output Shape Override applied for output {name}\");")
            lines.append(f"    }}")

            lines.extend([
                f"    ret = CreateOutputTensor({name}Shape, sizeof({sizeof_type}), &{name}DeviceAddr, {acl_dtype}, &{name}Tensor);",
                f"    CHECK_RET(ret == SUCCESS, return FAILED);",
                f"}}"
            ])

        for proto_name, group in dynamic_output_groups.items():
            lines.append(f"\n// Prepare Dynamic Output ListTensor '{proto_name}'")
            for tensor_desc in group['tensors']:
                tname = tensor_desc['name']
                lines.append(f"{{ // Scope for dynamic output tensor '{tname}'")
                shape_str = str(tensor_desc['shape']).replace('[', '{').replace(']', '}')
                json_type = tensor_desc['data_type'].lower()
                sizeof_type = mappings.JSON_TO_SIZEOF_TYPE.get(json_type, "/*_err_*/")
                acl_dtype = mappings.JSON_TO_ACL_DTYPE.get(json_type, "/*_err_*/")
                lines.append(f"    std::vector<int64_t> {tname}Shape = {shape_str};")
                lines.append(f"    if (outputShapes.count(\"{tname}\") > 0) {{")
                lines.append(f"        {tname}Shape = outputShapes.at(\"{tname}\");")
                lines.append(f"        INFO_LOG(\"Output Shape Override applied for dynamic output {tname}\");")
                lines.append(f"    }}")
                lines.extend([
                    f"    ret = CreateOutputTensor({tname}Shape, sizeof({sizeof_type}), &{tname}DeviceAddr, {acl_dtype}, &{tname}Tensor);",
                    f"    CHECK_RET(ret == SUCCESS, return FAILED);",
                    f"}}"
                ])
            tensor_names_arr = ", ".join([f"{td['name']}Tensor" for td in group['tensors']])
            count = group['count']
            lines.append(f"{{ // Create output TensorList for '{proto_name}'")
            lines.append(f"    aclTensor* {proto_name}Tensors[] = {{{tensor_names_arr}}};")
            lines.append(f"    {proto_name}TensorList = aclCreateTensorList({proto_name}Tensors, {count});")
            lines.append(f"    CHECK_RET({proto_name}TensorList != nullptr, LOG_PRINT(\"aclCreateTensorList failed for output {proto_name}.\\n\"); return FAILED);")
            lines.append(f"}}")

        lines.append("INFO_LOG(\"Output preparation success.\");")
        
        lines.append("\n// Execute Operator")
        input_args = []
        for proto_input in self.op_def.inputs:
            name = proto_input['name']
            if proto_input.get('param_type') == 'dynamic':
                input_args.append(f"{name}TensorList")
            elif name in case_scalar_inputs_map:
                input_args.append(f"{name}Scalar")
            elif name in case_tensor_inputs_map:
                input_args.append(f"{name}Tensor")
            else:
                input_args.append("nullptr")
        attr_args = []
        for attr_proto in self.op_def.attrs:
            name = attr_proto['name']
            attr_type = attr_proto['type'].lower()
            if attr_type in mappings.SCALAR_ATTR_TO_ACL_DTYPE:
                attr_args.append(f"{name}Scalar")
            elif attr_type in mappings.LIST_ATTR_TO_ACL_ARRAY_TYPE:
                attr_args.append(f"{name}Acl")
            elif attr_type == 'string':
                attr_args.append(f"const_cast<char*>({name}.c_str())")
            else:
                attr_args.append(name)
        ws_args_list = []
        if is_fully_inplace:
            lines.append("// This is a fully inplace operator, output tensors are omitted from the call.")
            ws_args_list = input_args + attr_args
        else:
            output_args = []
            for out in self.op_def.outputs:
                oname = out['name']
                if out.get('param_type') == 'dynamic':
                    output_args.append(f"{oname}TensorList")
                else:
                    output_args.append(f"{oname}Tensor")
            ws_args_list = input_args + attr_args + output_args
        
        lines.append("aclOpExecutor* executor;")
        lines.append(f"ret = aclnn{self.op_def.op_name}GetWorkspaceSize({', '.join(ws_args_list)}, &workspaceSize, &executor);")
        lines.append(f"CHECK_RET(ret == SUCCESS, LOG_PRINT(\"GetWorkspaceSize failed.\\n\"); return FAILED);")
        
        lines.append("if (workspaceSize > 0) {{ ret = aclrtMalloc(&workspaceAddr, workspaceSize, ACL_MEM_MALLOC_HUGE_FIRST); CHECK_RET(ret == SUCCESS, LOG_PRINT(\"Malloc workspace failed.\\n\"); return FAILED); }}")
        
        lines.append(f"ret = aclnn{self.op_def.op_name}(workspaceAddr, workspaceSize, executor, stream);")
        lines.append(f"CHECK_RET(ret == SUCCESS, LOG_PRINT(\"Execution failed.\\n\"); return FAILED);")
        
        lines.append("ret = aclrtSynchronizeStream(stream);")
        lines.append("CHECK_RET(ret == SUCCESS, LOG_PRINT(\"Synchronize stream failed.\\n\"); return FAILED);")
        
        lines.append("\n// Get and Write Outputs")
        for conf in case.get('output_desc', []):
            name = conf['name']
            lines.append(f"{{ // Scope for retrieving output '{name}'")
            lines.append(f"    std::string finalOutputPath;")
            if conf.get('data_path_is_default', False):
                lines.append(f"    finalOutputPath = defaultDataDir + \"/output/{conf['data_path']}\";")
            else:
                is_abs = os.path.isabs(conf['data_path'])
                lines.append(f"    finalOutputPath = {'true' if is_abs else 'false'} ? \"{conf['data_path']}\" : casePath + \"/{conf['data_path']}\";")
            
            shape_str = str(conf['shape']).replace('[', '{').replace(']', '}')
            json_type = conf['data_type'].lower()
            cpp_type = mappings.JSON_TO_CPP_TYPE.get(json_type, "/*_err_*/")
            sizeof_type = mappings.JSON_TO_SIZEOF_TYPE.get(json_type, "/*_err_*/")
            
            lines.append(f"    std::vector<int64_t> {name}Shape = {shape_str};")
            lines.append(f"    if (outputShapes.count(\"{name}\") > 0) {{ {name}Shape = outputShapes.at(\"{name}\"); }}")

            lines.extend([
                f"    size_t {name}Size = GetShapeSize({name}Shape);",
                f"    std::vector<{cpp_type}> {name}ResultData({name}Size);",
                f"    ret = aclrtMemcpy({name}ResultData.data(), {name}Size * sizeof({sizeof_type}), {name}DeviceAddr, {name}Size * sizeof({sizeof_type}), ACL_MEMCPY_DEVICE_TO_HOST);",
                "    CHECK_RET(ret == SUCCESS, LOG_PRINT(\"Copy result failed.\\n\"); return FAILED);",
                f"    WriteFile(finalOutputPath, {name}ResultData.data(), {name}Size * sizeof({sizeof_type}));",
                f"}}"
            ])

        for proto_name, group in dynamic_output_groups.items():
            for tensor_desc in group['tensors']:
                tname = tensor_desc['name']
                lines.append(f"{{ // Scope for retrieving dynamic output '{tname}'")
                lines.append(f"    std::string finalOutputPath;")
                if tensor_desc.get('data_path_is_default', False):
                    lines.append(f"    finalOutputPath = defaultDataDir + \"/output/{tensor_desc['data_path']}\";")
                else:
                    is_abs = os.path.isabs(tensor_desc['data_path'])
                    lines.append(f"    finalOutputPath = {'true' if is_abs else 'false'} ? \"{tensor_desc['data_path']}\" : casePath + \"/{tensor_desc['data_path']}\";")
                shape_str = str(tensor_desc['shape']).replace('[', '{').replace(']', '}')
                json_type = tensor_desc['data_type'].lower()
                cpp_type = mappings.JSON_TO_CPP_TYPE.get(json_type, "/*_err_*/")
                sizeof_type = mappings.JSON_TO_SIZEOF_TYPE.get(json_type, "/*_err_*/")
                lines.append(f"    std::vector<int64_t> {tname}Shape = {shape_str};")
                lines.append(f"    if (outputShapes.count(\"{tname}\") > 0) {{ {tname}Shape = outputShapes.at(\"{tname}\"); }}")
                lines.extend([
                    f"    size_t {tname}Size = GetShapeSize({tname}Shape);",
                    f"    std::vector<{cpp_type}> {tname}ResultData({tname}Size);",
                    f"    ret = aclrtMemcpy({tname}ResultData.data(), {tname}Size * sizeof({sizeof_type}), {tname}DeviceAddr, {tname}Size * sizeof({sizeof_type}), ACL_MEMCPY_DEVICE_TO_HOST);",
                    "    CHECK_RET(ret == SUCCESS, LOG_PRINT(\"Copy dynamic output result failed.\\n\"); return FAILED);",
                    f"    WriteFile(finalOutputPath, {tname}ResultData.data(), {tname}Size * sizeof({sizeof_type}));",
                    f"}}"
                ])

        lines.append("INFO_LOG(\"Write output success.\");")
        
        # --- 3. CLEANUP ---
        lines.append("\n// 3. CLEANUP")
        # Clean up unique resources only once
        for name in sorted(list(all_unique_tensor_names)):
            is_tensor_in_case = name in case_tensor_inputs_map or name in {c['name'] for c in case.get('output_desc', [])}
            if is_tensor_in_case:
                lines.append(f"if ({name}Tensor) aclDestroyTensor({name}Tensor);")
                lines.append(f"if ({name}DeviceAddr) aclrtFree({name}DeviceAddr);")

        for proto_name, group in dynamic_input_groups.items():
            lines.append(f"if ({proto_name}TensorList) aclDestroyTensorList({proto_name}TensorList);")
            for tensor_desc in group['tensors']:
                tname = tensor_desc['name']
                lines.append(f"if ({tname}Tensor) aclDestroyTensor({tname}Tensor);")
                lines.append(f"if ({tname}DeviceAddr) aclrtFree({tname}DeviceAddr);")
        for proto_name, group in dynamic_output_groups.items():
            lines.append(f"if ({proto_name}TensorList) aclDestroyTensorList({proto_name}TensorList);")
            for tensor_desc in group['tensors']:
                tname = tensor_desc['name']
                lines.append(f"if ({tname}Tensor) aclDestroyTensor({tname}Tensor);")
                lines.append(f"if ({tname}DeviceAddr) aclrtFree({tname}DeviceAddr);")

        lines.append("if (workspaceAddr) aclrtFree(workspaceAddr);")

        for s_inp in case_scalar_inputs:
            lines.append(f"if ({s_inp['name']}Scalar) aclDestroyScalar({s_inp['name']}Scalar);")
        for attr in processed_attrs:
            name = attr['name']
            attr_type = attr['type']
            if attr_type in mappings.SCALAR_ATTR_TO_ACL_DTYPE:
                lines.append(f"if ({name}Scalar) aclDestroyScalar({name}Scalar);")
            elif attr_type in mappings.LIST_ATTR_TO_ACL_ARRAY_TYPE:
                destroy_func = mappings.LIST_ATTR_TO_ACL_DESTROY_FUNC[attr_type]
                lines.append(f"if ({name}Acl) {destroy_func}({name}Acl);")

        lines.append("aclrtDestroyStream(stream);")
        lines.append("aclrtResetDevice(deviceId);")
        lines.append("aclFinalize();")
        lines.append("return SUCCESS;")
        
        return "\n".join(lines)

    def _generate_main_dispatcher(self) -> str:
        """Generates a main function that robustly parses args."""
        lines = [
            "int main(int argc, char* argv[])",
            "{",
            "    std::string case_name;",
            "    std::string timestamp;",
            "    std::string output_shapes_str;",
            "",
            "    // Robust argument parsing",
            "    for (int i = 1; i < argc; ++i) {",
            "        if (strcmp(argv[i], \"--case_name\") == 0 && i + 1 < argc) {",
            "            case_name = argv[++i];",
            "        } else if (strcmp(argv[i], \"--timestamp\") == 0 && i + 1 < argc) {",
            "            timestamp = argv[++i];",
            "        } else if (strcmp(argv[i], \"--output_shapes\") == 0 && i + 1 < argc) {",
            "            output_shapes_str = argv[++i];",
            "        }",
            "    }",
            "",
            "    if (case_name.empty() || timestamp.empty()) {",
            "        std::cout << \"Usage: \" << argv[0] << \" --case_name <case> --timestamp <ts> [--output_shapes <dict_str>]\" << std::endl;",
            "        return FAILED;",
            "    }",
            "",
            "    // Parse Output Shapes",
            "    auto outputShapes = ParseOutputShapesStr(output_shapes_str);",
            "    auto ret = FAILED;",
            ""
        ]
        
        # Build the if-else if chain
        for i, case in enumerate(self.cases):
            condition = "if" if i == 0 else "else if"
            case_name_str = case['case_name']
            lines.append(f"    {condition} (case_name == \"{case_name_str}\") {{")
            lines.append(f"        INFO_LOG(\"Running case: {case_name_str}\");")
            lines.append(f"        ret = run_case_{case_name_str}(timestamp, outputShapes);") 
            lines.append("    }")

        lines.extend([
            "    else {",
            "        ERROR_LOG(\"Unknown case name: %s\", case_name.c_str());",
            "    }",
            "",
            "    // 3. PRINT FINAL STATUS",
            "    if (ret == SUCCESS) {",
            "        INFO_LOG(\"Successfully generated output for '%s' !\", case_name.c_str());",
            "    } else {",
            "        ERROR_LOG(\"Failed to generate output for '%s' !\", case_name.c_str());",
            "    }",
            "    return ret;",
            "}",
        ])
        
        return "\n".join(lines)