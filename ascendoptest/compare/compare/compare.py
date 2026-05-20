from ml_dtypes import bfloat16
from compare.accuracy_config import AccuracyConfig
import numpy as np
import os

def replace_inf(arr):
    # 分离浮点类型和整数类型的处理逻辑
    if np.issubdtype(arr.dtype, np.floating):
        # 处理浮点类型
        finfo = np.finfo(arr.dtype)

        # 替换正无穷为类型最大值
        posinf_mask = np.isposinf(arr)
        arr[posinf_mask] = finfo.max

        # 替换负无穷为类型最小负值（-finfo.max）
        neginf_mask = np.isneginf(arr)
        arr[neginf_mask] = -finfo.max
        return arr

    elif np.issubdtype(arr.dtype, np.integer):
        # 整数类型无 inf，直接返回原数组
        return arr
    elif np.issubdtype(arr.dtype, bfloat16):
        # bfloat16手动设置最大和最小值
        finfo_max = np.array([3.3881315e+38], dtype=np.float32).item()  # bfloat16 最大值
        finfo_min = -finfo_max
        finfo = type('', (), {'max': finfo_max, 'min': finfo_min})()  # 模拟 finfo 对象
        posinf_mask = np.isposinf(arr)
        arr[posinf_mask] = finfo.max
        neginf_mask = np.isneginf(arr)
        arr[neginf_mask] = -finfo.max

        return arr
    else:
        # 其他类型
        return arr


def compare_complex(output, expect, err_threshold, show_err_num=10):
    """
    复数对比函数 - 分别检查实部和虚部误差
    :param output: 实际输出数组 (复数)
    :param expect: 预期输出数组 (复数)
    :param err_threshold: 误差阈值 (绝对误差, 错误率)
    :param show_err_num: 展示错误数量
    :return: 对比结果 (bool)
    """
    tolerance_value = err_threshold[0]
    error_rate = err_threshold[1]
    
    # 分离实部和虚部
    output_real = output.real
    output_imag = output.imag
    expect_real = expect.real
    expect_imag = expect.imag
    
    # 计算实部和虚部的绝对误差
    real_diff = np.abs(output_real - expect_real)
    imag_diff = np.abs(output_imag - expect_imag)
    
    # 分别检查实部和虚部是否在容忍范围内
    real_valid = real_diff <= tolerance_value
    imag_valid = imag_diff <= tolerance_value
    
    # 只有实部和虚部同时满足要求才算有效
    combined_valid = real_valid & imag_valid
    
    if not combined_valid.all():
        error_count = np.sum(~combined_valid)
        if error_count > output.size * error_rate:
            if show_err_num > 0:
                error_positions = np.argwhere(~combined_valid)
                total_errors = len(error_positions)
                # 后续可以打印错误统计
                # print(f"❌ Total number of errors: {total_errors}, Error ratio: {total_errors/output.size:.2%}")
                print(f"📊 the first {min(show_err_num, total_errors)} erroneous data:")
                for i, pos in enumerate(error_positions[:show_err_num]):
                    out_val = output[pos]
                    exp_val = expect[pos]
                    real_err = real_diff[pos]
                    imag_err = imag_diff[pos]
                    
                    print(f"index: {pos}", f"  → real output value: {out_val}", f"  → expected value: {exp_val}")
            return False
    return True


