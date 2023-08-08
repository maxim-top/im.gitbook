---
title: im::floo::floolib::BMXChatService
summary: 聊天Service
---

# im::floo::floolib::BMXChatService

聊天Service

## Public Functions

|                                                                                   | Name                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void                                                                 | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md#function-delete)()                                                                                                                                                                                                                                           |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-sendmessage"><strong>sendMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>发送消息，消息状态变化会通过listener通知</p>                                                                                                     |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-resendmessage"><strong>resendMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>重新发送消息，消息状态变化会通过listener通知</p>                                                                                               |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-recallmessage"><strong>recallMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>撤回消息，消息状态变化会通过listener通知</p>                                                                                                 |
| \[BMXErrorCode]                                                                   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-forwardmessage"><strong>forwardMessage</strong></a>(BMXMessageList list, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md">BMXConversation</a> to, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> newMsg)<br>合并转发消息</p>  |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-forwardmessage"><strong>forwardMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>简单转发消息，用户应当通过BMXMessage::createForwardMessage()先创建转发消息</p>                                                                 |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-ackmessage"><strong>ackMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>发送已读回执</p>                                                                                                                         |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-ackmessagedelivered"><strong>ackMessageDelivered</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>发送送达回执</p>                                                                                                       |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-ackplaymessage"><strong>ackPlayMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>发送已播放回执</p>                                                                                                                |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-readcancel"><strong>readCancel</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>标记此消息为未读，该消息同步到当前用户的所有设备</p>                                                                                                       |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-readallmessage"><strong>readAllMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>标记此消息及之前全部消息为已读，该消息同步到当前用户的所有设备</p>                                                                                        |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-removemessage"><strong>removeMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, boolean synchronize)<br>删除此消息，该消息同步到当前用户的其它设备</p>                                                                               |
| void                                                                              | [**removeMessage**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md#function-removemessage)([BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md) msg)                                                                                                                                                  |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-downloadthumbnail"><strong>downloadThumbnail</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, BMXChatService.ThumbnailStrategy strategy)<br>下载缩略图，下载状态变化和进度通过listener通知 缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。</p> |
| void                                                                              | [**downloadThumbnail**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md#function-downloadthumbnail)([BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md) msg)                                                                                                                                          |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-downloadattachment"><strong>downloadAttachment</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>下载附件，下载状态变化和进度通过listener通知</p>                                                                                     |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-downloadattachmentbyurl"><strong>downloadAttachmentByUrl</strong></a>(long msgId, String url, String path)<br>下载附件，下载状态变化和进度通过listener通知</p>                                                                                                                    |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-canceluploadattachment"><strong>cancelUploadAttachment</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>取消上传附件</p>                                                                                                 |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-canceldownloadattachment"><strong>cancelDownloadAttachment</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>取消上传附件</p>                                                                                             |
| int                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-transferingnum"><strong>transferingNum</strong></a>()<br>上传或下载中的文件数</p>                                                                                                                                                                                         |
| \[BMXErrorCode]                                                                   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-insertmessages"><strong>insertMessages</strong></a>(BMXMessageList list)<br>插入消息</p>                                                                                                                                                                            |
| [BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md)           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getmessage"><strong>getMessage</strong></a>(long msgId)<br>读取一条消息</p>                                                                                                                                                                                           |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-deleteconversation"><strong>deleteConversation</strong></a>(long conversationId, boolean synchronize)<br>删除会话</p>                                                                                                                                               |
| void                                                                              | [**deleteConversation**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md#function-deleteconversation)(long conversationId)                                                                                                                                                                                                |
| [BMXConversation](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md) | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-openconversation"><strong>openConversation</strong></a>(long conversationId, BMXConversation.Type type, boolean createIfNotExist)<br>打开一个会话</p>                                                                                                                 |
| [BMXConversation](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md) | [**openConversation**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md#function-openconversation)(long conversationId, BMXConversation.Type type)                                                                                                                                                                         |
| String                                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-attachmentdir"><strong>attachmentDir</strong></a>()<br>获取附件保存路径</p>                                                                                                                                                                                             |
| String                                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-attachmentdirforconversation"><strong>attachmentDirForConversation</strong></a>(long conversationId)<br>获取会话的附件保存路径</p>                                                                                                                                         |
| BMXConversationList                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getallconversations"><strong>getAllConversations</strong></a>()<br>获取所有会话</p>                                                                                                                                                                                   |
| int                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getallconversationsunreadcount"><strong>getAllConversationsUnreadCount</strong></a>()<br>获取所有会话的全部未读数（标记为屏蔽的个人和群组的未读数不统计在内）</p>                                                                                                                                 |
| \[BMXErrorCode]                                                                   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-retrievehistorymessages"><strong>retrieveHistoryMessages</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md">BMXConversation</a> conversation, long refMsgId, long size, BMXMessageList result)<br>拉取历史消息</p>                           |
| \[BMXErrorCode]                                                                   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-searchmessagesbykeywords"><strong>searchMessagesByKeyWords</strong></a>(String keywords, long refTime, long size, BMXMessageListList result, BMXConversation.Direction arg4)<br>搜索消息</p>                                                                        |
| \[BMXErrorCode]                                                                   | [**searchMessagesByKeyWords**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md#function-searchmessagesbykeywords)(String keywords, long refTime, long size, BMXMessageListList result)                                                                                                                                    |
| \[BMXErrorCode]                                                                   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-searchmessages"><strong>searchMessages</strong></a>(String keywords, long refTime, long size, BMXMessageListList result, BMXConversation.Direction arg4)<br>搜索消息</p>                                                                                            |
| \[BMXErrorCode]                                                                   | [**searchMessages**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md#function-searchmessages)(String keywords, long refTime, long size, BMXMessageListList result)                                                                                                                                                        |
| \[BMXErrorCode]                                                                   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getgroupackmessageuseridlist"><strong>getGroupAckMessageUserIdList</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, ListOfLongLong groupMemberIdList)<br>获取发送的群组消息已读用户id列表</p>                                        |
| \[BMXErrorCode]                                                                   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getgroupackmessageunreaduseridlist"><strong>getGroupAckMessageUnreadUserIdList</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, ListOfLongLong groupMemberIdList)<br>获取发送的群组消息未读用户id列表</p>                            |
| \[BMXErrorCode]                                                                   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getgroupplayackmessageuseridlist"><strong>getGroupPlayAckMessageUserIdList</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, ListOfLongLong groupMemberIdList)<br>获取发送的群组消息已播放用户id列表</p>                               |
| \[BMXErrorCode]                                                                   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getgroupunplayackmessageuseridlist"><strong>getGroupUnPlayAckMessageUserIdList</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, ListOfLongLong groupMemberIdList)<br>获取发送的群组消息未播放用户id列表</p>                           |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-addchatlistener"><strong>addChatListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md">BMXChatServiceListener</a> listener)<br>添加聊天监听者</p>                                                                               |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-removechatlistener"><strong>removeChatListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md">BMXChatServiceListener</a> listener)<br>移除聊天监听者</p>                                                                         |

## Protected Functions

|      | Name                                                                                                                                                                                   |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXChatService**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md#function-bmxchatservice)(long cPtr, boolean cMemoryOwn)                                           |
| void | [**finalize**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md#function-finalize)()                                                                                    |
| long | [**getCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md#function-getcptr)([BMXChatService](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md) obj) |

## Protected Attributes

|                   | Name                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------- |
| transient boolean | [**swigCMemOwn**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md#variable-swigcmemown) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function sendMessage

```java
inline void sendMessage(
    BMXMessage msg
)
```

发送消息，消息状态变化会通过listener通知

**Parameters**:

* **msg** 发送的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function resendMessage

```java
inline void resendMessage(
    BMXMessage msg
)
```

重新发送消息，消息状态变化会通过listener通知

**Parameters**:

* **msg** 重新发送的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function recallMessage

```java
inline void recallMessage(
    BMXMessage msg
)
```

撤回消息，消息状态变化会通过listener通知

**Parameters**:

* **msg** 撤回的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function forwardMessage

```java
inline BMXErrorCode forwardMessage(
    BMXMessageList list,
    BMXConversation to,
    BMXMessage newMsg
)
```

合并转发消息

**Parameters**:

* **list** 转发的消息列表
* **to** 消息被转发到的会话
* **newMsg** 转发的消息列表合并后生成的新的单条转发消息

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function forwardMessage

```java
inline void forwardMessage(
    BMXMessage msg
)
```

简单转发消息，用户应当通过BMXMessage::createForwardMessage()先创建转发消息

**Parameters**:

* **msg** 转发的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function ackMessage

```java
inline void ackMessage(
    BMXMessage msg
)
```

发送已读回执

**Parameters**:

* **msg** 需要发送已读回执的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function ackMessageDelivered

```java
inline void ackMessageDelivered(
    BMXMessage msg
)
```

发送送达回执

**Parameters**:

* **msg** 需要发送送达回执的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function ackPlayMessage

```java
inline void ackPlayMessage(
    BMXMessage msg
)
```

发送已播放回执

**Parameters**:

* **msg** 需要发送已读回播放的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function readCancel

```java
inline void readCancel(
    BMXMessage msg
)
```

标记此消息为未读，该消息同步到当前用户的所有设备

**Parameters**:

* **msg** 需要发送消息已读取消的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function readAllMessage

```java
inline void readAllMessage(
    BMXMessage msg
)
```

标记此消息及之前全部消息为已读，该消息同步到当前用户的所有设备

**Parameters**:

* **msg** 需要标记为此消息以前全部消息为已读的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function removeMessage

```java
inline void removeMessage(
    BMXMessage msg,
    boolean synchronize
)
```

删除此消息，该消息同步到当前用户的其它设备

**Parameters**:

* **msg** 需要删除的消息
* **synchronize** 是否同步到其它设备，不同步的情况下只会删除本地存储的该条消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function removeMessage

```java
inline void removeMessage(
    BMXMessage msg
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function downloadThumbnail

```java
inline void downloadThumbnail(
    BMXMessage msg,
    BMXChatService.ThumbnailStrategy strategy
)
```

下载缩略图，下载状态变化和进度通过listener通知 缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。

**Parameters**:

* **msg** 需要下载缩略图的消息
* **strategy** 缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function downloadThumbnail

```java
inline void downloadThumbnail(
    BMXMessage msg
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function downloadAttachment

```java
inline void downloadAttachment(
    BMXMessage msg
)
```

下载附件，下载状态变化和进度通过listener通知

**Parameters**:

* **msg** 需要下载附件的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function downloadAttachmentByUrl

```java
inline void downloadAttachmentByUrl(
    long msgId,
    String url,
    String path
)
```

下载附件，下载状态变化和进度通过listener通知

**Parameters**:

* **msgId** 需要下载附件的消息
* **url** 文件远程地址
* **path** 文件本地路径

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function cancelUploadAttachment

```java
inline void cancelUploadAttachment(
    BMXMessage msg
)
```

取消上传附件

**Parameters**:

* **msg** 需要取消上传附件的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function cancelDownloadAttachment

```java
inline void cancelDownloadAttachment(
    BMXMessage msg
)
```

取消上传附件

**Parameters**:

* **msg** 需要取消上传附件的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function transferingNum

```java
inline int transferingNum()
```

上传或下载中的文件数

**Return**: 文件数

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function insertMessages

```java
inline BMXErrorCode insertMessages(
    BMXMessageList list
)
```

插入消息

**Parameters**:

* **list** 插入消息列表

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function getMessage

```java
inline BMXMessage getMessage(
    long msgId
)
```

读取一条消息

**Parameters**:

* **msgId** 需要获取消息的消息id

**Return**: [BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function deleteConversation

```java
inline void deleteConversation(
    long conversationId,
    boolean synchronize
)
```

删除会话

**Parameters**:

* **conversationId** 需要删除会话的会话id
* **synchronize** 是否同步删除其它设备该会话，默认为false，仅删除本设备会话

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function deleteConversation

```java
inline void deleteConversation(
    long conversationId
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function openConversation

```java
inline BMXConversation openConversation(
    long conversationId,
    BMXConversation.Type type,
    boolean createIfNotExist
)
```

打开一个会话

**Parameters**:

* **conversationId** 需要打开的会话的会话id
* **type** 会话的类型，单聊还是群聊。
* **createIfNotExist** 会话不存在的情况下是否要创建本地会话，默认为创建

**Return**: [BMXConversation](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function openConversation

```java
inline BMXConversation openConversation(
    long conversationId,
    BMXConversation.Type type
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function attachmentDir

```java
inline String attachmentDir()
```

获取附件保存路径

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function attachmentDirForConversation

```java
inline String attachmentDirForConversation(
    long conversationId
)
```

获取会话的附件保存路径

**Parameters**:

* **conversationId** 需要获取会话附件路径的会话id

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function getAllConversations

```java
inline BMXConversationList getAllConversations()
```

获取所有会话

**Return**: BMXConversationList

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function getAllConversationsUnreadCount

```java
inline int getAllConversationsUnreadCount()
```

获取所有会话的全部未读数（标记为屏蔽的个人和群组的未读数不统计在内）

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function retrieveHistoryMessages

```java
inline BMXErrorCode retrieveHistoryMessages(
    BMXConversation conversation,
    long refMsgId,
    long size,
    BMXMessageList result
)
```

拉取历史消息

**Parameters**:

* **conversation** 需要拉取历史消息的会话
* **refMsgId** 拉取会话消息的起始消息Id
* **size** 拉取的最大消息条数
* **result** 拉取操作获取的消息列表，外部初始化传入空列表。

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function searchMessagesByKeyWords

```java
inline BMXErrorCode searchMessagesByKeyWords(
    String keywords,
    long refTime,
    long size,
    BMXMessageListList result,
    BMXConversation.Direction arg4
)
```

搜索消息

**Parameters**:

* **keywords** 搜索的关键字
* **refTime** 搜索消息的起始时间
* **size** 搜索的最大消息条数
* **result** 搜索到的消息结果列表，外部初始化传入空列表。
* **arg4** 消息搜索方向，默认（Direction::Up）是从更早的消息中搜索

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function searchMessagesByKeyWords

```java
inline BMXErrorCode searchMessagesByKeyWords(
    String keywords,
    long refTime,
    long size,
    BMXMessageListList result
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function searchMessages

```java
inline BMXErrorCode searchMessages(
    String keywords,
    long refTime,
    long size,
    BMXMessageListList result,
    BMXConversation.Direction arg4
)
```

搜索消息

**Parameters**:

* **keywords** 搜索的关键字
* **refTime** 搜索消息的起始时间
* **size** 搜索的最大消息条数
* **result** 搜索到的消息结果列表，外部初始化传入空列表。
* **arg4** 消息搜索方向，默认（Direction::Up）是从更早的消息中搜索

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function searchMessages

```java
inline BMXErrorCode searchMessages(
    String keywords,
    long refTime,
    long size,
    BMXMessageListList result
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function getGroupAckMessageUserIdList

```java
inline BMXErrorCode getGroupAckMessageUserIdList(
    BMXMessage msg,
    ListOfLongLong groupMemberIdList
)
```

获取发送的群组消息已读用户id列表

**Parameters**:

* **msg** 需要获取已读用户id列表的消息
* **groupMemberIdList** 对该条消息已读的用户id列表，初始传入为空列表

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function getGroupAckMessageUnreadUserIdList

```java
inline BMXErrorCode getGroupAckMessageUnreadUserIdList(
    BMXMessage msg,
    ListOfLongLong groupMemberIdList
)
```

获取发送的群组消息未读用户id列表

**Parameters**:

* **msg** 需要获取未读用户id列表的消息
* **groupMemberIdList** 对该条消息未读的用户id列表，初始传入为空列表

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function getGroupPlayAckMessageUserIdList

```java
inline BMXErrorCode getGroupPlayAckMessageUserIdList(
    BMXMessage msg,
    ListOfLongLong groupMemberIdList
)
```

获取发送的群组消息已播放用户id列表

**Parameters**:

* **msg** 需要获取已播放用户id列表的消息
* **groupMemberIdList** 对该条消息已播放的用户id列表，初始传入为空列表

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function getGroupUnPlayAckMessageUserIdList

```java
inline BMXErrorCode getGroupUnPlayAckMessageUserIdList(
    BMXMessage msg,
    ListOfLongLong groupMemberIdList
)
```

获取发送的群组消息未播放用户id列表

**Parameters**:

* **msg** 需要获取未播放用户id列表的消息
* **groupMemberIdList** 对该条消息未播放的用户id列表，初始传入为空列表

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function addChatListener

```java
inline void addChatListener(
    BMXChatServiceListener listener
)
```

添加聊天监听者

**Parameters**:

* **listener** 聊天监听者

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function removeChatListener

```java
inline void removeChatListener(
    BMXChatServiceListener listener
)
```

移除聊天监听者

**Parameters**:

* **listener** 聊天监听者

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function BMXChatService

```java
inline BMXChatService(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function finalize

```java
inline void finalize()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function getCPtr

```java
static inline long getCPtr(
    BMXChatService obj
)
```

## Protected Attributes Documentation

### variable swigCMemOwn

```java
transient boolean swigCMemOwn;
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```



Updated on 2022-01-26 at 17:18:31 +0800
