---
title: floo::BMXMessage
summary: 消息
---

# floo::BMXMessage

消息

`#include <bmx_message.h>`

Inherits from BMXBaseObject

## Public Types

|            | Name                                                                                                                                                                       |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class | <p><a href="classfloo_1_1_b_m_x_message.md#enum-deliverystatus"><strong>DeliveryStatus</strong></a> { New, Delivering, Deliveried, Failed, Recalled}<br>消息投递状态</p>         |
| enum class | <p><a href="classfloo_1_1_b_m_x_message.md#enum-messagetype"><strong>MessageType</strong></a> { Single, Group, System}<br>消息类型</p>                                         |
| enum class | <p><a href="classfloo_1_1_b_m_x_message.md#enum-contenttype"><strong>ContentType</strong></a> { Text, Image, Voice, Video, File, Location, Command, Forward}<br>消息内容类型</p> |
| enum class | <p><a href="classfloo_1_1_b_m_x_message.md#enum-deliveryqos"><strong>DeliveryQos</strong></a> { AtLastOnce, AtMostOnce, ExactlyOnce}<br>消息投递质量</p>                         |

## Public Functions

|                                                                            | Name                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| virtual                                                                    | <p><a href="classfloo_1_1_b_m_x_message.md#function-~bmxmessage"><strong>~BMXMessage</strong></a>()<br>析构函数</p>                                                                                                                                                                                                                                                                      |
| int64\_t                                                                   | <p><a href="classfloo_1_1_b_m_x_message.md#function-msgid"><strong>msgId</strong></a>()<br>消息唯一ID</p>                                                                                                                                                                                                                                                                                |
| int64\_t                                                                   | <p><a href="classfloo_1_1_b_m_x_message.md#function-clientmsgid"><strong>clientMsgId</strong></a>()<br>消息客户端ID,仅在消息发送端存在</p>                                                                                                                                                                                                                                                         |
| int64\_t                                                                   | <p><a href="classfloo_1_1_b_m_x_message.md#function-fromid"><strong>fromId</strong></a>()<br>消息发送方ID</p>                                                                                                                                                                                                                                                                             |
| int64\_t                                                                   | <p><a href="classfloo_1_1_b_m_x_message.md#function-toid"><strong>toId</strong></a>()<br>消息接收方ID</p>                                                                                                                                                                                                                                                                                 |
| [MessageType](classfloo\_1\_1\_b\_m\_x\_message.md#enum-messagetype)       | <p><a href="classfloo_1_1_b_m_x_message.md#function-type"><strong>type</strong></a>()<br>消息类型</p>                                                                                                                                                                                                                                                                                    |
| int64\_t                                                                   | <p><a href="classfloo_1_1_b_m_x_message.md#function-conversationid"><strong>conversationId</strong></a>()<br>消息所属会话ID</p>                                                                                                                                                                                                                                                            |
| [DeliveryStatus](classfloo\_1\_1\_b\_m\_x\_message.md#enum-deliverystatus) | <p><a href="classfloo_1_1_b_m_x_message.md#function-deliverystatus"><strong>deliveryStatus</strong></a>()<br>消息投递状态</p>                                                                                                                                                                                                                                                              |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setdeliverystatus"><strong>setDeliveryStatus</strong></a>(<a href="classfloo_1_1_b_m_x_message.md#enum-deliverystatus">DeliveryStatus</a> )<br>设置消息投递状态</p>                                                                                                                                                                      |
| int64\_t                                                                   | <p><a href="classfloo_1_1_b_m_x_message.md#function-servertimestamp"><strong>serverTimestamp</strong></a>()<br>消息时间戳（服务端收到时的时间）</p>                                                                                                                                                                                                                                                  |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setservertimestamp"><strong>setServerTimestamp</strong></a>(int64_t )<br>设置时间戳（服务端收到时的时间）</p>                                                                                                                                                                                                                                    |
| int64\_t                                                                   | <p><a href="classfloo_1_1_b_m_x_message.md#function-clienttimestamp"><strong>clientTimestamp</strong></a>()<br>本地时间戳（消息创建或者收到时的本地时间）</p>                                                                                                                                                                                                                                             |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setclienttimestamp"><strong>setClientTimestamp</strong></a>(int64_t )<br>设置消息本地时间戳</p>                                                                                                                                                                                                                                           |
| bool                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-isplayed"><strong>isPlayed</strong></a>()<br>语音或者视频消息是否播放过，仅对收到的音视频消息有效</p>                                                                                                                                                                                                                                                      |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setisplayed"><strong>setIsPlayed</strong></a>(bool )<br>设置语音或者视频消息是否播放过，仅对收到的音视频消息有效</p>                                                                                                                                                                                                                                         |
| bool                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-isplayacked"><strong>isPlayAcked</strong></a>()<br>对于发送方表示是否收到了已播放回执，对于接收方表示是否发送了已播放回执</p>                                                                                                                                                                                                                                       |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setisplayacked"><strong>setIsPlayAcked</strong></a>(bool )<br>设置已播放回执</p>                                                                                                                                                                                                                                                        |
| bool                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-isreceivemsg"><strong>isReceiveMsg</strong></a>()<br>是否接收的消息</p>                                                                                                                                                                                                                                                                 |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setisreceivemsg"><strong>setIsReceiveMsg</strong></a>(bool )<br>设置是否接收的消息</p>                                                                                                                                                                                                                                                    |
| bool                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-isread"><strong>isRead</strong></a>()<br>消息是否已读标志</p>                                                                                                                                                                                                                                                                            |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setisread"><strong>setIsRead</strong></a>(bool )<br>消息是否已读标志</p>                                                                                                                                                                                                                                                                 |
| bool                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-isreadacked"><strong>isReadAcked</strong></a>()<br>对于发送方表示是否收到了已读回执，对于接收方表示是否发送了已读回执</p>                                                                                                                                                                                                                                         |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setisreadacked"><strong>setIsReadAcked</strong></a>(bool )<br>设置已读回执</p>                                                                                                                                                                                                                                                         |
| bool                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-isdeliveryacked"><strong>isDeliveryAcked</strong></a>()<br>对于发送方表示消息是否已投递到对方，对于接收方表示是否发送了消息已到达回执</p>                                                                                                                                                                                                                             |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setisdeliveryacked"><strong>setIsDeliveryAcked</strong></a>(bool )<br>设置投递回执</p>                                                                                                                                                                                                                                                 |
| const std::string &                                                        | <p><a href="classfloo_1_1_b_m_x_message.md#function-content"><strong>content</strong></a>()<br>消息文本内容</p>                                                                                                                                                                                                                                                                            |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setcontent"><strong>setContent</strong></a>(const std::string &#x26; content)<br>消息文本内容</p>                                                                                                                                                                                                                                      |
| [ContentType](classfloo\_1\_1\_b\_m\_x\_message.md#enum-contenttype)       | <p><a href="classfloo_1_1_b_m_x_message.md#function-contenttype"><strong>contentType</strong></a>()<br>消息内容类型，如果带附件就表示附件类型，不带附件就是文本类型</p>                                                                                                                                                                                                                                            |
| BMXMessageAttachmentPtr                                                    | <p><a href="classfloo_1_1_b_m_x_message.md#function-attachment"><strong>attachment</strong></a>()<br>消息附件，BMXMessage拥有附件的所有权，负责释放</p>                                                                                                                                                                                                                                                |
| BMXMessageConfigPtr                                                        | <p><a href="classfloo_1_1_b_m_x_message.md#function-config"><strong>config</strong></a>()<br>消息的配置信息</p>                                                                                                                                                                                                                                                                             |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setconfig"><strong>setConfig</strong></a>(BMXMessageConfigPtr )<br>设置消息配置信息</p>                                                                                                                                                                                                                                                  |
| const JSON &                                                               | <p><a href="classfloo_1_1_b_m_x_message.md#function-extension"><strong>extension</strong></a>()<br>消息扩展信息</p>                                                                                                                                                                                                                                                                        |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setextension"><strong>setExtension</strong></a>(const JSON &#x26; )<br>设置消息扩展信息</p>                                                                                                                                                                                                                                              |
| [DeliveryQos](classfloo\_1\_1\_b\_m\_x\_message.md#enum-deliveryqos)       | <p><a href="classfloo_1_1_b_m_x_message.md#function-deliveryqos"><strong>deliveryQos</strong></a>()<br>消息投递QOS</p>                                                                                                                                                                                                                                                                   |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setdeliveryqos"><strong>setDeliveryQos</strong></a>(<a href="classfloo_1_1_b_m_x_message.md#enum-deliveryqos">DeliveryQos</a> qos)<br>设置消息投递QOS</p>                                                                                                                                                                              |
| const std::string &                                                        | <p><a href="classfloo_1_1_b_m_x_message.md#function-sendername"><strong>senderName</strong></a>()<br>消息发送者的显示名称</p>                                                                                                                                                                                                                                                                  |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setsendername"><strong>setSenderName</strong></a>(const std::string &#x26; senderName)<br>设置消息的发送者显示名称</p>                                                                                                                                                                                                                       |
| int                                                                        | <p><a href="classfloo_1_1_b_m_x_message.md#function-groupackcount"><strong>groupAckCount</strong></a>()<br>群消息已读AckCount数目</p>                                                                                                                                                                                                                                                       |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setgroupackcount"><strong>setGroupAckCount</strong></a>(int count)<br>设置消息已读groupAckCount数目(SDK 内部调用接口，上层不应该调用)</p>                                                                                                                                                                                                              |
| int                                                                        | <p><a href="classfloo_1_1_b_m_x_message.md#function-groupackunreadcount"><strong>groupAckUnreadCount</strong></a>()<br>群消息未读AckCount数目</p>                                                                                                                                                                                                                                           |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setgroupackunreadcount"><strong>setGroupAckUnreadCount</strong></a>(int count)<br>设置消息未读groupAckCount数目(SDK 内部调用接口，上层不应该调用)</p>                                                                                                                                                                                                  |
| bool                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-groupackreadall"><strong>groupAckReadAll</strong></a>()<br>群消息是否全部已读</p>                                                                                                                                                                                                                                                         |
| int                                                                        | <p><a href="classfloo_1_1_b_m_x_message.md#function-groupplayackcount"><strong>groupPlayAckCount</strong></a>()<br>群消息已播放AckCount数目（仅用于音频/视频附件消息）</p>                                                                                                                                                                                                                                |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setgroupplayackcount"><strong>setGroupPlayAckCount</strong></a>(int count)<br>设置消息已播放groupAckCount数目(SDK 内部调用接口，上层不应该调用)（仅用于音频/视频附件消息）</p>                                                                                                                                                                                       |
| int                                                                        | <p><a href="classfloo_1_1_b_m_x_message.md#function-groupplayackunreadcount"><strong>groupPlayAckUnreadCount</strong></a>()<br>群消息未播放AckCount数目（仅用于音频/视频附件消息）</p>                                                                                                                                                                                                                    |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setgroupplayackunreadcount"><strong>setGroupPlayAckUnreadCount</strong></a>(int count)<br>设置消息未播放groupAckCount数目(SDK 内部调用接口，上层不应该调用)（仅用于音频/视频附件消息）</p>                                                                                                                                                                           |
| bool                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-groupplayackreadall"><strong>groupPlayAckReadAll</strong></a>()<br>群消息是否全部已播放</p>                                                                                                                                                                                                                                                |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setpriority"><strong>setPriority</strong></a>(int priority)<br>设置消息的扩散优先级，默认为0。0表示扩散，数字越小扩散的越多。</p>                                                                                                                                                                                                                              |
| int                                                                        | <p><a href="classfloo_1_1_b_m_x_message.md#function-priority"><strong>priority</strong></a>()<br>消息的扩散优先级</p>                                                                                                                                                                                                                                                                        |
| void                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-setpushmessagemode"><strong>setPushMessageMode</strong></a>(bool )<br>设置消息是否为推送消息。</p>                                                                                                                                                                                                                                           |
| bool                                                                       | <p><a href="classfloo_1_1_b_m_x_message.md#function-ispushmessage"><strong>isPushMessage</strong></a>()<br>消息是否是推送消息</p>                                                                                                                                                                                                                                                             |
| BMXMessagePtr                                                              | <p><a href="classfloo_1_1_b_m_x_message.md#function-createmessage"><strong>createMessage</strong></a>(int64_t from, int64_t to, <a href="classfloo_1_1_b_m_x_message.md#enum-messagetype">MessageType</a> type, int64_t conversationId, const std::string &#x26; content)<br>创建发送文本消息</p>                                                                                            |
| BMXMessagePtr                                                              | <p><a href="classfloo_1_1_b_m_x_message.md#function-createmessage"><strong>createMessage</strong></a>(int64_t from, int64_t to, <a href="classfloo_1_1_b_m_x_message.md#enum-messagetype">MessageType</a> type, int64_t conversationId, BMXMessageAttachmentPtr attachment)<br>创建发送附件消息</p>                                                                                          |
| BMXMessagePtr                                                              | <p><a href="classfloo_1_1_b_m_x_message.md#function-createcommandmessage"><strong>createCommandMessage</strong></a>(int64_t from, int64_t to, <a href="classfloo_1_1_b_m_x_message.md#enum-messagetype">MessageType</a> type, int64_t conversationId, const std::string &#x26; content)<br>创建发送命令消息(命令消息通过content字段或者extension字段存放命令信息)</p>                                          |
| BMXMessagePtr                                                              | <p><a href="classfloo_1_1_b_m_x_message.md#function-createmessage"><strong>createMessage</strong></a>(int64_t msgId, int64_t from, int64_t to, <a href="classfloo_1_1_b_m_x_message.md#enum-messagetype">MessageType</a> type, int64_t conversationId, const std::string &#x26; content, int64_t serverTimestamp)<br>创建收到的消息</p>                                                     |
| BMXMessagePtr                                                              | <p><a href="classfloo_1_1_b_m_x_message.md#function-createmessage"><strong>createMessage</strong></a>(int64_t msgId, int64_t from, int64_t to, <a href="classfloo_1_1_b_m_x_message.md#enum-messagetype">MessageType</a> type, int64_t conversationId, BMXMessageAttachmentPtr attachment, int64_t serverTimestamp)<br>创建收到的消息</p>                                                   |
| BMXMessagePtr                                                              | <p><a href="classfloo_1_1_b_m_x_message.md#function-createcommandmessage"><strong>createCommandMessage</strong></a>(int64_t msgId, int64_t from, int64_t to, <a href="classfloo_1_1_b_m_x_message.md#enum-messagetype">MessageType</a> type, int64_t conversationId, const std::string &#x26; content, int64_t serverTimestamp)<br>创建收到的命令消息(命令消息通过content字段或者extension字段存放命令信息)</p> |
| BMXMessagePtr                                                              | <p><a href="classfloo_1_1_b_m_x_message.md#function-createforwardmessage"><strong>createForwardMessage</strong></a>(BMXMessagePtr msg, int64_t from, int64_t to, <a href="classfloo_1_1_b_m_x_message.md#enum-messagetype">MessageType</a> type, int64_t conversationId)<br>创建转发消息</p>                                                                                               |

## Public Types Documentation

### enum DeliveryStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| New        |       | 新创建消息       |
| Delivering |       | 消息投递中       |
| Deliveried |       | 消息已投递       |
| Failed     |       | 消息投递失败      |
| Recalled   |       | 消息已撤回       |

消息投递状态

### enum MessageType

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Single     |       | 单聊消息        |
| Group      |       | 群聊消息        |
| System     |       | 系统消息        |

消息类型

### enum ContentType

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Text       |       | 文本消息        |
| Image      |       | 图片消息        |
| Voice      |       | 语音消息        |
| Video      |       | 视频片段消息      |
| File       |       | 文件消息        |
| Location   |       | 位置消息        |
| Command    |       | 命令消息        |
| Forward    |       | 转发消息        |

消息内容类型

### enum DeliveryQos

| Enumerator  | Value | Description |
| ----------- | ----- | ----------- |
| AtLastOnce  |       | 最少投递一次      |
| AtMostOnce  |       | 最多投递一次      |
| ExactlyOnce |       | 仅投递一次       |

消息投递质量

## Public Functions Documentation

### function \~BMXMessage

```cpp
virtual ~BMXMessage()
```

析构函数

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function msgId

```cpp
int64_t msgId()
```

消息唯一ID

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function clientMsgId

```cpp
int64_t clientMsgId()
```

消息客户端ID,仅在消息发送端存在

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function fromId

```cpp
int64_t fromId()
```

消息发送方ID

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function toId

```cpp
int64_t toId()
```

消息接收方ID

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function type

```cpp
MessageType type()
```

消息类型

**Return**: MessageType

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function conversationId

```cpp
int64_t conversationId()
```

消息所属会话ID

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function deliveryStatus

```cpp
DeliveryStatus deliveryStatus()
```

消息投递状态

**Return**: DeliveryStatus

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setDeliveryStatus

```cpp
void setDeliveryStatus(
    DeliveryStatus 
)
```

设置消息投递状态

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function serverTimestamp

```cpp
int64_t serverTimestamp()
```

消息时间戳（服务端收到时的时间）

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setServerTimestamp

```cpp
void setServerTimestamp(
    int64_t 
)
```

设置时间戳（服务端收到时的时间）

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function clientTimestamp

```cpp
int64_t clientTimestamp()
```

本地时间戳（消息创建或者收到时的本地时间）

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setClientTimestamp

```cpp
void setClientTimestamp(
    int64_t 
)
```

设置消息本地时间戳

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function isPlayed

```cpp
bool isPlayed()
```

语音或者视频消息是否播放过，仅对收到的音视频消息有效

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setIsPlayed

```cpp
void setIsPlayed(
    bool 
)
```

设置语音或者视频消息是否播放过，仅对收到的音视频消息有效

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function isPlayAcked

```cpp
bool isPlayAcked()
```

对于发送方表示是否收到了已播放回执，对于接收方表示是否发送了已播放回执

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setIsPlayAcked

```cpp
void setIsPlayAcked(
    bool 
)
```

设置已播放回执

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function isReceiveMsg

```cpp
bool isReceiveMsg()
```

是否接收的消息

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setIsReceiveMsg

```cpp
void setIsReceiveMsg(
    bool 
)
```

设置是否接收的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function isRead

```cpp
bool isRead()
```

消息是否已读标志

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setIsRead

```cpp
void setIsRead(
    bool 
)
```

消息是否已读标志

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function isReadAcked

```cpp
bool isReadAcked()
```

对于发送方表示是否收到了已读回执，对于接收方表示是否发送了已读回执

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setIsReadAcked

```cpp
void setIsReadAcked(
    bool 
)
```

设置已读回执

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function isDeliveryAcked

```cpp
bool isDeliveryAcked()
```

对于发送方表示消息是否已投递到对方，对于接收方表示是否发送了消息已到达回执

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setIsDeliveryAcked

```cpp
void setIsDeliveryAcked(
    bool 
)
```

设置投递回执

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function content

```cpp
const std::string & content()
```

消息文本内容

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setContent

```cpp
void setContent(
    const std::string & content
)
```

消息文本内容

**Parameters**:

* **content** 消息文本内容

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function contentType

```cpp
ContentType contentType()
```

消息内容类型，如果带附件就表示附件类型，不带附件就是文本类型

**Return**: ContentType

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function attachment

```cpp
BMXMessageAttachmentPtr attachment()
```

消息附件，BMXMessage拥有附件的所有权，负责释放

**Return**: BMXMessageAttachmentPtr

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function config

```cpp
BMXMessageConfigPtr config()
```

消息的配置信息

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setConfig

```cpp
void setConfig(
    BMXMessageConfigPtr 
)
```

设置消息配置信息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function extension

```cpp
const JSON & extension()
```

消息扩展信息

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setExtension

```cpp
void setExtension(
    const JSON & 
)
```

设置消息扩展信息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function deliveryQos

```cpp
DeliveryQos deliveryQos()
```

消息投递QOS

**Return**: DeliveryQos

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setDeliveryQos

```cpp
void setDeliveryQos(
    DeliveryQos qos
)
```

设置消息投递QOS

**Parameters**:

* **qos** 消息投递QOS

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function senderName

```cpp
const std::string & senderName()
```

消息发送者的显示名称

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setSenderName

```cpp
void setSenderName(
    const std::string & senderName
)
```

设置消息的发送者显示名称

**Parameters**:

* **senderName** 消息文本内容

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function groupAckCount

```cpp
int groupAckCount()
```

群消息已读AckCount数目

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setGroupAckCount

```cpp
void setGroupAckCount(
    int count
)
```

设置消息已读groupAckCount数目(SDK 内部调用接口，上层不应该调用)

**Parameters**:

* **count** 设置群消息已读数目

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function groupAckUnreadCount

```cpp
int groupAckUnreadCount()
```

群消息未读AckCount数目

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setGroupAckUnreadCount

```cpp
void setGroupAckUnreadCount(
    int count
)
```

设置消息未读groupAckCount数目(SDK 内部调用接口，上层不应该调用)

**Parameters**:

* **count** 设置群消息未读数目

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function groupAckReadAll

```cpp
bool groupAckReadAll()
```

群消息是否全部已读

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function groupPlayAckCount

```cpp
int groupPlayAckCount()
```

群消息已播放AckCount数目（仅用于音频/视频附件消息）

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setGroupPlayAckCount

```cpp
void setGroupPlayAckCount(
    int count
)
```

设置消息已播放groupAckCount数目(SDK 内部调用接口，上层不应该调用)（仅用于音频/视频附件消息）

**Parameters**:

* **count** 设置群消息已读数目

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function groupPlayAckUnreadCount

```cpp
int groupPlayAckUnreadCount()
```

群消息未播放AckCount数目（仅用于音频/视频附件消息）

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setGroupPlayAckUnreadCount

```cpp
void setGroupPlayAckUnreadCount(
    int count
)
```

设置消息未播放groupAckCount数目(SDK 内部调用接口，上层不应该调用)（仅用于音频/视频附件消息）

**Parameters**:

* **count** 设置群消息未播放数目

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function groupPlayAckReadAll

```cpp
bool groupPlayAckReadAll()
```

群消息是否全部已播放

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function priority

```cpp
int priority()
```

消息的扩散优先级

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function setPushMessageMode

```cpp
void setPushMessageMode(
    bool 
)
```

设置消息是否为推送消息。

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

### function isPushMessage

```cpp
bool isPushMessage()
```

消息是否是推送消息

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
