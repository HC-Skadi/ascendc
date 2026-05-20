# AscendOpTest 常用脚本

## 概述
`scripts` 模块是 AscendOpTest 项目的功能拓展部分，其主要职责是提供各种自定义需求的功能实现脚本，以满足用户在测试过程中的各种定制化需求。

## 目录结构
```plaintext
scripts/
|-- gen_case.py
|-- get_prof.py
|-- README.md
```

## 主要文件及功能

* get_prof.py：解析性能数据文件，提取其中的性能数据结合用例生成性能数据文件。
* gen_case.py：根据算子原型文件和约束文件，生成符合要求的测试用例。


## 使用方法
### gen_case.py
直接运行 gen_case.py 脚本，通过命令行参数指定算子原型文件、约束文件、输出文件、用例数量、维度、是否生成广播用例，即可快速生成测试用例。

    gen_case.py 参数说明:
    - `-i` 算子原型文件，必选
    - `-c` 约束文件，可选
    - `-f` 约束函数，可选，如果使用了约束文件，则默认为constraint_condition
    - `-o` 输出用例文件，可选，默认值为case.json
    - `-n` 用例数量，可选，默认值为1
    - `-d` 指定生成的用例维度，可选，默认值为所有维度，指定时仅生成指定维度的用例
    - `-b` 是否生成广播用例，可选，默认值为False，设置为True时，10%概率生成广播用例

##### 约束文件内的约束函数应输入输出都为case，在约束函数内可以对单个case的所有字段值进行修改，示例如下：
```python
def constraint_condition(case):
    for input_desc in case["input_desc"]:
        if case["case_name"] == "Test_001":
            if input_desc["name"] == "x":
                input_desc["data_type"] = "float32" # 仅对Test_001用例生效,设置x输入类型为float32
        input_desc["value_range"] = [123, 123] # 设置所有输入取值范围为[123, 123]
    for output_desc in case["output_desc"]:
        if case["case_name"] == "Test_001":
            if output_desc["name"] == "z":
                output_desc["data_type"] = "float32" # 仅对Test_001用例生效,设置z输出类型为float32
                output_desc["shape"] = [123, 123] # 设置所有输出shape为[123, 123]
    for attr in case["attr_desc"]:
        if case["case_name"] == "Test_001":
            if attr["name"] == "alpha":
                attr["value"] = 1.0 # 设置用例Test_001的alpha属性值为1.0               

    return case
```
示例命令如下:
生成AddCustom算子的1个用例，保存到case.json文件中
```
python gen_case.py -i AddCustom.json
```
生成AddCustom算子的10个用例，保存到case.json文件中
```
python gen_case.py -i AddCustom.json -o case.json -n 10
```
生成AddCustom算子的10用例，保存到aaa/bbb/case.json文件中
```
python gen_case.py -i AddCustom.json -o aaa/bbb/case.json -n 10
```
生成AddCustom算子的2D维度的用例，保存到case.json文件中
```
python gen_case.py -i AddCustom.json -o case.json -n 10 -d 2
```
生成AddCustom算子的10个用例，支持生成广播用例，保存到case.json文件中
```
python gen_case.py -i AddCustom.json -o case.json -n 10 -b True
```
按照约束文件constraint_condition.py的constraint_condition函数生成用例，保存到case.json文件中
```
python gen_case.py -i AddCustom.json -o case.json -n 10 -c constraint_condition.py -f constraint_condition
```


### get_prof.py
直接运行 get_prof.py 脚本，通过命令行参数指定测试用例、性能文件目录、报表生成目录，即可生成性能数据文件。

    get_prof.py 参数说明:
    - `-c` 自定义算子性能数据文件，支持包含多次测试的性能数据，可选
    - `-b` build-in内置算子性能数据文件，支持包含多次测试的性能数据，可选
    - `-f` 测试用例文件，必选
    - `-d` 解析后的表格的输出目录，可选，不设置时，生成在当前目录下


示例命令如下：
解析自定义性能数据文件和build-in内置算子性能数据生成报表到prof_dir目录下
```
python get_prof.py -c Test_001_20251110080815_msprof_op -b Test_001_20251110084119_msprof_op -f case.json -d prof_dir
```
单独解析自定义性能数据生成报表到当前目录
```
python get_prof.py -c Test_001_20251110080815_msprof_op -f case.json
```
单独解析build-in内置算子性能数据生成报表到当前目录
```
python get_prof.py -b Test_001_20251110084119_msprof_op -f case.json
```