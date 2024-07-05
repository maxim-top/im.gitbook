---
description: 除了Chat2SQL，如何使用AI访问数据库
keywords: AI, 数据库访问, IM SDK, 第三方推送
---
# 除了Chat2SQL，如何使用AI访问数据库

原创 小蓝懂AI 蓝莺IM _2024-02-04 17:35_ _发表于上海_

> 本文介绍如何使用ChatGPT访问数据库，相信对不喜欢SQL的你会有帮助。😁
> 
> 如果你想了解如何创建BI Copilot，打造工作台AI助手，这个方案也是适合的。
> 
> 这是蓝莺AI案例分享第三篇。
> 
> 欢迎持续关注我们，也可以添加文后微信进群随时交流👏🏻👏🏻👏🏻

AI时代我们需要什么样的产品？这个问题困扰在所有做AI应用的产品人头上。

刚开始的时候，我们发现ChatGPT数学虽有短板，但它擅长将自然语言翻译成SQL语言，所以有了Chat2SQL，仿佛AI这事与数据库无关，只需要应用层做些适配。

![](../assets/articles/autogen-4a81e3c77672f77d69260404f3f13d03c5af7cae7a40b1af92c3643b9a6ba3de.jpeg)

然而事情当然不会这么简单。

我们很快也发现，AI虽然可以写SQL语句，但方案却有很大的缺陷，无法进行权限控制，这在企业级数据管理中是无法接受的。

随着函数调用等功能的发布，我们找到了AI与业务结合的新方式，那就是函数调用和Serverless API。

通过把数据库封装成API服务，把原来的生成SQL语句查询数据库的过程，转变为生成SQL语句然后调用API接口。

这样既保留了SQL语言的灵活度，也保证了权限的有效管控。而且既然AI要解决用户掌握SQL语言的难题，完全可以更进一步，不需要用户接触SQL语言才是终结解脱。

因此，当我知道PingCAP在内测[TiDB Serverless\[1\]](https://tidb.cloud/?_gl=11ep1exl*_gaMTk1Njk1NjY2MC4xNzA3MDI0MTY4_ga_3JVXJ41175MTcwNzAyNDE2Ny4xLjEuMTcwNzAyNDMyNC42MC4wLjA)的时候，第一反应便是，这就是我们需要的。

![使用API访问AI DB](../assets/articles/autogen-2666de5a06dd27197bc582422a4435c6df31e248611b6a937dd6f5857edfc692.png)

也就是说，你可以在蓝莺智能插件中定义一个ChatTiDB的插件：

![在蓝莺AI服务中创建ChatTiDB插件](../assets/articles/autogen-9a511a14959950d24142c8dd375f2534e6e5c98fc4bde5109e74f5238d444f1e.png)

这个插件定义了两个函数，实际上调用的是同一个TiDB Serverless API，我们通过函数描述，提醒AI服务可以通过API获取数据库Schema以更准确组装SQL语句：

![定义Schema获取函数](../assets/articles/autogen-36ceb4bd2505f73ca1ddbb40e1b62a79ae26669ce966c5cfc7b700005db1654e.png)

需要注意的是，我们这里还设计了**函数优先级**功能。也就是可以**通过调整不同函数的优先级，可以提醒AI调用顺序，这在需要级联操作的功能中作用还是比较明显的**。

先获取Schema，就可以生成更准确的适配当前数据库结构的SQL语句，然后获取准确数据。

在这个例子，我们使用的是一个客户发过来的巨大Excel数据表格将其导入TiDB后，由后者自动建表后生成了Serverless API服务。

数据是某电网招投标项目的公开设备信息，数据较大远超过AI的上下文空间，而且满是专业术语。

我们问了一个关于「大类编码」的统计问题，这个问题中大类编码是只有在数据表格中出现，是特定场景的分类属于，统计又是ChatGPT的软肋。但当期读取了数据表格的结构后，明显是看懂了这句话：

![使用AI访问数据库中专有设备信息](../assets/articles/autogen-fbe335e1b8df479e6fd4701f2dbc49b51e6abdbd272e75804f2acdd69f4cff85.jpeg)

最后给出结论：

> 大类编码是10的物料共有26574种。

这便是我们今天介绍的蓝莺AI案例分享：**使用智能插件访问数据库服务**。

想要体验，可以使用以下链接跟AI聊一聊：

[https://lanying.link/5x7876 \[2\]](https://lanying.link/5x7876)

你可以问很多类似的问题：

> Q1 统计一下大类编码是10的物料有多少
> 
> Q2 列一下物料编码为 500132241 的详细信息
> 
> Q3 一次设备和二次设备信息里，中类名称是避雷器的还有那些小类名称？
> 
> Q4 统计下中类名称是避雷器的设备有多少小类
> 
> Q5 查询一次设备和二次设备表，列出小类名称是可控避雷器的物料编码

非专业人士看不懂但是AI回答准确，也许就是这个方案进步的地方了吧😊

这个方案适用于大部分与数据有关的场景，包括各种BI系统，可以为内部工作台提供Copilot助手的同时，保证权限管控。

PS：TiDB的探索远不止于此，他们还开始内置向量搜索的功能，并开始邀请内测，感兴趣的同学，可以[阅读此文\[3\]](https://www.pingcap.com/blog/integrating-vector-search-into-tidb-for-ai-applications/)。

## 后记

这是蓝莺AI案例分享第三篇，上一篇是[AI开发助手与MultiAgent](https://docs.lanyingim.com/articles/product-and-technologies/2024-be-kind-to-programmers-give-them-an-AI-assistant-first.html)。

如果你想关注我们关于AI的最新尝试或者参与讨论，也欢迎添加「小蓝会聊天」微信进群，让我们一起探索智能时代的新应用：

![扫码添加小蓝会聊天](../assets/articles/autogen-5d8b60effd72306cf5e0fbd4c1eda8269dd75bcde3679710d310f6541420ffb1.png)

本文内容已进入小蓝文章知识库，可使用蓝莺 Link 提问：

[https://lanying.link/00h0vp \[4\]](https://lanying.link/00h0vp)

## 关于蓝莺IM

**蓝莺IM是新一代智能聊天云服务。**

企业可以通过集成蓝莺IMSDK，同时拥有Chat和AI两大功能，当前AI引擎已支持ChatGPT（包括OpenAI和Microsoft Azure)、Anthropic Claude、Minimax、百度文心一言、智谱AI，讯飞星火、阿里通义千问陆续接入中。

我们会持续分享关于智能聊天ChatAI、大模型技术进展、AI Agent设计等方面的内容，也会分享典型AI应用案例，扫码关注不失联：

![打造新一代智能聊天APP，使用蓝莺IM SDK！](../assets/articles/autogen-20269538e00e0ddb6d6943e64f4e231fe573e37747283ab32bae58095aea24f5.jpeg)

### 参考资料

1. [TiDB Serverless](https://tidb.cloud/?_gl=11ep1exl*_gaMTk1Njk1NjY2MC4xNzA3MDI0MTY4_ga_3JVXJ41175MTcwNzAyNDE2Ny4xLjEuMTcwNzAyNDMyNC42MC4wLjA)
2. [某电网招投标AI助手](https://lanying.link/5x7876)
3. [TiDB Vector Search & Serverless](https://www.pingcap.com/blog/integrating-vector-search-into-tidb-for-ai-applications/)
4. [小蓝AI文章助手](https://lanying.link/00h0vp)
