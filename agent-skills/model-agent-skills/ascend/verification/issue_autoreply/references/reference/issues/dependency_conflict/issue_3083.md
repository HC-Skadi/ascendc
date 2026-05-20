# Issue #3083: [Bug]: Fix vllm main issue (0922)

## 基本信息

- **编号**: #3083
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3083
- **创建时间**: 2025-09-22T03:39:13Z
- **关闭时间**: 2025-12-23T12:53:43Z
- **更新时间**: 2025-12-23T12:53:43Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

bug; vllm-break

## 问题描述

### Your current environment

https://github.com/vllm-project/vllm-ascend/actions/workflows/vllm_ascend_test_full_vllm_main.yaml

```
# cat ~/.cache/run_single.sh
set -ex
export VLLM_WORKER_MULTIPROC_METHOD=spawn
export VLLM_USE_MODELSCOPE=True
# export VLLM_LOGGING_LEVEL=ERROR

pytest -sv tests/e2e/singlecard/test_aclgraph.py
pytest -sv tests/e2e/singlecard/test_ascend_scheduler.py
pytest -sv tests/e2e/singlecard/test_camem.py
pytest -sv tests/e2e/singlecard/test_chunked.py
pytest -sv tests/e2e/singlecard/test_embedding.py
pytest -sv tests/e2e/singlecard/test_guided_decoding.py
#pytest -sv tests/e2e/singlecard/test_ilama_lora.py
pytest -sv tests/e2e/singlecard/test_profile_execute_duration.py
pytest -sv tests/e2e/singlecard/test_quantization.py
pytest -sv tests/e2e/singlecard/test_sampler.py
pytest -sv tests/e2e/singlecard/test_vlm.py

# ------------------------------------ v1 spec decode test ------------------------------------ #
pytest -sv tests/e2e/singlecard/spec_decode_v1/test_v1_mtp_correctness.py
pytest -sv tests/e2e/singlecard/spec_decode_v1/test_v1_mtp_torchair_correctness.py
pytest -sv tests/e2e/singlecard/spec_decode_v1/test_v1_spec_decode.py

# pytest -sv tests/e2e/singlecard/ops/
```

### 🐛 Describe the bug
0. https://github.com/vllm-project/vllm-ascend/pull/2907
- This pr bump vllm commit to https://github.com/vllm-project/vllm/commit/6d8246aaffff3ebec84767e373212a7b8da328e2
- fix upstream changes https://github.com/vllm-project/vllm/pull/24548 abort multi-modal kwargs, make vllm main and `v0.10.2` both adaptable
- fix metadata_builder changes introduced by https://github.com/vllm-project/vllm/pull/23693
- fix `structured_outputs_config` changes introduced by https://github.com/vllm-project/vllm/pull/22772
- fix `moe_config` changes introduced by https://github.com/vllm-project/vllm/pull/22537

1. Introduced by: https://github.com/vllm-project/vllm/commit/aed16879a9191a58adc5b8ac3973454dddefe018
Resolved: https://github.com/vllm-project/vllm-ascend/pull/3067

2. https://github.com/vllm-project/vllm/commit/9607d5eb449711b349d4c2bee0a9c94afcc7ed14
```
TypeError: AttentionGroup.__init__() missing 1 required positional argument: 'kv_cache_spec'
```
Resolved: https://github.com/vllm-project/vllm-ascend/pull/3070

3. https://github.com/vllm-project/vllm/commit/2821986450bc31869714885ed4203650a42f3cb0
Resolved: TBD

4.  https://github.com/vllm-project/vllm/commit/26e673fe9303ad759a47e19a087764393c69109f
``` 
VLLM_VERSION=0.10.33 ~/.cache/run_single.sh
++ export VLLM_WORKER_MULTIPROC_METHOD=spawn
++ VLLM_WORKER_MULTIPROC_METHOD=spawn
++ export VLLM_USE_MODELSCOPE=True
++ VLLM_USE_MODELSCOPE=True
++ pytest -sv tests/e2e/singlecard/test_aclgraph.py
ImportError while loading conftest '/vllm-workspace/vllm-ascend/tests/e2e/conftest.py'.
tests/e2e/conftest.py:47: in <module>
    from tests.e2e.model_utils import (TokensTextLogprobs,
tests/e2e/model_utils.py:22: in <module>
    from vllm.sequence import PromptLogprobs, SampleLogprobs
E   ImportError: cannot import name 'PromptLogprobs' from 'vllm.sequence' (/vllm-workspace/vllm/vllm/sequence.py)
```
```diff
diff --git a/tests/e2e/model_utils.py b/tests/e2e/model_utils.py
index 1a3ea5ba0..dec88cd0b 100644
--- a/tests/e2e/model_utils.py
+++ b/tests/e2e/model_utils.py
@@ -19,7 +19,11 @@

 from typing import Dict, List, Optional, Sequence, Tuple, Union

-from vllm.sequence import PromptLogprobs, SampleLogprobs
+from vllm_ascend.utils import vllm_version_is
+if vllm_version_is("0.10.2"):
+    from vllm.sequence import PromptLogprobs, SampleLogprobs
+else:
+    from vllm.logprobs import PromptLogprobs, SampleLogprobs

 TokensText = Tuple[List[int], str]
```

5. `AttributeError: 'SchedulerConfig' object has no attribute 'delay_factor'`
https://github.com/vllm-project/vllm/commit/0ff8ebb2d700b2e39457a661ef979b0da2ad73b3