def compare_default(output, expect ,err_threshold, show_err_num=10):
    tolerance_value = err_threshold[0]
    error_rate = err_threshold[1]
    minimum = 10e-10
    # 处理inf值
    output = replace_inf(output)
    expect = replace_inf(expect)
    result = np.abs(output - expect)  # 计算运算结果和预期结果偏差
    result_atol = np.less_equal(result, tolerance_value)  # 计算绝对误差
    #计算相对误差
    maxmin = np.maximum(np.abs(expect), np.abs(output)) # 取最大的绝对值
    maxmin = maxmin + (10e-10) # 避免除0
    result_rtol = np.less_equal(result / maxmin, tolerance_value)  # 计算相对误差
    result_diff = np.where(result >= 1, result_rtol, result_atol)  # 如果偏差值大于1，使用相对误差，如果偏差值小于1使用绝对误差

    both_nan = np.isnan(output) & np.isnan(expect) # 判断是否实际输出和预期输出都是nan
    result_diff = result_diff | both_nan  # 忽略都是nan的情况

    if not result_diff.all():
        if  np.sum(result_diff == False) > output.size * error_rate:  # 误差超出预期时返回打印错误，返回对比失败
            if show_err_num > 0:
                error_positions = np.argwhere(result_diff == False)
                total_errors = len(error_positions)
                
                # 后续可以打印错误统计
                # print(f"❌ Total number of errors: {total_errors}, Error ratio: {total_errors/output.size:.2%}")
                print(f"📊 the first {min(show_err_num, total_errors)} erroneous data:")
                
                # 根据show_err_num打印具体错误数据位置和值
                for i, pos in enumerate(error_positions[:show_err_num]):
                    out_val = output[pos]
                    exp_val = expect[pos]
                    print(f"index: {pos} ", f"real output value: {out_val}{' (inf)' if np.isinf(out_val) else ''}", f"expected value: {exp_val}{' (inf)' if np.isinf(exp_val) else ''}")

            return False
    return True

def compare(output_desc, case_name, show_err_num=10):
    output_name = output_desc.name
    output_dtype = output_desc.data_type
    if output_dtype == "float": # numpy的float对应的数据类型为float64，应改为float32作为实际数据类型
        output_dtype = "float32"
    err_threshold = output_desc.err_threshold
    if err_threshold is None or len(err_threshold) == 0:
        err_threshold = AccuracyConfig.default_acc[output_dtype]
    if os.path.exists(output_desc.data_path) == False:
        print(f"case_name: {case_name}, output_name: {output_name}  compare failed, data_path { os.path.abspath(output_desc.data_path)} not exist")
        return False
    if os.path.exists(output_desc.golden_path) == False:
        print(f"case_name: {case_name}, output_name: {output_name}  compare failed, golden_path { os.path.abspath(output_desc.golden_path)} not exist")
        return False
    output_data = np.fromfile(output_desc.data_path, dtype=output_dtype).reshape(-1)
    expect_data = np.fromfile(output_desc.golden_path, dtype=output_dtype).reshape(-1)
    if len(output_data) != len(expect_data):
        print(f"case_name: {case_name}, output_name: {output_name}  compare failed, len not equal, output_len: {len(output_data)}, expect_len: {len(expect_data)}")
        return False
    if output_dtype == "complex64":
        result = compare_complex(output_data, expect_data, err_threshold, show_err_num)
        if result:
            print(f"case_name: {case_name}, output_name: {output_name}  compare passed")
            return True
        else:
            print(f"case_name: {case_name}, output_name: {output_name}  compare failed")
            return False
        
    elif output_dtype == "complex128":
        result = compare_complex(output_data, expect_data, err_threshold, show_err_num)
        if result:
            print(f"case_name: {case_name}, output_name: {output_name}  compare passed")
            return True
        else:
            print(f"case_name: {case_name}, output_name: {output_name}  compare failed")
            return False
    elif output_dtype == "bool":
        output_data = output_data.astype(np.uint8)
        expect_data = expect_data.astype(np.uint8)
        result = compare_default(output_data, expect_data, err_threshold, show_err_num)
        if result:
            print(f"case_name: {case_name}, output_name: {output_name}  compare passed")
        else:
            print(f"case_name: {case_name}, output_name: {output_name}  compare failed")
        return result
    else:
        result = compare_default(output_data, expect_data, err_threshold, show_err_num)
        if result:
            print(f"case_name: {case_name}, output_name: {output_name}  compare passed")
        else:
            print(f"case_name: {case_name}, output_name: {output_name}  compare failed")
        return result

   