# Issue #3052: [Bug]: Many redundant `Forward context is None, skipping the operation.` print

## 基本信息

- **编号**: #3052
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/3052
- **创建时间**: 2025-09-20T02:23:54Z
- **关闭时间**: 2025-12-23T12:52:50Z
- **更新时间**: 2025-12-23T12:52:50Z
- **提交者**: @Yikun
- **评论数**: 1

## 标签

bug

## 问题描述

### Your current environment

https://productionresultssa0.blob.core.windows.net/actions-results/1f17fc73-2303-4202-b6fb-bad0a0692e3a/workflow-job-run-f3dd521e-e738-56d1-b05f-548fa09b9433/logs/job/job-logs.txt?rsct=text%2Fplain&se=2025-09-20T02%3A26%3A16Z&sig=YB3e4HKX%2Bj7hGfZXc30ZudDtGJn%2FqBQarBaJPwelgEk%3D&ske=2025-09-20T11%3A11%3A09Z&skoid=ca7593d4-ee42-46cd-af88-8b886a2f84eb&sks=b&skt=2025-09-19T23%3A11%3A09Z&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skv=2025-11-05&sp=r&spr=https&sr=b&st=2025-09-20T02%3A16%3A11Z&sv=2025-11-05

```
025-09-19T19:19:47.8429278Z [1;36m(APIServer pid=4183)[0;0m INFO:     127.0.0.1:33688 - "POST /v1/chat/completions HTTP/1.1" 200 OK
2025-09-19T19:19:48.9537740Z [1;36m(APIServer pid=4183)[0;0m 2025-09-19 19:19:48,953 - modelscope - INFO - Target directory already exists, skipping creation.
2025-09-19T19:19:53.1652840Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1654529Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1678698Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1680643Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1699172Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1700767Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1713993Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1715585Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1728845Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1730409Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1743736Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1745288Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1759320Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1760934Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1774083Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1775641Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1789421Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1791018Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1804141Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1806043Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1819158Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1820749Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1834582Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1836194Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1849344Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1850922Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1864098Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1865654Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1879277Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1880843Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1894015Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1895593Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1909087Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1910631Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1923733Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1925286Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1938811Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1940657Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1954111Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1955676Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1968835Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1970381Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1983443Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1985072Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.1998481Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2000019Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2013197Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2014741Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2028097Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2029870Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2043203Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2044780Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2058089Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2059653Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2073011Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2074923Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2087651Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2089228Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2102399Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2103967Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2117415Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2118983Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2132270Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:53.2133873Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:53.3929736Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:53 [acl_graph.py:184] Replaying aclgraph
2025-09-19T19:19:55.9182571Z 
2025-09-19T19:19:55.9182895Z  |          | 00:09 elapsed, 1481:29:02 remaining
2025-09-19T19:19:55.9184553Z Initial test run completed. Starting main benchmark run...
2025-09-19T19:19:55.9185212Z Traffic request rate: 1.0
2025-09-19T19:19:55.9185737Z Burstiness factor: 1.0 (Poisson process)
2025-09-19T19:19:55.9186129Z 
2025-09-19T19:19:55.9186337Z Maximum request concurrency: None
2025-09-19T19:19:56.7442651Z [1;36m(APIServer pid=4183)[0;0m Downloading Model from https://www.modelscope.cn to directory: /github/home/.cache/modelscope/hub/models/Qwen/Qwen2.5-VL-7B-Instruct
2025-09-19T19:19:56.7444354Z [1;36m(APIServer pid=4183)[0;0m INFO:     127.0.0.1:33688 - "POST /v1/chat/completions HTTP/1.1" 200 OK
2025-09-19T19:19:58.1004593Z [1;36m(APIServer pid=4183)[0;0m INFO:     127.0.0.1:36502 - "POST /v1/chat/completions HTTP/1.1" 200 OK
2025-09-19T19:19:58.1896398Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.1898056Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.1913800Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.1915408Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.1928755Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.1930640Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.1944134Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.1945754Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.1959706Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.1961293Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.1974855Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.1976423Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.1990126Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.1991680Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2005142Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2006742Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2020569Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2022150Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2035722Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2037283Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2050756Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2052406Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2065916Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2067644Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2081424Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2083095Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2096556Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2098173Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2111941Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2113491Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2127058Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2128659Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2142078Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2143657Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2157576Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2159147Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2172417Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2173974Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2187525Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2189330Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2202724Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2204587Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2217607Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2219823Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2232673Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2234278Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2249228Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2251732Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2268587Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2270583Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2286733Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2288709Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2304347Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2306322Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2321791Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2323784Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2338997Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2340964Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2356449Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2358454Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2374022Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2375923Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2391816Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:58.2393791Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:58 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:58.9511972Z [1;36m(APIServer pid=4183)[0;0m INFO:     127.0.0.1:54518 - "POST /v1/chat/completions HTTP/1.1" 200 OK
2025-09-19T19:19:59.0222809Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0224850Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0240168Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0241737Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0254777Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0256315Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0269697Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0271295Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0284548Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0286132Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0299355Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0300901Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0314105Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0315672Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0328622Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0330213Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0343144Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0344690Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0357807Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0359772Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0372406Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0373960Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0387017Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0388692Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0401864Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0403417Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0417017Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0418602Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0431713Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0433284Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0446307Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0447850Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0460986Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0462529Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0475902Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0477434Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0490701Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0492244Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0507377Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0509442Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0522334Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0523920Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0536746Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0538300Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0551711Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0553286Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0566289Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0567852Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0581075Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0582819Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0596306Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0597904Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0610642Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0612378Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0625376Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0626919Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0640278Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0641845Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0654935Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0656471Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0669926Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0671489Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0684646Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.0686193Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.7129098Z   0%|          | 0/200 [00:00<?, ?it/s]
2025-09-19T19:19:59.7500150Z [1;36m(APIServer pid=4183)[0;0m INFO:     127.0.0.1:33688 - "POST /v1/chat/completions HTTP/1.1" 200 OK
2025-09-19T19:19:59.8388477Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8390096Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8404924Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8407068Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8419475Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8421043Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8434385Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8435916Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8448810Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8450374Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8463890Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8465474Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8478587Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8480161Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8492986Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8494551Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8507585Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8509564Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8524791Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8526367Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8539456Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8541044Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8554456Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8556016Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8569001Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8570548Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8583525Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8585079Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8598525Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8600078Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:139] Forward context is None, skipping the operation.
2025-09-19T19:19:59.8613044Z [1;36m(EngineCore_DP0 pid=4534)[0;0m INFO 09-19 19:19:59 [register_custom_ops.py:109] Forward context is None, skipping the operation.
```

### 🐛 Describe the bug

https://productionresultssa0.blob.core.windows.net/actions-results/1f17fc73-2303-4202-b6fb-bad0a0692e3a/workflow-job-run-f3dd521e-e738-56d1-b05f-548fa09b9433/logs/job/job-logs.txt?rsct=text%2Fplain&se=2025-09-20T02%3A26%3A16Z&sig=YB3e4HKX%2Bj7hGfZXc30ZudDtGJn%2FqBQarBaJPwelgEk%3D&ske=2025-09-20T11%3A11%3A09Z&skoid=ca7593d4-ee42-46cd-af88-8b886a2f84eb&sks=b&skt=2025-09-19T23%3A11%3A09Z&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skv=2025-11-05&sp=r&spr=https&sr=b&st=2025-09-20T02%3A16%3A11Z&sv=2025-11-05
