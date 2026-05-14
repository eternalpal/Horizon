---
layout: default
title: "Horizon Summary: 2026-05-14 (ZH)"
date: 2026-05-14
lang: zh
---

> From 31 items, 12 important content pieces were selected

---

1. [前员工被解雇后删除 96 个政府数据库](#item-1) ⭐️ 9.0/10
2. [三星电子工会抗议致芯片产出骤降，代工与存储线受严重波及  ​三星电子最大工会称，因大批员工离岗参与加薪抗议集会，公司在韩国本土的芯片产量在周四夜班时段出现大幅下](#item-2) ⭐️ 9.0/10
3. [小米发布 Xiaomi OneVL 一步式潜空间推理框架并全面开源](#item-3) ⭐️ 9.0/10
4. [The Emacsification of Software](#item-4) ⭐️ 8.0/10
5. [📱 Meta 美国员工反对公司用工作电脑行为数据训练 AI](#item-5) ⭐️ 8.0/10
6. [♻️ 英伟达确认黄仁勋将参加特朗普访华行程](#item-6) ⭐️ 8.0/10
7. [Altman 证称马斯克曾考虑将 OpenAI 传给子女](#item-7) ⭐️ 8.0/10
8. [OpenAI 官方状态页面显示 Codex 5.5 引擎出现高错误率，gpt-5.5 当前错误率持续升高。](#item-8) ⭐️ 8.0/10
9. [Setting up a free *.city.state.us locality domain (2025)](#item-9) ⭐️ 7.0/10
10. [Welcome to the Datasette blog](#item-10) ⭐️ 7.0/10
11. [Quoting Boris Mann](#item-11) ⭐️ 7.0/10
12. [马化腾在股东大会回应腾讯 AI 进展](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [前员工被解雇后删除 96 个政府数据库](https://arstechnica.com/tech-policy/2026/05/drop-database-what-not-to-do-after-losing-an-it-job/) ⭐️ 9.0/10

两名前雇员（一对双胞胎兄弟）在 2025 年 3 月 12 日被解雇后几分钟内，恶意删除了 96 个政府数据库，其中包括一个国土安全部（DHS）的数据库，暴露了严重的安全漏洞。其中一名兄弟使用了“DROP DATABASE dhsproddb”命令，随后向 AI 工具询问如何清除系统日志。 此次事件严重凸显了内部威胁带来的巨大风险，并强调了组织（尤其是政府机构）在员工离职时实施强大的特权访问管理和即时用户权限撤销协议的紧迫性。此类故障可能导致严重的数据丢失、运营中断和国家安全风险。 其中一名兄弟执行了特定的 SQL 命令“DROP DATABASE dhsproddb”来删除国土安全部数据库，随后还使用 AI 工具询问如何清除 SQL 服务器的系统日志。调查还发现，其中一名兄弟尽管有犯罪记录，却持有枪支，这引发了对敏感职位背景调查彻底性的担忧。

hackernews · jnord · May 12, 22:28

**背景**: 特权访问管理（PAM）是一种网络安全方法，用于控制、监控和保护对组织最敏感数据和关键系统的访问，通常通过将凭据存储在安全保管库中并记录所有访问。而用户权限撤销则是当员工离职或在公司内部改变角色时，撤销其所有系统和应用程序访问权限的关键过程。这两种做法对于预防内部威胁至关重要，内部威胁是指拥有授权访问权限的个人利用其特权造成损害。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://emudhra.com/en/blog/privileged-access-management-pam-preventing-insider-threats-in-a-hybrid-workforce">Privileged Access Management : Prevent Insider Threats</a></li>
<li><a href="https://medium.com/identity-beyond-borders/pim-pam-something-different-from-iam-66f39d74a8c9">PIM? PAM ?….. Something different from IAM? | Medium</a></li>
<li><a href="https://www.securends.com/blog/what-is-user-deprovisioning/">What Is User Deprovisioning? Meaning, Process & Best Practices</a></li>

</ul>
</details>

**社区讨论**: 社区讨论主要表达了对这对双胞胎兄弟最初如何被聘用担任敏感政府 IT 职位的难以置信和嘲讽，质疑背景调查和安全许可的充分性。评论者还讨论了对雇主离职政策的更广泛影响，建议公司可能会采取更即时的访问权限终止措施，并对公司随后解雇了负责招聘这对双胞胎的人员感到好笑。

**标签**: `#Cybersecurity`, `#Insider Threat`, `#Data Breach`, `#Government IT`, `#Access Control`

---

<a id="item-2"></a>
## [三星电子工会抗议致芯片产出骤降，代工与存储线受严重波及  ​三星电子最大工会称，因大批员工离岗参与加薪抗议集会，公司在韩国本土的芯片产量在周四夜班时段出现大幅下](https://t.me/zaihuapd/41355) ⭐️ 9.0/10

三星电子最大工会因薪资纠纷发起抗议，导致芯片产出大幅下降，并威胁将进行全面罢工，可能严重扰乱全球半导体供应链。

telegram · zaihuapd · May 13, 01:11

**标签**: `#半导体制造`, `#供应链中断`, `#劳资关系`, `#全球科技影响`

---

<a id="item-3"></a>
## [小米发布 Xiaomi OneVL 一步式潜空间推理框架并全面开源](https://mp.weixin.qq.com/s/7po3r6YtmuXm8Xny1bw61Q) ⭐️ 9.0/10

小米发布并开源了 OneVL 一步式潜空间语言视觉推理框架，首次在自动驾驶领域统一了 VLA 和世界模型，通过隐式推理超越了显式 CoT，实现了 SOTA 性能和极低延迟。

telegram · zaihuapd · May 13, 10:33

**标签**: `#自动驾驶`, `#多模态AI`, `#潜空间推理`, `#开源`, `#AI研究`

---

<a id="item-4"></a>
## [The Emacsification of Software](https://sockpuppet.org/blog/2026/05/12/emacsification/) ⭐️ 8.0/10

The article proposes that the increasing ease of building personal software, particularly with the aid of LLMs, is leading to an 'Emacsification' where individuals create highly customized applications rather than relying on pre-packaged solutions.

hackernews · rdslw · May 13, 07:06

**标签**: `#Software Trends`, `#Personal Software`, `#LLMs`, `#Customization`, `#Software Philosophy`

---

<a id="item-5"></a>
## [📱 Meta 美国员工反对公司用工作电脑行为数据训练 AI](https://cybernews.com/ai-news/meta-employees-revolt-ai-mouse-keystroke-tracking/) ⭐️ 8.0/10

Meta US employees are reportedly protesting the company's requirement to install software on work computers that tracks their behavior and screen activity to train AI models, citing privacy concerns and potential labor law violations.

telegram · zaihuapd · May 13, 01:56

**标签**: `#AI Ethics`, `#Employee Privacy`, `#Labor Rights`, `#Corporate Policy`, `#Data Collection`

---

<a id="item-6"></a>
## [♻️ 英伟达确认黄仁勋将参加特朗普访华行程](https://www.cnbc.com/2026/05/13/nvidia-says-ceo-jensen-huang-is-joining-trumps-china-trip.html) ⭐️ 8.0/10

英伟达 CEO 黄仁勋将随美国总统特朗普访问中国，此举在中美科技关系和 AI 芯片销售限制的背景下，对未来 AI 芯片市场具有重要影响。

telegram · zaihuapd · May 13, 02:41

**标签**: `#地缘政治`, `#AI硬件`, `#贸易政策`, `#英伟达`, `#中美关系`

---

<a id="item-7"></a>
## [Altman 证称马斯克曾考虑将 OpenAI 传给子女](https://techcrunch.com/2026/05/12/musk-mulled-handing-openai-to-his-children-altman-testifies/) ⭐️ 8.0/10

OpenAI 首席执行官 Sam Altman 在马斯克提起的诉讼中作证，称马斯克曾考虑将 OpenAI 传给子女，并批评其管理方式，揭示了早期关于先进 AI 控制权和治理的冲突。

telegram · zaihuapd · May 13, 08:39

**标签**: `#AI治理`, `#OpenAI历史`, `#Elon Musk`, `#Sam Altman`, `#法律纠纷`

---

<a id="item-8"></a>
## [OpenAI 官方状态页面显示 Codex 5.5 引擎出现高错误率，gpt-5.5 当前错误率持续升高。](http://status.openai.com/) ⭐️ 8.0/10

OpenAI's official status page indicates high and rising error rates for its Codex 5.5 engine and GPT-5.5 models, signaling potential service disruptions.

telegram · zaihuapd · May 13, 08:56

**标签**: `#OpenAI`, `#API Status`, `#AI Models`, `#Service Performance`, `#GPT`

---

<a id="item-9"></a>
## [Setting up a free *.city.state.us locality domain (2025)](https://fredchan.org/blog/locality-domains-guide/) ⭐️ 7.0/10

这份指南详细介绍了设置免费 *.city.state.us 区域域名的过程，这是互联网基础设施中一个利基且通常行政复杂的方面。

hackernews · speckx · May 13, 14:45

**标签**: `#域名管理`, `#互联网基础设施`, `#网络`, `#政府服务`, `#系统管理`

---

<a id="item-10"></a>
## [Welcome to the Datasette blog](https://simonwillison.net/2026/May/13/welcome-to-the-datasette-blog/#atom-everything) ⭐️ 7.0/10

Simon Willison announces the launch of the official Datasette blog, built using OpenAI Codex desktop, which will host upcoming project announcements.

rss · Simon Willison · May 13, 23:59

**标签**: `#Datasette`, `#AI-assisted programming`, `#Generative AI`, `#LLMs`, `#Project announcement`

---

<a id="item-11"></a>
## [Quoting Boris Mann](https://simonwillison.net/2026/May/13/boris-mann/#atom-everything) ⭐️ 7.0/10

Boris Mann（由 Simon Willison 引用）认为“11 个 AI 代理”这样的说法毫无意义，并将其比作计算电子表格或浏览器标签，强调了 AI 代理定义需要更清晰。

rss · Simon Willison · May 13, 16:15

**标签**: `#AI Agents`, `#AI Terminology`, `#Conceptual Clarity`, `#AI Hype`

---

<a id="item-12"></a>
## [马化腾在股东大会回应腾讯 AI 进展](https://mp.weixin.qq.com/s/I9s-JnFS7hCyCB99B28O0w) ⭐️ 7.0/10

腾讯 CEO 马化腾在股东大会上承认公司 AI 曾一度落后，但目前已站稳脚跟并正加速发展，强调将结合自身优势稳步推进 AI 战略。

telegram · zaihuapd · May 13, 13:09

**标签**: `#腾讯`, `#AI战略`, `#企业领导力`, `#人工智能`, `#科技行业`

---