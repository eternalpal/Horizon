---
layout: default
title: "Horizon Summary: 2026-11-23 (ZH)"
date: 2026-11-23
lang: zh
---

> From 22 items, 12 important content pieces were selected

---

1. [Z.ai 发布 GLM-5.3-Flash：18B 激活参数，价格降至上代十分之一](#item-1) ⭐️ 9.0/10
2. [A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth](#item-2) ⭐️ 8.0/10
3. [Muru：面向 Python Web 应用的 AI 辅助 Rust 服务器](#item-3) ⭐️ 8.0/10
4. [群联推出 Pascari 太空 SSD 系列用于轨道数据中心](#item-4) ⭐️ 8.0/10
5. [谷歌搭建模拟互联网测试 Chrome AI 代理](#item-5) ⭐️ 8.0/10
6. [字节跳动与红杉领投机器人公司 1.4 亿美元融资  中国具身智能初创企业 X Square Robot 完成 10 亿元人民币（约合 1.4 亿美元）的 A++ 轮](#item-6) ⭐️ 8.0/10
7. [🚘 特斯拉开始推送 FSD v15  特斯拉今日在海外推出 FSD v15。](#item-7) ⭐️ 8.0/10
8. [美 FCC 拟禁止中国三大运营商直接获取美国号码资源  美国联邦通信委员会 10 月 29 日表示，将于 11 月 19 日表决一项提案，以国家安全、防范诈骗骚](#item-8) ⭐️ 7.0/10
9. [腾讯 AI 语音输入工具 Chatterfly 开启限时内测](#item-9) ⭐️ 7.0/10
10. [超级厄尔尼诺海温破纪录，粮食援助承压](#item-10) ⭐️ 7.0/10
11. [摩尔线程产品经理：庐山 GPU 显存 64 GB](#item-11) ⭐️ 7.0/10
12. [微软新服务器系统默认跑不了 32 位老软件，需要可手动装回](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Z.ai 发布 GLM-5.3-Flash：18B 激活参数，价格降至上代十分之一](https://t.me/zaihuapd/45309) ⭐️ 9.0/10

Z.ai 发布了 GLM-5.3-Flash，这是其首个原生多模态模型，拥有 18B 激活参数，性能超越 GLM-5.2 并接近 Claude Opus 4.8。该模型的价格大幅降低至上代的十分之一，限时优惠期间 API 输入价格低至每百万 Tokens 0.075 美元。 此次发布通过大幅降低成本，显著提高了先进 AI 能力的普惠性，使高性能多模态 AI 更易于开发者和企业使用。这种价格下降对 AI 应用开发具有变革性影响，并加剧了市场竞争，有望加速各行业的创新。 GLM-5.3-Flash 的总参数为 320B，激活参数为 18B，其性能超越 GLM-5.2 并接近 Claude Opus 4.8。在限时优惠期间，API 输入价格为每百万 Tokens 0.075 美元，缓存输入为 0.015 美元，输出为 0.25 美元，缓存存储暂时免费。

telegram · zaihuapd · Nov 23, 04:47

**背景**: GLM 模型是由清华大学开发的大语言模型，通常基于 Transformer 架构，并可能采用 MoE（专家混合）结构以提高效率。原生多模态模型从设计之初就将文本、图像等多种模态统一建模，提供统一的理解能力，而非独立处理。在大语言模型中，总参数指模型的整体容量，而激活参数是针对特定输入实际参与计算的较小参数子集，这对于优化推理速度和资源使用至关重要，尤其是在稀疏的 MoE 架构中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.csdn.net/u012856866/article/details/147147164">【大模型】GLM模型架构及原理详解-CSDN博客</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2036759233539077945">原生多模态模型技术全景 - 知乎 - 知乎专栏</a></li>
<li><a href="https://blog.csdn.net/lovingsoft/article/details/165891582">大模型什么是激活参数，分清总参数与激活参数，看懂 MoE 宣传陷阱_大...</a></li>

</ul>
</details>

**标签**: `#AI模型`, `#大语言模型`, `#多模态AI`, `#API定价`, `#成本效益`

---

<a id="item-2"></a>
## [A Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth](https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth) ⭐️ 8.0/10

This guide introduces beginners to running local AI models using tools like Inkling, Qwen, and Unsloth, complemented by a robust community discussion offering practical, cost-effective hardware solutions and setup advice.

hackernews · Retell15 · Nov 22, 21:01

**标签**: `#Local AI`, `#LLM`, `#Hardware`, `#AI Deployment`, `#Beginner Guide`

---

<a id="item-3"></a>
## [Muru：面向 Python Web 应用的 AI 辅助 Rust 服务器](https://simonwillison.net/2026/Nov/21/muru/) ⭐️ 8.0/10

mod_wsgi 的创建者 Graham Dumpleton 推出了 Muru，这是一个新的由 AI 辅助的 Rust 服务器，旨在为开发和生产环境中的 Python ASGI 和 WSGI 应用程序提供最佳服务工具。该项目旨在改进其在 Python Web 应用程序服务领域二十年的经验。 鉴于 Graham Dumpleton 在 mod_wsgi 方面二十年的经验，这一发展具有高度重要性，预示着 Python Web 服务基础设施可能迎来重大进步。Muru 旨在提供“最佳工具”的抱负，可能会为 Python 应用程序的性能、可靠性和易用性设定新标准。 Muru 采用以性能和安全性著称的 Rust 构建，并在其设计中融入了 AI 辅助，这反映了其创建者的一种“生活方式选择”。该项目同时支持 WSGI 和 ASGI 接口，这对于现代和传统的 Python Web 框架至关重要，并且 Dumpleton 正在发布极其详细的开发日志。

rss · Simon Willison · Nov 21, 23:56

**背景**: WSGI（Web 服务器网关接口）是 Python Web 应用程序与 Web 服务器通信的长期标准，而 ASGI（异步服务器网关接口）是其现代继任者，支持 WebSocket 等异步功能。由 Graham Dumpleton 创建的 mod_wsgi 等服务器在历史上对于高效部署 Python 应用程序至关重要。

**标签**: `#Python`, `#Web Server`, `#ASGI/WSGI`, `#Rust`, `#Infrastructure`

---

<a id="item-4"></a>
## [群联推出 Pascari 太空 SSD 系列用于轨道数据中心](https://videocardz.com/newz/phison-announces-488tb-of-ssd-storage-for-space-data-centers-pricing-expected-to-be-astronomical) ⭐️ 8.0/10

群联（Phison）正式推出了其 Pascari 太空 SSD 系列，专为航天器和轨道数据中心设计，Lonestar Data Holdings 计划在 2027 年上半年在其 StarVault-001 轨道数据中心部署 488 TB 的此类固态硬盘。这些 SSD 单盘容量最高可达 128 TB，并通过 pSLC 技术将写入寿命提高多达 60 倍。 这一发展对于推进在轨数据处理和存储能力至关重要，它解决了太空极端环境的挑战，并为未来的天基计算基础设施奠定了基础。这标志着在地球之外实现更自主、数据密集型操作迈出了重要一步。 Pascari 太空 SSD 系列包括飞行关键型、主存储型和轨道数据中心型，Lonestar 的 StarVault-001 轨道数据中心预计将从总计 488 TB 的部署容量中获得约 370 TB 的可用容量。群联强调，在某些型号中使用 pSLC 技术可将写入寿命延长多达 60 倍，这对于天基存储的寿命至关重要。

telegram · zaihuapd · Nov 22, 10:31

**背景**: 固态硬盘（SSD）是一种使用集成电路组件作为存储介质来持久存储数据的设备，由于没有移动部件，与传统硬盘（HDD）相比，它提供更快的性能和更高的耐用性。轨道数据中心是设计在太空中（通常是低地球轨道 LEO）运行的设施，旨在为天基资产提供更近的数据处理和存储，或用于需要极端安全或环境隔离的应用。pSLC（伪单层单元）是一种 NAND 闪存技术，通过模拟 SLC 的方式写入数据来提高耐用性，即使底层物理单元是 MLC 或 TLC，从而增加擦写循环次数。

**标签**: `#Space Technology`, `#SSDs`, `#Data Storage`, `#Orbital Computing`

---

<a id="item-5"></a>
## [谷歌搭建模拟互联网测试 Chrome AI 代理](https://www.landian.news/archives/128701.html) ⭐️ 8.0/10

Google has developed 'Mirror Dimension,' a simulated internet with thousands of websites, to rigorously test its Chrome AI agent in isolation, focusing on security against attacks like prompt injection.

telegram · zaihuapd · Nov 23, 01:30

**标签**: `#AI Agents`, `#AI Safety`, `#Software Testing`, `#Browser Technology`, `#Cybersecurity`

---

<a id="item-6"></a>
## [字节跳动与红杉领投机器人公司 1.4 亿美元融资  中国具身智能初创企业 X Square Robot 完成 10 亿元人民币（约合 1.4 亿美元）的 A++ 轮](https://t.me/zaihuapd/45305) ⭐️ 8.0/10

中国具身智能初创企业 X Square Robot 完成了由字节跳动和红杉中国联合领投的 1.4 亿美元 A++轮融资，成为唯一一家同时获得字节跳动、美团和阿里巴巴集团支持的具身智能公司。

telegram · zaihuapd · Nov 23, 02:02

**标签**: `#AI投资`, `#具身智能`, `#机器人`, `#风险投资`, `#中国科技`

---

<a id="item-7"></a>
## [🚘 特斯拉开始推送 FSD v15  特斯拉今日在海外推出 FSD v15。](https://t.me/zaihuapd/45307) ⭐️ 8.0/10

特斯拉已开始在海外推送 FSD v15，该版本在安全关键场景处理能力上提升了 25 倍，并引入了“Tesla Reality View”可视化界面以及多项驾驶体验优化。

telegram · zaihuapd · Nov 23, 03:33

**标签**: `#自动驾驶`, `#AI系统`, `#软件更新`, `#用户体验`, `#车载技术`

---

<a id="item-8"></a>
## [美 FCC 拟禁止中国三大运营商直接获取美国号码资源  美国联邦通信委员会 10 月 29 日表示，将于 11 月 19 日表决一项提案，以国家安全、防范诈骗骚](https://t.me/zaihuapd/45292) ⭐️ 7.0/10

美国联邦通信委员会（FCC）计划投票通过一项提案，以国家安全和防范诈骗为由，禁止中国三大运营商及相关 VoIP 服务商直接获取美国电话号码资源。

telegram · zaihuapd · Nov 22, 06:44

**标签**: `#电信`, `#监管政策`, `#国家安全`, `#地缘政治`, `#FCC`

---

<a id="item-9"></a>
## [腾讯 AI 语音输入工具 Chatterfly 开启限时内测](https://chatterfly.tencent.com/) ⭐️ 7.0/10

腾讯发布了 AI 语音输入工具 Chatterfly，旨在通过理解上下文和整理口语来高效生成文稿并执行任务，目前正在 Windows、macOS 和 Android 平台进行限时内测。

telegram · zaihuapd · Nov 22, 12:36

**标签**: `#AI`, `#语音识别`, `#自然语言处理`, `#生产力工具`, `#腾讯`

---

<a id="item-10"></a>
## [超级厄尔尼诺海温破纪录，粮食援助承压](https://www.wired.com/story/how-this-years-super-el-nino-will-worsen-global-hunger/) ⭐️ 7.0/10

创纪录的超级厄尔尼诺现象预计将导致全球海温达到峰值，并在 2027 年前使额外 4900 万人陷入急性粮食不安全，而全球援助资金正在大幅下降。

telegram · zaihuapd · Nov 22, 14:09

**标签**: `#气候变化`, `#厄尔尼诺`, `#粮食安全`, `#人道主义危机`, `#全球影响`

---

<a id="item-11"></a>
## [摩尔线程产品经理：庐山 GPU 显存 64 GB](https://www.tomshardware.com/pc-components/gpus/moore-threads-next-lushan-gaming-gpu-could-pack-a-record-64gb-of-vram-doubles-the-rtx-5090s-32gb-lofty-claims-of-15x-gaming-and-50x-ray-tracing-over-mtt-s80) ⭐️ 7.0/10

据非官方消息，摩尔线程即将推出的庐山 GPU 有望配备 64GB 显存，并声称在游戏、光追和 AI 性能上将有大幅提升，预计在 12 月底正式发布。

telegram · zaihuapd · Nov 22, 15:11

**标签**: `#GPU`, `#显存`, `#摩尔线程`, `#AI硬件`, `#游戏硬件`

---

<a id="item-12"></a>
## [微软新服务器系统默认跑不了 32 位老软件，需要可手动装回](https://www.windowslatest.com/2026/11/23/32-bit-apps-days-are-numbered-as-microsoft-strips-support-bit-by-bit-starting-with-windows-server-2028-but-windows-11-is-safe-for-now/) ⭐️ 7.0/10

微软的 Windows Server 2028 将默认移除 32 位应用支持，但用户可手动重新安装以运行旧软件，此举旨在减少攻击面。

telegram · zaihuapd · Nov 23, 03:03

**标签**: `#Windows Server`, `#32位应用`, `#系统管理`, `#操作系统`, `#软件兼容性`

---