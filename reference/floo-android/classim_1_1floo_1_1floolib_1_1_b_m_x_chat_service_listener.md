---
title: im::floo::floolib::BMXChatServiceListener
summary: 聊天监听者 

---

# im::floo::floolib::BMXChatServiceListener



聊天监听者 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-delete)**() |
| void | **[swigReleaseOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-swigreleaseownership)**() |
| void | **[swigTakeOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-swigtakeownership)**() |
| void | **[onStatusChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onstatuschanged)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, [BMXErrorCode] error)<br>消息发送状态发生变化  |
| void | **[onAttachmentUploadProgressChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onattachmentuploadprogresschanged)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, int percent)<br>附件上传进度发送变化  |
| void | **[onRecallStatusChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onrecallstatuschanged)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, [BMXErrorCode] error)<br>消息撤回状态发送变化  |
| void | **[onReceive](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceive)**(BMXMessageList list)<br>收到消息  |
| void | **[onReceiveCommandMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivecommandmessages)**(BMXMessageList list)<br>收到命令消息  |
| void | **[onReceiveSystemMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivesystemmessages)**(BMXMessageList list)<br>收到系统通知消息  |
| void | **[onReceiveReadAcks](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivereadacks)**(BMXMessageList list)<br>收到消息已读回执  |
| void | **[onReceiveDeliverAcks](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivedeliveracks)**(BMXMessageList list)<br>收到消息已送达回执  |
| void | **[onReceiveRecallMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceiverecallmessages)**(BMXMessageList list)<br>收到撤回消息  |
| void | **[onReceiveReadCancels](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivereadcancels)**(BMXMessageList list)<br>收到消息已读取消（多设备其他设备同步消息已读状态变为未读）  |
| void | **[onReceiveReadAllMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivereadallmessages)**(BMXMessageList list)<br>收到消息全部已读（多设备同步某消息之前消息全部设置为已读）  |
| void | **[onReceiveDeleteMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivedeletemessages)**(BMXMessageList list)<br>收到删除消息 （多设备同步删除消息）  |
| void | **[onReceivePlayAcks](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceiveplayacks)**(BMXMessageList list)<br>收到消息已播放回执  |
| void | **[onAttachmentStatusChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onattachmentstatuschanged)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, [BMXErrorCode] error, int percent)<br>附件下载状态发生变化  |
| void | **[onAttachmentDownloadByUrlStatusChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onattachmentdownloadbyurlstatuschanged)**(long msgId, [BMXErrorCode] error, int percent)<br>附件下载状态发生变化  |
| void | **[onRetrieveHistoryMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onretrievehistorymessages)**([BMXConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md) conversation)<br>拉取历史消息  |
| void | **[onLoadAllConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onloadallconversation)**()<br>已经加载完未读会话列表  |
| void | **[onConversationCreate](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onconversationcreate)**([BMXConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md) conversation, [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>本地创建新会话  |
| void | **[onConversationDelete](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onconversationdelete)**(long conversationId, [BMXErrorCode] error)<br>删除会话  |
| void | **[onTotalUnreadCountChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-ontotalunreadcountchanged)**(int unreadCount)<br>更新总未读数  |
| | **[BMXChatServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-bmxchatservicelistener)**() |
| void | **[registerChatService](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-registerchatservice)**([BMXChatService](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md) service) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXChatServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-bmxchatservicelistener)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-finalize)**() |
| void | **[swigDirectorDisconnect](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-swigdirectordisconnect)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-getcptr)**([BMXChatServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md) obj) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| transient boolean | **[swigCMemOwn](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#variable-swigcmemown)**  |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


### function swigReleaseOwnership

```java
inline void swigReleaseOwnership()
```


### function swigTakeOwnership

```java
inline void swigTakeOwnership()
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


### function onReceive

```java
inline void onReceive(
    BMXMessageList list
)
```

收到消息 

**Parameters**: 

  * **list** 接收到的消息列表 


### function onReceiveCommandMessages

```java
inline void onReceiveCommandMessages(
    BMXMessageList list
)
```

收到命令消息 

**Parameters**: 

  * **list** 接收到的消息列表 


### function onReceiveSystemMessages

```java
inline void onReceiveSystemMessages(
    BMXMessageList list
)
```

收到系统通知消息 

**Parameters**: 

  * **list** 接收到的系统消息列表 


### function onReceiveReadAcks

```java
inline void onReceiveReadAcks(
    BMXMessageList list
)
```

收到消息已读回执 

**Parameters**: 

  * **list** 接收到的已读回执消息列表 


### function onReceiveDeliverAcks

```java
inline void onReceiveDeliverAcks(
    BMXMessageList list
)
```

收到消息已送达回执 

**Parameters**: 

  * **list** 接收到的已送达回执消息列表 


### function onReceiveRecallMessages

```java
inline void onReceiveRecallMessages(
    BMXMessageList list
)
```

收到撤回消息 

**Parameters**: 

  * **list** 接收到的撤回消息列表 


### function onReceiveReadCancels

```java
inline void onReceiveReadCancels(
    BMXMessageList list
)
```

收到消息已读取消（多设备其他设备同步消息已读状态变为未读） 

**Parameters**: 

  * **list** 接收到的消息已读取消消息列表 


### function onReceiveReadAllMessages

```java
inline void onReceiveReadAllMessages(
    BMXMessageList list
)
```

收到消息全部已读（多设备同步某消息之前消息全部设置为已读） 

**Parameters**: 

  * **list** 接收到的消息全部已读消息列表 


### function onReceiveDeleteMessages

```java
inline void onReceiveDeleteMessages(
    BMXMessageList list
)
```

收到删除消息 （多设备同步删除消息） 

**Parameters**: 

  * **list** 接收到的删除消息列表 


### function onReceivePlayAcks

```java
inline void onReceivePlayAcks(
    BMXMessageList list
)
```

收到消息已播放回执 

**Parameters**: 

  * **list** 接收到的已读回执消息列表 


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


### function onRetrieveHistoryMessages

```java
inline void onRetrieveHistoryMessages(
    BMXConversation conversation
)
```

拉取历史消息 

**Parameters**: 

  * **conversation** 发生了拉取指历史消息的会话 


### function onLoadAllConversation

```java
inline void onLoadAllConversation()
```

已经加载完未读会话列表 

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


### function onTotalUnreadCountChanged

```java
inline void onTotalUnreadCountChanged(
    int unreadCount
)
```

更新总未读数 

**Parameters**: 

  * **unreadCount** 本地全部会话未读总数 


### function BMXChatServiceListener

```java
inline BMXChatServiceListener()
```


### function registerChatService

```java
inline void registerChatService(
    BMXChatService service
)
```


## Protected Functions Documentation

### function BMXChatServiceListener

```java
inline BMXChatServiceListener(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
```


### function swigDirectorDisconnect

```java
inline void swigDirectorDisconnect()
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


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800