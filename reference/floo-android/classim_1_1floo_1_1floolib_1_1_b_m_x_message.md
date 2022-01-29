---
title: im::floo::floolib::BMXMessage
summary: 消息 

---

# im::floo::floolib::BMXMessage



消息 

Inherits from BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-delete)**() |
| long | **[msgId](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-msgid)**()<br>消息唯一ID  |
| long | **[clientMsgId](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-clientmsgid)**()<br>消息客户端ID,仅在消息发送端存在  |
| long | **[fromId](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-fromid)**()<br>消息发送方ID  |
| long | **[toId](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-toid)**()<br>消息接收方ID  |
| BMXMessage.MessageType | **[type](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-type)**()<br>消息类型  |
| long | **[conversationId](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-conversationid)**()<br>消息所属会话ID  |
| BMXMessage.DeliveryStatus | **[deliveryStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-deliverystatus)**()<br>消息投递状态  |
| void | **[setDeliveryStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setdeliverystatus)**(BMXMessage.DeliveryStatus arg0)<br>设置消息投递状态  |
| long | **[serverTimestamp](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-servertimestamp)**()<br>消息时间戳（服务端收到时的时间）  |
| void | **[setServerTimestamp](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setservertimestamp)**(long arg0)<br>设置时间戳（服务端收到时的时间）  |
| long | **[clientTimestamp](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-clienttimestamp)**()<br>本地时间戳（消息创建或者收到时的本地时间）  |
| void | **[setClientTimestamp](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setclienttimestamp)**(long arg0)<br>设置消息本地时间戳  |
| boolean | **[isPlayed](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isplayed)**()<br>语音或者视频消息是否播放过，仅对收到的音视频消息有效  |
| void | **[setIsPlayed](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setisplayed)**(boolean arg0) |
| boolean | **[isPlayAcked](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isplayacked)**()<br>语音或者视频消息是否收到播放回执，仅对收到的音视频消息有效  |
| void | **[setIsPlayAcked](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setisplayacked)**(boolean arg0) |
| boolean | **[isReceiveMsg](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isreceivemsg)**()<br>是否接收的消息  |
| void | **[setIsReceiveMsg](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setisreceivemsg)**(boolean arg0) |
| boolean | **[isRead](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isread)**()<br>消息是否已读标志  |
| void | **[setIsRead](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setisread)**(boolean arg0) |
| boolean | **[isReadAcked](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isreadacked)**()<br>对于发送方表示是否收到了已读回执，对于接收方表示是否发送了已读回执  |
| void | **[setIsReadAcked](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setisreadacked)**(boolean arg0) |
| boolean | **[isDeliveryAcked](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isdeliveryacked)**()<br>对于发送方表示消息是否已投递到对方，对于接收方表示是否发送了消息已到达回执  |
| void | **[setIsDeliveryAcked](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setisdeliveryacked)**(boolean arg0) |
| String | **[content](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-content)**()<br>消息文本内容  |
| void | **[setContent](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setcontent)**(String content)<br>消息文本内容  |
| BMXMessage.ContentType | **[contentType](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-contenttype)**()<br>消息内容类型，如果带附件就表示附件类型，不带附件就是文本类型  |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | **[attachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-attachment)**()<br>消息附件，BMXMessage拥有附件的所有权，负责释放  |
| [BMXMessageConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md) | **[config](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-config)**()<br>消息的配置信息  |
| void | **[setConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setconfig)**([BMXMessageConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md) arg0)<br>设置消息配置信息  |
| String | **[extension](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-extension)**()<br>消息扩展信息  |
| void | **[setExtension](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setextension)**(String arg0)<br>设置消息扩展信息  |
| BMXMessage.DeliveryQos | **[deliveryQos](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-deliveryqos)**()<br>消息投递QOS  |
| void | **[setDeliveryQos](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setdeliveryqos)**(BMXMessage.DeliveryQos qos)<br>设置消息投递QOS  |
| String | **[senderName](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-sendername)**()<br>消息发送者的显示名称  |
| void | **[setSenderName](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setsendername)**(String senderName)<br>设置消息的发送者显示名称  |
| int | **[groupAckCount](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupackcount)**()<br>群消息已读AckCount数目  |
| void | **[setGroupAckCount](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setgroupackcount)**(int count)<br>设置消息已读groupAckCount数目(SDK 内部调用接口，上层不应该调用)  |
| int | **[groupAckUnreadCount](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupackunreadcount)**()<br>群消息未读AckCount数目  |
| void | **[setGroupAckUnreadCount](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setgroupackunreadcount)**(int count)<br>设置消息未读groupAckCount数目(SDK 内部调用接口，上层不应该调用)  |
| boolean | **[groupAckReadAll](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupackreadall)**()<br>群消息是否全部已读  |
| int | **[groupPlayAckCount](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupplayackcount)**()<br>获取群消息已播放计数  |
| void | **[setGroupPlayAckCount](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setgroupplayackcount)**(int count) |
| int | **[groupPlayAckUnreadCount](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupplayackunreadcount)**()<br>获取群消息已播放回执未读计数  |
| void | **[setGroupPlayAckUnreadCount](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setgroupplayackunreadcount)**(int count) |
| boolean | **[groupPlayAckReadAll](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupplayackreadall)**()<br>设置所有群消息已播回执为已读  |
| void | **[setPriority](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setpriority)**(int priority)<br>设置消息的扩散优先级，默认为0。0表示扩散，数字越小扩散的越多。 取值范围0-10。普通人在聊天室发送的消息级别默认为5，可以丢弃。管理员默认为0不会丢弃。其它值可以根据业务自行设置。  |
| int | **[priority](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-priority)**()<br>消息的扩散优先级  |
| void | **[setPushMessageMode](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setpushmessagemode)**(boolean arg0)<br>设置是否推送消息  |
| boolean | **[isPushMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-ispushmessage)**()<br>是否是推送消息  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) | **[createMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createmessage)**(long from, long to, BMXMessage.MessageType type, long conversationId, String content)<br>创建发送文本消息  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) | **[createMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createmessage)**(long from, long to, BMXMessage.MessageType type, long conversationId, [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) attachment)<br>创建发送附件消息  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) | **[createCommandMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createcommandmessage)**(long from, long to, BMXMessage.MessageType type, long conversationId, String content)<br>创建发送命令消息(命令消息通过content字段或者extension字段存放命令信息)  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) | **[createMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createmessage)**(long msgId, long from, long to, BMXMessage.MessageType type, long conversationId, String content, long serverTimestamp)<br>创建收到的消息  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) | **[createMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createmessage)**(long msgId, long from, long to, BMXMessage.MessageType type, long conversationId, [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) attachment, long serverTimestamp)<br>创建收到的消息  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) | **[createCommandMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createcommandmessage)**(long msgId, long from, long to, BMXMessage.MessageType type, long conversationId, String content, long serverTimestamp)<br>创建收到的命令消息(命令消息通过content字段或者extension字段存放命令信息)  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) | **[createForwardMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createforwardmessage)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, long from, long to, BMXMessage.MessageType type, long conversationId)<br>创建转发消息  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-bmxmessage)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-getcptr)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) obj) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


