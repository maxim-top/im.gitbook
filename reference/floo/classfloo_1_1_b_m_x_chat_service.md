---
title: floo::BMXChatService
summary: 聊天Service 

---

# floo::BMXChatService



聊天Service 


`#include <bmx_chat_service.h>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[ThumbnailStrategy](classfloo_1_1_b_m_x_chat_service.md#enum-thumbnailstrategy)** { ThirdpartyServerCreate = 1, LocalServerCreate}<br>缩略图生成策略,  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXChatService](classfloo_1_1_b_m_x_chat_service.md#function-~bmxchatservice)**() |
| virtual void | **[sendMessage](classfloo_1_1_b_m_x_chat_service.md#function-sendmessage)**(BMXMessagePtr msg) =0<br>发送消息，消息状态变化会通过listener通知  |
| virtual void | **[resendMessage](classfloo_1_1_b_m_x_chat_service.md#function-resendmessage)**(BMXMessagePtr msg) =0<br>重新发送消息，消息状态变化会通过listener通知  |
| virtual void | **[recallMessage](classfloo_1_1_b_m_x_chat_service.md#function-recallmessage)**(BMXMessagePtr msg) =0<br>撤回消息，消息状态变化会通过listener通知  |
| virtual BMXErrorCode | **[forwardMessage](classfloo_1_1_b_m_x_chat_service.md#function-forwardmessage)**(const BMXMessageList & list, BMXConversationPtr to, BMXMessagePtr & newMsg) =0<br>合并转发消息  |
| virtual void | **[forwardMessage](classfloo_1_1_b_m_x_chat_service.md#function-forwardmessage)**(BMXMessagePtr msg) =0<br>简单转发消息，用户应当通过BMXMessage::createForwardMessage()先创建转发消息  |
| virtual void | **[ackMessage](classfloo_1_1_b_m_x_chat_service.md#function-ackmessage)**(BMXMessagePtr msg) =0<br>发送已读回执  |
| virtual void | **[ackMessageDelivered](classfloo_1_1_b_m_x_chat_service.md#function-ackmessagedelivered)**(BMXMessagePtr msg) =0<br>发送送达回执  |
| virtual void | **[ackPlayMessage](classfloo_1_1_b_m_x_chat_service.md#function-ackplaymessage)**(BMXMessagePtr msg) =0<br>发送音频/视频消息已播放回执  |
| virtual void | **[readCancel](classfloo_1_1_b_m_x_chat_service.md#function-readcancel)**(BMXMessagePtr msg) =0<br>标记此消息为未读，该消息同步到当前用户的所有设备  |
| virtual void | **[readAllMessage](classfloo_1_1_b_m_x_chat_service.md#function-readallmessage)**(BMXMessagePtr msg) =0<br>标记此消息及之前全部消息为已读，该消息同步到当前用户的所有设备  |
| virtual void | **[removeMessage](classfloo_1_1_b_m_x_chat_service.md#function-removemessage)**(BMXMessagePtr msg, bool synchronize =true) =0<br>删除此消息，该消息同步到当前用户的其它设备  |
| virtual void | **[downloadThumbnail](classfloo_1_1_b_m_x_chat_service.md#function-downloadthumbnail)**(BMXMessagePtr msg, [ThumbnailStrategy](classfloo_1_1_b_m_x_chat_service.md#enum-thumbnailstrategy) strategy =[ThumbnailStrategy::ThirdpartyServerCreate](classfloo_1_1_b_m_x_chat_service.md#enumvalue-thirdpartyservercreate)) =0<br>下载缩略图，下载状态变化和进度通过listener通知 缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。  |
| virtual void | **[downloadAttachment](classfloo_1_1_b_m_x_chat_service.md#function-downloadattachment)**(BMXMessagePtr msg) =0<br>下载附件，下载状态变化和进度通过listener通知  |
| virtual void | **[downloadAttachmentByUrl](classfloo_1_1_b_m_x_chat_service.md#function-downloadattachmentbyurl)**(int64_t msgId, const std::string & url, const std::string & path) =0<br>下载附件，下载状态变化和进度通过listener通知  |
| virtual void | **[cancelUploadAttachment](classfloo_1_1_b_m_x_chat_service.md#function-canceluploadattachment)**(BMXMessagePtr msg) =0<br>取消上传附件  |
| virtual void | **[cancelDownloadAttachment](classfloo_1_1_b_m_x_chat_service.md#function-canceldownloadattachment)**(BMXMessagePtr msg) =0<br>取消下载附件  |
| virtual int | **[transferingNum](classfloo_1_1_b_m_x_chat_service.md#function-transferingnum)**() =0<br>上传或下载中的文件数  |
| virtual BMXErrorCode | **[insertMessages](classfloo_1_1_b_m_x_chat_service.md#function-insertmessages)**(const BMXMessageList & list) =0<br>插入消息  |
| virtual BMXMessagePtr | **[getMessage](classfloo_1_1_b_m_x_chat_service.md#function-getmessage)**(int64_t msgId) =0<br>读取一条消息  |
| virtual void | **[deleteConversation](classfloo_1_1_b_m_x_chat_service.md#function-deleteconversation)**(int64_t conversationId, bool synchronize =false) =0<br>删除会话  |
| virtual BMXConversationPtr | **[openConversation](classfloo_1_1_b_m_x_chat_service.md#function-openconversation)**(int64_t conversationId, [BMXConversation::Type](classfloo_1_1_b_m_x_conversation.md#enum-type) type, bool createIfNotExist =true) =0<br>打开一个会话  |
| virtual std::string | **[attachmentDir](classfloo_1_1_b_m_x_chat_service.md#function-attachmentdir)**() =0<br>获取附件保存路径  |
| virtual std::string | **[attachmentDirForConversation](classfloo_1_1_b_m_x_chat_service.md#function-attachmentdirforconversation)**(int64_t conversationId) =0<br>获取会话的附件保存路径  |
| virtual BMXConversationList | **[getAllConversations](classfloo_1_1_b_m_x_chat_service.md#function-getallconversations)**() =0<br>获取所有会话  |
| virtual int | **[getAllConversationsUnreadCount](classfloo_1_1_b_m_x_chat_service.md#function-getallconversationsunreadcount)**() =0<br>获取所有会话的全部未读数（标记为屏蔽的个人和群组的未读数不统计在内）  |
| virtual BMXErrorCode | **[retrieveHistoryMessages](classfloo_1_1_b_m_x_chat_service.md#function-retrievehistorymessages)**(BMXConversationPtr conversation, int64_t refMsgId, size_t size, BMXMessageList & result) =0<br>拉取历史消息  |
| virtual BMXErrorCode | **[searchMessagesByKeyWords](classfloo_1_1_b_m_x_chat_service.md#function-searchmessagesbykeywords)**(const std::string & keywords, int64_t refTime, size_t size, std::vector< BMXMessageList > & result, [BMXConversation::Direction](classfloo_1_1_b_m_x_conversation.md#enum-direction)  =[BMXConversation::Direction::Up](classfloo_1_1_b_m_x_conversation.md#enumvalue-up)) =0<br>使用关键字搜索消息  |
| virtual BMXErrorCode | **[searchMessages](classfloo_1_1_b_m_x_chat_service.md#function-searchmessages)**(const std::string & keywords, int64_t refTime, size_t size, std::vector< BMXMessageList > & result, [BMXConversation::Direction](classfloo_1_1_b_m_x_conversation.md#enum-direction)  =[BMXConversation::Direction::Up](classfloo_1_1_b_m_x_conversation.md#enumvalue-up)) =0<br>Deprecated.  |
| virtual BMXErrorCode | **[getGroupAckMessageUserIdList](classfloo_1_1_b_m_x_chat_service.md#function-getgroupackmessageuseridlist)**(BMXMessagePtr msg, std::vector< int64_t > & groupMemberIdList) =0<br>获取发送的群组消息已读用户id列表  |
| virtual BMXErrorCode | **[getGroupAckMessageUnreadUserIdList](classfloo_1_1_b_m_x_chat_service.md#function-getgroupackmessageunreaduseridlist)**(BMXMessagePtr msg, std::vector< int64_t > & groupMemberIdList) =0<br>获取发送的群组消息未读用户id列表  |
| virtual BMXErrorCode | **[getGroupPlayAckMessageUserIdList](classfloo_1_1_b_m_x_chat_service.md#function-getgroupplayackmessageuseridlist)**(BMXMessagePtr msg, std::vector< int64_t > & groupMemberIdList) =0<br>获取发送的群组音频/视频消息已播放用户id列表（仅用于音频/视频消息）  |
| virtual BMXErrorCode | **[getGroupUnPlayAckMessageUserIdList](classfloo_1_1_b_m_x_chat_service.md#function-getgroupunplayackmessageuseridlist)**(BMXMessagePtr msg, std::vector< int64_t > & groupMemberIdList) =0<br>获取发送的群组音频/视频消息未播放用户id列表（仅用于音频/视频消息）  |
| virtual void | **[addChatListener](classfloo_1_1_b_m_x_chat_service.md#function-addchatlistener)**([BMXChatServiceListener](classfloo_1_1_b_m_x_chat_service_listener.md) * listener) =0<br>添加聊天监听者  |
| virtual void | **[removeChatListener](classfloo_1_1_b_m_x_chat_service.md#function-removechatlistener)**([BMXChatServiceListener](classfloo_1_1_b_m_x_chat_service_listener.md) * listener) =0<br>移除聊天监听者  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXChatService](classfloo_1_1_b_m_x_chat_service.md#function-bmxchatservice)**() |
| void | **[updateMessageId](classfloo_1_1_b_m_x_chat_service.md#function-updatemessageid)**(BMXMessagePtr msg, int64_t newId) |

## Public Types Documentation

### enum ThumbnailStrategy

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| ThirdpartyServerCreate | 1| 第三方服务器生成   |
| LocalServerCreate | | 本地服务器生成   |



缩略图生成策略, 

## Public Functions Documentation

### function ~BMXChatService

```cpp
inline virtual ~BMXChatService()
```


### function sendMessage

```cpp
virtual void sendMessage(
    BMXMessagePtr msg
) =0
```

发送消息，消息状态变化会通过listener通知 

**Parameters**: 

  * **msg** 发送的消息 


### function resendMessage

```cpp
virtual void resendMessage(
    BMXMessagePtr msg
) =0
```

重新发送消息，消息状态变化会通过listener通知 

**Parameters**: 

  * **msg** 重新发送的消息 


### function recallMessage

```cpp
virtual void recallMessage(
    BMXMessagePtr msg
) =0
```

撤回消息，消息状态变化会通过listener通知 

**Parameters**: 

  * **msg** 撤回的消息 


### function forwardMessage

```cpp
virtual BMXErrorCode forwardMessage(
    const BMXMessageList & list,
    BMXConversationPtr to,
    BMXMessagePtr & newMsg
) =0
```

合并转发消息 

**Parameters**: 

  * **list** 转发的消息列表 
  * **to** 消息被转发到的会话 
  * **newMsg** 转发的消息列表合并后生成的新的单条转发消息 


**Return**: BMXErrorCode 

### function forwardMessage

```cpp
virtual void forwardMessage(
    BMXMessagePtr msg
) =0
```

简单转发消息，用户应当通过BMXMessage::createForwardMessage()先创建转发消息 

**Parameters**: 

  * **msg** 转发的消息 


### function ackMessage

```cpp
virtual void ackMessage(
    BMXMessagePtr msg
) =0
```

发送已读回执 

**Parameters**: 

  * **msg** 需要发送已读回执的消息 


### function ackMessageDelivered

```cpp
virtual void ackMessageDelivered(
    BMXMessagePtr msg
) =0
```

发送送达回执 

### function ackPlayMessage

```cpp
virtual void ackPlayMessage(
    BMXMessagePtr msg
) =0
```

发送音频/视频消息已播放回执 

**Parameters**: 

  * **msg** 需要发送已读回执的消息 


### function readCancel

```cpp
virtual void readCancel(
    BMXMessagePtr msg
) =0
```

标记此消息为未读，该消息同步到当前用户的所有设备 

**Parameters**: 

  * **msg** 需要发送消息已读取消的消息 


### function readAllMessage

```cpp
virtual void readAllMessage(
    BMXMessagePtr msg
) =0
```

标记此消息及之前全部消息为已读，该消息同步到当前用户的所有设备 

**Parameters**: 

  * **msg** 需要标记为此消息以前全部消息为已读的消息 


### function removeMessage

```cpp
virtual void removeMessage(
    BMXMessagePtr msg,
    bool synchronize =true
) =0
```

删除此消息，该消息同步到当前用户的其它设备 

**Parameters**: 

  * **msg** 需要删除的消息 
  * **synchronize** 是否同步到其它设备，不同步的情况下只会删除本地存储的该条消息 


### function downloadThumbnail

```cpp
virtual void downloadThumbnail(
    BMXMessagePtr msg,
    ThumbnailStrategy strategy =ThumbnailStrategy::ThirdpartyServerCreate
) =0
```

下载缩略图，下载状态变化和进度通过listener通知 缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。 

**Parameters**: 

  * **msg** 需要下载缩略图的消息 
  * **strategy** 缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。 


### function downloadAttachment

```cpp
virtual void downloadAttachment(
    BMXMessagePtr msg
) =0
```

下载附件，下载状态变化和进度通过listener通知 

**Parameters**: 

  * **msg** 需要下载附件的消息 


### function downloadAttachmentByUrl

```cpp
virtual void downloadAttachmentByUrl(
    int64_t msgId,
    const std::string & url,
    const std::string & path
) =0
```

下载附件，下载状态变化和进度通过listener通知 

### function cancelUploadAttachment

```cpp
virtual void cancelUploadAttachment(
    BMXMessagePtr msg
) =0
```

取消上传附件 

**Parameters**: 

  * **msg** 需要取消上传附件的消息 


### function cancelDownloadAttachment

```cpp
virtual void cancelDownloadAttachment(
    BMXMessagePtr msg
) =0
```

取消下载附件 

**Parameters**: 

  * **msg** 需要取消下载附件的消息 


### function transferingNum

```cpp
virtual int transferingNum() =0
```

上传或下载中的文件数 

**Return**: 文件数 

### function insertMessages

```cpp
virtual BMXErrorCode insertMessages(
    const BMXMessageList & list
) =0
```

插入消息 

**Parameters**: 

  * **list** 插入消息列表 


**Return**: BMXErrorCode 

### function getMessage

```cpp
virtual BMXMessagePtr getMessage(
    int64_t msgId
) =0
```

读取一条消息 

**Parameters**: 

  * **msgId** 需要获取消息的消息id 


**Return**: BMXMessagePtr 

### function deleteConversation

```cpp
virtual void deleteConversation(
    int64_t conversationId,
    bool synchronize =false
) =0
```

删除会话 

**Parameters**: 

  * **conversationId** 需要删除会话的会话id 
  * **synchronize** 是否同步删除其它设备该会话，默认为false，仅删除本设备会话 


### function openConversation

```cpp
virtual BMXConversationPtr openConversation(
    int64_t conversationId,
    BMXConversation::Type type,
    bool createIfNotExist =true
) =0
```

打开一个会话 

**Parameters**: 

  * **conversationId** 需要打开的会话的会话id 
  * **type** 会话的类型，单聊还是群聊。 
  * **createIfNotExist** 会话不存在的情况下是否要创建本地会话，默认为创建 


**Return**: BMXConversationPtr 

### function attachmentDir

```cpp
virtual std::string attachmentDir() =0
```

获取附件保存路径 

**Return**: std::string 

### function attachmentDirForConversation

```cpp
virtual std::string attachmentDirForConversation(
    int64_t conversationId
) =0
```

获取会话的附件保存路径 

**Parameters**: 

  * **conversationId** 需要获取会话附件路径的会话id 


**Return**: std::string 

### function getAllConversations

```cpp
virtual BMXConversationList getAllConversations() =0
```

获取所有会话 

**Return**: BMXConversationList 

### function getAllConversationsUnreadCount

```cpp
virtual int getAllConversationsUnreadCount() =0
```

获取所有会话的全部未读数（标记为屏蔽的个人和群组的未读数不统计在内） 

**Return**: int 

### function retrieveHistoryMessages

```cpp
virtual BMXErrorCode retrieveHistoryMessages(
    BMXConversationPtr conversation,
    int64_t refMsgId,
    size_t size,
    BMXMessageList & result
) =0
```

拉取历史消息 

**Parameters**: 

  * **conversation** 需要拉取历史消息的会话 
  * **refMsgId** 拉取会话消息的起始消息Id 
  * **size** 拉取的最大消息条数 
  * **result** 拉取操作获取的消息列表，外部初始化传入空列表。 


**Return**: BMXErrorCode 

### function searchMessagesByKeyWords

```cpp
virtual BMXErrorCode searchMessagesByKeyWords(
    const std::string & keywords,
    int64_t refTime,
    size_t size,
    std::vector< BMXMessageList > & result,
    BMXConversation::Direction  =BMXConversation::Direction::Up
) =0
```

使用关键字搜索消息 

**Parameters**: 

  * **keywords** 搜索的关键字 
  * **refTime** 搜索消息的起始时间 
  * **size** 搜索的最大消息条数 
  * **result** 搜索到的消息结果列表，外部初始化传入空列表。 
  * **Direction** 消息搜索方向，默认（Direction::Up）是从更早的消息中搜索 


**Return**: BMXErrorCode 

### function searchMessages

```cpp
virtual BMXErrorCode searchMessages(
    const std::string & keywords,
    int64_t refTime,
    size_t size,
    std::vector< BMXMessageList > & result,
    BMXConversation::Direction  =BMXConversation::Direction::Up
) =0
```

Deprecated. 

**Parameters**: 

  * **keywords** 搜索的关键字 
  * **refTime** 搜索消息的起始时间 
  * **size** 搜索的最大消息条数 
  * **result** 搜索到的消息结果列表，外部初始化传入空列表。 
  * **Direction** 消息搜索方向，默认（Direction::Up）是从更早的消息中搜索 


**Return**: BMXErrorCode 

use searchMessagesByKeyWords instead.

搜索消息 


### function getGroupAckMessageUserIdList

```cpp
virtual BMXErrorCode getGroupAckMessageUserIdList(
    BMXMessagePtr msg,
    std::vector< int64_t > & groupMemberIdList
) =0
```

获取发送的群组消息已读用户id列表 

**Parameters**: 

  * **msg** 需要获取已读用户id列表的消息 
  * **groupMemberIdList** 对该条消息已读的用户id列表，初始传入为空列表 


**Return**: BMXErrorCode 

### function getGroupAckMessageUnreadUserIdList

```cpp
virtual BMXErrorCode getGroupAckMessageUnreadUserIdList(
    BMXMessagePtr msg,
    std::vector< int64_t > & groupMemberIdList
) =0
```

获取发送的群组消息未读用户id列表 

**Parameters**: 

  * **msg** 需要获取未读用户id列表的消息 
  * **groupMemberIdList** 对该条消息未读的用户id列表，初始传入为空列表 


**Return**: BMXErrorCode 

### function getGroupPlayAckMessageUserIdList

```cpp
virtual BMXErrorCode getGroupPlayAckMessageUserIdList(
    BMXMessagePtr msg,
    std::vector< int64_t > & groupMemberIdList
) =0
```

获取发送的群组音频/视频消息已播放用户id列表（仅用于音频/视频消息） 

**Parameters**: 

  * **msg** 需要获取已播放用户id列表的消息 
  * **groupMemberIdList** 对该条消息已播放的用户id列表，初始传入为空列表 


**Return**: BMXErrorCode 

### function getGroupUnPlayAckMessageUserIdList

```cpp
virtual BMXErrorCode getGroupUnPlayAckMessageUserIdList(
    BMXMessagePtr msg,
    std::vector< int64_t > & groupMemberIdList
) =0
```

获取发送的群组音频/视频消息未播放用户id列表（仅用于音频/视频消息） 

**Parameters**: 

  * **msg** 需要获取未播放用户id列表的消息 
  * **groupMemberIdList** 对该条消息未播放的用户id列表，初始传入为空列表 


**Return**: BMXErrorCode 

### function addChatListener

```cpp
virtual void addChatListener(
    BMXChatServiceListener * listener
) =0
```

添加聊天监听者 

**Parameters**: 

  * **listener** 聊天监听者 


### function removeChatListener

```cpp
virtual void removeChatListener(
    BMXChatServiceListener * listener
) =0
```

移除聊天监听者 

**Parameters**: 

  * **listener** 聊天监听者 


## Protected Functions Documentation

### function BMXChatService

```cpp
inline BMXChatService()
```


### function updateMessageId

```cpp
void updateMessageId(
    BMXMessagePtr msg,
    int64_t newId
)
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800