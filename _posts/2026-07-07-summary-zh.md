---
layout: default
title: "Horizon Summary: 2026-07-07 (ZH)"
date: 2026-07-07
lang: zh
---

> From 22 items, 12 important content pieces were selected

---

1. [腾讯发布 Hy3：295B MoE 大模型，具备 256K 长上下文](#item-1) ⭐️ 9.0/10
2. [腾讯混元 Hy3 preview MoE 模型开源发布](#item-2) ⭐️ 9.0/10
3. [SpaceX 火箭碎片正在引发空气污染  马斯克的 SpaceX 每次发射都在全网刷屏，但你可能不知道，这些燃烧的钢铁巨兽正在给地球的高空“投毒”。](#item-3) ⭐️ 9.0/10
4. [中国正在论证构建小行星防御系统](#item-4) ⭐️ 9.0/10
5. [OpenWrt One – Open Hardware Router](#item-5) ⭐️ 8.0/10
6. [CoMaps – FOSS Offline Maps](#item-6) ⭐️ 8.0/10
7. [A global workspace in language models](#item-7) ⭐️ 8.0/10
8. [全球最大动漫盗版站 HiAnime 运营者在越南被捕](#item-8) ⭐️ 8.0/10
9. [微软欧盟披露：近四成税前利润记在爱尔兰，当地员工仅占全球 3%](#item-9) ⭐️ 8.0/10
10. [Claude Cowork 漏洞可逃逸沙箱](#item-10) ⭐️ 8.0/10
11. [任天堂将在欧洲推出可换电池版 Switch 2，旧 Switch 明年停售](#item-11) ⭐️ 8.0/10
12. [sqlite-utils 4.0rc3](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [腾讯发布 Hy3：295B MoE 大模型，具备 256K 长上下文](https://simonwillison.net/2026/Jul/6/hy3/#atom-everything) ⭐️ 9.0/10

腾讯发布了 Hy3，这是一个 2950 亿参数的 MoE（专家混合）模型，拥有 210 亿活跃参数，并采用 Apache 2.0 许可证。该模型具有 256K 的超长上下文窗口，并声称性能优于同等规模的模型，甚至能与参数量大 2-5 倍的旗舰级开源模型媲美。 此次发布对开源 AI 领域意义重大，因为它提供了一个功能强大、大规模的 MoE 模型，拥有开放许可证和超长上下文窗口，可能降低高级 LLM 应用的门槛。其声称的性能可与大型模型媲美，有望推动高效、强大 AI 模型开发的创新和竞争。 完整的 Hy3 模型在 Hugging Face 上占用 598GB 存储空间，而 FP8 量化版本为 300GB，使其更易于部署。该模型以 210 亿活跃参数运行，并可在 OpenRouter 上免费使用至 7 月 21 日。

rss · Simon Willison · Jul 6, 23:57

**背景**: 专家混合（MoE）是一种人工智能架构，它将模型划分为多个“专家”子模型，每个子模型专门处理输入数据的不同部分，与密集模型相比，这使得模型能够更高效地扩展和训练。大型语言模型的上下文长度定义了模型在单个输入序列中可以处理或“记住”的最大文本量（以 token 为单位）。FP8 量化是一种通过使用 8 位浮点数而不是训练时常用的 16 位或 32 位格式来表示模型权重和激活，从而减少神经网络内存占用和计算需求的技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://www.ibm.com/think/topics/context-window">What is a context window? | IBM</a></li>
<li><a href="https://www.spheron.network/blog/fp8-quantization-inference-performance-hardware-explained/">What is FP8 Quantization? AI Inference Performance, Accuracy, and Hardware Support Explained (2026) | Spheron Blog</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#MoE`, `#AI Models`, `#Open Source AI`, `#Long Context`

---

<a id="item-2"></a>
## [腾讯混元 Hy3 preview MoE 模型开源发布](https://t.me/zaihuapd/42385) ⭐️ 9.0/10

腾讯正式发布并开源了其首个架构重建后的混合专家模型（MoE）混元 Hy3 preview，该模型拥有 295B 总参数、21B 激活参数和 256K 上下文长度。该模型显著提升了复杂推理和 AI Agent 应用能力，其推理性能得到显著优化，例如 CodeBuddy 等产品的首 token 延迟降低了 54%。 此次发布标志着大语言模型在复杂推理和 AI Agent 应用方面取得了重大进展，腾讯作为一家主要科技公司开源如此强大的 MoE 模型，将加速 AI 研究和开发。改进的推理性能和扩展的上下文长度将使依赖高级 AI 能力处理复杂任务的开发者和用户受益，从而促进更广泛的 AI 生态系统创新。 混元 Hy3 preview 模型是腾讯首个架构重建后的 MoE 模型，拥有 295B 总参数、21B 激活参数和令人印象深刻的 256K 上下文长度。其核心能力定位于数学、科学等理工科推理任务及 AI Agent 应用，由于模型架构与推理框架的深度协同，CodeBuddy 等产品的首 token 延迟降低了 54%。

telegram · zaihuapd · Jul 6, 10:09

**背景**: 混合专家模型（MoE）是一种在大语言模型中使用的技术，它利用多个不同的子模型（或称为“专家”）来提升模型的整体质量。与单一的庞大模型不同，MoE 会针对每个输入动态选择并激活少数几个最相关的专家来工作，从而提高效率和性能。在生成式 AI 的背景下，AI Agent 是智能系统，它们能够追求目标、使用工具并以不同程度的自主性采取行动，通常在人类定义的目标范围内运作，并能自动化复杂的业务流程。大语言模型的上下文长度是指模型在单次交互中可以处理和生成的最大 token 数量，更大的上下文窗口允许处理更广泛、更复杂的信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.csdn.net/qq_32907491/article/details/145394117">混 合 专 家 模 型 MoE 的全面详解-CSDN博客</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent</a></li>
<li><a href="https://www.mambabit.com/tutorial/llm-context-window-why-it-matters">揭开 大 模 型 上 下 文 窗口的神秘面纱，为什么它如此重要？ -曼巴比特</a></li>

</ul>
</details>

**标签**: `#大语言模型`, `#混合专家模型`, `#开源AI`, `#AI Agent`, `#腾讯AI`

---

<a id="item-3"></a>
## [SpaceX 火箭碎片正在引发空气污染  马斯克的 SpaceX 每次发射都在全网刷屏，但你可能不知道，这些燃烧的钢铁巨兽正在给地球的高空“投毒”。](https://t.me/zaihuapd/42387) ⭐️ 9.0/10

一项发表在《Nature》子刊上的最新研究表明，SpaceX 猎鹰 9 号火箭重返大气层时，会在高空留下浓度惊人的金属污染羽流，对地球高层大气造成影响。

telegram · zaihuapd · Jul 6, 11:17

**标签**: `#SpaceX`, `#环境影响`, `#火箭技术`, `#大气科学`, `#污染`

---

<a id="item-4"></a>
## [中国正在论证构建小行星防御系统](http://paper.people.com.cn/rmrb/pc/content/202607/06/content_30166956.html) ⭐️ 9.0/10

中国正在论证构建一个天地一体化的小行星防御系统，旨在通过先进的监测预警网络和动能撞击、引力牵引等防御技术，提升应对近地天体撞击风险的能力。

telegram · zaihuapd · Jul 6, 13:36

**标签**: `#行星防御`, `#空间技术`, `#国家战略`, `#小行星`, `#预警系统`

---

<a id="item-5"></a>
## [OpenWrt One – Open Hardware Router](https://openwrt.org/toh/openwrt/one) ⭐️ 8.0/10

The OpenWrt One is an officially supported open-hardware router designed to run OpenWrt firmware, addressing common issues with commercial routers by providing a long-term, open-source solution for network enthusiasts.

hackernews · peter_d_sherman · Jul 6, 18:23

**标签**: `#OpenWrt`, `#Open Hardware`, `#Networking`, `#Router`, `#Open Source`

---

<a id="item-6"></a>
## [CoMaps – FOSS Offline Maps](https://www.comaps.app/) ⭐️ 8.0/10

CoMaps is a FOSS offline map application, forked from Organic Maps due to governance concerns, offering a community-driven alternative that leverages OpenStreetMap data, though users note common search limitations.

hackernews · basilikum · Jul 6, 18:55

**标签**: `#FOSS`, `#Offline Maps`, `#OpenStreetMap`, `#Community Governance`, `#Mobile Development`

---

<a id="item-7"></a>
## [A global workspace in language models](https://www.anthropic.com/research/global-workspace) ⭐️ 8.0/10

Anthropic 的研究提出并探讨了语言模型中“全局工作空间”的概念，为理解这些模型如何内部处理和整合信息提供了新的视角。

hackernews · in-silico · Jul 6, 17:44

**标签**: `#AI Research`, `#Large Language Models`, `#Mechanistic Interpretability`, `#Model Architecture`

---

<a id="item-8"></a>
## [全球最大动漫盗版站 HiAnime 运营者在越南被捕](https://x.com/IntCyberDigest/status/2073827560048263671) ⭐️ 8.0/10

全球最大动漫盗版网站 HiAnime 的运营者在越南被捕，该团伙通过运营逾百个盗版网站获利超过 1200 万美元，此次行动是多方国际合作的结果。

telegram · zaihuapd · Jul 6, 03:30

**标签**: `#盗版`, `#网络犯罪`, `#知识产权`, `#数字内容`, `#执法`

---

<a id="item-9"></a>
## [微软欧盟披露：近四成税前利润记在爱尔兰，当地员工仅占全球 3%](https://www.techspot.com/news/113001-microsoft-new-eu-disclosure-shows-exactly-how-tech.html) ⭐️ 8.0/10

微软最新欧盟披露显示，其近四成税前利润记在爱尔兰，而当地员工仅占全球 3%，揭示了大型科技公司利用国际税收差异进行利润转移的策略，并受到欧盟新透明度规则和美国国税局追税行动的关注。

telegram · zaihuapd · Jul 6, 09:19

**标签**: `#企业税收`, `#科技巨头`, `#欧盟法规`, `#财务透明度`, `#微软`

---

<a id="item-10"></a>
## [Claude Cowork 漏洞可逃逸沙箱](https://cyberpress.org/claude-cowork-flaw/) ⭐️ 8.0/10

Anthropic Claude 桌面版 Windows 应用中的 Cowork 功能存在一个沙箱逃逸漏洞链，攻击者在本地执行代码后可获得隔离 VM 的 root 权限，绕过网络限制并窃取敏感数据。

telegram · zaihuapd · Jul 6, 14:53

**标签**: `#网络安全`, `#漏洞`, `#沙箱逃逸`, `#AI安全`

---

<a id="item-11"></a>
## [任天堂将在欧洲推出可换电池版 Switch 2，旧 Switch 明年停售](https://www.nintendo.com/en-gb/Support/Nintendo-Switch-2/Information-about-upcoming-battery-related-revisions-to-some-Nintendo-products-3132901.html) ⭐️ 8.0/10

任天堂宣布为遵守欧盟法规，将从 2026 年起在欧洲推出内置用户可更换电池的 Switch 2 及相关产品，并于 2027 年初停止在欧洲销售旧款 Switch 主机。

telegram · zaihuapd · Jul 6, 15:53

**标签**: `#Nintendo Switch`, `#欧盟法规`, `#消费电子`, `#产品设计`, `#可持续性`

---

<a id="item-12"></a>
## [sqlite-utils 4.0rc3](https://simonwillison.net/2026/Jul/6/sqlite-utils/#atom-everything) ⭐️ 7.0/10

sqlite-utils 4.0rc3 发布，主要增加了对复合外键的支持和遵循 SQLite 大小写不敏感列名约定，并包含一个相关的破坏性变更。

rss · Simon Willison · Jul 6, 05:40

**标签**: `#sqlite-utils`, `#Database`, `#Python`, `#Release`

---