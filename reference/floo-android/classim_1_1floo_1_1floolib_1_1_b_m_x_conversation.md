---
title: im::floo::floolib::BMXConversation
summary: Session 

---

# im::floo::floolib::BMXConversation



Session 

Inherits from BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-delete)**() |
| long | **[conversationId](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-conversationid)**()<br>Session Id  |
| BMXConversation.Type | **[type](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-type)**()<br>Session type  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) | **[lastMsg](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-lastmsg)**()<br>Latest message  |
| int | **[unreadNumber](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-unreadnumber)**()<br>Unread message-number  |
| int | **[messageCount](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-messagecount)**()<br>Total message-number in session  |
| boolean | **[isMuteNotification](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-ismutenotification)**()<br>Whether the user is alerted to the message, without which the session total unread-number does not count this session.  |
| String | **[extension](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-extension)**()<br>Extension information  |
| [BMXErrorCode] | **[setExtension](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-setextension)**(String ext)<br>Set the Extension information  |
| String | **[editMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-editmessage)**()<br>Edit message  |
| [BMXErrorCode] | **[setEditMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-seteditmessage)**(String editMessage)<br>Set the Edit Message  |
| [BMXErrorCode] | **[searchMessagesByKeyWords](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessagesbykeywords)**(String keywords, long refTime, long size, BMXMessageList result, BMXConversation.Direction arg4)<br>Search for messages, starting with latest if not specified  |
| [BMXErrorCode] | **[searchMessagesByKeyWords](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessagesbykeywords)**(String keywords, long refTime, long size, BMXMessageList result) |
| [BMXErrorCode] | **[searchMessagesByType](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessagesbytype)**(BMXMessage.ContentType type, long refTime, long size, BMXMessageList result, BMXConversation.Direction arg4)<br>Search for messages by type, starting with latest if not specified  |
| [BMXErrorCode] | **[searchMessagesByType](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessagesbytype)**(BMXMessage.ContentType type, long refTime, long size, BMXMessageList result) |
| void | **[setMessagePlayedStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-setmessageplayedstatus)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, final boolean status, final BMXCallBack callBack)<br>Set message playback state (valid only for voice/video messages)  |
| void | **[setMessageReadStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-setmessagereadstatus)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, final boolean status, final BMXCallBack callBack)<br>Set message unread state, update unread message-number  |
| void | **[setAllMessagesRead](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-setallmessagesread)**(final BMXCallBack callBack)<br>Set all messages to read, update number of unread messages  |
| void | **[updateMessageExtension](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-updatemessageextension)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, final BMXCallBack callBack)<br>Update the extend field info of a database-stored message  |
| void | **[insertMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-insertmessage)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, final BMXCallBack callBack)<br>Insert a message  |
| void | **[loadMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-loadmessage)**(final long msgId, final BMXDataCallBack< [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) > callBack)<br>Read a message  |
| void | **[removeAllMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-removeallmessages)**(final BMXCallBack callBack)<br>Delete all messages in sesstion  |
| void | **[loadMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-loadmessages)**(final long refMsgId, final long size, final BMXConversation.Direction arg3, final BMXDataCallBack< BMXMessageList > callBack)<br>Load message, starting with latest if not specified  |
| void | **[loadMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-loadmessages)**(final long refMsgId, final long size, final BMXDataCallBack< BMXMessageList > callBack) |
| void | **[searchMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessages)**(final String keywords, final long refTime, final long size, final BMXConversation.Direction arg4, final BMXDataCallBack< BMXMessageList > callBack)<br>Search for messages, starting with latest if not specified  |
| void | **[searchMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessages)**(final String keywords, final long refTime, final long size, final BMXDataCallBack< BMXMessageList > callBack) |
| void | **[searchMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessages)**(final BMXMessage.ContentType type, final long refTime, final long size, final BMXConversation.Direction arg4, final BMXDataCallBack< BMXMessageList > callBack)<br>Search for messages by type, starting with latest if not specified  |
| void | **[searchMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessages)**(final BMXMessage.ContentType type, final long refTime, final long size, final BMXDataCallBack< BMXMessageList > callBack) |
| void | **[refreshConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-refreshconversation)**(final BMXCallBack callBack)<br>Read the total message-number from current session of the database, forces to update the total message-number and unread message-number.  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-bmxconversation)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-getcptr)**([BMXConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md) obj) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


