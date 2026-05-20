# Issue #857: [Guide]: How to use disaggregated_prefill

## 基本信息

- **编号**: #857
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/857
- **创建时间**: 2025-05-14T07:24:16Z
- **关闭时间**: 2025-06-15T07:52:56Z
- **更新时间**: 2025-06-15T07:52:56Z
- **提交者**: @Potabk
- **评论数**: 1

## 标签

guide

## 问题描述

### Your current environment

```text
The output of above commands
```


### How would you like to use vllm on ascend

I want to run inference of with the feature `disaggregated_prefill`. How to ?
## Run offline inference with docker
for now, vllm-ascend's `PD separation` is based on [llm_datadist](https://www.hiascend.com/document/detail/zh/canncommercial/80RC2/apiref/llmdatadist/llm_python_005.html), should get npu chip's ip in advance by `hccn_tool`, so plz note the [hccn_tool](https://support.huawei.com/enterprise/zh/doc/EDOC1100388691/7ea8eb00?idPath=23710424|251366513|22892968|252309113|250702818) binary executable files mounted

- docker run
```bash
# note: should mont -v /usr/local/Ascend/driver/tools/hccn_tool:/usr/local/Ascend/driver/tools/hccn_tool
export IMAGE=m.daocloud.io/quay.io/ascend/vllm-ascend:main
docker run --rm \
--name disaggregeted_prefill \
--device /dev/davinci3 \
--device /dev/davinci7 \
--device /dev/davinci_manager \
--device /dev/devmm_svm \
--device /dev/hisi_hdc \
-v /usr/local/dcmi:/usr/local/dcmi \
-v /usr/local/Ascend/driver/tools/hccn_tool:/usr/local/Ascend/driver/tools/hccn_tool \
-v /usr/local/bin/npu-smi:/usr/local/bin/npu-smi \
-v /usr/local/Ascend/driver/lib64/:/usr/local/Ascend/driver/lib64/ \
-v /usr/local/Ascend/driver/version.info:/usr/local/Ascend/driver/version.info \
-v /etc/ascend_install.info:/etc/ascend_install.info \
-v /root/.cache:/root/.cache \
-it $IMAGE bash
```
- append `hccn_tool` path to the sys path
```bash
export PATH=/usr/local/Ascend/driver/tools/:$PATH
```
- get npu chip you use
```bash
# if multi npu is in using, should get them all
hccn_tool -i {device_num} -ip -g
```

- run inference
referring to https://github.com/vllm-project/vllm-ascend/blob/main/examples/disaggregated_prefill/disaggregated_prefill_offline.py
```python
import multiprocessing as mp
import os
import time
from multiprocessing import Event, Process

kv_connector_extra_config = {
    # replace with your npu ip got from hccn_tool
    "prompt_device_ips": ["1.1.1.1"],
    "decode_device_ips": ["1.1.1.1"],
    "llmdatadist_comm_port": 26000,
}


def clean_up():
    import gc

    import torch
    from vllm.distributed.parallel_state import (
        destroy_distributed_environment, destroy_model_parallel)
    destroy_model_parallel()
    destroy_distributed_environment()
    gc.collect()
    torch.npu.empty_cache()


def run_prefill(prefill_done, process_close):
    os.environ["ASCEND_RT_VISIBLE_DEVICES"] = "0"

    from vllm import LLM, SamplingParams
    from vllm.config import KVTransferConfig

    prompts = [
        "Hello, how are you today?", "Hi, what is your name?",
        "Tell me a very long story.", "what is your favourite book?"
    ]
    sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=1)

    ktc = KVTransferConfig.from_cli(
        '{"kv_connector":"AscendSimpleConnector","kv_buffer_device":"npu","kv_role":"kv_producer", "kv_parallel_size":2}'
    )
    global kv_connector_extra_config
    ktc.kv_connector_extra_config = kv_connector_extra_config
    llm = LLM(model="deepseek-ai/DeepSeek-V2-Lite",
              kv_transfer_config=ktc,
              max_model_len=2000,
              gpu_memory_utilization=0.8,
              tensor_parallel_size=1,
              trust_remote_code=True)

    llm.generate(prompts, sampling_params)
    print("Prefill node is finished.")
    prefill_done.set()

    # To keep the prefill node running in case the decode node is not done;
    # otherwise, the script might exit prematurely, causing incomplete decoding.
    try:
        while not process_close.is_set():
            time.sleep(1)
    except KeyboardInterrupt:
        print("Script stopped by user.")
    finally:
        print("Cleanup prefill resources")
        del llm
        clean_up()


def run_decode(prefill_done):
    os.environ["ASCEND_RT_VISIBLE_DEVICES"] = "1"

    from vllm import LLM, SamplingParams
    from vllm.config import KVTransferConfig

    prompts = [
        "Hello, how are you today?",
        "Hi, what is your name?",
    ]
    sampling_params = SamplingParams(temperature=0, top_p=0.95)

    ktc = KVTransferConfig.from_cli(
        '{"kv_connector":"AscendSimpleConnector","kv_buffer_device":"npu","kv_role":"kv_consumer","kv_parallel_size":2}'
    )
    global kv_connector_extra_config
    ktc.kv_connector_extra_config = kv_connector_extra_config
    llm = LLM(model="deepseek-ai/DeepSeek-V2-Lite",
              kv_transfer_config=ktc,
              max_model_len=2000,
              gpu_memory_utilization=0.8,
              tensor_parallel_size=1,
              trust_remote_code=True)

    # Wait for the producer to start the consumer
    print("Waiting for prefill node to finish...")
    prefill_done.wait()

    # At this point when the prefill_done is set, the kv-cache should have been
    # transferred to this decode node, so we can start decoding.
    outputs = llm.generate(prompts, sampling_params)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")

    del llm
    clean_up()


if __name__ == "__main__":
    mp.get_context('spawn')

    prefill_done = Event()
    process_close = Event()
    prefill_process = Process(target=run_prefill,
                              args=(
                                  prefill_done,
                                  process_close,
                              ))
    decode_process = Process(target=run_decode, args=(prefill_done, ))

    # Start prefill node
    prefill_process.start()

    # Start decode node
    decode_process.start()

    # Terminate the prefill node when decode is finished
    decode_process.join()

    # Terminate prefill process
    process_close.set()
    prefill_process.join()
    prefill_process.terminate()
    print("All process done!")
```


