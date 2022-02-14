# 用 SWIG 生成 Java 代码（IM SDK）

原创 一乐 美信拓扑 _2020-05-26 18:23_

> 美信拓扑技术分享系列 0x02：Floo-android 开源和高级 API 介绍
>
> 代码开源在 Github，你可以参照生成其他语言版本的 IM SDK。阅读本文你可以了解：
>
> 1. SWIG，一个联结 C/C++ 软件与其它各种高级编程语言的开发工具；
> 2. 一个在生产环境实际使用的 SWIG 案例；
> 3. 一个跨平台云服务 IM SDK的典型设计；
> 4. 即时通讯 IM 业务 与 API 设计；
>
> 关注「美信拓扑」微信公众号，第一时间阅读本系列后续文章，了解美信拓扑IM的协议、架构和源码。

作者 | 一乐

前几天在直播里介绍过的内部创新项目，代码正式开源了\[1]，喜欢玩的同学可以去 Github 看看（star）啦。

为了更好的让大家理解项目，本文会介绍 SWIG 和本工程代码，同时也会介绍项目背景，也即美信拓扑跨平台 IM SDK 的设计与实践。

## SWIG 是什么

![Photo by Marco Djallo on @unsplash](../../.gitbook/assets/articles/autogen-d616ae0b2710058ffe22ef723448515e7f1bfe8af5f04771cf6b348a2ee08786.webp)

SWIG 全称是 Simplified Wrapper and Interface Generator \[2]。这个名字相当直白，翻译过来就是简化的包装和接口生成器。官方介绍是一个联结 C/C++ 软件与其它各种高级编程语言的开发工具。其实主要做了一件事，就是把 C/C++ 写的软件库封装成其他高级编程语言可以调用的本地库。

现在它支持的高级编程语言不仅包括 Javascript，Perl，PHP，Python，Tcl 以及 Ruby 这样的脚本语言，也支持非脚本语言如 C#，D，Golang，Java（包括Android），Lua，OCaml，Octave，Scilab 以及 R 语言。

这正是美信拓扑的 IM SDK 需要的，我们底层通讯层使用 C++ 实现，然后再在上层进行本地化封装（为什么这么做，后面讲）。

开源这个库的目的，一方面是为了介绍 SWIG 框架，因为自动生成代码，虽然大多数人并不陌生，RPC 框架如 Thrift 可以自动生成客户端服务器代码，序列化库如 protobuf 可以自动生成序列化反序列化的类，进行面向对象编程的可以借助 UML 生成类框架，数据库工具可以自动生成建库 SQL 脚本等等。但到了相对复杂的业务系统，用的就少多了，毕竟手写出来的最踏实（即使会 Bug 很多）。

另一方面，我们用 SWIG 生成了供安卓使用的本地 Java 库，但是难免遇到有开发者需要其他语言的时候，因此我们将工程模板也开源出来，如果有朋友想玩的话，可以直接改造 SWIG 脚本生成需要的其他语言库。

如果你做了，请第一时间告诉我们，不管是任何时候。有神秘礼物等着你哦 :)

看代码前，我们先介绍下美信拓扑这个跨平台的 IM SDK。

## 跨平台 IM SDK 架构

如前所述，美信拓扑IM SDK（研发代号 Floo ）底层使用 C++ 实现，各平台（Android、iOS、Linux等）在此基础上再行封装， 完成本地库的开发，以达到多平台复用的目的，并保持跨平台协议实现的一致性。如下图所示：

![图片](../../.gitbook/assets/articles/autogen-50c4b239aa07b7781371f1dc7320b4bf03ad5434d38abeeb357c8eb919d6e659.webp)

左边蓝色是本地库，包括Android、iOS、Linux等，右边黄色是 Web，包括浏览器、小程序、H5等。所有库的分层基本一致，从下往上依次是

1. 系统层，包括操作系统和系统库；
2. 协议层，实现了 XSync 协议，美信拓扑自定义的基于同步的IM协议；
3. 转接层，将 C++ 库转接适配成各平台可以调用的原生应用库，本次开源的 floo-android 即属于此层；
4. UI层，提取 UI Kit 等需要；
5. 应用层，实现 App 业务功能；

这样分层的好处在于协议之需要实现一次，即减少了工作量，又减少了潜在的Bug。在一个优秀的 IM 系统实现里，可靠高效的协议设计，与灵活柔性的客户端 SDK和高性能的服务端，是同等重要的。

有朋友可能好奇 Floo 是什么意思？研发代号 Floo 来源于哈利波特里的飞路粉\[3]，根据介绍它是

