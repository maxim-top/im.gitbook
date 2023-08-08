# 如何为开源仓库文档添加示例代码

大海 蓝莺IM _2022-09-27 20:27_

> 开源，把代码公开出来就够了吗？不，还是要有文档。
>
> 蓝莺IM新文档中心上线，不仅增加了多语言支持，文档中的示例直接关联了开源仓库的代码。
>
> 为Gitbook文档添加示例代码的功能就是通过这个插件（lanying-code-snippet）实现的，如果你的项目文档是通过 Gitbook 创建，可以玩玩。
>
> 目前，蓝莺IM国际化基本完成，官网、文档中心、控制台和DemoAPP（安卓\&iOS）均已增加多语言支持，欢迎观摩👏🏻

作者 | 大海

编辑 | 小蓝会聊天

![](../../../\_book/assets/articles/autogen-f76e48cd9591e13554f7ee7a488b311f06e397dcf8f8587af14ce34686ec9693.jpeg)

“源码之前，了无秘密。”

跟团队讨论起开源仓库和文档，当我说出这句话的时候，原本期待的赞同并没有出现，而是一阵沉默。我忽然好像明白了什么。

没记错的话，这句话是侯捷老师在《STL源码解析》里说的。最开始看到的时候，我还处在对 C++ 的热爱中，对《Effective C++》《More Effective C+++》爱不释手。你没猜错，后面后面这两本书也都是侯捷老师翻译的，Scott Meyers 所著。

现在说起来，那时候微软还通过 MFC 框架在 C++ 领域大杀特杀，一转眼十几年过去，前几天看到的新闻是 Azure CTO 开始呼吁停止使用 C/C++ 开发新项目而改用 Rust了。

那时候也流行折腾代码，但凡遇到一个项目，第一反应就是把源码下载下来，运行调试把玩一番。当然有一点也不得不提，就是很多开源项目的文档也不完全，阅读源码是了解一个项目最高效准确的方式。多种原因交织之下，遇到的问题很多也是靠通过源码分析来定位解决。实际上，互联网服务线上问题的解决，也是如此。

所以「源码之前，了无秘密」就是提醒我们，有了代码啥都不怕。

然而技术的发展就像大河东流，越宽的水面越流得缓慢，也越势不可挡。就像我们之前在《[过去的十五年，我们怎样做 IM？](../Industry-development/how-we-build-an-instant-messging-system-in-the-past-fifteen-years.md)》里所说，软件开发已经进入了云服务时代，现在流行的是使用组件和 API 服务，自然代码就看得少了，文档也变得越来越重要。

言归正传。

在蓝莺IM DemoAPP刚刚开源的一段时间，我们的文档并不完善。这一方面是由于产品仍在快速迭代，文档的更新维护会比源码慢半拍，另一方面也是因为我们内心仍然会想，应用层的代码很简单并且已经开源，开发者直接使用开源仓库根据 Demo 操作即可找到示例，比文档要方便多了。

事实并非完全如此，虽然最终开发者仍会运行起 Demo 工程，但一个顺手的文档仍然是开始接触项目和解决问题时候的有力支持。

这便是我们开发这个Gitbook插件的主要原因。通过插件的方式，可以在 Gitbook 文档中的 API 说明里需要示例的地方，直接显示对应开源仓库中的使用代码和链接。

下文是详细介绍，如果暂时用不到，可以进入 Github 先 Fork\&Star 收藏：

LCS（Lanying Code Snippet）：

https://github.com/maxim-top/gitbook-plugin-lanying-code-snippet

## Lanying Code Snippet 介绍

Gitbook 可以将 markdown 文档转换成 html 页面，LCS 是 Gitbook 插件，在转换的过程中根据标记来补充页面内容。

也就是说，只要在 markdown 文件中插入带有仓库名称、类名和函数名的标签，LCS 插件据此来搜索 Github 仓库，在标签位置插入调用这个函数的代码块和github 链接。

LCS 搜索代码时使用的是 joern，一个可以分析代码和二进制的开源工具。通过预先分析源码仓库生成代码数据库，方便在读到文档标签时进行快速搜索。目前已支持C/C++/Java/Javascript/Objective-C 语言。

例如使用标签

```
 {% lanying_code_snippet 
   repo="lanying-im-web", 
   class="userManage", 
   function="asyncRegister" %}</div>
```

，可以生成下面的代码块： ![](../../../\_book/assets/articles/autogen-13ee65a46ac7ad686e7afb0c16fade0513efd26a387a8feadaf5aaba998d414c.png)

基本步骤只需四步：

