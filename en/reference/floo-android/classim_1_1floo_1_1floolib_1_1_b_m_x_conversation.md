---
title: im::floo::floolib::BMXConversation
summary: Conversation 

---

# im::floo::floolib::BMXConversation



Conversation 

Inherits from BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-delete)**() |
| long | **[conversationId](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-conversationid)**()<br>Conversation Id  |
| BMXConversation.Type | **[type](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-type)**()<br>Conversation type  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) | **[lastMsg](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-lastmsg)**()<br>Latest message  |
| int | **[unreadNumber](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-unreadnumber)**()<br>Number of unread messages  |
| int | **[messageCount](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-messagecount)**()<br>Total number of messages in conversation  |
| boolean | **[isMuteNotification](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-ismutenotification)**()<br>Whether the user is alerted to the message, without which the conversation total number of unread messages does not count this conversation.  |
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
| void | **[refreshConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-refreshconversation)**(final BMXCallBack callBack)<br>Read the total message-number from current conversation of the database, forces to update the total message-number and unread message-number.  |

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


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="delete" %}{% endlanying_code_snippet %}
```
### function conversationId

```java
inline long conversationId()
```

Conversation Id 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="conversationId" %}{% endlanying_code_snippet %}
```
### function type

```java
inline BMXConversation.Type type()
```

Conversation type 

**Return**: [Type]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="type" %}{% endlanying_code_snippet %}
```
### function lastMsg

```java
inline BMXMessage lastMsg()
```

Latest message 

**Return**: BMXMessagePtr 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="lastMsg" %}{% endlanying_code_snippet %}
```
### function unreadNumber

```java
inline int unreadNumber()
```

Number of unread messages 

**Return**: int32_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="unreadNumber" %}{% endlanying_code_snippet %}
```
### function messageCount

```java
inline int messageCount()
```

Total number of messages in conversation 

**Return**: int32_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="messageCount" %}{% endlanying_code_snippet %}
```
### function isMuteNotification

```java
inline boolean isMuteNotification()
```

Whether the user is alerted to the message, without which the conversation total number of unread messages does not count this conversation. 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="isMuteNotification" %}{% endlanying_code_snippet %}
```
### function extension

```java
inline String extension()
```

Extension information 

**Return**: JSON(std::string) 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="extension" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="setExtension" %}{% endlanying_code_snippet %}
```
### function editMessage

```java
inline String editMessage()
```

Edit message 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="editMessage" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="setEditMessage" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="searchMessagesByKeyWords" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="searchMessagesByKeyWords" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="searchMessagesByType" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="searchMessagesByType" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="setMessagePlayedStatus" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="setMessageReadStatus" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="setAllMessagesRead" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="updateMessageExtension" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="insertMessage" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="loadMessage" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="removeAllMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="loadMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="loadMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="searchMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="searchMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="searchMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="searchMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="refreshConversation" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="BMXConversation" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="finalize" %}{% endlanying_code_snippet %}
```
### function getCPtr

```java
static inline long getCPtr(
    BMXConversation obj
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800