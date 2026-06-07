---
layout: default
title: "Horizon Summary: 2026-06-07 (ZH)"
date: 2026-06-07
lang: zh
---

> From 26 items, 1 important content pieces were selected

---

1. [Xposed QQ 模块 QStory 被曝内置云控后门](#item-1) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [Xposed QQ 模块 QStory 被曝内置云控后门](https://t.me/zaihuapd/41807) ⭐️ 9.0/10

流行的 Android QQ Xposed 模块“QStory”的 `QStory_2.6.2-release.apk` 版本被发现内置了严重的云控后门。该后门可在用户不知情的情况下，远程执行清空好友、解散群聊以及删除本地数据等恶意操作。 这一发现对安装了该模块的 QQ 用户的个人数据完整性和隐私构成了重大威胁，凸显了第三方修改工具和流行模块中潜在恶意代码的风险。它强调了对与核心应用程序深度交互的模块进行安全审查的极端重要性。 QStory_2.6.2-release.apk 中的后门能够执行破坏性操作，例如批量删除所有好友、强制退出或解散所有群组、删除相册和下载内容，以及清除所有本地 QQ 数据。这些操作无需用户交互即可远程执行，并且明显不属于模块所声明的正常功能范畴。

telegram · zaihuapd · Jun 6, 12:06

**背景**: Xposed 框架是一个 Android 工具，允许用户在不修改应用程序原始 APK 的情况下，通过 Hook Android 运行时来改变系统和应用程序的行为。云控后门是指一种恶意机制，攻击者可以通过基于云的服务器远程控制被入侵的设备或应用程序，从而实现集中式命令和控制以执行未经授权的破坏性操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnblogs.com/baiqiantao/p/10699552.html">Xposed 框 架 hook 简介 原理 案例 - 白乾涛 - 博客园</a></li>
<li><a href="https://cloud.baidu.com/article/2762440">云控系统：从原理到实践的探索</a></li>
<li><a href="https://blog.csdn.net/hu166123/article/details/116492859">揭秘：云控系统运行原理，有效规避风控_云控脚本原理是什么-CSDN博客</a></li>

</ul>
</details>

**社区讨论**: 社区讨论显示，该模块的仓库作者对曝光做出了回应，声称相关恶意代码已被移除并否认与自己有关。这表明在后门被公开发现后，作者试图撇清责任。

**标签**: `#Android安全`, `#Xposed框架`, `#恶意软件`, `#数据隐私`, `#QQ`

---