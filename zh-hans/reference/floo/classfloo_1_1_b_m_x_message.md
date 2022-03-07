---
title: floo::BMXMessage
summary: 消息 

---

# floo::BMXMessage



消息 


`#include <bmx_message.h>`

Inherits from BMXBaseObject

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[DeliveryStatus](classfloo_1_1_b_m_x_message.md#enum-deliverystatus)** { New, Delivering, Deliveried, Failed, Recalled}<br>消息投递状态  |
| enum class| **[MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype)** { Single, Group, System}<br>消息类型  |
| enum class| **[ContentType](classfloo_1_1_b_m_x_message.md#enum-contenttype)** { Text, Image, Voice, Video, File, Location, Command, Forward}<br>消息内容类型  |
| enum class| **[DeliveryQos](classfloo_1_1_b_m_x_message.md#enum-deliveryqos)** { AtLastOnce, AtMostOnce, ExactlyOnce}<br>消息投递质量  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXMessage](classfloo_1_1_b_m_x_message.md#function-~bmxmessage)**()<br>析构函数  |
| int64_t | **[msgId](classfloo_1_1_b_m_x_message.md#function-msgid)**()<br>消息唯一ID  |
| int64_t | **[clientMsgId](classfloo_1_1_b_m_x_message.md#function-clientmsgid)**()<br>消息客户端ID,仅在消息发送端存在  |
| int64_t | **[fromId](classfloo_1_1_b_m_x_message.md#function-fromid)**()<br>消息发送方ID  |
| int64_t | **[toId](classfloo_1_1_b_m_x_message.md#function-toid)**()<br>消息接收方ID  |
| [MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype) | **[type](classfloo_1_1_b_m_x_message.md#function-type)**()<br>消息类型  |
| int64_t | **[conversationId](classfloo_1_1_b_m_x_message.md#function-conversationid)**()<br>消息所属会话ID  |
| [DeliveryStatus](classfloo_1_1_b_m_x_message.md#enum-deliverystatus) | **[deliveryStatus](classfloo_1_1_b_m_x_message.md#function-deliverystatus)**()<br>消息投递状态  |
| void | **[setDeliveryStatus](classfloo_1_1_b_m_x_message.md#function-setdeliverystatus)**([DeliveryStatus](classfloo_1_1_b_m_x_message.md#enum-deliverystatus) )<br>设置消息投递状态  |
| int64_t | **[serverTimestamp](classfloo_1_1_b_m_x_message.md#function-servertimestamp)**()<br>消息时间戳（服务端收到时的时间）  |
| void | **[setServerTimestamp](classfloo_1_1_b_m_x_message.md#function-setservertimestamp)**(int64_t )<br>设置时间戳（服务端收到时的时间）  |
| int64_t | **[clientTimestamp](classfloo_1_1_b_m_x_message.md#function-clienttimestamp)**()<br>本地时间戳（消息创建或者收到时的本地时间）  |
| void | **[setClientTimestamp](classfloo_1_1_b_m_x_message.md#function-setclienttimestamp)**(int64_t )<br>设置消息本地时间戳  |
| bool | **[isPlayed](classfloo_1_1_b_m_x_message.md#function-isplayed)**()<br>语音或者视频消息是否播放过，仅对收到的音视频消息有效  |
| void | **[setIsPlayed](classfloo_1_1_b_m_x_message.md#function-setisplayed)**(bool )<br>设置语音或者视频消息是否播放过，仅对收到的音视频消息有效  |
| bool | **[isPlayAcked](classfloo_1_1_b_m_x_message.md#function-isplayacked)**()<br>对于发送方表示是否收到了已播放回执，对于接收方表示是否发送了已播放回执  |
| void | **[setIsPlayAcked](classfloo_1_1_b_m_x_message.md#function-setisplayacked)**(bool )<br>设置已播放回执  |
| bool | **[isReceiveMsg](classfloo_1_1_b_m_x_message.md#function-isreceivemsg)**()<br>是否接收的消息  |
| void | **[setIsReceiveMsg](classfloo_1_1_b_m_x_message.md#function-setisreceivemsg)**(bool )<br>设置是否接收的消息  |
| bool | **[isRead](classfloo_1_1_b_m_x_message.md#function-isread)**()<br>消息是否已读标志  |
| void | **[setIsRead](classfloo_1_1_b_m_x_message.md#function-setisread)**(bool )<br>消息是否已读标志  |
| bool | **[isReadAcked](classfloo_1_1_b_m_x_message.md#function-isreadacked)**()<br>对于发送方表示是否收到了已读回执，对于接收方表示是否发送了已读回执  |
| void | **[setIsReadAcked](classfloo_1_1_b_m_x_message.md#function-setisreadacked)**(bool )<br>设置已读回执  |
| bool | **[isDeliveryAcked](classfloo_1_1_b_m_x_message.md#function-isdeliveryacked)**()<br>对于发送方表示消息是否已投递到对方，对于接收方表示是否发送了消息已到达回执  |
| void | **[setIsDeliveryAcked](classfloo_1_1_b_m_x_message.md#function-setisdeliveryacked)**(bool )<br>设置投递回执  |
| const std::string & | **[content](classfloo_1_1_b_m_x_message.md#function-content)**()<br>消息文本内容  |
| void | **[setContent](classfloo_1_1_b_m_x_message.md#function-setcontent)**(const std::string & content)<br>消息文本内容  |
| [ContentType](classfloo_1_1_b_m_x_message.md#enum-contenttype) | **[contentType](classfloo_1_1_b_m_x_message.md#function-contenttype)**()<br>消息内容类型，如果带附件就表示附件类型，不带附件就是文本类型  |
| BMXMessageAttachmentPtr | **[attachment](classfloo_1_1_b_m_x_message.md#function-attachment)**()<br>消息附件，BMXMessage拥有附件的所有权，负责释放  |
| BMXMessageConfigPtr | **[config](classfloo_1_1_b_m_x_message.md#function-config)**()<br>消息的配置信息  |
| void | **[setConfig](classfloo_1_1_b_m_x_message.md#function-setconfig)**(BMXMessageConfigPtr )<br>设置消息配置信息  |
| const JSON & | **[extension](classfloo_1_1_b_m_x_message.md#function-extension)**()<br>消息扩展信息  |
| void | **[setExtension](classfloo_1_1_b_m_x_message.md#function-setextension)**(const JSON & )<br>设置消息扩展信息  |
| [DeliveryQos](classfloo_1_1_b_m_x_message.md#enum-deliveryqos) | **[deliveryQos](classfloo_1_1_b_m_x_message.md#function-deliveryqos)**()<br>消息投递QOS  |
| void | **[setDeliveryQos](classfloo_1_1_b_m_x_message.md#function-setdeliveryqos)**([DeliveryQos](classfloo_1_1_b_m_x_message.md#enum-deliveryqos) qos)<br>设置消息投递QOS  |
| const std::string & | **[senderName](classfloo_1_1_b_m_x_message.md#function-sendername)**()<br>消息发送者的显示名称  |
| void | **[setSenderName](classfloo_1_1_b_m_x_message.md#function-setsendername)**(const std::string & senderName)<br>设置消息的发送者显示名称  |
| int | **[groupAckCount](classfloo_1_1_b_m_x_message.md#function-groupackcount)**()<br>群消息已读AckCount数目  |
| void | **[setGroupAckCount](classfloo_1_1_b_m_x_message.md#function-setgroupackcount)**(int count)<br>设置消息已读groupAckCount数目(SDK 内部调用接口，上层不应该调用)  |
| int | **[groupAckUnreadCount](classfloo_1_1_b_m_x_message.md#function-groupackunreadcount)**()<br>群消息未读AckCount数目  |
| void | **[setGroupAckUnreadCount](classfloo_1_1_b_m_x_message.md#function-setgroupackunreadcount)**(int count)<br>设置消息未读groupAckCount数目(SDK 内部调用接口，上层不应该调用)  |
| bool | **[groupAckReadAll](classfloo_1_1_b_m_x_message.md#function-groupackreadall)**()<br>群消息是否全部已读  |
| int | **[groupPlayAckCount](classfloo_1_1_b_m_x_message.md#function-groupplayackcount)**()<br>群消息已播放AckCount数目（仅用于音频/视频附件消息）  |
| void | **[setGroupPlayAckCount](classfloo_1_1_b_m_x_message.md#function-setgroupplayackcount)**(int count)<br>设置消息已播放groupAckCount数目(SDK 内部调用接口，上层不应该调用)（仅用于音频/视频附件消息）  |
| int | **[groupPlayAckUnreadCount](classfloo_1_1_b_m_x_message.md#function-groupplayackunreadcount)**()<br>群消息未播放AckCount数目（仅用于音频/视频附件消息）  |
| void | **[setGroupPlayAckUnreadCount](classfloo_1_1_b_m_x_message.md#function-setgroupplayackunreadcount)**(int count)<br>设置消息未播放groupAckCount数目(SDK 内部调用接口，上层不应该调用)（仅用于音频/视频附件消息）  |
| bool | **[groupPlayAckReadAll](classfloo_1_1_b_m_x_message.md#function-groupplayackreadall)**()<br>群消息是否全部已播放  |
| void | **[setPriority](classfloo_1_1_b_m_x_message.md#function-setpriority)**(int priority)<br>设置消息的扩散优先级，默认为0。0表示扩散，数字越小扩散的越多。  |
| int | **[priority](classfloo_1_1_b_m_x_message.md#function-priority)**()<br>消息的扩散优先级  |
| void | **[setPushMessageMode](classfloo_1_1_b_m_x_message.md#function-setpushmessagemode)**(bool )<br>设置消息是否为推送消息。  |
| bool | **[isPushMessage](classfloo_1_1_b_m_x_message.md#function-ispushmessage)**()<br>消息是否是推送消息  |
| BMXMessagePtr | **[createMessage](classfloo_1_1_b_m_x_message.md#function-createmessage)**(int64_t from, int64_t to, [MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype) type, int64_t conversationId, const std::string & content)<br>创建发送文本消息  |
| BMXMessagePtr | **[createMessage](classfloo_1_1_b_m_x_message.md#function-createmessage)**(int64_t from, int64_t to, [MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype) type, int64_t conversationId, BMXMessageAttachmentPtr attachment)<br>创建发送附件消息  |
| BMXMessagePtr | **[createCommandMessage](classfloo_1_1_b_m_x_message.md#function-createcommandmessage)**(int64_t from, int64_t to, [MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype) type, int64_t conversationId, const std::string & content)<br>创建发送命令消息(命令消息通过content字段或者extension字段存放命令信息)  |
| BMXMessagePtr | **[createMessage](classfloo_1_1_b_m_x_message.md#function-createmessage)**(int64_t msgId, int64_t from, int64_t to, [MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype) type, int64_t conversationId, const std::string & content, int64_t serverTimestamp)<br>创建收到的消息  |
| BMXMessagePtr | **[createMessage](classfloo_1_1_b_m_x_message.md#function-createmessage)**(int64_t msgId, int64_t from, int64_t to, [MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype) type, int64_t conversationId, BMXMessageAttachmentPtr attachment, int64_t serverTimestamp)<br>创建收到的消息  |
| BMXMessagePtr | **[createCommandMessage](classfloo_1_1_b_m_x_message.md#function-createcommandmessage)**(int64_t msgId, int64_t from, int64_t to, [MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype) type, int64_t conversationId, const std::string & content, int64_t serverTimestamp)<br>创建收到的命令消息(命令消息通过content字段或者extension字段存放命令信息)  |
| BMXMessagePtr | **[createForwardMessage](classfloo_1_1_b_m_x_message.md#function-createforwardmessage)**(BMXMessagePtr msg, int64_t from, int64_t to, [MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype) type, int64_t conversationId)<br>创建转发消息  |

## Public Types Documentation

### enum DeliveryStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| New | | 新创建消息   |
| Delivering | | 消息投递中   |
| Deliveried | | 消息已投递   |
| Failed | | 消息投递失败   |
| Recalled | | 消息已撤回   |



消息投递状态 

### enum MessageType

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Single | | 单聊消息   |
| Group | | 群聊消息   |
| System | | 系统消息   |



消息类型 

### enum ContentType

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Text | | 文本消息   |
| Image | | 图片消息   |
| Voice | | 语音消息   |
| Video | | 视频片段消息   |
| File | | 文件消息   |
| Location | | 位置消息   |
| Command | | 命令消息   |
| Forward | | 转发消息   |



消息内容类型 

### enum DeliveryQos

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| AtLastOnce | | 最少投递一次   |
| AtMostOnce | | 最多投递一次   |
| ExactlyOnce | | 仅投递一次   |



消息投递质量 

## Public Functions Documentation

### function ~BMXMessage

```cpp
virtual ~BMXMessage()
```

析构函数 

### function msgId

```cpp
int64_t msgId()
```

消息唯一ID 

**Return**: int64_t 

### function clientMsgId

```cpp
int64_t clientMsgId()
```

消息客户端ID,仅在消息发送端存在 

**Return**: int64_t 

### function fromId

```cpp
int64_t fromId()
```

消息发送方ID 

**Return**: int64_t 

### function toId

```cpp
int64_t toId()
```

消息接收方ID 

**Return**: int64_t 

### function type

```cpp
MessageType type()
```

消息类型 

**Return**: MessageType 

### function conversationId

```cpp
int64_t conversationId()
```

消息所属会话ID 

**Return**: int64_t 

### function deliveryStatus

```cpp
DeliveryStatus deliveryStatus()
```

消息投递状态 

**Return**: DeliveryStatus 

### function setDeliveryStatus

```cpp
void setDeliveryStatus(
    DeliveryStatus 
)
```

设置消息投递状态 

### function serverTimestamp

```cpp
int64_t serverTimestamp()
```

消息时间戳（服务端收到时的时间） 

**Return**: int64_t 

### function setServerTimestamp

```cpp
void setServerTimestamp(
    int64_t 
)
```

设置时间戳（服务端收到时的时间） 

### function clientTimestamp

```cpp
int64_t clientTimestamp()
```

本地时间戳（消息创建或者收到时的本地时间） 

**Return**: int64_t 

### function setClientTimestamp

```cpp
void setClientTimestamp(
    int64_t 
)
```

设置消息本地时间戳 

### function isPlayed

```cpp
bool isPlayed()
```

语音或者视频消息是否播放过，仅对收到的音视频消息有效 

**Return**: bool 

### function setIsPlayed

```cpp
void setIsPlayed(
    bool 
)
```

设置语音或者视频消息是否播放过，仅对收到的音视频消息有效 

### function isPlayAcked

```cpp
bool isPlayAcked()
```

对于发送方表示是否收到了已播放回执，对于接收方表示是否发送了已播放回执 

**Return**: bool 

### function setIsPlayAcked

```cpp
void setIsPlayAcked(
    bool 
)
```

设置已播放回执 

### function isReceiveMsg

```cpp
bool isReceiveMsg()
```

是否接收的消息 

**Return**: bool 

### function setIsReceiveMsg

```cpp
void setIsReceiveMsg(
    bool 
)
```

设置是否接收的消息 

### function isRead

```cpp
bool isRead()
```

消息是否已读标志 

**Return**: bool 

### function setIsRead

```cpp
void setIsRead(
    bool 
)
```

消息是否已读标志 

### function isReadAcked

```cpp
bool isReadAcked()
```

对于发送方表示是否收到了已读回执，对于接收方表示是否发送了已读回执 

**Return**: bool 

### function setIsReadAcked

```cpp
void setIsReadAcked(
    bool 
)
```

设置已读回执 

### function isDeliveryAcked

```cpp
bool isDeliveryAcked()
```

对于发送方表示消息是否已投递到对方，对于接收方表示是否发送了消息已到达回执 

**Return**: bool 

### function setIsDeliveryAcked

```cpp
void setIsDeliveryAcked(
    bool 
)
```

设置投递回执 

### function content

```cpp
const std::string & content()
```

消息文本内容 

**Return**: std::string 

### function setContent

```cpp
void setContent(
    const std::string & content
)
```

消息文本内容 

**Parameters**: 

  * **content** 消息文本内容 


### function contentType

```cpp
ContentType contentType()
```

消息内容类型，如果带附件就表示附件类型，不带附件就是文本类型 

**Return**: ContentType 

### function attachment

```cpp
BMXMessageAttachmentPtr attachment()
```

消息附件，BMXMessage拥有附件的所有权，负责释放 

**Return**: BMXMessageAttachmentPtr 

### function config

```cpp
BMXMessageConfigPtr config()
```

消息的配置信息 

**Return**: JSON(std::string) 

### function setConfig

```cpp
void setConfig(
    BMXMessageConfigPtr 
)
```

设置消息配置信息 

### function extension

```cpp
const JSON & extension()
```

消息扩展信息 

**Return**: JSON(std::string) 

### function setExtension

```cpp
void setExtension(
    const JSON & 
)
```

设置消息扩展信息 

### function deliveryQos

```cpp
DeliveryQos deliveryQos()
```

消息投递QOS 

**Return**: DeliveryQos 

### function setDeliveryQos

```cpp
void setDeliveryQos(
    DeliveryQos qos
)
```

设置消息投递QOS 

**Parameters**: 

  * **qos** 消息投递QOS 


### function senderName

```cpp
const std::string & senderName()
```

消息发送者的显示名称 

**Return**: std::string 

### function setSenderName

```cpp
void setSenderName(
    const std::string & senderName
)
```

设置消息的发送者显示名称 

**Parameters**: 

  * **senderName** 消息文本内容 


### function groupAckCount

```cpp
int groupAckCount()
```

群消息已读AckCount数目 

**Return**: int 

### function setGroupAckCount

```cpp
void setGroupAckCount(
    int count
)
```

设置消息已读groupAckCount数目(SDK 内部调用接口，上层不应该调用) 

**Parameters**: 

  * **count** 设置群消息已读数目 


### function groupAckUnreadCount

```cpp
int groupAckUnreadCount()
```

群消息未读AckCount数目 

**Return**: int 

### function setGroupAckUnreadCount

```cpp
void setGroupAckUnreadCount(
    int count
)
```

设置消息未读groupAckCount数目(SDK 内部调用接口，上层不应该调用) 

**Parameters**: 

  * **count** 设置群消息未读数目 


### function groupAckReadAll

```cpp
bool groupAckReadAll()
```

群消息是否全部已读 

**Return**: bool 

### function groupPlayAckCount

```cpp
int groupPlayAckCount()
```

群消息已播放AckCount数目（仅用于音频/视频附件消息） 

**Return**: int 

### function setGroupPlayAckCount

```cpp
void setGroupPlayAckCount(
    int count
)
```

设置消息已播放groupAckCount数目(SDK 内部调用接口，上层不应该调用)（仅用于音频/视频附件消息） 

**Parameters**: 

  * **count** 设置群消息已读数目 


### function groupPlayAckUnreadCount

```cpp
int groupPlayAckUnreadCount()
```

群消息未播放AckCount数目（仅用于音频/视频附件消息） 

**Return**: int 

### function setGroupPlayAckUnreadCount

```cpp
void setGroupPlayAckUnreadCount(
    int count
)
```

设置消息未播放groupAckCount数目(SDK 内部调用接口，上层不应该调用)（仅用于音频/视频附件消息） 

**Parameters**: 

  * **count** 设置群消息未播放数目 


### function groupPlayAckReadAll

```cpp
bool groupPlayAckReadAll()
```

群消息是否全部已播放 

**Return**: bool 

### function setPriority

```cpp
void setPriority(
    int priority
)
```

设置消息的扩散优先级，默认为0。0表示扩散，数字越小扩散的越多。 

**Parameters**: 

  * **priority** 设置群消息未读数目 


取值范围0-10。普通人在聊天室发送的消息级别默认为5，可以丢弃。管理员默认为0不会丢弃。其它值可以根据业务自行设置。 


### function priority

```cpp
int priority()
```

消息的扩散优先级 

**Return**: int 

### function setPushMessageMode

```cpp
void setPushMessageMode(
    bool 
)
```

设置消息是否为推送消息。 

### function isPushMessage

```cpp
bool isPushMessage()
```

消息是否是推送消息 

**Return**: bool 

### function createMessage

```cpp
static BMXMessagePtr createMessage(
    int64_t from,
    int64_t to,
    MessageType type,
    int64_t conversationId,
    const std::string & content
)
```

创建发送文本消息 

**Parameters**: 

  * **from** 消息发送者 
  * **to** 消息接收者 
  * **type** 消息类型 
  * **conversationId** 会话id 
  * **content** 消息内容 


### function createMessage

```cpp
static BMXMessagePtr createMessage(
    int64_t from,
    int64_t to,
    MessageType type,
    int64_t conversationId,
    BMXMessageAttachmentPtr attachment
)
```

创建发送附件消息 

**Parameters**: 

  * **from** 消息发送者 
  * **to** 消息接收者 
  * **type** 消息类型 
  * **conversationId** 会话id 
  * **attachment** 附件 


### function createCommandMessage

```cpp
static BMXMessagePtr createCommandMessage(
    int64_t from,
    int64_t to,
    MessageType type,
    int64_t conversationId,
    const std::string & content
)
```

创建发送命令消息(命令消息通过content字段或者extension字段存放命令信息) 

**Parameters**: 

  * **from** 消息发送者 
  * **to** 消息接收者 
  * **type** 消息类型 
  * **conversationId** 会话id 
  * **content** 消息内容 


### function createMessage

```cpp
static BMXMessagePtr createMessage(
    int64_t msgId,
    int64_t from,
    int64_t to,
    MessageType type,
    int64_t conversationId,
    const std::string & content,
    int64_t serverTimestamp
)
```

创建收到的消息 

**Parameters**: 

  * **msgId** 消息id 
  * **from** 消息发送者 
  * **to** 消息接收者 
  * **type** 消息类型 
  * **conversationId** 会话id 
  * **content** 消息内容 
  * **serverTimestamp** 服务器时间戳 


### function createMessage

```cpp
static BMXMessagePtr createMessage(
    int64_t msgId,
    int64_t from,
    int64_t to,
    MessageType type,
    int64_t conversationId,
    BMXMessageAttachmentPtr attachment,
    int64_t serverTimestamp
)
```

创建收到的消息 

**Parameters**: 

  * **msgId** 消息id 
  * **from** 消息发送者 
  * **to** 消息接收者 
  * **type** 消息类型 
  * **conversationId** 会话id 
  * **attachment** 附件 
  * **serverTimestamp** 服务器时间戳 


### function createCommandMessage

```cpp
static BMXMessagePtr createCommandMessage(
    int64_t msgId,
    int64_t from,
    int64_t to,
    MessageType type,
    int64_t conversationId,
    const std::string & content,
    int64_t serverTimestamp
)
```

创建收到的命令消息(命令消息通过content字段或者extension字段存放命令信息) 

**Parameters**: 

  * **msgId** 消息id 
  * **from** 消息发送者 
  * **to** 消息接收者 
  * **type** 消息类型 
  * **conversationId** 会话id 
  * **content** 消息内容 
  * **serverTimestamp** 服务器时间戳 


### function createForwardMessage

```cpp
static BMXMessagePtr createForwardMessage(
    BMXMessagePtr msg,
    int64_t from,
    int64_t to,
    MessageType type,
    int64_t conversationId
)
```

创建转发消息 

**Parameters**: 

  * **msg** 要转发的消息 
  * **from** 消息发送者 
  * **to** 消息接收者 
  * **type** 消息类型 
  * **conversationId** 会话id 


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800