# 【美信拓扑开源】IM SDK Web版开源

原创 一乐 美信拓扑 _2021-08-13 19:15_

> 这是一份来自美信拓扑的七夕礼物，节日快乐！O(∩\_∩)O哈哈\~
>
> **截止到 2021.08.13，美信拓扑开源代码已达 163277 行。**

我们一直在认真的开源，因为我们知道，把代码开放简单，但做一个可靠让人喜欢的库就并没有那么容易。也因此即使我们花了很多精力在整理代码，只不过在开放的那一刻，还是会有一丝不好意思。

上月 PingCAP DevCon 的时候，刘奇分享了一个观点打动了我。他说开源连接的是人，是社区里那些志同道合的开发者。

什么是志同道合？就是你在做 IM SDK，他们也感兴趣；你想做专业的更好的服务，他们也这样想。

通过把这样分散在各处的力量通过项目集合起来，一起合作，创造更好的技术与服务，才是开源值得追求的地方。

我大受震撼，但也听懂了。

是的，一个好的开源项目，自己要下功夫，也要学会发挥社区的力量。

所以我们不只是会继续开源，还会将系统设计、协议等方面的材料公开出来，欢迎感兴趣的朋友持续关注。

![图片](../../.gitbook/assets/articles/autogen-86648f536f547fb95b7eebc3087e71653b7333ce945666222af6b2b9bdc1a111.webp)

## 美信拓扑开源计划（MTOS）

之前已经将 IM SDK 的安卓原生库和 iOS 原生库都开放了，这次开源的是 IM SDK Web 版，主要涉及两个库：

*   floo-web

    给 PC Web 使用的 IM SDK Web 版，使用了 socket.io 作为传输层，同时也是美信拓扑IM PC 版的基础，后者通过 Electron 封装的是这个版本。

    [https://github.com/maxim-top/floo-web](https://github.com/maxim-top/floo-web)
*   floo-uniapp

    给 H5 或小程序使用的 IM SDK Uniapp 版，使用 Uniapp 的 socket 作为传输层，完全兼容微信的传输层。

    [https://github.com/maxim-top/floo-uniapp](https://github.com/maxim-top/floo-uniapp)

经过一年多时间的迭代，以上两个库的协议解析层已经完成同步，也就是从 API 和事件处理的角度是完全一致的。这也是为什么我们会跟开发者说参考美信拓扑 IM DemoApp 使用 API 可以任意参考网页端或者小程序端的原因。

当前美信拓扑开源代码累计 163277 行，计划完成进度 42%。完整计划如下：

![图片](../../.gitbook/assets/articles/autogen-5fd0ab991b1f0bd2f6079c07ad463678352e2ee272431522d524173dd0438bde.webp)

希望你能喜欢这份七夕礼物，节日快乐！O(∩\_∩)O哈哈\~

### ✨为什么叫 Floo？✨

熟悉的朋友早就知道，美信拓扑的 IM SDK 别名 floo，因为《哈利波特》里是通过在火炉里撒飞路粉（floo powder）瞬移的。我们希望通过努力制造这样的粉末，为有（xie）魔（dai）法（ma）的你提供一条便捷的通讯传输链路。

是的，也因此我们的服务端别名是火炉（fireplace）。

### ✨关于美信拓扑✨

**美信拓扑**，一家很酷的技术公司，他们研发的一键启用多云架构的即时通讯云服务，具有超强的伸缩能力，可以支撑从亿级用户千万并发的公有云服务，到一台主机十分钟安装完成的私有云。目前各种组件正在陆续开源。

**特别提示**

继续关注「美信拓扑」，了解一键启用多云架构的即时通讯云服务。

记得 Fork & Star 哦✨✨✨✨✨✨✨✨✨

![图片](../../.gitbook/assets/articles/autogen-9c1da9e4a9e37fe718184c6ceeb84a3401afabccc3269ff9a5bd7ef8b087462e.webp)