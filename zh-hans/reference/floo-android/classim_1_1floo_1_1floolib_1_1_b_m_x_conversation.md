---
title: im::floo::floolib::BMXConversation
summary: 会话
---

# im::floo::floolib::BMXConversation

会话

Inherits from BMXBaseObject

## Public Functions

|                                                                         | Name                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void                                                       | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md#function-delete)()                                                                                                                                                                                                                                   |
| long                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-conversationid"><strong>conversationId</strong></a>()<br>会话Id</p>                                                                                                                                                                                      |
| BMXConversation.Type                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-type"><strong>type</strong></a>()<br>会话类型</p>                                                                                                                                                                                                          |
| [BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md) | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-lastmsg"><strong>lastMsg</strong></a>()<br>最新消息</p>                                                                                                                                                                                                    |
| int                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-unreadnumber"><strong>unreadNumber</strong></a>()<br>未读消息数</p>                                                                                                                                                                                         |
| int                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-messagecount"><strong>messageCount</strong></a>()<br>会话中所有消息的数量</p>                                                                                                                                                                                    |
| boolean                                                                 | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-ismutenotification"><strong>isMuteNotification</strong></a>()<br>是否提醒用户消息,不提醒的情况下会话总未读数不会统计该会话计数。</p>                                                                                                                                                  |
| String                                                                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-extension"><strong>extension</strong></a>()<br>扩展信息</p>                                                                                                                                                                                                |
| \[BMXErrorCode]                                                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-setextension"><strong>setExtension</strong></a>(String ext)<br>设置扩展信息</p>                                                                                                                                                                              |
| String                                                                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-editmessage"><strong>editMessage</strong></a>()<br>编辑消息</p>                                                                                                                                                                                            |
| \[BMXErrorCode]                                                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-seteditmessage"><strong>setEditMessage</strong></a>(String editMessage)<br>设置编辑消息</p>                                                                                                                                                                  |
| \[BMXErrorCode]                                                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessagesbykeywords"><strong>searchMessagesByKeyWords</strong></a>(String keywords, long refTime, long size, BMXMessageList result, BMXConversation.Direction arg4)<br>搜索消息，如果不指定则从最新消息开始</p>                                                     |
| \[BMXErrorCode]                                                         | [**searchMessagesByKeyWords**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md#function-searchmessagesbykeywords)(String keywords, long refTime, long size, BMXMessageList result)                                                                                                                                |
| \[BMXErrorCode]                                                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessagesbytype"><strong>searchMessagesByType</strong></a>(BMXMessage.ContentType type, long refTime, long size, BMXMessageList result, BMXConversation.Direction arg4)<br>按照类型搜索消息，如果不指定则从最新消息开始</p>                                             |
| \[BMXErrorCode]                                                         | [**searchMessagesByType**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md#function-searchmessagesbytype)(BMXMessage.ContentType type, long refTime, long size, BMXMessageList result)                                                                                                                            |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-setmessageplayedstatus"><strong>setMessagePlayedStatus</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, final boolean status, final BMXCallBack callBack)<br>设置消息播放状态（只对语音/视频消息有效）</p>                 |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-setmessagereadstatus"><strong>setMessageReadStatus</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, final boolean status, final BMXCallBack callBack)<br>设置消息未读状态，更新未读消息数</p>                          |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-setallmessagesread"><strong>setAllMessagesRead</strong></a>(final BMXCallBack callBack)<br>把所有消息设置为已读，更新未读消息数</p>                                                                                                                                      |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-updatemessageextension"><strong>updateMessageExtension</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, final BMXCallBack callBack)<br>更新一条数据库存储消息的扩展字段信息</p>                                          |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-insertmessage"><strong>insertMessage</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, final BMXCallBack callBack)<br>插入一条消息</p>                                                                        |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-loadmessage"><strong>loadMessage</strong></a>(final long msgId, final BMXDataCallBack&#x3C; <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> > callBack)<br>读取一条消息</p>                                                         |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-removeallmessages"><strong>removeAllMessages</strong></a>(final BMXCallBack callBack)<br>删除会话中的所有消息</p>                                                                                                                                                |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-loadmessages"><strong>loadMessages</strong></a>(final long refMsgId, final long size, final BMXConversation.Direction arg3, final BMXDataCallBack&#x3C; BMXMessageList > callBack)<br>加载消息，如果不指定则从最新消息开始</p>                                           |
| void                                                                    | [**loadMessages**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md#function-loadmessages)(final long refMsgId, final long size, final BMXDataCallBack< BMXMessageList > callBack)                                                                                                                                 |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessages"><strong>searchMessages</strong></a>(final String keywords, final long refTime, final long size, final BMXConversation.Direction arg4, final BMXDataCallBack&#x3C; BMXMessageList > callBack)<br>搜索消息，如果不指定则从最新消息开始</p>                 |
| void                                                                    | [**searchMessages**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md#function-searchmessages)(final String keywords, final long refTime, final long size, final BMXDataCallBack< BMXMessageList > callBack)                                                                                                       |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-searchmessages"><strong>searchMessages</strong></a>(final BMXMessage.ContentType type, final long refTime, final long size, final BMXConversation.Direction arg4, final BMXDataCallBack&#x3C; BMXMessageList > callBack)<br>按照类型搜索消息，如果不指定则从最新消息开始</p> |
| void                                                                    | [**searchMessages**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md#function-searchmessages)(final BMXMessage.ContentType type, final long refTime, final long size, final BMXDataCallBack< BMXMessageList > callBack)                                                                                           |
| void                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md#function-refreshconversation"><strong>refreshConversation</strong></a>(final BMXCallBack callBack)<br>读取数据库当前会话所有消息数量，强制更新conversation的消息总数和未读消息数。</p>                                                                                                          |

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

会话Id

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function type

```java
inline BMXConversation.Type type()
```

会话类型

**Return**: \[Type]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function lastMsg

```java
inline BMXMessage lastMsg()
```

最新消息

**Return**: BMXMessagePtr

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function unreadNumber

```java
inline int unreadNumber()
```

未读消息数

**Return**: int32\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function messageCount

```java
inline int messageCount()
```

会话中所有消息的数量

**Return**: int32\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function isMuteNotification

```java
inline boolean isMuteNotification()
```

是否提醒用户消息,不提醒的情况下会话总未读数不会统计该会话计数。

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function extension

```java
inline String extension()
```

扩展信息

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

设置扩展信息

**Parameters**:

* **ext** 会话扩展消息

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXConversation'></div>
```

### function editMessage

```java
inline String editMessage()
```

编辑消息

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

设置编辑消息

**Parameters**:

* **editMessage** 会话正在编辑的文本消息

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

搜索消息，如果不指定则从最新消息开始

**Parameters**:

* **keywords** 搜索消息的关键字
* **refTime** 搜索消息的起始时间
* **size** 最大加载消息条数
* **result** 搜索到的消息结果列表
* **arg4** 消息搜索方向，默认（Direction::Up）是从更早的消息中搜索

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

按照类型搜索消息，如果不指定则从最新消息开始

**Parameters**:

* **type** 搜索消息的类型
* **refTime** 搜索消息的起始时间
* **size** 最大加载消息条数
* **result** 搜索到的消息结果列表
* **arg4** 消息搜索方向，默认（Direction::Up）是从更早的消息中搜索

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

设置消息播放状态（只对语音/视频消息有效）

**Parameters**:

* **msg** 需要设置播放状态的消息
* **status** 消息是否已经播放
* **callBack** 回调

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

设置消息未读状态，更新未读消息数

**Parameters**:

* **msg** 需要设置消息已读状态的消息
* **status** 消息是否设置已读
* **callBack** 回调

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

把所有消息设置为已读，更新未读消息数

**Parameters**:

* **callBack** 回调

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

更新一条数据库存储消息的扩展字段信息

**Parameters**:

* **msg** 需要更改扩展信息的消息此时msg部分已经更新扩展字椴信息
* **callBack** 回调

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

插入一条消息

**Parameters**:

* **msg** 插入的消息
* **callBack** 回调

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

读取一条消息

**Parameters**:

* **msgId** 需要读取的消息的消息id
* **callBack** 回调

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

删除会话中的所有消息

**Parameters**:

* **callBack** 回调

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

加载消息，如果不指定则从最新消息开始

**Parameters**:

* **refMsgId** 加载消息的起始id
* **size** 最大加载消息条数
* **arg3** 加载消息的方向，默认是加载更早的消息
* **callBack** 回调

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

搜索消息，如果不指定则从最新消息开始

**Parameters**:

* **keywords** 搜索消息的关键字
* **refTime** 搜索消息的起始时间
* **size** 最大加载消息条数
* **arg4** 消息搜索方向，默认（Direction::Up）是从更早的消息中搜索
* **callBack** 回调

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

按照类型搜索消息，如果不指定则从最新消息开始

**Parameters**:

* **type** 搜索消息的类型
* **refTime** 搜索消息的起始时间
* **size** 最大加载消息条数
* **arg4** 消息搜索方向，默认（Direction::Up）是从更早的消息中搜索
* **callBack** 回调

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

读取数据库当前会话所有消息数量，强制更新conversation的消息总数和未读消息数。

**Parameters**:

* **callBack** 回调

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
