---
layout: default
title: "Horizon Summary: 2026-10-20 (ZH)"
date: 2026-10-20
lang: zh
---

> From 27 items, 13 important content pieces were selected

---

1. [vLLM v0.32.0 发布，支持低精度 KV 缓存和结构化输出](#item-1) ⭐️ 9.0/10
2. [Wine ported to OpenBSD](#item-2) ⭐️ 9.0/10
3. [中国脑机接口实现跨地域千人同步采集  中国科研团队 7 月 22 日发布新型脑电信号采集装置，首次在全球实现跨地域上千人同步脑电信号采集，为神经大模型训练和脑机](#item-3) ⭐️ 9.0/10
4. [两部门发布离岸信托个税新规，装入财产及收益须申报纳税  财政部、税务总局 7 月 24 日发布 2026 年第 21 号公告，明确离岸信托个人所得税征管规则，自](#item-4) ⭐️ 9.0/10
5. [Lula supporters protest against Meta to denounce its 'electoral interference'](#item-5) ⭐️ 8.0/10
6. [I built a drone with only one motor (video)](#item-6) ⭐️ 8.0/10
7. [My obituary for programming](#item-7) ⭐️ 8.0/10
8. [MiniMax 发布 M3.1 Flash，推理速度提升近 3 倍，成本降低 70%](#item-8) ⭐️ 8.0/10
9. [🤖 美国国土安全部下令，将 DeepSeek 产品排除出联邦文职部门采购并清除现有系统](#item-9) ⭐️ 8.0/10
10. [Manus 上线 AI 游戏生成器，描述即可做网页游戏](#item-10) ⭐️ 8.0/10
11. [MiniMax M3.1 Flash](#item-11) ⭐️ 7.0/10
12. [💬 微信发起公众号小说改编短剧激励活动](#item-12) ⭐️ 7.0/10
13. [工信部拟新规：小蓝灯进国标，车灯禁文字与语音](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vLLM v0.32.0 发布，支持低精度 KV 缓存和结构化输出](https://github.com/vllm-project/vllm/releases/tag/v0.32.0) ⭐️ 9.0/10

vLLM v0.32.0 版本已发布，通过在 NVIDIA SM8x、SM12x、SM90、SM100 和 ROCm 等多种硬件上广泛支持低精度 KV 缓存，显著提升了 LLM 推理效率。此版本还引入了通过 POST /v1/systemone 端点实现结构化决策的新功能，以及能够自动读取模型 response_template 的通用解析器。 此次发布对于扩展 AI 应用至关重要，因为它显著提高了 LLM 推理的内存效率和吞吐量，降低了运营成本，并使得在现有硬件上运行更大的模型或处理更长的上下文成为可能。新的结构化输出功能通过确保可靠且易于解析的响应，简化了 LLM 与复杂系统的集成，这对于构建强大的 AI 驱动应用至关重要。 低精度 KV 缓存包括在 SM8x/SM12x/SM90 上的 NVFP4，在 SM100 上的 FP8（将 KV 内存减半，吞吐量提高 2.3-5.5%），以及在 ROCm 上的 4 位 ultraquant_4bit，其密度约为 FP8 的两倍。通过 POST /v1/systemone 端点，可以实现针对 choice、noul 和 score 问题的结构化决策，而新的 hf 工具和推理解析器则消除了对模型特定解析器的需求。

github · khluu · Oct 18, 06:50

**背景**: 在大型语言模型（LLM）推理过程中，KV（键值）缓存存储中间的自注意力张量，以避免重复计算，但这些缓存会占用大量 GPU 内存，特别是对于长序列。低精度 KV 缓存通过以压缩格式（例如 8 位、4 位）存储这些张量来解决这个问题，从而减少内存占用并提高吞吐量。XQA（eXtended Query Attention）是一种优化的注意力机制，常用于 NVIDIA 的 TensorRT-LLM 中，专门设计用于加速 LLM 推理的令牌生成（解码）阶段。稀疏注意力机制通过仅关注令牌子集，降低了传统注意力机制相对于序列长度的二次计算成本，从而使 LLM 能够更高效地处理更长的上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bilwasiva.github.io/2026-01-09-kv-cache/">The Hidden Bottleneck in Modern LLMs</a></li>
<li><a href="https://www.emergentmind.com/topics/sparse-attention-variants">Sparse Attention Variants Overview</a></li>

</ul>
</details>

**标签**: `#LLM Inference`, `#Performance Optimization`, `#AI Infrastructure`, `#vLLM`, `#Structured Output`

---

<a id="item-2"></a>
## [Wine ported to OpenBSD](https://marc.info/?l=openbsd-ports&m=179236125692175) ⭐️ 9.0/10

Wine has been successfully ported to OpenBSD, enabling the execution of Windows applications on the security-focused operating system.

hackernews · iamnothere · Oct 19, 13:35

**标签**: `#OpenBSD`, `#Wine`, `#Operating Systems`, `#Software Compatibility`, `#Porting`

---

<a id="item-3"></a>
## [中国脑机接口实现跨地域千人同步采集  中国科研团队 7 月 22 日发布新型脑电信号采集装置，首次在全球实现跨地域上千人同步脑电信号采集，为神经大模型训练和脑机](https://t.me/zaihuapd/44536) ⭐️ 9.0/10

中国科研团队发布新型脑电信号采集装置，首次在全球实现跨地域千人同步脑电信号采集，为神经大模型训练和脑机接口通用技术研发提供关键支持。

telegram · zaihuapd · Oct 19, 12:28

**标签**: `#脑机接口`, `#神经科学`, `#人工智能`, `#数据采集`, `#医疗技术`

---

<a id="item-4"></a>
## [两部门发布离岸信托个税新规，装入财产及收益须申报纳税  财政部、税务总局 7 月 24 日发布 2026 年第 21 号公告，明确离岸信托个人所得税征管规则，自](https://t.me/zaihuapd/44537) ⭐️ 9.0/10

中国财政部和税务总局发布离岸信托个人所得税新规，明确居民个人将财产装入离岸信托及信托存续期间的收益均须申报纳税。

telegram · zaihuapd · Oct 19, 12:58

**标签**: `#税务政策`, `#离岸信托`, `#财富管理`, `#中国监管`, `#个人所得税`

---

<a id="item-5"></a>
## [Lula supporters protest against Meta to denounce its 'electoral interference'](https://efe.com/english/latest-news/2026-10-20/lula-supporters-protest-against-meta-to-denounce-its-electoral-interference/) ⭐️ 8.0/10

卢拉的支持者抗议 Meta，指责这家科技巨头干预选举，这引发了 Hacker News 上关于算法偏见、平台治理和科技公司对全球政治影响的深入讨论。

hackernews · jumpocelot · Oct 20, 00:53

**标签**: `#科技伦理`, `#平台治理`, `#选举干预`, `#社交媒体影响`, `#算法偏见`

---

<a id="item-6"></a>
## [I built a drone with only one motor (video)](https://www.youtube.com/watch?v=Ndftcft6XhU) ⭐️ 8.0/10

一个单电机无人机通过创新的铰链设计、磁编码器和扭矩调制实现飞行控制，有效地取代了传统直升机的倾斜盘。

hackernews · hakonjdjohnsen · Oct 19, 09:05

**标签**: `#机器人技术`, `#无人机技术`, `#欠驱动系统`, `#机械工程`, `#控制系统`

---

<a id="item-7"></a>
## [My obituary for programming](https://simonwillison.net/2026/Oct/19/my-obituary-for-programming/) ⭐️ 8.0/10

这篇文章探讨了 AI/LLM 对编程职业的潜在影响，区分了享受解决逻辑难题的程序员（可能因 AI 而感到失落）和专注于构建系统的人（将 AI 视为福音）。

rss · Simon Willison · Oct 19, 23:58

**标签**: `#AI Impact`, `#Future of Programming`, `#Software Engineering`, `#Developer Roles`, `#LLMs`

---

<a id="item-8"></a>
## [MiniMax 发布 M3.1 Flash，推理速度提升近 3 倍，成本降低 70%](https://mp.weixin.qq.com/s/fO9snz_lnPxVg0q55chDFg) ⭐️ 8.0/10

MiniMax 发布了 M3.1 Flash 模型，该模型专注于 Agent、编程和电脑操作能力，推理速度提升近 3 倍，成本降低 70%，并在 DeepSWE 和 OSWorld 基准测试中取得高分。

telegram · zaihuapd · Oct 19, 11:27

**标签**: `#LLM`, `#AI Agents`, `#Inference Performance`, `#Cost Optimization`, `#Generative AI`

---

<a id="item-9"></a>
## [🤖 美国国土安全部下令，将 DeepSeek 产品排除出联邦文职部门采购并清除现有系统](https://www.federalregister.gov/public-inspection/2026-21447/order-exclusion-and-removal-of-deepseek-products-from-federal-civilian-executive-branch-information) ⭐️ 8.0/10

美国国土安全部已下令联邦文职行政部门将杭州深度求索人工智能基础技术研究有限公司（DeepSeek）及其关联实体的信息技术产品和服务排除出采购范围，并从现有系统中移除，理由是联邦采购供应链安全法。

telegram · zaihuapd · Oct 19, 13:32

**标签**: `#AI政策`, `#国家安全`, `#供应链安全`, `#政府采购`, `#地缘政治`

---

<a id="item-10"></a>
## [Manus 上线 AI 游戏生成器，描述即可做网页游戏](https://manus.im/features/game-dev) ⭐️ 8.0/10

Manus has launched an AI game generator that allows users to create playable web games using natural language descriptions, eliminating the need for coding and providing features for sharing and analytics.

telegram · zaihuapd · Oct 20, 01:18

**标签**: `#AI Game Generation`, `#No-code Development`, `#Web Games`, `#Game Development`, `#AI Tools`

---

<a id="item-11"></a>
## [MiniMax M3.1 Flash](https://www.minimax.io/blog/minimax-m31f) ⭐️ 7.0/10

MiniMax 发布了其 M3.1 Flash 大语言模型，但 Hacker News 社区对其真实性能和基准测试的有效性表示怀疑，并引发了关于 LLM 性价比和实际应用价值的讨论。

hackernews · jtg · Oct 19, 16:39

**标签**: `#LLM`, `#AI模型`, `#基准测试`, `#社区讨论`, `#模型评估`

---

<a id="item-12"></a>
## [💬 微信发起公众号小说改编短剧激励活动](https://mp.weixin.qq.com/s/3OLBTZTEz6VSjJ_5QtbFtg) ⭐️ 7.0/10

微信发起了一项激励活动，鼓励将公众号小说改编成短剧并在微信生态内优先发行，为作者和承制方提供额外的现金奖励。

telegram · zaihuapd · Oct 19, 10:28

**标签**: `#微信`, `#内容战略`, `#短剧`, `#IP变现`, `#数字出版`

---

<a id="item-13"></a>
## [工信部拟新规：小蓝灯进国标，车灯禁文字与语音](https://www.ithome.com/1/015/123.htm) ⭐️ 7.0/10

中国工信部拟定新的汽车强制性国家标准，包括对 ADS 标志灯的专用蓝绿色要求，禁止车灯显示文字、语音关闭或手势控制，并规定转向灯不得与制动灯和后雾灯混合，预计 2028 年实施。

telegram · zaihuapd · Oct 20, 02:27

**标签**: `#汽车法规`, `#ADAS`, `#HMI`, `#中国政策`, `#车辆安全`

---