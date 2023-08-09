---
title: im::floo::floolib::BMXConversation
summary: 会话 

---

# im::floo::floolib::BMXConversation



会话 

Inherits from BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-delete)**() |
| long | **[conversationId](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-conversationid)**()<br>会话Id  |
| BMXConversation.Type | **[type](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-type)**()<br>会话类型  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) | **[lastMsg](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-lastmsg)**()<br>最新消息  |
| int | **[unreadNumber](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-unreadnumber)**()<br>未读消息数  |
| int | **[messageCount](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-messagecount)**()<br>会话中所有消息的数量  |
| boolean | **[isMuteNotification](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-ismutenotification)**()<br>是否提醒用户消息,不提醒的情况下会话总未读数不会统计该会话计数。  |
| String | **[extension](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-extension)**()<br>扩展信息  |
| [BMXErrorCode] | **[setExtension](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-setextension)**(String ext)<br>设置扩展信息  |
| String | **[editMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-editmessage)**()<br>编辑消息  |
| [BMXErrorCode] | **[setEditMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-seteditmessage)**(String editMessage)<br>设置编辑消息  |
| [BMXErrorCode] | **[searchMessagesByKeyWords](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessagesbykeywords)**(String keywords, long refTime, long size, BMXMessageList result, BMXConversation.Direction arg4)<br>搜索消息，如果不指定则从最新消息开始  |
| [BMXErrorCode] | **[searchMessagesByKeyWords](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessagesbykeywords)**(String keywords, long refTime, long size, BMXMessageList result) |
| [BMXErrorCode] | **[searchMessagesByType](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessagesbytype)**(BMXMessage.ContentType type, long refTime, long size, BMXMessageList result, BMXConversation.Direction arg4)<br>按照类型搜索消息，如果不指定则从最新消息开始  |
| [BMXErrorCode] | **[searchMessagesByType](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessagesbytype)**(BMXMessage.ContentType type, long refTime, long size, BMXMessageList result) |
| void | **[setMessagePlayedStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-setmessageplayedstatus)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, final boolean status, final BMXCallBack callBack)<br>设置消息播放状态（只对语音/视频消息有效）  |
| void | **[setMessageReadStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-setmessagereadstatus)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, final boolean status, final BMXCallBack callBack)<br>设置消息未读状态，更新未读消息数  |
| void | **[setAllMessagesRead](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-setallmessagesread)**(final BMXCallBack callBack)<br>把所有消息设置为已读，更新未读消息数  |
| void | **[updateMessageExtension](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-updatemessageextension)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, final BMXCallBack callBack)<br>更新一条数据库存储消息的扩展字段信息  |
| void | **[insertMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-insertmessage)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, final BMXCallBack callBack)<br>插入一条消息  |
| void | **[loadMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-loadmessage)**(final long msgId, final BMXDataCallBack< [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) > callBack)<br>读取一条消息  |
| void | **[removeAllMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-removeallmessages)**(final BMXCallBack callBack)<br>删除会话中的所有消息  |
| void | **[loadMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-loadmessages)**(final long refMsgId, final long size, final BMXConversation.Direction arg3, final BMXDataCallBack< BMXMessageList > callBack)<br>加载消息，如果不指定则从最新消息开始  |
| void | **[loadMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-loadmessages)**(final long refMsgId, final long size, final BMXDataCallBack< BMXMessageList > callBack) |
| void | **[searchMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessages)**(final String keywords, final long refTime, final long size, final BMXConversation.Direction arg4, final BMXDataCallBack< BMXMessageList > callBack)<br>搜索消息，如果不指定则从最新消息开始  |
| void | **[searchMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessages)**(final String keywords, final long refTime, final long size, final BMXDataCallBack< BMXMessageList > callBack) |
| void | **[searchMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessages)**(final BMXMessage.ContentType type, final long refTime, final long size, final BMXConversation.Direction arg4, final BMXDataCallBack< BMXMessageList > callBack)<br>按照类型搜索消息，如果不指定则从最新消息开始  |
| void | **[searchMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessages)**(final BMXMessage.ContentType type, final long refTime, final long size, final BMXDataCallBack< BMXMessageList > callBack) |
| void | **[refreshConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-refreshconversation)**(final BMXCallBack callBack)<br>读取数据库当前会话所有消息数量，强制更新conversation的消息总数和未读消息数。  |

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

