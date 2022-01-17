# C++ SDK (floo) 快速集成指南

## SDK 整体架构

SDK 架构说明

* BMXClient:SDK功能聚合类，包含了所有的service类、实现了网络事件监听接口。
* BMXChatService:消息发送、消息历史获取、会话列表
* BMXUserService:注册账号、登入、登出、我的设置
* BMXRosterService:好友列表、黑名单、
* BMXGroupService:群管理（创建、解散、查找、设置、成员管理、邀请、申请、接受、拒绝）
* BMXChatServiceListener:消息到达事件、消息发送结果事件监听
* BMXGroupServiceListener:群事件监听
* BMXUserServiceListener:用户事件监听
* BMXRosterServiceListener:好友事件监听
* BMXNetworkListener:网络事件监听接口，由BMXClient实现
* BMXConversation:会话
* BMXMessage:消息
* BMXGroup:群
* BMXRosterItem花名册项（好友、陌生人、黑名单、前好友）
* BMXUserProfile:用户信息

主要类之间的关系如下：

```
>BMXClient
>|----BMXNetworkListener
>|----BMXChatService
>    |----BMXChatServiceListener
>    |----BMXConversation
>    |----BMXMessage
>|----BMXUserService
>    |----BMXUserServiceListener
>    |----BMXUserProfile
>|----BMXRosterService
>    |----BMXRosterServiceListener
>    |----BMXRosterItem
>|----BMXGroupService
>    |----BMXGroupServiceListener
>    |----BMXGroup
```

## SDK集成

1. SDK文件说明
2. 添加系统库依赖 您在工程中导入SDK之前，需要添加如下系统库的引用。

* libz 解压缩库
* libcrypto openssl加密库
* libsqlite3 sqlite3本地数据库
* lcurl libcurl网络库
* lcurses ncurses库，运行embedded版本demo需要使用

### 一、初始化，导入相关头文件

```
#include "bmx_client.h"
config = BMXSDKConfigPtr(new BMXSDKConfig(BMXClientType::macOS, "10", "./data", "./data", "2.0", "1234", "userAgent"));
config->setAppID("dxgeuidhhutk");
config->setDeviceUuid("b81f412e-fcb2-44fb-9f44-5e8e5b1e809e");
config->setConsoleOutput(false);
client = BMXClient::create(config);
```

### 二、注册用户

```
BMXUserProfilePtr profile;
BMXErrorCode errorCode = config->getUserService().signUpNewUser("maximtest1", "123456", "1", profile);
if (BMXErrorCode::NoError == errorCode) {
  std::cout << "signUpNewUser successs!" << std::endl;
} else {
  std::cout << "signUpNewUser failure!" << std::endl;
  std::cout << getErrorMessage(errorCode) << std::endl;
}
```

### 三、登录链接服务器

将您在上一步获取到的 账号密码，通过 BMXClient的单例，UserService类，传入 -signInById 方法，即可建立与服务器的连接。

提供两种登录模式：一种是普通手动登录，另一种是快速登录模式

```
BMXErrorCode errorCode = client->getUserService().signInByName("maximtest1", "1");
if (BMXErrorCode::NoError == errorCode) {
  std::cout << "signInByName successs!" << std::endl;
} else {
  std::cout << "signInByName failure!" << std::endl;
  std::cout << getErrorMessage(errorCode) << std::endl;
}

// 快速登录,不需要获取token
BMXErrorCode errorCode = client->getUserService().fastSignInByName("maximtest1", "1");
if (BMXErrorCode::NoError == errorCode) {
  std::cout << "signInByName successs!" << std::endl;
} else {
  std::cout << "signInByName failure!" << std::endl;
  std::cout << getErrorMessage(errorCode) << std::endl;
}
```

### 四、获取会话列表

通过 BMXClient的单例，ChatService类的getAllConversations 方法，获取所有会话列表。返回BMXConversationPtr对象的数组列表。

如果需要获取多设备同步的离线会话列表，需要在SDK初始化配置setLoadAllServerConversations属性值为true，默认只获取本地会话列表。

```
BMXConversationList list = client->getChatService().getAllConversations();
```

### 五、断开连接

在断开与MaxIM服务器的连接时，默认会停止接收消息。

```
BMXErrorCode errorCode = client->getChatService().signOut();
if (BMXErrorCode::NoError == errorCode) {
  std::cout << "signInByName successs!" << std::endl;
} else {
  std::cout << "signInByName failure!" << std::endl;
  std::cout << getErrorMessage(errorCode) << std::endl;
}
```