### function msgId

```java
inline long msgId()
```

消息唯一ID 

**Return**: int64_t 

### function clientMsgId

```java
inline long clientMsgId()
```

消息客户端ID,仅在消息发送端存在 

**Return**: int64_t 

### function fromId

```java
inline long fromId()
```

消息发送方ID 

**Return**: int64_t 

### function toId

```java
inline long toId()
```

消息接收方ID 

**Return**: int64_t 

### function type

```java
inline BMXMessage.MessageType type()
```

消息类型 

**Return**: [MessageType]

### function conversationId

```java
inline long conversationId()
```

消息所属会话ID 

**Return**: int64_t 

### function deliveryStatus

```java
inline BMXMessage.DeliveryStatus deliveryStatus()
```

消息投递状态 

**Return**: [DeliveryStatus]

### function setDeliveryStatus

```java
inline void setDeliveryStatus(
    BMXMessage.DeliveryStatus arg0
)
```

设置消息投递状态 

### function serverTimestamp

```java
inline long serverTimestamp()
```

消息时间戳（服务端收到时的时间） 

**Return**: int64_t 

### function setServerTimestamp

```java
inline void setServerTimestamp(
    long arg0
)
```

设置时间戳（服务端收到时的时间） 

### function clientTimestamp

```java
inline long clientTimestamp()
```

本地时间戳（消息创建或者收到时的本地时间） 

**Return**: int64_t 

### function setClientTimestamp

```java
inline void setClientTimestamp(
    long arg0
)
```

设置消息本地时间戳 

### function isPlayed

```java
inline boolean isPlayed()
```

语音或者视频消息是否播放过，仅对收到的音视频消息有效 

**Return**: bool 

### function setIsPlayed

```java
inline void setIsPlayed(
    boolean arg0
)
```


### function isPlayAcked

```java
inline boolean isPlayAcked()
```

语音或者视频消息是否收到播放回执，仅对收到的音视频消息有效 

**Return**: bool 

### function setIsPlayAcked

```java
inline void setIsPlayAcked(
    boolean arg0
)
```


### function isReceiveMsg

```java
inline boolean isReceiveMsg()
```

是否接收的消息 

**Return**: bool 

### function setIsReceiveMsg

```java
inline void setIsReceiveMsg(
    boolean arg0
)
```


### function isRead

```java
inline boolean isRead()
```

消息是否已读标志 

**Return**: bool 

