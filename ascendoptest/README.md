# AscendOpTest

#### 介绍
基于昇腾CANN构建高效易用的Ascend C算子精度、性能测试工具。

#### 软件架构
软件架构说明
该项目主要包含以下几个模块，各模块分工明确，协同完成 Ascend C 算子的精度与性能测试工作：

- **`aclnn-gen` 模块**：用于生成 ACLNN 相关的内容。
  - `aclnn_gen`：核心功能实现目录。
  - `pyproject.toml`：Python 项目配置文件，定义项目元数据和依赖项。
  - `requirements.txt`：列出项目所需的 Python 依赖库。
  - `setup.cfg`：Python 项目的配置文件，用于配置打包相关信息。

- **`compare` 模块**：负责预期数据和实际数据对比，判断测试结果是否符合预期。
  - `compare`：包含数据比较的核心代码。
  - `data_compare.py`：模块入口，可以单独调用该模块进行数据对比。
  - `output_parse`：用于解析测试输出结果的目录。

- **`data_gen` 模块**：生成测试所需的数据。
  - `data_gen`：数据生成的核心代码目录。
  - `data_gen.py`：模块入口，可以单独调用该模块进行数据生成。
  - `input_parse`：用于解析测试输入的目录。

- **`golden` 模块**：生成预期数据。
  - `case_parse`：用于解析测试用例的目录。
  - `golden_gen`：基准数据生成的核心代码目录。
  - `golden_gen.py`：模块入口，可以单独调用该模块进行预期数据生成。

- **`run_test.py`**：项目的主测试脚本，用于协调各模块完成测试任务。

#### 使用约束

- <span style="color:red">算子描述文件内输入、输出、属性顺序和测试用例文件内输入、输出、属性顺序保持一致，且name字段值一致。</span>
- <span style="color:red">如果有可选输入或可选输出，测试用例文件内可不选填，但仍需要保持其他输入、输出、属性的顺序与算子描述文件内一致，且name字段值一致。</span>
- <span style="color:red">预期函数内参数名应和算子描述文件、case文件内的输入、属性顺序一致，且name字段一致</span>
- <span style="color:red">自定义算子部署目录的算子测试前一定要执行source 部署目录下的vendors/customize/bin/set_env.bash, 确保部署算子生效。</span>

#### 使用说明

1.  使用前需要安装CANN，并完成相关环境变量配置，参照 [快速安装CANN](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/83RC1alpha001/softwareinst/instg/instg_quick.html?Mode=PmIns&OS=Debian&Software=cannToolKit), 使用前需要安装ml_dtypes库，用于使用numpy生成或者解析bfloat16类型数据，执行以下命令安装：
    ```
    pip install ml_dtypes
    ```
