---
title: im::floo::floolib::BMXChatManager
summary: 聊天管理器 

---

# im::floo::floolib::BMXChatManager



聊天管理器 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXChatManager](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-bmxchatmanager)**([BMXChatService](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md) service) |
| void | **[sendMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-sendmessage)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>发送消息，消息状态变化会通过listener通知  |
| void | **[resendMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-resendmessage)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>重新发送消息，消息状态变化会通过listener通知  |
| void | **[recallMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-recallmessage)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>撤回消息，消息状态变化会通过listener通知  |
| void | **[forwardMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-forwardmessage)**(final BMXMessageList list, final [BMXConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md) to, final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) newMsg, final BMXCallBack callBack)<br>合并转发消息  |
| void | **[forwardMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-forwardmessage)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>简单转发消息，用户应当通过BMXMessage::createForwardMessage()先创建转发消息  |
| void | **[readAllMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-readallmessage)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>标记此消息及之前全部消息为已读，该消息同步到当前用户的所有设备  |
| void | **[removeMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-removemessage)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, final boolean synchronize)<br>删除此消息，该消息同步到当前用户的其它设备  |
| void | **[removeMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-removemessage)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg) |
| void | **[ackMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-ackmessage)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>发送已读回执  |
| void | **[readCancel](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-readcancel)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>设置未读  |
| void | **[downloadThumbnail](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-downloadthumbnail)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>下载缩略图，下载状态变化和进度通过listener通知 缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。  |
| void | **[downloadAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-downloadattachment)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>下载附件，下载状态变化和进度通过listener通知  |
| void | **[cancelDownloadAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-canceldownloadattachment)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>取消下载附件  |
| int | **[transferingNum](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-transferingnum)**()<br>正在上传或下载中的文件数  |
| void | **[insertMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-insertmessages)**(final BMXMessageList list, final BMXCallBack callBack)<br>插入消息  |
| void | **[getMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-getmessage)**(final long msgId, final BMXDataCallBack< [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) > callBack)<br>读取一条消息  |
| void | **[deleteConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-deleteconversation)**(final long conversationId, final Boolean sync)<br>删除会话  |
| void | **[openConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-openconversation)**(final long conversationId, final BMXConversation.Type type, final boolean createIfNotExist, final BMXDataCallBack< [BMXConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md) > callBack)<br>打开一个会话  |
| void | **[getAllConversations](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-getallconversations)**(final BMXDataCallBack< BMXConversationList > callBack)<br>获取所有会话  |
| void | **[getAllConversationsUnreadCount](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-getallconversationsunreadcount)**(final BMXDataCallBack< Integer > callBack)<br>获取所有会话的全部未读数（标记为屏蔽的个人和群组的未读数不统计在内）  |
| void | **[retrieveHistoryMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-retrievehistorymessages)**(final [BMXConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md) conversation, final long refMsgId, final long size, final BMXDataCallBack< BMXMessageList > callBack)<br>拉取历史消息  |
| void | **[searchMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-searchmessages)**(final String keywords, final long refTime, final long size, final BMXConversation.Direction arg4, final BMXDataCallBack< BMXMessageListList > callBack)<br>搜索消息  |
| void | **[searchMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-searchmessages)**(final String keywords, final long refTime, final long size, final BMXDataCallBack< BMXMessageListList > callBack) |
| void | **[getGroupAckMessageUserIdList](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-getgroupackmessageuseridlist)**(final [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, final BMXDataCallBack< ListOfLongLong > callBack)<br>获取发送的群组消息已读用户id列表  |
| void | **[addChatListener](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-addchatlistener)**([BMXChatServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md) listener)<br>添加聊天监听者  |
| void | **[removeChatListener](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-removechatlistener)**([BMXChatServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md) listener)<br>移除聊天监听者  |

## Public Functions Documentation

### function BMXChatManager

```java
inline BMXChatManager(
    BMXChatService service
)
```


### function sendMessage

```java
inline void sendMessage(
    final BMXMessage msg
)
```

发送消息，消息状态变化会通过listener通知 

**Parameters**: 

  * **msg** 发送的消息 


### function resendMessage

```java
inline void resendMessage(
    final BMXMessage msg
)
```

重新发送消息，消息状态变化会通过listener通知 

**Parameters**: 

  * **msg** 重新发送的消息 


### function recallMessage

```java
inline void recallMessage(
    final BMXMessage msg
)
```

撤回消息，消息状态变化会通过listener通知 

**Parameters**: 

  * **msg** 撤回的消息 


### function forwardMessage

```java
inline void forwardMessage(
    final BMXMessageList list,
    final BMXConversation to,
    final BMXMessage newMsg,
    final BMXCallBack callBack
)
```

合并转发消息 

**Parameters**: 

  * **list** 转发的消息列表 
  * **to** 消息被转发到的会话 
  * **newMsg** 转发的消息列表合并后生成的新的单条转发消息 
  * **callBack** [BMXErrorCode]


### function forwardMessage

```java
inline void forwardMessage(
    final BMXMessage msg
)
```

简单转发消息，用户应当通过BMXMessage::createForwardMessage()先创建转发消息 

**Parameters**: 

  * **msg** 转发的消息 


### function readAllMessage

```java
inline void readAllMessage(
    final BMXMessage msg
)
```

标记此消息及之前全部消息为已读，该消息同步到当前用户的所有设备 

**Parameters**: 

  * **msg** 需要标记为此消息以前全部消息为已读的消息 


### function removeMessage

```java
inline void removeMessage(
    final BMXMessage msg,
    final boolean synchronize
)
```

删除此消息，该消息同步到当前用户的其它设备 

**Parameters**: 

  * **msg** 需要删除的消息 
  * **synchronize** 是否同步到其它设备，不同步的情况下只会删除本地存储的该条消息 


### function removeMessage

```java
inline void removeMessage(
    final BMXMessage msg
)
```


### function ackMessage

```java
inline void ackMessage(
    final BMXMessage msg
)
```

发送已读回执 

### function readCancel

```java
inline void readCancel(
    final BMXMessage msg
)
```

设置未读 

### function downloadThumbnail

```java
inline void downloadThumbnail(
    final BMXMessage msg
)
```

下载缩略图，下载状态变化和进度通过listener通知 缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。 

**Parameters**: 

  * **msg** 需要下载缩略图的消息 


### function downloadAttachment

```java
inline void downloadAttachment(
    final BMXMessage msg
)
```

下载附件，下载状态变化和进度通过listener通知 

**Parameters**: 

  * **msg** 需要下载附件的消息 


### function cancelDownloadAttachment

```java
inline void cancelDownloadAttachment(
    final BMXMessage msg
)
```

取消下载附件 

**Parameters**: 

  * **msg** 需要下载附件的消息 


### function transferingNum

```java
inline int transferingNum()
```

正在上传或下载中的文件数 

**Return**: 传输中的文件数 

### function insertMessages

```java
inline void insertMessages(
    final BMXMessageList list,
    final BMXCallBack callBack
)
```

插入消息 

**Parameters**: 

  * **list** 插入消息列表 
  * **callBack** [BMXErrorCode]


### function getMessage

```java
inline void getMessage(
    final long msgId,
    final BMXDataCallBack< BMXMessage > callBack
)
```

读取一条消息 

**Parameters**: 

  * **msgId** 需要获取消息的消息id 
  * **callBack** [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md)


### function deleteConversation

```java
inline void deleteConversation(
    final long conversationId,
    final Boolean sync
)
```

删除会话 

**Parameters**: 

  * **conversationId** 需要删除会话的会话id 
  * **sync** 是否同步删除其它设备该会话，默认为false，仅删除本设备会话 


### function openConversation

```java
inline void openConversation(
    final long conversationId,
    final BMXConversation.Type type,
    final boolean createIfNotExist,
    final BMXDataCallBack< BMXConversation > callBack
)
```

打开一个会话 

**Parameters**: 

  * **conversationId** 需要打开的会话的会话id 
  * **type** 会话的类型，单聊还是群聊。 
  * **createIfNotExist** 会话不存在的情况下是否要创建本地会话，默认为创建 
  * **callBack** [BMXConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md)


### function getAllConversations

```java
inline void getAllConversations(
    final BMXDataCallBack< BMXConversationList > callBack
)
```

获取所有会话 

**Parameters**: 

  * **callBack** BMXConversationList 


### function getAllConversationsUnreadCount

```java
inline void getAllConversationsUnreadCount(
    final BMXDataCallBack< Integer > callBack
)
```

获取所有会话的全部未读数（标记为屏蔽的个人和群组的未读数不统计在内） 

**Parameters**: 

  * **callBack** 未读数 


### function retrieveHistoryMessages

```java
inline void retrieveHistoryMessages(
    final BMXConversation conversation,
    final long refMsgId,
    final long size,
    final BMXDataCallBack< BMXMessageList > callBack
)
```

拉取历史消息 

**Parameters**: 

  * **conversation** 需要拉取历史消息的会话 
  * **refMsgId** 拉取会话消息的起始消息Id 
  * **size** 拉取的最大消息条数 
  * **callBack** BMXErrorCode，拉取操作获取的消息列表 


### function searchMessages

```java
inline void searchMessages(
    final String keywords,
    final long refTime,
    final long size,
    final BMXConversation.Direction arg4,
    final BMXDataCallBack< BMXMessageListList > callBack
)
```

搜索消息 

**Parameters**: 

  * **keywords** 搜索的关键字 
  * **refTime** 搜索消息的起始时间 
  * **size** 搜索的最大消息条数 
  * **arg4** 消息搜索方向，默认（Direction::Up）是从更早的消息中搜索 
  * **callBack** BMXErrorCode，搜索到的消息结果列表 


### function searchMessages

```java
inline void searchMessages(
    final String keywords,
    final long refTime,
    final long size,
    final BMXDataCallBack< BMXMessageListList > callBack
)
```


### function getGroupAckMessageUserIdList

```java
inline void getGroupAckMessageUserIdList(
    final BMXMessage msg,
    final BMXDataCallBack< ListOfLongLong > callBack
)
```

获取发送的群组消息已读用户id列表 

**Parameters**: 

  * **msg** 需要获取已读用户id列表的消息 
  * **callBack** [BMXErrorCode],对该条消息已读的用户id列表 


### function addChatListener

```java
inline void addChatListener(
    BMXChatServiceListener listener
)
```

添加聊天监听者 

**Parameters**: 

  * **listener** 聊天监听者 


### function removeChatListener

```java
inline void removeChatListener(
    BMXChatServiceListener listener
)
```

移除聊天监听者 

**Parameters**: 

  * **listener** 聊天监听者 


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800