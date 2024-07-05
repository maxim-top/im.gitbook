---
description: 讨论了ChatGPT的下一步发展以及GPTs在企业级应用中的重要性
keywords: ChatGPT, GPTs, AI智能体, IM云服务
---
# ChatGPT的下一步，AltGPTs

原创 一乐 蓝莺IM _2023-12-12 10:11_ _发表于北京_

> 蓝莺GPT商店发布，AI开发者们可以分享自己定制的Chatbot了！🎉🎉🎉
> 
> 阅读本文，跟我们一起回顾生成式AI元年，看GPTs为何如此重要。
> 
> 也看看为什么要做企业级GPT，然后聊聊这个新的GPT商店怎么玩 :D

ChatGPT一周年，[以OpenAI的宫斗结束](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652412695&idx=3&sn=21103223bfa7b097758780a9bf8d4594&scene=21#wechat_redirect)，八卦与狗血，一度将DevDay的光芒遮蔽。

也让很多人忽略了这个可能是OpenAI生态建设的最重要措施，可分享的GPTs和GPT商店。

11月4日，OpenAI DevDay发布GPTs消息时，我们的GPT商店AltGPTs就已完成产品设计，并在随后的[GTLC华中站·Agent黑客马拉松](https://docs.lanyingim.com/articles/activity-report/what-can-we-make-in-an-ai-agent-hackathon.html)中对所有参与者进行了预览发布。

参加黑客马拉松的所有作品均使用蓝莺AI服务搭建，包括智能消息、企业知识库和AI插件，并将Chatbot发布成GPT胶囊，供其他Chatbot创建者使用。

这里，我们将可生成定制Chatbot的GPT应用称为GPT胶囊，而不是GPTs，因为它比GPTs更加强大，用《七龙珠》里的万能胶囊形容更加贴切，具体原因我们稍后展开。

在下文关于应用分发机制的讨论中，你可以认为GPT应用、GPTs、GPT胶囊是一样的，他们都是由开发者定制的GPT。

如果把GPTs看做GPT应用的初始形态，那GPT商店其实是GPTs的分发平台，毫无疑问，它对OpenAI的重要性会像APPStore之于Apple一样。鉴于当前阶段仍是百模大战，OpenAI并没有像Apple一样的生态统治力，这也就意味着，所有大模型都需要一个这样的分发平台。

因此，我们发布这个**企业级的GPT商店，蓝莺AltGPTs**，让所有大模型服务都可以有一个GPT商店。

![DALL·E 2023-12-12 04.00.52 - A high-resolution image of 1920x1280 for an AI robot marketplace named 'AltGPTs', with the 'G' in 'AltGPTs' capitalized. ](../assets/articles/autogen-49af4a3b6cad3ab41d234caed5bbf98fa41f68308e4f4da117e35c60585abb4a.jpeg)

看名字你也知道，它也是对Altman的一次致敬。

在详细介绍AltGPTs前，我想有必要讨论两个问题，1）为什么我们觉得GPTs如此重要；2）为什么我们需要企业级GPT，而不仅是GPTs。

## 为什么GPTs如此重要

权游大戏已经落幕，让我们回归AI本身，看看过去一年跟AI一起走过的路。

2022年11月30日，OpenAI在发布ChatGPT的时候，我们就意识到，AI的跨越升级开始了。于是12月上线智能消息服务，并说明了[如何在APP中增加ChatGPT](https://docs.lanyingim.com/articles/product-and-technologies/how-to-add-chatgpt-to-your-app.html)。

2023年3月，因为RLHF能力的强大，我们也开始将AI应用在[智能客服](https://docs.lanyingim.com/articles/product-and-technologies/how-to-implement-an-intelligent-customer-service-by-chatgpt.html)中，并尝试用提示词解决幻觉等实际问题，提出了[ChatGPT做智能客服的十条服务准则](https://docs.lanyingim.com/articles/product-and-technologies/chatgpt-intelligent-customer-service-ten-service-guidelines.html)。

随着大模型AI技术的热潮到来，越来越多的人加入大模型产业。大模型上下文的限制以及开源大模型Llama等的出现，促使很多垂直领域的公司开始搞基座大模型。

7月，基于对大模型工程技术的了解和成本产出比的朴素认知，我们开始提醒客户和合作伙伴循序渐进使用大模型AI服务，[不要总想着自己训练大模型，你的业务可能并不需要](https://docs.lanyingim.com/articles/Industry-development/do-not-train-your-own-llm-your-business-might-not-need-it.html)。

与此同时，我们发布了[企业知识库服务BlueVector](https://docs.lanyingim.com/articles/product-and-technologies/It-is-time-to-make-LLM-learn-enterprise-knowledge.html)，支持通过通过上传文档和配置网站内容来定制AI，作为我们对垂直领域场景的解决方案。

同时增加了[给微信公众号配置客服AI](https://docs.lanyingim.com/articles/product-and-technologies/We-added-an-AI-assistant-to-our-WeChat-Official-Account.html)的功能。

8月，国产大模型开始商业化，加上监管新规的执行，我们增加了[国产大模型支持](https://docs.lanyingim.com/articles/product-and-technologies/how-to-choose-domestic-llm-services.html)。

10月，我们发布了使用函数调用实现的AI插件服务，让[AI可以驱动应用](https://docs.lanyingim.com/articles/product-and-technologies/AI-Powered-Applications-Plugins-App-Store-and-AI-Agents.html)。其实早在3月，OpenAI就发布了插件机制，可惜曲高和寡，作为调整方案，其又在6月发布了支撑插件服务的函数调用接口，这个功能让AI可以更高效识别用户意图进行函数调用。

11月，OpenAI发布一周年到来之际，OpenAI DevDay发布了GPTs，并介绍了未来的GPT商店。如前所述，我们的AltGPTs也已开始开发，这就是你今天看到的跨大模型的企业级GPT商店。

这一年里，我们做的事情都在围绕AI应用落地，我们也接到了来自从国企央企到互联网公司，再到超级个体KOL的各种需求，我们清楚看到了市场两极分化的程度，看到了能力与应用之间的鸿沟。

**企业应用方面进展比预期要慢。**

一方面，很多企业并没有想清楚如何将AI应用在业务中，他们也需要理解为什么大模型AI与之前的AI不同，什么是适合AI做的，什么不是。

另一方面，很多看似简单的原理和方案，在实际应用中仍然有很多工程问题要解决。这虽然是我们做应用框架的机会，但很多公司都忍不住要自己先试一试，即使他们最终都会发现跟我们方案之间成熟度易用性的的差距。

这明显拖延了AI在企业应用中落地的速度。

**但大模型从未停止进化。我们看到了越来越多的可能性，也越发相信智能时代的未来。**

跟我们有同样感受的，就是那些在各个社群里分享AI技巧的极客们。他们或在完善或在突破，不断探索AI能力的边界。

他们欣喜的交流最近用ChatGPT完成的工作，做到的炫酷的事情，但是最后分享的，缺只能是一段冗长的提示词，需要感兴趣的朋友复制粘贴，在自己的OpenAI账号下艰难重现。

让这种情况越来越难的，是AI Agent的热潮，由Lilian Weng的一篇关于[大模型驱动的自治智能体](https://mp.weixin.qq.com/s?__biz=Mzg2OTY0MDk0NQ==&mid=2247502724&idx=1&sn=3d3eea620abbb46f09dc3b7440ac36be&poc_token=HOhLd2WjFJ5od4HrU6BnWKuiko_OkCmD49iRUoju&scene=21#wechat_redirect)文章引爆。

因为一个完整的AI Agent不是几句提示词所能够代替的，它需要更强的规划以实现完成业务，需要有更大的记忆来存储领域知识，还需要有驱动业务的工具。

这也分离了**GPT开发者和GPT使用者。**

我们用前者来代替那些走在前面的AI探路者，那些充满AI技巧的极客们，用后者来代替那些对AI充满好奇，但由于研究时间和经验限制，主要精力都在体验和感受AI的人。

我之所以有这样的感慨，因为我今年在多个大会分享过，也观察了TGO鲲鹏会会员对AI的使用。在这个号称集中了全中国最懂技术的一千个CTO的社群里，还有相当一部分人没有用过ChatGPT，这令人难以想象。

但是你看，当我们将GPTs看为应用，区分开了GPT的开发者和使用者，这是不是像极了APP开发者和使用者？

**有了GPTs，GPT开发者的发现和知识可以从解决自己的问题到开始解决别人的问题，从分享好玩的文字（提示词）到分享好玩的工具，甚至通过分享这样的工具获得收益**。

GPTs让OpenAI有了开发者生态，而只有有了开发者，企业对AI的理解和后续的应用落地才有可能加速。

## GPTs的局限与企业级GPT

但GPTs是有局限的，这也是很多人用起来的感受，它还是不够强大。

1\. 知识库大小受限且类型单一

我们知道，GPTs可以上传文件，但文件大小是有限制的，而且使用方式较为单一。按照之前我们对Agent所需要的记忆的理解，这种存储模式其实还只能用在知识记忆和有限的历史记忆，而不是更丰富的业务记忆和会话记忆。

2\. 知识文件没有权限控制和数据保护

最重要的上传的文件可以轻松通过提示词被使用者获取，这在企业应用甚至是某些个人应用或数字分身里，都是很难令人接受的设定。

3\. 动作Action比较简单

GPTs确实可以通过Action来调用外部系统，但是这跟能够支持[千级别API导入处理的AI插件](https://docs.lanyingim.com/articles/product-and-technologies/Enable-AI-integration-for-businesses-with-APIs.html)来比，说玩具虽然有些夸张，但差距仍是十分明显的。

在API调用鉴权特别是OAuth的时候不稳定经常出错，是尝试过的朋友的第一感受。

4\. 使用对话方式构建GPT有难度

当前构建Agent的方式，有三种典型操作：

一种是手写提示词，然后对话调教，就像GPT Builder一样； 另一种是通过GUI界面定义工作流，使用拖拽等方式进行流程沉淀，例如[ChatFlow\[1\]](https://github.com/prompt-engineering/chat-flow)； 还有一种更倾向于使用编程方式进行流程定义和编排，像[微软PromptFlow\[2\]](https://github.com/microsoft/promptflow)、刚刚开源的[微博RillFlow\[3\]](https://rill-flow.github.io)以及尚未发布的[xAI PromptIDE\[4\]](https://ide.x.ai)。

虽然我们不能排除未来应用开发方式以对话构建的可能，但我们相信，在相当长一段时间内，需求和应用的复杂性意味着其需要更强大的IDE支持。

5\. 厂商锁定仅限于OpenAI

严格来讲，这不能算是GPTs的局限，GPTs当然是服务OpenAI的。但是对于企业级应用来讲，厂商锁定仍是一个巨大的风险，对于国内监管新规下企业更是不可忽视的问题。

以上这些，都是企业级GPT要解决的问题。

## 一个跨大模型的GPT商店

有了企业级GPT，就要有发现与分发机制，这就是我们今天发布的AltGPTs：

1. 它是企业级GPT/Agent的分发平台，因为我们支持构建企业级GPT；
2. 它是跨大模型AI的，因为我们支持多大语言模型，也只是随时配置；
3. 它可以让GPT开发者赚到钱，因为我们会增加GPT应用定价机制；

因为好用的工具，就是要完成应用的闭环，不管AI多么强大，它都需要与当前企业应用做对接，这部分并不是聊天那么简单。

而蓝莺AltGPTs将为所有LLM创建GPT商店机制，创建Agent开发、分发、收益分成的统一平台。

**如果你是AI领域超级玩家，喜欢分享自己的GPT应用，或者希望为私域的用户提供增值服务，欢迎添加文后公众号提前试用收费GPT。**

### 如何使用

如前所述，你只需要在创建Chatbot之后，使用生成GPT胶囊即可创建自己的GPT应用。

![生成GPT胶囊](../assets/articles/autogen-3b7216a66b5cd4ac9e8956f463f18b349c188d031dd9ced0c460840a745e4d6b.png)

生成时需要填写的主要内容为GPT简介，以及一个GPT开发者的lanying.link地址，方便使用者联系作者，再加上密码和定价：

![配置GPT胶囊](../assets/articles/autogen-57ce7b9e6e58e5601b4ffe0fbdbad668be7f79877020ae54cd5508c435a35d71.png)

之后，GPT开发者即可在创建Chatbot时导入GPT胶囊即可：

![导入GPT胶囊](../assets/articles/autogen-21019880c52176c2726afe539368b0b8b8210e6b5d5d561e0a930f3246c5cac2.png)

至于如何创建Chatbot，可直接搜索本公众号视频号查看使用指南。

## 后记

我们当然也知道，这一年，[多模态技术接连突破](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652386232&idx=2&sn=d3ca4bca6e4ca5d88db6f1486f6807cf&scene=21#wechat_redirect)，[开源大模型能力突飞猛进](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650898655&idx=4&sn=5ecf66dc8e862eb4dbd2d1b241327fdd&scene=21#wechat_redirect)，但我们关注大模型的能力进展，我们更加关注AI带来的新应用机会。

如果你有自己的观点或者想参与讨论，欢迎添加「小蓝会聊天」微信进群：

![扫码添加小蓝会聊天](../assets/articles/autogen-5d8b60effd72306cf5e0fbd4c1eda8269dd75bcde3679710d310f6541420ffb1.png)

本文内容已进入小蓝文章知识库，可使用蓝莺 Link 提问：

[https://lanying.link/00h0vp \[5\]](https://lanying.link/00h0vp)

## 关于蓝莺IM

**蓝莺IM是新一代智能聊天云服务。**

企业可以通过集成蓝莺IMSDK，同时拥有Chat和AI两大功能，当前AI引擎已支持ChatGPT（包括OpenAI和Microsoft Azure)、Minimax、百度文心一言、智谱AI，讯飞星火、阿里通义千问陆续接入中。

如果你希望在强AI时代打磨好自己的产品，欢迎继续关注蓝莺IM，我们会持续输出最新的经验与技术：

![打造新一代智能聊天APP，使用蓝莺IM SDK！](../assets/articles/autogen-20269538e00e0ddb6d6943e64f4e231fe573e37747283ab32bae58095aea24f5.jpeg)

## 参考资料

1. [ChatFlow](https://github.com/prompt-engineering/chat-flow)
2. [微软PromptFlow](https://github.com/microsoft/promptflow)
3. [微博RillFlow](https://rill-flow.github.io)
4. [xAI PromptIDE](https://ide.x.ai)
5. [小蓝文章助手](https://lanying.link/00h0vp)