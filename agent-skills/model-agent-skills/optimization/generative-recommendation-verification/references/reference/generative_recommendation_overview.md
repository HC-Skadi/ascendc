# 探索无限可能：生成式推荐的演进、前沿与挑战

> 来源：https://zhuanlan.zhihu.com/p/1915425008597079412  
> 作者：京东零售技术  
> 转载自CSDN（内容相同）

## TL;DR

过去一年间，生成式推荐取得了长足的实质性进展，特别是在凭借大型语言模型强大的序列建模与推理能力提升整体推荐性能方面。基于LLM（Large Language Models, LLMs）的生成式推荐（Generative Recommendations, GRs）正逐步形成一种区别于判别式推荐的新范式，展现出替代依赖复杂手工特征的传统推荐系统的强大潜力。

## 一、引言：传统推荐的困境与LLM的破局

### 传统推荐范式的瓶颈

传统推荐范式（MLR和DLR），侧重于基于手工特征工程和复杂的级联建模结构来预测相似性或排序分数：

- **MLR**：主要依赖传统的机器学习算法，通常建立在显式的特征工程之上
- **DLR**：主要利用深度神经网络的力量，直接从原始或稀疏特征中自动学习复杂的非线性表示

一线算法工程师普遍面临困境：**简单地增加一些特征或扩大现有模型规模，并不能带来预期的效果提升**

深层次原因：
- **特征工程依赖**：成熟业务特征工程"矿山"基本被挖掘殆尽
- **模型工程天花板**：现有架构无法有效建模"世界知识"、"用户意图Reasoning"
- **级联架构导致误差放大**：召回-粗排-精排-重排，算法目标被分散，出现目标割裂和误差传播

### LLM的颠覆性潜力

- **长序列建模强化**：将用户行为视作时序信号，通过自回归预测捕捉复杂依赖
- **世界知识注入**：LLM/VLM预训练语料蕴含跨领域、多模态知识
- **端到端生成**：单一模型直接输出排序列表，消除级联误差

**范式变革的本质：从"预测相似性"到"推理用户需求"**

### 为什么是现在？

1. **LLM生态成熟**：分布式训练框架、FlashAttention/PagedAttention推理优化
2. **工业级验证**：Meta GR、美团MTGR、百度COBRA、字节RankMixer、快手OneRec等

## 二、技术演进：从模块化到端到端的生成式架构

### 2.1 LLM4Rec：技术探索前夜

三种探索范式：
1. **LLM Embeddings + RS**：将LLM作为特征抽取器
2. **LLM Tokens + RS**：生成特定标识符（Token）
3. **LLM as RS**：直接作为推荐系统核心

### 2.2 生成式推荐Online应用范式

1. **与传统级联系统的相应模块协作或模块替换**
   - 召回策略：Google TIGER
   - 精排模型：Meta GR

2. **直接应用生成模型进行端到端推荐**
   - 召排一体：快手OneRec

### 2.3 GRs核心技术要点

#### 2.3.1 判别式->生成式的转变

**判别式推荐**：给定用户、物品和上下文特征，模型预估用户喜欢物品的概率

**生成式推荐**：利用用户的行为历史序列，基于生成式模型的结构，在无输入候选的情况下直接生成若干用户最有可能交互的物品

#### 2.3.2 Google TIGER：召回阶段用自回归生成式模型

- **核心价值**：首次将自回归生成引入召回阶段，通过语义ID压缩Item空间
- **模型**：基于Transformer的T5模型
- **输入输出**：均为语义ID序列（Semantic ID Sequence）
- **自回归生成过程**：Transformer解码器块计算隐状态，与全库词嵌入计算logits，再进行TopK采样

#### 2.3.3 Meta GR：精排阶段发现Scaling Law

- **模型架构**：提出HSTU（Hierarchical Sequential Transduction Units）
- **性能提升**：比FlashAttention2-based Transformers快5.3x-15.2x
- **推理优化**：M-FALCON，通过微批处理完全分摊计算成本
- **Scaling Law**：模型参数量高达万亿，计算量提升1000x

**HSTU是本skill验证的核心架构**

### 2.3.2 基于语义ID的生成

**为什么语义ID这么受青睐？**
- 自回归生成需与整个Vocab Embedding计算
- 大语言模型Vocab约15万Token
- 京东40亿商品需压缩Vocab Embedding规模

**语义ID（Semantic ID）**：
- 通过将十亿级稀疏Item ID抽象为万级别语义表示
- 将item参数体量与LLM的Vocab Embedding对齐
- 使自回归生成的logits计算开销降低99.9%

**语义ID的生成过程**：
1. Item提取Embedding，再量化成语义ID（RQ-VAE或RQ-Kmeans）
2. Next语义ID生成预测（Beam Search）

### 2.3.3 稀疏特征依然很重要

- Meta GR效果难以复现：特征工程简化太厉害
- **美团MTGR**：保留全部DLRM原始特征
- **快手OneRec V2**：输入改为稀疏ID特征（而非Semantic ID）

### 2.3.4 Encoder-Decoder vs Decoder-Only

| 架构 | 应用 | 特点 |
|------|------|------|
| Encoder-Decoder | Google TIGER、快手OneRec | T5结构，Cross Attention |
| Decoder-Only | LLM（Llama、Qwen、DeepSeek） | Fully Visible Cross Attention |

当前阶段，T5 Encoder-Decoder架构在处理长用户行为序列上效果可能更优。

## 三、工程攻坚：主要考量和挑战

### 3.1 LLM/DLRM/GRs异同点

| 维度 | DLRM | LLM | GRs |
|------|------|-----|-----|
| Feature Engineering | ID化、分桶、交叉组合 | Tokenizer | Tokenizer/DeTokenizer |
| Feature Store | 100G~10T | Vocab M级 | 十GB级 |
| Embedding | 10G~1TB稀疏参数 | <10G | GB级 |
| Model | 几十M Dense | 1B~1T | 0.1B~10B |
| 生成方式 | Point-wise Scoring | Autoregressive | Autoregressive |

### 3.2 生成式推荐GRs的发展趋势

三个技术象限：
1. **Sparse Scaling Up**：10TB级Embedding的秒级流式更新
2. **Dense Scaling Up**：MoE结构达到10B参数规模
3. **Generation Paradigm**：MTP并行解码、Diffusion并行生成

### 3.3 推理性能瓶颈

- 推荐系统在线链路时延要求：百毫秒级别
- 用户流量：几万~几十万QPS

**核心挑战**：
1. 用户行为序列的高效生产、存储与查询
2. 生成式推理优化
3. 模型架构革新（O(N²) → O(N)）

## 四、未来方向

- **从"生成"到"深度推理"（Reasoning）**
- **奖励机制的前沿探索**
- **真正的多模态对齐**
- **并行生成优化**（MTP、Diffusion Models）
- **全链路联动与决策**

## 五、结语

生成式推荐并非简单的渐进式优化，而是推荐系统的一次认知升维：
- 突破天花板：Scaling Law拓展性能边界
- 重构价值链：从"猜你喜欢"走向"懂你所想"

---

## 附录参考

- Google TIGER: https://arxiv.org/pdf/2305.05065
- Meta GR: https://arxiv.org/abs/2402.17152
- 美团MTGR: https://zhuanlan.zhihu.com/p/1906722156563394693
- 百度COBRA: https://arxiv.org/abs/2503.02453
- 快手OneRec: https://arxiv.org/abs/2506.13695
- 百度GRAB: https://mp.weixin.qq.com/s/mT8DmHzgc3ag57PVMqZ3Rw
- 字节RankMixer: https://www.arxiv.org/abs/2507.15551