### function conversationId

```java
inline long conversationId()
```

Session Id 

**Return**: int64_t 

### function type

```java
inline BMXConversation.Type type()
```

Session type 

**Return**: [Type]

### function lastMsg

```java
inline BMXMessage lastMsg()
```

Latest message 

**Return**: BMXMessagePtr 

### function unreadNumber

```java
inline int unreadNumber()
```

Unread message-number 

**Return**: int32_t 

### function messageCount

```java
inline int messageCount()
```

Total message-number in session 

**Return**: int32_t 

### function isMuteNotification

```java
inline boolean isMuteNotification()
```

Whether the user is alerted to the message, without which the session total unread-number does not count this session. 

**Return**: bool 

### function extension

```java
inline String extension()
```

Extension information 

**Return**: JSON(std::string) 

### function setExtension

```java
inline BMXErrorCode setExtension(
    String ext
)
```

Set the Extension information 

**Parameters**: 

  * **ext** Session extension message 


**Return**: [BMXErrorCode]

### function editMessage

```java
inline String editMessage()
```

Edit message 

**Return**: std::string 

### function setEditMessage

```java
inline BMXErrorCode setEditMessage(
    String editMessage
)
```

Set the Edit Message 

**Parameters**: 

  * **editMessage** Text message being edited by session 


**Return**: [BMXErrorCode]

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
  * **size** Maximum number of loaded messages 
  * **result** List of searched message results 
  * **arg4** Message search direction, default (Direction::Up)means search from earlier messages. 


**Return**: [BMXErrorCode]

### function searchMessagesByKeyWords

```java
inline BMXErrorCode searchMessagesByKeyWords(
    String keywords,
    long refTime,
    long size,
    BMXMessageList result
)
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
  * **size** Maximum number of loaded messages 
  * **result** List of searched message results 
  * **arg4** Message search direction, default (Direction::Up)means search from earlier messages. 


**Return**: [BMXErrorCode]

### function searchMessagesByType

```java
inline BMXErrorCode searchMessagesByType(
    BMXMessage.ContentType type,
    long refTime,
    long size,
    BMXMessageList result
)
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


### function setAllMessagesRead

```java
inline void setAllMessagesRead(
    final BMXCallBack callBack
)
```

Set all messages to read, update number of unread messages 

**Parameters**: 

  * **callBack** Callback 


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


### function removeAllMessages

```java
inline void removeAllMessages(
    final BMXCallBack callBack
)
```

Delete all messages in sesstion 

**Parameters**: 

  * **callBack** Callback 


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
  * **size** Maximum number of loaded messages 
  * **arg3** Message loading direction, default to load earlier messages 
  * **callBack** Callback 


### function loadMessages

```java
inline void loadMessages(
    final long refMsgId,
    final long size,
    final BMXDataCallBack< BMXMessageList > callBack
)
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
  * **size** Maximum number of loaded messages 
  * **arg4** Message search direction, default (Direction::Up)means search from earlier messages. 
  * **callBack** Callback 


### function searchMessages

```java
inline void searchMessages(
    final String keywords,
    final long refTime,
    final long size,
    final BMXDataCallBack< BMXMessageList > callBack
)
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
  * **size** Maximum number of loaded messages 
  * **arg4** Message search direction, default (Direction::Up)means search from earlier messages. 
  * **callBack** Callback 


### function searchMessages

```java
inline void searchMessages(
    final BMXMessage.ContentType type,
    final long refTime,
    final long size,
    final BMXDataCallBack< BMXMessageList > callBack
)
```


### function refreshConversation

```java
inline void refreshConversation(
    final BMXCallBack callBack
)
```

Read the total message-number from current session of the database, forces to update the total message-number and unread message-number. 

**Parameters**: 

  * **callBack** Callback 


## Protected Functions Documentation

### function BMXConversation

```java
inline BMXConversation(
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
    BMXConversation obj
)
```


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800