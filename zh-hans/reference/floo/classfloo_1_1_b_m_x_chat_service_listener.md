---
title: floo::BMXChatServiceListener
summary: 聊天监听者 

---

# floo::BMXChatServiceListener



聊天监听者 


`#include <bmx_chat_service_listener.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXChatServiceListener](classfloo_1_1_b_m_x_chat_service_listener.md#function-bmxchatservicelistener)**()<br>构造函数  |
| virtual | **[~BMXChatServiceListener](classfloo_1_1_b_m_x_chat_service_listener.md#function-~bmxchatservicelistener)**()<br>析构函数  |
| virtual void | **[onStatusChanged](classfloo_1_1_b_m_x_chat_service_listener.md#function-onstatuschanged)**(BMXMessagePtr msg, BMXErrorCode error)<br>消息发送状态发生变化  |
| virtual void | **[onAttachmentUploadProgressChanged](classfloo_1_1_b_m_x_chat_service_listener.md#function-onattachmentuploadprogresschanged)**(BMXMessagePtr msg, int percent)<br>附件上传进度发送变化  |
| virtual void | **[onRecallStatusChanged](classfloo_1_1_b_m_x_chat_service_listener.md#function-onrecallstatuschanged)**(BMXMessagePtr msg, BMXErrorCode error)<br>消息撤回状态发送变化  |
| virtual void | **[onReceive](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceive)**(const BMXMessageList & list)<br>收到消息  |
| virtual void | **[onReceiveCommandMessages](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivecommandmessages)**(const BMXMessageList & list)<br>收到命令消息  |
| virtual void | **[onReceiveSystemMessages](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivesystemmessages)**(const BMXMessageList & list)<br>收到系统通知消息  |
| virtual void | **[onReceiveReadAcks](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivereadacks)**(const BMXMessageList & list)<br>收到消息已读回执  |
| virtual void | **[onReceiveDeliverAcks](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivedeliveracks)**(const BMXMessageList & list)<br>收到消息已送达回执  |
| virtual void | **[onReceiveRecallMessages](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceiverecallmessages)**(const BMXMessageList & list)<br>收到撤回消息  |
| virtual void | **[onReceiveReadCancels](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivereadcancels)**(const BMXMessageList & list)<br>收到消息已读取消（多设备其他设备同步消息已读状态变为未读）  |
| virtual void | **[onReceiveReadAllMessages](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivereadallmessages)**(const BMXMessageList & list)<br>收到消息全部已读（多设备同步某消息之前消息全部设置为已读）  |
| virtual void | **[onReceiveDeleteMessages](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivedeletemessages)**(const BMXMessageList & list)<br>收到删除消息 （多设备同步删除消息）  |
| virtual void | **[onReceivePlayAcks](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceiveplayacks)**(const BMXMessageList & list)<br>收到音频/视频消息已播放回执  |
| virtual void | **[onAttachmentStatusChanged](classfloo_1_1_b_m_x_chat_service_listener.md#function-onattachmentstatuschanged)**(BMXMessagePtr msg, BMXErrorCode error, int percent)<br>附件下载状态发生变化  |
| virtual void | **[onAttachmentDownloadByUrlStatusChanged](classfloo_1_1_b_m_x_chat_service_listener.md#function-onattachmentdownloadbyurlstatuschanged)**(int64_t msgId, BMXErrorCode error, int percent)<br>附件下载状态发生变化  |
| virtual void | **[onRetrieveHistoryMessages](classfloo_1_1_b_m_x_chat_service_listener.md#function-onretrievehistorymessages)**(BMXConversationPtr conversation)<br>拉取历史消息  |
| virtual void | **[onLoadAllConversation](classfloo_1_1_b_m_x_chat_service_listener.md#function-onloadallconversation)**()<br>已经加载完未读会话列表  |
| virtual void | **[onConversationCreate](classfloo_1_1_b_m_x_chat_service_listener.md#function-onconversationcreate)**(BMXConversationPtr conversation, BMXMessagePtr msg)<br>本地创建新会话  |
| virtual void | **[onConversationDelete](classfloo_1_1_b_m_x_chat_service_listener.md#function-onconversationdelete)**(int64_t conversationId, BMXErrorCode error)<br>删除会话  |
| virtual void | **[onTotalUnreadCountChanged](classfloo_1_1_b_m_x_chat_service_listener.md#function-ontotalunreadcountchanged)**(int unreadCount)<br>更新总未读数  |
| void | **[registerChatService](classfloo_1_1_b_m_x_chat_service_listener.md#function-registerchatservice)**([BMXChatService](classfloo_1_1_b_m_x_chat_service.md) * service)<br>注册BMXChatServiceListener绑定到的BMXChatService（SDK内部自动注册）  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [BMXChatService](classfloo_1_1_b_m_x_chat_service.md) * | **[mService](classfloo_1_1_b_m_x_chat_service_listener.md#variable-mservice)**  |

## Public Functions Documentation

### function BMXChatServiceListener

```cpp
inline BMXChatServiceListener()
```

构造函数 

### function ~BMXChatServiceListener

```cpp
inline virtual ~BMXChatServiceListener()
```

析构函数 

### function onStatusChanged

```cpp
inline virtual void onStatusChanged(
    BMXMessagePtr msg,
    BMXErrorCode error
)
```

消息发送状态发生变化 

**Parameters**: 

  * **msg** 发生状态变化的消息 
  * **error** 状态错误码 


### function onAttachmentUploadProgressChanged

```cpp
inline virtual void onAttachmentUploadProgressChanged(
    BMXMessagePtr msg,
    int percent
)
```

附件上传进度发送变化 

**Parameters**: 

  * **msg** 上传附件的消息 
  * **percent** 附件上传的进度 


### function onRecallStatusChanged

```cpp
inline virtual void onRecallStatusChanged(
    BMXMessagePtr msg,
    BMXErrorCode error
)
```

消息撤回状态发送变化 

**Parameters**: 

  * **msg** 撤回状态发生变化的消息 
  * **error** 状态错误码 


### function onReceive

```cpp
inline virtual void onReceive(
    const BMXMessageList & list
)
```

收到消息 

**Parameters**: 

  * **list** 接收到的消息列表 


### function onReceiveCommandMessages

```cpp
inline virtual void onReceiveCommandMessages(
    const BMXMessageList & list
)
```

收到命令消息 

**Parameters**: 

  * **list** 接收到的消息列表 


### function onReceiveSystemMessages

```cpp
inline virtual void onReceiveSystemMessages(
    const BMXMessageList & list
)
```

收到系统通知消息 

**Parameters**: 

  * **list** 接收到的系统消息列表 


### function onReceiveReadAcks

```cpp
inline virtual void onReceiveReadAcks(
    const BMXMessageList & list
)
```

收到消息已读回执 

**Parameters**: 

  * **list** 接收到的已读回执消息列表 


### function onReceiveDeliverAcks

```cpp
inline virtual void onReceiveDeliverAcks(
    const BMXMessageList & list
)
```

收到消息已送达回执 

**Parameters**: 

  * **list** 接收到的已送达回执消息列表 


### function onReceiveRecallMessages

```cpp
inline virtual void onReceiveRecallMessages(
    const BMXMessageList & list
)
```

收到撤回消息 

**Parameters**: 

  * **list** 接收到的撤回消息列表 


### function onReceiveReadCancels

```cpp
inline virtual void onReceiveReadCancels(
    const BMXMessageList & list
)
```

收到消息已读取消（多设备其他设备同步消息已读状态变为未读） 

**Parameters**: 

  * **list** 接收到的消息已读取消消息列表 


### function onReceiveReadAllMessages

```cpp
inline virtual void onReceiveReadAllMessages(
    const BMXMessageList & list
)
```

收到消息全部已读（多设备同步某消息之前消息全部设置为已读） 

**Parameters**: 

  * **list** 接收到的消息全部已读消息列表 


### function onReceiveDeleteMessages

```cpp
inline virtual void onReceiveDeleteMessages(
    const BMXMessageList & list
)
```

收到删除消息 （多设备同步删除消息） 

**Parameters**: 

  * **list** 接收到的删除消息列表 


### function onReceivePlayAcks

```cpp
inline virtual void onReceivePlayAcks(
    const BMXMessageList & list
)
```

收到音频/视频消息已播放回执 

**Parameters**: 

  * **list** 接收到的音频/视频消息已播放回执消息列表 


### function onAttachmentStatusChanged

```cpp
inline virtual void onAttachmentStatusChanged(
    BMXMessagePtr msg,
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

```cpp
inline virtual void onAttachmentDownloadByUrlStatusChanged(
    int64_t msgId,
    BMXErrorCode error,
    int percent
)
```

附件下载状态发生变化 

**Parameters**: 

  * **msgId** 发生下载状态变化的消息Id 
  * **error** 状态错误码 
  * **percent** 附件下载的进度 


### function onRetrieveHistoryMessages

```cpp
inline virtual void onRetrieveHistoryMessages(
    BMXConversationPtr conversation
)
```

拉取历史消息 

**Parameters**: 

  * **conversation** 发生了拉取指历史消息的会话 


### function onLoadAllConversation

```cpp
inline virtual void onLoadAllConversation()
```

已经加载完未读会话列表 

### function onConversationCreate

```cpp
inline virtual void onConversationCreate(
    BMXConversationPtr conversation,
    BMXMessagePtr msg
)
```

本地创建新会话 

**Parameters**: 

  * **conversation** 新创建的本地会话 
  * **msg** 会话的最新消息，存在返回不存在返回为空 


### function onConversationDelete

```cpp
inline virtual void onConversationDelete(
    int64_t conversationId,
    BMXErrorCode error
)
```

删除会话 

**Parameters**: 

  * **conversationId** 删除的本地会话id 
  * **error** 状态错误码 


### function onTotalUnreadCountChanged

```cpp
inline virtual void onTotalUnreadCountChanged(
    int unreadCount
)
```

更新总未读数 

**Parameters**: 

  * **unreadCount** 本地全部会话未读总数 


### function registerChatService

```cpp
inline void registerChatService(
    BMXChatService * service
)
```

注册BMXChatServiceListener绑定到的BMXChatService（SDK内部自动注册） 

**Parameters**: 

  * **service** [BMXChatService](classfloo_1_1_b_m_x_chat_service.md)


## Protected Attributes Documentation

### variable mService

```cpp
BMXChatService * mService;
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800