### function setIsRead

```java
inline void setIsRead(
    boolean arg0
)
```


### function isReadAcked

```java
inline boolean isReadAcked()
```

对于发送方表示是否收到了已读回执，对于接收方表示是否发送了已读回执 

**Return**: bool 

### function setIsReadAcked

```java
inline void setIsReadAcked(
    boolean arg0
)
```


### function isDeliveryAcked

```java
inline boolean isDeliveryAcked()
```

对于发送方表示消息是否已投递到对方，对于接收方表示是否发送了消息已到达回执 

**Return**: bool 

### function setIsDeliveryAcked

```java
inline void setIsDeliveryAcked(
    boolean arg0
)
```


### function content

```java
inline String content()
```

消息文本内容 

**Return**: std::string 

### function setContent

```java
inline void setContent(
    String content
)
```

消息文本内容 

**Parameters**: 

  * **content** 消息文本内容 


### function contentType

```java
inline BMXMessage.ContentType contentType()
```

消息内容类型，如果带附件就表示附件类型，不带附件就是文本类型 

**Return**: [ContentType]

### function attachment

```java
inline BMXMessageAttachment attachment()
```

消息附件，BMXMessage拥有附件的所有权，负责释放 

**Return**: BMXMessageAttachmentPtr 

### function config

```java
inline BMXMessageConfig config()
```

消息的配置信息 

**Return**: JSON(std::string) 

### function setConfig

```java
inline void setConfig(
    BMXMessageConfig arg0
)
```

设置消息配置信息 

### function extension

```java
inline String extension()
```

消息扩展信息 

**Return**: JSON(std::string) 

### function setExtension

```java
inline void setExtension(
    String arg0
)
```

设置消息扩展信息 

### function deliveryQos

```java
inline BMXMessage.DeliveryQos deliveryQos()
```

消息投递QOS 

**Return**: [DeliveryQos]

### function setDeliveryQos

```java
inline void setDeliveryQos(
    BMXMessage.DeliveryQos qos
)
```

设置消息投递QOS 

**Parameters**: 

  * **qos** 消息投递QOS 


### function senderName

```java
inline String senderName()
```

消息发送者的显示名称 

**Return**: std::string 

### function setSenderName

```java
inline void setSenderName(
    String senderName
)
```

设置消息的发送者显示名称 

**Parameters**: 

  * **senderName** 消息文本内容 


### function groupAckCount

```java
inline int groupAckCount()
```

群消息已读AckCount数目 

**Return**: int 

### function setGroupAckCount

```java
inline void setGroupAckCount(
    int count
)
```

设置消息已读groupAckCount数目(SDK 内部调用接口，上层不应该调用) 

**Parameters**: 

  * **count** 设置群消息已读数目 


### function groupAckUnreadCount

```java
inline int groupAckUnreadCount()
```

群消息未读AckCount数目 

**Return**: int 

### function setGroupAckUnreadCount

```java
inline void setGroupAckUnreadCount(
    int count
)
```

设置消息未读groupAckCount数目(SDK 内部调用接口，上层不应该调用) 

**Parameters**: 

  * **count** 设置群消息未读数目 


### function groupAckReadAll

```java
inline boolean groupAckReadAll()
```

群消息是否全部已读 

**Return**: bool 

### function groupPlayAckCount

```java
inline int groupPlayAckCount()
```

获取群消息已播放计数 

**Return**: bool 

### function setGroupPlayAckCount

```java
inline void setGroupPlayAckCount(
    int count
)
```


### function groupPlayAckUnreadCount

```java
inline int groupPlayAckUnreadCount()
```

获取群消息已播放回执未读计数 

**Return**: bool 

### function setGroupPlayAckUnreadCount

```java
inline void setGroupPlayAckUnreadCount(
    int count
)
```


### function groupPlayAckReadAll

```java
inline boolean groupPlayAckReadAll()
```

设置所有群消息已播回执为已读 

**Return**: bool 

### function setPriority

```java
inline void setPriority(
    int priority
)
```

设置消息的扩散优先级，默认为0。0表示扩散，数字越小扩散的越多。 取值范围0-10。普通人在聊天室发送的消息级别默认为5，可以丢弃。管理员默认为0不会丢弃。其它值可以根据业务自行设置。 

**Parameters**: 

  * **priority** 设置群消息未读数目 


### function priority

```java
inline int priority()
```

消息的扩散优先级 

**Return**: int 

### function setPushMessageMode

```java
inline void setPushMessageMode(
    boolean arg0
)
```

设置是否推送消息 

### function isPushMessage

```java
inline boolean isPushMessage()
```

是否是推送消息 

**Return**: boolean 

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

### function BMXMessage

```java
inline BMXMessage(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
```


### function getCPtr

```java
static inline long getCPtr(
    BMXMessage obj
)
```


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800