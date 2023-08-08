---
title: im::floo::floolib::BMXMessage
summary: Message
---

# im::floo::floolib::BMXMessage

Message

Inherits from BMXBaseObject

## Public Functions

|                                                                                               | Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void                                                                             | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md#function-delete)()                                                                                                                                                                                                                                                                                                                                                                                 |
| long                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-msgid"><strong>msgId</strong></a>()<br>Message unique ID</p>                                                                                                                                                                                                                                                                                                                                         |
| long                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-clientmsgid"><strong>clientMsgId</strong></a>()<br>Message client ID, only exists on message sender-side</p>                                                                                                                                                                                                                                                                                         |
| long                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-fromid"><strong>fromId</strong></a>()<br>Message sender ID</p>                                                                                                                                                                                                                                                                                                                                       |
| long                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-toid"><strong>toId</strong></a>()<br>Message receiver ID</p>                                                                                                                                                                                                                                                                                                                                         |
| BMXMessage.MessageType                                                                        | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-type"><strong>type</strong></a>()<br>Message type</p>                                                                                                                                                                                                                                                                                                                                                |
| long                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-conversationid"><strong>conversationId</strong></a>()<br>Conversation ID that message belongs to</p>                                                                                                                                                                                                                                                                                                 |
| BMXMessage.DeliveryStatus                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-deliverystatus"><strong>deliveryStatus</strong></a>()<br>Messaging state</p>                                                                                                                                                                                                                                                                                                                         |
| void                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setdeliverystatus"><strong>setDeliveryStatus</strong></a>(BMXMessage.DeliveryStatus arg0)<br>Set messaging state</p>                                                                                                                                                                                                                                                                                 |
| long                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-servertimestamp"><strong>serverTimestamp</strong></a>()<br>Message timestamp (when received by server-side)</p>                                                                                                                                                                                                                                                                                      |
| void                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setservertimestamp"><strong>setServerTimestamp</strong></a>(long arg0)<br>Set message timestamp (when received by server-side)</p>                                                                                                                                                                                                                                                                   |
| long                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-clienttimestamp"><strong>clientTimestamp</strong></a>()<br>Local timestamp (local time when message created or received)</p>                                                                                                                                                                                                                                                                         |
| void                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setclienttimestamp"><strong>setClientTimestamp</strong></a>(long arg0)<br>Set message local timestamp</p>                                                                                                                                                                                                                                                                                            |
| boolean                                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isplayed"><strong>isPlayed</strong></a>()<br>Whether voice or video message has been played, valid only for received audio/video messages</p>                                                                                                                                                                                                                                                        |
| void                                                                                          | [**setIsPlayed**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md#function-setisplayed)(boolean arg0)                                                                                                                                                                                                                                                                                                                                                           |
| boolean                                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isplayacked"><strong>isPlayAcked</strong></a>()<br>Whether voice or video message receives a playback acknowledgement, valid only for received audio/video messages</p>                                                                                                                                                                                                                              |
| void                                                                                          | [**setIsPlayAcked**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md#function-setisplayacked)(boolean arg0)                                                                                                                                                                                                                                                                                                                                                     |
| boolean                                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isreceivemsg"><strong>isReceiveMsg</strong></a>()<br>Message whether to receive</p>                                                                                                                                                                                                                                                                                                                  |
| void                                                                                          | [**setIsReceiveMsg**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md#function-setisreceivemsg)(boolean arg0)                                                                                                                                                                                                                                                                                                                                                   |
| boolean                                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isread"><strong>isRead</strong></a>()<br>Message read or unread mark</p>                                                                                                                                                                                                                                                                                                                             |
| void                                                                                          | [**setIsRead**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md#function-setisread)(boolean arg0)                                                                                                                                                                                                                                                                                                                                                               |
| boolean                                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isreadacked"><strong>isReadAcked</strong></a>()<br>Show sender whether read acknowledgement received, and show receiver whether message read acknowledgement sent</p>                                                                                                                                                                                                                                |
| void                                                                                          | [**setIsReadAcked**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md#function-setisreadacked)(boolean arg0)                                                                                                                                                                                                                                                                                                                                                     |
| boolean                                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-isdeliveryacked"><strong>isDeliveryAcked</strong></a>()<br>Show sender whether message has been delivered to the other party, and show receiver whether message delivered acknowledgement has been sent</p>                                                                                                                                                                                          |
| void                                                                                          | [**setIsDeliveryAcked**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md#function-setisdeliveryacked)(boolean arg0)                                                                                                                                                                                                                                                                                                                                             |
| String                                                                                        | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-content"><strong>content</strong></a>()<br>Message text content</p>                                                                                                                                                                                                                                                                                                                                  |
| void                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setcontent"><strong>setContent</strong></a>(String content)<br>Message text content</p>                                                                                                                                                                                                                                                                                                              |
| BMXMessage.ContentType                                                                        | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-contenttype"><strong>contentType</strong></a>()<br>Message content type, attachment-type with attachment, text-type with no attachment</p>                                                                                                                                                                                                                                                           |
| [BMXMessageAttachment](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md) | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-attachment"><strong>attachment</strong></a>()<br>Message attachment, BMXMessage owns the attachment and is responsible for releasing it</p>                                                                                                                                                                                                                                                          |
| [BMXMessageConfig](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_config.md)         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-config"><strong>config</strong></a>()<br>Message settings</p>                                                                                                                                                                                                                                                                                                                                        |
| void                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setconfig"><strong>setConfig</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md">BMXMessageConfig</a> arg0)<br>Set message config information</p>                                                                                                                                                                                                                          |
| String                                                                                        | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-extension"><strong>extension</strong></a>()<br>Message extension information</p>                                                                                                                                                                                                                                                                                                                     |
| void                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setextension"><strong>setExtension</strong></a>(String arg0)<br>Set message extension information</p>                                                                                                                                                                                                                                                                                                |
| BMXMessage.DeliveryQos                                                                        | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-deliveryqos"><strong>deliveryQos</strong></a>()<br>QOS of messaging</p>                                                                                                                                                                                                                                                                                                                              |
| void                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setdeliveryqos"><strong>setDeliveryQos</strong></a>(BMXMessage.DeliveryQos qos)<br>Set QOS of messaging</p>                                                                                                                                                                                                                                                                                          |
| String                                                                                        | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-sendername"><strong>senderName</strong></a>()<br>Display name of message sender</p>                                                                                                                                                                                                                                                                                                                  |
| void                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setsendername"><strong>setSenderName</strong></a>(String senderName)<br>Set display name of message sender</p>                                                                                                                                                                                                                                                                                       |
| int                                                                                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupackcount"><strong>groupAckCount</strong></a>()<br>AckCount of read group messages</p>                                                                                                                                                                                                                                                                                                           |
| void                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setgroupackcount"><strong>setGroupAckCount</strong></a>(int count)<br>Set groupAckCount of read messages (an SDK internal calling interface that shall not be called by upper layer)</p>                                                                                                                                                                                                             |
| int                                                                                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupackunreadcount"><strong>groupAckUnreadCount</strong></a>()<br>AckCount of unread group messages</p>                                                                                                                                                                                                                                                                                             |
| void                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setgroupackunreadcount"><strong>setGroupAckUnreadCount</strong></a>(int count)<br>Set groupAckCount of unread messages (an SDK internal calling interface that shall not be called by upper layer)</p>                                                                                                                                                                                               |
| boolean                                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupackreadall"><strong>groupAckReadAll</strong></a>()<br>Whether all group messages are read</p>                                                                                                                                                                                                                                                                                                   |
| int                                                                                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupplayackcount"><strong>groupPlayAckCount</strong></a>()<br>Get count of played group messages</p>                                                                                                                                                                                                                                                                                                |
| void                                                                                          | [**setGroupPlayAckCount**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md#function-setgroupplayackcount)(int count)                                                                                                                                                                                                                                                                                                                                            |
| int                                                                                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupplayackunreadcount"><strong>groupPlayAckUnreadCount</strong></a>()<br>Get count of unread playback acknowledgements of group messages</p>                                                                                                                                                                                                                                                       |
| void                                                                                          | [**setGroupPlayAckUnreadCount**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md#function-setgroupplayackunreadcount)(int count)                                                                                                                                                                                                                                                                                                                                |
| boolean                                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-groupplayackreadall"><strong>groupPlayAckReadAll</strong></a>()<br>Set all playback acknowledgements of group messages as read</p>                                                                                                                                                                                                                                                                   |
| void                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setpriority"><strong>setPriority</strong></a>(int priority)<br>Set message diffusion priority, default 0. 0 means diffusion, and the smaller the number, the more diffused. Value range 0-10. The default level of messages sent by ordinary users in chatroom is 5, which can be discarded. Admin level defaults to 0 and will not be discarded. Other values can be set according to business.</p> |
| int                                                                                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-priority"><strong>priority</strong></a>()<br>Message diffusion priority</p>                                                                                                                                                                                                                                                                                                                          |
| void                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-setpushmessagemode"><strong>setPushMessageMode</strong></a>(boolean arg0)<br>Set whether to push messages</p>                                                                                                                                                                                                                                                                                        |
| boolean                                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-ispushmessage"><strong>isPushMessage</strong></a>()<br>Whether it is a push message</p>                                                                                                                                                                                                                                                                                                              |
| [BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md)                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createmessage"><strong>createMessage</strong></a>(long from, long to, BMXMessage.MessageType type, long conversationId, String content)<br>Create a text message</p>                                                                                                                                                                                                                                 |
| [BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md)                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createmessage"><strong>createMessage</strong></a>(long from, long to, BMXMessage.MessageType type, long conversationId, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md">BMXMessageAttachment</a> attachment)<br>Create a sent-attachment message</p>                                                                                                                            |
| [BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md)                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createcommandmessage"><strong>createCommandMessage</strong></a>(long from, long to, BMXMessage.MessageType type, long conversationId, String content)<br>Create a sent command message (command message holds command information in a content field or an extension field)</p>                                                                                                                      |
| [BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md)                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createmessage"><strong>createMessage</strong></a>(long msgId, long from, long to, BMXMessage.MessageType type, long conversationId, String content, long serverTimestamp)<br>Create a received message</p>                                                                                                                                                                                           |
| [BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md)                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createmessage"><strong>createMessage</strong></a>(long msgId, long from, long to, BMXMessage.MessageType type, long conversationId, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md">BMXMessageAttachment</a> attachment, long serverTimestamp)<br>Create a received message</p>                                                                                                 |
| [BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md)                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createcommandmessage"><strong>createCommandMessage</strong></a>(long msgId, long from, long to, BMXMessage.MessageType type, long conversationId, String content, long serverTimestamp)<br>Create a received command message (command message holds command information in a content field or an extension field)</p>                                                                                |
| [BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md)                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md#function-createforwardmessage"><strong>createForwardMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, long from, long to, BMXMessage.MessageType type, long conversationId)<br>Create a forwarding message</p>                                                                                                                                               |

## Protected Functions

|      | Name                                                                                                                                                                   |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXMessage**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md#function-bmxmessage)(long cPtr, boolean cMemoryOwn)                                         |
| void | [**finalize**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md#function-finalize)()                                                                          |
| long | [**getCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md#function-getcptr)([BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md) obj) |

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

Message unique ID

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function clientMsgId

```java
inline long clientMsgId()
```

Message client ID, only exists on message sender-side

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function fromId

```java
inline long fromId()
```

Message sender ID

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function toId

```java
inline long toId()
```

Message receiver ID

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function type

```java
inline BMXMessage.MessageType type()
```

Message type

**Return**: \[MessageType]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function conversationId

```java
inline long conversationId()
```

Conversation ID that message belongs to

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function deliveryStatus

```java
inline BMXMessage.DeliveryStatus deliveryStatus()
```

Messaging state

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

Set messaging state

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function serverTimestamp

```java
inline long serverTimestamp()
```

Message timestamp (when received by server-side)

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

Set message timestamp (when received by server-side)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function clientTimestamp

```java
inline long clientTimestamp()
```

Local timestamp (local time when message created or received)

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

Set message local timestamp

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function isPlayed

```java
inline boolean isPlayed()
```

Whether voice or video message has been played, valid only for received audio/video messages

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

Whether voice or video message receives a playback acknowledgement, valid only for received audio/video messages

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

Message whether to receive

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

Message read or unread mark

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

Show sender whether read acknowledgement received, and show receiver whether message read acknowledgement sent

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

Show sender whether message has been delivered to the other party, and show receiver whether message delivered acknowledgement has been sent

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

Message text content

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

Message text content

**Parameters**:

* **content** Message text content

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function contentType

```java
inline BMXMessage.ContentType contentType()
```

Message content type, attachment-type with attachment, text-type with no attachment

**Return**: \[ContentType]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function attachment

```java
inline BMXMessageAttachment attachment()
```

Message attachment, BMXMessage owns the attachment and is responsible for releasing it

**Return**: BMXMessageAttachmentPtr

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function config

```java
inline BMXMessageConfig config()
```

Message settings

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

Set message config information

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function extension

```java
inline String extension()
```

Message extension information

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

Set message extension information

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function deliveryQos

```java
inline BMXMessage.DeliveryQos deliveryQos()
```

QOS of messaging

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

Set QOS of messaging

**Parameters**:

* **qos** QOS of messaging

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function senderName

```java
inline String senderName()
```

Display name of message sender

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

Set display name of message sender

**Parameters**:

* **senderName** Message text content

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function groupAckCount

```java
inline int groupAckCount()
```

AckCount of read group messages

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

Set groupAckCount of read messages (an SDK internal calling interface that shall not be called by upper layer)

**Parameters**:

* **count** Set the number of read group messages

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function groupAckUnreadCount

```java
inline int groupAckUnreadCount()
```

AckCount of unread group messages

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

Set groupAckCount of unread messages (an SDK internal calling interface that shall not be called by upper layer)

**Parameters**:

* **count** Set the number of unread group messages

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function groupAckReadAll

```java
inline boolean groupAckReadAll()
```

Whether all group messages are read

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function groupPlayAckCount

```java
inline int groupPlayAckCount()
```

Get count of played group messages

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

Get count of unread playback acknowledgements of group messages

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

Set all playback acknowledgements of group messages as read

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

Set message diffusion priority, default 0. 0 means diffusion, and the smaller the number, the more diffused. Value range 0-10. The default level of messages sent by ordinary users in chatroom is 5, which can be discarded. Admin level defaults to 0 and will not be discarded. Other values can be set according to business.

**Parameters**:

* **priority** Set the number of unread group messages

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function priority

```java
inline int priority()
```

Message diffusion priority

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

Set whether to push messages

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessage'></div>
```

### function isPushMessage

```java
inline boolean isPushMessage()
```

Whether it is a push message

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

Create a text message

**Parameters**:

* **from** Message sender
* **to** Message receiver
* **type** Message type
* **conversationId** Conversation id
* **content** Message content

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

Create a sent-attachment message

**Parameters**:

* **from** Message sender
* **to** Message receiver
* **type** Message type
* **conversationId** Conversation id
* **attachment** Attachment

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

Create a sent command message (command message holds command information in a content field or an extension field)

**Parameters**:

* **from** Message sender
* **to** Message receiver
* **type** Message type
* **conversationId** Conversation id
* **content** Message content

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

Create a received message

**Parameters**:

* **msgId** Message id
* **from** Message sender
* **to** Message receiver
* **type** Message type
* **conversationId** Conversation id
* **content** Message content
* **serverTimestamp** Server timestamp

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

Create a received message

**Parameters**:

* **msgId** Message id
* **from** Message sender
* **to** Message receiver
* **type** Message type
* **conversationId** Conversation id
* **attachment** Attachment
* **serverTimestamp** Server timestamp

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

Create a received command message (command message holds command information in a content field or an extension field)

**Parameters**:

* **msgId** Message id
* **from** Message sender
* **to** Message receiver
* **type** Message type
* **conversationId** Conversation id
* **content** Message content
* **serverTimestamp** Server timestamp

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

Create a forwarding message

**Parameters**:

* **msg** Message to forward
* **from** Message sender
* **to** Message receiver
* **type** Message type
* **conversationId** Conversation id

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



Updated on 2022-01-26 at 17:18:31 +0800
