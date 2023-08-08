---
title: im::floo::floolib::BMXConversation
summary: Conversation
---

# im::floo::floolib::BMXConversation

Conversation

Inherits from BMXBaseObject

## Public Functions

|                                                                         | Name                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void                                                       | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md#function-delete)()                                                                                                                                                                                                                                                                               |
| long                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-conversationid"><strong>conversationId</strong></a>()<br>Conversation Id</p>                                                                                                                                                                                                                       |
| BMXConversation.Type                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-type"><strong>type</strong></a>()<br>Conversation type</p>                                                                                                                                                                                                                                         |
| [BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md) | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-lastmsg"><strong>lastMsg</strong></a>()<br>Latest message</p>                                                                                                                                                                                                                                      |
| int                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-unreadnumber"><strong>unreadNumber</strong></a>()<br>Number of unread messages</p>                                                                                                                                                                                                                 |
| int                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-messagecount"><strong>messageCount</strong></a>()<br>Total number of messages in conversation</p>                                                                                                                                                                                                  |
| boolean                                                                 | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-ismutenotification"><strong>isMuteNotification</strong></a>()<br>Whether the user is alerted to the message, without which the conversation total number of unread messages does not count this conversation.</p>                                                                                  |
| String                                                                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-extension"><strong>extension</strong></a>()<br>Extension information</p>                                                                                                                                                                                                                           |
| \[BMXErrorCode]                                                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-setextension"><strong>setExtension</strong></a>(String ext)<br>Set the Extension information</p>                                                                                                                                                                                                   |
| String                                                                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-editmessage"><strong>editMessage</strong></a>()<br>Edit message</p>                                                                                                                                                                                                                                |
| \[BMXErrorCode]                                                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-seteditmessage"><strong>setEditMessage</strong></a>(String editMessage)<br>Set the Edit Message</p>                                                                                                                                                                                                |
| \[BMXErrorCode]                                                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessagesbykeywords"><strong>searchMessagesByKeyWords</strong></a>(String keywords, long refTime, long size, BMXMessageList result, BMXConversation.Direction arg4)<br>Search for messages, starting with latest if not specified</p>                                                         |
| \[BMXErrorCode]                                                         | [**searchMessagesByKeyWords**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md#function-searchmessagesbykeywords)(String keywords, long refTime, long size, BMXMessageList result)                                                                                                                                                                            |
| \[BMXErrorCode]                                                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessagesbytype"><strong>searchMessagesByType</strong></a>(BMXMessage.ContentType type, long refTime, long size, BMXMessageList result, BMXConversation.Direction arg4)<br>Search for messages by type, starting with latest if not specified</p>                                             |
| \[BMXErrorCode]                                                         | [**searchMessagesByType**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md#function-searchmessagesbytype)(BMXMessage.ContentType type, long refTime, long size, BMXMessageList result)                                                                                                                                                                        |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-setmessageplayedstatus"><strong>setMessagePlayedStatus</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, final boolean status, final BMXCallBack callBack)<br>Set message playback state (valid only for voice/video messages)</p>                  |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-setmessagereadstatus"><strong>setMessageReadStatus</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, final boolean status, final BMXCallBack callBack)<br>Set message unread state, update unread message-number</p>                                |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-setallmessagesread"><strong>setAllMessagesRead</strong></a>(final BMXCallBack callBack)<br>Set all messages to read, update number of unread messages</p>                                                                                                                                          |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-updatemessageextension"><strong>updateMessageExtension</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, final BMXCallBack callBack)<br>Update the extend field info of a database-stored message</p>                                               |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-insertmessage"><strong>insertMessage</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, final BMXCallBack callBack)<br>Insert a message</p>                                                                                                          |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-loadmessage"><strong>loadMessage</strong></a>(final long msgId, final BMXDataCallBack&#x3C; <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> > callBack)<br>Read a message</p>                                                                                             |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-removeallmessages"><strong>removeAllMessages</strong></a>(final BMXCallBack callBack)<br>Delete all messages in sesstion</p>                                                                                                                                                                       |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-loadmessages"><strong>loadMessages</strong></a>(final long refMsgId, final long size, final BMXConversation.Direction arg3, final BMXDataCallBack&#x3C; BMXMessageList > callBack)<br>Load message, starting with latest if not specified</p>                                                      |
| void                                                                    | [**loadMessages**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md#function-loadmessages)(final long refMsgId, final long size, final BMXDataCallBack< BMXMessageList > callBack)                                                                                                                                                                             |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessages"><strong>searchMessages</strong></a>(final String keywords, final long refTime, final long size, final BMXConversation.Direction arg4, final BMXDataCallBack&#x3C; BMXMessageList > callBack)<br>Search for messages, starting with latest if not specified</p>                     |
| void                                                                    | [**searchMessages**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md#function-searchmessages)(final String keywords, final long refTime, final long size, final BMXDataCallBack< BMXMessageList > callBack)                                                                                                                                                   |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessages"><strong>searchMessages</strong></a>(final BMXMessage.ContentType type, final long refTime, final long size, final BMXConversation.Direction arg4, final BMXDataCallBack&#x3C; BMXMessageList > callBack)<br>Search for messages by type, starting with latest if not specified</p> |
| void                                                                    | [**searchMessages**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md#function-searchmessages)(final BMXMessage.ContentType type, final long refTime, final long size, final BMXDataCallBack< BMXMessageList > callBack)                                                                                                                                       |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-refreshconversation"><strong>refreshConversation</strong></a>(final BMXCallBack callBack)<br>Read the total message-number from current conversation of the database, forces to update the total message-number and unread message-number.</p>                                                     |

## Protected Functions

|      | Name                                                                                                                                                                                  |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXConversation**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md#function-bmxconversation)(long cPtr, boolean cMemoryOwn)                                         |
| void | [**finalize**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md#function-finalize)()                                                                                    |
| long | [**getCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md#function-getcptr)([BMXConversation](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md) obj) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function conversationId

```java
inline long conversationId()
```

Conversation Id

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function type

```java
inline BMXConversation.Type type()
```

Conversation type

**Return**: \[Type]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function lastMsg

```java
inline BMXMessage lastMsg()
```

Latest message

**Return**: BMXMessagePtr

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function unreadNumber

```java
inline int unreadNumber()
```

Number of unread messages

**Return**: int32\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function messageCount

```java
inline int messageCount()
```

Total number of messages in conversation

**Return**: int32\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function isMuteNotification

```java
inline boolean isMuteNotification()
```

Whether the user is alerted to the message, without which the conversation total number of unread messages does not count this conversation.

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function extension

```java
inline String extension()
```

Extension information

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function setExtension

```java
inline BMXErrorCode setExtension(
    String ext
)
```

Set the Extension information

**Parameters**:

* **ext** Conversation extension message

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function editMessage

```java
inline String editMessage()
```

Edit message

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function setEditMessage

```java
inline BMXErrorCode setEditMessage(
    String editMessage
)
```

Set the Edit Message

**Parameters**:

* **editMessage** Text message being edited by conversation

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function searchMessagesByKeyWords

```java
inline BMXErrorCode searchMessagesByKeyWords(
    String keywords,
    long refTime,
    long size,
    BMXMessageList result,
    BMXConversation.Direction arg4
)
```

Search for messages, starting with latest if not specified

**Parameters**:

* **keywords** Keyword for search message
* **refTime** Start time of message search
* **size** Maximum number of searched messages
* **result** List of searched message results
* **arg4** Message search direction, default (Direction::Up)means search from earlier messages.

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function searchMessagesByKeyWords

```java
inline BMXErrorCode searchMessagesByKeyWords(
    String keywords,
    long refTime,
    long size,
    BMXMessageList result
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function searchMessagesByType

```java
inline BMXErrorCode searchMessagesByType(
    BMXMessage.ContentType type,
    long refTime,
    long size,
    BMXMessageList result,
    BMXConversation.Direction arg4
)
```

Search for messages by type, starting with latest if not specified

**Parameters**:

* **type** Type of search message
* **refTime** Start time of message search
* **size** Maximum number of searched messages
* **result** List of searched message results
* **arg4** Message search direction, default (Direction::Up)means search from earlier messages.

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function searchMessagesByType

```java
inline BMXErrorCode searchMessagesByType(
    BMXMessage.ContentType type,
    long refTime,
    long size,
    BMXMessageList result
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function setMessagePlayedStatus

```java
inline void setMessagePlayedStatus(
    final BMXMessage msg,
    final boolean status,
    final BMXCallBack callBack
)
```

Set message playback state (valid only for voice/video messages)

**Parameters**:

* **msg** Message for which playback state needs to be set
* **status** Whether the message has been played
* **callBack** Callback

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function setMessageReadStatus

```java
inline void setMessageReadStatus(
    final BMXMessage msg,
    final boolean status,
    final BMXCallBack callBack
)
```

Set message unread state, update unread message-number

**Parameters**:

* **msg** Message for which the read state needs to be set
* **status** Whether the message is set to read
* **callBack** Callback

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function setAllMessagesRead

```java
inline void setAllMessagesRead(
    final BMXCallBack callBack
)
```

Set all messages to read, update number of unread messages

**Parameters**:

* **callBack** Callback

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function updateMessageExtension

```java
inline void updateMessageExtension(
    final BMXMessage msg,
    final BMXCallBack callBack
)
```

Update the extend field info of a database-stored message

**Parameters**:

* **msg** The message that needs to change the extension information when the msg section has updated its extension field
* **callBack** Callback

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function insertMessage

```java
inline void insertMessage(
    final BMXMessage msg,
    final BMXCallBack callBack
)
```

Insert a message

**Parameters**:

* **msg** Inserted message
* **callBack** Callback

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function loadMessage

```java
inline void loadMessage(
    final long msgId,
    final BMXDataCallBack< BMXMessage > callBack
)
```

Read a message

**Parameters**:

* **msgId** Message id of the message to read
* **callBack** Callback

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function removeAllMessages

```java
inline void removeAllMessages(
    final BMXCallBack callBack
)
```

Delete all messages in sesstion

**Parameters**:

* **callBack** Callback

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function loadMessages

```java
inline void loadMessages(
    final long refMsgId,
    final long size,
    final BMXConversation.Direction arg3,
    final BMXDataCallBack< BMXMessageList > callBack
)
```

Load message, starting with latest if not specified

**Parameters**:

* **refMsgId** Start id of the message to load
* **size** Maximum number of searched messages
* **arg3** Message loading direction, default to load earlier messages
* **callBack** Callback

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function loadMessages

```java
inline void loadMessages(
    final long refMsgId,
    final long size,
    final BMXDataCallBack< BMXMessageList > callBack
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function searchMessages

```java
inline void searchMessages(
    final String keywords,
    final long refTime,
    final long size,
    final BMXConversation.Direction arg4,
    final BMXDataCallBack< BMXMessageList > callBack
)
```

Search for messages, starting with latest if not specified

**Parameters**:

* **keywords** Keyword for search message
* **refTime** Start time of message search
* **size** Maximum number of searched messages
* **arg4** Message search direction, default (Direction::Up)means search from earlier messages.
* **callBack** Callback

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function searchMessages

```java
inline void searchMessages(
    final String keywords,
    final long refTime,
    final long size,
    final BMXDataCallBack< BMXMessageList > callBack
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function searchMessages

```java
inline void searchMessages(
    final BMXMessage.ContentType type,
    final long refTime,
    final long size,
    final BMXConversation.Direction arg4,
    final BMXDataCallBack< BMXMessageList > callBack
)
```

Search for messages by type, starting with latest if not specified

**Parameters**:

* **type** Type of search message
* **refTime** Start time of message search
* **size** Maximum number of searched messages
* **arg4** Message search direction, default (Direction::Up)means search from earlier messages.
* **callBack** Callback

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function searchMessages

```java
inline void searchMessages(
    final BMXMessage.ContentType type,
    final long refTime,
    final long size,
    final BMXDataCallBack< BMXMessageList > callBack
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function refreshConversation

```java
inline void refreshConversation(
    final BMXCallBack callBack
)
```

Read the total message-number from current conversation of the database, forces to update the total message-number and unread message-number.

**Parameters**:

* **callBack** Callback

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function BMXConversation

```java
inline BMXConversation(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function finalize

```java
inline void finalize()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function getCPtr

```java
static inline long getCPtr(
    BMXConversation obj
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```



Updated on 2022-01-26 at 17:18:31 +0800