会话Id 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="conversationId" %}{% endlanying_code_snippet %}
```
### function type

```java
inline BMXConversation.Type type()
```

会话类型 

**Return**: [Type]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="type" %}{% endlanying_code_snippet %}
```
### function lastMsg

```java
inline BMXMessage lastMsg()
```

最新消息 

**Return**: BMXMessagePtr 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="lastMsg" %}{% endlanying_code_snippet %}
```
### function unreadNumber

```java
inline int unreadNumber()
```

未读消息数 

**Return**: int32_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="unreadNumber" %}{% endlanying_code_snippet %}
```
### function messageCount

```java
inline int messageCount()
```

会话中所有消息的数量 

**Return**: int32_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="messageCount" %}{% endlanying_code_snippet %}
```
### function isMuteNotification

```java
inline boolean isMuteNotification()
```

是否提醒用户消息,不提醒的情况下会话总未读数不会统计该会话计数。 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="isMuteNotification" %}{% endlanying_code_snippet %}
```
### function extension

```java
inline String extension()
```

扩展信息 

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

设置扩展信息 

**Parameters**: 

  * **ext** 会话扩展消息 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXConversation",function="setExtension" %}{% endlanying_code_snippet %}
```
### function editMessage

```java
inline String editMessage()
```

编辑消息 

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

设置编辑消息 

**Parameters**: 

  * **editMessage** 会话正在编辑的文本消息 


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

搜索消息，如果不指定则从最新消息开始 

**Parameters**: 

  * **keywords** 搜索消息的关键字 
  * **refTime** 搜索消息的起始时间 
  * **size** 最大加载消息条数 
  * **result** 搜索到的消息结果列表 
  * **arg4** 消息搜索方向，默认（Direction::Up）是从更早的消息中搜索 


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

按照类型搜索消息，如果不指定则从最新消息开始 

**Parameters**: 

  * **type** 搜索消息的类型 
  * **refTime** 搜索消息的起始时间 
  * **size** 最大加载消息条数 
  * **result** 搜索到的消息结果列表 
  * **arg4** 消息搜索方向，默认（Direction::Up）是从更早的消息中搜索 


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

设置消息播放状态（只对语音/视频消息有效） 

**Parameters**: 

  * **msg** 需要设置播放状态的消息 
  * **status** 消息是否已经播放 
  * **callBack** 回调 


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

设置消息未读状态，更新未读消息数 

**Parameters**: 

  * **msg** 需要设置消息已读状态的消息 
  * **status** 消息是否设置已读 
  * **callBack** 回调 


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

把所有消息设置为已读，更新未读消息数 

**Parameters**: 

  * **callBack** 回调 


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

更新一条数据库存储消息的扩展字段信息 

**Parameters**: 

  * **msg** 需要更改扩展信息的消息此时msg部分已经更新扩展字椴信息 
  * **callBack** 回调 


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

插入一条消息 

**Parameters**: 

  * **msg** 插入的消息 
  * **callBack** 回调 


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

读取一条消息 

**Parameters**: 

  * **msgId** 需要读取的消息的消息id 
  * **callBack** 回调 


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

删除会话中的所有消息 

**Parameters**: 

  * **callBack** 回调 


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

加载消息，如果不指定则从最新消息开始 

**Parameters**: 

  * **refMsgId** 加载消息的起始id 
  * **size** 最大加载消息条数 
  * **arg3** 加载消息的方向，默认是加载更早的消息 
  * **callBack** 回调 


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

搜索消息，如果不指定则从最新消息开始 

**Parameters**: 

  * **keywords** 搜索消息的关键字 
  * **refTime** 搜索消息的起始时间 
  * **size** 最大加载消息条数 
  * **arg4** 消息搜索方向，默认（Direction::Up）是从更早的消息中搜索 
  * **callBack** 回调 


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

按照类型搜索消息，如果不指定则从最新消息开始 

**Parameters**: 

  * **type** 搜索消息的类型 
  * **refTime** 搜索消息的起始时间 
  * **size** 最大加载消息条数 
  * **arg4** 消息搜索方向，默认（Direction::Up）是从更早的消息中搜索 
  * **callBack** 回调 


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

读取数据库当前会话所有消息数量，强制更新conversation的消息总数和未读消息数。 

**Parameters**: 

  * **callBack** 回调 


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