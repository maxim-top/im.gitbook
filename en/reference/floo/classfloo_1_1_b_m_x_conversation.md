---
title: floo::BMXConversation
summary: Conversation
---

# floo::BMXConversation

Conversation

`#include <bmx_conversation.h>`

Inherits from BMXBaseObject

## Public Types

|            | Name                                                                                                                                       |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| enum class | <p><a href="classfloo_1_1_b_m_x_conversation.md#enum-type"><strong>Type</strong></a> { Single, Group, System}<br>Conversation type</p>     |
| enum class | <p><a href="classfloo_1_1_b_m_x_conversation.md#enum-direction"><strong>Direction</strong></a> { Up, Down}<br>Message search direction</p> |

## Public Functions

|                                                                     | Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual                                                             | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-~bmxconversation"><strong>~BMXConversation</strong></a>()<br>Destructor</p>                                                                                                                                                                                                                                                                                                                                                                                    |
| virtual int64\_t                                                    | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-conversationid"><strong>conversationId</strong></a>() =0<br>Conversation Id</p>                                                                                                                                                                                                                                                                                                                                                                                |
| virtual [Type](classfloo\_1\_1\_b\_m\_x\_conversation.md#enum-type) | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-type"><strong>type</strong></a>() =0<br>Conversation type</p>                                                                                                                                                                                                                                                                                                                                                                                                  |
| virtual BMXMessagePtr                                               | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-lastmsg"><strong>lastMsg</strong></a>() =0<br>Latest message</p>                                                                                                                                                                                                                                                                                                                                                                                               |
| virtual int32\_t                                                    | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-unreadnumber"><strong>unreadNumber</strong></a>() =0<br>Number of unread messages</p>                                                                                                                                                                                                                                                                                                                                                                          |
| virtual int32\_t                                                    | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-messagecount"><strong>messageCount</strong></a>() =0<br>Total number of messages in conversation</p>                                                                                                                                                                                                                                                                                                                                                           |
| virtual bool                                                        | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-ismutenotification"><strong>isMuteNotification</strong></a>() =0<br>Whether the user is alerted to the message, without which the conversation total number of unread messages does not count this conversation.</p>                                                                                                                                                                                                                                           |
| virtual const JSON &                                                | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-extension"><strong>extension</strong></a>() =0<br>Extension information</p>                                                                                                                                                                                                                                                                                                                                                                                    |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-setextension"><strong>setExtension</strong></a>(const std::string &#x26; ext) =0<br>Set the Extension information</p>                                                                                                                                                                                                                                                                                                                                          |
| virtual const std::string &                                         | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-editmessage"><strong>editMessage</strong></a>() =0<br>Edit message</p>                                                                                                                                                                                                                                                                                                                                                                                         |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-seteditmessage"><strong>setEditMessage</strong></a>(const std::string &#x26; editMessage) =0<br>Set the Edit Message</p>                                                                                                                                                                                                                                                                                                                                       |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-setmessageplayedstatus"><strong>setMessagePlayedStatus</strong></a>(BMXMessagePtr msg, bool status) =0<br>Set message playback state (valid only for voice/video messages)</p>                                                                                                                                                                                                                                                                                 |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-setmessagereadstatus"><strong>setMessageReadStatus</strong></a>(BMXMessagePtr msg, bool status) =0<br>Set message unread state, update unread message-number</p>                                                                                                                                                                                                                                                                                               |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-setallmessagesread"><strong>setAllMessagesRead</strong></a>() =0<br>Set all messages to read, update number of unread messages</p>                                                                                                                                                                                                                                                                                                                             |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-updatemessageextension"><strong>updateMessageExtension</strong></a>(BMXMessagePtr msg) =0<br>Update the extend field info of a database-stored message</p>                                                                                                                                                                                                                                                                                                     |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-insertmessage"><strong>insertMessage</strong></a>(BMXMessagePtr msg) =0<br>Insert a message</p>                                                                                                                                                                                                                                                                                                                                                                |
| virtual BMXMessagePtr                                               | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-loadmessage"><strong>loadMessage</strong></a>(int64_t msgId) =0<br>Read a message</p>                                                                                                                                                                                                                                                                                                                                                                          |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-removeallmessages"><strong>removeAllMessages</strong></a>() =0<br>Delete all messages in sesstion</p>                                                                                                                                                                                                                                                                                                                                                          |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-loadmessages"><strong>loadMessages</strong></a>(int64_t refMsgId, size_t size, BMXMessageList &#x26; result, <a href="classfloo_1_1_b_m_x_conversation.md#enum-direction">Direction</a> =<a href="classfloo_1_1_b_m_x_conversation.md#enumvalue-up">Direction::Up</a>) =0<br>Load message, starting with latest if not specified</p>                                                                                                                           |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-searchmessagesbykeywords"><strong>searchMessagesByKeyWords</strong></a>(const std::string &#x26; keywords, int64_t refTime, size_t size, BMXMessageList &#x26; result, <a href="classfloo_1_1_b_m_x_conversation.md#enum-direction">Direction</a> =<a href="classfloo_1_1_b_m_x_conversation.md#enumvalue-up">Direction::Up</a>) =0<br>Search for messages, starting with latest if not specified</p>                                                          |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-searchmessages"><strong>searchMessages</strong></a>(const std::string &#x26; keywords, int64_t refTime, size_t size, BMXMessageList &#x26; result, <a href="classfloo_1_1_b_m_x_conversation.md#enum-direction">Direction</a> =<a href="classfloo_1_1_b_m_x_conversation.md#enumvalue-up">Direction::Up</a>) =0<br>Deprecated.</p>                                                                                                                             |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-searchmessagesbytype"><strong>searchMessagesByType</strong></a>(<a href="classfloo_1_1_b_m_x_message.md#enum-contenttype">BMXMessage::ContentType</a> type, int64_t refTime, size_t size, BMXMessageList &#x26; result, <a href="classfloo_1_1_b_m_x_conversation.md#enum-direction">Direction</a> =<a href="classfloo_1_1_b_m_x_conversation.md#enumvalue-up">Direction::Up</a>) =0<br>Search for messages by type, starting with latest if not specified</p> |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-searchmessages"><strong>searchMessages</strong></a>(<a href="classfloo_1_1_b_m_x_message.md#enum-contenttype">BMXMessage::ContentType</a> type, int64_t refTime, size_t size, BMXMessageList &#x26; result, <a href="classfloo_1_1_b_m_x_conversation.md#enum-direction">Direction</a> =<a href="classfloo_1_1_b_m_x_conversation.md#enumvalue-up">Direction::Up</a>) =0<br>Deprecated.</p>                                                                    |
| virtual BMXErrorCode                                                | <p><a href="classfloo_1_1_b_m_x_conversation.md#function-refreshconversation"><strong>refreshConversation</strong></a>() =0<br>Read the total message-number from current conversation of the database, forces to update the total message-number and unread message-number.</p>                                                                                                                                                                                                                                        |

## Protected Functions

|   | Name                                                                                        |
| - | ------------------------------------------------------------------------------------------- |
|   | [**BMXConversation**](classfloo\_1\_1\_b\_m\_x\_conversation.md#function-bmxconversation)() |

## Public Types Documentation

### enum Type

| Enumerator | Value | Description         |
| ---------- | ----- | ------------------- |
| Single     |       | Single chat         |
| Group      |       | Group chat          |
| System     |       | System notification |

Conversation type

### enum Direction

| Enumerator | Value | Description         |
| ---------- | ----- | ------------------- |
| Up         |       | Fetch older message |
| Down       |       | Fetch newer message |

Message search direction

## Public Functions Documentation

### function \~BMXConversation

```cpp
inline virtual ~BMXConversation()
```

Destructor

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function conversationId

```cpp
virtual int64_t conversationId() =0
```

Conversation Id

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function type

```cpp
virtual Type type() =0
```

Conversation type

**Return**: Type

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function lastMsg

```cpp
virtual BMXMessagePtr lastMsg() =0
```

Latest message

**Return**: BMXMessagePtr

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function unreadNumber

```cpp
virtual int32_t unreadNumber() =0
```

Number of unread messages

**Return**: int32\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function messageCount

```cpp
virtual int32_t messageCount() =0
```

Total number of messages in conversation

**Return**: int32\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function isMuteNotification

```cpp
virtual bool isMuteNotification() =0
```

Whether the user is alerted to the message, without which the conversation total number of unread messages does not count this conversation.

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function extension

```cpp
virtual const JSON & extension() =0
```

Extension information

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function setExtension

```cpp
virtual BMXErrorCode setExtension(
    const std::string & ext
) =0
```

Set the Extension information

**Parameters**:

* **ext** Conversation extension message

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function editMessage

```cpp
virtual const std::string & editMessage() =0
```

Edit message

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function setEditMessage

```cpp
virtual BMXErrorCode setEditMessage(
    const std::string & editMessage
) =0
```

Set the Edit Message

**Parameters**:

* **editMessage** Text message being edited by conversation

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function setMessagePlayedStatus

```cpp
virtual BMXErrorCode setMessagePlayedStatus(
    BMXMessagePtr msg,
    bool status
) =0
```

Set message playback state (valid only for voice/video messages)

**Parameters**:

* **msg** Message for which playback state needs to be set
* **status** Whether the message has been played

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function setMessageReadStatus

```cpp
virtual BMXErrorCode setMessageReadStatus(
    BMXMessagePtr msg,
    bool status
) =0
```

Set message unread state, update unread message-number

**Parameters**:

* **msg** Message for which the read state needs to be set
* **status** Whether the message is set to read

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function setAllMessagesRead

```cpp
virtual BMXErrorCode setAllMessagesRead() =0
```

Set all messages to read, update number of unread messages

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function updateMessageExtension

```cpp
virtual BMXErrorCode updateMessageExtension(
    BMXMessagePtr msg
) =0
```

Update the extend field info of a database-stored message

**Parameters**:

* **msg** The message that needs to change the extension information when the msg section has updated its extension field

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function insertMessage

```cpp
virtual BMXErrorCode insertMessage(
    BMXMessagePtr msg
) =0
```

Insert a message

**Parameters**:

* **msg** Inserted message

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function loadMessage

```cpp
virtual BMXMessagePtr loadMessage(
    int64_t msgId
) =0
```

Read a message

**Parameters**:

* **msgId** Message id of the message to read

**Return**: BMXMessagePtr

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function removeAllMessages

```cpp
virtual BMXErrorCode removeAllMessages() =0
```

Delete all messages in sesstion

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function loadMessages

```cpp
virtual BMXErrorCode loadMessages(
    int64_t refMsgId,
    size_t size,
    BMXMessageList & result,
    Direction  =Direction::Up
) =0
```

Load message, starting with latest if not specified

**Parameters**:

* **refMsgId** Start id of the message to load
* **size** Maximum number of searched messages
* **result** List of loaded messages returned by database
* **Direction** Message loading direction, default to load earlier messages

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function searchMessagesByKeyWords

```cpp
virtual BMXErrorCode searchMessagesByKeyWords(
    const std::string & keywords,
    int64_t refTime,
    size_t size,
    BMXMessageList & result,
    Direction  =Direction::Up
) =0
```

Search for messages, starting with latest if not specified

**Parameters**:

* **keywords** Keyword for search message
* **refTime** Start time of message search
* **size** Maximum number of searched messages
* **result** List of searched message results
* **Direction** Message search direction, default (Direction::Up)means search from earlier messages.

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function searchMessages

```cpp
virtual BMXErrorCode searchMessages(
    const std::string & keywords,
    int64_t refTime,
    size_t size,
    BMXMessageList & result,
    Direction  =Direction::Up
) =0
```

Deprecated.

**Parameters**:

* **keywords** Keyword for search message
* **refTime** Start time of message search
* **size** Maximum number of searched messages
* **result** List of searched message results
* **Direction** Message search direction, default (Direction::Up)means search from earlier messages.

**Return**: BMXErrorCode

use searchMessagesByKeyWords instead.

Search for messages, starting with latest if not specified

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function searchMessagesByType

```cpp
virtual BMXErrorCode searchMessagesByType(
    BMXMessage::ContentType type,
    int64_t refTime,
    size_t size,
    BMXMessageList & result,
    Direction  =Direction::Up
) =0
```

Search for messages by type, starting with latest if not specified

**Parameters**:

* **type** Type of search message
* **refTime** Start time of message search
* **size** Maximum number of searched messages
* **result** List of searched message results
* **Direction** Message search direction, default (Direction::Up)means search from earlier messages.

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function searchMessages

```cpp
virtual BMXErrorCode searchMessages(
    BMXMessage::ContentType type,
    int64_t refTime,
    size_t size,
    BMXMessageList & result,
    Direction  =Direction::Up
) =0
```

Deprecated.

**Parameters**:

* **type** Type of search message
* **refTime** Start time of message search
* **size** Maximum number of searched messages
* **result** List of searched message results
* **Direction** Message search direction, default (Direction::Up)means search from earlier messages.

**Return**: BMXErrorCode

use searchMessagesByType instead.

Search for messages by type, starting with latest if not specified

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function refreshConversation

```cpp
virtual BMXErrorCode refreshConversation() =0
```

Read the total message-number from current conversation of the database, forces to update the total message-number and unread message-number.

**Return**: BMXErrorCode

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```

### function BMXConversation

```cpp
inline BMXConversation()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXConversation'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
