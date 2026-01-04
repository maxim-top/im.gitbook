---
title: im::floo::floolib::BMXChatService
summary: 聊天Service 

---

# im::floo::floolib::BMXChatService



聊天Service 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-delete)**() |
| void | **[sendMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-sendmessage)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>发送消息，消息状态变化会通过listener通知  |
| void | **[resendMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-resendmessage)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>重新发送消息，消息状态变化会通过listener通知  |
| void | **[recallMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-recallmessage)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>撤回消息，消息状态变化会通过listener通知  |
| [BMXErrorCode] | **[forwardMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-forwardmessage)**(BMXMessageList list, [BMXConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md) to, [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) newMsg)<br>合并转发消息  |
| void | **[forwardMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-forwardmessage)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>简单转发消息，用户应当通过BMXMessage::createForwardMessage()先创建转发消息  |
| void | **[ackMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-ackmessage)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>发送已读回执  |
| void | **[ackMessageDelivered](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-ackmessagedelivered)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>发送送达回执  |
| void | **[ackPlayMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-ackplaymessage)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>发送已播放回执  |
| void | **[readCancel](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-readcancel)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>标记此消息为未读，该消息同步到当前用户的所有设备  |
| void | **[readAllMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-readallmessage)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>标记此消息及之前全部消息为已读，该消息同步到当前用户的所有设备  |
| void | **[removeMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-removemessage)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, boolean synchronize)<br>删除此消息，该消息同步到当前用户的其它设备  |
| void | **[removeMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-removemessage)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg) |
| void | **[downloadThumbnail](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-downloadthumbnail)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, BMXChatService.ThumbnailStrategy strategy)<br>下载缩略图，下载状态变化和进度通过listener通知 缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。  |
| void | **[downloadThumbnail](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-downloadthumbnail)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg) |
| void | **[downloadAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-downloadattachment)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>下载附件，下载状态变化和进度通过listener通知  |
| void | **[downloadAttachmentByUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-downloadattachmentbyurl)**(long msgId, String url, String path)<br>下载附件，下载状态变化和进度通过listener通知  |
| void | **[cancelUploadAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-canceluploadattachment)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>取消上传附件  |
| void | **[cancelDownloadAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-canceldownloadattachment)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>取消上传附件  |
| int | **[transferingNum](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-transferingnum)**()<br>上传或下载中的文件数  |
| [BMXErrorCode] | **[insertMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-insertmessages)**(BMXMessageList list)<br>插入消息  |
| [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) | **[getMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getmessage)**(long msgId)<br>读取一条消息  |
| void | **[deleteConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-deleteconversation)**(long conversationId, boolean synchronize)<br>删除会话  |
| void | **[deleteConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-deleteconversation)**(long conversationId) |
| [BMXConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md) | **[openConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-openconversation)**(long conversationId, BMXConversation.Type type, boolean createIfNotExist)<br>打开一个会话  |
| [BMXConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md) | **[openConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-openconversation)**(long conversationId, BMXConversation.Type type) |
| String | **[attachmentDir](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-attachmentdir)**()<br>获取附件保存路径  |
| String | **[attachmentDirForConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-attachmentdirforconversation)**(long conversationId)<br>获取会话的附件保存路径  |
| BMXConversationList | **[getAllConversations](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getallconversations)**()<br>获取所有会话  |
| int | **[getAllConversationsUnreadCount](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getallconversationsunreadcount)**()<br>获取所有会话的全部未读数（标记为屏蔽的个人和群组的未读数不统计在内）  |
| [BMXErrorCode] | **[retrieveHistoryMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-retrievehistorymessages)**([BMXConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md) conversation, long refMsgId, long size, BMXMessageList result)<br>拉取历史消息  |
| [BMXErrorCode] | **[searchMessagesByKeyWords](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-searchmessagesbykeywords)**(String keywords, long refTime, long size, BMXMessageListList result, BMXConversation.Direction arg4)<br>搜索消息  |
| [BMXErrorCode] | **[searchMessagesByKeyWords](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-searchmessagesbykeywords)**(String keywords, long refTime, long size, BMXMessageListList result) |
| [BMXErrorCode] | **[searchMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-searchmessages)**(String keywords, long refTime, long size, BMXMessageListList result, BMXConversation.Direction arg4)<br>搜索消息  |
| [BMXErrorCode] | **[searchMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-searchmessages)**(String keywords, long refTime, long size, BMXMessageListList result) |
| [BMXErrorCode] | **[getGroupAckMessageUserIdList](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getgroupackmessageuseridlist)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, ListOfLongLong groupMemberIdList)<br>获取发送的群组消息已读用户id列表  |
| [BMXErrorCode] | **[getGroupAckMessageUnreadUserIdList](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getgroupackmessageunreaduseridlist)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, ListOfLongLong groupMemberIdList)<br>获取发送的群组消息未读用户id列表  |
| [BMXErrorCode] | **[getGroupPlayAckMessageUserIdList](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getgroupplayackmessageuseridlist)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, ListOfLongLong groupMemberIdList)<br>获取发送的群组消息已播放用户id列表  |
| [BMXErrorCode] | **[getGroupUnPlayAckMessageUserIdList](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getgroupunplayackmessageuseridlist)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, ListOfLongLong groupMemberIdList)<br>获取发送的群组消息未播放用户id列表  |
| void | **[addChatListener](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-addchatlistener)**([BMXChatServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md) listener)<br>添加聊天监听者  |
| void | **[removeChatListener](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-removechatlistener)**([BMXChatServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md) listener)<br>移除聊天监听者  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXChatService](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-bmxchatservice)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getcptr)**([BMXChatService](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md) obj) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| transient boolean | **[swigCMemOwn](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#variable-swigcmemown)**  |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="delete" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="sendMessage" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="resendMessage" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="recallMessage" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="forwardMessage" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="forwardMessage" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="ackMessage" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="ackMessageDelivered" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="ackPlayMessage" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="readCancel" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="readAllMessage" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="removeMessage" %}{% endlanying_code_snippet %}
```
### function removeMessage

```java
inline void removeMessage(
    BMXMessage msg
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="removeMessage" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="downloadThumbnail" %}{% endlanying_code_snippet %}
```
### function downloadThumbnail

```java
inline void downloadThumbnail(
    BMXMessage msg
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="downloadThumbnail" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="downloadAttachment" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="downloadAttachmentByUrl" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="cancelUploadAttachment" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="cancelDownloadAttachment" %}{% endlanying_code_snippet %}
```
### function transferingNum

```java
inline int transferingNum()
```

上传或下载中的文件数 

**Return**: 文件数 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="transferingNum" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="insertMessages" %}{% endlanying_code_snippet %}
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


**Return**: [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md)

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="getMessage" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="deleteConversation" %}{% endlanying_code_snippet %}
```
### function deleteConversation

```java
inline void deleteConversation(
    long conversationId
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="deleteConversation" %}{% endlanying_code_snippet %}
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


**Return**: [BMXConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md)

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="openConversation" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="openConversation" %}{% endlanying_code_snippet %}
```
### function attachmentDir

```java
inline String attachmentDir()
```

获取附件保存路径 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="attachmentDir" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="attachmentDirForConversation" %}{% endlanying_code_snippet %}
```
### function getAllConversations

```java
inline BMXConversationList getAllConversations()
```

获取所有会话 

**Return**: BMXConversationList 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="getAllConversations" %}{% endlanying_code_snippet %}
```
### function getAllConversationsUnreadCount

```java
inline int getAllConversationsUnreadCount()
```

获取所有会话的全部未读数（标记为屏蔽的个人和群组的未读数不统计在内） 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="getAllConversationsUnreadCount" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="retrieveHistoryMessages" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="searchMessagesByKeyWords" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="searchMessagesByKeyWords" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="searchMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="searchMessages" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="getGroupAckMessageUserIdList" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="getGroupAckMessageUnreadUserIdList" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="getGroupPlayAckMessageUserIdList" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="getGroupUnPlayAckMessageUserIdList" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="addChatListener" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="removeChatListener" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="BMXChatService" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="finalize" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatService",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800