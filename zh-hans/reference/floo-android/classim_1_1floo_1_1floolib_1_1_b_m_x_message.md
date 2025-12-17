---
title: im::floo::floolib::BMXMessage
summary: 消息
---

# im::floo::floolib::BMXMessage

消息

Inherits from BMXBaseObject

## Public Functions

|                                                                                    | Name                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void                                                                  | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-delete)()                                                                                                                                                                                                                                                                         |
| long                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-msgid"><strong>msgId</strong></a>()<br>消息唯一ID</p>                                                                                                                                                                                                                                  |
| long                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-clientmsgid"><strong>clientMsgId</strong></a>()<br>消息客户端ID,仅在消息发送端存在</p>                                                                                                                                                                                                           |
| long                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-fromid"><strong>fromId</strong></a>()<br>消息发送方ID</p>                                                                                                                                                                                                                               |
| long                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-toid"><strong>toId</strong></a>()<br>消息接收方ID</p>                                                                                                                                                                                                                                   |
| BMXMessage.MessageType                                                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-type"><strong>type</strong></a>()<br>消息类型</p>                                                                                                                                                                                                                                      |
| long                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-conversationid"><strong>conversationId</strong></a>()<br>消息所属会话ID</p>                                                                                                                                                                                                              |
| BMXMessage.DeliveryStatus                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-deliverystatus"><strong>deliveryStatus</strong></a>()<br>消息投递状态</p>                                                                                                                                                                                                                |
| void                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setdeliverystatus"><strong>setDeliveryStatus</strong></a>(BMXMessage.DeliveryStatus arg0)<br>设置消息投递状态</p>                                                                                                                                                                          |
| long                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-servertimestamp"><strong>serverTimestamp</strong></a>()<br>消息时间戳（服务端收到时的时间）</p>                                                                                                                                                                                                    |
| void                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setservertimestamp"><strong>setServerTimestamp</strong></a>(long arg0)<br>设置时间戳（服务端收到时的时间）</p>                                                                                                                                                                                     |
| long                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-clienttimestamp"><strong>clientTimestamp</strong></a>()<br>本地时间戳（消息创建或者收到时的本地时间）</p>                                                                                                                                                                                               |
| void                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setclienttimestamp"><strong>setClientTimestamp</strong></a>(long arg0)<br>设置消息本地时间戳</p>                                                                                                                                                                                            |
| boolean                                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isplayed"><strong>isPlayed</strong></a>()<br>语音或者视频消息是否播放过，仅对收到的音视频消息有效</p>                                                                                                                                                                                                        |
| void                                                                               | [**setIsPlayed**](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setisplayed)(boolean arg0)                                                                                                                                                                                                                                                   |
| boolean                                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isplayacked"><strong>isPlayAcked</strong></a>()<br>语音或者视频消息是否收到播放回执，仅对收到的音视频消息有效</p>                                                                                                                                                                                               |
| void                                                                               | [**setIsPlayAcked**](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setisplayacked)(boolean arg0)                                                                                                                                                                                                                                             |
| boolean                                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isreceivemsg"><strong>isReceiveMsg</strong></a>()<br>是否接收的消息</p>                                                                                                                                                                                                                   |
| void                                                                               | [**setIsReceiveMsg**](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setisreceivemsg)(boolean arg0)                                                                                                                                                                                                                                           |
| boolean                                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isread"><strong>isRead</strong></a>()<br>消息是否已读标志</p>                                                                                                                                                                                                                              |
| void                                                                               | [**setIsRead**](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setisread)(boolean arg0)                                                                                                                                                                                                                                                       |
| boolean                                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isreadacked"><strong>isReadAcked</strong></a>()<br>对于发送方表示是否收到了已读回执，对于接收方表示是否发送了已读回执</p>                                                                                                                                                                                           |
| void                                                                               | [**setIsReadAcked**](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setisreadacked)(boolean arg0)                                                                                                                                                                                                                                             |
| boolean                                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isdeliveryacked"><strong>isDeliveryAcked</strong></a>()<br>对于发送方表示消息是否已投递到对方，对于接收方表示是否发送了消息已到达回执</p>                                                                                                                                                                               |
| void                                                                               | [**setIsDeliveryAcked**](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setisdeliveryacked)(boolean arg0)                                                                                                                                                                                                                                     |
| String                                                                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-content"><strong>content</strong></a>()<br>消息文本内容</p>                                                                                                                                                                                                                              |
| void                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setcontent"><strong>setContent</strong></a>(String content)<br>消息文本内容</p>                                                                                                                                                                                                          |
| BMXMessage.ContentType                                                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-contenttype"><strong>contentType</strong></a>()<br>消息内容类型，如果带附件就表示附件类型，不带附件就是文本类型</p>                                                                                                                                                                                              |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-attachment"><strong>attachment</strong></a>()<br>消息附件，BMXMessage拥有附件的所有权，负责释放</p>                                                                                                                                                                                                  |
| [BMXMessageConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md)         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-config"><strong>config</strong></a>()<br>消息的配置信息</p>                                                                                                                                                                                                                               |
| void                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setconfig"><strong>setConfig</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md">BMXMessageConfig</a> arg0)<br>设置消息配置信息</p>                                                                                                                              |
| String                                                                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-extension"><strong>extension</strong></a>()<br>消息扩展信息</p>                                                                                                                                                                                                                          |
| void                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setextension"><strong>setExtension</strong></a>(String arg0)<br>设置消息扩展信息</p>                                                                                                                                                                                                       |
| BMXMessage.DeliveryQos                                                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-deliveryqos"><strong>deliveryQos</strong></a>()<br>消息投递QOS</p>                                                                                                                                                                                                                     |
| void                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setdeliveryqos"><strong>setDeliveryQos</strong></a>(BMXMessage.DeliveryQos qos)<br>设置消息投递QOS</p>                                                                                                                                                                                   |
| String                                                                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-sendername"><strong>senderName</strong></a>()<br>消息发送者的显示名称</p>                                                                                                                                                                                                                    |
| void                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setsendername"><strong>setSenderName</strong></a>(String senderName)<br>设置消息的发送者显示名称</p>                                                                                                                                                                                           |
| int                                                                                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupackcount"><strong>groupAckCount</strong></a>()<br>群消息已读AckCount数目</p>                                                                                                                                                                                                         |
| void                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setgroupackcount"><strong>setGroupAckCount</strong></a>(int count)<br>设置消息已读groupAckCount数目(SDK 内部调用接口，上层不应该调用)</p>                                                                                                                                                                |
| int                                                                                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupackunreadcount"><strong>groupAckUnreadCount</strong></a>()<br>群消息未读AckCount数目</p>                                                                                                                                                                                             |
| void                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setgroupackunreadcount"><strong>setGroupAckUnreadCount</strong></a>(int count)<br>设置消息未读groupAckCount数目(SDK 内部调用接口，上层不应该调用)</p>                                                                                                                                                    |
| boolean                                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupackreadall"><strong>groupAckReadAll</strong></a>()<br>群消息是否全部已读</p>                                                                                                                                                                                                           |
| int                                                                                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupplayackcount"><strong>groupPlayAckCount</strong></a>()<br>获取群消息已播放计数</p>                                                                                                                                                                                                      |
| void                                                                               | [**setGroupPlayAckCount**](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setgroupplayackcount)(int count)                                                                                                                                                                                                                                    |
| int                                                                                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupplayackunreadcount"><strong>groupPlayAckUnreadCount</strong></a>()<br>获取群消息已播放回执未读计数</p>                                                                                                                                                                                      |
| void                                                                               | [**setGroupPlayAckUnreadCount**](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setgroupplayackunreadcount)(int count)                                                                                                                                                                                                                        |
| boolean                                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupplayackreadall"><strong>groupPlayAckReadAll</strong></a>()<br>设置所有群消息已播回执为已读</p>                                                                                                                                                                                              |
| void                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setpriority"><strong>setPriority</strong></a>(int priority)<br>设置消息的扩散优先级，默认为0。0表示扩散，数字越小扩散的越多。 取值范围0-10。普通人在聊天室发送的消息级别默认为5，可以丢弃。管理员默认为0不会丢弃。其它值可以根据业务自行设置。</p>                                                                                                                    |
| int                                                                                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-priority"><strong>priority</strong></a>()<br>消息的扩散优先级</p>                                                                                                                                                                                                                          |
| void                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setpushmessagemode"><strong>setPushMessageMode</strong></a>(boolean arg0)<br>设置是否推送消息</p>                                                                                                                                                                                          |
| boolean                                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-ispushmessage"><strong>isPushMessage</strong></a>()<br>是否是推送消息</p>                                                                                                                                                                                                                 |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md)                      | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createmessage"><strong>createMessage</strong></a>(long from, long to, BMXMessage.MessageType type, long conversationId, String content)<br>创建发送文本消息</p>                                                                                                                            |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md)                      | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createmessage"><strong>createMessage</strong></a>(long from, long to, BMXMessage.MessageType type, long conversationId, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md">BMXMessageAttachment</a> attachment)<br>创建发送附件消息</p>                                  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md)                      | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createcommandmessage"><strong>createCommandMessage</strong></a>(long from, long to, BMXMessage.MessageType type, long conversationId, String content)<br>创建发送命令消息(命令消息通过content字段或者extension字段存放命令信息)</p>                                                                          |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md)                      | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createmessage"><strong>createMessage</strong></a>(long msgId, long from, long to, BMXMessage.MessageType type, long conversationId, String content, long serverTimestamp)<br>创建收到的消息</p>                                                                                           |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md)                      | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createmessage"><strong>createMessage</strong></a>(long msgId, long from, long to, BMXMessage.MessageType type, long conversationId, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md">BMXMessageAttachment</a> attachment, long serverTimestamp)<br>创建收到的消息</p> |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md)                      | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createcommandmessage"><strong>createCommandMessage</strong></a>(long msgId, long from, long to, BMXMessage.MessageType type, long conversationId, String content, long serverTimestamp)<br>创建收到的命令消息(命令消息通过content字段或者extension字段存放命令信息)</p>                                       |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md)                      | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createforwardmessage"><strong>createForwardMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, long from, long to, BMXMessage.MessageType type, long conversationId)<br>创建转发消息</p>                                                  |

