# Issue #618: [Doc]: Run accuracy test according "Using lm-eval" guide with modelscope source, errors take place: "has no revision: main !" and "Invalid repo_id: dataset, must be of format namespace/name""

## 基本信息

- **编号**: #618
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/618
- **创建时间**: 2025-04-22T09:32:54Z
- **关闭时间**: 2025-10-11T01:23:09Z
- **更新时间**: 2025-10-11T01:23:09Z
- **提交者**: @leo-pony
- **评论数**: 2

## 标签

documentation

## 问题描述

### 📚 The doc issue
Run accuracy test according [Using lm-eval](https://vllm-ascend.readthedocs.io/en/latest/developer_guide/evaluation/using_lm_eval.html) guide with modelscope source, errors take place:
Test command:

```
lm_eval --model vllm --model_args pretrained=Qwen/Qwen2.5-7B-Instruct,revision=master,max_model_len=4096,dtype=auto,tensor_parallel_size=1,gpu_memory_utilization=0.8 --tasks gsm8k --apply_chat_template --fewshot_as_multiturn --batch_size auto --num_fewshot 5
```

First Error:
```
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/modelscope/hub/snapshot_download.py", line 257, in _snapshot_download
[rank0]:     revision_detail = _api.get_valid_revision_detail(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/modelscope/hub/api.py", line 600, in get_valid_revision_detail
[rank0]:     raise NotExistError('The model: %s has no revision: %s !' % (model_id, revision))
[rank0]: modelscope.hub.errors.NotExistError: The model: Qwen/Qwen2.5-VL-7B-Instruct has no revision: main !
```
Second Error:
```
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/modelscope/hub/api.py", line 332, in get_endpoint_for_read
[rank0]:     if not self.repo_exists(
[rank0]:   File "/usr/local/python3.10/lib/python3.10/site-packages/modelscope/hub/api.py", line 379, in repo_exists
[rank0]:     raise Exception('Invalid repo_id: %s, must be of format namespace/name' % repo_type)
[rank0]: Exception: Invalid repo_id: dataset, must be of format namespace/name
[ERROR] 2025-04-22-08:55:47 (PID:293, Device:0, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```


### Suggest a potential alternative/fix

_No response_
