---
title: im::floo::floolib::BMXMessage
summary: Message 

---

# im::floo::floolib::BMXMessage



Message 

Inherits from BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-delete)**() |
| long | **[msgId](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-msgid)**()<br>Message unique ID  |
| long | **[clientMsgId](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-clientmsgid)**()<br>Message client ID, only exists on message sender-side  |
| long | **[fromId](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-fromid)**()<br>Message sender ID  |
| long | **[toId](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-toid)**()<br>Message receiver ID  |
| BMXMessage.MessageType | **[type](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-type)**()<br>Message type  |
| long | **[conversationId](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-conversationid)**()<br>Session ID that message belongs to  |
| BMXMessage.DeliveryStatus | **[deliveryStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-deliverystatus)**()<br>Messaging state  |
| void | **[setDeliveryStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setdeliverystatus)**(BMXMessage.DeliveryStatus arg0)<br>Set messaging state  |
| long | **[serverTimestamp](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-servertimestamp)**()<br>Message timestamp (when received by server-side)  |
| void | **[setServerTimestamp](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setservertimestamp)**(long arg0)<br>Set message timestamp (when received by server-side)  |
| long | **[clientTimestamp](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-clienttimestamp)**()<br>Local timestamp (local time when message created or received)  |
| void | **[setClientTimestamp](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setclienttimestamp)**(long arg0)<br>Set message local timestamp  |
| boolean | **[isPlayed](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isplayed)**()<br>Whether voice or video message has been played, valid only for received audio/video messages  |
| void | **[setIsPlayed](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setisplayed)**(boolean arg0) |
| boolean | **[isPlayAcked](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isplayacked)**()<br>Whether voice or video message receives a playback receipt, valid only for received audio/video messages  |
| void | **[setIsPlayAcked](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setisplayacked)**(boolean arg0) |
| boolean | **[isReceiveMsg](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isreceivemsg)**()<br>Message whether to receive  |
| void | **[setIsReceiveMsg](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setisreceivemsg)**(boolean arg0) |
| boolean | **[isRead](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isread)**()<br>Message read or unread mark  |
| void | **[setIsRead](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setisread)**(boolean arg0) |
| boolean | **[isReadAcked](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isreadacked)**()<br>Show sender whether read receipt received, and show receiver whether message read receipt sent  |
| void | **[setIsReadAcked](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setisreadacked)**(boolean arg0) |
| boolean | **[isDeliveryAcked](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isdeliveryacked)**()<br>Show sender whether message has been delivered to the other party, and show receiver whether message delivered receipt has been sent  |
| void | **[setIsDeliveryAcked](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setisdeliveryacked)**(boolean arg0) |
| String | **[content](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-content)**()<br>Message text content  |
| void | **[setContent](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setcontent)**(String content)<br>Message text content  |
| BMXMessage.ContentType | **[contentType](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-contenttype)**()<br>Message content type, attachment-type with attachment, text-type with no attachment  |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | **[attachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-attachment)**()<br>Message attachment, BMXMessage owns the attachment and is responsible for releasing it  |
| [BMXMessageConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md) | **[config](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-config)**()<br>Message settings  |
| void | **[setConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setconfig)**([BMXMessageConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md) arg0)<br>Set message config information  |
| String | **[extension](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-extension)**()<br>Message extension information  |
| void | **[setExtension](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setextension)**(String arg0)<br>Set message extension information  |
| BMXMessage.DeliveryQos | **[deliveryQos](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-deliveryqos)**()<br>QOS of messaging  |
| void | **[setDeliveryQos](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setdeliveryqos)**(BMXMessage.DeliveryQos qos)<br>Set QOS of messaging  |
| String | **[senderName](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-sendername)**()<br>Display name of message sender  |
| void | **[setSenderName](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setsendername)**(String senderName)<br>Set display name of message sender  |
| int | **[groupAckCount](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupackcount)**()<br>AckCount of read group messages  |
| void | **[setGroupAckCount](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setgroupackcount)**(int count)<br>Set groupAckCount of read messages (an SDK internal calling interface that shall not be called by upper layer)  |
| int | **[groupAckUnreadCount](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupackunreadcount)**()<br>AckCount of unread group messages  |
| void | **[setGroupAckUnreadCount](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setgroupackunreadcount)**(int count)<br>Set groupAckCount of unread messages (an SDK internal calling interface that shall not be called by upper layer)  |
| boolean | **[groupAckReadAll](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupackreadall)**()<br>Whether all group messages are read  |
| int | **[groupPlayAckCount](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupplayackcount)**()<br>Get count of played group messages  |
| void | **[setGroupPlayAckCount](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setgroupplayackcount)**(int count) |
| int | **[groupPlayAckUnreadCount](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupplayackunreadcount)**()<br>Get count of unread playback receipts of group messages  |
| void | **[setGroupPlayAckUnreadCount](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setgroupplayackunreadcount)**(int count) |
| boolean | **[groupPlayAckReadAll](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupplayackreadall)**()<br>Set all playback receipts of group messages as read  |
| void | **[setPriority](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setpriority)**(int priority)<br>Set message diffusion priority, default 0. 0 means diffusion, and the smaller the number, the more diffused. Value range 0-10. The default level of messages sent by ordinary users in chatroom is 5, which can be discarded. Admin level defaults to 0 and will not be discarded. Other values can be set according to business.  |
| int | **[priority](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-priority)**()<br>Message diffusion priority  |
| void | **[setPushMessageMode](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setpushmessagemode)**(boolean arg0)<br>Set whether to push messages  |
| boolean | **[isPushMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-ispushmessage)**()<br>Whether it is a push message  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) | **[createMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createmessage)**(long from, long to, BMXMessage.MessageType type, long conversationId, String content)<br>Create a text message  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) | **[createMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createmessage)**(long from, long to, BMXMessage.MessageType type, long conversationId, [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) attachment)<br>Create a sent-attachment message  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) | **[createCommandMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createcommandmessage)**(long from, long to, BMXMessage.MessageType type, long conversationId, String content)<br>Create a sent command message (command message holds command information in a content field or an extension field)  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) | **[createMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createmessage)**(long msgId, long from, long to, BMXMessage.MessageType type, long conversationId, String content, long serverTimestamp)<br>Create a received message  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) | **[createMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createmessage)**(long msgId, long from, long to, BMXMessage.MessageType type, long conversationId, [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) attachment, long serverTimestamp)<br>Create a received message  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) | **[createCommandMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createcommandmessage)**(long msgId, long from, long to, BMXMessage.MessageType type, long conversationId, String content, long serverTimestamp)<br>Create a received command message (command message holds command information in a content field or an extension field)  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) | **[createForwardMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createforwardmessage)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, long from, long to, BMXMessage.MessageType type, long conversationId)<br>Create a forwarding message  |

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