## 用户好友体系

* 添加好友

```
BMXErrorCode errorCode = client->getRosterService().apply(rosterId, "apply");
if (BMXErrorCode::NoError == errorCode) {
  std::cout << "apply successs!" << std::endl;
} else {
  std::cout << "apply failure!" << std::endl;
  std::cout << getErrorMessage(errorCode) << std::endl;
}
```

* 删除好友

```
BMXErrorCode errorCode = client->getRosterService().remove(rosterId);
if (BMXErrorCode::NoError == errorCode) {
  std::cout << "remove successs!" << std::endl;
} else {
  std::cout << "remove failure!" << std::endl;
  std::cout << getErrorMessage(errorCode) << std::endl;
}
```

* 同意添加好友

```
BMXErrorCode errorCode = client->getRosterService().accept(rosterId);
if (BMXErrorCode::NoError == errorCode) {
  std::cout << "accept successs!" << std::endl;
} else {
  std::cout << "accept failure!" << std::endl;
  std::cout << getErrorMessage(errorCode) << std::endl;
}
```

* 拒绝添加好友

```
BMXErrorCode errorCode = client->getRosterService().decline(rosterId, "reason");
if (BMXErrorCode::NoError == errorCode) {
  std::cout << "decline successs!" << std::endl;
} else {
  std::cout << "decline failure!" << std::endl;
  std::cout << getErrorMessage(errorCode) << std::endl;
}
```

* 获取好友列表

开发者可以通过参数forceRefresh,选择从服务器或者是从本地获取好友列表数据。 如果设置为NO, 当本地数为空，会自动从服务器去获取数据后返回结果。

```
std::vector<int64_t> list;
BMXErrorCode errorCode = client->getRosterService().get(list, true);
if (list.size() > 0) {
  cout << list[0] << endl;
}
```

## 基础功能

### 消息内容格式

* 文字
* 表情
* 语音片段
* 视频片段
* 图片
* 地理位置
* 自定义消息

### 单聊

单聊是最基本的聊天界面，提供文字、表情、语音片段、图片等多种输入内容，解决 App 内用户的沟通瓶颈。单聊的 BMXConversationType 是 BMXConversationSingle，toId 是单聊对象的 userId。

### 群聊

群聊是指附带角色和权限的用户集合内进行的内部广播方式的聊天功能，群组的 BMXConversationType 是 BMXConversationGroup，toId 是群组 Id。

* 创建群组

开发者可以注册监听，创建群组成功后, 收到相应回调通知,开发者可以进行一些UI处理。

```
BMXGroupPtr group;
BMXGroupService::CreateGroupOptions options("Test", "Test", "Test");
BMXErrorCode errorCode = client->getGroupService().create(options, group);
if (BMXErrorCode::NoError == errorCode) {
  std::cout << "create group successs!" << std::endl;
} else {
  std::cout << "create group failure!" << std::endl;
  std::cout << getErrorMessage(errorCode) << std::endl;
}
```

* 加入群组

```
BMXErrorCode errorCode = client->getGroupService().join(group, message);
```

* 退出群组

```
BMXErrorCode errorCode = client->getGroupService().leave(group);
```

* 解散群组

```
BMXErrorCode errorCode = client->getGroupService().destroy(group);
```

* 获取群成员列表

```
BMXGroupMemberResultPagePtr result;
std::string cursor = "";
int pageSize = 100;

do {
  errorCode = client->getGroupService().getMembers(group, result, cursor, pageSize);
  cursor = result->cursor();
  for (auto member : result->result()) {
    cout << member->mUid << endl;
  }
} while (cursor.size());
```

* 获取群组列表

```
@param list 群组id列表，传入空列表函数返回后从此处获取返回的群组id列表
@param forceRefresh 设置为true强制从服务器获取，本地获取失败的情况sdk会自动从服务器获取
BMXGroupList list;
bool forceRefresh = false;
BMXErrorCode errorCode = client->getGroupService().search(list, forceRefresh);
```

* 获取群组信息

```
BMXGroupPtr group;
errorCode = client->getGroupService().search(groupId, group, true);
```

## 消息发送

登录成功之后才能进行聊天操作。发消息时，单聊和群聊调用的是统一接口，区别只是要设置下 BMXConversationType。

### 构建消息实体

* 文本消息

