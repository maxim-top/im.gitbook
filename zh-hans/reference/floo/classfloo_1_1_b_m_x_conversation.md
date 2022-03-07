---
title: floo::BMXConversation
summary: 会话 

---

# floo::BMXConversation



会话 


`#include <bmx_conversation.h>`

Inherits from BMXBaseObject

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[Type](classfloo_1_1_b_m_x_conversation.md#enum-type)** { Single, Group, System}<br>会话类型  |
| enum class| **[Direction](classfloo_1_1_b_m_x_conversation.md#enum-direction)** { Up, Down}<br>消息搜索方向  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXConversation](classfloo_1_1_b_m_x_conversation.md#function-~bmxconversation)**()<br>析构函数  |
| virtual int64_t | **[conversationId](classfloo_1_1_b_m_x_conversation.md#function-conversationid)**() =0<br>会话Id  |
| virtual [Type](classfloo_1_1_b_m_x_conversation.md#enum-type) | **[type](classfloo_1_1_b_m_x_conversation.md#function-type)**() =0<br>会话类型  |
| virtual BMXMessagePtr | **[lastMsg](classfloo_1_1_b_m_x_conversation.md#function-lastmsg)**() =0<br>最新消息  |
| virtual int32_t | **[unreadNumber](classfloo_1_1_b_m_x_conversation.md#function-unreadnumber)**() =0<br>未读消息数  |
| virtual int32_t | **[messageCount](classfloo_1_1_b_m_x_conversation.md#function-messagecount)**() =0<br>会话中所有消息的数量  |
| virtual bool | **[isMuteNotification](classfloo_1_1_b_m_x_conversation.md#function-ismutenotification)**() =0<br>是否提醒用户消息,不提醒的情况下会话总未读数不会统计该会话计数。  |
| virtual const JSON & | **[extension](classfloo_1_1_b_m_x_conversation.md#function-extension)**() =0<br>扩展信息  |
| virtual BMXErrorCode | **[setExtension](classfloo_1_1_b_m_x_conversation.md#function-setextension)**(const std::string & ext) =0<br>设置扩展信息  |
| virtual const std::string & | **[editMessage](classfloo_1_1_b_m_x_conversation.md#function-editmessage)**() =0<br>编辑消息  |
| virtual BMXErrorCode | **[setEditMessage](classfloo_1_1_b_m_x_conversation.md#function-seteditmessage)**(const std::string & editMessage) =0<br>设置编辑消息  |
| virtual BMXErrorCode | **[setMessagePlayedStatus](classfloo_1_1_b_m_x_conversation.md#function-setmessageplayedstatus)**(BMXMessagePtr msg, bool status) =0<br>设置消息播放状态（只对语音/视频消息有效）  |
| virtual BMXErrorCode | **[setMessageReadStatus](classfloo_1_1_b_m_x_conversation.md#function-setmessagereadstatus)**(BMXMessagePtr msg, bool status) =0<br>设置消息未读状态，更新未读消息数  |
| virtual BMXErrorCode | **[setAllMessagesRead](classfloo_1_1_b_m_x_conversation.md#function-setallmessagesread)**() =0<br>把所有消息设置为已读，更新未读消息数  |
| virtual BMXErrorCode | **[updateMessageExtension](classfloo_1_1_b_m_x_conversation.md#function-updatemessageextension)**(BMXMessagePtr msg) =0<br>更新一条数据库存储消息的扩展字段信息  |
| virtual BMXErrorCode | **[insertMessage](classfloo_1_1_b_m_x_conversation.md#function-insertmessage)**(BMXMessagePtr msg) =0<br>插入一条消息  |
| virtual BMXMessagePtr | **[loadMessage](classfloo_1_1_b_m_x_conversation.md#function-loadmessage)**(int64_t msgId) =0<br>读取一条消息  |
| virtual BMXErrorCode | **[removeAllMessages](classfloo_1_1_b_m_x_conversation.md#function-removeallmessages)**() =0<br>删除会话中的所有消息  |
| virtual BMXErrorCode | **[loadMessages](classfloo_1_1_b_m_x_conversation.md#function-loadmessages)**(int64_t refMsgId, size_t size, BMXMessageList & result, [Direction](classfloo_1_1_b_m_x_conversation.md#enum-direction)  =[Direction::Up](classfloo_1_1_b_m_x_conversation.md#enumvalue-up)) =0<br>加载消息，如果不指定则从最新消息开始  |
| virtual BMXErrorCode | **[searchMessagesByKeyWords](classfloo_1_1_b_m_x_conversation.md#function-searchmessagesbykeywords)**(const std::string & keywords, int64_t refTime, size_t size, BMXMessageList & result, [Direction](classfloo_1_1_b_m_x_conversation.md#enum-direction)  =[Direction::Up](classfloo_1_1_b_m_x_conversation.md#enumvalue-up)) =0<br>搜索消息，如果不指定则从最新消息开始  |
| virtual BMXErrorCode | **[searchMessages](classfloo_1_1_b_m_x_conversation.md#function-searchmessages)**(const std::string & keywords, int64_t refTime, size_t size, BMXMessageList & result, [Direction](classfloo_1_1_b_m_x_conversation.md#enum-direction)  =[Direction::Up](classfloo_1_1_b_m_x_conversation.md#enumvalue-up)) =0<br>Deprecated.  |
| virtual BMXErrorCode | **[searchMessagesByType](classfloo_1_1_b_m_x_conversation.md#function-searchmessagesbytype)**([BMXMessage::ContentType](classfloo_1_1_b_m_x_message.md#enum-contenttype) type, int64_t refTime, size_t size, BMXMessageList & result, [Direction](classfloo_1_1_b_m_x_conversation.md#enum-direction)  =[Direction::Up](classfloo_1_1_b_m_x_conversation.md#enumvalue-up)) =0<br>按照类型搜索消息，如果不指定则从最新消息开始  |
| virtual BMXErrorCode | **[searchMessages](classfloo_1_1_b_m_x_conversation.md#function-searchmessages)**([BMXMessage::ContentType](classfloo_1_1_b_m_x_message.md#enum-contenttype) type, int64_t refTime, size_t size, BMXMessageList & result, [Direction](classfloo_1_1_b_m_x_conversation.md#enum-direction)  =[Direction::Up](classfloo_1_1_b_m_x_conversation.md#enumvalue-up)) =0<br>Deprecated.  |
| virtual BMXErrorCode | **[refreshConversation](classfloo_1_1_b_m_x_conversation.md#function-refreshconversation)**() =0<br>读取数据库当前会话所有消息数量，强制更新conversation的消息总数和未读消息数。  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXConversation](classfloo_1_1_b_m_x_conversation.md#function-bmxconversation)**() |

## Public Types Documentation

### enum Type

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Single | | 单聊   |
| Group | | 群聊   |
| System | | 系统通知   |



会话类型 

### enum Direction

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Up | | 取更旧消息   |
| Down | | 取更新消息   |



消息搜索方向 

## Public Functions Documentation

### function ~BMXConversation

```cpp
inline virtual ~BMXConversation()
```

析构函数 

### function conversationId

```cpp
virtual int64_t conversationId() =0
```

会话Id 

**Return**: int64_t 

### function type

```cpp
virtual Type type() =0
```

会话类型 

**Return**: Type 

### function lastMsg

```cpp
virtual BMXMessagePtr lastMsg() =0
```

最新消息 

**Return**: BMXMessagePtr 

### function unreadNumber

```cpp
virtual int32_t unreadNumber() =0
```

未读消息数 

**Return**: int32_t 

### function messageCount

```cpp
virtual int32_t messageCount() =0
```

会话中所有消息的数量 

**Return**: int32_t 

### function isMuteNotification

```cpp
virtual bool isMuteNotification() =0
```

是否提醒用户消息,不提醒的情况下会话总未读数不会统计该会话计数。 

**Return**: bool 

### function extension

```cpp
virtual const JSON & extension() =0
```

扩展信息 

**Return**: JSON(std::string) 

### function setExtension

```cpp
virtual BMXErrorCode setExtension(
    const std::string & ext
) =0
```

设置扩展信息 

**Parameters**: 

  * **ext** 会话扩展消息 


**Return**: BMXErrorCode 

### function editMessage

```cpp
virtual const std::string & editMessage() =0
```

编辑消息 

**Return**: std::string 

### function setEditMessage

```cpp
virtual BMXErrorCode setEditMessage(
    const std::string & editMessage
) =0
```

设置编辑消息 

**Parameters**: 

  * **editMessage** 会话正在编辑的文本消息 


**Return**: BMXErrorCode 

### function setMessagePlayedStatus

```cpp
virtual BMXErrorCode setMessagePlayedStatus(
    BMXMessagePtr msg,
    bool status
) =0
```

设置消息播放状态（只对语音/视频消息有效） 

**Parameters**: 

  * **msg** 需要设置播放状态的消息 
  * **status** 消息是否已经播放 


**Return**: BMXErrorCode 

### function setMessageReadStatus

```cpp
virtual BMXErrorCode setMessageReadStatus(
    BMXMessagePtr msg,
    bool status
) =0
```

设置消息未读状态，更新未读消息数 

**Parameters**: 

  * **msg** 需要设置消息已读状态的消息 
  * **status** 消息是否设置已读 


**Return**: BMXErrorCode 

### function setAllMessagesRead

```cpp
virtual BMXErrorCode setAllMessagesRead() =0
```

把所有消息设置为已读，更新未读消息数 

**Return**: BMXErrorCode 

### function updateMessageExtension

```cpp
virtual BMXErrorCode updateMessageExtension(
    BMXMessagePtr msg
) =0
```

更新一条数据库存储消息的扩展字段信息 

**Parameters**: 

  * **msg** 需要更改扩展信息的消息此时msg部分已经更新扩展字椴信息 


**Return**: BMXErrorCode 

### function insertMessage

```cpp
virtual BMXErrorCode insertMessage(
    BMXMessagePtr msg
) =0
```

插入一条消息 

**Parameters**: 

  * **msg** 插入的消息 


**Return**: BMXErrorCode 

### function loadMessage

```cpp
virtual BMXMessagePtr loadMessage(
    int64_t msgId
) =0
```

读取一条消息 

**Parameters**: 

  * **msgId** 需要读取的消息的消息id 


**Return**: BMXMessagePtr 

### function removeAllMessages

```cpp
virtual BMXErrorCode removeAllMessages() =0
```

删除会话中的所有消息 

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

加载消息，如果不指定则从最新消息开始 

**Parameters**: 

  * **refMsgId** 加载消息的起始id 
  * **size** 最大加载消息条数 
  * **result** 数据库返回的加载消息列表 
  * **Direction** 加载消息的方向，默认是加载更早的消息 


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

搜索消息，如果不指定则从最新消息开始 

**Parameters**: 

  * **keywords** 搜索消息的关键字 
  * **refTime** 搜索消息的起始时间 
  * **size** 最大加载消息条数 
  * **result** 搜索到的消息结果列表 
  * **Direction** 消息搜索方向，默认（Direction::Up）是从更早的消息中搜索 


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

  * **keywords** 搜索消息的关键字 
  * **refTime** 搜索消息的起始时间 
  * **size** 最大加载消息条数 
  * **result** 搜索到的消息结果列表 
  * **Direction** 消息搜索方向，默认（Direction::Up）是从更早的消息中搜索 


**Return**: BMXErrorCode 

use searchMessagesByKeyWords instead.

搜索消息，如果不指定则从最新消息开始 


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

按照类型搜索消息，如果不指定则从最新消息开始 

**Parameters**: 

  * **type** 搜索消息的类型 
  * **refTime** 搜索消息的起始时间 
  * **size** 最大加载消息条数 
  * **result** 搜索到的消息结果列表 
  * **Direction** 消息搜索方向，默认（Direction::Up）是从更早的消息中搜索 


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

  * **type** 搜索消息的类型 
  * **refTime** 搜索消息的起始时间 
  * **size** 最大加载消息条数 
  * **result** 搜索到的消息结果列表 
  * **Direction** 消息搜索方向，默认（Direction::Up）是从更早的消息中搜索 


**Return**: BMXErrorCode 

use searchMessagesByType instead.

按照类型搜索消息，如果不指定则从最新消息开始 


### function refreshConversation

```cpp
virtual BMXErrorCode refreshConversation() =0
```

读取数据库当前会话所有消息数量，强制更新conversation的消息总数和未读消息数。 

**Return**: BMXErrorCode 

## Protected Functions Documentation

### function BMXConversation

```cpp
inline BMXConversation()
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800