1. 要使用 Gitbook 来管理文档，需要安装 Gitbook；
2. 使用自动文档生成工具，例如 doxygen、AppleDoc 等，从代码注释中生成 markdown（建议）；
3. 配置 Lanying Code Snippet 插件；
4. 运行 Gitbook 生成工具，生成最终文档；

详细安装过程如下：

## 1. 安装 Gitbook

1.1 安装 Node.js，推荐版本v16.17.0, 在此页面下载对应系统的安装包；

1.2 安装 Gitbook：

```
    npm install gitbook-cli -g
```

1.3 更新依赖库graceful-fs的版本：

```
cd `npm root -g`/gitbook-cli/node_modules/npm/node_modules
npm install graceful-fs@4.2.0 --save
```

## 2. 安装插件依赖

2.1 安装 JDK 11：

```
curl -s "https://get.sdkman.io" | bash && \
source "/Users/zoujinhai/.sdkman/bin/sdkman-init.sh" && \
sdk install java 11.0.16-amzn
```

2.2 安装 joern：

```
curl -L "https://github.com/joernio/joern/releases/latest/download/joern-install.sh" -o joern-install.sh && \
chmod u+x joern-install.sh && ./joern-install.sh
```

2.3 安装xcode 11 （要引用的代码仓库使用 Objective-C 语言时需要安装）

点击[此链接](https://download.developer.apple.com/Developer\_Tools/Xcode\_11.7/Xcode\_11.7.xip)下载Xcode 11， 并解压，然后将得到的xcode.app文件夹复制到 /Applications 目录：

2.4 安装 llvm2cpg （要引用的代码仓库使用 Objective-C 语言时需要安装）

点击[llvm2cpg](https://github.com/ShiftLeftSecurity/llvm2cpg)，下载到可执行目录，并增加可执行权限：

2.5 在Gitbook book.json里增加如下插件, 然后运行 `gitbook install`。 第一次可能会失败，如果失败需要再执行一次 `gitbook install`。

```
{ "plugins": ["lanying-code-snippet"] }
```

## 3. 配置 LCS

配置格式为：

```
{
    "plugins": [
        "lanying-code-snippet"
    ],
    "pluginsConfig": {
        "lanying-code-snippet": {
            "showLink": true,
            "reindent": true,
            "maxLine": 20,
            "maxSnippetCount": 10,
            "repositories": [
                {
                    "name":"lanying-im-web",
                    "url":"https://github.com/maxim-top/lanying-im-web.git",
                    "branch":"master"
                },
                {
                    "name":"lanying-im-android",
                    "url":"https://github.com/maxim-top/lanying-im-android.git",
                    "branch":"master",
                    "cacheDir": "../cache/lanying-im-android"
                }
            ]
        }
    }
}
```

配置说明：

* showLink=true 是否在代码下显示github链接，默认为true
* reindent=true 是否调整代码缩进. 默认为true
* maxLine=20 每个代码片段的最大行数， 默认为20
* maxSnippetCount=10 最多显示多少个代码片段， 默认为10
* repositories 代码仓库信息
  * repositories\[\*].url 仓库地址
  * repositories\[\*].branch 仓库分支
  * repositories\[\*].name 仓库名称，用于在标签里引用仓库
  * repositories\[\*].cacheDir github仓库的本地缓存路径， 如果不设置，会使用/tmp目录下的随机目录。如果使用Objective-C语言，cacheDir必须设置。

## 4. 生成文档

在 markdown 里插入下面格式的标签，然后使用

```
    gitbook build
```

或

```
    gitbook serve
```

就会将标签替换为相应的代码块：

```
{% lanying_code_snippet 
  repo="lanying-im-web",
  class="userManage",
  function="asyncRegister" %}

</div>
```

其中，repo 是仓库名称，需要与配置里的仓库名称一样。class是类名， function是函数名。

最后展现的效果，就是现在的[蓝莺IM文档中心](https://docs.lanyingim.com)，好好玩吧 🎉🎉🎉

## 蓝莺IM开源计划（LIMOS）

截至 2021.08，蓝莺IM开源计划 LIMOS 已开源代码 163277 行。

以蓝莺IM开源项目为基础，我们也在打造一个专业的即时通讯技术社区，这便是我们的「蓝朋友计划」。

此计划将会邀请社区技术专家一起，共同分享关于即时通讯（IM）技术相关内容，欢迎持续关注，也欢迎自荐或推荐。

![](../../../\_book/assets/articles/autogen-cc84b94b1144d2b03fb6b83cad49f5f8f8bdcf42914d2ce8525459134b3c3c5e.png)
