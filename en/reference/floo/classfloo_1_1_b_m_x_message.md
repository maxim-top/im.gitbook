---
title: floo::BMXMessage
summary: Message 

---

# floo::BMXMessage



Message 


`#include <bmx_message.h>`

Inherits from BMXBaseObject

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[DeliveryStatus](classfloo_1_1_b_m_x_message.md#enum-deliverystatus)** { New, Delivering, Deliveried, Failed, Recalled}<br>Messaging state  |
| enum class| **[MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype)** { Single, Group, System}<br>Message type  |
| enum class| **[ContentType](classfloo_1_1_b_m_x_message.md#enum-contenttype)** { Text, Image, Voice, Video, File, Location, Command, Forward}<br>Type of message content  |
| enum class| **[DeliveryQos](classfloo_1_1_b_m_x_message.md#enum-deliveryqos)** { AtLastOnce, AtMostOnce, ExactlyOnce}<br>Messaging quality  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXMessage](classfloo_1_1_b_m_x_message.md#function-~bmxmessage)**()<br>Destructor  |
| int64_t | **[msgId](classfloo_1_1_b_m_x_message.md#function-msgid)**()<br>Message unique ID  |
| int64_t | **[clientMsgId](classfloo_1_1_b_m_x_message.md#function-clientmsgid)**()<br>Message client ID, only exists on message sender-side  |
| int64_t | **[fromId](classfloo_1_1_b_m_x_message.md#function-fromid)**()<br>Message sender ID  |
| int64_t | **[toId](classfloo_1_1_b_m_x_message.md#function-toid)**()<br>Message receiver ID  |
| [MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype) | **[type](classfloo_1_1_b_m_x_message.md#function-type)**()<br>Message type  |
| int64_t | **[conversationId](classfloo_1_1_b_m_x_message.md#function-conversationid)**()<br>Conversation ID that message belongs to  |
| [DeliveryStatus](classfloo_1_1_b_m_x_message.md#enum-deliverystatus) | **[deliveryStatus](classfloo_1_1_b_m_x_message.md#function-deliverystatus)**()<br>Messaging state  |
| void | **[setDeliveryStatus](classfloo_1_1_b_m_x_message.md#function-setdeliverystatus)**([DeliveryStatus](classfloo_1_1_b_m_x_message.md#enum-deliverystatus) )<br>Set messaging state  |
| int64_t | **[serverTimestamp](classfloo_1_1_b_m_x_message.md#function-servertimestamp)**()<br>Message timestamp (when received by server-side)  |
| void | **[setServerTimestamp](classfloo_1_1_b_m_x_message.md#function-setservertimestamp)**(int64_t )<br>Set message timestamp (when received by server-side)  |
| int64_t | **[clientTimestamp](classfloo_1_1_b_m_x_message.md#function-clienttimestamp)**()<br>Local timestamp (local time when message created or received)  |
| void | **[setClientTimestamp](classfloo_1_1_b_m_x_message.md#function-setclienttimestamp)**(int64_t )<br>Set message local timestamp  |
| bool | **[isPlayed](classfloo_1_1_b_m_x_message.md#function-isplayed)**()<br>Whether voice or video message has been played, valid only for received audio/video messages  |
| void | **[setIsPlayed](classfloo_1_1_b_m_x_message.md#function-setisplayed)**(bool )<br>Set whether a voice or video message has been played, valid only for received audio or video messages  |
| bool | **[isPlayAcked](classfloo_1_1_b_m_x_message.md#function-isplayacked)**()<br>Means whether playback acknowledgement received for sender, and whether playback acknowledgement sent for receiver  |
| void | **[setIsPlayAcked](classfloo_1_1_b_m_x_message.md#function-setisplayacked)**(bool )<br>Set playback acknowledgement  |
| bool | **[isReceiveMsg](classfloo_1_1_b_m_x_message.md#function-isreceivemsg)**()<br>Message whether to receive  |
| void | **[setIsReceiveMsg](classfloo_1_1_b_m_x_message.md#function-setisreceivemsg)**(bool )<br>Message to set receiving condition  |
| bool | **[isRead](classfloo_1_1_b_m_x_message.md#function-isread)**()<br>Message read or unread mark  |
| void | **[setIsRead](classfloo_1_1_b_m_x_message.md#function-setisread)**(bool )<br>Message read or unread mark  |
| bool | **[isReadAcked](classfloo_1_1_b_m_x_message.md#function-isreadacked)**()<br>Show sender whether read acknowledgement received, and show receiver whether message read acknowledgement sent  |
| void | **[setIsReadAcked](classfloo_1_1_b_m_x_message.md#function-setisreadacked)**(bool )<br>Set read acknowledgement  |
| bool | **[isDeliveryAcked](classfloo_1_1_b_m_x_message.md#function-isdeliveryacked)**()<br>Show sender whether message has been delivered to the other party, and show receiver whether message delivered acknowledgement has been sent  |
| void | **[setIsDeliveryAcked](classfloo_1_1_b_m_x_message.md#function-setisdeliveryacked)**(bool )<br>Set delivery acknowledgement  |
| const std::string & | **[content](classfloo_1_1_b_m_x_message.md#function-content)**()<br>Message text content  |
| void | **[setContent](classfloo_1_1_b_m_x_message.md#function-setcontent)**(const std::string & content)<br>Message text content  |
| [ContentType](classfloo_1_1_b_m_x_message.md#enum-contenttype) | **[contentType](classfloo_1_1_b_m_x_message.md#function-contenttype)**()<br>Message content type, attachment-type with attachment, text-type with no attachment  |
| BMXMessageAttachmentPtr | **[attachment](classfloo_1_1_b_m_x_message.md#function-attachment)**()<br>Message attachment, BMXMessage owns the attachment and is responsible for releasing it  |
| BMXMessageConfigPtr | **[config](classfloo_1_1_b_m_x_message.md#function-config)**()<br>Message settings  |
| void | **[setConfig](classfloo_1_1_b_m_x_message.md#function-setconfig)**(BMXMessageConfigPtr )<br>Set message config information  |
| const JSON & | **[extension](classfloo_1_1_b_m_x_message.md#function-extension)**()<br>Message extension information  |
| void | **[setExtension](classfloo_1_1_b_m_x_message.md#function-setextension)**(const JSON & )<br>Set message extension information  |
| [DeliveryQos](classfloo_1_1_b_m_x_message.md#enum-deliveryqos) | **[deliveryQos](classfloo_1_1_b_m_x_message.md#function-deliveryqos)**()<br>QOS of messaging  |
| void | **[setDeliveryQos](classfloo_1_1_b_m_x_message.md#function-setdeliveryqos)**([DeliveryQos](classfloo_1_1_b_m_x_message.md#enum-deliveryqos) qos)<br>Set QOS of messaging  |
| const std::string & | **[senderName](classfloo_1_1_b_m_x_message.md#function-sendername)**()<br>Display name of message sender  |
| void | **[setSenderName](classfloo_1_1_b_m_x_message.md#function-setsendername)**(const std::string & senderName)<br>Set display name of message sender  |
| int | **[groupAckCount](classfloo_1_1_b_m_x_message.md#function-groupackcount)**()<br>AckCount of read group messages  |
| void | **[setGroupAckCount](classfloo_1_1_b_m_x_message.md#function-setgroupackcount)**(int count)<br>Set groupAckCount of read messages (an SDK internal calling interface that shall not be called by upper layer)  |
| int | **[groupAckUnreadCount](classfloo_1_1_b_m_x_message.md#function-groupackunreadcount)**()<br>AckCount of unread group messages  |
| void | **[setGroupAckUnreadCount](classfloo_1_1_b_m_x_message.md#function-setgroupackunreadcount)**(int count)<br>Set groupAckCount of unread messages (an SDK internal calling interface that shall not be called by upper layer)  |
| bool | **[groupAckReadAll](classfloo_1_1_b_m_x_message.md#function-groupackreadall)**()<br>Whether all group messages are read  |
| int | **[groupPlayAckCount](classfloo_1_1_b_m_x_message.md#function-groupplayackcount)**()<br>AckCount of played group messages (valid only for messages with audio/video attachment)  |
| void | **[setGroupPlayAckCount](classfloo_1_1_b_m_x_message.md#function-setgroupplayackcount)**(int count)<br>Set groupAckCount of played messages (an SDK internal calling interface that shall not be called by upper layer) (valid only for messages with audio/video attachment)  |
| int | **[groupPlayAckUnreadCount](classfloo_1_1_b_m_x_message.md#function-groupplayackunreadcount)**()<br>AckCount of unplayed group messages (valid only for messages with audio/video attachment)  |
| void | **[setGroupPlayAckUnreadCount](classfloo_1_1_b_m_x_message.md#function-setgroupplayackunreadcount)**(int count)<br>Set groupAckCount of unplayed messages (an SDK internal calling interface that shall not be called by upper layer) (valid only for messages with audio/video attachment)  |
| bool | **[groupPlayAckReadAll](classfloo_1_1_b_m_x_message.md#function-groupplayackreadall)**()<br>Whether all group messages have been played  |
| void | **[setPriority](classfloo_1_1_b_m_x_message.md#function-setpriority)**(int priority)<br>Set message diffusion priority, default 0. 0 means diffusion, and the smaller the number, the more diffused.  |
| int | **[priority](classfloo_1_1_b_m_x_message.md#function-priority)**()<br>Message diffusion priority  |
| void | **[setPushMessageMode](classfloo_1_1_b_m_x_message.md#function-setpushmessagemode)**(bool )<br>Set whether the message is a push.  |
| bool | **[isPushMessage](classfloo_1_1_b_m_x_message.md#function-ispushmessage)**()<br>Whether the message is a push  |
| BMXMessagePtr | **[createMessage](classfloo_1_1_b_m_x_message.md#function-createmessage)**(int64_t from, int64_t to, [MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype) type, int64_t conversationId, const std::string & content)<br>Create a text message  |
| BMXMessagePtr | **[createMessage](classfloo_1_1_b_m_x_message.md#function-createmessage)**(int64_t from, int64_t to, [MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype) type, int64_t conversationId, BMXMessageAttachmentPtr attachment)<br>Create a sent-attachment message  |
| BMXMessagePtr | **[createCommandMessage](classfloo_1_1_b_m_x_message.md#function-createcommandmessage)**(int64_t from, int64_t to, [MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype) type, int64_t conversationId, const std::string & content)<br>Create a sent command message (command message holds command information in a content field or an extension field)  |
| BMXMessagePtr | **[createMessage](classfloo_1_1_b_m_x_message.md#function-createmessage)**(int64_t msgId, int64_t from, int64_t to, [MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype) type, int64_t conversationId, const std::string & content, int64_t serverTimestamp)<br>Create a received message  |
| BMXMessagePtr | **[createMessage](classfloo_1_1_b_m_x_message.md#function-createmessage)**(int64_t msgId, int64_t from, int64_t to, [MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype) type, int64_t conversationId, BMXMessageAttachmentPtr attachment, int64_t serverTimestamp)<br>Create a received message  |
| BMXMessagePtr | **[createCommandMessage](classfloo_1_1_b_m_x_message.md#function-createcommandmessage)**(int64_t msgId, int64_t from, int64_t to, [MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype) type, int64_t conversationId, const std::string & content, int64_t serverTimestamp)<br>Create a received command message (command message holds command information in a content field or an extension field)  |
| BMXMessagePtr | **[createForwardMessage](classfloo_1_1_b_m_x_message.md#function-createforwardmessage)**(BMXMessagePtr msg, int64_t from, int64_t to, [MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype) type, int64_t conversationId)<br>Create a forwarding message  |

## Public Types Documentation

### enum DeliveryStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| New | | Newly created message   |
| Delivering | | Message delivering   |
| Deliveried | | Message delivered   |
| Failed | | Message delivery failed   |
| Recalled | | Message delivery canceled   |



Messaging state 

### enum MessageType

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Single | | Single chat message   |
| Group | | Group chat message   |
| System | | System message   |



Message type 

### enum ContentType

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Text | | Text message   |
| Image | | Image message   |
| Voice | | Voice message   |
| Video | | Video clip message   |
| File | | File message   |
| Location | | Location message   |
| Command | | Command message   |
| Forward | | Forward message   |



Type of message content 

### enum DeliveryQos

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| AtLastOnce | | Deliver at least once   |
| AtMostOnce | | Deliver at most once   |
| ExactlyOnce | | Deliver only once   |



Messaging quality 

## Public Functions Documentation

### function ~BMXMessage

```cpp
virtual ~BMXMessage()
```

Destructor 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="~BMXMessage" %}{% endlanying_code_snippet %}
```
### function msgId

```cpp
int64_t msgId()
```

Message unique ID 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="msgId" %}{% endlanying_code_snippet %}
```
### function clientMsgId

```cpp
int64_t clientMsgId()
```

Message client ID, only exists on message sender-side 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="clientMsgId" %}{% endlanying_code_snippet %}
```
### function fromId

```cpp
int64_t fromId()
```

Message sender ID 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="fromId" %}{% endlanying_code_snippet %}
```
### function toId

```cpp
int64_t toId()
```

Message receiver ID 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="toId" %}{% endlanying_code_snippet %}
```
### function type

```cpp
MessageType type()
```

Message type 

**Return**: MessageType 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="type" %}{% endlanying_code_snippet %}
```
### function conversationId

```cpp
int64_t conversationId()
```

Conversation ID that message belongs to 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="conversationId" %}{% endlanying_code_snippet %}
```
### function deliveryStatus

```cpp
DeliveryStatus deliveryStatus()
```

Messaging state 

**Return**: DeliveryStatus 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="deliveryStatus" %}{% endlanying_code_snippet %}
```
### function setDeliveryStatus

```cpp
void setDeliveryStatus(
    DeliveryStatus 
)
```

Set messaging state 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setDeliveryStatus" %}{% endlanying_code_snippet %}
```
### function serverTimestamp

```cpp
int64_t serverTimestamp()
```

Message timestamp (when received by server-side) 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="serverTimestamp" %}{% endlanying_code_snippet %}
```
### function setServerTimestamp

```cpp
void setServerTimestamp(
    int64_t 
)
```

Set message timestamp (when received by server-side) 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setServerTimestamp" %}{% endlanying_code_snippet %}
```
### function clientTimestamp

```cpp
int64_t clientTimestamp()
```

Local timestamp (local time when message created or received) 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="clientTimestamp" %}{% endlanying_code_snippet %}
```
### function setClientTimestamp

```cpp
void setClientTimestamp(
    int64_t 
)
```

Set message local timestamp 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setClientTimestamp" %}{% endlanying_code_snippet %}
```
### function isPlayed

```cpp
bool isPlayed()
```

Whether voice or video message has been played, valid only for received audio/video messages 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="isPlayed" %}{% endlanying_code_snippet %}
```
### function setIsPlayed

```cpp
void setIsPlayed(
    bool 
)
```

Set whether a voice or video message has been played, valid only for received audio or video messages 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setIsPlayed" %}{% endlanying_code_snippet %}
```
### function isPlayAcked

```cpp
bool isPlayAcked()
```

Means whether playback acknowledgement received for sender, and whether playback acknowledgement sent for receiver 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="isPlayAcked" %}{% endlanying_code_snippet %}
```
### function setIsPlayAcked

```cpp
void setIsPlayAcked(
    bool 
)
```

Set playback acknowledgement 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setIsPlayAcked" %}{% endlanying_code_snippet %}
```
### function isReceiveMsg

```cpp
bool isReceiveMsg()
```

Message whether to receive 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="isReceiveMsg" %}{% endlanying_code_snippet %}
```
### function setIsReceiveMsg

```cpp
void setIsReceiveMsg(
    bool 
)
```

Message to set receiving condition 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setIsReceiveMsg" %}{% endlanying_code_snippet %}
```
### function isRead

```cpp
bool isRead()
```

Message read or unread mark 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="isRead" %}{% endlanying_code_snippet %}
```
### function setIsRead

```cpp
void setIsRead(
    bool 
)
```

Message read or unread mark 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setIsRead" %}{% endlanying_code_snippet %}
```
### function isReadAcked

```cpp
bool isReadAcked()
```

Show sender whether read acknowledgement received, and show receiver whether message read acknowledgement sent 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="isReadAcked" %}{% endlanying_code_snippet %}
```
### function setIsReadAcked

```cpp
void setIsReadAcked(
    bool 
)
```

Set read acknowledgement 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setIsReadAcked" %}{% endlanying_code_snippet %}
```
### function isDeliveryAcked

```cpp
bool isDeliveryAcked()
```

Show sender whether message has been delivered to the other party, and show receiver whether message delivered acknowledgement has been sent 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="isDeliveryAcked" %}{% endlanying_code_snippet %}
```
### function setIsDeliveryAcked

```cpp
void setIsDeliveryAcked(
    bool 
)
```

Set delivery acknowledgement 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setIsDeliveryAcked" %}{% endlanying_code_snippet %}
```
### function content

```cpp
const std::string & content()
```

Message text content 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="content" %}{% endlanying_code_snippet %}
```
### function setContent

```cpp
void setContent(
    const std::string & content
)
```

Message text content 

**Parameters**: 

  * **content** Message text content 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setContent" %}{% endlanying_code_snippet %}
```
### function contentType

```cpp
ContentType contentType()
```

Message content type, attachment-type with attachment, text-type with no attachment 

**Return**: ContentType 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="contentType" %}{% endlanying_code_snippet %}
```
### function attachment

```cpp
BMXMessageAttachmentPtr attachment()
```

Message attachment, BMXMessage owns the attachment and is responsible for releasing it 

**Return**: BMXMessageAttachmentPtr 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="attachment" %}{% endlanying_code_snippet %}
```
### function config

```cpp
BMXMessageConfigPtr config()
```

Message settings 

**Return**: JSON(std::string) 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="config" %}{% endlanying_code_snippet %}
```
### function setConfig

```cpp
void setConfig(
    BMXMessageConfigPtr 
)
```

Set message config information 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setConfig" %}{% endlanying_code_snippet %}
```
### function extension

```cpp
const JSON & extension()
```

Message extension information 

**Return**: JSON(std::string) 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="extension" %}{% endlanying_code_snippet %}
```
### function setExtension

```cpp
void setExtension(
    const JSON & 
)
```

Set message extension information 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setExtension" %}{% endlanying_code_snippet %}
```
### function deliveryQos

```cpp
DeliveryQos deliveryQos()
```

QOS of messaging 

**Return**: DeliveryQos 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="deliveryQos" %}{% endlanying_code_snippet %}
```
### function setDeliveryQos

```cpp
void setDeliveryQos(
    DeliveryQos qos
)
```

Set QOS of messaging 

**Parameters**: 

  * **qos** QOS of messaging 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setDeliveryQos" %}{% endlanying_code_snippet %}
```
### function senderName

```cpp
const std::string & senderName()
```

Display name of message sender 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="senderName" %}{% endlanying_code_snippet %}
```
### function setSenderName

```cpp
void setSenderName(
    const std::string & senderName
)
```

Set display name of message sender 

**Parameters**: 

  * **senderName** Message text content 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setSenderName" %}{% endlanying_code_snippet %}
```
### function groupAckCount

```cpp
int groupAckCount()
```

AckCount of read group messages 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="groupAckCount" %}{% endlanying_code_snippet %}
```
### function setGroupAckCount

```cpp
void setGroupAckCount(
    int count
)
```

Set groupAckCount of read messages (an SDK internal calling interface that shall not be called by upper layer) 

**Parameters**: 

  * **count** Set the number of read group messages 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setGroupAckCount" %}{% endlanying_code_snippet %}
```
### function groupAckUnreadCount

```cpp
int groupAckUnreadCount()
```

AckCount of unread group messages 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="groupAckUnreadCount" %}{% endlanying_code_snippet %}
```
### function setGroupAckUnreadCount

```cpp
void setGroupAckUnreadCount(
    int count
)
```

Set groupAckCount of unread messages (an SDK internal calling interface that shall not be called by upper layer) 

**Parameters**: 

  * **count** Set the number of unread group messages 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setGroupAckUnreadCount" %}{% endlanying_code_snippet %}
```
### function groupAckReadAll

```cpp
bool groupAckReadAll()
```

Whether all group messages are read 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="groupAckReadAll" %}{% endlanying_code_snippet %}
```
### function groupPlayAckCount

```cpp
int groupPlayAckCount()
```

AckCount of played group messages (valid only for messages with audio/video attachment) 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="groupPlayAckCount" %}{% endlanying_code_snippet %}
```
### function setGroupPlayAckCount

```cpp
void setGroupPlayAckCount(
    int count
)
```

Set groupAckCount of played messages (an SDK internal calling interface that shall not be called by upper layer) (valid only for messages with audio/video attachment) 

**Parameters**: 

  * **count** Set the number of read group messages 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setGroupPlayAckCount" %}{% endlanying_code_snippet %}
```
### function groupPlayAckUnreadCount

```cpp
int groupPlayAckUnreadCount()
```

AckCount of unplayed group messages (valid only for messages with audio/video attachment) 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="groupPlayAckUnreadCount" %}{% endlanying_code_snippet %}
```
### function setGroupPlayAckUnreadCount

```cpp
void setGroupPlayAckUnreadCount(
    int count
)
```

Set groupAckCount of unplayed messages (an SDK internal calling interface that shall not be called by upper layer) (valid only for messages with audio/video attachment) 

**Parameters**: 

  * **count** Set the number of unplayed group messages 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setGroupPlayAckUnreadCount" %}{% endlanying_code_snippet %}
```
### function groupPlayAckReadAll

```cpp
bool groupPlayAckReadAll()
```

Whether all group messages have been played 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="groupPlayAckReadAll" %}{% endlanying_code_snippet %}
```
### function setPriority

```cpp
void setPriority(
    int priority
)
```

Set message diffusion priority, default 0. 0 means diffusion, and the smaller the number, the more diffused. 

**Parameters**: 

  * **priority** Set the number of unread group messages 


Value range 0-10. The default level of messages sent by ordinary users in chatroom is 5, which can be discarded. Admin level defaults to 0 and will not be discarded. Other values can be set according to business. 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setPriority" %}{% endlanying_code_snippet %}
```
### function priority

```cpp
int priority()
```

Message diffusion priority 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="priority" %}{% endlanying_code_snippet %}
```
### function setPushMessageMode

```cpp
void setPushMessageMode(
    bool 
)
```

Set whether the message is a push. 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="setPushMessageMode" %}{% endlanying_code_snippet %}
```
### function isPushMessage

```cpp
bool isPushMessage()
```

Whether the message is a push 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="isPushMessage" %}{% endlanying_code_snippet %}
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

Create a text message 

**Parameters**: 

  * **from** Message sender 
  * **to** Message receiver 
  * **type** Message type 
  * **conversationId** Conversation id 
  * **content** Message content 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="createMessage" %}{% endlanying_code_snippet %}
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

Create a sent-attachment message 

**Parameters**: 

  * **from** Message sender 
  * **to** Message receiver 
  * **type** Message type 
  * **conversationId** Conversation id 
  * **attachment** Attachment 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="createMessage" %}{% endlanying_code_snippet %}
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

Create a sent command message (command message holds command information in a content field or an extension field) 

**Parameters**: 

  * **from** Message sender 
  * **to** Message receiver 
  * **type** Message type 
  * **conversationId** Conversation id 
  * **content** Message content 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="createCommandMessage" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="createMessage" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="createMessage" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="createCommandMessage" %}{% endlanying_code_snippet %}
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

Create a forwarding message 

**Parameters**: 

  * **msg** Message to forward 
  * **from** Message sender 
  * **to** Message receiver 
  * **type** Message type 
  * **conversationId** Conversation id 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessage",function="createForwardMessage" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800