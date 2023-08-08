---
title: im::floo::floolib::BMXChatServiceListener
summary: 聊天监听者
---

# im::floo::floolib::BMXChatServiceListener

聊天监听者

## Public Functions

|                   | Name                                                                                                                                                                                                                                                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| synchronized void | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service\_listener.md#function-delete)()                                                                                                                                                                                                                                        |
| void              | [**swigReleaseOwnership**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service\_listener.md#function-swigreleaseownership)()                                                                                                                                                                                                            |
| void              | [**swigTakeOwnership**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service\_listener.md#function-swigtakeownership)()                                                                                                                                                                                                                  |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onstatuschanged"><strong>onStatusChanged</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, [BMXErrorCode] error)<br>消息发送状态发生变化</p>                                                                                   |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onattachmentuploadprogresschanged"><strong>onAttachmentUploadProgressChanged</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, int percent)<br>附件上传进度发送变化</p>                                                        |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onrecallstatuschanged"><strong>onRecallStatusChanged</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, [BMXErrorCode] error)<br>消息撤回状态发送变化</p>                                                                       |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceive"><strong>onReceive</strong></a>(BMXMessageList list)<br>收到消息</p>                                                                                                                                                                                    |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivecommandmessages"><strong>onReceiveCommandMessages</strong></a>(BMXMessageList list)<br>收到命令消息</p>                                                                                                                                                    |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivesystemmessages"><strong>onReceiveSystemMessages</strong></a>(BMXMessageList list)<br>收到系统通知消息</p>                                                                                                                                                    |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivereadacks"><strong>onReceiveReadAcks</strong></a>(BMXMessageList list)<br>收到消息已读回执</p>                                                                                                                                                                |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivedeliveracks"><strong>onReceiveDeliverAcks</strong></a>(BMXMessageList list)<br>收到消息已送达回执</p>                                                                                                                                                         |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceiverecallmessages"><strong>onReceiveRecallMessages</strong></a>(BMXMessageList list)<br>收到撤回消息</p>                                                                                                                                                      |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivereadcancels"><strong>onReceiveReadCancels</strong></a>(BMXMessageList list)<br>收到消息已读取消（多设备其他设备同步消息已读状态变为未读）</p>                                                                                                                                     |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivereadallmessages"><strong>onReceiveReadAllMessages</strong></a>(BMXMessageList list)<br>收到消息全部已读（多设备同步某消息之前消息全部设置为已读）</p>                                                                                                                             |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivedeletemessages"><strong>onReceiveDeleteMessages</strong></a>(BMXMessageList list)<br>收到删除消息 （多设备同步删除消息）</p>                                                                                                                                          |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceiveplayacks"><strong>onReceivePlayAcks</strong></a>(BMXMessageList list)<br>收到消息已播放回执</p>                                                                                                                                                               |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onattachmentstatuschanged"><strong>onAttachmentStatusChanged</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, [BMXErrorCode] error, int percent)<br>附件下载状态发生变化</p>                                                  |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onattachmentdownloadbyurlstatuschanged"><strong>onAttachmentDownloadByUrlStatusChanged</strong></a>(long msgId, [BMXErrorCode] error, int percent)<br>附件下载状态发生变化</p>                                                                                          |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onretrievehistorymessages"><strong>onRetrieveHistoryMessages</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md">BMXConversation</a> conversation)<br>拉取历史消息</p>                                                                      |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onloadallconversation"><strong>onLoadAllConversation</strong></a>()<br>已经加载完未读会话列表</p>                                                                                                                                                                        |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onconversationcreate"><strong>onConversationCreate</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md">BMXConversation</a> conversation, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>本地创建新会话</p> |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onconversationdelete"><strong>onConversationDelete</strong></a>(long conversationId, [BMXErrorCode] error)<br>删除会话</p>                                                                                                                                        |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-ontotalunreadcountchanged"><strong>onTotalUnreadCountChanged</strong></a>(int unreadCount)<br>更新总未读数</p>                                                                                                                                                      |
|                   | [**BMXChatServiceListener**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service\_listener.md#function-bmxchatservicelistener)()                                                                                                                                                                                                        |
| void              | [**registerChatService**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service\_listener.md#function-registerchatservice)([BMXChatService](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md) service)                                                                                                                     |

## Protected Functions

|      | Name                                                                                                                                                                                                               |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|      | [**BMXChatServiceListener**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service\_listener.md#function-bmxchatservicelistener)(long cPtr, boolean cMemoryOwn)                                             |
| void | [**finalize**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service\_listener.md#function-finalize)()                                                                                                      |
| void | [**swigDirectorDisconnect**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service\_listener.md#function-swigdirectordisconnect)()                                                                          |
| long | [**getCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service\_listener.md#function-getcptr)([BMXChatServiceListener](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service\_listener.md) obj) |

## Protected Attributes

|                   | Name                                                                                                              |
| ----------------- | ----------------------------------------------------------------------------------------------------------------- |
| transient boolean | [**swigCMemOwn**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service\_listener.md#variable-swigcmemown) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function swigReleaseOwnership

```java
inline void swigReleaseOwnership()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function swigTakeOwnership

```java
inline void swigTakeOwnership()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onStatusChanged

```java
inline void onStatusChanged(
    BMXMessage msg,
    BMXErrorCode error
)
```

消息发送状态发生变化

**Parameters**:

* **msg** 发生状态变化的消息
* **error** 状态错误码

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onAttachmentUploadProgressChanged

```java
inline void onAttachmentUploadProgressChanged(
    BMXMessage msg,
    int percent
)
```

附件上传进度发送变化

**Parameters**:

* **msg** 上传附件的消息
* **percent** 附件上传的进度

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onRecallStatusChanged

```java
inline void onRecallStatusChanged(
    BMXMessage msg,
    BMXErrorCode error
)
```

消息撤回状态发送变化

**Parameters**:

* **msg** 撤回状态发生变化的消息
* **error** 状态错误码

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onReceive

```java
inline void onReceive(
    BMXMessageList list
)
```

收到消息

**Parameters**:

* **list** 接收到的消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onReceiveCommandMessages

```java
inline void onReceiveCommandMessages(
    BMXMessageList list
)
```

收到命令消息

**Parameters**:

* **list** 接收到的消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onReceiveSystemMessages

```java
inline void onReceiveSystemMessages(
    BMXMessageList list
)
```

收到系统通知消息

**Parameters**:

* **list** 接收到的系统消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onReceiveReadAcks

```java
inline void onReceiveReadAcks(
    BMXMessageList list
)
```

收到消息已读回执

**Parameters**:

* **list** 接收到的已读回执消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onReceiveDeliverAcks

```java
inline void onReceiveDeliverAcks(
    BMXMessageList list
)
```

收到消息已送达回执

**Parameters**:

* **list** 接收到的已送达回执消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onReceiveRecallMessages

```java
inline void onReceiveRecallMessages(
    BMXMessageList list
)
```

收到撤回消息

**Parameters**:

* **list** 接收到的撤回消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onReceiveReadCancels

```java
inline void onReceiveReadCancels(
    BMXMessageList list
)
```

收到消息已读取消（多设备其他设备同步消息已读状态变为未读）

**Parameters**:

* **list** 接收到的消息已读取消消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onReceiveReadAllMessages

```java
inline void onReceiveReadAllMessages(
    BMXMessageList list
)
```

收到消息全部已读（多设备同步某消息之前消息全部设置为已读）

**Parameters**:

* **list** 接收到的消息全部已读消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onReceiveDeleteMessages

```java
inline void onReceiveDeleteMessages(
    BMXMessageList list
)
```

收到删除消息 （多设备同步删除消息）

**Parameters**:

* **list** 接收到的删除消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onReceivePlayAcks

```java
inline void onReceivePlayAcks(
    BMXMessageList list
)
```

收到消息已播放回执

**Parameters**:

* **list** 接收到的已读回执消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onAttachmentStatusChanged

```java
inline void onAttachmentStatusChanged(
    BMXMessage msg,
    BMXErrorCode error,
    int percent
)
```

附件下载状态发生变化

**Parameters**:

* **msg** 发生下载状态变化的消息
* **error** 状态错误码
* **percent** 附件下载的进度

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onAttachmentDownloadByUrlStatusChanged

```java
inline void onAttachmentDownloadByUrlStatusChanged(
    long msgId,
    BMXErrorCode error,
    int percent
)
```

附件下载状态发生变化

**Parameters**:

* **msgId** 发生下载状态变化的消息ID
* **error** 状态错误码
* **percent** 附件下载的进度

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onRetrieveHistoryMessages

```java
inline void onRetrieveHistoryMessages(
    BMXConversation conversation
)
```

拉取历史消息

**Parameters**:

* **conversation** 发生了拉取指历史消息的会话

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onLoadAllConversation

```java
inline void onLoadAllConversation()
```

已经加载完未读会话列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onConversationCreate

```java
inline void onConversationCreate(
    BMXConversation conversation,
    BMXMessage msg
)
```

本地创建新会话

**Parameters**:

* **conversation** 新创建的本地会话
* **msg** 会话的最新消息，存在返回不存在返回为空

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onConversationDelete

```java
inline void onConversationDelete(
    long conversationId,
    BMXErrorCode error
)
```

删除会话

**Parameters**:

* **conversationId** 删除的本地会话id
* **error** 状态错误码

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function onTotalUnreadCountChanged

```java
inline void onTotalUnreadCountChanged(
    int unreadCount
)
```

更新总未读数

**Parameters**:

* **unreadCount** 本地全部会话未读总数

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function BMXChatServiceListener

```java
inline BMXChatServiceListener()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function registerChatService

```java
inline void registerChatService(
    BMXChatService service
)
```

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function BMXChatServiceListener

```java
inline BMXChatServiceListener(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function finalize

```java
inline void finalize()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function swigDirectorDisconnect

```java
inline void swigDirectorDisconnect()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

### function getCPtr

```java
static inline long getCPtr(
    BMXChatServiceListener obj
)
```

## Protected Attributes Documentation

### variable swigCMemOwn

```java
transient boolean swigCMemOwn;
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```



Updated on 2022-01-26 at 17:18:31 +0800
