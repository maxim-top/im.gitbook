---
description: 2024，对程序员们好一点，先给他们一个AI助手吧
keywords: AI助手, MultiAgent, IM SDK, 即时通讯SDK
---
# 2024，对程序员们好一点，先给他们一个AI助手吧

原创 小蓝会聊天 蓝莺IM _2024-01-26 10:02_ _发表于北京_

> 蓝莺AI开发助手上线，集成蓝莺SDK和API的时候，可以让AI帮忙写代码啦。
> 
> 每一个有API的SaaS/PaaS平台，都应该有一个API助手，如果你重视开发者体验的话。
> 
> 这是蓝莺AI案例分享第二篇《**AI开发助手与MultiAgent**》，第一篇是[智能客服](https://docs.lanyingim.com/articles/product-and-technologies/It-is-time-to-make-LLM-learn-enterprise-knowledge.html)。
> 
> 如果你关注大模型AI实践经验，欢迎持续关注我们，也可以添加文后微信进群，欢迎随时交流👏🏻👏🏻👏🏻

程序员们都应该用好ChatGPT，至少对于程序开发，ChatGPT就是下一代的搜索引擎。

我们很早就在分享这个观点，这来源于我们团队的实践。

当程序员们遇到问题时不再使用搜索引擎查找文章或问答社区，而是更多通过对话询问AI的时候，当[产品经理也开始编程](https://mp.weixin.qq.com/s?__biz=MjM5ODQwMjA4MA==&mid=2649294202&idx=1&sn=d3d47e35cc21292e24ac4ec7bf80be18&scene=21#wechat_redirect)，我们知道，**一个新的开发时代到来了**。

![](../assets/articles/autogen-bee6161648efd23887599ea5f54cf3ee086f731b23a409b826e36e0e6bc98d02.jpeg)

所以，作为一个在意团队成长的技术领导者，2024年首先应该做的，就是为团队成员提供这样的机会，让每个人用上ChatGPT。

与此同时，作为一个并不简单的PaaS平台，我们也一直在考虑如何提高开发者体验。

今天，这个问题终于有了一个不错的答案。

## 使用MultiAgent方式实现跨领域AI助手

作为一个IM PaaS平台/云服务商，我们是提供SDK和API服务的。虽然比起自行实现一个即时通讯系统来讲要简单得多，但大量的接口对于集成服务的开发者来讲还是有不少的难度。

准确来讲，单是服务端API接口有128个，同时与之对应的，每一个客户端也都有类似的接口。也就是说，在安卓、iOS、Web、C++等各端均有一套接口，而且它们属于不同语言的库。

在发布完企业知识库后，我们就在考虑使用API文档定制AI，为开发者提供一个懂蓝莺IM API的AI开发助手。但我们并没有对外发布，因为我们很快遇到了一个严重问题，**跨域干涉**。

因为不同端的这些接口，虽然语言不同，但功能基本相似，准确的说是一一对应。

如果选择将所有端的文档加入同一个知识库，当某端开发者（比如安卓）询问发送消息接口如何调用的时候，知识库里所有端的文档都会召回类似的知识。

而此时开发者只在意某一端（此为安卓端）的API用法，这样的知识库使用不仅浪费大量的上下文，也会让AI无从选择，最终它只能随机猜测，导致回复无法达到应有的领域精准度。比如，给安卓开发者提供iOS示例代码，给Web开发者提供C++示例代码等。

退一步的方案是，将知识库分别与不同的AI助手绑定，让每个AI助手只学习单独一端的知识，解决该端的相关问题。比如，安卓助手只加载安卓开发文档，iOS助手只加载iOS开发文档。这样通过五个AI开发助手，可以提供五种不同端的开发辅助服务。

这个方案虽然可行，但并不令人满意，因为它需要用户先选择AI助手，无法保证入口的统一，也就没办法使用一个微信/公众号提供全部服务。

**直到 MultiAgent 方案的出现**。

通过为所有助手增加了一个统一的协调者，做一个管理所有Agents的Agent。对外入口只有一个AI开发助手，它会先分析判断用户关注的是哪一个端，进一步将问题转给对应端的Agent。这样的转接完成后，对应端的Agent就可以针对性的加载知识库，直接服务开发者了。

我们也就得到了一个全新的小蓝AI：

![小蓝AI设计](../assets/articles/autogen-75f4d09598b3cfe9459fd8fd1c0890f5a795a8b373811d3ced17100f5e6fa348.png)

如图所示，它可以做三件事：产品介绍、商务咨询、开发辅助。

开发辅助方面，也就是我们刚才讲的开发助手，通过MultiAgent机制，其实是协调了六个垂直领域的Agent。背后每一个Agent，不仅通过企业知识库加载了领域知识，也通过智能插件（函数调用）增加了人工客服的支持。

所以，现在你可以跟AI询问API的用法：

![小蓝AI转接问题给指定开发助手](../assets/articles/autogen-4941f65d1572077c82aed619ce97b89c5756fbb6684af141dbc27b8b263cbd45.png)

![AI回答：发送消息接口如何调用](../assets/articles/autogen-5f3e9f1817f1bd56e1f79b91a5472e08ba6a7a8fb323ba26878c98eec216d827.png)

它也会在适当的时候提醒人工介入：

![AI提醒人工介入](../assets/articles/autogen-b9d9412be6c389d018ccaeaba31705ad73801574dab9704d2be8169643a47feb.png)

想要体验？点击[**查看原文**](https://lanying.link/3qur4g)，跟小蓝AI聊聊天吧~~

[https://lanying.link/3qur4g](https://lanying.link/3qur4g)

## 今日小发现：AI是会摸鱼的！

如前所述，我们转人工功能是通过智能插件也就是函数调用来实现的。基本原理就是告诉AI转人工的函数，然后提示词里说明「如果有回答不上来的问题，就转给人工」。

实际测试的时候却发现，它并不是在回答不上来的时候转人工，而是所有问题默认都转了人工。

是的，它在摸鱼。

为此，我们不得不将提示词中的「回答不上来可转人工」去掉，改成只有用户明确要求才将问题转给人工。

![智能插件：转人工](../assets/articles/autogen-32600b842321e796fc8657450c7874b64a3db50cd25956f49918a7ce41479dd8.png)

虽然是一个提示词设计问题，但当你发现这种摸鱼行为的时候，还是会有一种奇妙的感觉，哈哈。

如果你对使用智能插件感兴趣，可以阅读[这篇文章](https://docs.lanyingim.com/articles/product-and-technologies/AI-Powered-Applications-Plugins-App-Store-and-AI-Agents.html)，或者观看蓝莺IM视频号相关介绍：

## 后记

如果你有自己的观点或者想参与讨论，也欢迎添加「小蓝会聊天」微信进群：

![扫码添加小蓝会聊天](../assets/articles/autogen-5d8b60effd72306cf5e0fbd4c1eda8269dd75bcde3679710d310f6541420ffb1.png)

**让我们一起拥抱AI，期待美好的智能未来。**

本文内容已进入小蓝文章知识库，可使用蓝莺 Link 提问：

[https://lanying.link/00h0vp](https://lanying.link/00h0vp)

## 关于蓝莺IM

**蓝莺IM是新一代智能聊天云服务。**

企业可以通过集成蓝莺IMSDK，同时拥有Chat和AI两大功能，当前AI引擎已支持ChatGPT（包括OpenAI和Microsoft Azure）、Minimax、百度文心一言、智谱AI，讯飞星火、阿里通义千问陆续接入中。

我们会持续分享关于智能聊天ChatAI、大模型技术进展、AI Agent设计等方面的内容，也会分享典型AI应用案例，扫码关注再不失联：

![打造新一代智能聊天APP，使用蓝莺IM SDK！](../assets/articles/autogen-20269538e00e0ddb6d6943e64f4e231fe573e37747283ab32bae58095aea24f5.jpeg)
