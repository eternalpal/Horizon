---
layout: default
title: "Horizon Summary: 2026-07-25 (ZH)"
date: 2026-07-25
lang: zh
---

> From 27 items, 11 important content pieces were selected

---

1. [sglang v0.5.16 发布：DSpark 和 Inkling 模型支持](#item-1) ⭐️ 9.0/10
2. [Claude Opus 5](#item-2) ⭐️ 9.0/10
3. [My security camera shipped a GitHub admin token in its login page](#item-3) ⭐️ 9.0/10
4. [Quoting Boris Cherny](#item-4) ⭐️ 9.0/10
5. [长鑫年底产能逼近美光 中国将成全球第二大 DRAM 产地  Citrini Research 预测，长鑫存储有望在 2026 年底达到约 35 万片/月的 DR](#item-5) ⭐️ 9.0/10
6. [Postgres LISTEN/NOTIFY actually scales](#item-6) ⭐️ 8.0/10
7. [If coding has been solved, why does software keep getting worse?](#item-7) ⭐️ 8.0/10
8. [一加将调整 ColorOS 16+ 设备解锁政策](#item-8) ⭐️ 7.0/10
9. [OpenRouter 被传收购，估值或高于 13 亿美元  AI 模型路由平台 OpenRouter 已被多家大型科技公司接触，探讨潜在收购可能；意向估值或高于](#item-9) ⭐️ 7.0/10
10. [✈️ Telegram 现支付漏洞：日本账户超低价购星币，目前已修复  7 月 23 日，Telegram 一个已修复的漏洞影响日本账户，可超低价购入星币(St](#item-10) ⭐️ 7.0/10
11. [上海携程商务公司因数据出境违规被罚 1000 万元  上海网信办 6 月 13 日公示，上海携程商务有限公司因未落实数据出境安全评估要求、违法出境个人信息等行为](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [sglang v0.5.16 发布：DSpark 和 Inkling 模型支持](https://github.com/sgl-project/sglang/releases/tag/v0.5.16) ⭐️ 9.0/10

sglang v0.5.16 版本发布了 DSpark，这是一种新颖的置信度驱动推测解码算法，可显著提升大型语言模型（LLM）的推理速度。此外，它还增加了对拥有 9750 亿参数的多模态 Inkling 模型的支持，并在 Blackwell 硬件上展示了令人印象深刻的性能。 此次发布至关重要，因为 DSpark 显著提升了 LLM 推理速度和效率，使先进的 AI 模型在各种应用中更具可访问性和成本效益。集成 9750 亿参数的多模态 Inkling 模型也推动了 AI 能力的前沿，特别是在新硬件上，从而实现更复杂、更多功能的 AI 系统。 DSpark 通过半自回归地分块草拟并根据草稿的置信度动态调整验证窗口大小来改进推测解码，在 DeepSeek-V4-Pro 上实现了 383.7 令牌/秒的速度。Inkling 模型是一个拥有 9750 亿参数的多模态 MoE 模型，具有 100 万令牌上下文，融合了滑动窗口、全注意力以及 Mamba2 线性注意力，在 Blackwell 上实现了高达 71.7k 令牌/秒的输入速度和 171.0 令牌/秒的每用户解码速度。

github · Qiaolin-Yu · Jul 25, 00:13

**背景**: 推测解码是一种 LLM 推理优化技术，它通过并行预测和验证多个令牌来显著降低延迟，而不是逐个生成令牌。专家混合（MoE）是一种大型模型的架构方法，其中针对输入的不同部分选择性地激活不同的“专家”子网络，从而使模型能够扩展到万亿参数，同时保持计算成本可控。多模态 MoE 模型将这一概念扩展到处理文本、图像和音频等各种数据类型，从而实现统一的理解能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lmsys.org/blog/2026-07-06-dspark-sglang">DSpark in SGLang: Speculative Decoding with Confidence-Driven, Variable-Length Verification - LMSYS Org</a></li>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/">An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog</a></li>
<li><a href="https://uni-moe.github.io/">Scaling Unified Multimodal LLMs with Mixture of Experts</a></li>

</ul>
</details>

**标签**: `#LLM Inference`, `#Speculative Decoding`, `#Multimodal AI`, `#AI Performance`, `#AI Systems`

---

<a id="item-2"></a>
## [Claude Opus 5](https://www.anthropic.com/news/claude-opus-5) ⭐️ 9.0/10

Anthropic has released Claude Opus 5, its new flagship AI model, boasting improved performance in tasks like image-to-HTML conversion and a critical policy update removing data retention requirements, enhancing its appeal for organizational use.

hackernews · alvis · Jul 24, 16:57

**标签**: `#AI Models`, `#Large Language Models`, `#Anthropic`, `#Enterprise AI`, `#Multimodal AI`

---

<a id="item-3"></a>
## [My security camera shipped a GitHub admin token in its login page](https://hhh.hn/hanwha-github-token/) ⭐️ 9.0/10

一款安全摄像头被发现其登录页面中包含 GitHub 管理员令牌，并且固件中硬编码了美国国防部的 IP 地址，揭示了严重的安全性缺陷并引发了重大的隐私担忧。

hackernews · hhh · Jul 24, 11:54

**标签**: `#IoT安全`, `#漏洞`, `#供应链安全`, `#嵌入式系统`, `#隐私`

---

<a id="item-4"></a>
## [Quoting Boris Cherny](https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything) ⭐️ 9.0/10

Boris Cherny highlights that Anthropic's Claude Opus 5 model represents a significant breakthrough in AI safety, being their least prompt-injectable model to date, making it very difficult to successfully prompt inject.

rss · Simon Willison · Jul 25, 00:42

**标签**: `#prompt-injection`, `#AI security`, `#Large Language Models`, `#Anthropic`, `#AI safety`

---

<a id="item-5"></a>
## [长鑫年底产能逼近美光 中国将成全球第二大 DRAM 产地  Citrini Research 预测，长鑫存储有望在 2026 年底达到约 35 万片/月的 DR](https://t.me/zaihuapd/42741) ⭐️ 9.0/10

Citrini Research 预测，长鑫存储的 DRAM 产能到 2026 年底将逼近美光，使中国成为全球第二大 DRAM 生产基地，并预计到 2030 年中国总产能将大幅增长。

telegram · zaihuapd · Jul 24, 07:30

**标签**: `#半导体`, `#DRAM`, `#供应链`, `#中国科技`, `#制造业`

---

<a id="item-6"></a>
## [Postgres LISTEN/NOTIFY actually scales](https://www.dbos.dev/blog/postgres-listen-notify-scalability) ⭐️ 8.0/10

This article presents evidence that Postgres's LISTEN/NOTIFY feature can scale effectively, challenging the common belief that it does not, and potentially opening up new architectural possibilities for event-driven systems.

hackernews · KraftyOne · Jul 24, 19:05

**标签**: `#Postgres`, `#Scalability`, `#Event-driven`, `#Database`, `#System Design`

---

<a id="item-7"></a>
## [If coding has been solved, why does software keep getting worse?](https://ptrchm.com/posts/nothing-works-and-everyone-is-euphoric/) ⭐️ 8.0/10

The content explores the paradox of why software quality appears to be worsening despite advancements in coding, attributing it to factors like misaligned corporate incentives, user dread of updates, and non-technical decision-makers.

hackernews · pchm · Jul 24, 09:08

**标签**: `#Software Quality`, `#Software Engineering`, `#Industry Trends`, `#Developer Culture`, `#User Experience`

---

<a id="item-8"></a>
## [一加将调整 ColorOS 16+ 设备解锁政策](https://bbs.oneplus.com/) ⭐️ 7.0/10

一加宣布将调整 ColorOS 16 及以上版本设备的 Bootloader 解锁政策，要求用户通过官方深度测试计划申请，并设置了严格的申请条件和分阶段的开放时间。

telegram · zaihuapd · Jul 24, 09:20

**标签**: `#OnePlus`, `#ColorOS`, `#Bootloader`, `#设备政策`, `#Android开发`

---

<a id="item-9"></a>
## [OpenRouter 被传收购，估值或高于 13 亿美元  AI 模型路由平台 OpenRouter 已被多家大型科技公司接触，探讨潜在收购可能；意向估值或高于](https://t.me/zaihuapd/42746) ⭐️ 7.0/10

AI 模型路由平台 OpenRouter 据传正被多家大型科技公司接触，探讨潜在收购，估值可能超过 13 亿美元，反映了其在 AI 生态系统中的快速增长和战略重要性。

telegram · zaihuapd · Jul 24, 11:35

**标签**: `#AI基础设施`, `#收购`, `#AI市场`, `#估值`, `#创业公司`

---

<a id="item-10"></a>
## [✈️ Telegram 现支付漏洞：日本账户超低价购星币，目前已修复  7 月 23 日，Telegram 一个已修复的漏洞影响日本账户，可超低价购入星币(St](https://t.me/zaihuapd/42752) ⭐️ 7.0/10

Telegram 修复了一个影响日本账户的支付漏洞，该漏洞允许用户以极低价格购买星币，目前已冻结相关星币并可能回滚购买和账户。

telegram · zaihuapd · Jul 24, 16:27

**标签**: `#安全漏洞`, `#Telegram`, `#支付系统`, `#应用内购买`, `#漏洞利用`

---

<a id="item-11"></a>
## [上海携程商务公司因数据出境违规被罚 1000 万元  上海网信办 6 月 13 日公示，上海携程商务有限公司因未落实数据出境安全评估要求、违法出境个人信息等行为](https://t.me/zaihuapd/42758) ⭐️ 7.0/10

上海携程商务公司因未落实数据出境安全评估要求并违法出境个人信息，被上海网信办处以 1000 万元罚款，表明中国对数据隐私的监管执法力度持续加强。

telegram · zaihuapd · Jul 25, 02:24

**标签**: `#数据隐私`, `#监管合规`, `#跨境数据`, `#中国科技政策`, `#数据治理`

---