## Protected Functions

|      | Name                                                                                                                                               |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXMessage**](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-bmxmessage)(long cPtr, boolean cMemoryOwn)                               |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-finalize)()                                                                |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-getcptr)([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) obj) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function msgId

```java
inline long msgId()
```

消息唯一ID

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function clientMsgId

```java
inline long clientMsgId()
```

消息客户端ID,仅在消息发送端存在

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function fromId

```java
inline long fromId()
```

消息发送方ID

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function toId

```java
inline long toId()
```

消息接收方ID

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function type

```java
inline BMXMessage.MessageType type()
```

消息类型

**Return**: \[MessageType]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function conversationId

```java
inline long conversationId()
```

消息所属会话ID

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function deliveryStatus

```java
inline BMXMessage.DeliveryStatus deliveryStatus()
```

消息投递状态

**Return**: \[DeliveryStatus]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setDeliveryStatus

```java
inline void setDeliveryStatus(
    BMXMessage.DeliveryStatus arg0
)
```

设置消息投递状态

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function serverTimestamp

```java
inline long serverTimestamp()
```

消息时间戳（服务端收到时的时间）

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setServerTimestamp

```java
inline void setServerTimestamp(
    long arg0
)
```

设置时间戳（服务端收到时的时间）

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function clientTimestamp