> 一种亮晶晶的银色粉末，在男女巫师用飞路网旅行时使用。飞路网与绝大多数巫师家庭和魔法建筑相连接。
>
> 使用时人们将一把粉末撒入已连接飞路网的壁炉，走进火焰，并口齿清晰、大声地说出目的地，则能确保顺利到达目的地。
>
> https://harrypotter.fandom.com/zh/wiki/飞路粉

这也是我们服务端叫 Fireplace 的原因，如果你前几天跟我们一起玩过树莓派\[4]\[5]，在安装后的服务里会发现它。

## 如何掌握 IM API

![Photo by @JamieDotSt on @unsplash](../../.gitbook/assets/articles/autogen-5a1ed68575ebd20a7a616e396eecc9b6b59e4704496429c5570987f8c0b1e86a.webp)

在我们说起一个 IM SDK 的时候，经常有一种声音出现，他们说，IM嘛，不就一个聊天，能发消息就行呗。

大多时候我只是笑笑，心情好的时候还会说你说的对。

但如果是好朋友，还会告诉他们，一个典型的 IM SDK，会有 40 余类几百个方法\[6]，因为要同时兼顾分层设计和灵活性，保证协议实现的质量，又要支持事件通知和自定义协议等确保业务逻辑的完整。

我会告诉他们，在移动网络这种长延迟不稳定链路下，要保证消息的有序投递，又要保证软实时且可靠，XMPP 协议有太多的限制，你需要全新设计和优化的 IM 协议。这也是现在真正高质量 IM 的基础。

在这些的基础上，才是跨平台实现要考虑的问题，独立的协议解析层，插件式的底层系统库和上层应用库实现。底层系统库容易理解，就是网络调用、文件读写以及数据库操作；上层应用库主要是 HTTP 库，各平台并不一样，因此协议库的 HTTP 实现，需要通过与各端上层协调来实现。

当然这些是设计实现一个好的云服务 IM SDK 才需考虑，如果只是使用，自然可以找简单的方式。

从业务上看，IM 有三条主线，消息，用户和关系。

消息的核心是聊天，这包括单聊与群聊，所有聊天都会有发送与接收，发送涉及同步异步以及失败重试，接收涉及回调监听以及未读数计算。内容上，除了文本之外，还会支持图片、语音、附件等富媒体，这些会进一步转化为与存储系统的交互，上传和下载。

用户方面，首先是个人身份，用户 ID 设计，登陆鉴权；然后是信息，头像、昵称以及第三方账号身份打通。

关系有三种，好友、群组和黑名单。好友需要考虑的是好友列表、单向/双向关系以及陌生人的消息控制；群组则是进群、退群、成员管理，以及群组设置；然后在此之上，有好友黑名单，群组黑名单。

沿着这三条主线，各种功能在相关类中依次展开，或作为方法，或作为变量，或作为组合（先调用后监听）分布在类库的各个角落。

掌握了这三条主线，再多的类也不怕啦。

也因此，介绍类库时，我们首先会提四个 Service 类，他们是 BMXUserService、BMXChatService、BMXRosterService 和 BMXGroupService。

不过在完整介绍类库之前，我们还有最后一个问题要说明，那就是同步和异步。

## 同步 vs 异步

如前所述，用 SWIG 生成的 Java 代码，通过 JNI 方式调用底层 C++ 类库，因此大部分接口均为同步，这便是 Floo-android 低级 API 的主体。 代码生成和转换的过程中，相关数据结构得以直接映射到底层类库，减少了内存拷贝，因此其性能接近于直接调用底层库。

同时，又考虑到开发者集成方便，我们也基于此类重新封装了高级 API，使用了更为友好的数据结构，并完成了异步机制封装。

也因此，整个类库（floo-android）分为三部分：

```
                                                 +---> BMXUserService
                                                 |
                              +---------------+  +---> BMXChatService
                              |               |  |
                          +---+ 低级 API: L/S  +------> BMXRosterService
                          |   |               |  |
                          |   +---------------+  +---> BMXGroupService
                          |
                          |                         +---> BMXUserManager
                          |   +---------------+     |
+----------------------+  |   |               |     +---> BMXChatManager
|                      |  +---+ 高级 API: H/A +-----+
| 美信拓扑 IM SDK: Floo +--+   |               |     +---> BMXRosterManager
|                      |  |   +---------------+     |
+----------------------+  |                         +---> BMXGroupManager
                          |
                          |                       +--->  BMXClient
                          |   +----------------+  |
                          |   |                |  +--->  BMXSDKConfig
                          +---+ Utility：工具类 +--+
                              |                |  +--->  BMXMessage
                              +----------------+  |
                                                  +--->  BMXConversation
                                                  |
                                                  +--->  BMXUserProfile
                                                  |
                                                  +--->  BMXGroup
                                                  |
                                                  +--->  BMXDevice
```

