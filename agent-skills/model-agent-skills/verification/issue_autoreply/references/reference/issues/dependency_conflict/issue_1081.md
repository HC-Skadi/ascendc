# Issue #1081: [Bug]: qwen2.5vl72b+v1部分情况乱码

## 基本信息

- **编号**: #1081
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1081
- **创建时间**: 2025-06-05T08:16:07Z
- **关闭时间**: 2025-07-16T07:01:52Z
- **更新时间**: 2025-09-12T12:17:09Z
- **提交者**: @lfx777
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

torch2.5.1
cann8.0.rc1
vllm main 
vllm asecnd https://github.com/vllm-project/vllm-ascend/pull/736

### 🐛 Describe the bug

基于https://github.com/vllm-project/vllm-ascend/pull/736

的pr测试
在v1模式下，测试qwen2.5vl72b出现乱码

测试1：小图片推理正常，分辨率300到400
测试2：大图片推理第一次异常，第二次正常。换另一张大图片一样，在同一个服务拉起测试。图片分辨率3K*1K，4k*3K
测试3：修改权重下preprocessor_config.json的max_pixels，改小后均正常

复现：
拉起服务
```
ASCEND_RT_VISIBLE_DEVICES=0,1,2,3 VLLM_USE_V1=1 VLLM_WORKER_MULTIPROC_METHOD=spawn python -m vllm.entrypoints.openai.api_server --model /home/xxx/weights/Qwen2.5-VL-72B-Instruct --max-num-seqs=256 --max-model-len=32768 --tensor-parallel-size=4 --block-size=128 --dtype bfloat16 --host=127.0.0.1 --port=8000 --gpu-memory-utilization=0.9 --trust-remote-code

```
测试脚本，分别用大图片和小图片
```

import base64
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--port', default='8001', type=str)
args = parser.parse_args()

image_path = f"./cat.jpg"

api_url = f"http://localhost:{args.port}/v1/chat/completions"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def run_inference():
    image_base64 = encode_image(image_path)

    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "model": "/home/xxx/weights/Qwen2.5-VL-72B-Instruct",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "请详细描述这张图片"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 64,
        "temperature": 0,
        "stream": False
    }

    response = requests.post(api_url, headers=headers, json=payload)
    try:
        output = response.json()
        print(f"输出内容: {output['choices'][0]['message']['content']}")
    except:
        print("解析响应失败:", response.text)


if __name__ == "__main__":
    for i in range(1):
        run_inference()


```
修改preprocessor_config.json的max_pixels成1003520，再次测试正常
