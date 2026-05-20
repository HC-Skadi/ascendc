# AscendOpTest 基准数据生成模块

## 概述
`golden` 模块是 AscendOpTest 项目的关键组成部分，其主要职责是生成算子测试所需的预期（基准）数据。在对 Ascend C 算子进行精度和性能测试时，预期数据可作为参考标准，与算子的实际输出进行对比，从而验证算子功能的正确性。

## 目录结构
```plaintext
golden/
|-- __init__.py
|-- __pycache__/
|-- case_parse/
|   |-- __init__.py
|   |-- case_parse.py
|   |-- case_desc.py
|-- golden_gen/
|   |-- __init__.py
|   |-- compute.py
|   |-- save_data.py
|-- golden_gen.py
|-- README.md
```

## 主要文件及功能

* case_parse.py：解析测试用例配置文件，将其中的信息转换为程序可处理的对象。
* case_desc.py：定义测试用例描述的数据结构，规范测试用例信息的格式。

* compute.py：核心计算逻辑文件，依据测试用例配置和输入数据计算预期输出。
* save_data.py：将计算得到的预期数据保存到指定文件中。
* golden_gen.py：模块的入口脚本，可直接运行以生成基准数据。

## 使用方法
生成基准数据
直接运行 golden_gen.py 脚本，通过命令行参数指定测试用例配置文件和输入数据文件路径，即可生成基准数据。示例命令如下：
生成所有用例预期结果
```
python golden_gen.py ir.json case.json
```
生成指定用例预期结果
```
python golden_gen.py ir.json case.json case_name
```
