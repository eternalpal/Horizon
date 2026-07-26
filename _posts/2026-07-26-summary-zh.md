---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
---

> From 23 items, 9 important content pieces were selected

---

1. [SGLang v0.5.16 发布，引入 DSpark 和 Inkling 支持](#item-1) ⭐️ 9.0/10
2. [Anthropic 发布 Claude Opus 5：一款深思熟虑且积极主动的 AI 模型](#item-2) ⭐️ 9.0/10
3. [近 200 家硅谷公司反对禁中国开放权重 AI  近 200 家硅谷公司，包括 Proton 和 Y Combinator，致信特朗普政府，反对切断美国对中国开](#item-3) ⭐️ 9.0/10
4. [Ruff v0.16.0](#item-4) ⭐️ 8.0/10
5. [Quoting Boris Cherny](#item-5) ⭐️ 8.0/10
6. [开发者发布 iOS 27 usbliter8 越狱方案，目前仅支持 iPhone 11 Pro](#item-6) ⭐️ 8.0/10
7. [✈️ Telegram 现支付漏洞：日本账户超低价购星币，目前已修复  7 月 23 日，Telegram 一个已修复的漏洞影响日本账户，可超低价购入星币(St](#item-7) ⭐️ 7.0/10
8. [就业确定性主导高考志愿 军警师范升温与临床医学降温](#item-8) ⭐️ 7.0/10
9. [🤖 Grok 4.5 向免费用户开放试用  Grok 4.5 现已向免费用户开放试用。](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.16 发布，引入 DSpark 和 Inkling 支持](https://github.com/sgl-project/sglang/releases/tag/v0.5.16) ⭐️ 9.0/10

SGLang v0.5.16 已发布，引入了 DSpark，这是一种新型的置信度驱动推测解码算法，旨在加速大型语言模型（LLM）推理。此版本还增加了对 Inkling 的支持，这是一种拥有 9750 亿参数的多模态 MoE 模型，并在 Blackwell 硬件上展示了高性能。 这些进展对于提高大型语言模型（LLM）推理的效率和速度至关重要，直接影响 AI 应用的成本和响应能力。对 Inkling 等先进模型在 Blackwell 等尖端硬件上的支持，展示了 SGLang 在推动 AI 性能和多模态能力方面的作用。 DSpark 利用置信度驱动的验证机制，以块为单位进行半自回归草稿生成，并根据草稿自身的置信度动态调整验证窗口大小，在 DeepSeek-V4-Pro 上实现了 383.7 tok/s 的速度。Inkling 是一个 9750 亿参数的多模态 MoE 模型，结合了滑动窗口、全注意力及 Mamba2 线性注意力，并支持 NVFP4 MoE，在 Blackwell 上实现了高达 71.7k tok/s 的输入吞吐量。

github · Qiaolin-Yu · Jul 25, 00:13

**背景**: 推测解码是一种大型语言模型（LLM）推理优化技术，通过使用一个更小、更快的“草稿”模型来预测多个后续词元，然后由更大、更准确的“目标”模型进行验证，从而加速词元生成。这种方法显著降低了延迟，同时确保输出质量与标准自回归解码相同。多模态专家混合（MoE）模型是一种先进的 AI 架构，能够处理和生成跨不同模态（如文本、图像和音频）的内容，通过选择性地激活针对输入不同部分优化的“专家”子网络，从而实现参数量巨大但推理高效的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/">An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog</a></li>
<li><a href="https://venturebeat.com/orchestration/deepseek-open-sources-dspark-a-new-framework-to-speed-up-llm-inference-by-up-to-85">DeepSeek open sources DSpark, a new framework to speed up LLM inference by up to 85% | VentureBeat</a></li>
<li><a href="https://www.marktechpost.com/2026/07/15/thinking-machines-lab-releases-inkling-a-975b-parameter-open-weights-multimodal-moe-with-41b-active-parameters-and-controllable-thinking-effort/">Thinking Machines Lab Releases Inkling: A 975B-Parameter Open-Weights Multimodal MoE With 41B Active Parameters And Controllable Thinking Effort - MarkTechPost</a></li>

</ul>
</details>

**标签**: `#LLM推理`, `#推测解码`, `#多模态AI`, `#模型服务`, `#性能优化`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Opus 5：一款深思熟虑且积极主动的 AI 模型](https://simonwillison.net/2026/Jul/24/introducing-claude-opus-5/#atom-everything) ⭐️ 9.0/10

Anthropic 发布了 Claude Opus 5，这是一款被描述为“思虑周全且积极主动”的新型大型语言模型，它以 Claude Fable 5 一半的价格提供了接近前沿的智能。这款新模型已在 Artificial Analysis 排行榜上名列前茅，甚至超越了 Fable 5，并且定价与前代 Opus 4.8 相同。 此次发布标志着 AI 领域的一项重大进展，它使尖端智能更具可访问性和成本效益，有望加速各行业的创新和采用。该模型在一个知名排行榜上的卓越表现，使其在快速发展的大型语言模型领域中成为一个强劲的竞争者，将影响寻求强大 AI 解决方案的开发者和企业。 Claude Opus 5 展示了卓越的积极主动性，它能够独立开发计算机视觉管道，从无法直接查看的图纸中重建 3D 模型，这体现了其先进的问题解决能力。尽管该模型在发现网络安全漏洞方面有了显著提升，接近 Mythos 5 的水平，但它被有意设计为不利用这些漏洞，从而优先考虑安全性。

rss · Simon Willison · Jul 24, 23:48

**背景**: 大型语言模型（LLM）是先进的人工智能程序，例如 ChatGPT，旨在基于海量数据理解、生成和处理类人文本。它们代表了语言建模的最新演变，主要利用 Transformer 架构来实现复杂的语言能力。Artificial Analysis 排行榜是一个重要的平台，它通过一系列基准测试评估和排名各种 AI 模型和 API 的性能，提供一个“智能指数”来比较它们的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://juejin.cn/post/7481220690671632447">LLM、Prompt、AI Agent、RAG.</a></li>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index | Artificial Analysis</a></li>

</ul>
</details>

**标签**: `#AI`, `#大型语言模型`, `#Anthropic`, `#机器学习`, `#生成式AI`

---

<a id="item-3"></a>
## [近 200 家硅谷公司反对禁中国开放权重 AI  近 200 家硅谷公司，包括 Proton 和 Y Combinator，致信特朗普政府，反对切断美国对中国开](https://t.me/zaihuapd/42772) ⭐️ 9.0/10

近 200 家硅谷公司，包括 Proton 和 Y Combinator，致信特朗普政府，反对切断美国对中国开放权重 AI 模型的获取，认为全面禁令将重创美国初创企业，并主张采取更有针对性的安全措施。

telegram · zaihuapd · Jul 26, 02:00

**标签**: `#AI政策`, `#中美科技竞争`, `#AI初创企业`, `#开放权重AI`, `#科技监管`

---

<a id="item-4"></a>
## [Ruff v0.16.0](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 8.0/10

Ruff v0.16.0 significantly increases the number of default enabled linting rules to 413, potentially causing CI failures for Python projects with unpinned dependencies.

rss · Simon Willison · Jul 25, 22:44

**标签**: `#Python`, `#Linting`, `#Developer Tools`, `#Software Engineering`, `#CI/CD`

---

<a id="item-5"></a>
## [Quoting Boris Cherny](https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything) ⭐️ 8.0/10

Anthropic 的 Boris Cherny 宣布，Claude Opus 5 是他们迄今为止最难被提示注入的模型，标志着 AI 安全性方面的一个重要进步。

rss · Simon Willison · Jul 25, 00:42

**标签**: `#AI安全`, `#提示注入`, `#大型语言模型`, `#Anthropic`, `#生成式AI`

---

<a id="item-6"></a>
## [开发者发布 iOS 27 usbliter8 越狱方案，目前仅支持 iPhone 11 Pro](https://github.com/34306/usbliter8-fun) ⭐️ 8.0/10

开发者发布了一个利用 usbliter8 漏洞的 iOS 27 越狱方案，目前仅支持 iPhone 11 Pro，但会抹除数据并破坏多项设备功能，主要面向安全研究和备用机。

telegram · zaihuapd · Jul 25, 11:00

**标签**: `#iOS`, `#Jailbreak`, `#Security Research`, `#Exploit`, `#Reverse Engineering`

---

<a id="item-7"></a>
## [✈️ Telegram 现支付漏洞：日本账户超低价购星币，目前已修复  7 月 23 日，Telegram 一个已修复的漏洞影响日本账户，可超低价购入星币(St](https://t.me/zaihuapd/42752) ⭐️ 7.0/10

Telegram 修复了一个支付漏洞，该漏洞允许日本账户以超低价购买星币，但相关星币已被冻结，Telegram 将回滚购买并可能冻结涉事账户。

telegram · zaihuapd · Jul 24, 16:27

**标签**: `#支付漏洞`, `#Telegram`, `#安全`, `#数字货币`, `#平台经济`

---

<a id="item-8"></a>
## [就业确定性主导高考志愿 军警师范升温与临床医学降温](https://www.caixin.com/2026-07-17/102464976.html) ⭐️ 7.0/10

In 2026, Chinese college applicants are increasingly prioritizing job security, leading to a surge in popularity for military, police, and public-funded teaching programs, while traditional high-status fields like five-year clinical medicine programs see a decline.

telegram · zaihuapd · Jul 25, 04:49

**标签**: `#Education`, `#China`, `#Career Trends`, `#Societal Impact`, `#Gaokao`

---

<a id="item-9"></a>
## [🤖 Grok 4.5 向免费用户开放试用  Grok 4.5 现已向免费用户开放试用。](https://t.me/zaihuapd/42763) ⭐️ 7.0/10

Grok 4.5 现已向所有 X 或 SuperGrok 账户的免费用户开放试用，用户可通过 Grok Build 体验并提供反馈。

telegram · zaihuapd · Jul 25, 05:34

**标签**: `#AI`, `#Grok`, `#xAI`, `#LLM`, `#产品发布`

---