---
layout: default
title: "Horizon Summary: 2026-05-03 (ZH)"
date: 2026-05-03
lang: zh
---

> From 22 items, 8 important content pieces were selected

---

1. [Dav2d：下一代 AV2 视频标准的超高速开源解码器](#item-1) ⭐️ 9.0/10
2. [PyPI 包 lightning 遭供应链攻击，窃取开发者凭证并毒化仓库](#item-2) ⭐️ 9.0/10
3. [白宫反对 Anthropic 扩大 Mythos 模型使用范围  Anthropic 提议将 AI 模型 Mythos 的使用权限从约 50 家实体扩展至约 1](#item-3) ⭐️ 9.0/10
4. [🤖 DeepSeek-V4 的预览版本正式上线并同步开源，极其便宜大碗且适配 Agent  相比前代模型，DeepSeek-V4-Pro 的 Agent 能力显](#item-4) ⭐️ 9.0/10
5. [VS Code inserting 'Co-Authored-by Copilot' into commits regardless of usage](#item-5) ⭐️ 8.0/10
6. [黑钱组织付费让 TikTok 网红渲染中国 AI 威胁](#item-6) ⭐️ 8.0/10
7. [Do_not_track](#item-7) ⭐️ 7.0/10
8. [iNaturalist Sightings](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Dav2d：下一代 AV2 视频标准的超高速开源解码器](https://code.videolan.org/videolan/dav2d) ⭐️ 9.0/10

Dav2d 已发布，成为 Alliance for Open Media (AOMedia) 下一代视频编码标准 AV2 最快的开源解码器。这个新的解码器支持 AV2，预计其压缩效率将比前身 AV1 提高 30%。 这一进展意义重大，因为 AV2 增强的压缩效率对于以更低比特率实现高质量视频流媒体至关重要，满足了数字媒体领域不断变化的需求。像 Dav2d 这样快速、开源解码器的推出，是 AV2 标准在各种平台和应用中广泛采用和实施的关键推动因素。 Dav2d 专门设计为小巧、便携且在所有平台上都极其快速，使其成为解码 AV2 内容的高效解决方案。AV2 标准由 AOMedia 开发，建立在 AV1 的基础上，旨在提供卓越的压缩效率，其最终规范预计将于 2025 年底发布。

hackernews · dabinat · May 2, 17:32

**背景**: 视频编码标准，也称为视频编解码器，对于压缩和解压缩数字视频数据至关重要，能够实现高效的存储和流媒体传输。AV1 (AOMedia Video 1) 是由领先科技公司组成的联盟 Alliance for Open Media (AOMedia) 开发的一种开放、免版税的视频编码格式。AV2 是 AOMedia 的下一代标准，它建立在 AV1 的基础上，旨在进一步提高互联网视频的压缩效率。解码器，例如 Dav2d，是一种将压缩视频数据转换回可观看格式的软件或硬件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AV1">AV1 - Wikipedia</a></li>
<li><a href="https://aomedia.org/">Alliance for Open Media</a></li>

</ul>
</details>

**社区讨论**: 社区对 AV2 表现出热情，强调其与 AV1 相比可降低 30% 比特率的潜力，并认可 Dav2d 是关键一步。然而，大家也实际地认识到，尽管 AV2 的最终规范预计在 2025 年底发布，但开发可用的编码器（类似于 SVT-AV1 的经验）可能需要额外的时间。

**标签**: `#Video Codec`, `#AV2`, `#Decoder`, `#Compression`, `#Streaming`

---

<a id="item-2"></a>
## [PyPI 包 lightning 遭供应链攻击，窃取开发者凭证并毒化仓库](https://socket.dev/blog/lightning-pypi-package-compromised) ⭐️ 9.0/10

PyPI 包 lightning 的 2.6.2 和 2.6.3 版本遭遇供应链攻击，恶意代码窃取开发者凭证并毒化仓库，建议用户立即移除受影响版本并轮换密钥。

telegram · zaihuapd · May 2, 00:36

**标签**: `#供应链攻击`, `#PyPI安全`, `#凭证窃取`, `#恶意软件`, `#深度学习`

---

<a id="item-3"></a>
## [白宫反对 Anthropic 扩大 Mythos 模型使用范围  Anthropic 提议将 AI 模型 Mythos 的使用权限从约 50 家实体扩展至约 1](https://t.me/zaihuapd/41172) ⭐️ 9.0/10

白宫以国家安全为由，反对 Anthropic 将其能发现和利用软件漏洞的 Mythos AI 模型的使用权限从约 50 家实体扩展至约 120 家。

telegram · zaihuapd · May 2, 01:48

**标签**: `#AI政策`, `#国家安全`, `#AI监管`, `#Anthropic`, `#网络安全`

---

<a id="item-4"></a>
## [🤖 DeepSeek-V4 的预览版本正式上线并同步开源，极其便宜大碗且适配 Agent  相比前代模型，DeepSeek-V4-Pro 的 Agent 能力显](https://t.me/zaihuapd/41185) ⭐️ 9.0/10

DeepSeek has launched the preview version of its open-source DeepSeek-V4 LLM, featuring significantly enhanced agent capabilities, claiming to outperform other open-source models and offer cost-effective API services.

telegram · zaihuapd · May 3, 02:21

**标签**: `#Large Language Models`, `#Open Source AI`, `#AI Agents`, `#DeepSeek`, `#Model Performance`

---

<a id="item-5"></a>
## [VS Code inserting 'Co-Authored-by Copilot' into commits regardless of usage](https://github.com/microsoft/vscode/pull/310226) ⭐️ 8.0/10

VS Code 正在默认将 'Co-Authored-by Copilot' 插入到 Git 提交中，无论是否实际使用了 Copilot，这引发了关于提交历史完整性和对 AI 集成开发工具信任的重大争议。

hackernews · indrora · May 2, 19:57

**标签**: `#软件工程`, `#开发者工具`, `#AI伦理`, `#Git`, `#VS Code`

---

<a id="item-6"></a>
## [黑钱组织付费让 TikTok 网红渲染中国 AI 威胁](https://www.wired.com/story/super-pac-backed-by-openai-and-palantir-is-paying-tiktok-influencers-to-fear-monger-about-china/) ⭐️ 8.0/10

一个名为“Build American AI”的“黑钱组织”，由与 OpenAI 和 Palantir 关联人物支持的超级政治行动委员会“Leading the Future”资助，正以每条视频约 5000 美元的价格，付费给 TikTok 和 Instagram 网红，让他们散布“中国 AI 威胁论”。这些网红先推广美国 AI 创新，然后直接渲染中国技术崛起将危及美国就业与隐私。 这一揭露引发了关于在 AI 等关键技术领域塑造公众舆论的透明度和宣传的重大伦理和政治担忧，可能侵蚀公众信任并影响政策决策。它凸显了科技公司、政治行动和信息传播之间复杂的相互作用，影响着 AI 的负责任发展和公众认知。 营销机构 SM4 负责招募生活类博主参与此次宣传活动，他们每条视频获得约 5000 美元报酬，用于在 TikTok 和 Instagram 上发布内容。包括媒体学教授在内的批评者认为，网红仅标注“广告”而不披露资金来源的做法构成了宣传，并腐蚀了民主进程。

telegram · zaihuapd · May 2, 02:43

**标签**: `#AI伦理`, `#地缘政治`, `#社交媒体影响`, `#宣传`, `#科技政策`

---

<a id="item-7"></a>
## [Do_not_track](https://donottrack.sh/) ⭐️ 7.0/10

The "Do_not_track" initiative proposes a standard for opting out of telemetry, sparking a high-value community discussion about the persistent challenges of user privacy, default tracking, and the practical difficulties developers face in disabling data collection in modern software.

hackernews · RubyGuy · May 2, 17:40

**标签**: `#Privacy`, `#Telemetry`, `#Software Engineering`, `#User Control`, `#Open Standards`

---

<a id="item-8"></a>
## [iNaturalist Sightings](https://simonwillison.net/2026/May/1/inat-sightings/#atom-everything) ⭐️ 7.0/10

Simon Willison 在露营期间使用手机、Claude Code 和 Git scraping 技术，开发了一个名为“iNaturalist Sightings”的个人工具，用于获取并按时间和距离对他的 iNaturalist 观察记录进行分组。

rss · Simon Willison · May 1, 19:35

**标签**: `#软件工程`, `#数据处理`, `#Git Scraping`, `#AI辅助开发`, `#个人项目`

---