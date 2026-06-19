---
layout: default
title: "Horizon Summary: 2026-06-19 (ZH)"
date: 2026-06-19
lang: zh
---

> From 28 items, 7 important content pieces were selected

---

1. [研究发现 1 万个 GitHub 仓库分发木马恶意软件](#item-1) ⭐️ 9.0/10
2. [Apple 与 Intel 达成初步芯片代工协议  Apple 与 Intel 已达成初步协议，由 Intel 代工生产部分 Apple 设备所需的芯片。](#item-2) ⭐️ 9.0/10
3. [Ubiquiti 推出基于 ZFS 和 25GbE 的企业级 NAS](#item-3) ⭐️ 8.0/10
4. [Datasette Apps: Host custom HTML applications inside Datasette](#item-4) ⭐️ 8.0/10
5. [CS 6120: Advanced Compilers: The Self-Guided Online Course (2020)](#item-5) ⭐️ 7.0/10
6. [datasette-acl 0.6a0](#item-6) ⭐️ 7.0/10
7. [国家发改委：第三批 625 亿元国补 6 月底前下达](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [研究发现 1 万个 GitHub 仓库分发木马恶意软件](https://orchidfiles.com/github-repositories-distributing-malware/) ⭐️ 9.0/10

一名研究人员最近发现大约 1 万个 GitHub 仓库正在积极分发木马恶意软件，这表明软件供应链面临着广泛而重大的威胁。这种大规模的恶意活动涉及旨在诱捕自动化代理和不知情开发人员的新仓库。 这一发现凸显了开源软件供应链中的一个关键漏洞，因为开发人员和自动化系统经常从 GitHub 集成依赖项，这可能导致广泛的感染。它对任何依赖开源项目的组织或个人都构成风险，可能危及他们的系统和数据。 攻击者主要针对新仓库，并每隔几小时频繁删除并推送新提交，这种策略旨在使其恶意仓库出现在“最新更新”搜索的顶部，并诱捕自动化代理而非人类用户。这种方法旨在通过在部分依赖项搜索中出现来实现机会性感染。

hackernews · theorchid · Jun 18, 11:45

**背景**: 软件供应链安全是指用于保护软件组件从开发到部署的完整性和可信度的实践和技术。它确保应用程序中使用的所有代码和依赖项都没有恶意修改，这对于广泛使用 GitHub 等开源组件的情况至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.codacy.com/software-supply-chain-security">Software Supply Chain Security Explained</a></li>
<li><a href="https://www.comptiaexamprep.com/2025/11/supply-chain-security-explained-risks.html">ITF+, A+, Network+, Security +, CySA+: Supply Chain Security ...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论表达了对攻击者策略的强烈担忧，指出恶意行为者频繁更新仓库以出现在“最新更新”搜索中，并针对自动化代理而非人类用户。用户还分享了他们的合法项目被模仿或他们的名字与不相关的恶意仓库关联的个人经历，这强调了实际影响以及即使是经验丰富的工程师也很难区分合法代码和恶意代码。

**标签**: `#Cybersecurity`, `#Software Supply Chain`, `#Malware`, `#GitHub Security`, `#Open Source Security`

---

<a id="item-2"></a>
## [Apple 与 Intel 达成初步芯片代工协议  Apple 与 Intel 已达成初步协议，由 Intel 代工生产部分 Apple 设备所需的芯片。](https://t.me/zaihuapd/42031) ⭐️ 9.0/10

苹果与英特尔达成初步协议，由英特尔代工生产部分苹果设备所需的芯片，此举受到美国政府的深度推动，对双方及半导体行业具有重要战略意义。

telegram · zaihuapd · Jun 18, 09:19

**标签**: `#半导体`, `#芯片制造`, `#供应链`, `#苹果`, `#英特尔`

---

<a id="item-3"></a>
## [Ubiquiti 推出基于 ZFS 和 25GbE 的企业级 NAS](https://blog.ui.com/article/introducing-enterprise-nas) ⭐️ 8.0/10

Ubiquiti 推出了一款企业级网络附加存储 (NAS) 解决方案，该方案基于 ZFS 文件系统构建，配备双 25 千兆 SFP28 端口和冗余电源。这项新产品旨在为企业提供高性能且无月度订阅费用的存储选择。 Ubiquiti 凭借基于 ZFS、高速且无月费的解决方案进入企业级 NAS 市场，这可能会扰乱现有存储供应商，并为寻求经济高效、强大存储的企业提供有吸引力的替代方案。此举将 Ubiquiti 的生态系统从网络扩展到核心数据基础设施领域。 这款企业级 NAS 配备双 25 千兆 SFP28 端口和冗余电源，以增强弹性和性能，并利用以数据完整性和高级功能而闻名的 ZFS 文件系统。该产品定价为 3999 美元，采用无月度订阅费模式，这使其有别于许多基于订阅的企业解决方案。

hackernews · ksec · Jun 18, 14:24

**背景**: 网络附加存储 (NAS) 是一种专用的文件存储设备，允许多个用户和异构客户端设备通过网络从集中式磁盘容量中检索数据。ZFS 是一种结合了文件系统和逻辑卷管理器的技术，以其强大的数据完整性功能、快照能力和高效存储管理而闻名，因此在企业和数据密集型应用中广受欢迎。

**社区讨论**: 社区对 Ubiquiti 进入 NAS 领域并采用 ZFS 表示欢迎，并赞赏其无月度订阅费模式是一个显著优势。然而，也有人对 Ubiquiti 过去的软件质量和安全记录提出了重大担忧，同时质疑传统硬盘驱动器是否能充分利用双 25 千兆链路的带宽。

**标签**: `#Enterprise Storage`, `#ZFS`, `#Ubiquiti`, `#NAS`, `#Networking`

---

<a id="item-4"></a>
## [Datasette Apps: Host custom HTML applications inside Datasette](https://simonwillison.net/2026/Jun/18/datasette-apps/#atom-everything) ⭐️ 8.0/10

A new Datasette plugin, datasette-apps, allows users to embed self-contained HTML+JavaScript applications within Datasette, enabling them to run read-only or configured write SQL queries against the hosted data.

rss · Simon Willison · Jun 18, 23:58

**标签**: `#Datasette`, `#Web Development`, `#Data Applications`, `#Plugins`, `#Data Tools`

---

<a id="item-5"></a>
## [CS 6120: Advanced Compilers: The Self-Guided Online Course (2020)](https://www.cs.cornell.edu/courses/cs6120/2025fa/self-guided/) ⭐️ 7.0/10

Cornell University's CS 6120 'Advanced Compilers' is a self-guided online course offering deep insights into compiler design, with community discussion providing expert critique and context.

hackernews · ibobev · Jun 18, 11:04

**标签**: `#Compilers`, `#Computer Science Education`, `#Online Learning`, `#Software Engineering`, `#Systems Programming`

---

<a id="item-6"></a>
## [datasette-acl 0.6a0](https://simonwillison.net/2026/Jun/18/datasette-acl/#atom-everything) ⭐️ 7.0/10

datasette-acl 0.6a0 版本发布，将插件的权限管理能力从仅限于表扩展到通用的资源共享系统。

rss · Simon Willison · Jun 18, 19:03

**标签**: `#datasette`, `#access control`, `#permissions`, `#plugin`, `#data management`

---

<a id="item-7"></a>
## [国家发改委：第三批 625 亿元国补 6 月底前下达](https://www.chinanews.com.cn/cj/2026/06-18/10642965.shtml) ⭐️ 7.0/10

国家发改委宣布，将在 6 月底前下达今年全部 2000 亿元设备更新项目清单和第三批 625 亿元消费品以旧换新资金。

telegram · zaihuapd · Jun 18, 08:39

**标签**: `#经济政策`, `#政府公告`, `#设备更新`, `#消费刺激`, `#中国经济`

---