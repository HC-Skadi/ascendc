# AscendOpTest 比较模块

## 概述
`compare` 模块是 AscendOpTest 项目的重要组成部分，主要负责对预期数据和实际数据进行对比，从而判断算子测试结果是否符合预期。通过该模块，可以有效验证 Ascend C 算子的精度，确保算子在不同场景下的计算准确性。

## 目录结构
```plaintext
compare/
|-- __init__.py
|-- accuracy_config.py
|-- compare.py
|-- verify_result.py
|-- data_compare.py
|-- output_parse/
|   |-- __init__.py
|   |-- output_desc.py
|   `-- output_parse.py
```
## 主要文件
* accuracy_config.py：该文件用于配置精度比较相关的参数，例如误差阈值等，为数据对比提供基础配置。
* compare.py：包含数据比较的核心代码，实现了预期数据和实际数据对比的主要逻辑。
* verify_result.py：负责验证对比结果，根据对比结果判断测试是否通过。

* output_desc.py：定义了输出结果的描述信息，方便对测试输出进行结构化处理。
* output_parse.py：用于解析测试输出结果，将原始输出转换为便于分析的格式。

* data_compare.py：模块的入口文件，可以单独调用该模块进行数据对比操作。

## 使用方法
单独调用数据对比模块
可以直接运行 data_compare.py 进行数据对比，示例命令如下：

对比所有用例输出：
```
python data_compare.py -i ir_json -c case.json
```
或对比指定用例输出:
```
python data_compare.py -i ir_json -c case.json -n case_name
```