1\. 低级 API (low-level)

同步调用接口，类名以Service结尾，为方便理解，下文说明中用 L/S 表示，其中 L 表示 Low-level, S 表示 Sync。

主要有 BMXUserService、BMXChatService、BMXRosterService、BMXGroupService。

2\. 高级 API (high-level)

异步调用接口，类名以Manager结尾，为方便理解，下文用 H/A 表示，其中 H 表示 High-level, A 表示 Async。

主要有 BMXUserManager、BMXChatManager、BMXRosterManager、BMXGroupManager。

简单来讲，相关调用会在子线程执行具体操作（例如：搜索好友），当前线程会直接返回而不阻塞。具体操作的结果则通过回调函数通知调用方，后者可以在其中处理 UI 刷新等业务逻辑。

3\. 工具类 Utility

包括客户端实例化类 BMXClient 、配置类 BMXSDKConfig、消息类 BMXMessage、会话类 BMXConversation、用户身份类 BMXUserProfile、群类 BMXGroup、设备类 BMXDevice等。

我们这里不再赘述，如果需要参照可以阅读美信拓扑快速集成指南安卓版\[6]，或者查看详细类库文档\[7]，当然后者也是此次开源仓库自动生成的。

最后，让我们看看代码吧。

TIPS：如果你已阅读到这里，可以给自己点个赞啦。

## 代码

整个工程代码结构比较简单，IM API 相关的头文件和so文件已经放在工程里，而运行命令也只有关键的一行：

```
/usr/local/bin/swig -debug-classes -debug-module 4 -debug-typemap -c++ -java -package im.floo.floolib -outdir src/main/java/im/floo/floolib/ -o src/main/cpp/floo_wrap.cxx -Ifloo/include -Ifloo/src swig/floo.i
```

指定输出 Java 代码的包名是 im.floo.floolib，指定 floo 头文件的地址，剩下的就是 SWIG 定义文件了，他们都放在 ./swig/floo.i \[7] 里，下面是 49-126 行：

```
%include "std_shared_ptr.i"
%include "std_vector.i"
%include "std_string.i"
%shared_ptr(floo::BMXMessageConfig)
%shared_ptr(floo::BMXMessage)
%template(BMXMessageList) std::vector<std::shared_ptr<floo::BMXMessage>>;

typedef floo::BMXConversation::Type BMXConversationType;

%shared_ptr(floo::BMXConversation)
%template(BMXConversationList) std::vector<std::shared_ptr<floo::BMXConversation>>;

%shared_ptr(floo::BMXRosterItem)
%template(BMXRosterItemList) std::vector<std::shared_ptr<floo::BMXRosterItem>>;
%shared_ptr(floo::BMXDevice)
%template(BMXDeviceList) std::vector<std::shared_ptr<floo::BMXDevice>>;

%shared_ptr(floo::BMXImageAttachment)
%shared_ptr(floo::BMXLocationAttachment)
%shared_ptr(floo::BMXMessageAttachment)
%shared_ptr(floo::BMXNetworkListener)
%shared_ptr(floo::BMXClient)
%shared_ptr(floo::BMXBaseObject)
%shared_ptr(floo::BMXSDKConfig)
%shared_ptr(floo::BMXFileAttachment)
%shared_ptr(floo::BMXGroup)
%shared_ptr(floo::BMXGroup::Member)
%shared_ptr(floo::BMXGroup::BannedMember)
%shared_ptr(floo::BMXGroup::Announcement)
%shared_ptr(floo::BMXGroup::SharedFile)
%shared_ptr(floo::BMXRosterService::Application)
%shared_ptr(floo::BMXGroup::Application)
%shared_ptr(floo::BMXGroup::Invitation)
%shared_ptr(floo::BMXUserProfile)
%shared_ptr(floo::UserProfileImpl)
%shared_ptr(floo::BMXVoiceAttachment)
%shared_ptr(floo::BMXVideoAttachment)
%shared_ptr(floo::BMXResultPage<floo::BMXMessage>)

%template(BMXGroupList) std::vector<std::shared_ptr<floo::BMXGroup>>;
%template(BMXGroupMemberList) std::vector<std::shared_ptr<floo::BMXGroup::Member>>;
%template(BMXGroupBannedMemberList) std::vector<std::shared_ptr<floo::BMXGroup::BannedMember>>;
%template(BMXGroupSharedFileList) std::vector<std::shared_ptr<floo::BMXGroup::SharedFile>>;
%template(BMXGroupAnnouncementList) std::vector<std::shared_ptr<floo::BMXGroup::Announcement>>;
%template(BMXRosterServiceApplicationList) std::vector<std::shared_ptr<floo::BMXRosterService::Application>>;
%template(BMXGroupApplicationList) std::vector<std::shared_ptr<floo::BMXGroup::Application>>;
%template(BMXGroupInvitationList) std::vector<std::shared_ptr<floo::BMXGroup::Invitation>>;

%template(ListOfLongLong) std::vector<long long>;

%include "bmx_error.h"
%include "bmx_defines.h"
%include "bmx_device.h"
%include "bmx_base_object.h"
%include "bmx_message_attachment.h"
%include "bmx_message_config.h"
%include "bmx_message.h"
%include "bmx_conversation.h"
%include "bmx_sdk_config.h"
%include "bmx_network_listener.h"
%include "bmx_chat_service.h"
%include "bmx_chat_service_listener.h"
%include "bmx_client.h"
%include "bmx_file_attachment.h"
%exception floo::BMXFileAttachment::dynamic_cast(floo::BMXMessageAttachment *attachment) {
  $action
    if (!result) {
      jclass excep = jenv->FindClass("java/lang/ClassCastException");
      if (excep) {
        jenv->ThrowNew(excep, "dynamic_cast exception");
      }
    }
}
%extend floo::BMXFileAttachment {
  static floo::BMXFileAttachment *dynamic_cast(floo::BMXMessageAttachment *attachment) {
    return dynamic_cast<floo::BMXFileAttachment *>(attachment);
  }
};
```

