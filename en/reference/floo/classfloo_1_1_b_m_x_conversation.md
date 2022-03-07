---
title: floo::BMXConversation
summary: Conversation 

---

# floo::BMXConversation



Conversation 


`#include <bmx_conversation.h>`

Inherits from BMXBaseObject

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[Type](classfloo_1_1_b_m_x_conversation.md#enum-type)** { Single, Group, System}<br>Conversation type  |
| enum class| **[Direction](classfloo_1_1_b_m_x_conversation.md#enum-direction)** { Up, Down}<br>Message search direction  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXConversation](classfloo_1_1_b_m_x_conversation.md#function-~bmxconversation)**()<br>Destructor  |
| virtual int64_t | **[conversationId](classfloo_1_1_b_m_x_conversation.md#function-conversationid)**() =0<br>Conversation Id  |
| virtual [Type](classfloo_1_1_b_m_x_conversation.md#enum-type) | **[type](classfloo_1_1_b_m_x_conversation.md#function-type)**() =0<br>Conversation type  |
| virtual BMXMessagePtr | **[lastMsg](classfloo_1_1_b_m_x_conversation.md#function-lastmsg)**() =0<br>Latest message  |
| virtual int32_t | **[unreadNumber](classfloo_1_1_b_m_x_conversation.md#function-unreadnumber)**() =0<br>Number of unread messages  |
| virtual int32_t | **[messageCount](classfloo_1_1_b_m_x_conversation.md#function-messagecount)**() =0<br>Total number of messages in conversation  |
| virtual bool | **[isMuteNotification](classfloo_1_1_b_m_x_conversation.md#function-ismutenotification)**() =0<br>Whether the user is alerted to the message, without which the conversation total number of unread messages does not count this conversation.  |
| virtual const JSON & | **[extension](classfloo_1_1_b_m_x_conversation.md#function-extension)**() =0<br>Extension information  |
| virtual BMXErrorCode | **[setExtension](classfloo_1_1_b_m_x_conversation.md#function-setextension)**(const std::string & ext) =0<br>Set the Extension information  |
| virtual const std::string & | **[editMessage](classfloo_1_1_b_m_x_conversation.md#function-editmessage)**() =0<br>Edit message  |
| virtual BMXErrorCode | **[setEditMessage](classfloo_1_1_b_m_x_conversation.md#function-seteditmessage)**(const std::string & editMessage) =0<br>Set the Edit Message  |
| virtual BMXErrorCode | **[setMessagePlayedStatus](classfloo_1_1_b_m_x_conversation.md#function-setmessageplayedstatus)**(BMXMessagePtr msg, bool status) =0<br>Set message playback state (valid only for voice/video messages)  |
| virtual BMXErrorCode | **[setMessageReadStatus](classfloo_1_1_b_m_x_conversation.md#function-setmessagereadstatus)**(BMXMessagePtr msg, bool status) =0<br>Set message unread state, update unread message-number  |
| virtual BMXErrorCode | **[setAllMessagesRead](classfloo_1_1_b_m_x_conversation.md#function-setallmessagesread)**() =0<br>Set all messages to read, update number of unread messages  |
| virtual BMXErrorCode | **[updateMessageExtension](classfloo_1_1_b_m_x_conversation.md#function-updatemessageextension)**(BMXMessagePtr msg) =0<br>Update the extend field info of a database-stored message  |
| virtual BMXErrorCode | **[insertMessage](classfloo_1_1_b_m_x_conversation.md#function-insertmessage)**(BMXMessagePtr msg) =0<br>Insert a message  |
| virtual BMXMessagePtr | **[loadMessage](classfloo_1_1_b_m_x_conversation.md#function-loadmessage)**(int64_t msgId) =0<br>Read a message  |
| virtual BMXErrorCode | **[removeAllMessages](classfloo_1_1_b_m_x_conversation.md#function-removeallmessages)**() =0<br>Delete all messages in sesstion  |
| virtual BMXErrorCode | **[loadMessages](classfloo_1_1_b_m_x_conversation.md#function-loadmessages)**(int64_t refMsgId, size_t size, BMXMessageList & result, [Direction](classfloo_1_1_b_m_x_conversation.md#enum-direction)  =[Direction::Up](classfloo_1_1_b_m_x_conversation.md#enumvalue-up)) =0<br>Load message, starting with latest if not specified  |
| virtual BMXErrorCode | **[searchMessagesByKeyWords](classfloo_1_1_b_m_x_conversation.md#function-searchmessagesbykeywords)**(const std::string & keywords, int64_t refTime, size_t size, BMXMessageList & result, [Direction](classfloo_1_1_b_m_x_conversation.md#enum-direction)  =[Direction::Up](classfloo_1_1_b_m_x_conversation.md#enumvalue-up)) =0<br>Search for messages, starting with latest if not specified  |
| virtual BMXErrorCode | **[searchMessages](classfloo_1_1_b_m_x_conversation.md#function-searchmessages)**(const std::string & keywords, int64_t refTime, size_t size, BMXMessageList & result, [Direction](classfloo_1_1_b_m_x_conversation.md#enum-direction)  =[Direction::Up](classfloo_1_1_b_m_x_conversation.md#enumvalue-up)) =0<br>Deprecated.  |
| virtual BMXErrorCode | **[searchMessagesByType](classfloo_1_1_b_m_x_conversation.md#function-searchmessagesbytype)**([BMXMessage::ContentType](classfloo_1_1_b_m_x_message.md#enum-contenttype) type, int64_t refTime, size_t size, BMXMessageList & result, [Direction](classfloo_1_1_b_m_x_conversation.md#enum-direction)  =[Direction::Up](classfloo_1_1_b_m_x_conversation.md#enumvalue-up)) =0<br>Search for messages by type, starting with latest if not specified  |
| virtual BMXErrorCode | **[searchMessages](classfloo_1_1_b_m_x_conversation.md#function-searchmessages)**([BMXMessage::ContentType](classfloo_1_1_b_m_x_message.md#enum-contenttype) type, int64_t refTime, size_t size, BMXMessageList & result, [Direction](classfloo_1_1_b_m_x_conversation.md#enum-direction)  =[Direction::Up](classfloo_1_1_b_m_x_conversation.md#enumvalue-up)) =0<br>Deprecated.  |
| virtual BMXErrorCode | **[refreshConversation](classfloo_1_1_b_m_x_conversation.md#function-refreshconversation)**() =0<br>Read the total message-number from current conversation of the database, forces to update the total message-number and unread message-number.  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXConversation](classfloo_1_1_b_m_x_conversation.md#function-bmxconversation)**() |

## Public Types Documentation

### enum Type

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Single | | Single chat   |
| Group | | Group chat   |
| System | | System notification   |



Conversation type 

### enum Direction

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Up | | Fetch older message   |
| Down | | Fetch newer message   |



Message search direction 

## Public Functions Documentation

### function ~BMXConversation

```cpp
inline virtual ~BMXConversation()
```

Destructor 

### function conversationId

```cpp
virtual int64_t conversationId() =0
```

Conversation Id 

**Return**: int64_t 

### function type

```cpp
virtual Type type() =0
```

Conversation type 

**Return**: Type 

### function lastMsg

```cpp
virtual BMXMessagePtr lastMsg() =0
```

Latest message 

**Return**: BMXMessagePtr 

### function unreadNumber

```cpp
virtual int32_t unreadNumber() =0
```

Number of unread messages 

**Return**: int32_t 

### function messageCount

```cpp
virtual int32_t messageCount() =0
```

Total number of messages in conversation 

**Return**: int32_t 

### function isMuteNotification

```cpp
virtual bool isMuteNotification() =0
```

Whether the user is alerted to the message, without which the conversation total number of unread messages does not count this conversation. 

**Return**: bool 

### function extension

```cpp
virtual const JSON & extension() =0
```

Extension information 

**Return**: JSON(std::string) 

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

### function editMessage

```cpp
virtual const std::string & editMessage() =0
```

Edit message 

**Return**: std::string 

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

### function setAllMessagesRead

```cpp
virtual BMXErrorCode setAllMessagesRead() =0
```

Set all messages to read, update number of unread messages 

**Return**: BMXErrorCode 

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

### function removeAllMessages

```cpp
virtual BMXErrorCode removeAllMessages() =0
```

Delete all messages in sesstion 

**Return**: BMXErrorCode 

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


### function refreshConversation

```cpp
virtual BMXErrorCode refreshConversation() =0
```

Read the total message-number from current conversation of the database, forces to update the total message-number and unread message-number. 

**Return**: BMXErrorCode 

## Protected Functions Documentation

### function BMXConversation

```cpp
inline BMXConversation()
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800