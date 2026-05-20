# Issue #1270: [Usage]: Modelslim

## 基本信息

- **编号**: #1270
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1270
- **创建时间**: 2025-06-18T06:37:28Z
- **关闭时间**: 2025-12-29T11:27:06Z
- **更新时间**: 2025-12-29T11:27:06Z
- **提交者**: @pichangping
- **评论数**: 5

## 标签

无

## 问题描述

w4a8减层权重生成步骤（4层）
```Modelslim
安装步骤
使用分支 master
git clone https://gitee.com/ascend/msit.git
cd msit/msmodelslim
bash install.sh

deepseek量化
pip install transformers==4.48.2

进入目录cd /example/DeepSeek
命令 参考 msmodelslim/example/DeepSeek/README.md
执行运行前必检和DeepSeek-R1 w4a8 混合量化
参考命令：python3 quant_deepseek_w4a8.py --model_path {浮点权重路径} --save_path {W4A8量化权重路径} --layer_count 4 --mindie_format

python3 quant_deepseek_w4a8.py --model_path /mnt/nfs/DeepSeek-R1-BF16 --save_path /mnt/nfs/w4a8_4_layer_new --layer_count 4 --mindie_format
由于mindie_format生成的是mindie格式，vllm使用还需要做些适配修改
quant_model_description_w8a8_dynamic.json 重命名为 quant_model_description.json，并在其中修改"group_size": 0"为group_size": 256的配置
config.json的修改：model_type修改为deepseek_v3; quantization_config删掉;修改hidden_layers为4
```



