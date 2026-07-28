---
layout: default
title: "Horizon Summary: 2026-07-28 (ZH)"
date: 2026-07-28
lang: zh
---

> From 24 items, 10 important content pieces were selected

---

1. [moonshotai/Kimi-K3](#item-1) ⭐️ 9.0/10
2. [SpaceX 拒接 Falcon 9 远期订单，全力押注 Starship](#item-2) ⭐️ 9.0/10
3. [Kimi K3 发布：开源 2.8T 模型，前端编程基准测试夺冠](#item-3) ⭐️ 9.0/10
4. [Fastjson 1.x 被曝无 gadget 高危 RCE 漏洞  安全研究人员 Kirill Firsov 披露，Fastjson 1.2.68 至 1.2](#item-4) ⭐️ 9.0/10
5. [vllm-project/vllm released v0.26.0](#item-5) ⭐️ 8.0/10
6. [Our position on open-weights models](#item-6) ⭐️ 8.0/10
7. [An Inside Look at the Relay Market Powering Token Resellers and Fraud](#item-7) ⭐️ 8.0/10
8. [阿里将推千问办公，整合三款智能体  阿里将推出千问办公，整合旗下 QoderWork、悟空、MuleRun 三款智能体产品，由钉钉新任 CEO 陈宇森负责。](#item-8) ⭐️ 8.0/10
9. [♻️ 黄仁勋首次发帖分享英伟达支持开源模型公开信  黄仁勋首次发帖，分享英伟达签署的一封强调开源模型重要性的公开信。](#item-9) ⭐️ 8.0/10
10. [An opinionated guide to which AI to use to do stuff](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [moonshotai/Kimi-K3](https://simonwillison.net/2026/Jul/27/kimi-k3/#atom-everything) ⭐️ 9.0/10

Moonshot 已在 Hugging Face 上发布了其 2.8 万亿参数 Kimi K3 模型的权重（1.56TB），并附带了一个修改版的 MIT 许可，要求大型商业实体进行归属。

rss · Simon Willison · Jul 27, 23:39

**标签**: `#Large Language Models`, `#Model Weights`, `#AI Licensing`, `#Hugging Face`

---

<a id="item-2"></a>
## [SpaceX 拒接 Falcon 9 远期订单，全力押注 Starship](https://www.bloomberg.com/news/articles/2026-07-23/spacex-is-turning-away-falcon-customers-in-major-bet-on-starship) ⭐️ 9.0/10

SpaceX is phasing out Falcon 9 orders after 2028 and reducing its production to fully commit to Starship, a high-risk strategy critical for its future endeavors but potentially creating a global launch capacity gap if Starship faces further delays.

telegram · zaihuapd · Jul 26, 12:42

**标签**: `#SpaceX`, `#Starship`, `#Falcon 9`, `#Space Launch`, `#Aerospace Industry`

---

<a id="item-3"></a>
## [Kimi K3 发布：开源 2.8T 模型，前端编程基准测试夺冠](https://t.me/zaihuapd/42793) ⭐️ 9.0/10

月之暗面发布了 Kimi K3，这是全球首个开源的 2.8 万亿参数模型，其基于 Kimi Delta Attention 和 Attention Residuals 架构，并拥有原生视觉能力和 100 万 token 上下文窗口。该模型在第三方基准 Frontend Code Arena 中以 1679 分位居榜首，从 Kimi K2.6 的第 18 名跃升至第一。 此次发布标志着 AI 领域的一项重大突破，它为开源模型提供了前所未有的规模，并在前端编程等实际应用领域展现出卓越性能。其先进的架构和多模态能力有望加速大型语言模型开发领域的创新和普及。 Kimi K3 采用了 Kimi Delta Attention 和 Attention Residuals 架构，这有助于其性能和效率的提升。该模型在 Frontend Code Arena 的 7 个评测领域中，有 6 项位居榜首，仅在游戏领域表现略逊。

telegram · zaihuapd · Jul 27, 06:27

**背景**: Kimi Delta Attention (KDA) 是 Kimi Linear 架构中的一项核心创新，它是一种新型的门控线性注意力变体，通过更精细的门控机制实现对循环神经网络有限状态记忆的有效利用。Attention Residuals (AttnRes) 是一种替代 Transformer 中标准残差连接的架构设计，它允许每一层通过学习到的、基于输入的注意力机制选择性地聚合之前的表示，从而解决隐藏状态随深度增长的问题。Frontend Code Arena 是一个第三方基准测试平台，用于评估 AI 模型在前端和 Web 应用程序开发任务中的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agifrontier.github.io/tutorials/kimi-linear-an-expressive-efficient-attention-architecture/">Kimi Linear: An Expressive, Efficient Attention Architecture | AI前沿分享</a></li>
<li><a href="https://github.com/MoonshotAI/Attention-Residuals">GitHub - MoonshotAI/Attention-Residuals · GitHub</a></li>
<li><a href="https://aitoolhunt.co/blog/kimi-k3-benchmarks-frontend-code-arena-2026">Kimi K3 Benchmarks: Frontend Leap and Review... | AIToolHunt</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Open Source AI`, `#Frontend AI`, `#AI Architecture`, `#Multimodal AI`

---

<a id="item-4"></a>
## [Fastjson 1.x 被曝无 gadget 高危 RCE 漏洞  安全研究人员 Kirill Firsov 披露，Fastjson 1.2.68 至 1.2](https://t.me/zaihuapd/42797) ⭐️ 9.0/10

安全研究人员披露了 Fastjson 1.x 版本 1.2.68 至 1.2.83 中一个无需 autoTypeSupport 或 classpath gadget 的高危远程代码执行漏洞，且由于该版本已停止维护，官方不会提供补丁。

telegram · zaihuapd · Jul 27, 10:31

**标签**: `#Java安全`, `#RCE`, `#Fastjson`, `#漏洞`, `#软件工程`

---

<a id="item-5"></a>
## [vllm-project/vllm released v0.26.0](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 版本发布，主要亮点包括新增对 Inkling 模型家族的全面支持、DeepSeek-V4 在多供应商上的性能提升，以及通过 fp32 `lm_head`改进生成模型的准确性。

github · khluu · Jul 27, 01:06

**标签**: `#LLM推理`, `#vLLM`, `#模型优化`, `#AI框架`, `#深度学习`

---

<a id="item-6"></a>
## [Our position on open-weights models](https://www.anthropic.com/news/position-open-weights-models) ⭐️ 8.0/10

Anthropic published its stance on open-weights models, advocating for mandatory safety testing for all sufficiently capable models, which ignited a strong, critical debate among the community regarding potential regulatory implications and the company's motives.

hackernews · surprisetalk · Jul 27, 22:03

**标签**: `#AI Policy`, `#Open Source AI`, `#AI Safety`, `#Regulation`, `#Anthropic`

---

<a id="item-7"></a>
## [An Inside Look at the Relay Market Powering Token Resellers and Fraud](https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything) ⭐️ 8.0/10

一项调查揭露了一个新兴的非法市场，主要在中国，转售商通过滥用免费试用、未受保护的机器人或被盗凭据，并常利用开源 API 代理软件，提供折扣的 LLM 代币。

rss · Simon Willison · Jul 26, 19:30

**标签**: `#LLM Security`, `#API Abuse`, `#Cybercrime`, `#Digital Economy`, `#Fraud`

---

<a id="item-8"></a>
## [阿里将推千问办公，整合三款智能体  阿里将推出千问办公，整合旗下 QoderWork、悟空、MuleRun 三款智能体产品，由钉钉新任 CEO 陈宇森负责。](https://t.me/zaihuapd/42792) ⭐️ 8.0/10

阿里巴巴将整合旗下三款 AI 智能体产品推出“千问办公”，由钉钉新任 CEO 负责，旨在抢占 AI 智能体办公市场，并预示着与腾讯、字节跳动等在 AI 办公生态领域的竞争将加剧。

telegram · zaihuapd · Jul 27, 05:45

**标签**: `#AI智能体`, `#企业软件`, `#阿里巴巴`, `#办公自动化`, `#行业趋势`

---

<a id="item-9"></a>
## [♻️ 黄仁勋首次发帖分享英伟达支持开源模型公开信  黄仁勋首次发帖，分享英伟达签署的一封强调开源模型重要性的公开信。](https://t.me/zaihuapd/42804) ⭐️ 8.0/10

NVIDIA CEO Jensen Huang made his first social media post to share an open letter signed by NVIDIA, advocating for the importance of open-source AI models in driving innovation, security, and technological sovereignty alongside closed-source models.

telegram · zaihuapd · Jul 28, 01:11

**标签**: `#AI Policy`, `#Open Source AI`, `#NVIDIA`, `#Industry Leadership`, `#AI Strategy`

---

<a id="item-10"></a>
## [An opinionated guide to which AI to use to do stuff](https://simonwillison.net/2026/Jul/27/an-opinionated-guide-to-which-ai-to-use-to-do-stuff/#atom-everything) ⭐️ 7.0/10

Simon Willison 回顾了 Ethan Mollick 关于 AI 工具的最新指南，指出 AI 使用正从简单的聊天模型转向能够执行复杂任务的代理系统，并观察到 Gemini 在此演变中的地位有所下降。

rss · Simon Willison · Jul 27, 21:55

**标签**: `#AI工具`, `#代理AI`, `#AI趋势`, `#LLM应用`

---