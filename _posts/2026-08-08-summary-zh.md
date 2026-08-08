---
layout: default
title: "Horizon Summary: 2026-08-08 (ZH)"
date: 2026-08-08
lang: zh
---

> From 26 items, 12 important content pieces were selected

---

1. [SGLang v0.5.17 发布，增强大型语言模型服务能力](#item-1) ⭐️ 9.0/10
2. [DeepSeek V4 Flash 0731](#item-2) ⭐️ 9.0/10
3. [Assembly Hall of Shame](#item-3) ⭐️ 8.0/10
4. [What happens if an entire class of workers loses faith in their careers](#item-4) ⭐️ 8.0/10
5. [Oracle bans AI-generated code from OpenJDK](#item-5) ⭐️ 8.0/10
6. [🤖 OpenAI 首曝 ChatGPT 全球国别数据：AI 从问答走向干活](#item-6) ⭐️ 8.0/10
7. [亚马逊整顿内部 CPU 浪费，智能体 AI 推高算力需求](#item-7) ⭐️ 8.0/10
8. [🤖 爆料：OpenAI 拟下周发布新模型 Astra  有爆料称，OpenAI 正准备发布名为 Astra 的新模型，目标时间为下周。](#item-8) ⭐️ 8.0/10
9. [微软 Edge 将淘汰旧版广告拦截器，uBlock Origin 再失阵地](#item-9) ⭐️ 8.0/10
10. [datasette 0.65.3](#item-10) ⭐️ 7.0/10
11. [Simon Willison on Technical Blogging](#item-11) ⭐️ 7.0/10
12. [纳斯达克申请将交易时间延长至 23 小时  美国纳斯达克交易所 12 月 15 日向证券交易委员会（SEC）申请增加交易时段，拟从东部时间晚上 9 时至次日凌晨](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.17 发布，增强大型语言模型服务能力](https://github.com/sgl-project/sglang/releases/tag/v0.5.17) ⭐️ 9.0/10

SGLang v0.5.17 已发布，引入了先进的服务能力，包括对假设的 Kimi K3 多模态模型（2.8T 参数，1M 上下文）和 MiniMax-H3 视频生成模型的“零日支持”。此版本集成了 DSpark 推测解码、分布式推理策略（DCP, DWDP）以及 KDA 感知前缀缓存等功能。 此次发布意义重大，它展示了 SGLang 在大型语言模型推理和分布式系统方面的尖端工程能力，推动了服务超大规模、复杂多模态模型的效率极限。这些优化对于使未来如 Kimi K3 般庞大的 AI 模型在实际应用中变得可行且高性能至关重要。 Kimi K3 支持利用了具有 896 个专家和 KDA 线性注意力层的 LatentMoE 架构，通过 DCP、DSpark 推测解码和分块预填充并行技术提供服务。MiniMax-H3 支持实现了文本到视频和音频以及参考条件任务的原生服务，并在 NVIDIA B200/H100 和 RTX 5090 GPU 上进行了验证。

github · Fridge003 · Aug 8, 00:19

**背景**: 推测解码是一种大型语言模型优化技术，它利用一个更小、更快的草稿模型提前预测多个 token，然后由更大的目标模型进行验证，从而显著加快推理速度。LatentMoE（专家混合）是一种模型架构，它在将 token 路由到专家之前，将其投影到一个更小的潜在维度，旨在通过减少内存带宽和通信瓶颈来优化每 FLOP 和每参数的准确性。KDA（Kimi Delta Attention）是一种高效的线性注意力机制，它通过通道级门控增强 RNN 建模能力，并减少 KV 缓存使用，从而提高解码速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llminfo.tech/posts/1hzew4v/">ollama短期内不会有 推 测 解 码 ，有替代方案吗？ | LLM Info</a></li>
<li><a href="https://arxiv.org/abs/2601.18089">[2601.18089] LatentMoE: Toward Optimal Accuracy per FLOP and ... GitHub - kyegomez/Latent-MoE: Implementation of LatentMoE ... Images LatentMoE：Kimi K3 背后的 MoE 高效变体 | Oilbeater 的自习室 最新大模型的新架构-Latent MoE - 知乎 从kimi k3看下一代 MoE 架构的转折点：潜在 MoE - 知乎 LatentMoE: Toward Optimal Accuracy per FLOP and Parameter in ...</a></li>
<li><a href="https://blog.csdn.net/weixin_42744466/article/details/154196690">【AI-Infra】KIMI-Linear论文解读：超越MLA!超高效的线性注意力机制</a></li>

</ul>
</details>

**标签**: `#LLM Serving`, `#Multimodal AI`, `#Distributed Inference`, `#Speculative Decoding`, `#Large Language Models`

---

<a id="item-2"></a>
## [DeepSeek V4 Flash 0731](https://arcprize.org/results/deepseek-v4-flash-0731) ⭐️ 9.0/10

DeepSeek V4 Flash 0731 is a new, highly capable, and cost-effective large language model, praised by users for its significant performance improvements and speed, making it suitable for extensive use in various applications.

hackernews · tosh · Aug 7, 17:56

**标签**: `#LLM`, `#Model Performance`, `#Cost Efficiency`, `#Generative AI`, `#AI Development`

---

<a id="item-3"></a>
## [Assembly Hall of Shame](https://github.com/xoreaxeaxeax/asm-hall-of-shame) ⭐️ 8.0/10

一个 GitHub 仓库，收录了极其缓慢或低效的汇编指令，作为低级系统性能和怪癖的“耻辱堂”，引发了专家之间深入的技术讨论。

hackernews · piotrgrabowski · Aug 7, 18:01

**标签**: `#Assembly Language`, `#System Internals`, `#Performance Engineering`, `#Low-level Security`, `#Hardware Interaction`

---

<a id="item-4"></a>
## [What happens if an entire class of workers loses faith in their careers](https://www.noemamag.com/why-is-everyone-in-tech-so-sad/) ⭐️ 8.0/10

这篇文章探讨了科技行业工作者日益增长的职业倦怠现象，分析了其原因以及对个人和行业可能产生的长期影响。

hackernews · RickJWagner · Aug 7, 12:42

**标签**: `#科技行业`, `#职业发展`, `#心理健康`, `#工作文化`, `#社会学`

---

<a id="item-5"></a>
## [Oracle bans AI-generated code from OpenJDK](https://app.dealroom.co/news/feed/oracle-bans-ai-generated-code-from-openjdk-despite-ellison-s-claim-oracle-isn-t-writing-its-own-code) ⭐️ 8.0/10

Oracle has implemented an interim policy banning AI-generated code from OpenJDK contributions, citing concerns over provenance and the burden on human reviewers, sparking significant discussion within the developer community.

hackernews · delduca · Aug 7, 17:36

**标签**: `#OpenJDK`, `#AI Ethics`, `#Open Source`, `#Software Governance`, `#Legal Policy`

---

<a id="item-6"></a>
## [🤖 OpenAI 首曝 ChatGPT 全球国别数据：AI 从问答走向干活](https://openai.com/index/how-the-world-is-putting-chatgpt-to-work/) ⭐️ 8.0/10

OpenAI 发布首份 ChatGPT 全球国别使用数据，显示 AI 正从问答转向工作和生产任务，新兴市场采用率快速增长，35 岁以上用户参与度提升，多媒体成为增长最快的使用场景。

telegram · zaihuapd · Aug 7, 08:43

**标签**: `#AI Adoption`, `#ChatGPT`, `#Usage Data`, `#AI Trends`, `#Productivity Tools`

---

<a id="item-7"></a>
## [亚马逊整顿内部 CPU 浪费，智能体 AI 推高算力需求](https://www.tomshardware.com/pc-components/cpus/amazon-cracks-down-on-cpu-waste-among-engineers-as-agentic-ai-crunch-intensifies-cpu-demand-makes-low-utilization-ec2-instances-a-hot-commodity) ⭐️ 8.0/10

亚马逊 AWS 正在整顿内部 CPU 浪费，因为智能体 AI 工作负载对 CPU 的需求激增，改变了数据中心的 CPU:GPU 配比，并促使硬件厂商加大对数据中心 CPU 的投资。

telegram · zaihuapd · Aug 7, 16:31

**标签**: `#智能体AI`, `#云计算`, `#资源管理`, `#数据中心`, `#AWS`

---

<a id="item-8"></a>
## [🤖 爆料：OpenAI 拟下周发布新模型 Astra  有爆料称，OpenAI 正准备发布名为 Astra 的新模型，目标时间为下周。](https://t.me/zaihuapd/43046) ⭐️ 8.0/10

有爆料称 OpenAI 计划下周发布代号为 Astra 的全新预训练模型，据称是自 GPT-4.5 以来训练过的最大模型。

telegram · zaihuapd · Aug 7, 16:44

**标签**: `#OpenAI`, `#AI模型`, `#LLM`, `#AI发展`, `#传闻`

---

<a id="item-9"></a>
## [微软 Edge 将淘汰旧版广告拦截器，uBlock Origin 再失阵地](https://www.theverge.com/tech/976880/microsoft-edge-extensions-ad-blockers-mv2-mv3) ⭐️ 8.0/10

微软 Edge 宣布将逐步淘汰对 Manifest V2 扩展平台的支持，此举将影响 uBlock Origin 等旧版广告拦截器，并促使消费者和企业用户转向 MV3 替代品或考虑其他浏览器。

telegram · zaihuapd · Aug 8, 01:14

**标签**: `#浏览器扩展`, `#Microsoft Edge`, `#广告拦截`, `#Manifest V3`, `#网络标准`

---

<a id="item-10"></a>
## [datasette 0.65.3](https://simonwillison.net/2026/Aug/6/datasette-2/#atom-everything) ⭐️ 7.0/10

Datasette version 0.65.3 was released, back-porting a critical SQL Injection security fix from a newer alpha version.

rss · Simon Willison · Aug 6, 18:22

**标签**: `#datasette`, `#security`, `#SQL Injection`, `#software update`, `#vulnerability`

---

<a id="item-11"></a>
## [Simon Willison on Technical Blogging](https://simonwillison.net/2026/Aug/6/simon-willison-on-technical-blogging/#atom-everything) ⭐️ 7.0/10

Simon Willison 在一次采访中分享了他关于技术博客的经验和建议，包括开始博客的原因、最自豪的帖子以及给初学者的实用技巧，其中最重要的是要放低标准并坚持发布。

rss · Simon Willison · Aug 6, 18:04

**标签**: `#技术博客`, `#内容创作`, `#职业发展`, `#知识分享`, `#Simon Willison`

---

<a id="item-12"></a>
## [纳斯达克申请将交易时间延长至 23 小时  美国纳斯达克交易所 12 月 15 日向证券交易委员会（SEC）申请增加交易时段，拟从东部时间晚上 9 时至次日凌晨](https://t.me/zaihuapd/43037) ⭐️ 7.0/10

纳斯达克已向美国证券交易委员会（SEC）申请将其工作日交易时间延长至 23 小时，即从美国东部时间晚上 9 点至次日凌晨 4 点，预计如获批准将于 2026 年第三季度初启动。

telegram · zaihuapd · Aug 7, 10:03

**标签**: `#金融市场`, `#金融科技`, `#交易系统`, `#市场监管`, `#系统影响`

---