Message unique ID 

**Return**: int64_t 

### function clientMsgId

```java
inline long clientMsgId()
```

Message client ID, only exists on message sender-side 

**Return**: int64_t 

### function fromId

```java
inline long fromId()
```

Message sender ID 

**Return**: int64_t 

### function toId

```java
inline long toId()
```

Message receiver ID 

**Return**: int64_t 

### function type

```java
inline BMXMessage.MessageType type()
```

Message type 

**Return**: [MessageType]

### function conversationId

```java
inline long conversationId()
```

Session ID that message belongs to 

**Return**: int64_t 

### function deliveryStatus

```java
inline BMXMessage.DeliveryStatus deliveryStatus()
```

Messaging state 

**Return**: [DeliveryStatus]

### function setDeliveryStatus

```java
inline void setDeliveryStatus(
    BMXMessage.DeliveryStatus arg0
)
```

Set messaging state 

### function serverTimestamp

```java
inline long serverTimestamp()
```

Message timestamp (when received by server-side) 

**Return**: int64_t 

### function setServerTimestamp

```java
inline void setServerTimestamp(
    long arg0
)
```

Set message timestamp (when received by server-side) 

### function clientTimestamp

```java
inline long clientTimestamp()
```

Local timestamp (local time when message created or received) 

**Return**: int64_t 

### function setClientTimestamp

```java
inline void setClientTimestamp(
    long arg0
)
```

Set message local timestamp 

### function isPlayed

```java
inline boolean isPlayed()
```

Whether voice or video message has been played, valid only for received audio/video messages 

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

Whether voice or video message receives a playback receipt, valid only for received audio/video messages 

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

Message whether to receive 

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

Message read or unread mark 

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

Show sender whether read receipt received, and show receiver whether message read receipt sent 

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

Show sender whether message has been delivered to the other party, and show receiver whether message delivered receipt has been sent 

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

Message text content 

**Return**: std::string 

### function setContent

```java
inline void setContent(
    String content
)
```

Message text content 

**Parameters**: 

  * **content** Message text content 


### function contentType

```java
inline BMXMessage.ContentType contentType()
```

Message content type, attachment-type with attachment, text-type with no attachment 

**Return**: [ContentType]

### function attachment

```java
inline BMXMessageAttachment attachment()
```

Message attachment, BMXMessage owns the attachment and is responsible for releasing it 