详细代码可以去仓库里查看，这里只提几点，希望对你后续使用有所帮助：

1\. 标准库有专门头文件，如果你用了它们，也需要首先关联它们的定义文件

```
%include "std_shared_ptr.i"
```

2\. 继承可以用 % entend 关键字

```
%extend floo::BMXFileAttachment {
  static floo::BMXFileAttachment *dynamic_cast(floo::BMXMessageAttachment *attachment) {
    return dynamic_cast<floo::BMXFileAttachment *>(attachment);
  }
};
```

3\. 最后一点，也是最重要的一点是：顺序很重要，顺序很重要，顺序很重要！

因为代码生成的过程是单次遍历，所以在生成当前代码的时候，如果用到的类没有被定义，就会重新级联生成一个新的辅助类，这样你会得到很多命名超长的类，很难看很难用。

总的来说，虽然要学习一个新的框架，还要定义一些配置，但问题都搞定后，还真挺香的，哈哈。

今天的分享就到这里，欢迎试玩，也欢迎继续关注「美信拓扑」微信公众号，第一时间阅读本系列后续文章，了解美信拓扑IM的协议、架构和源码。

![图片](../../.gitbook/assets/articles/autogen-9c1da9e4a9e37fe718184c6ceeb84a3401afabccc3269ff9a5bd7ef8b087462e.webp)

**美信拓扑**是一家很酷的技术公司。美信拓扑 IM 是第一个多云架构的即时通讯云服务，具有超强的伸缩能力，可以支撑从亿级用户千万并发的公有云服务，到一台主机十分钟安装完成的私有云。目前各种组件正在陆续开源。

## **引用**

1、美信拓扑IM SDK 安卓版（Floo-Android）Github地址\
https://github.com/maxim-top/floo-android\
2、SWIG：简化的包装和接口生成器\
http://www.swig.org/\
3、飞路粉（floo powder）\
https://harrypotter.fandom.com/zh/wiki/飞路粉\
4、[十分钟安装一套即时通讯 IM 私有云](install-an-instant-messaging-im-private-cloud-in-ten-minutes.md)\
5、[树莓派中的 IM 私有云支持多少并发？](how-much-concurrency-is-supported-by-im-private-cloud-in-raspberry-pi.md)\
6、Floo-android reference 类库文档\
https://www.maximtop.com/docs/android/\
7、Floo-android Github 仓库里的 floo.i\
https://github.com/maxim-top/floo-android/blob/master/app/swig/floo.i\
8、十分钟安装的即时通讯私有云 美信拓扑\
https://www.maximtop.com

## **特别提示**

美信拓扑海外可用区「印度区」正在内测，如果有印度出海的公司或业务可以官网直接申请。

美信拓扑已经是阿里云和AWS的技术合作伙伴，借助于先进的多云架构，美信拓扑IM的「专有云服务」可以在你业务需要的任何地区进行部署实施，为您和您的用户提供更好的聊天体验。

海外专有云定价与国内专有云定价方式一致，差价仅来源于服务资源差异，且可以与客户共管阿里云或AWS账号。