```
/**
  * @param from 消息发送者Id
  * @param to 消息接收者Id
  * @param type 消息类型
  * @param conversationId 会话id
  * @param content 消息内容
  **/
  BMXMessagePtr msg = BMXMessage::createMessage(2272061685216, 2272061881760, (BMXMessage::MessageType)1, 2272061881760, "test");
```

* 图片消息

```
/**
  * @param path 本地路径
  * @param size 图片的大小，宽度和高度
  * @param displayName 展示名
  **/
BMXImageAttachmentPtr attachment(new BMXImageAttachment(path, size, displayName));
BMXMessagePtr msg = BMXMessage::createMessage(2272061685216, 2272061881760, (BMXMessage::MessageType)1, 2272061881760, attachment);
```

* 文件消息

```
BMXFileAttachmentPtr attachment(new BMXFileAttachment(path, displayName));
BMXMessagePtr msg = BMXMessage::createMessage(2272061685216, 2272061881760, (BMXMessage::MessageType)1, 2272061881760, attachment);
```

* 位置消息

```
BMXLocationAttachmentPtr attachment(new BMXLocationAttachment(latitude, longitude, address));
BMXMessagePtr msg = BMXMessage::createMessage(2272061685216, 2272061881760, (BMXMessage::MessageType)1, 2272061881760, attachment);
```

* 语音消息

```
BMXVoiceAttachmentPtr attachment(new BMXVoiceAttachmentPtr(path, duration, displayName));
BMXMessagePtr msg = BMXMessage::createMessage(2272061685216, 2272061881760, (BMXMessage::MessageType)1, 2272061881760, attachment);
```

* 视频消息

```
BMXVideoAttachmentPtr attachment(new BMXVideoAttachment(path, duration, size, displayName));
BMXMessagePtr msg = BMXMessage::createMessage(2272061685216, 2272061881760, (BMXMessage::MessageType)1, 2272061881760, attachment);
```

### 消息操作

消息实体构建完成后，通过 BMXClient的单例，ChatService类，调用 sendMessage: 方法，将构建好的消息实体传入，即可实现消息发送。消息状态变化会通过注册的BMXChatServiceListener类型的listener回调通知。

* 发送

```
client->getChatService().sendMessage(msg);
```

* 转发

```
BMXMessagePtr forwardMsg = BMXMessage::createForwardMessage(msg, from, to, type, conversationId);
client->getChatService().forwardMessage(msg);
```

* 重发

```
client->getChatService().resendMessage(msg);
```

* 撤回

```
client->getChatService().recallMessage(msg);
```

* 下载消息附件

```
client->getChatService().downloadAttachment(msg);
```

### 消息接收监听

注册消息回调

```
client->getChatService().addChatListener(listener); //添加聊天监听者
client->getChatService().removeChatListener(listener);  //移除聊天监听者
```

* 接收到消息通知

```
void onReceive(const BMXMessageList& list)  {}
```

* 消息发送后状态回调通知

```
void onStatusChanged(BMXMessagePtr msg, BMXErrorCode error) {}
```

* 附件消息发送状态回调

```
void onAttachmentUploadProgressChanged(BMXMessagePtr msg, int percent)  {}
```

* 附件消息下载状态变化

```
void onAttachmentStatusChanged(BMXMessagePtr msg, BMXErrorCode error, int percent)  {}
```

## 功能进阶

BMXMessage实体中，提供可扩展属性(extension 和 config) extension 为开发使用的扩展字段，例如编辑状态。 config 为SDK自用的扩展字段，例如mention功能，push功能。

* 群组@功能 群组中支持 @ 功能，满足您 @ 指定用户或 @ 所有人的需求，开发者在BMXMessage中通过设置 setConfig 来实现群主@功能，已经@成员后的会同时在移动端下发推送通知。config对象中通过设置setMentionList可以设置@通知列表。通过setMentionAll设置是否@全部群成员。
* 消息正在输入状态

```
// 可以使用extensionJson，来扩展正在编辑状态消息，（json格式，可以扩展多种自定义功能）
void setExtension(const JSON&)
```

可以使用BMXMessage的setExtension函数设置json格式的信息，表明客户端在进行输入。

* 消息搜索

根据关键字搜索指定消息内容

```
/**
  * @param keywords 搜索的关键字
  * @param refTime 搜索消息的起始时间
  * @param size 搜索的最大消息条数
  * @param result 搜索到的消息结果列表，外部初始化传入空列表。
  * @param Direction 消息搜索方向，默认（Direction::Up）是从更早的消息中搜索
  **/
BMXErrorCode errorCode = client->getChatService().searchMessages(keywords, refTime, size, result, direction);
```
