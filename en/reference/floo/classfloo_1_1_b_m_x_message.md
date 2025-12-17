---
title: floo::BMXMessage
summary: Message
---

# floo::BMXMessage

Message

`#include <bmx_message.h>`

Inherits from BMXBaseObject

## Public Types

|            | Name                                                                                                                                                                                        |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class | <p><a href="classfloo_1_1_b_m_x_message.md#enum-deliverystatus"><strong>DeliveryStatus</strong></a> { New, Delivering, Deliveried, Failed, Recalled}<br>Messaging state</p>                 |
| enum class | <p><a href="classfloo_1_1_b_m_x_message.md#enum-messagetype"><strong>MessageType</strong></a> { Single, Group, System}<br>Message type</p>                                                  |
| enum class | <p><a href="classfloo_1_1_b_m_x_message.md#enum-contenttype"><strong>ContentType</strong></a> { Text, Image, Voice, Video, File, Location, Command, Forward}<br>Type of message content</p> |
| enum class | <p><a href="classfloo_1_1_b_m_x_message.md#enum-deliveryqos"><strong>DeliveryQos</strong></a> { AtLastOnce, AtMostOnce, ExactlyOnce}<br>Messaging quality</p>                               |

## Public Functions

|                                                                      | Name                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual                                                              | <p><a href="classfloo_1_1_b_m_x_message.md#function-~bmxmessage"><strong>~BMXMessage</strong></a>()<br>Destructor</p>                                                                                                                                                                                                                                                                                                                                         |
| int64\_t                                                             | <p><a href="classfloo_1_1_b_m_x_message.md#function-msgid"><strong>msgId</strong></a>()<br>Message unique ID</p>                                                                                                                                                                                                                                                                                                                                              |
| int64\_t                                                             | <p><a href="classfloo_1_1_b_m_x_message.md#function-clientmsgid"><strong>clientMsgId</strong></a>()<br>Message client ID, only exists on message sender-side</p>                                                                                                                                                                                                                                                                                              |
| int64\_t                                                             | <p><a href="classfloo_1_1_b_m_x_message.md#function-fromid"><strong>fromId</strong></a>()<br>Message sender ID</p>                                                                                                                                                                                                                                                                                                                                            |
| int64\_t                                                             | <p><a href="classfloo_1_1_b_m_x_message.md#function-toid"><strong>toId</strong></a>()<br>Message receiver ID</p>                                                                                                                                                                                                                                                                                                                                              |
| [MessageType](classfloo_1_1_b_m_x_message.md#enum-messagetype)       | <p><a href="classfloo_1_1_b_m_x_message.md#function-type"><strong>type</strong></a>()<br>Message type</p>                                                                                                                                                                                                                                                                                                                                                     |
| int64\_t                                                             | <p><a href="classfloo_1_1_b_m_x_message.md#function-conversationid"><strong>conversationId</strong></a>()<br>Conversation ID that message belongs to</p>                                                                                                                                                                                                                                                                                                      |
| [DeliveryStatus](classfloo_1_1_b_m_x_message.md#enum-deliverystatus) | <p><a href="classfloo_1_1_b_m_x_message.md#function-deliverystatus"><strong>deliveryStatus</strong></a>()<br>Messaging state</p>                                                                                                                                                                                                                                                                                                                              |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setdeliverystatus"><strong>setDeliveryStatus</strong></a>(<a href="classfloo_1_1_b_m_x_message.md#enum-deliverystatus">DeliveryStatus</a> )<br>Set messaging state</p>                                                                                                                                                                                                                                    |
| int64\_t                                                             | <p><a href="classfloo_1_1_b_m_x_message.md#function-servertimestamp"><strong>serverTimestamp</strong></a>()<br>Message timestamp (when received by server-side)</p>                                                                                                                                                                                                                                                                                           |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setservertimestamp"><strong>setServerTimestamp</strong></a>(int64_t )<br>Set message timestamp (when received by server-side)</p>                                                                                                                                                                                                                                                                         |
| int64\_t                                                             | <p><a href="classfloo_1_1_b_m_x_message.md#function-clienttimestamp"><strong>clientTimestamp</strong></a>()<br>Local timestamp (local time when message created or received)</p>                                                                                                                                                                                                                                                                              |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setclienttimestamp"><strong>setClientTimestamp</strong></a>(int64_t )<br>Set message local timestamp</p>                                                                                                                                                                                                                                                                                                  |
| bool                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-isplayed"><strong>isPlayed</strong></a>()<br>Whether voice or video message has been played, valid only for received audio/video messages</p>                                                                                                                                                                                                                                                             |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setisplayed"><strong>setIsPlayed</strong></a>(bool )<br>Set whether a voice or video message has been played, valid only for received audio or video messages</p>                                                                                                                                                                                                                                         |
| bool                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-isplayacked"><strong>isPlayAcked</strong></a>()<br>Means whether playback acknowledgement received for sender, and whether playback acknowledgement sent for receiver</p>                                                                                                                                                                                                                                 |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setisplayacked"><strong>setIsPlayAcked</strong></a>(bool )<br>Set playback acknowledgement</p>                                                                                                                                                                                                                                                                                                            |
| bool                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-isreceivemsg"><strong>isReceiveMsg</strong></a>()<br>Message whether to receive</p>                                                                                                                                                                                                                                                                                                                       |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setisreceivemsg"><strong>setIsReceiveMsg</strong></a>(bool )<br>Message to set receiving condition</p>                                                                                                                                                                                                                                                                                                    |
| bool                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-isread"><strong>isRead</strong></a>()<br>Message read or unread mark</p>                                                                                                                                                                                                                                                                                                                                  |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setisread"><strong>setIsRead</strong></a>(bool )<br>Message read or unread mark</p>                                                                                                                                                                                                                                                                                                                       |
| bool                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-isreadacked"><strong>isReadAcked</strong></a>()<br>Show sender whether read acknowledgement received, and show receiver whether message read acknowledgement sent</p>                                                                                                                                                                                                                                     |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setisreadacked"><strong>setIsReadAcked</strong></a>(bool )<br>Set read acknowledgement</p>                                                                                                                                                                                                                                                                                                                |
| bool                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-isdeliveryacked"><strong>isDeliveryAcked</strong></a>()<br>Show sender whether message has been delivered to the other party, and show receiver whether message delivered acknowledgement has been sent</p>                                                                                                                                                                                               |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setisdeliveryacked"><strong>setIsDeliveryAcked</strong></a>(bool )<br>Set delivery acknowledgement</p>                                                                                                                                                                                                                                                                                                    |
| const std::string &                                                  | <p><a href="classfloo_1_1_b_m_x_message.md#function-content"><strong>content</strong></a>()<br>Message text content</p>                                                                                                                                                                                                                                                                                                                                       |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setcontent"><strong>setContent</strong></a>(const std::string &#x26; content)<br>Message text content</p>                                                                                                                                                                                                                                                                                                 |
| [ContentType](classfloo_1_1_b_m_x_message.md#enum-contenttype)       | <p><a href="classfloo_1_1_b_m_x_message.md#function-contenttype"><strong>contentType</strong></a>()<br>Message content type, attachment-type with attachment, text-type with no attachment</p>                                                                                                                                                                                                                                                                |
| BMXMessageAttachmentPtr                                              | <p><a href="classfloo_1_1_b_m_x_message.md#function-attachment"><strong>attachment</strong></a>()<br>Message attachment, BMXMessage owns the attachment and is responsible for releasing it</p>                                                                                                                                                                                                                                                               |
| BMXMessageConfigPtr                                                  | <p><a href="classfloo_1_1_b_m_x_message.md#function-config"><strong>config</strong></a>()<br>Message settings</p>                                                                                                                                                                                                                                                                                                                                             |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setconfig"><strong>setConfig</strong></a>(BMXMessageConfigPtr )<br>Set message config information</p>                                                                                                                                                                                                                                                                                                     |
| const JSON &                                                         | <p><a href="classfloo_1_1_b_m_x_message.md#function-extension"><strong>extension</strong></a>()<br>Message extension information</p>                                                                                                                                                                                                                                                                                                                          |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setextension"><strong>setExtension</strong></a>(const JSON &#x26; )<br>Set message extension information</p>                                                                                                                                                                                                                                                                                              |
| [DeliveryQos](classfloo_1_1_b_m_x_message.md#enum-deliveryqos)       | <p><a href="classfloo_1_1_b_m_x_message.md#function-deliveryqos"><strong>deliveryQos</strong></a>()<br>QOS of messaging</p>                                                                                                                                                                                                                                                                                                                                   |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setdeliveryqos"><strong>setDeliveryQos</strong></a>(<a href="classfloo_1_1_b_m_x_message.md#enum-deliveryqos">DeliveryQos</a> qos)<br>Set QOS of messaging</p>                                                                                                                                                                                                                                            |
| const std::string &                                                  | <p><a href="classfloo_1_1_b_m_x_message.md#function-sendername"><strong>senderName</strong></a>()<br>Display name of message sender</p>                                                                                                                                                                                                                                                                                                                       |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setsendername"><strong>setSenderName</strong></a>(const std::string &#x26; senderName)<br>Set display name of message sender</p>                                                                                                                                                                                                                                                                          |
| int                                                                  | <p><a href="classfloo_1_1_b_m_x_message.md#function-groupackcount"><strong>groupAckCount</strong></a>()<br>AckCount of read group messages</p>                                                                                                                                                                                                                                                                                                                |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setgroupackcount"><strong>setGroupAckCount</strong></a>(int count)<br>Set groupAckCount of read messages (an SDK internal calling interface that shall not be called by upper layer)</p>                                                                                                                                                                                                                  |
| int                                                                  | <p><a href="classfloo_1_1_b_m_x_message.md#function-groupackunreadcount"><strong>groupAckUnreadCount</strong></a>()<br>AckCount of unread group messages</p>                                                                                                                                                                                                                                                                                                  |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setgroupackunreadcount"><strong>setGroupAckUnreadCount</strong></a>(int count)<br>Set groupAckCount of unread messages (an SDK internal calling interface that shall not be called by upper layer)</p>                                                                                                                                                                                                    |
| bool                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-groupackreadall"><strong>groupAckReadAll</strong></a>()<br>Whether all group messages are read</p>                                                                                                                                                                                                                                                                                                        |
| int                                                                  | <p><a href="classfloo_1_1_b_m_x_message.md#function-groupplayackcount"><strong>groupPlayAckCount</strong></a>()<br>AckCount of played group messages (valid only for messages with audio/video attachment)</p>                                                                                                                                                                                                                                                |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setgroupplayackcount"><strong>setGroupPlayAckCount</strong></a>(int count)<br>Set groupAckCount of played messages (an SDK internal calling interface that shall not be called by upper layer) (valid only for messages with audio/video attachment)</p>                                                                                                                                                  |
| int                                                                  | <p><a href="classfloo_1_1_b_m_x_message.md#function-groupplayackunreadcount"><strong>groupPlayAckUnreadCount</strong></a>()<br>AckCount of unplayed group messages (valid only for messages with audio/video attachment)</p>                                                                                                                                                                                                                                  |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setgroupplayackunreadcount"><strong>setGroupPlayAckUnreadCount</strong></a>(int count)<br>Set groupAckCount of unplayed messages (an SDK internal calling interface that shall not be called by upper layer) (valid only for messages with audio/video attachment)</p>                                                                                                                                    |
| bool                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-groupplayackreadall"><strong>groupPlayAckReadAll</strong></a>()<br>Whether all group messages have been played</p>                                                                                                                                                                                                                                                                                        |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setpriority"><strong>setPriority</strong></a>(int priority)<br>Set message diffusion priority, default 0. 0 means diffusion, and the smaller the number, the more diffused.</p>                                                                                                                                                                                                                           |
| int                                                                  | <p><a href="classfloo_1_1_b_m_x_message.md#function-priority"><strong>priority</strong></a>()<br>Message diffusion priority</p>                                                                                                                                                                                                                                                                                                                               |
| void                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-setpushmessagemode"><strong>setPushMessageMode</strong></a>(bool )<br>Set whether the message is a push.</p>                                                                                                                                                                                                                                                                                              |
| bool                                                                 | <p><a href="classfloo_1_1_b_m_x_message.md#function-ispushmessage"><strong>isPushMessage</strong></a>()<br>Whether the message is a push</p>                                                                                                                                                                                                                                                                                                                  |
| BMXMessagePtr                                                        | <p><a href="classfloo_1_1_b_m_x_message.md#function-createmessage"><strong>createMessage</strong></a>(int64_t from, int64_t to, <a href="classfloo_1_1_b_m_x_message.md#enum-messagetype">MessageType</a> type, int64_t conversationId, const std::string &#x26; content)<br>Create a text message</p>                                                                                                                                                        |
| BMXMessagePtr                                                        | <p><a href="classfloo_1_1_b_m_x_message.md#function-createmessage"><strong>createMessage</strong></a>(int64_t from, int64_t to, <a href="classfloo_1_1_b_m_x_message.md#enum-messagetype">MessageType</a> type, int64_t conversationId, BMXMessageAttachmentPtr attachment)<br>Create a sent-attachment message</p>                                                                                                                                           |
| BMXMessagePtr                                                        | <p><a href="classfloo_1_1_b_m_x_message.md#function-createcommandmessage"><strong>createCommandMessage</strong></a>(int64_t from, int64_t to, <a href="classfloo_1_1_b_m_x_message.md#enum-messagetype">MessageType</a> type, int64_t conversationId, const std::string &#x26; content)<br>Create a sent command message (command message holds command information in a content field or an extension field)</p>                                             |
| BMXMessagePtr                                                        | <p><a href="classfloo_1_1_b_m_x_message.md#function-createmessage"><strong>createMessage</strong></a>(int64_t msgId, int64_t from, int64_t to, <a href="classfloo_1_1_b_m_x_message.md#enum-messagetype">MessageType</a> type, int64_t conversationId, const std::string &#x26; content, int64_t serverTimestamp)<br>Create a received message</p>                                                                                                            |
| BMXMessagePtr                                                        | <p><a href="classfloo_1_1_b_m_x_message.md#function-createmessage"><strong>createMessage</strong></a>(int64_t msgId, int64_t from, int64_t to, <a href="classfloo_1_1_b_m_x_message.md#enum-messagetype">MessageType</a> type, int64_t conversationId, BMXMessageAttachmentPtr attachment, int64_t serverTimestamp)<br>Create a received message</p>                                                                                                          |
| BMXMessagePtr                                                        | <p><a href="classfloo_1_1_b_m_x_message.md#function-createcommandmessage"><strong>createCommandMessage</strong></a>(int64_t msgId, int64_t from, int64_t to, <a href="classfloo_1_1_b_m_x_message.md#enum-messagetype">MessageType</a> type, int64_t conversationId, const std::string &#x26; content, int64_t serverTimestamp)<br>Create a received command message (command message holds command information in a content field or an extension field)</p> |
| BMXMessagePtr                                                        | <p><a href="classfloo_1_1_b_m_x_message.md#function-createforwardmessage"><strong>createForwardMessage</strong></a>(BMXMessagePtr msg, int64_t from, int64_t to, <a href="classfloo_1_1_b_m_x_message.md#enum-messagetype">MessageType</a> type, int64_t conversationId)<br>Create a forwarding message</p>                                                                                                                                                   |

## Public Types Documentation

### enum DeliveryStatus

| Enumerator | Value | Description               |
| ---------- | ----- | ------------------------- |
| New        |       | Newly created message     |
| Delivering |       | Message delivering        |
| Deliveried |       | Message delivered         |
| Failed     |       | Message delivery failed   |
| Recalled   |       | Message delivery canceled |

Messaging state

### enum MessageType

| Enumerator | Value | Description         |
| ---------- | ----- | ------------------- |
| Single     |       | Single chat message |
| Group      |       | Group chat message  |
| System     |       | System message      |

Message type

### enum ContentType

| Enumerator | Value | Description        |
| ---------- | ----- | ------------------ |
| Text       |       | Text message       |
| Image      |       | Image message      |
| Voice      |       | Voice message      |
| Video      |       | Video clip message |
| File       |       | File message       |
| Location   |       | Location message   |
| Command    |       | Command message    |
| Forward    |       | Forward message    |

Type of message content

### enum DeliveryQos

| Enumerator  | Value | Description           |
| ----------- | ----- | --------------------- |
| AtLastOnce  |       | Deliver at least once |
| AtMostOnce  |       | Deliver at most once  |
| ExactlyOnce |       | Deliver only once     |

Messaging quality

## Public Functions Documentation

### function \~BMXMessage

```cpp
virtual ~BMXMessage()
```

Destructor

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function msgId

```cpp
int64_t msgId()
```

Message unique ID

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function clientMsgId

```cpp
int64_t clientMsgId()
```

Message client ID, only exists on message sender-side

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function fromId

```cpp
int64_t fromId()
```

Message sender ID

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function toId

```cpp
int64_t toId()
```

Message receiver ID

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function type

```cpp
MessageType type()
```

Message type

**Return**: MessageType

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function conversationId

```cpp
int64_t conversationId()
```

Conversation ID that message belongs to

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function deliveryStatus

```cpp
DeliveryStatus deliveryStatus()
```

Messaging state

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

Set messaging state

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function serverTimestamp

```cpp
int64_t serverTimestamp()
```

Message timestamp (when received by server-side)

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

Set message timestamp (when received by server-side)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function clientTimestamp

```cpp
int64_t clientTimestamp()
```

Local timestamp (local time when message created or received)

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

Set message local timestamp

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function isPlayed

```cpp
bool isPlayed()
```

Whether voice or video message has been played, valid only for received audio/video messages

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

Set whether a voice or video message has been played, valid only for received audio or video messages

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function isPlayAcked

```cpp
bool isPlayAcked()
```

Means whether playback acknowledgement received for sender, and whether playback acknowledgement sent for receiver

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

Set playback acknowledgement

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function isReceiveMsg

```cpp
bool isReceiveMsg()
```

Message whether to receive

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

Message to set receiving condition

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function isRead

```cpp
bool isRead()
```

Message read or unread mark

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

Message read or unread mark

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function isReadAcked

```cpp
bool isReadAcked()
```

Show sender whether read acknowledgement received, and show receiver whether message read acknowledgement sent

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

Set read acknowledgement

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function isDeliveryAcked

```cpp
bool isDeliveryAcked()
```

Show sender whether message has been delivered to the other party, and show receiver whether message delivered acknowledgement has been sent

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

Set delivery acknowledgement

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function content

```cpp
const std::string & content()
```

Message text content

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

Message text content

**Parameters**:

* **content** Message text content

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function contentType

```cpp
ContentType contentType()
```

Message content type, attachment-type with attachment, text-type with no attachment

**Return**: ContentType

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function attachment

```cpp
BMXMessageAttachmentPtr attachment()
```

Message attachment, BMXMessage owns the attachment and is responsible for releasing it

**Return**: BMXMessageAttachmentPtr

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function config

```cpp
BMXMessageConfigPtr config()
```

Message settings

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

Set message config information

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function extension

```cpp
const JSON & extension()
```

Message extension information

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

Set message extension information

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function deliveryQos

```cpp
DeliveryQos deliveryQos()
```

QOS of messaging

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

Set QOS of messaging

**Parameters**:

* **qos** QOS of messaging

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function senderName

```cpp
const std::string & senderName()
```

Display name of message sender

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

Set display name of message sender

**Parameters**:

* **senderName** Message text content

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function groupAckCount

```cpp
int groupAckCount()
```

AckCount of read group messages

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

Set groupAckCount of read messages (an SDK internal calling interface that shall not be called by upper layer)

**Parameters**:

* **count** Set the number of read group messages

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function groupAckUnreadCount

```cpp
int groupAckUnreadCount()
```

AckCount of unread group messages

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

Set groupAckCount of unread messages (an SDK internal calling interface that shall not be called by upper layer)

**Parameters**:

* **count** Set the number of unread group messages

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function groupAckReadAll

```cpp
bool groupAckReadAll()
```

Whether all group messages are read

**Return**: bool

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function groupPlayAckCount

```cpp
int groupPlayAckCount()
```

AckCount of played group messages (valid only for messages with audio/video attachment)

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

Set groupAckCount of played messages (an SDK internal calling interface that shall not be called by upper layer) (valid only for messages with audio/video attachment)

**Parameters**:

* **count** Set the number of read group messages

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function groupPlayAckUnreadCount

```cpp
int groupPlayAckUnreadCount()
```

AckCount of unplayed group messages (valid only for messages with audio/video attachment)

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

Set groupAckCount of unplayed messages (an SDK internal calling interface that shall not be called by upper layer) (valid only for messages with audio/video attachment)

**Parameters**:

* **count** Set the number of unplayed group messages

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function groupPlayAckReadAll

```cpp
bool groupPlayAckReadAll()
```

Whether all group messages have been played

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

Set message diffusion priority, default 0. 0 means diffusion, and the smaller the number, the more diffused.

**Parameters**:

* **priority** Set the number of unread group messages

Value range 0-10. The default level of messages sent by ordinary users in chatroom is 5, which can be discarded. Admin level defaults to 0 and will not be discarded. Other values can be set according to business.

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function priority

```cpp
int priority()
```

Message diffusion priority

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

Set whether the message is a push.

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>

```

### function isPushMessage

```cpp
bool isPushMessage()
```

Whether the message is a push

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

Create a text message

**Parameters**:

* **from** Message sender
* **to** Message receiver
* **type** Message type
* **conversationId** Conversation id
* **content** Message content

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

Create a sent-attachment message

**Parameters**:

* **from** Message sender
* **to** Message receiver
* **type** Message type
* **conversationId** Conversation id
* **attachment** Attachment

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

Create a sent command message (command message holds command information in a content field or an extension field)

**Parameters**:

* **from** Message sender
* **to** Message receiver
* **type** Message type
* **conversationId** Conversation id
* **content** Message content

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

Create a forwarding message

**Parameters**:

* **msg** Message to forward
* **from** Message sender
* **to** Message receiver
* **type** Message type
* **conversationId** Conversation id

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessage'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
