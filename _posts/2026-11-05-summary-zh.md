---
layout: default
title: "Horizon Summary: 2026-11-05 (ZH)"
date: 2026-11-05
lang: zh
---

> From 33 items, 15 important content pieces were selected

---

1. [Residential proxies detected on White House network](#item-1) ⭐️ 9.0/10
2. [Go 语言新的 JSON API](#item-2) ⭐️ 9.0/10
3. [飞机噪音多普勒效应泄露视频拍摄地点](#item-3) ⭐️ 9.0/10
4. [腾讯向甲骨文租用 10 万枚 AI 芯片  腾讯与甲骨文签订价值约 70 亿美元的租约，租用约 10 万枚在中国买不到的先进 AI 芯片，成为其史上最大海外租赁](#item-4) ⭐️ 9.0/10
5. [🤖 KIMI K3.1-Pro 模型正式发布  Kimi 发布 K3.1 Pro，这是 K3.1 系列首款模型，定位为其目前最强的三万亿参数级开放权重模型，支持](#item-5) ⭐️ 9.0/10
6. [🤖 OpenAI 发布 ChatGPT Images 2.0 强化文本渲染与联网推理能力  OpenAI 推出基于 GPT Image 2 的新一代图像生成模型](#item-6) ⭐️ 9.0/10
7. [A thousand fewer paths to root](#item-7) ⭐️ 8.0/10
8. [Kimi K3.1 Pro model weights are out](#item-8) ⭐️ 8.0/10
9. [Qwen 3.8 27B on my laptop can interpret model weights, too](#item-9) ⭐️ 8.0/10
10. [🤖 Anthropic：蒸馏数据初步减少 90% 至 99%  Anthropic 10 月 12 日表示，初步证据显示，针对窃取 Claude 能力的模型蒸馏](#item-10) ⭐️ 8.0/10
11. [🐦 X 新版网页将慢网首帖时间缩至 2.7 秒](#item-11) ⭐️ 8.0/10
12. [Ripple-65B Preview: U.S. Open-Weight SOTA on Agentic Coding](#item-12) ⭐️ 7.0/10
13. [Cloudflare 上线个人 AI 代理流量分析与分级管控](#item-13) ⭐️ 7.0/10
14. [🍏 macOS 27.3 让 Markdown 文件可直接预览](#item-14) ⭐️ 7.0/10
15. [🤖 爆料：ChatGPT 使用记录出现 GPT 6.2 Astra 模型，疑似灰测  11 月 1 日，LINUX DO 上有用户发帖称，自己前一天测试时便发现](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Residential proxies detected on White House network](https://layer3intel.com/blog/residential-proxies-white-house-network) ⭐️ 9.0/10

一项网络安全分析发现，白宫网络中的设备存在住宅代理活动，主要发生在晚上，这表明是受感染的个人设备而非公共 Wi-Fi。

hackernews · Rasbora · Nov 4, 20:45

**标签**: `#网络安全`, `#网络安全`, `#国家安全`, `#代理网络`, `#设备入侵`

---

<a id="item-2"></a>
## [Go 语言新的 JSON API](https://go.dev/blog/jsonv2) ⭐️ 9.0/10

Go 语言推出了一个新的 `encoding/json/v2` API，旨在显著增强语言内部的 JSON 处理能力。此次更新代表了 Go 核心 JSON 库的一次重大修订，解决了长期存在的挑战并引入了新功能。 此次更新对 Go 开发者至关重要，因为 JSON 是一种基本的数据交换格式，改进的 API 可以带来更高效、更健壮、性能更好的应用程序。它反映了 Go 持续致力于完善其核心库并适应现代软件开发需求，将影响使用 Go 构建的各种服务和应用程序。 新的 `encoding/json/v2` API 引入了改进性能和灵活性的变化，一些开发者指出 `MarshalIndent` 的移除增加了迁移的复杂性。讨论还强调了 SIMD 等高级解析技术以及 `jsontext` 包在高性能、模式感知解析方面的实用性。

hackernews · olexsmir · Nov 4, 17:52

**背景**: JavaScript Object Notation (JSON) 是一种轻量级的数据交换格式，易于人类阅读和编写，也易于机器解析和生成。它被广泛用于网络应用程序中的数据传输，因此高效且健壮的 JSON 处理对于 Go 这样的现代编程语言来说是一项关键功能。最初的 `encoding/json` 包一直是核心组件，但不断变化的需求和性能要求促使了新版本的开发。

**社区讨论**: 社区普遍欢迎 `encoding/json/v2` API，尽管一些人对 `MarshalIndent` 等功能的移除以及相关的迁移工作表示担忧。讨论还围绕着 JSON 尽管看似简单但固有的复杂性、SIMD 等高级解析技术提升性能的潜力，以及 AI 在生成 Go 代码（甚至包括这些新 API）中日益增长的作用。

**标签**: `#Go`, `#JSON`, `#API Design`, `#Software Engineering`, `#Performance`

---

<a id="item-3"></a>
## [飞机噪音多普勒效应泄露视频拍摄地点](https://simonwillison.net/2026/Nov/3/a-sound-that-leaks-your-exact-location/) ⭐️ 9.0/10

安全研究员 Colsto 开发了一种新颖的开源情报（OSINT）技术，通过分析视频背景中几乎难以察觉的飞机噪音的多普勒曲线，并与公开的 ADS-B 飞行数据进行交叉比对，从而精确地确定视频的拍摄地点。这种方法能够根据飞机的速度、距离以及不同航班之间的间隔来精确推断视频的录制位置。 这一发现代表了开源情报（OSINT）能力的一项重大突破，展示了如何从看似无关紧要的音频数据中提取敏感的位置信息，从而引发了重要的隐私担忧。它突显了监视技术的日益复杂性以及意想不到的数据源揭示个人信息的潜力。 该技术涉及从音轨中螺旋桨飞机声音中提取多普勒频移曲线，并将其与存档的 ADS-B 飞行路径进行匹配，以估算录音位置。一个名为 `franken_doppler_finder` 的 Rust 命令行工具已被开发出来，用于自动化这一音频取证过程，并能生成带有置信半径的地图。

rss · Simon Willison · Nov 3, 05:32

**背景**: 多普勒效应描述了波（如声波）的频率或波长相对于波源移动的观察者发生变化的现象。当声源向观察者移动时，音调听起来更高；当声源远离时，音调听起来更低。广播式自动相关监视（ADS-B）是一种飞机监视技术，飞机通过卫星导航系统确定自身位置，并定期广播这些数据，从而使它们能够被地面站和其他飞机追踪。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bilibili.com/video/BV1xb4M6zEfy/">仅凭1分钟背景音，我用多普勒效应精准锁定了录音地点 | colsto_哔哩哔... franken_doppler_finder：基于多普勒曲线与 ADS-B 的音频定位工具 基于多普勒效应的声学信号分析算法 - 百度文库 【声学基础】多普勒效应（Doppler Effect） - 知乎 多普勒效应原理与应用：从声音变调到雷达测速的全面解析-CSDN博客 MATLAB多普勒效应仿真：洒水车音频物理实验全解析-CSDN博客 飞机多普勒曲线定位术：任何有声视频可被反推拍摄地点· AGI Hunt</a></li>
<li><a href="https://zh.wikipedia.org/wiki/广播式自动相关监视">广播式自动相关监视 - 维基百科，自由的百科全书</a></li>
<li><a href="https://kaiyuanbang.cn/zh-cn/repo/dicklesworthstone-franken-doppler-finder.html">franken_doppler_finder：基于多普勒曲线与 ADS-B 的音频定位工具</a></li>

</ul>
</details>

**社区讨论**: 这一发现引起了广泛关注，尤其是在 Lobste.rs 等平台上，它被誉为“天才般的开源情报（OSINT）作品”。社区讨论反映了对该技术独创性的惊叹以及对其深远隐私影响的担忧。

**标签**: `#OSINT`, `#隐私`, `#地理定位`, `#音频分析`

---

<a id="item-4"></a>
## [腾讯向甲骨文租用 10 万枚 AI 芯片  腾讯与甲骨文签订价值约 70 亿美元的租约，租用约 10 万枚在中国买不到的先进 AI 芯片，成为其史上最大海外租赁](https://t.me/zaihuapd/44912) ⭐️ 9.0/10

腾讯与甲骨文签订了一项价值 70 亿美元的五年期租约，在东南亚租用 10 万枚先进 AI 芯片，以规避美国出口限制并加速其 AI 模型开发。

telegram · zaihuapd · Nov 4, 11:01

**标签**: `#AI芯片`, `#地缘政治`, `#云基础设施`, `#腾讯`, `#出口管制`

---

<a id="item-5"></a>
## [🤖 KIMI K3.1-Pro 模型正式发布  Kimi 发布 K3.1 Pro，这是 K3.1 系列首款模型，定位为其目前最强的三万亿参数级开放权重模型，支持](https://t.me/zaihuapd/44920) ⭐️ 9.0/10

Kimi officially launched its K3.1-Pro model, touted as its strongest three-trillion parameter-level open-weight model with a 1 million token context, demonstrating superior performance in programming and other complex tasks compared to leading models.

telegram · zaihuapd · Nov 4, 15:47

**标签**: `#LLM`, `#Open-weight AI`, `#Context Window`, `#AI Agents`, `#Programming AI`

---

<a id="item-6"></a>
## [🤖 OpenAI 发布 ChatGPT Images 2.0 强化文本渲染与联网推理能力  OpenAI 推出基于 GPT Image 2 的新一代图像生成模型](https://t.me/zaihuapd/44923) ⭐️ 9.0/10

OpenAI 发布了 ChatGPT Images 2.0，该模型通过引入逻辑推理和联网搜索能力，实现了生成多张视觉一致的图像、支持复杂构图，并显著解决了 AI 绘图中的文本拼写难题，尤其对非拉丁语系表现优异。

telegram · zaihuapd · Nov 4, 23:42

**标签**: `#AI`, `#Generative AI`, `#Image Generation`, `#OpenAI`, `#Machine Learning`

---

<a id="item-7"></a>
## [A thousand fewer paths to root](https://openai.com/index/a-thousand-fewer-paths-to-root/) ⭐️ 8.0/10

OpenAI 的工作显著减少了近千个特权升级漏洞，引发了社区关于系统安全、内核复杂性和实际影响的高质量讨论。

hackernews · dangelosaurus · Nov 4, 23:33

**标签**: `#系统安全`, `#特权升级`, `#Linux内核`, `#网络安全`, `#漏洞管理`

---

<a id="item-8"></a>
## [Kimi K3.1 Pro model weights are out](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) ⭐️ 8.0/10

月之暗面发布了 Kimi K3.1 Pro 模型的开放权重，引发了社区对其性能、硬件需求和第三方推理支持的广泛讨论。

hackernews · abrarthought · Nov 4, 15:30

**标签**: `#LLMs`, `#Model Weights`, `#AI Inference`, `#AI Benchmarking`, `#Open Models`

---

<a id="item-9"></a>
## [Qwen 3.8 27B on my laptop can interpret model weights, too](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/) ⭐️ 8.0/10

Simon Willison 演示了 Qwen 3.8 27B 模型在笔记本电脑上能够解释和修改神经网络权重，从而验证了最近一篇论文中提出的“权重空间编程”概念。

rss · Simon Willison · Nov 3, 16:29

**标签**: `#AI/ML`, `#大型语言模型`, `#模型解释`, `#权重空间编程`, `#本地AI`

---

<a id="item-10"></a>
## [🤖 Anthropic：蒸馏数据初步减少 90% 至 99%  Anthropic 10 月 12 日表示，初步证据显示，针对窃取 Claude 能力的模型蒸馏](https://t.me/zaihuapd/44911) ⭐️ 8.0/10

Anthropic 宣布，针对窃取 Claude 能力的模型蒸馏攻击，其新防护措施已初步将提取数据减少 90-99%，并已封禁数万相关账号。

telegram · zaihuapd · Nov 4, 10:16

**标签**: `#AI安全`, `#大型语言模型`, `#知识产权`, `#Anthropic`, `#模型蒸馏`

---

<a id="item-11"></a>
## [🐦 X 新版网页将慢网首帖时间缩至 2.7 秒](http://x.com/) ⭐️ 8.0/10

X 的新版网页通过采用单一服务器和流式 HTML 渲染等技术，成功将慢速网络下个人主页首帖的加载时间从 22 秒以上大幅缩短至 2.7 秒。

telegram · zaihuapd · Nov 4, 23:32

**标签**: `#Web性能`, `#前端工程`, `#系统架构`, `#性能优化`, `#用户体验`

---

<a id="item-12"></a>
## [Ripple-65B Preview: U.S. Open-Weight SOTA on Agentic Coding](https://www.ricursive.com/ripple) ⭐️ 7.0/10

Ripple-65B is a new 65B open-weight large language model from Ricursive, claiming U.S. open-weight SOTA for agentic coding, though community discussion critically debates this claim and highlights practical inference challenges.

hackernews · Philpax · Nov 4, 18:53

**标签**: `#Large Language Models`, `#Agentic AI`, `#Code Generation`, `#Open-weight Models`, `#AI Benchmarking`

---

<a id="item-13"></a>
## [Cloudflare 上线个人 AI 代理流量分析与分级管控](https://blog.cloudflare.com/personal-agents-visibility-control/) ⭐️ 7.0/10

Cloudflare 推出新功能，允许用户分析和分级管控个人 AI 代理的流量，包括新增分析类别、详细统计和灵活的访问策略。

telegram · zaihuapd · Nov 4, 15:42

**标签**: `#Cloudflare`, `#AI Agents`, `#Traffic Management`, `#Web Security`, `#Analytics`

---

<a id="item-14"></a>
## [🍏 macOS 27.3 让 Markdown 文件可直接预览](https://www.macrumors.com/2026/11/04/macos-27-3-makes-markdown-files-easier-to-read/) ⭐️ 7.0/10

macOS 27.3 在 Quick Look 中加入了原生 Markdown 渲染功能，使用户可以直接在 Finder 中预览格式化的.md 文件，无需额外安装软件。

telegram · zaihuapd · Nov 4, 16:36

**标签**: `#macOS`, `#Markdown`, `#Quick Look`, `#开发者工具`, `#用户体验`

---

<a id="item-15"></a>
## [🤖 爆料：ChatGPT 使用记录出现 GPT 6.2 Astra 模型，疑似灰测  11 月 1 日，LINUX DO 上有用户发帖称，自己前一天测试时便发现](https://t.me/zaihuapd/44924) ⭐️ 7.0/10

有用户报告在 ChatGPT 使用记录中发现了“GPT 6.2 Astra”模型，疑似 OpenAI 正在灰度测试新的 AI 模型。

telegram · zaihuapd · Nov 5, 00:48

**标签**: `#AI模型`, `#OpenAI`, `#ChatGPT`, `#爆料`, `#产品开发`

---