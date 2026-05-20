from ml_dtypes import bfloat16
import numpy as np
from pathlib import Path
import os

def generate_data_default(value_range, shape, dtype):
    if dtype == "bool":
        data = np.random.choice([True, False], size=shape)
    elif dtype == "bf16":
        data = np.random.uniform(value_range[0], value_range[1], shape).astype(bfloat16)
    elif dtype == "bfloat16":
        data = np.random.uniform(value_range[0], value_range[1], shape).astype(bfloat16)
    elif dtype == "float": # 通常float会指向float32，但numpy的float实际为double类型，要指定类型为Float时生成float32类型数据
        data = np.random.uniform(value_range[0], value_range[1], shape).astype(np.float32)
    elif dtype == "complex64":
        data_real = np.random.uniform(value_range[0], value_range[1], shape).astype(np.float32)
        data_imag = np.random.uniform(value_range[0], value_range[1], shape).astype(np.float32)
        data = data_real + 1j * data_imag
        data = data.astype(np.complex64)
    elif dtype == "complex128":
        data_real = np.random.uniform(value_range[0], value_range[1], shape).astype(np.float64)
        data_imag = np.random.uniform(value_range[0], value_range[1], shape).astype(np.float64)
        data = data_real + 1j * data_imag
        data = data.astype(np.complex128)
    else:
        data = np.random.uniform(value_range[0], value_range[1], shape).astype(dtype)
    return data

def generate_data(input_desc):
    if os.path.exists(input_desc.data_path):
        print("data file exists, skip gen data", input_desc.name, " data_path:", input_desc.data_path)
        return os.path.abspath(input_desc.data_path)
    data = generate_data_default(input_desc.value_range, input_desc.shape, input_desc.data_type)

    file_path = Path(input_desc.data_path)
    dir_path = file_path.parent
    if not dir_path.exists():
        dir_path.mkdir(parents=True)
    data.tofile(input_desc.data_path)
    print("gen data", input_desc.name, " success, data save in ",os.path.abspath(input_desc.data_path))
    return os.path.abspath(input_desc.data_path)

def generate_data_tensor_list(input_desc):
    if os.path.exists(input_desc.data_path):
        print("data file exists, skip gen data", input_desc.name, " data_path:", input_desc.data_path)
        return os.path.abspath(input_desc.data_path)
    tensor_list = []
    for shape in input_desc.shape:
        data = generate_data_default(input_desc.value_range, shape, input_desc.data_type)
        tensor_list.append(data)
    np_tensor_list = np.array(tensor_list)
    np_tensor_list.tofile(input_desc.data_path)
    print("gen data", input_desc.name, " success, data save in ",input_desc.data_path)
    return os.path.abspath(input_desc.data_path)
