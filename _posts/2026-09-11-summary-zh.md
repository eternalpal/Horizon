---
layout: default
title: "Horizon Summary: 2026-09-11 (ZH)"
date: 2026-09-11
lang: zh
---

> From 28 items, 14 important content pieces were selected

---

1. [vLLM v0.29.0 发布：Model Runner V2 默认启用，性能显著提升并支持新模型](#item-1) ⭐️ 9.0/10
2. [Shopify is moving from React Native back to Swift and Kotlin](#item-2) ⭐️ 9.0/10
3. [Quoting Calif Research](#item-3) ⭐️ 9.0/10
4. [🌙 月之暗面秘密递交港股 IPO 申请，新一轮融资投前估值 500 亿美元  月之暗面（Kimi）已以保密形式向港交所递交 A1 文件，正式启动港股 IPO，公](#item-4) ⭐️ 9.0/10
5. [More questions about whether researchers can trust OpenAI with unpublished math](#item-5) ⭐️ 8.0/10
6. [Cognition launches new SWE-2 model, Rivaling Fable 5.1 and GPT-Astra](#item-6) ⭐️ 8.0/10
7. [.blend URL Viewer](#item-7) ⭐️ 8.0/10
8. [🤖 DeepSeek V4.1 Flash：更强、更快、更普惠](#item-8) ⭐️ 8.0/10
9. [中国 AI 芯片厂商涨价，HBM 短缺成为新瓶颈](#item-9) ⭐️ 8.0/10
10. [腾讯混元发布开源音频编辑模型 AuK](#item-10) ⭐️ 8.0/10
11. [Anthropic 前研究员警告 AI 可能是人类创造的最危险技术](#item-11) ⭐️ 8.0/10
12. [Technique for Manipulating Satellite Photos Now Reveals Ancient Images (2025)](#item-12) ⭐️ 7.0/10
13. [📱 海外科技博主曝华为相关推广要求隐藏赞助标识  科技博主 GregsGadgets 称，在 iPhone 发布前后，华为给他们的一份相关推广简报要求创作者不要](#item-13) ⭐️ 7.0/10
14. [Google 将 Gemini 桌面应用带到 Windows](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vLLM v0.29.0 发布：Model Runner V2 默认启用，性能显著提升并支持新模型](https://github.com/vllm-project/vllm/releases/tag/v0.29.0) ⭐️ 9.0/10

vLLM v0.29.0 版本将 Model Runner V2 设为所有模型的默认配置，通过 CUDA 图内存分析和批分片采样等功能，显著提升了大型语言模型推理的性能和内存效率。此次发布还扩展了对多种新型大型语言模型的支持，包括 Hy4-preview、Qwen3.8-Flash-Next 和 GraniteSWA。 此次更新对大型语言模型生态系统至关重要，因为它提供了显著的性能和内存优化，使得大型语言模型的部署更加高效和经济。扩展的模型支持也让开发者能够将 vLLM 的优化应用于更广泛的尖端 AI 模型，从而加速 AI 应用的创新。 Model Runner V2 现在包含了用于 KV 缓存自动调整大小的 CUDA 图内存分析和批分片采样，后者将每步 logits 内存减少了 1/TP。此次发布还为 Kimi-K3 和 DeepSeek V4 模型带来了特定的性能增强，同时改进了推测解码和强化学习权重同步功能。

github · khluu · Sep 9, 08:54

**背景**: vLLM 是一个开源库，旨在实现大型语言模型快速高效的推理，以其 PagedAttention 算法而闻名。Model Runner V2 是 vLLM 核心执行引擎的重新实现，旨在实现更清晰、更模块化、更高效的设计，以提高性能并减少技术债务。KV 缓存自动调整大小功能动态管理分配给键值 (KV) 缓存的内存，KV 缓存存储过去的注意力状态，尤其是在长上下文长度下，会消耗大量 GPU 内存。推测解码是一种优化技术，它使用一个更小、更快的“草稿”模型来提议多个 token，然后由更大的“目标”模型在单次前向传递中验证这些 token，从而显著降低推理延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm-website-m20r6h0mr-inferact-inc.vercel.app/blog/mrv2">Model Runner V 2 : A Modular and Faster Core for vLLM | vLLM Blog</a></li>
<li><a href="https://wideareaai.com/blog/how-much-vram-do-you-need">How much VRAM do you actually need? The honest LLM sizing guide</a></li>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/">An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog</a></li>

</ul>
</details>

**标签**: `#LLM Inference`, `#vLLM`, `#Performance Optimization`, `#AI/ML Frameworks`, `#GPU Computing`

---

<a id="item-2"></a>
## [Shopify is moving from React Native back to Swift and Kotlin](https://shopify.engineering/back-to-native) ⭐️ 9.0/10

Shopify is migrating its mobile applications from React Native back to native Swift and Kotlin, a significant move for a major company, reportedly enabled by leveraging LLMs for the large-scale code migration.

hackernews · fnthawar2 · Sep 10, 14:09

**标签**: `#Mobile Development`, `#React Native`, `#Native Development`, `#LLMs`, `#Software Migration`

---

<a id="item-3"></a>
## [Quoting Calif Research](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research 展示了 WeWorm，一个通过微信通话传播的零点击蠕虫，并强调 AI 显著加速了漏洞发现和利用开发过程。

rss · Simon Willison · Sep 10, 00:56

**标签**: `#AI安全`, `#网络安全`, `#零点击漏洞`, `#移动安全`, `#AI伦理`

---

<a id="item-4"></a>
## [🌙 月之暗面秘密递交港股 IPO 申请，新一轮融资投前估值 500 亿美元  月之暗面（Kimi）已以保密形式向港交所递交 A1 文件，正式启动港股 IPO，公](https://t.me/zaihuapd/43743) ⭐️ 9.0/10

月之暗面（Kimi）已秘密递交港股 IPO 申请，并以 500 亿美元投前估值推进新一轮融资，显示出其在 AI 大模型领域的快速增长和市场认可。

telegram · zaihuapd · Sep 10, 10:58

**标签**: `#AI产业`, `#IPO`, `#估值`, `#大语言模型`, `#中国科技`

---

<a id="item-5"></a>
## [More questions about whether researchers can trust OpenAI with unpublished math](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

Researchers are questioning OpenAI's ethical practices concerning the use of unpublished mathematical ideas shared during model collaborations, raising concerns about potential unattributed publication of concepts.

hackernews · pred_ · Sep 10, 06:49

**标签**: `#AI Ethics`, `#Research Integrity`, `#Intellectual Property`, `#OpenAI`, `#Scientific Collaboration`

---

<a id="item-6"></a>
## [Cognition launches new SWE-2 model, Rivaling Fable 5.1 and GPT-Astra](https://cognition.com/blog/swe-2) ⭐️ 8.0/10

Cognition announced SWE-2, a new AI coding model claiming to rival top performers, but the community expresses significant skepticism about its benchmarks, generalization, and the company's history, while also debating the value of closed-weight models.

hackernews · seelos · Sep 10, 15:29

**标签**: `#AI`, `#Large Language Models`, `#Benchmarking`, `#Software Engineering`, `#Open Source`

---

<a id="item-7"></a>
## [.blend URL Viewer](https://simonwillison.net/2026/Sep/9/blender-viewer/) ⭐️ 8.0/10

Simon Willison 发布了一个新的".blend URL Viewer"工具，并分享了他使用 ChatGPT Images 2.5 生成法贝热彩蛋图像的实验，这反映了他对将 GPT-6 Astra 等 AI 模型与 Blender 结合的持续探索。

rss · Simon Willison · Sep 9, 23:58

**标签**: `#Blender`, `#AI`, `#Tools`, `#Generative AI`, `#3D Modeling`

---

<a id="item-8"></a>
## [🤖 DeepSeek V4.1 Flash：更强、更快、更普惠](https://mp.weixin.qq.com/s/qg0NU3NNUbp1co2PdkAPAg) ⭐️ 8.0/10

DeepSeek 正式发布了 V4.1 Flash 模型，这是其全新模型结构系列中最小尺寸的模型，采用 552B Causal-Encoder-Decoder 结构并原生支持多模态视觉理解，现已上线 DeepSeek API。

telegram · zaihuapd · Sep 10, 05:54

**标签**: `#AI模型`, `#大语言模型`, `#多模态AI`, `#API更新`, `#DeepSeek`

---

<a id="item-9"></a>
## [中国 AI 芯片厂商涨价，HBM 短缺成为新瓶颈](https://www.reuters.com/world/asia-pacific/chinas-ai-chipmakers-raise-prices-high-bandwidth-memory-shortage-bites-2026-09-10/) ⭐️ 8.0/10

由于全球高带宽存储器（HBM）短缺和美国出口限制，中国 AI 芯片厂商如华为和寒武纪已大幅上调产品价格，HBM 短缺正成为中国 AI 芯片产业扩张的新瓶颈。

telegram · zaihuapd · Sep 10, 09:29

**标签**: `#AI芯片`, `#HBM`, `#供应链`, `#市场分析`, `#地缘政治`

---

<a id="item-10"></a>
## [腾讯混元发布开源音频编辑模型 AuK](https://x.com/TencentHunyuan/status/2097996926876795197) ⭐️ 8.0/10

腾讯混元发布了开源的 AuK 音频编辑模型及其加速版本 AuK-Flash，该模型可通过自然语言指令和参考音频统一完成语音生成与编辑，支持多种高级功能。

telegram · zaihuapd · Sep 10, 11:56

**标签**: `#AI Audio`, `#Open Source`, `#Speech Processing`, `#Natural Language Processing`, `#Machine Learning`

---

<a id="item-11"></a>
## [Anthropic 前研究员警告 AI 可能是人类创造的最危险技术](https://x.com/FoxNews/status/2097815633828172097) ⭐️ 8.0/10

Anthropic 前研究员 Jacob Coxon 警告称，AI 可能是人类最危险的技术，并批评 Anthropic 和 OpenAI 等公司将模型竞争置于安全之上，呼吁全球合作以避免灾难。

telegram · zaihuapd · Sep 10, 13:31

**标签**: `#AI安全`, `#AI伦理`, `#AI发展`, `#科技风险`, `#全球合作`

---

<a id="item-12"></a>
## [Technique for Manipulating Satellite Photos Now Reveals Ancient Images (2025)](https://spinoff.nasa.gov/Manipulating_Satellite_Photos_Now_Reveals_Ancient_Images) ⭐️ 7.0/10

一项最初用于卫星照片的 NASA 图像处理技术（Decorrelation Stretch）现已被成功应用于揭示古代岩画和其他隐藏图像，为考古学和文化遗产研究提供了新工具。

hackernews · gumby · Sep 10, 15:29

**标签**: `#图像处理`, `#考古学`, `#遥感`, `#信号处理`, `#文化遗产`

---

<a id="item-13"></a>
## [📱 海外科技博主曝华为相关推广要求隐藏赞助标识  科技博主 GregsGadgets 称，在 iPhone 发布前后，华为给他们的一份相关推广简报要求创作者不要](https://t.me/zaihuapd/43735) ⭐️ 7.0/10

多位海外科技博主爆料称，华为在推广其产品时要求创作者隐藏赞助标识，此举涉嫌违反美国联邦贸易委员会（FTC）的规定并损害受众知情权。

telegram · zaihuapd · Sep 10, 05:50

**标签**: `#科技伦理`, `#数字营销`, `#KOL营销`, `#华为`, `#FTC合规`

---

<a id="item-14"></a>
## [Google 将 Gemini 桌面应用带到 Windows](https://9to5google.com/2026/09/10/gemini-windows-app/) ⭐️ 7.0/10

Google 已为 Windows 10 和 11 推出了 Gemini 桌面应用，支持 Alt + Space 唤起，并提供 Connected Apps、Gemini Spark 个人 AI 代理以及图像和视频生成功能，未来计划增加更多原生桌面功能。

telegram · zaihuapd · Sep 10, 23:27

**标签**: `#AI助手`, `#Google Gemini`, `#Windows应用`, `#桌面AI`, `#产品发布`

---