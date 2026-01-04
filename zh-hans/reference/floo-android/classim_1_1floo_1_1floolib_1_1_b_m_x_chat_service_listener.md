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


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="delete" %}{% endlanying_code_snippet %}
```
### function swigReleaseOwnership

```java
inline void swigReleaseOwnership()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="swigReleaseOwnership" %}{% endlanying_code_snippet %}
```
### function swigTakeOwnership

```java
inline void swigTakeOwnership()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="swigTakeOwnership" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onStatusChanged" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onAttachmentUploadProgressChanged" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onRecallStatusChanged" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceive" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceiveCommandMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceiveSystemMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceiveReadAcks" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceiveDeliverAcks" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceiveRecallMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceiveReadCancels" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceiveReadAllMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceiveDeleteMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceivePlayAcks" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onAttachmentStatusChanged" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onAttachmentDownloadByUrlStatusChanged" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onRetrieveHistoryMessages" %}{% endlanying_code_snippet %}
```
### function onLoadAllConversation

```java
inline void onLoadAllConversation()
```

已经加载完未读会话列表 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onLoadAllConversation" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onConversationCreate" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onConversationDelete" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onTotalUnreadCountChanged" %}{% endlanying_code_snippet %}
```
### function BMXChatServiceListener

```java
inline BMXChatServiceListener()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="BMXChatServiceListener" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="registerChatService" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="BMXChatServiceListener" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="finalize" %}{% endlanying_code_snippet %}
```
### function swigDirectorDisconnect

```java
inline void swigDirectorDisconnect()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="swigDirectorDisconnect" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800