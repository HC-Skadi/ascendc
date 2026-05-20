# Issue #1364: [Bug]: The inference process hangs when launched via Ray, identified as an issue in the from_engine_args function of the AsyncLLM class.

## 基本信息

- **编号**: #1364
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1364
- **创建时间**: 2025-06-23T06:23:34Z
- **关闭时间**: 2025-06-24T00:34:19Z
- **更新时间**: 2025-06-24T00:34:19Z
- **提交者**: @zhenjie521
- **评论数**: 2

## 标签

bug

## 问题描述

### Your current environment

<details>
import httpx
import io
import json
import torch
import asyncio

class CriticClient:
    def __init__(self):
        self.ep_ips = ["175.100.2.5"]
        self.ep_ports = [61000]
        self.timeout = 180
    def wait_until_sampler_server_is_ready(self):
        for ep_ip, ep_port in zip(self.ep_ips, self.ep_ports, strict=True):
            print("NNNNNNNNNNN",self.ep_ports)
            with httpx.Client() as cli:
                print(f'http://{ep_ip}:{ep_port}/heartbeat')
                url = f'http://{ep_ip}:{ep_port}/heartbeat'
                while True:
                    try:
                        resp = cli.get(url)
                        break
                    except httpx.HTTPError as e:
                        print(f"wait_until_sampler_server_is_ready {ep_ip=} {ep_port=}", flush=True)
                        time.sleep(15)

    def setup(self):
        import pdb; pdb.set_trace()
        print("正在初始化 Critic 客户端连接...")
        async def rpc_co(ep_ip, ep_port):
            url = f'http://{ep_ip}:{ep_port}/setup'
            send_data = json.dumps({})
            print(">>>>>>>>>>>>>>>>send_data<<<<<<<<<<<<<<<<<<<",send_data)
            async with httpx.AsyncClient() as cli:
                while True:
                    try:
                        print(">>>>>>>>>>>>>>>>cli<<<<<<<<<<<<<<<<<<<",ep_port)
                        resp = await cli.post(url, content=send_data, timeout=self.timeout)
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        return resp
                    except httpx.HTTPError as e:
                        print(f"连接失败，{ep_ip}:{ep_port}:{e}  不可用，15秒后重试...")
                        await asyncio.sleep(15)

        async def co():
            rpc_cos = []
            for ep_ip, ep_port in zip(self.ep_ips, self.ep_ports, strict=True):
                rpc_cos.append(rpc_co(ep_ip, ep_port))
            return await asyncio.gather(*rpc_cos)

        asyncio.run(co())
        print("Critic 客户端初始化完成")

    def sleep(self):
        print("正在发送休眠请求...")
        async def rpc_co(ep_ip, ep_port):
            url = f'http://{ep_ip}:{ep_port}/sleep'
            async with httpx.AsyncClient() as cli:
                while True:
                    try:
                        resp = await cli.post(url, timeout=self.timeout)
                        return resp
                    except httpx.HTTPError:
                        print(f"休眠请求失败，{ep_ip}:{ep_port} 不可用，15秒后重试...")
                        await asyncio.sleep(15)

        async def co():
            rpc_cos = []
            for ep_ip, ep_port in zip(self.ep_ips, self.ep_ports, strict=True):
                rpc_cos.append(rpc_co(ep_ip, ep_port))
            return await asyncio.gather(*rpc_cos)

        asyncio.run(co())
        print("休眠请求已发送")

    async def get_infer_rm_critic_result(self, ppo_step=0, sample_idx=0):
        print(f"正在获取推理结果 (ppo_step={ppo_step}, sample_idx={sample_idx})...")
        ep_idx = 0
        ep_ip = self.ep_ips[ep_idx]
        ep_port = self.ep_ports[ep_idx]

        send_data = {
            'actor_dp_rank': 0,
            'ppo_step': ppo_step,
            'sample_idx': sample_idx,
        }
        fio = io.BytesIO()
        torch.save(send_data, fio)
        send_data = fio.getvalue()

        async with httpx.AsyncClient() as cli:
            url = f'http://{ep_ip}:{ep_port}/get_infer_rm_critic_result'
            while True:
                try:
                    resp = await cli.post(url, content=send_data, timeout=self.timeout)
                    resp = torch.load(io.BytesIO(resp.content), weights_only=False)
                    if not resp['ready']:
                        print(f"结果未准备好，{ep_ip}:{ep_port}，10秒后重试...")
                        await asyncio.sleep(10)
                    else:
                        print(f"推理结果获取成功 (ppo_step={ppo_step}, sample_idx={sample_idx})")
                        return resp
                except httpx.HTTPError as e:
                    print(f"请求失败: {str(e)}，10秒后重试...")
                    await asyncio.sleep(10)

if __name__ == "__main__":
    
    print("=== 启动 Critic 客户端 ===")
    critic_client = CriticClient()
    print("=== heatlth ===")
    critic_client.wait_until_sampler_server_is_ready()
    print("=== setup ===")
    critic_client.setup()
    print("=== sleep ===")
    critic_client.sleep()
    result = asyncio.run(critic_client.get_infer_rm_critic_result())
    print("=== 任务完成 ===")
    print(f"最终结果: {result}")

The current issue is with resp = await cli.post(url, content=send_data, timeout=self.timeout) in critic_client.setup()，After troubleshooting, it is found that the from_engine_args function in the AsyncLLM class of the v1/engine/async_llm.py file of the vllm library is blocked
```text
Your output of above commands here
```

</details>


### 🐛 Describe the bug

The screenshot is：

![Image](https://github.com/user-attachments/assets/cd373e64-9e3c-41f5-97bb-d877062d15a2)

The invocation relationship is if infer_engine_impl == 'vllm':
            print("----------------vllm------------------------------")
            engine_args = AsyncEngineArgs(
                model=model,
                dtype=dtype,
                distributed_executor_backend=distributed_executor_backend,
                tensor_parallel_size=tensor_parallel_size,
                pipeline_parallel_size=pipeline_parallel_size,
                gpu_memory_utilization=gpu_memory_utilization,
                enforce_eager=enforce_eager,
                trust_remote_code=True,
                enable_sleep_mode=True,
            )
            print("----------------infer_engine-----start-------------------------")
            infer_engine = AsyncLLM.from_engine_args(engine_args)
            print("----------------infer_engine------end------------------------")

The current environment ：
vllm 0.8.5post1
vllm-ascend  0.8.5rc1
torch 2.5.1
torch_npu 2.5.1
megatron core_0.12.1
CANN 8.1.RC1
