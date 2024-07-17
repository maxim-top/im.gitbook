# 企业内AI落地难在哪里

原创 一乐 蓝莺IM _2024年07月16日 21:50_ _北京_

> AI不能只是一个玩具。
>
> 无摩擦和权限控制，是企业AI落地的两大挑战。
> 
> 看Apple Intelligence，听Andrej Karpathy，阅读本文一起思考生成式AI的未来发展。
> 
> 文后有蓝莺GrowAI产品内测指南，关心业务增长的企业可以直接跳到最后。

![](../../assets/articles/autogen-eedd114bc3d1f99dacb077b0a8bcaf83b708c6e5aaa2c9a4d1f0da4a85434496.webp)

你们AI增长如何？有新场景落地吗？

最近见面寒暄最多的主题还是AI，只是与以往不同的是，很多朋友眼中没有了兴奋与激情，却多了一份犹豫。

是的，已经很少有人谈论大模型幻觉，按说AI的能力已经得到了相当的认可，为什么好像听到的落地案例没有很多呢。

AI落地难，因为AI不能只是一个玩具，我还会这样回复。

去年，蓝莺AI早早完成了智能体Agent平台的建设，也接触了不少客户。从年底开始，我们便在提醒客户，接入AI只是第一步，一定要[跨越智能应用的鸿沟](https://docs.lanyingim.com/articles/Build-Your-AI-Application-Quickly-GPT-Mention.html)。

这条鸿沟，就是能否将AI嵌入真实的业务中，产生价值。而跨越，不会是加个Copilot助手那么简单。

如果我们对应用的要求是企业级的，那么对AI的要求就必须也是企业级的。

这便是我们今天聊的主题，如何打造自己的企业级AI产品。

## 看看苹果智能（Apple Intelligence）

上月，在苹果全球开发者大会WWDC上，苹果交出了自己在新智能时代的答卷。[苹果智能（Apple Intelligence）发布](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650921293&idx=1&sn=7dd34e37b5285f85000ddc98c17949b5&scene=21#wechat_redirect)，一个全新接入生成式AI的个性化智能系统。

Andrej Karpathy总结了苹果智能的几个重点：

> 1.  多模态输入 / 输出。苹果启用了文本 / 音频 / 图像 / 视频读写功能。
> 2.  Agentic。苹果允许操作系统和应用程序的所有部分通过「函数调用」进行互操作，内核进程 LLM 可根据用户查询安排和协调它们之间的工作。
> 3.  无摩擦。苹果以一种高度流畅、快速、always on 和上下文的方式全面集成这些功能。无需四处复制粘贴信息、提示工程等。还对用户界面进行了相应调整。
> 4.  主动性。苹果没有根据提示执行任务，而是预测提示、提出建议并主动执行任务。
> 5.  分级授权。尽可能多地将智能移动到设备上（苹果芯片非常有帮助且适合），但允许将工作可选地派发到云端。
> 6.  模块化。允许操作系统访问并支持整个不断增长的 LLM 生态系统（例如 ChatGPT 公告）。
> 7.  隐私。

关于Karpathy你要知道的是，他不仅是个普及AI的硬核网红，职业履历也很关键。他曾是OpenAI的创始成员，也曾是特斯拉AI的负责人。他对于AI和应用的思考，都很深入且具有启发性。

回到刚才的总结，我们在之前已经分别针对性的给过答案：

1. 多模态输入输出。可以结合[小蓝AI的多模态设计\[1\]](https://docs.lanyingim.com/articles/Lanying-AI-Please-Enable-Voice-Communication.html)。
2. Agentic。在我们构建完蓝莺Agent平台时，就提出要做[智能插件\[2\]](https://docs.lanyingim.com/articles/AI-Powered-Applications-Plugins-App-Store-and-AI-Agents.html)，[用AI驱动业务\[3\]](https://docs.lanyingim.com/articles/Enable-AI-integration-for-businesses-with-APIs.html)。
3. 主动性。AI不只是会变懒，它本身的设计就是响应式的，要让其比用户更主动，[做好销售而不是客服\[4\]](https://docs.lanyingim.com/articles/Implement-Sales-AI-with-Large-Language-Model.html)，就不能忽略这一点。
4. 模块化。你需要[一个设计成熟的AI SDK\[5\]](https://docs.lanyingim.com/articles/Build-Your-AI-Application-Quickly-GPT-Mention.html)，而不是深度耦合的一段段代码。

剩下的3和5，也就是无摩擦和分级授权，则是我们今天讨论的主题，企业内AI落地的两大挑战。

## 企业级AI的两大挑战

### 一、摩擦

很多人从ChatGPT开始认识大语言模型LLM，会自然觉得其是以对话方式开始工作的。这容易理解，但我们必须意识到，LLM AI让人机对话变得简单，但是对话并不是它最强的地方，与机器的交互才是。

比起人类的自然语言，它当然更熟悉编程语言，甚至机器语言。所以如果一个任务，当你对其组织的自然语言回复满意时，大概率直接完成这个任务也是可以的。

很多业务系统的AI改造，是给系统增加了一个AI聊天助手，然后需要操作用户来对AI回复的内容进行理解或加工，最后将其添回过去的操作界面。

**这就是摩擦。**

这样的设计，从用户体验角度来看是远远不够的，很难吸引用户吸引用户迁移到新系统上。

当然这方面值得学的例子也很多，除了Github Copilot等编程插件，OpenAI的GPT Builder本身，也是一个不错的例子。

### 二、权限

当我们看到AI的能力是，我们重点关注的是AI能做什么，但在落地时，AI能做什么，跟使用AI的人能做什么之间还有一个关系，那就是权限。

当我们说AI可以做企业运营助手，给它加上企业知识库和内部系统调用接口，就可以进行对话操作了。但是，一个强大的能调用内部所有系统的AI并不是每个人都可以用的。

就像不能把自毁开关放到小孩子手中一样，权限控制的首要目标是不给不需要的人多余的权限。

在使用企业知识库的时候，你不能给研发部门销售运营的知识库，也不能给行政部门开发文档的知识库。

更进一步，同一部门的AI都开通了人力资源服务接口，但主管可以查询部门所有人员的人力资源信息，员工个人只能查询自己的休假信息。

这是AI企业落地前必须解决的问题。

关于权限控制，之前给很多企业开发者分享过，这里做个简单的总结：

#### 1\. 分离企业知识库

不同业务场景，对AI的使用是不一样的，要求的知识也不一样。就像一个企业的各个部门，你可以在创建知识库的时候进行规划，让不同场景下的AI加载不同知识即可。

这也是AI领域知识隔离的设计点，是[MultiAgent设计\[6\]](https://docs.lanyingim.com/articles/2024-be-kind-to-programmers-give-them-an-AI-assistant-first.html)的基础。

#### 2\. 智能插件调用权限控制

在智能插件的实现里，AI通过函数调用（FunctionCall）来与外部系统交互有两步，第一步从自然语言的交互中抽取调用数据JSON，由AI完成，第二步将上述调用转化为实际的API调用，由蓝莺AI框架完成。

在第二步中，我们增加了内置参数，就是调用者的蓝莺IM用户ID。这个用户ID是前端对话者的蓝莺IM用户映射，根据这个用户，就可以将权限控制粒度做到最细，满足最复杂的控制需求。

如图中黄线所示：

![蓝莺AI权限控制](../../assets/articles/autogen-f4495098d976087ee335687e78c7989755ed4719d0648ac53058ea34bf3a8378.webp)

#### 3\. 借助外部权限

前面2的方式，适合新系统，但如果遇到复杂的系统，改造工作量是巨大的。

因此借助于蓝莺IM的自定义协议设计，我们将函数调用第二步里的API调用通过指令下发到客户端，这样对接后，可以利用对话客户原有的权限，从用户界面直接发起请求，跟操作者自己操作一样。见上图红线所示。

以上，都是我们在AI落地过程中的实践，也是对客户提问的解答，如果你有类似的问题或者经验分享，欢迎一起来讨论，这会对我们打造蓝莺企业级AI很有帮助。

关于企业内AI落地的更多内容，也欢迎添加「小蓝会聊天」微信进群：

![扫码添加小蓝会聊天](../../assets/articles/autogen-678480e75c7fcdbf6ec3492f1b2f9386e73af14e551ee9fa2baa98b93db02dcb.webp)

## 本期重要产品更新 🚀🚀🚀

### 1\. 必应搜索 BingSearch

蓝莺AI增加BingSearch插件，可以在 “AI智能/智能插件/创建导入插件/公共插件” 这里导入Bing搜索插件。

将插件绑定到Chatbot上，就可以调用[机器人同步API\[7\]](https://docs.lanyingim.com/reference/server-api/ai.html#put__ai_message_send)来获取机器人回复。

### 2\. 蓝莺GrowAI内测 ‼️

GrowAI，一个使用AI为企业构建Wiki或文档网站的工具，是蓝莺Agent平台的新服务，也是我们认为企业级AI落地的典型产品案例。

产品正在内测中，继续有限开放征集使用者，要求：

1.  有线上产品，希望做流量/SEO，Growth Hacking；
2.  技术产品，企业服务/2B SaaS优先；
    

内测期间除了忍受稍显粗糙的产品设计外，你还会获得专属的AI支持群，以及代金券补贴，以及产品上线后的折扣优惠。

最重要的，当然要在AI和流量的红利期，实现自己的业务增长，对吧？！😝😝😝

## 关于蓝莺IM

**蓝莺IM是新一代智能聊天云服务。**

集成蓝莺ChatAI SDK，同时拥有Chat和AI两大功能，接入大模型AI、使用企业知识库以及更多AI服务。

当前已支持ChatGPT（包括OpenAI和Microsoft Azure)、Anthropic Claude、Minimax、百度文心一言、智谱AI。

我们会持续分享关于智能聊天ChatAI、大模型技术进展、AI Agent设计等方面的内容，也会分享典型AI应用案例，欢迎关注：

![打造新一代智能聊天APP，使用蓝莺IM SDK！](../../assets/articles/autogen-1fdbd901f4a0c5b667df0e25fda7b53203aa868bb4da0962845b112f26e2d5b5.webp)

## 参考资料

1. [小蓝AI的多模态设计](https://docs.lanyingim.com/articles/Lanying-AI-Please-Enable-Voice-Communication.html)
2. [要做智能插件](https://docs.lanyingim.com/articles/AI-Powered-Applications-Plugins-App-Store-and-AI-Agents.html)
3. [用AI驱动业务](https://docs.lanyingim.com/articles/Enable-AI-integration-for-businesses-with-APIs.html)
4. [做好销售而不是客服](https://docs.lanyingim.com/articles/Implement-Sales-AI-with-Large-Language-Model.html)
5. [一个设计成熟的AI SDK](https://docs.lanyingim.com/articles/Build-Your-AI-Application-Quickly-GPT-Mention.html)
6. [MultiAgent设计](https://docs.lanyingim.com/articles/2024-be-kind-to-programmers-give-them-an-AI-assistant-first.html)
7. [机器人同步API](https://docs.lanyingim.com/reference/server-api/ai.html#put__ai_message_send)