```java
inline long clientTimestamp()
```

本地时间戳（消息创建或者收到时的本地时间）

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setClientTimestamp

```java
inline void setClientTimestamp(
    long arg0
)
```

设置消息本地时间戳

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function isPlayed

```java
inline boolean isPlayed()
```

语音或者视频消息是否播放过，仅对收到的音视频消息有效

**Return**: bool

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setIsPlayed

```java
inline void setIsPlayed(
    boolean arg0
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function isPlayAcked

```java
inline boolean isPlayAcked()
```

语音或者视频消息是否收到播放回执，仅对收到的音视频消息有效

**Return**: bool

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setIsPlayAcked

```java
inline void setIsPlayAcked(
    boolean arg0
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function isReceiveMsg

```java
inline boolean isReceiveMsg()
```

是否接收的消息

**Return**: bool

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setIsReceiveMsg

```java
inline void setIsReceiveMsg(
    boolean arg0
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function isRead

```java
inline boolean isRead()
```

消息是否已读标志

**Return**: bool

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setIsRead

```java
inline void setIsRead(
    boolean arg0
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function isReadAcked

```java
inline boolean isReadAcked()
```

对于发送方表示是否收到了已读回执，对于接收方表示是否发送了已读回执

**Return**: bool

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setIsReadAcked

```java
inline void setIsReadAcked(
    boolean arg0
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function isDeliveryAcked

```java
inline boolean isDeliveryAcked()
```

对于发送方表示消息是否已投递到对方，对于接收方表示是否发送了消息已到达回执

**Return**: bool

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setIsDeliveryAcked

```java
inline void setIsDeliveryAcked(
    boolean arg0
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function content

```java
inline String content()
```

消息文本内容

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setContent

```java
inline void setContent(
    String content
)
```

消息文本内容

**Parameters**:

* **content** 消息文本内容

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function contentType

```java
inline BMXMessage.ContentType contentType()
```

消息内容类型，如果带附件就表示附件类型，不带附件就是文本类型

**Return**: \[ContentType]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function attachment

```java
inline BMXMessageAttachment attachment()
```

消息附件，BMXMessage拥有附件的所有权，负责释放

**Return**: BMXMessageAttachmentPtr

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function config

```java
inline BMXMessageConfig config()
```

消息的配置信息

**Return**: JSON(std::string)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setConfig

```java
inline void setConfig(
    BMXMessageConfig arg0
)
```

设置消息配置信息

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function extension

```java
inline String extension()
```

消息扩展信息

**Return**: JSON(std::string)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setExtension

```java
inline void setExtension(
    String arg0
)
```

设置消息扩展信息

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function deliveryQos

```java
inline BMXMessage.DeliveryQos deliveryQos()
```

消息投递QOS

**Return**: \[DeliveryQos]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setDeliveryQos

```java
inline void setDeliveryQos(
    BMXMessage.DeliveryQos qos
)
```

设置消息投递QOS

**Parameters**:

* **qos** 消息投递QOS

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function senderName

```java
inline String senderName()
```

消息发送者的显示名称

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setSenderName

```java
inline void setSenderName(
    String senderName
)
```

设置消息的发送者显示名称

**Parameters**:

* **senderName** 消息文本内容

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function groupAckCount

```java
inline int groupAckCount()
```

群消息已读AckCount数目

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setGroupAckCount

```java
inline void setGroupAckCount(
    int count
)
```

设置消息已读groupAckCount数目(SDK 内部调用接口，上层不应该调用)

**Parameters**:

* **count** 设置群消息已读数目

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function groupAckUnreadCount

```java
inline int groupAckUnreadCount()
```

群消息未读AckCount数目

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setGroupAckUnreadCount

```java
inline void setGroupAckUnreadCount(
    int count
)
```

设置消息未读groupAckCount数目(SDK 内部调用接口，上层不应该调用)

**Parameters**:

* **count** 设置群消息未读数目

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function groupAckReadAll

```java
inline boolean groupAckReadAll()
```

群消息是否全部已读

**Return**: bool

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function groupPlayAckCount

```java
inline int groupPlayAckCount()
```

获取群消息已播放计数

**Return**: bool

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setGroupPlayAckCount

```java
inline void setGroupPlayAckCount(
    int count
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function groupPlayAckUnreadCount

```java
inline int groupPlayAckUnreadCount()
```

获取群消息已播放回执未读计数

**Return**: bool

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setGroupPlayAckUnreadCount

```java
inline void setGroupPlayAckUnreadCount(
    int count
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function groupPlayAckReadAll

```java
inline boolean groupPlayAckReadAll()
```

设置所有群消息已播回执为已读

**Return**: bool

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setPriority

```java
inline void setPriority(
    int priority
)
```

设置消息的扩散优先级，默认为0。0表示扩散，数字越小扩散的越多。 取值范围0-10。普通人在聊天室发送的消息级别默认为5，可以丢弃。管理员默认为0不会丢弃。其它值可以根据业务自行设置。

**Parameters**:

* **priority** 优先级

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function priority

```java
inline int priority()
```

消息的扩散优先级

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function setPushMessageMode

```java
inline void setPushMessageMode(
    boolean arg0
)
```

设置是否推送消息

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function isPushMessage

```java
inline boolean isPushMessage()
```

是否是推送消息

**Return**: boolean

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function createMessage

```java
static inline BMXMessage createMessage(
    long from,
    long to,
    BMXMessage.MessageType type,
    long conversationId,
    String content
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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function createMessage

```java
static inline BMXMessage createMessage(
    long from,
    long to,
    BMXMessage.MessageType type,
    long conversationId,
    BMXMessageAttachment attachment
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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function createCommandMessage

```java
static inline BMXMessage createCommandMessage(
    long from,
    long to,
    BMXMessage.MessageType type,
    long conversationId,
    String content
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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function createMessage

```java
static inline BMXMessage createMessage(
    long msgId,
    long from,
    long to,
    BMXMessage.MessageType type,
    long conversationId,
    String content,
    long serverTimestamp
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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function createMessage

```java
static inline BMXMessage createMessage(
    long msgId,
    long from,
    long to,
    BMXMessage.MessageType type,
    long conversationId,
    BMXMessageAttachment attachment,
    long serverTimestamp
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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function createCommandMessage

```java
static inline BMXMessage createCommandMessage(
    long msgId,
    long from,
    long to,
    BMXMessage.MessageType type,
    long conversationId,
    String content,
    long serverTimestamp
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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function createForwardMessage

```java
static inline BMXMessage createForwardMessage(
    BMXMessage msg,
    long from,
    long to,
    BMXMessage.MessageType type,
    long conversationId
)
```

创建转发消息

**Parameters**:

* **msg** 要转发的消息
* **from** 消息发送者
* **to** 消息接收者
* **type** 消息类型
* **conversationId** 会话id

## Protected Functions Documentation

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function BMXMessage

```java
inline BMXMessage(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function finalize

```java
inline void finalize()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>

```

### function getCPtr

```java
static inline long getCPtr(
    BMXMessage obj
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

***

Updated on 2022-01-26 at 17:18:31 +0800
