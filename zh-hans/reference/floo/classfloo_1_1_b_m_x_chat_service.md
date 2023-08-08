---
title: floo::BMXChatService
summary: 聊天Service
---

# floo::BMXChatService

聊天Service

`#include <bmx_chat_service.h>`

## Public Types

|            | Name                                                                                                                                                                            |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class | <p><a href="classfloo_1_1_b_m_x_chat_service.md#enum-thumbnailstrategy"><strong>ThumbnailStrategy</strong></a> { ThirdpartyServerCreate = 1, LocalServerCreate}<br>缩略图生成策略,</p> |

## Public Functions

|                             | Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual                     | [**\~BMXChatService**](classfloo\_1\_1\_b\_m\_x\_chat\_service.md#function-\~bmxchatservice)()                                                                                                                                                                                                                                                                                                                                                                      |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-sendmessage"><strong>sendMessage</strong></a>(BMXMessagePtr msg) =0<br>发送消息，消息状态变化会通过listener通知</p>                                                                                                                                                                                                                                                                                                        |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-resendmessage"><strong>resendMessage</strong></a>(BMXMessagePtr msg) =0<br>重新发送消息，消息状态变化会通过listener通知</p>                                                                                                                                                                                                                                                                                                  |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-recallmessage"><strong>recallMessage</strong></a>(BMXMessagePtr msg) =0<br>撤回消息，消息状态变化会通过listener通知</p>                                                                                                                                                                                                                                                                                                    |
| virtual BMXErrorCode        | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-forwardmessage"><strong>forwardMessage</strong></a>(const BMXMessageList &#x26; list, BMXConversationPtr to, BMXMessagePtr &#x26; newMsg) =0<br>合并转发消息</p>                                                                                                                                                                                                                                                 |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-forwardmessage"><strong>forwardMessage</strong></a>(BMXMessagePtr msg) =0<br>简单转发消息，用户应当通过BMXMessage::createForwardMessage()先创建转发消息</p>                                                                                                                                                                                                                                                                    |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-ackmessage"><strong>ackMessage</strong></a>(BMXMessagePtr msg) =0<br>发送已读回执</p>                                                                                                                                                                                                                                                                                                                            |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-ackmessagedelivered"><strong>ackMessageDelivered</strong></a>(BMXMessagePtr msg) =0<br>发送送达回执</p>                                                                                                                                                                                                                                                                                                          |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-ackplaymessage"><strong>ackPlayMessage</strong></a>(BMXMessagePtr msg) =0<br>发送音频/视频消息已播放回执</p>                                                                                                                                                                                                                                                                                                            |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-readcancel"><strong>readCancel</strong></a>(BMXMessagePtr msg) =0<br>标记此消息为未读，该消息同步到当前用户的所有设备</p>                                                                                                                                                                                                                                                                                                          |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-readallmessage"><strong>readAllMessage</strong></a>(BMXMessagePtr msg) =0<br>标记此消息及之前全部消息为已读，该消息同步到当前用户的所有设备</p>                                                                                                                                                                                                                                                                                           |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-removemessage"><strong>removeMessage</strong></a>(BMXMessagePtr msg, bool synchronize =true) =0<br>删除此消息，该消息同步到当前用户的其它设备</p>                                                                                                                                                                                                                                                                               |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-downloadthumbnail"><strong>downloadThumbnail</strong></a>(BMXMessagePtr msg, <a href="classfloo_1_1_b_m_x_chat_service.md#enum-thumbnailstrategy">ThumbnailStrategy</a> strategy =<a href="classfloo_1_1_b_m_x_chat_service.md#enumvalue-thirdpartyservercreate">ThumbnailStrategy::ThirdpartyServerCreate</a>) =0<br>下载缩略图，下载状态变化和进度通过listener通知 缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。</p>            |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-downloadattachment"><strong>downloadAttachment</strong></a>(BMXMessagePtr msg) =0<br>下载附件，下载状态变化和进度通过listener通知</p>                                                                                                                                                                                                                                                                                        |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-downloadattachmentbyurl"><strong>downloadAttachmentByUrl</strong></a>(int64_t msgId, const std::string &#x26; url, const std::string &#x26; path) =0<br>下载附件，下载状态变化和进度通过listener通知</p>                                                                                                                                                                                                                     |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-canceluploadattachment"><strong>cancelUploadAttachment</strong></a>(BMXMessagePtr msg) =0<br>取消上传附件</p>                                                                                                                                                                                                                                                                                                    |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-canceldownloadattachment"><strong>cancelDownloadAttachment</strong></a>(BMXMessagePtr msg) =0<br>取消下载附件</p>                                                                                                                                                                                                                                                                                                |
| virtual int                 | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-transferingnum"><strong>transferingNum</strong></a>() =0<br>上传或下载中的文件数</p>                                                                                                                                                                                                                                                                                                                                 |
| virtual BMXErrorCode        | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-insertmessages"><strong>insertMessages</strong></a>(const BMXMessageList &#x26; list) =0<br>插入消息</p>                                                                                                                                                                                                                                                                                                       |
| virtual BMXMessagePtr       | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-getmessage"><strong>getMessage</strong></a>(int64_t msgId) =0<br>读取一条消息</p>                                                                                                                                                                                                                                                                                                                                |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-deleteconversation"><strong>deleteConversation</strong></a>(int64_t conversationId, bool synchronize =false) =0<br>删除会话</p>                                                                                                                                                                                                                                                                                |
| virtual BMXConversationPtr  | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-openconversation"><strong>openConversation</strong></a>(int64_t conversationId, <a href="classfloo_1_1_b_m_x_conversation.md#enum-type">BMXConversation::Type</a> type, bool createIfNotExist =true) =0<br>打开一个会话</p>                                                                                                                                                                                      |
| virtual std::string         | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-attachmentdir"><strong>attachmentDir</strong></a>() =0<br>获取附件保存路径</p>                                                                                                                                                                                                                                                                                                                                     |
| virtual std::string         | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-attachmentdirforconversation"><strong>attachmentDirForConversation</strong></a>(int64_t conversationId) =0<br>获取会话的附件保存路径</p>                                                                                                                                                                                                                                                                              |
| virtual BMXConversationList | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-getallconversations"><strong>getAllConversations</strong></a>() =0<br>获取所有会话</p>                                                                                                                                                                                                                                                                                                                           |
| virtual int                 | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-getallconversationsunreadcount"><strong>getAllConversationsUnreadCount</strong></a>() =0<br>获取所有会话的全部未读数（标记为屏蔽的个人和群组的未读数不统计在内）</p>                                                                                                                                                                                                                                                                         |
| virtual BMXErrorCode        | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-retrievehistorymessages"><strong>retrieveHistoryMessages</strong></a>(BMXConversationPtr conversation, int64_t refMsgId, size_t size, BMXMessageList &#x26; result) =0<br>拉取历史消息</p>                                                                                                                                                                                                                       |
| virtual BMXErrorCode        | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-searchmessagesbykeywords"><strong>searchMessagesByKeyWords</strong></a>(const std::string &#x26; keywords, int64_t refTime, size_t size, std::vector&#x3C; BMXMessageList > &#x26; result, <a href="classfloo_1_1_b_m_x_conversation.md#enum-direction">BMXConversation::Direction</a> =<a href="classfloo_1_1_b_m_x_conversation.md#enumvalue-up">BMXConversation::Direction::Up</a>) =0<br>使用关键字搜索消息</p> |
| virtual BMXErrorCode        | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-searchmessages"><strong>searchMessages</strong></a>(const std::string &#x26; keywords, int64_t refTime, size_t size, std::vector&#x3C; BMXMessageList > &#x26; result, <a href="classfloo_1_1_b_m_x_conversation.md#enum-direction">BMXConversation::Direction</a> =<a href="classfloo_1_1_b_m_x_conversation.md#enumvalue-up">BMXConversation::Direction::Up</a>) =0<br>Deprecated.</p>                   |
| virtual BMXErrorCode        | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-getgroupackmessageuseridlist"><strong>getGroupAckMessageUserIdList</strong></a>(BMXMessagePtr msg, std::vector&#x3C; int64_t > &#x26; groupMemberIdList) =0<br>获取发送的群组消息已读用户id列表</p>                                                                                                                                                                                                                       |
| virtual BMXErrorCode        | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-getgroupackmessageunreaduseridlist"><strong>getGroupAckMessageUnreadUserIdList</strong></a>(BMXMessagePtr msg, std::vector&#x3C; int64_t > &#x26; groupMemberIdList) =0<br>获取发送的群组消息未读用户id列表</p>                                                                                                                                                                                                           |
| virtual BMXErrorCode        | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-getgroupplayackmessageuseridlist"><strong>getGroupPlayAckMessageUserIdList</strong></a>(BMXMessagePtr msg, std::vector&#x3C; int64_t > &#x26; groupMemberIdList) =0<br>获取发送的群组音频/视频消息已播放用户id列表（仅用于音频/视频消息）</p>                                                                                                                                                                                             |
| virtual BMXErrorCode        | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-getgroupunplayackmessageuseridlist"><strong>getGroupUnPlayAckMessageUserIdList</strong></a>(BMXMessagePtr msg, std::vector&#x3C; int64_t > &#x26; groupMemberIdList) =0<br>获取发送的群组音频/视频消息未播放用户id列表（仅用于音频/视频消息）</p>                                                                                                                                                                                         |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-addchatlistener"><strong>addChatListener</strong></a>(<a href="classfloo_1_1_b_m_x_chat_service_listener.md">BMXChatServiceListener</a> * listener) =0<br>添加聊天监听者</p>                                                                                                                                                                                                                                      |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-removechatlistener"><strong>removeChatListener</strong></a>(<a href="classfloo_1_1_b_m_x_chat_service_listener.md">BMXChatServiceListener</a> * listener) =0<br>移除聊天监听者</p>                                                                                                                                                                                                                                |

## Protected Functions

|      | Name                                                                                                                          |
| ---- | ----------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXChatService**](classfloo\_1\_1\_b\_m\_x\_chat\_service.md#function-bmxchatservice)()                                    |
| void | [**updateMessageId**](classfloo\_1\_1\_b\_m\_x\_chat\_service.md#function-updatemessageid)(BMXMessagePtr msg, int64\_t newId) |

## Public Types Documentation

### enum ThumbnailStrategy

| Enumerator             | Value | Description |
| ---------------------- | ----- | ----------- |
| ThirdpartyServerCreate | 1     | 第三方服务器生成    |
| LocalServerCreate      |       | 本地服务器生成     |

缩略图生成策略,

## Public Functions Documentation

### function \~BMXChatService

```cpp
inline virtual ~BMXChatService()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function resendMessage

```cpp
virtual void resendMessage(
    BMXMessagePtr msg
) =0
```

重新发送消息，消息状态变化会通过listener通知

**Parameters**:

* **msg** 重新发送的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function recallMessage

```cpp
virtual void recallMessage(
    BMXMessagePtr msg
) =0
```

撤回消息，消息状态变化会通过listener通知

**Parameters**:

* **msg** 撤回的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function forwardMessage

```cpp
virtual void forwardMessage(
    BMXMessagePtr msg
) =0
```

简单转发消息，用户应当通过BMXMessage::createForwardMessage()先创建转发消息

**Parameters**:

* **msg** 转发的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function ackMessage

```cpp
virtual void ackMessage(
    BMXMessagePtr msg
) =0
```

发送已读回执

**Parameters**:

* **msg** 需要发送已读回执的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function ackMessageDelivered

```cpp
virtual void ackMessageDelivered(
    BMXMessagePtr msg
) =0
```

发送送达回执

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function ackPlayMessage

```cpp
virtual void ackPlayMessage(
    BMXMessagePtr msg
) =0
```

发送音频/视频消息已播放回执

**Parameters**:

* **msg** 需要发送已读回执的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function readCancel

```cpp
virtual void readCancel(
    BMXMessagePtr msg
) =0
```

标记此消息为未读，该消息同步到当前用户的所有设备

**Parameters**:

* **msg** 需要发送消息已读取消的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function readAllMessage

```cpp
virtual void readAllMessage(
    BMXMessagePtr msg
) =0
```

标记此消息及之前全部消息为已读，该消息同步到当前用户的所有设备

**Parameters**:

* **msg** 需要标记为此消息以前全部消息为已读的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function downloadAttachment

```cpp
virtual void downloadAttachment(
    BMXMessagePtr msg
) =0
```

下载附件，下载状态变化和进度通过listener通知

**Parameters**:

* **msg** 需要下载附件的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function downloadAttachmentByUrl

```cpp
virtual void downloadAttachmentByUrl(
    int64_t msgId,
    const std::string & url,
    const std::string & path
) =0
```

下载附件，下载状态变化和进度通过listener通知

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function cancelUploadAttachment

```cpp
virtual void cancelUploadAttachment(
    BMXMessagePtr msg
) =0
```

取消上传附件

**Parameters**:

* **msg** 需要取消上传附件的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function cancelDownloadAttachment

```cpp
virtual void cancelDownloadAttachment(
    BMXMessagePtr msg
) =0
```

取消下载附件

**Parameters**:

* **msg** 需要取消下载附件的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function transferingNum

```cpp
virtual int transferingNum() =0
```

上传或下载中的文件数

**Return**: 文件数

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function attachmentDir

```cpp
virtual std::string attachmentDir() =0
```

获取附件保存路径

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function getAllConversations

```cpp
virtual BMXConversationList getAllConversations() =0
```

获取所有会话

**Return**: BMXConversationList

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function getAllConversationsUnreadCount

```cpp
virtual int getAllConversationsUnreadCount() =0
```

获取所有会话的全部未读数（标记为屏蔽的个人和群组的未读数不统计在内）

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function addChatListener

```cpp
virtual void addChatListener(
    BMXChatServiceListener * listener
) =0
```

添加聊天监听者

**Parameters**:

* **listener** 聊天监听者

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function BMXChatService

```cpp
inline BMXChatService()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function updateMessageId

```cpp
void updateMessageId(
    BMXMessagePtr msg,
    int64_t newId
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