2.  部署好待测试算子，参照[UnalignAddCustomSample](https://gitee.com/ascend/samples/tree/master/operator_contrib/UnalignAddCustomSample/FrameworkLaunch)，配置好算子描述文件，参照[创建算子工程](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/83RC1alpha001/opdevg/Ascendcopdevg/atlas_ascendc_10_0060.html)章节内创建算子工程使用的文件，配置好测试用例json文件，包括算子、输入数据、预期输出。
    以AddCustom为例，算子原型json文件格式:
    ```
    [
        {
            "op": "AddCustom",
            "input_desc": [
                {
                    "name": "x",
                    "param_type": "required",
                    "format": [
                        "ND",
                        "ND",
                        "ND"
                    ],
                    "type": [
                        "float16",
                        "float",
                        "int32"
                    ]
                },
                {
                    "name": "y",
                    "param_type": "required",
                    "format": [
                        "ND",
                        "ND",
                        "ND"
                    ],
                    "type": [
                        "float16",
                        "float",
                        "int32"
                    ]
                }
            ],
            "output_desc": [
                {
                    "name": "z",
                    "param_type": "required",
                    "format": [
                        "ND",
                        "ND",
                        "ND"
                    ],
                    "type": [
                        "float16",
                        "float",
                        "int32"
                    ]
                }
            ]
        }
    ]
    ```
    以AddCustom为例，测试用例json文件格式:
    ```
    [
        {
            "case_name": "Test_001",
            "op_name": "AddCustom",
            "case_path": "",
            "expect_func":"/xxx/custom_add.py:custom_add",
            "input_desc": [
                {
                    "name": "x",
                    "format": "ND",
                    "data_type": "float16",
                    "param_type":"required",
                    "shape": [2,3],
                    "data_path":"",
                    "value_range":[0,100]
                },
                {
                    "name": "y",
                    "format": "ND",
                    "data_type": "float16",
                    "param_type":"required",
                    "shape": [2,3],
                    "data_path":"",
                    "value_range":[0,100]
                }
            ],
            "output_desc": [
                {
                    "name": "z",
                    "format": "ND",
                    "data_type": "float16",
                    "param_type":"required",
                    "shape": [2,3],
                    "data_path":"",
                    "golden_path":"",
                    "err_threshold":[0.001,0.001]
                }
            ],
            "attr_desc": [
            ]
        }
    ]
    ```
    对于存在属性的算子，需要在attr_desc字段中配置算子属性，属性名称和属性值需要和算子原型描述文件中的属性名称和属性值以及顺序保持一致。
    例如[Tril](https://gitee.com/ascend/cann-ops/tree/master/src/math/tril):
    ```
    [
        {
            "case_name": "Test_001",
            "op_name": "Tril",
            "case_path":"",
            "expect_func":"xxxx/custom_op.py:custom",
            "input_desc": [
                {
                    "format": "ND",
                    "data_type": "float16",
                    "param_type":"required",
                    "shape": [3, 43,117],
                    "name": "x",
                    "data_path":"",
                    "value_range":[0,100]
                }
            ],
            "output_desc": [
                {
                    "format": "ND",
                    "data_type": "float16",
                    "param_type":"required",
                    "shape": [3, 43,117],
                    "name": "y",
                    "data_path":"",
                    "golden_path":"",
                    "err_threshold":[0.001,0.001]
                }
            ],
            
            "attr_desc": [
                {
                    "name": "diagonal",
                    "param_type": "optional",
                    "type": "int",
                    "value": 10
                }
            ]
        }
    ]
    ```

    对于输出shape不确定，需要根据Input或者attr的具体值计算的情况，需要在output_desc[].shape_depend字段中配置计算输出shape的函数。
    计算输出shape的函数需要在shape.py文件中实现，函数名需要和output_desc[].shape_depend字段中配置的函数名保持一致。
    函数参数为输入数据的shape，返回值为输出数据的shape。

    例如AddCustom算子的shape.py文件:
    ```
    def calc_expect_func( x,y):
        z = x + y
        shape = z.shape
        return [shape]
    ```
    ```
    [
        {
            "case_name": "Test_001",
            "op_name": "AddCustom",
            "case_path": "",
            "expect_func":"/xxx/custom_add.py:custom_add",
            "input_desc": [
                {
                    "name": "x",
                    "format": "ND",
                    "data_type": "float16",
                    "param_type":"required",
                    "shape": [2,3],
                    "data_path":"",
                    "value_range":[0,100]
                },
                {
                    "name": "y",
                    "format": "ND",
                    "data_type": "float16",
                    "param_type":"required",
                    "shape": [2,3],
                    "data_path":"",
                    "value_range":[0,100]
                }
            ],
            "output_desc": [
                {
                    "name": "z",
                    "format": "ND",
                    "data_type": "float16",
                    "param_type":"required",
                    "shape": [2,3],
                    "data_path":"",
                    "golden_path":"",
                    "err_threshold":[0.001,0.001],
                    "shape_depend":"shape.py:calc_expect_func"
                }
            ],
            "attr_desc": [
            ]
        }
    ]
    ```


    以下是对上述 JSON 文件中各 字段 的描述：
    | 字段 | 描述 |
    | --- | --- |
    | `case_name` | 测试用例的名称，用于唯一标识该测试用例。 |
    | `op_name` | 待测试算子的名称，此处为 `AddCustom`。 |
    | `case_path` | 测试用例数据及性能结果存放路径，用于指定测试用例输入输出bin文件所在的目录。默认值为执行run_test.py的目录。 |
    | `expect_func` | 指定计算预期结果的函数，格式为 `文件路径:函数名`。不配置时默认使用output_desc[].golden_path 作为预期输出 |
    | `input_desc` | 输入数组，包含所有输入数据的描述信息。 |
    | `input_desc[].name` | 输入数据的名称，用于标识不同的输入。该字段和算子原型描述文件中的name保持一致,且顺序一致 |
    | `input_desc[].format` | 输入数据的格式，例如 `ND`。 |
    | `input_desc[].data_type` | 输入数据的数据类型，如 `float16`。 |
    | `input_desc[].param_type` | 输入参数的类型，`required` 表示该参数为必需参数。 |
    | `input_desc[].shape` | 输入数据的形状，以列表形式表示。当值为[]时候,表示输入数据为标量(aclScalar) |
    | `input_desc[].data_path` | 输入数据文件的路径。不配置时默认为op_test/{op_name}_{case_name}_时间戳/input/{input_desc[].name}.bin |
    | `input_desc[].value_range` | 输入数据的值范围，以列表形式表示最小值和最大值。 |
    | `output_desc` | 输出数组，包含所有输出数据的描述信息。 |
    | `output_desc[].format` | 输出数据的格式，例如 `ND`。 |
    | `output_desc[].data_type` | 输出数据的数据类型，如 `float16`。 |
    | `output_desc[].param_type` | 输出参数的类型，`required` 表示该参数为必需参数。 |
    | `output_desc[].shape` | 输出数据的形状，以列表形式表示。 |
    | `output_desc[].name` | 输出数据的名称，用于标识不同的输出。该字段和算子原型描述文件中的name保持一致,且顺序一致 |
    | `output_desc[].data_path` | 输出数据文件的路径。 不配置时默认为{case_name}_{output_desc[].name}.bin |
    | `output_desc[].shape_depend` | 指定计算输出shape的函数，格式为 `文件路径:函数名`。不配置时默认使用output_desc[].shape 作为输出shape |
    | `output_desc[].golden_path` | 输出数据的基准文件路径，用于与实际输出对比。 不配置时默认为op_test/{op_name}_{case_name}_时间戳/output/golden_{output_desc[].name}.bin |
    | `output_desc[].err_threshold` | 输出数据的误差阈值，以列表形式表示允许的误差范围[绝对偏差值,错误率]。 |
    | `attr_desc` | 属性数组，包含算子的属性描述信息，当前示例为空。 |
    | `attr_desc[].name` | 属性的名称，用于标识不同的属性。该字段和算子原型描述文件中的name保持一致,且顺序一致 |
    | `attr_desc[].type` | 属性的数据类型，如 `int`、`float`、`string`等。与算子原型对应，可选值参考[OpAttrDef类成员函数](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/850alpha001/API/ascendcopapi/atlasascendc_api_07_0976.html)  与acl类型对应关系参考[aclnn-gen配置](https://gitee.com/sutonghua/ascendoptest/blob/master/aclnn-gen/aclnn_gen/config/mappings.py)|
    | `attr_desc[].value` | 属性的值，根据数据类型填写。 |
    | `attr_desc[].param_type` | 属性是否为可选属性，`optional` 表示该参数为可选属性。 必选属性配置为`required` |

预期函数格式:
```
def expect_func(input1, input2 ..., attr1, attr2 ...):
    return [out1, out2, out3, ...]
```
    输入参数为输入和属性，输出参数为输出数组，数组元素为numpy.ndarray类型。
以上文custom_add.py:custom_add为例，预期函数:
```
def custom_add(a, b):
    c = a + b
    return [c]
```
如果输入或输出数据类型为bfloat16，需要特殊处理，因为torch的from_tensor和.numpy()不支持对bfloat16类型的nparray转换，需要先将bfloat16转换为float32，再进行转换。例如：
```
def custom_add(a, b):
    a_tensor = torch.from_numpy(a.astype(np.float32)).bfloat16()
    b_tensor = torch.from_numpy(b.astype(np.float32)).bfloat16()
    c = torch.add(a_tensor, b_tensor)
    return [c.to(torch.float32).numpy().astype(bfloat16)]
```



3.  测试算子功能或性能需要配置LD_LIBRARY_PATH指定自定义算子的op_api库路径环境变量。
    eg:
    ```
    export LD_LIBRARY_PATH=/home/ma-user/Ascend/ascend-toolkit/latest/opp/vendors/customize/op_api/lib:$LD_LIBRARY_PATH
    ```
    应根据实际情况修改。例如华为云ECS默认算子部署安装路径为"/home/ma-user/Ascend/ascend-toolkit/latest/opp/vendors/customize"，此时环境变量应设置为:
    ```
    export LD_LIBRARY_PATH=/home/ma-user/Ascend/ascend-toolkit/latest/opp/vendors/customize/op_api/lib:$LD_LIBRARY_PATH
    ```

    测试算子仿真需要配置环境变量，参考 [msprof op simulator配置](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/82RC1/devaids/optool/atlasopdev_16_0083.html)
    ```
    export LD_LIBRARY_PATH=${INSTALL_DIR}/tools/simulator/Ascendxxxyy/lib:$LD_LIBRARY_PATH 
    ```

4.  运行 `run_test.py -i <算子描述文件> -c <测试用例文件> -n <测试用例名称>` ，即可完成测试。
    run_test.py 参数说明:
    - `-i` 算子描述文件，必选
    - `-c` 测试用例文件，必选
    - `-a` 指定AscendOpTest执行过程中生成的aclnn调用工程文件保存路径，可选，默认值为aclnn_test
    - `-e` 指定显示精度不足的数据个数，可选，不设置时，默认为显示10条
    - `-d` 指定抓取性能数据或仿真文件的输出目录，可选，不设置时，根据具体模式生成默认目录名
    - `-n` 测试用例名称，可选，默认为执行所有用例
    - `-k` 算子kernel名称，可选，用于指定算子性能测试时抓取的kernel名称，不传入时会通过测试用例中的op_name字段自动设置kernel_name,为op_name的下划线小写形式
    - `-r` 测试用例运行结果文件名，可选，默认值为result.csv
    - `--msprof` 是否设置性能测试，可选，默认值为False, 设置后，会在 `-d` 指定的输出目录下生成msprof文件
    - `--op` 抓取性能模式，可选，默认值为False，设置后会以 `msprof op` 形式抓取性能，不设置则以 `msprof --application` 形式抓取，设置后 `-d` 默认值为 `case_name_时间戳_msprof_op`，不设置 `-d` 默认路径为 `case_name_时间戳_msprof_application`
    - `--sim` 是否设置仿真模式，可选，设置时执行仿真测试，不设置时执行性能测试，设置后 `-d` 默认值为 `case_name_时间戳_msprof_op_simulator`, 必须设置 `--op` 后才能设置 `--sim`, 单独设置 `--sim` 无效
    - `--build` 是否需要重新编译aclnn调用程序，每次修改用例文件后需要配置该参数，重复测试可以不配置该参数
    - `--op-path` 指定ASCEND_CUSTOM_OPP_PATH，可选，默认值为 `/usr/local/Ascend/ascend-toolkit/latest/opp/vendors/customize/op_api`
    - `--op-type` 指定算子类型，可选，默认值为 `custom`，可选值为 `custom` 或 `builtin`，表示测试自定义算子或内置算子
    - `-h` 帮助信息

    精度测试示例:
    ```
    python run_test.py -i add_custom_prototype.json -c add_custom_cases.json
    ```

    指定用例精度测试示例:
    ```
    python run_test.py -i add_custom_prototype.json -c add_custom_cases.json -n Test_001
    ```

    msprof --application性能测试示例:
    ```
    python run_test.py -i add_custom_prototype.json -c add_custom_cases.json --msprof
    ```
    msprof --application性能测试指定输出目录示例:
    ```
    python run_test.py -i add_custom_prototype.json -c add_custom_cases.json --msprof -d msprof_dir
    ```
    msprof op性能测试示例:
    ```
    python run_test.py -i add_custom_prototype.json -c add_custom_cases.json --msprof --op
    ```
    msprof op simulator测试示例:
    ```
    python run_test.py -i add_custom_prototype.json -c add_custom_cases.json --msprof --op --sim
    ```

5. 针对ops-math、ops-nn等算子开源仓，测试时需确认待测试算子的手写aclnn接口函数名、文件名与自动生成的保持一致，若不一致需在测试工具生成的调用程序代码中修改对应的aclnn头文件和函数名。另外，因手写aclnn接口常会用到loop::xxx类接口，需在工具生成的调用程序CMakeLists.txt文件内补充对应的头文件路径及so依赖，例如：
![CMakeLists.txt修改前后对比](https://gitee.com/youmoxiao/resource/raw/master/img/diff.png)
完成上述修改后，先执行以下命令配置环境变量，确保aclnn调用程序能找到正确的库文件：
```shell
export DDK_PATH=${ASCEND_TOOLKIT_HOME}
export NPU_HOST_LIB=${ASCEND_TOOLKIT_HOME}/lib64
```
随后执行调用工程的build_aclnn.sh脚本完成编译，再运行run_test.py即可开展测试。注意测试时不要配置--build参数，否则会强制重新生成调用代码，覆盖之前手动修改的内容。

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request

## 待开发功能
1. 增加case生成的工具，支持单case模板生成及批量case生成
2. json文件支持相对路径，相对于入口脚本
3. json文件中的路径需要调整，指定一个统一的path，其余都用相对路径
4. README提供使用的示例或指导