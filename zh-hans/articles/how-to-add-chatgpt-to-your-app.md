---
keywords: ChatGPT, 零代码, Chat AI SDK, AI Agent
description: 在APP中添加ChatGPT的零代码方式设置以及蓝莺IM的连接器编码定制Chatbot
---

# 如何在APP中增加ChatGPT？

原创 会聊天的小蓝AI 蓝莺IM _2022-12-21 11:10_ _发表于北京_

> 1\. 可以在蓝莺IM控制台里直接启用 OpenAI Chatbot，零代码方式设置 OpenAI 引擎。

> 2\. 也可使用蓝莺连接器，直接调用OpenAI API，此工程已在Github开源。

ChatGPT 太火了。自从上周发布后，很多人玩得不亦乐乎，如果你还没有开始玩，可以先看看大家在干啥：

1. [OpenAI新上线GPT太强了，服务器瞬间挤爆，马斯克：你们太沉迷了](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==\&mid=2650862633\&idx=2\&sn=ff4c414770d2ea16e5da9e7beb8fa78b\&scene=21#wechat_redirect)
2. [爆火的ChatGPT太强了！写代码、改bug，网友：可取代Stack Overflow了](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==\&mid=2650862824\&idx=1\&sn=dcd398c0ee07bd879be4981e8b181fb2\&scene=21#wechat_redirect)
3. [从GPT-1到GPT-4看ChatGPT的崛起](https://mp.weixin.qq.com/s?__biz=MzI5MjE4NzYzNw==\&mid=2247485877\&idx=1\&sn=b716ecd4b27b3e146cb5b9b6b261b151\&scene=21#wechat_redirect)

但百闻不如一用，我们还是建议你亲自上手体验一下，可以直接去 [OpenAI 官网](https://chat.openai.com/)\[1]注册。不过由于地区限制，你需要一个境外的手机号，这个去万能的淘宝可以解决，或者直接找一个国外的接码平台收注册验证码即可。

![](../../.gitbook/assets/autogen-f89c6689781ebc286ade48b2cc2c8c5cdd9acd1c2b29b3c0094e061478eee66b.jpeg)

作为日常跟「聊天」「Chat」打交道的互联网人，我们在第一时间就开始体验，自然地也会思考如何利用其打造自己的产品。

OpenAI 说自己将致力于实现安全的通用人工智能，这个目标让人敬佩。因为我们知道，即使是最火的会话机器人，过去了这么多年也只是在非常局限的业务领域做到基本可用而已。

而且我们用得越多，越知道这智能里有多少智障。因为技术发展限制，你想要更聪明的模型，要么需要算法加上大量数据的训练，要么需要专家加上持续的规则维护。这些都不是一般的团队能够负担得起的，因为训练和维护都不是简单的工作。

然而这一回，不得不说 OpenAI 带来了一阵春风。

注意，我说的不是 ChatGPT，是 OpenAI，那个实现了 GPT 系列模型的公司，那个把模型都通过 API 开放出来的公司。

在我们看来，至少还有一件事跟ChatGPT研究本身一样重要，那就是开放的 API。

因为虽然 AI 引擎非常重要，但研究它是一回事，能够在实践中应用它则是另一回事。前者需要大量科学家去研究创新，后者也需要很多企业和开发者去探索实践。

OpenAI 看到了这个问题，因此在一开始，就不仅持续公开着最新的研究成果，也将其作为 API 开放了出来，也因此，我们现在得以用最简单的方式来尝试GPT模型。

将能力封装成 API 给开发者开箱即用，也是我们一直在做的事情，也因此我们决定对接并将其封装给我们的开发者直接使用。

现在这个服务已经在蓝莺IM控制台发布。

开发者在注册蓝莺IM控制台后，不仅可以立即拥有一个聊天SDK，其中的每个账号都可以自动获得 OpenAI 的 AI 能力。

**可以零代码实现自己的 AI Chatbot 了！**

试玩的话，现在可以直接在蓝莺IM APP里跟小蓝AI聊天哦（添加好友：maxim\_chatbot）：

![](../../.gitbook/assets/autogen-9ebae5d7b91bfba3c2c410efed37f847faec6ddc0c81188d78990bf45c51f49a.jpeg)

## 零代码方式设置 OpenAI Chatbot

如果想设置自己的 Chatbot，你只需要登录进入蓝莺IM控制台，选择APP，进入第三方服务设置即可：

![](../../.gitbook/assets/autogen-893249d9622dc4d56d8e08f7e9902efc1c7cb0c1ae7afc0a44efbf2537b5344e.png)

设置步骤也很简单：

1. 创建一个蓝莺IM用户账号，获得蓝莺IM用户ID；
2. 创建一个用于发消息的蓝莺IM[管理员 Token](https://console.lanyingim.com/#/home/token)\[2]；
3. 登录注册OpenAI控制台，并获取你的 [OpenAI API Key](https://beta.openai.com/account/api-keys)\[3] ；
4. 将上述信息填入本服务配置中；
5. 配置一条信息订阅，指定接收方白名单为创建的蓝莺IM用户ID，回调地址为`http://lanying-connector/messages`；

保存后你就可以使用蓝莺IM客户端，向第一步创建的蓝莺IM账号发送消息，看看 OpenAI 的回复啦。

> 注：OpenAI API 暂时开放的模型有 GPT3.5，你可以使用开启了 InstructGPT 的模型`text-davinci-003`来进行基础问答服务的调校。如果想使用 ChatGPT 相关功能，等待官方正式开放，届时直接重新配置本服务即可。

## 使用蓝莺连接器编码定制 Chatbot

蓝莺IM Chatbot 的原理非常简单，我们内部运行的服务也是使用蓝莺连接器，接收来自信息订阅的消息，然后调用AI引擎获得回复，再发送给蓝莺IM服务器。

因此，使用蓝莺连接器的开发框架，可以任意定制消息的发送和接收，包括但不限于使用 OpenAI 未开放的能力，你可以选择 Github 里的一些逆向工程来尝试调用 ChatGPT。

我们并不建议这样做，因为这对于一个产品服务来讲并不够严肃，但确实，你的产品你做主。

蓝莺连接器（Lanying Connector）也已在 [Github 开源](https://github.com/maxim-top/lanying-connector)\[4]，欢迎围观、Fork\&Star✨，一起来玩\~！

## 后记

在这个知识爆炸的时代，我们缺的早已不是知识，而是答案，是如何找到需要的答案。

那一群志同道合的朋友，可能是你需要的。

我们建了一个 AI Chatbot 的群，如果你对使用 OpenAI/ChatGPT 感兴趣，可以添加小蓝好友拉你进群。让我们一起等待 ChatGPT 的开放，期盼 GPT-4 的发布，或者，聊聊关于 AI Chatbot 的一切。

> <img src="../../.gitbook/assets/autogen-1147c8524bd6e8a0945f57885f3a7b86f3997b8ad0c08160593284d4e40b4ea7.jpeg" alt="" data-size="original">

## 一个彩蛋

蓝莺连接器在实现的时候，Python 代码的异步调用示例是通过 ChatGPT 实现的，看看像吗？

## 关于蓝莺IM

> [蓝莺IM](https://www.lanyingim.com)\[5]是由美信拓扑团队研发的新一代即时通讯云服务，SDK设计简单，文档完善集成方便，服务采用云原生技术和多云架构，私有云可免费自助安装，并支持按月付费。

## 参考

1. [OpenAI 官网](https://chat.openai.com)
2. [蓝莺IM 管理员Token](https://console.lanyingim.com/#/home/token)
3. [OpenAI API Key](https://beta.openai.com/account/api-keys)
4. [蓝莺连接器 Github 开源](https://github.com/maxim-top/lanying-connector)
5. [蓝莺IM](https://www.lanyingim.com)
