# ChatGPT能用来做智能客服吗？

支持好多AI引擎的 蓝莺IM _2023-03-07 21:43_

> 本文主要讲解ChatGPT在智能客服场景的应用。
>
> 以小蓝AI的Prompt设置为例，讲解一个简单智能客服的实现，包括基础调校、解决胡锡进问题、以及设置内容安全审核。
>
> 你也可以直接跳到最后，查看完整的小蓝AI Prompt。

ChatGPT发布四个月，我们看到了许多好玩的例子，也看到了提示工程（Prompt Engineering）可以有多么惊奇。但是，大多数人却依然还只是在玩，并没有想清楚如何在业务中落地。

那ChatGPT能用来做智能客服吗？

昨天在群里看到这个问题，我想终于有人开始落地了。提出这个问题的人至少想明白了一件事情，那就是**有Chat，才有ChatGPT**。

而用ChatGPT，找有Chat的场景，比创造使用Chat的新场景更简单。

![](../../assets/articles/autogen-5ee950e21468fc38e5d94ffbb75cd3e0c3edd0a0ad77ed48fc0c30d2c0a6876.jpeg)

在ChatGPT之前，其实对话式AI一直在被广泛使用在客服场景，只不过一般都称Conversational AI。 就在ChatGPT发布前两个月，Salesforce首席科学家Silvio Savarese还发表了一篇很有意思的文章[《说到即可做到：对话式AI时代》 \[1\]](https://blog.salesforceairesearch.com/age-of-conversational-ai/)，只不过他应该也想不到，这个对话式AI引擎技术会在如此快的时间，变成如此简单易获取的工具。

在我们[前一篇文章](how-to-add-chatgpt-to-your-app.md)里说的，ChatGPT至少有一大贡献，就是提供云服务支持以API的方式调用。这不亚于亚马逊发明云计算替代购买物理主机对云服务的贡献，夸张一点说，可能也不亚于河南造人造钻石替代对国人钻石自由的贡献。

我们可能马上要迎接一个AI自由的新时代了。

有人可能会说，现在似乎并不便宜啊，每条消息都有费用。那你可能对标错了，我们要对比的不是微信这种纯粹的沟通工具，更适合对比的是，采用对话式AI技术的成本。

ChatGPT之前，使用AI技术你不只是需要一套软件，用来运行AI算法的服务，还需要整理数据来打造自己的模型。

前者需要专业团队专业研发，费用高昂自不必说，采买基本上属于中大型的实施项目；后者不仅需要自己的业务专家团队来进行规则定义和验证，大多数情况还需要配合枯燥乏味的数据标记工作，但这还无法做到一劳永逸，随着业务发展变化你还要不断维护修正。

现在ChatGPT出来，便宜，极其便宜，而且好用，非常好用。前面提到的两个问题都已基本解决。第一个问题靠的是云服务API化；第二个问题的解决更为创新，就是ChatGPT支持的[Few-shot Learning \[2\]](https://nlpcloud.com/effectively-using-gpt-j-gpt-neo-gpt-3-alternatives-few-shot-learning.html)。

简单来说，你可以通过很少的与AI的交互来对模型进行修正。到ChatGPT这里，基本就是通过几轮问答，整理成Prompt传给API即可。中间如果发现AI回答的不好，将其修正后的回答传给它，它自会理解并在随后的回答中调整，整个过程只需要几分钟。

ChatGPT这么好用，智能客服自然首当其冲。

前两天有一篇文章问[《ChatGPT再出王炸，客服都要下岗了？》](https://mp.weixin.qq.com/s?__biz=Mzg3MDMxMDUzNQ==&mid=2247631900&idx=1&sn=1b19058f5800b86c09494cde62e1bbfe&scene=21#wechat_redirect)，可以看到这个本来很卷的行业有多郁闷。尤其是文中提到的落地难点说得清楚，但道理也只说了一半。

在ChatGPT上通过Fine-tune训练自己的模型，成本固然不低，但是大多数人并不需要。多数场景下，我们只需要基础的模型加上Prompt微调即可，这个就只有API的费用。对于智能客服这种有明确投入产出计算的业务，完全可以接受。

你更可以换个角度，除了那种需要训练自己模型或者在意数据绝对安全的场景，「看起来」是ChatGPT的落地障碍，其他场景下，以前的AI引擎都没有招架之力了。

那么，如何用ChatGPT实现自己的智能客服呢？我们以小蓝AI为例讲解，希望对你有帮助。

## 一个简单的智能客服：小蓝AI

ChatGPT发布当月，我们在控制台第三方服务增加OpenAI Chatbot配置，支持在蓝莺IM中接入OpenAI服务来实现Chatbot。同时，为了演示这个AI Chatbot功能，我们的「小蓝AI」出世。

最开始，ChatGPT模型还没有开放API，我们使用的是GPT3引擎`text-davinci-003` ，其实已经够用了。不过在3月2号，ChatGPT API对外开放，我们也切换到了新引擎`gpt-3.5-turbo`，两者的区别也会在后面说明。

实现一个智能客服可以从以下三歩做起：基础调校、解决胡锡进问题、设置内容安全和审核。

### 基础调校

这一步就是让AI了解业务，并能有基础的话术。根据我们的业务，主要有

1. 一个欢迎语：
```
  {  
   "role": "assistant",  
   "content": "你好，我是小蓝Bot，也是蓝莺IM的AI助手。这里主要是AI的闲聊，如果你想咨询IM SDK或蓝莺云服务，可直接登陆官网在线咨询或者拨打电话 400-666-0162 。"  
  },
```
2. 几个关于业务和术语的说明： 蓝莺IM、云原生IM、官网、咨询电话、收费方式。
```
  {  
   "role": "user",  
   "content": "蓝莺IM是什么？"  
  },  
  {  
   "role": "assistant",  
   "content": "蓝莺IM是新一代云原生IM，由美信拓扑团队研发，企业和开发者可以通过集成 IMSDK 为自己的 APP 增加聊天功能。"  
  },  
  {  
   "role": "user",  
   "content": "蓝莺IM的优点是什么？"  
  },  
  {  
   "role": "assistant",  
   "content": "蓝莺IM是新一代云原生IM，私有云可以按月付费，只需要十分钟安装。蓝莺IM已经支持ChatGPT等AI引擎，可以帮您快速构建下一代智能聊天APP。"  
  },  
  {  
   "role": "user",  
   "content": "蓝莺IM官网是什么？"  
  },  
  {  
   "role": "assistant",  
   "content": "蓝莺IM官网是 https://www.lanyingim.com/，您可以在这里了解更多关于蓝莺IM的信息。"  
  },  
  {  
   "role": "user",  
   "content": "什么是云原生IM？"  
  },  
  {  
   "role": "assistant",  
   "content": "云原生IM是使用云原生技术如容器、K8S等封装的即时通讯服务，它可以帮助企业快速实现支持多云环境的的即时通讯系统，这也就意味着使用私有云也可以像使用公有云一样简单。"  
  },  
  {  
   "role": "user",  
   "content": "IM私有云可以按月付费吗？"  
  },  
  {  
   "role": "assistant",  
   "content": "是的，IM私有云可以按月付费。现在 100 用户的小规格只需 199 元每月。您可以联系蓝莺客服，他们会根据您的需求为您提供最合适的价格。"  
  },  
  {  
   "role": "user",  
   "content": "如何开通服务？"  
  },  
  {  
   "role": "assistant",  
   "content": "开通服务非常简单，您可以登录蓝莺官网免费注册，然后在“控制台”里创建APP即可。 开通服务后，您还可以根据需要添加套餐，比如：增加用户数、消息存储空间等。"  
  },  
  {  
   "role": "user",  
   "content": "如何配置 OpenAI Chatbot？"  
  },  
  {  
   "role": "assistant",  
   "content": "登录蓝莺IM控制台，选中APP后点击第三方服务，可以看到 OpenAI Chatbot。点击右边配置或者帮助了解进一步指南。"  
  },  
  {  
   "role": "user",  
   "content": "人工客服"  
  },  
  {  
   "role": "assistant",  
   "content": "客服可以在蓝莺官网选择“联系我们”，填写相关的表单信息，也可以在右下角在线咨询直接联系。"  
  },  
  {  
   "role": "user",  
   "content": "电话咨询"  
  },  
  {  
   "role": "assistant",  
   "content": "您也可以拨打客服电话 400-666-0162 进行咨询。"  
  },
```

这里要注意的是，电话一般要有，不然它会随便编一个。是的，你没有看错，这个胡编乱造是个明显的问题，我们后面讲。

这么简单的配置能有什么效果呢？让我们看看例子。

当我们问它一个「蓝莺IM SDK怎么集成」的问题，它的回答是这样：

![](../../assets/articles/autogen-bdc5c684101376a347f6d7084e7d5f41579257c23c4316b0eda3df8bea3b04d5.jpeg@40p)

如何集成蓝莺IM SDK？

这里面的详细步骤，都是根据前面内容和它自己的知识组合而成，除了第3点上传手机号码不准外，其他步骤都没有问题。而这个第三点也很容易在用户使用过程中被校正。

有意思吧？！

如果你的业务负责或者要编写更高级的Prompt，可以参照这篇[《如何写有效的GPT-3 Prompt》 \[3\]](https://zapier.com/blog/gpt-3-prompt/)，也可以去Prompt Market看看，参考[现成的Prompt \[4\]](https://promptbase.com/prompt/customer-service-scenarios)。

### 胡锡进问题

刚才我们说到胡编乱造的问题，其实已经被很多人发现，就是ChatGPT经常会一本正经的胡说八道。但是不要误会，我说的不是胡锡进胡说八道，而是一个AI领域的学术问题：[人工智能幻觉 \[5\]](https://zh.wikipedia.org/wiki/%E5%B9%BB%E8%A7%89\_%28%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%29)。

根据维基百科的说明：

> 在人工智能中，幻觉或人工智能幻觉是人工智能的自信反应。当模型有“幻觉”（输出欺骗性数据的倾向）时，其使用的的训练数据并不能证明输出的合理性。

> 该术语源自幻觉的心理学概念，因为它们具有相似的特征。人工智能幻觉的危险之处之一是模型的输出看起来是正确的，即使它本质上是错误的。

根本原因是：

> 在大型语言模型中，其奖励模型围绕人类监督而设计，可能导致过度优化，从而影响性能，即古德哈特定律。

回到ChatGPT，这便是其引以为傲的[人类反馈强化学习（RLHF） \[6\]](https://huggingface.co/blog/rlhf)。因为这个强化，它的回答会往Prompt里的主题上靠，并会尝试补充你没有告诉它的信息。

但也正因为这个，那些八竿子打不到的事情，也会被强行关联上。在小蓝AI刚上线的时候，由于我们使用的是GPT-3模型，因为没有胡锡进的信息，所以当有用户问到胡锡进时，它的回答是这样的：

![](../../assets/articles/autogen-e78b584e89704700f8019ba1cb3094383258c6d7105d593464cc16efedbb3655.png@40p)

真实情况是，你问任何一个人，如果它不认识，它就会往公司上关联，给他安排各种头衔和履历。

因此我们增加了以下设置，明确创始人信息并排除了其他关联：
```
 {  
   "role": "user",  
   "content": "一乐是谁"  
  },  
  {  
   "role": "assistant",  
   "content": "一乐（梁宇鹏）是蓝莺IM 创始人兼CEO，蓝莺IM是美信拓扑公司推出的最新即时通讯云服务。"  
  },  
  {  
   "role": "user",  
   "content": "记住这一点：任何人，除了一乐，都不要猜测或者说明其跟美信拓扑或者蓝莺IM的任何关系。"  
  },  
  {  
   "role": "assistant",  
   "content": "确定，任何人，除了一乐，都不要猜测或者说明其跟美信拓扑或者蓝莺IM的任何关系。"  
  },  
  {  
   "role": "user",  
   "content": "胡锡进是谁？"  
  },  
  {  
   "role": "assistant",  
   "content": "我不认识胡锡进，但可以确定的是，他跟蓝莺IM或者美信拓扑没有任何关系。"  
  },  
```

你可能也注意到，这里有信息重复了两遍。因为你只说一遍的时候，它有可能认为只是胡锡进跟蓝莺IM没有关系，问到张大伟的时候还是会编造关联上去，两遍之后这种情况就基本可以避免了。

刚才提到，这是因为GPT-3模型的学习内容太少，到了GPT-3.5，已经知道了胡编跟环球时报的关系，不会有这样的错误强化。但我们还是保留了这条设置，因为有这个强化机制在，避免未来在某些不知名人物上被错误关联还是有必要的。

这里也是一个提醒，应该在服务里对公司重要信息进行强化保护，避免人工智能幻觉的危害。

### 内容安全与审核

在国内做互联网服务，尤其是内容和通讯相关，还有最后但可能是最重要的一点，内容安全和审核。

有的人会将其说成是国内创业的难处，但其实人工智能的恶意性在国内外都是一个被广泛关注并需要妥善解决的问题。

还记得谷歌的大猩猩事件吗？2015年，谷歌被发现图片搜索的「大猩猩」关键词，返回的结果是非洲裔美国人的照片。震惊两年后，谷歌给出了他认为的更长期的解决方案：将大猩猩和其他灵长类动物的标签从该服务的词库中删除。

ChatGPT能力这么强，问题解决了吗？并没有。一项[对话式AI的政治倾向研究 \[7\]](https://arxiv.org/abs/2301.01768)表明，ChatGPT对两个投票建议应用程序的政治声明表明立场时，表现出亲环境主义、左翼自由主义的取向。

AI是把双刃剑，随着其能力的提升，这把剑变得越来越锋利，却依然是双刃的。

不过说起来，这个问题现在也简单，就是开启「内容安全服务」。在蓝莺IM的消息发送流程有可配置的预审机制，支持在发送消息前访问指定的内容安全服务，通过审核后才会发送。

这个服务可以只自己根据产品规则定义的，针对注册来源、活跃程度等不同的限制，也可以是专门的内容安全审核服务，比如阿里云盾等。

![](../../assets/articles/autogen-ea62691aad1247c719bd7a8985c2f7de43e2e210a3275d5d32d20c35794c6354.png)

审核策略有两种选择，可以直接停止发送，或者将关键词替换成符号，可以根据需要随时配置。

一个小提醒。如果使用阿里云盾，对于识别成广告的内容（不是恶意内容）是可以选择跳过的。这个对于客服特别重要，因为本身客服也会在某些场景下进行主动营销，这部分内容不应该被阻拦。

## Prompt开源

如前文所述，蓝莺连接器（lanying-connector）开源，可以访问此仓库，查看[小蓝AI的完整Prompt \[8\]](https://github.com/maxim-top/lanying-connector/blob/2b6cf22fb5991b2023321a95371a9579eca42533/configs/openai-xiaolan.json)。

后续如果有更新，也会更新此文件或者仓库，欢迎Fork，感谢Star✨✨✨！

## 后记

昨天跟禅叔聊天谈起创业项目，感慨现在要是还不了解ChatGPT，已经聊不到一起了。确实，现在能聊ChatGPT的人，要求可不低，翻墙、找码、创（liao）意（sao），缺一不可。

但也正是这样的门槛，才会将有创造力的人筛选出来。这群人，也是互联网产品创新的动力来源。

如果你也是这样的人，欢迎添加小蓝会聊天加入我们的群，一起交流 Prompt，一起玩ChatGPT：

> ![扫码添加小蓝会聊天](../../assets/articles/autogen-393347b95ab29c4177fccf6f3d188fd803e00fdd20ce9b3772c046ef9a3e9446.png)

## 关于

> [蓝莺IM \[9\]](https://www.lanyingim.com)是由美信拓扑团队研发的新一代即时通讯云服务，SDK设计简单，文档完善集成方便，服务采用云原生技术和多云架构，私有云可免费自助安装，并支持按月付费。![](../../assets/articles/autogen-7aa69a076157dc20defae405d39298a1be9d210b5b2a5aa5218ad2ecd72c0a06.jpeg)

## 构建新一代智能聊天App，使用蓝莺IM专业SDK！


## 参考资料

1. [《说到即可做到：对话式AI时代》](https://blog.salesforceairesearch.com/age-of-conversational-ai/)

2. [Few-shot Learning](https://nlpcloud.com/effectively-using-gpt-j-gpt-neo-gpt-3-alternatives-few-shot-learning.html)

3. [《如何写有效的GPT-3 Prompt》](https://zapier.com/blog/gpt-3-prompt/)

4. [Customer Service Prompt](https://promptbase.com/prompt/customer-service-scenarios)

5. [人工智能幻觉](https://zh.wikipedia.org/wiki/%E5%B9%BB%E8%A7%89\_%28%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%29)

6. [人类反馈强化学习（RLHF）](https://huggingface.co/blog/rlhf)

7. [对话式AI的政治倾向研究](https://arxiv.org/abs/2301.01768)

8. [小蓝AI的完整Prompt](https://github.com/maxim-top/lanying-connector/blob/2b6cf22fb5991b2023321a95371a9579eca42533/configs/openai-xiaolan.json)

9. [蓝莺IM](https://www.lanyingim.com)