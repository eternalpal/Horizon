---
layout: default
title: "Horizon Summary: 2026-11-08 (ZH)"
date: 2026-11-08
lang: zh
---

> From 27 items, 17 important content pieces were selected

---

1. [MaxxBench – "Nice DeepSWE score. But is it true?"](#item-1) ⭐️ 9.0/10
2. [苹果披露人形机器人系统 HALO，用两个千问模型](#item-2) ⭐️ 9.0/10
3. [GitHub 新架构支持每秒 7200 次推送](#item-3) ⭐️ 9.0/10
4. [What I run on my $10 USD OpenStick homelab](#item-4) ⭐️ 8.0/10
5. [Claude Code's "Don't Ask Again" exposes passwords in 1,122 public GitHub files](#item-5) ⭐️ 8.0/10
6. [Need for Speed Underground 2 online in the browser](#item-6) ⭐️ 8.0/10
7. [Show HN: Coldframe, a honeypot that poses as a supermarket fridge controller](#item-7) ⭐️ 8.0/10
8. [Quoting Nilay Patel](#item-8) ⭐️ 8.0/10
9. [曝深圳手机厂盯上二手存储，新机流畅寿命直接腰斩至一年  受存储芯片涨价冲击，手机行业正出现“品质倒挂”危险信号——多家手机厂商正评估采用二手存储方案。](#item-9) ⭐️ 8.0/10
10. [🤖 Claude Code 被指搜索网页时可能泄露邮箱](#item-10) ⭐️ 8.0/10
11. [AI 假证平台 OnlyFake 创始人认罪后被驱逐](#item-11) ⭐️ 8.0/10
12. [美司法部「超级智能特别工作组」正式运作  美国司法部宣布「超级智能特别工作组」（SINTF）已开始运作。](#item-12) ⭐️ 8.0/10
13. [中国开源 AI 模型占全球近 30% 使用量  根据最新报告，中国开发的开源人工智能（AI）模型在全球范围内的使用量占比近 30%。](#item-13) ⭐️ 8.0/10
14. [马斯克：Optimus 机器人可能只租不卖](#item-14) ⭐️ 7.0/10
15. [🤖 Cat Wu 加入 OpenAI 负责核心产品管理  Cat Wu 宣布加入 OpenAI，负责核心产品的产品管理工作。](#item-15) ⭐️ 7.0/10
16. [🤖 消费者起诉 Anthropic，称其高端 AI 计划使用限额不实  华盛顿特区消费者 Karl Kahn 对 Anthropic 提起集体诉讼，指控其“Ma](#item-16) ⭐️ 7.0/10
17. [索尼进博会首发无线感知跌倒检测系统](#item-17) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [MaxxBench – "Nice DeepSWE score. But is it true?"](https://maxxbench.unlap.ai/research/why-maxxbench/) ⭐️ 9.0/10

MaxxBench 研究批判性地审视了 DeepSWE 等 LLM 基准测试的可靠性，展示了任务参数变化如何揭示报告分数中的缺陷，并提出了一种测试基准泛化能力的方法。

hackernews · antiuniverse · Nov 7, 17:19

**标签**: `#LLM评估`, `#基准测试`, `#AI/ML研究`, `#模型可靠性`, `#DeepSWE`

---

<a id="item-2"></a>
## [苹果披露人形机器人系统 HALO，用两个千问模型](https://weibo.com/1642634100/RqjjGllvw) ⭐️ 9.0/10

苹果研究团队发布了 HALO 人形机器人自主控制系统，该系统利用多层千问模型进行任务编 ibilities 和动作生成，并成功将仿真学习的动作迁移到真实世界，且已开源相关代码。

telegram · zaihuapd · Nov 7, 13:35

**标签**: `#Robotics`, `#AI/ML`, `#Large Language Models`, `#Humanoid Robots`, `#Open Source`

---

<a id="item-3"></a>
## [GitHub 新架构支持每秒 7200 次推送](https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/) ⭐️ 9.0/10

GitHub 推出了代号为 Rubicon 的新 Git 存储架构，旨在支持大量 AI 智能体并发操作单个仓库，在内部测试中实现了每秒 7200 次推送。该架构支持 5000 个智能体同时协作，并保持较低的读取延迟。 这一发展对大规模软件工程和 AI 驱动的开发至关重要，因为它显著提升了 GitHub 处理现代 AI 智能体高并发需求的能力。它使得 AI 驱动的开发团队和项目能够实现更高效、更协作的工作流程。 Rubicon 架构将 Git 对象存储在 Azure Blob Storage 中，通过 Ref-CAS 管理引用状态，并利用虚拟副本处理读写操作，同时后台节点负责压缩数据包。该系统目前处于有限的私有预览阶段，并将逐步扩大推广范围。

telegram · zaihuapd · Nov 7, 14:12

**标签**: `#Git`, `#分布式系统`, `#云架构`, `#AI/ML`, `#可扩展性`

---

<a id="item-4"></a>
## [What I run on my $10 USD OpenStick homelab](https://blog.bosscher.ch/posts/openstick/) ⭐️ 8.0/10

这篇文章详细介绍了如何使用一个价值 10 美元的 OpenStick 搭建一个功能齐全的家庭实验室，展示了适用于资源受限设备的各种自托管软件应用。

hackernews · LaurensBER · Nov 7, 18:12

**标签**: `#自托管`, `#家庭实验室`, `#ARM`, `#低成本计算`, `#系统管理`

---

<a id="item-5"></a>
## [Claude Code's "Don't Ask Again" exposes passwords in 1,122 public GitHub files](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again) ⭐️ 8.0/10

一项安全分析发现，当配置不当的 Claude Code 本地设置被提交到公共 GitHub 仓库时，无意中在 1,122 个文件中暴露了密码和秘密，引发了关于 AI 代理安全和开发者最佳实践的讨论。

hackernews · shmulc · Nov 7, 20:45

**标签**: `#AI安全`, `#软件工程`, `#GitHub`, `#秘密管理`, `#开发者工具`

---

<a id="item-6"></a>
## [Need for Speed Underground 2 online in the browser](https://nfsu2.xyz/) ⭐️ 8.0/10

一款经典赛车游戏《极品飞车：地下狂飙 2》已被逆向工程并在网页浏览器中实现多人在线游玩，引发了关于游戏保存和网络技术能力的讨论。

hackernews · fluxusars · Nov 7, 09:36

**标签**: `#Web Technologies`, `#Game Preservation`, `#Reverse Engineering`, `#Online Gaming`, `#Abandonware`

---

<a id="item-7"></a>
## [Show HN: Coldframe, a honeypot that poses as a supermarket fridge controller](https://github.com/hedgerow-dev/coldframe) ⭐️ 8.0/10

Coldframe 是一个基于 Python 的蜜罐，旨在精确模拟超市制冷控制器，以观察针对易受攻击的工业控制系统的攻击尝试，其灵感来源于最近的真实事件。

hackernews · hedgerow-dev · Nov 7, 17:27

**标签**: `#Honeypot`, `#ICS/OT Security`, `#Cybersecurity`, `#Python`, `#Industrial Control Systems`

---

<a id="item-8"></a>
## [Quoting Nilay Patel](https://simonwillison.net/2026/Nov/6/nilay-patel/) ⭐️ 8.0/10

Nilay Patel 严厉批评当前 AI 产品未能证明其高昂成本的合理性，指出其提供的实际价值不足且常产出低质量内容，并质疑 AI 行业面临的经济和伦理挑战。

rss · Simon Willison · Nov 6, 17:13

**标签**: `#AI批判`, `#AI伦理`, `#行业分析`, `#技术炒作`, `#产品价值`

---

<a id="item-9"></a>
## [曝深圳手机厂盯上二手存储，新机流畅寿命直接腰斩至一年  受存储芯片涨价冲击，手机行业正出现“品质倒挂”危险信号——多家手机厂商正评估采用二手存储方案。](https://t.me/zaihuapd/44979) ⭐️ 8.0/10

有报道称，受存储芯片涨价影响，部分深圳手机厂商正评估或已开始在新机中使用二手存储，可能导致新机流畅寿命从 2-3 年骤降至 1 年。

telegram · zaihuapd · Nov 7, 04:32

**标签**: `#移动行业`, `#供应链`, `#硬件质量`, `#消费者权益`, `#制造实践`

---

<a id="item-10"></a>
## [🤖 Claude Code 被指搜索网页时可能泄露邮箱](https://github.com/anthropics/claude-code/issues/107757) ⭐️ 8.0/10

Anthropic's Claude Code was found to be leaking user login emails during web searches by embedding them in network requests, leading to spam and raising significant privacy concerns, though the company is working on a permanent fix.

telegram · zaihuapd · Nov 7, 08:09

**标签**: `#AI Security`, `#Privacy`, `#Large Language Models`, `#Software Vulnerability`, `#Anthropic`

---

<a id="item-11"></a>
## [AI 假证平台 OnlyFake 创始人认罪后被驱逐](https://www.404media.co/an-ai-fraud-kingpins-confessions/) ⭐️ 8.0/10

OnlyFake 平台的创始人从手工伪造证件发展到整合生成式 AI，以低至 15 美元的价格生成假证件，最终在美国认罪并被驱逐出境，终身禁止再次入境。

telegram · zaihuapd · Nov 7, 10:54

**标签**: `#AI滥用`, `#网络犯罪`, `#生成式AI`, `#身份欺诈`, `#法律与监管`

---

<a id="item-12"></a>
## [美司法部「超级智能特别工作组」正式运作  美国司法部宣布「超级智能特别工作组」（SINTF）已开始运作。](https://t.me/zaihuapd/44993) ⭐️ 8.0/10

美国司法部已正式启动「超级智能特别工作组」（SINTF），旨在维护美国 AI 领先地位、反制外国 AI 滥用，并统筹涉 AI 刑事与民事案件，同时参与阻止「繁重监管」的立法建议。

telegram · zaihuapd · Nov 8, 01:30

**标签**: `#AI治理`, `#AI政策`, `#超级智能`, `#国家安全`, `#监管`

---

<a id="item-13"></a>
## [中国开源 AI 模型占全球近 30% 使用量  根据最新报告，中国开发的开源人工智能（AI）模型在全球范围内的使用量占比近 30%。](https://t.me/zaihuapd/44995) ⭐️ 8.0/10

一份最新报告显示，由 Qwen、DeepSeek、Kimi 等中国模型领跑的中国开源 AI 模型，在全球使用量占比已迅速增长至近 30%，并在 2025 年下半年呈现显著增长。

telegram · zaihuapd · Nov 8, 03:26

**标签**: `#AI趋势`, `#开源AI`, `#中国AI`, `#市场份额`, `#大语言模型`

---

<a id="item-14"></a>
## [马斯克：Optimus 机器人可能只租不卖](https://www.ithome.com/1/023/675.htm) ⭐️ 7.0/10

埃隆·马斯克宣布特斯拉的 Optimus 机器人可能只租不卖，初期成本约 3 万美元，声称效率是普通人的 5 倍，并计划在 2027 年底左右对外交付。

telegram · zaihuapd · Nov 7, 06:33

**标签**: `#机器人`, `#商业策略`, `#特斯拉`, `#人形机器人`, `#自动化`

---

<a id="item-15"></a>
## [🤖 Cat Wu 加入 OpenAI 负责核心产品管理  Cat Wu 宣布加入 OpenAI，负责核心产品的产品管理工作。](https://t.me/zaihuapd/44986) ⭐️ 7.0/10

Cat Wu 已加入 OpenAI 负责核心产品管理，将专注于开发帮助用户保持掌控并提高效率的 AI 智能体。

telegram · zaihuapd · Nov 7, 10:03

**标签**: `#AI行业`, `#OpenAI`, `#产品管理`, `#AI智能体`, `#人事变动`

---

<a id="item-16"></a>
## [🤖 消费者起诉 Anthropic，称其高端 AI 计划使用限额不实  华盛顿特区消费者 Karl Kahn 对 Anthropic 提起集体诉讼，指控其“Ma](https://t.me/zaihuapd/44989) ⭐️ 7.0/10

一名消费者对 Anthropic 提起集体诉讼，指控其高端 AI 订阅计划的实际使用限额远低于宣传，引发了对 AI 订阅市场透明度和消费者保护的关注。

telegram · zaihuapd · Nov 7, 12:44

**标签**: `#AI伦理`, `#消费者权益`, `#AI商业`, `#法律诉讼`, `#Anthropic`

---

<a id="item-17"></a>
## [索尼进博会首发无线感知跌倒检测系统](https://weibo.com/1642634100/RqojudB4Q) ⭐️ 7.0/10

索尼在进博会首发了一款由中国研究院本土开发的无线感知跌倒检测系统，该系统利用 Wi-Fi 信号和深度学习技术，无需穿戴设备或影像采集，即可实现隐私友好的居家养老跌倒监测。

telegram · zaihuapd · Nov 8, 02:21

**标签**: `#老年护理`, `#无线感知`, `#深度学习`, `#隐私保护`, `#物联网`

---