**Return**: BMXMessageAttachmentPtr 

### function config

```java
inline BMXMessageConfig config()
```

Message settings 

**Return**: JSON(std::string) 

### function setConfig

```java
inline void setConfig(
    BMXMessageConfig arg0
)
```

Set message config information 

### function extension

```java
inline String extension()
```

Message extension information 

**Return**: JSON(std::string) 

### function setExtension

```java
inline void setExtension(
    String arg0
)
```

Set message extension information 

### function deliveryQos

```java
inline BMXMessage.DeliveryQos deliveryQos()
```

QOS of messaging 

**Return**: [DeliveryQos]

### function setDeliveryQos

```java
inline void setDeliveryQos(
    BMXMessage.DeliveryQos qos
)
```

Set QOS of messaging 

**Parameters**: 

  * **qos** QOS of messaging 


### function senderName

```java
inline String senderName()
```

Display name of message sender 

**Return**: std::string 

### function setSenderName

```java
inline void setSenderName(
    String senderName
)
```

Set display name of message sender 

**Parameters**: 

  * **senderName** Message text content 


### function groupAckCount

```java
inline int groupAckCount()
```

AckCount of read group messages 

**Return**: int 

### function setGroupAckCount

```java
inline void setGroupAckCount(
    int count
)
```

Set groupAckCount of read messages (an SDK internal calling interface that shall not be called by upper layer) 

**Parameters**: 

  * **count** Set the number of read group messages 


### function groupAckUnreadCount

```java
inline int groupAckUnreadCount()
```

AckCount of unread group messages 

**Return**: int 

### function setGroupAckUnreadCount

```java
inline void setGroupAckUnreadCount(
    int count
)
```

Set groupAckCount of unread messages (an SDK internal calling interface that shall not be called by upper layer) 

**Parameters**: 

  * **count** Set the number of unread group messages 


### function groupAckReadAll

```java
inline boolean groupAckReadAll()
```

Whether all group messages are read 

**Return**: bool 

### function groupPlayAckCount

```java
inline int groupPlayAckCount()
```

Get count of played group messages 

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

Get count of unread playback receipts of group messages 

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

Set all playback receipts of group messages as read 

**Return**: bool 

### function setPriority

```java
inline void setPriority(
    int priority
)
```

Set message diffusion priority, default 0. 0 means diffusion, and the smaller the number, the more diffused. Value range 0-10. The default level of messages sent by ordinary users in chatroom is 5, which can be discarded. Admin level defaults to 0 and will not be discarded. Other values can be set according to business. 

**Parameters**: 

  * **priority** Set the number of unread group messages 


### function priority

```java
inline int priority()
```

Message diffusion priority 

**Return**: int 

### function setPushMessageMode

```java
inline void setPushMessageMode(
    boolean arg0
)
```

Set whether to push messages 

### function isPushMessage

```java
inline boolean isPushMessage()
```

Whether it is a push message 

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

Create a text message 

**Parameters**: 

  * **from** Message sender 
  * **to** Message receiver 
  * **type** Message type 
  * **conversationId** Session id 
  * **content** Message content 


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

Create a sent-attachment message 

**Parameters**: 

  * **from** Message sender 
  * **to** Message receiver 
  * **type** Message type 
  * **conversationId** Session id 
  * **attachment** Attachment 


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

Create a sent command message (command message holds command information in a content field or an extension field) 

**Parameters**: 

  * **from** Message sender 
  * **to** Message receiver 
  * **type** Message type 
  * **conversationId** Session id 
  * **content** Message content 


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

Create a received message 

**Parameters**: 

  * **msgId** Message id 
  * **from** Message sender 
  * **to** Message receiver 
  * **type** Message type 
  * **conversationId** Session id 
  * **content** Message content 
  * **serverTimestamp** Server timestamp 


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

Create a received message 

**Parameters**: 

  * **msgId** Message id 
  * **from** Message sender 
  * **to** Message receiver 
  * **type** Message type 
  * **conversationId** Session id 
  * **attachment** Attachment 
  * **serverTimestamp** Server timestamp 


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

Create a received command message (command message holds command information in a content field or an extension field) 

**Parameters**: 

  * **msgId** Message id 
  * **from** Message sender 
  * **to** Message receiver 
  * **type** Message type 
  * **conversationId** Session id 
  * **content** Message content 
  * **serverTimestamp** Server timestamp 


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

Create a forwarding message 

**Parameters**: 

  * **msg** Message to forward 
  * **from** Message sender 
  * **to** Message receiver 
  * **type** Message type 
  * **conversationId** Session id 


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