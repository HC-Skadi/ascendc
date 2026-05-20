# Issue #1543: [Usage]: Distributed model serving which deployed with LWS on Kubernetes

## 基本信息

- **编号**: #1543
- **状态**: closed
- **链接**: https://github.com/vllm-project/vllm-ascend/issues/1543
- **创建时间**: 2025-07-01T03:26:07Z
- **关闭时间**: 2025-12-31T02:33:19Z
- **更新时间**: 2025-12-31T02:33:19Z
- **提交者**: @zhaotyer
- **评论数**: 1

## 标签

无

## 问题描述

### Your current environment

```text
The output of above commands
```


### How would you like to use vllm on ascend

vLLM can be deployed with [LWS](https://github.com/kubernetes-sigs/lws) on Kubernetes for distributed model serving.
Does vllm-ascend support distributed model serving by lws， 
the vllm  lws template is:
```
apiVersion: leaderworkerset.x-k8s.io/v1
kind: LeaderWorkerSet
metadata:
  name: vllm
spec:
  replicas: 2
  leaderWorkerTemplate:
    size: 2
    restartPolicy: RecreateGroupOnPodRestart
    leaderTemplate:
      metadata:
        labels:
          role: leader
      spec:
        containers:
          - name: vllm-leader
            image: vllm/vllm-openai:latest
            env:
              - name: HUGGING_FACE_HUB_TOKEN
                value: <your-hf-token>
            command:
              - sh
              - -c
              - "bash /vllm-workspace/examples/online_serving/multi-node-serving.sh leader --ray_cluster_size=$(LWS_GROUP_SIZE); 
                 python3 -m vllm.entrypoints.openai.api_server --port 8001 --model meta-llama/Meta-Llama-3.1-405B-Instruct --tensor-parallel-size 8 --pipeline_parallel_size 2"
            resources:
              limits:
                nvidia.com/gpu: "8"
                memory: 1124Gi
                ephemeral-storage: 800Gi
              requests:
                ephemeral-storage: 800Gi
                cpu: 125
            ports:
              - containerPort: 8001
            readinessProbe:
              tcpSocket:
                port: 8001
              initialDelaySeconds: 15
              periodSeconds: 10
            volumeMounts:
              - mountPath: /dev/shm
                name: dshm
        volumes:
        - name: dshm
          emptyDir:
            medium: Memory
            sizeLimit: 15Gi
    workerTemplate:
      spec:
        containers:
          - name: vllm-worker
            image: vllm/vllm-openai:latest
            command:
              - sh
              - -c
              - "bash /vllm-workspace/examples/online_serving/multi-node-serving.sh worker --ray_address=$(LWS_LEADER_ADDRESS)"
            resources:
              limits:
                nvidia.com/gpu: "8"
                memory: 1124Gi
                ephemeral-storage: 800Gi
              requests:
                ephemeral-storage: 800Gi
                cpu: 125
            env:
              - name: HUGGING_FACE_HUB_TOKEN
                value: <your-hf-token>
            volumeMounts:
              - mountPath: /dev/shm
                name: dshm   
        volumes:
        - name: dshm
          emptyDir:
            medium: Memory
            sizeLimit: 15Gi

```
vllm-ascend must set:
```
export HCCL_IF_IP={local_ip}
export GLOO_SOCKET_IFNAME=bond1
export TP_SOCKET_IFNAME=bond1
export HCCL_SOCKET_IFNAME=bond1 
```
I'm not sure if these are still needed for lws deployment because I don't have enough cards to verify
