---
layout: default
title: "Horizon Summary: 2026-04-28 (ZH)"
date: 2026-04-28
lang: zh
---

> From 26 items, 12 important content pieces were selected

---

1. [vLLM v0.20.0 发布，支持 DeepSeek V4 并升级核心依赖](#item-1) ⭐️ 9.0/10
2. [Microsoft and OpenAI end their exclusive and revenue-sharing deal](#item-2) ⭐️ 9.0/10
3. [ChatGPT 5.2 在东大及京大入学考试中超过人类最高分](#item-3) ⭐️ 9.0/10
4. [微软启动 Windows K2 计划重塑 Windows 11 体验](#item-4) ⭐️ 9.0/10
5. [📱 小米正式开源 MiMo-V2.5 系列模型](#item-5) ⭐️ 9.0/10
6. [Is my blue your blue?](#item-6) ⭐️ 8.0/10
7. [microsoft/VibeVoice](#item-7) ⭐️ 8.0/10
8. [Tracking the history of the now-deceased OpenAI Microsoft AGI clause](#item-8) ⭐️ 8.0/10
9. [上海 11 家数据跨境服务中心正式成立](#item-9) ⭐️ 8.0/10
10. [📱 中国审查 Meta 收购 Manus，两名联合创始人被限制离境  中国监管部门正在审查 Meta 收购 AI 初创公司 Manus 是否违反投资规定。](#item-10) ⭐️ 8.0/10
11. [GitHub Copilot 代码审查将于 2026 年 6 月 1 日起消耗 Actions 额度](#item-11) ⭐️ 8.0/10
12. [Speech translation in Google Meet is now rolling out to mobile devices](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vLLM v0.20.0 发布，支持 DeepSeek V4 并升级核心依赖](https://github.com/vllm-project/vllm/releases/tag/v0.20.0) ⭐️ 9.0/10

vLLM v0.20.0 版本已发布，主要更新包括初步支持 DeepSeek V4 模型，将默认 CUDA 版本升级到 13.0，并将 PyTorch 更新到 2.11，这包含环境依赖的破坏性变更。此版本还增加了对 Python 3.14 的支持，将 FlashAttention 4 设为默认的 MLA 预填充后端，并引入了 TurboQuant 2 位 KV 缓存压缩。 此次发布对 LLM 推理生态系统意义重大，因为它增强了 vLLM 的功能，使用户能够利用 DeepSeek V4 等新模型，并从性能改进以及与最新深度学习框架的更广泛兼容性中受益。核心依赖项的升级确保 vLLM 始终处于高效 LLM 服务的前沿，影响着部署大型语言模型的研究人员、开发人员和公司。 升级到 PyTorch 2.11 和 CUDA 13.0 是环境依赖方面的破坏性变更，要求用户调整其设置，并建议在 CUDA 12.9 上使用 `uv` 和 `--torch-backend=cu129` 进行安装。值得注意的新功能包括 TurboQuant 2 位 KV 缓存压缩，可实现 4 倍容量，以及在线量化前端、用于未来内核工作的 vLLM IR 初始框架，以及广泛的 MoE 重构。

github · khluu · Apr 27, 21:20

**背景**: vLLM 是一个开源库，旨在实现大型语言模型 (LLM) 的高吞吐量和低延迟推理。它通过采用 PagedAttention 技术来实现这一目标，该技术在 LLM 生成过程中高效管理 KV 缓存（键值缓存），类似于操作系统管理虚拟内存的方式。这使得 vLLM 能够在单个 GPU 上同时处理多个推理请求，与传统方法相比，显著提高了 GPU 利用率和整体吞吐量。

**标签**: `#LLM推理`, `#vLLM`, `#深度学习`, `#软件发布`, `#AI基础设施`

---

<a id="item-2"></a>
## [Microsoft and OpenAI end their exclusive and revenue-sharing deal](https://www.bloomberg.com/news/articles/2026-04-27/microsoft-to-stop-sharing-revenue-with-main-ai-partner-openai) ⭐️ 9.0/10

微软和 OpenAI 已终止其独家和收入分成协议，标志着双方合作关系的重大战略转变，可能重塑 AI 云和竞争格局。

hackernews · helsinkiandrew · Apr 27, 13:22

**标签**: `#AI行业`, `#云市场`, `#战略合作`, `#OpenAI`, `#Microsoft Azure`

---

<a id="item-3"></a>
## [ChatGPT 5.2 在东大及京大入学考试中超过人类最高分](https://english.kyodonews.net/articles/-/74976) ⭐️ 9.0/10

ChatGPT 5.2 Thinking 模型在东京大学和京都大学的入学考试中超越了人类最高分，包括在数学科目中获得满分，引发了对当前考试制度的重新思考。

telegram · zaihuapd · Apr 27, 09:15

**标签**: `#AI`, `#LLM`, `#教育科技`, `#AI能力`, `#基准测试`

---

<a id="item-4"></a>
## [微软启动 Windows K2 计划重塑 Windows 11 体验](https://www.windowscentral.com/microsoft/windows-11/what-is-windows-k2-everything-you-need-to-know-saving-windows-11) ⭐️ 9.0/10

微软已启动“Windows K2”计划，旨在通过优先质量、性能和可靠性来全面重塑 Windows 11 体验，包括使用 WinUI 3 重建开始菜单、提升游戏性能至 SteamOS 水平以及减少系统更新频率。

telegram · zaihuapd · Apr 27, 10:31

**标签**: `#Windows`, `#Operating System`, `#Microsoft`, `#System Performance`, `#UI/UX`

---

<a id="item-5"></a>
## [📱 小米正式开源 MiMo-V2.5 系列模型](https://x.com/XiaomiMiMo/status/2048821516079661561) ⭐️ 9.0/10

小米正式开源了 MiMo-V2.5 系列模型，包含在 Agent 和代码任务中表现领先的 MiMo-V2.5-Pro 以及原生全模态的 MiMo-V2.5，均支持 1M token 上下文窗口并采用 MIT 许可。

telegram · zaihuapd · Apr 28, 00:27

**标签**: `#AI模型`, `#开源AI`, `#大语言模型`, `#AI Agent`, `#多模态AI`

---

<a id="item-6"></a>
## [Is my blue your blue?](https://ismy.blue/) ⭐️ 8.0/10

一个交互式网站允许用户测试和量化他们个人在蓝色和绿色之间的界限，揭示了颜色感知的主观性，并引发了热烈的社区讨论。

hackernews · theogravity · Apr 27, 20:24

**标签**: `#颜色感知`, `#认知科学`, `#人机交互`, `#心理学`, `#语言学`

---

<a id="item-7"></a>
## [microsoft/VibeVoice](https://simonwillison.net/2026/Apr/27/vibevoice/#atom-everything) ⭐️ 8.0/10

Microsoft has released VibeVoice, an MIT-licensed, Whisper-style speech-to-text model with built-in speaker diarization, which Simon Willison demonstrates running efficiently on a Mac using MLX.

rss · Simon Willison · Apr 27, 23:46

**标签**: `#Speech-to-Text`, `#AI/ML`, `#Open Source`, `#Speaker Diarization`, `#MLX`

---

<a id="item-8"></a>
## [Tracking the history of the now-deceased OpenAI Microsoft AGI clause](https://simonwillison.net/2026/Apr/27/now-deceased-agi-clause/#atom-everything) ⭐️ 8.0/10

Simon Willison 追踪并分析了微软与 OpenAI 合作协议中一项关键条款的历史，该条款规定一旦 AGI 实现，微软对 OpenAI 技术的商业知识产权将失效，而该条款现已被移除。

rss · Simon Willison · Apr 27, 18:38

**标签**: `#OpenAI`, `#Microsoft`, `#AGI`, `#AI治理`, `#商业策略`

---

<a id="item-9"></a>
## [上海 11 家数据跨境服务中心正式成立](https://mp.weixin.qq.com/s/RLFxjipgfl6_950_XbH5kQ) ⭐️ 8.0/10

上海正式成立 11 家数据跨境服务中心，并发布了旨在促进和规范数据出境的试行管理办法，以支持高水平对外开放并管理关键数据转移。

telegram · zaihuapd · Apr 27, 07:10

**标签**: `#数据治理`, `#数据跨境`, `#政策法规`, `#中国科技`, `#AI/ML影响`

---

<a id="item-10"></a>
## [📱 中国审查 Meta 收购 Manus，两名联合创始人被限制离境  中国监管部门正在审查 Meta 收购 AI 初创公司 Manus 是否违反投资规定。](https://t.me/zaihuapd/41088) ⭐️ 8.0/10

中国监管机构正在审查 Meta 对 AI 初创公司 Manus 的收购是否违反投资规定，并已限制 Manus 的两名联合创始人离境。

telegram · zaihuapd · Apr 27, 08:10

**标签**: `#AI`, `#M&A`, `#Regulation`, `#China`, `#Geopolitics`

---

<a id="item-11"></a>
## [GitHub Copilot 代码审查将于 2026 年 6 月 1 日起消耗 Actions 额度](https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026/) ⭐️ 8.0/10

自 2026 年 6 月 1 日起，GitHub Copilot 代码审查将更改计费模式，对于私有仓库将开始消耗 GitHub Actions 额度，影响 Pro、Pro+、Business 及 Enterprise 套餐用户。

telegram · zaihuapd · Apr 27, 16:34

**标签**: `#GitHub Copilot`, `#计费`, `#GitHub Actions`, `#AI工具`, `#成本管理`

---

<a id="item-12"></a>
## [Speech translation in Google Meet is now rolling out to mobile devices](https://simonwillison.net/2026/Apr/27/speech-translation-in-google-meet-is-now-rolling-out-to-mobile-d/#atom-everything) ⭐️ 7.0/10

Google Meet 正在向移动设备推出实时语音翻译的“alpha”版本，使用户能够以短暂延迟和语音模仿在支持的语言之间进行交流，尽管目前语言支持有限且存在一些兼容性问题。

rss · Simon Willison · Apr 27, 17:37

**标签**: `#AI/ML`, `#语音翻译`, `#Google Meet`, `#移动应用`, `#实时通信`

---