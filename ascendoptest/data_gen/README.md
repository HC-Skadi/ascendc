# AscendOpTest 数据生成模块

## 概述
`data_gen` 模块是 AscendOpTest 项目的核心组件之一，主要负责生成 Ascend C 算子测试所需的输入数据。通过灵活的配置，该模块能够根据不同的测试用例要求，生成符合格式、数据类型和形状的输入数据，为算子的精度和性能测试提供有力支持。

## 目录结构
```plaintext
data_gen/
|-- __init__.py
|-- __pycache__/
|-- data_generation.py
|-- gen_input.py
|-- data_gen.py
|-- input_parse/
|   |-- __init__.py
|   |-- input_desc.py
|   `-- input_parse.py
|-- README.md
```

## 主要文件及功能
* data_generation.py：核心数据生成逻辑文件，依据输入配置生成测试所需的输入数据。
* gen_input.py：提供生成输入数据的接口函数，可被其他模块调用。

* input_desc.py：定义输入数据描述的数据结构，用于规范输入数据的格式。
* input_parse.py：解析输入配置文件，将配置信息转换为程序可处理的对象。

* data_gen.py：模块的入口脚本，可直接运行以生成测试数据。

## 使用方法
生成测试数据
直接运行 data_gen.py 脚本，根据提示或命令行参数指定配置文件路径，即可生成测试数据。示例命令如下：
执行所有用例输入数据生成
```
python data_gen.py ir.json case.json
```
执行指定用例输入数据生成
```
python data_gen.py ir.json case.json case_name
```


## 输入配置文件示例
输入配置文件通常为 JSON 格式，示例如下：

```
[
    {
        "case_name": "Test_001",
        "op_name": "AddCustom",
        "expect_func":"custom_add.py:custom_add",
        "input_desc": [
            {
                "format": "ND",
                "data_type": "float16",
                "param_type":"required",
                "shape": [2,3],
                "name": "x",
                "data_path":"test_x.bin",
                "value_range":[0,100]
            },
            {
                "format": "ND",
                "data_type": "float16",
                "param_type":"required",
                "shape": [2,3],
                "name": "y",
                "data_path":"test_y.bin",
                "value_range":[0,100]
            }
        ],
        "output_desc": [
            {
                "format": "ND",
                "data_type": "float16",
                "param_type":"required",
                "shape": [2,3],
                "name": "z",
                "data_path":"test_z.bin",
                "golden_path":"test_golden_z.bin",
                "err_threshold":[0.001,0.001]
            }
        ],
        "attr_desc": [
        ]
    }
]
```