---
title: floo::BMXChatService
summary: Chat Service
---

# floo::BMXChatService

Chat Service

`#include <bmx_chat_service.h>`

## Public Types

|            | Name                                                                                                                                                                                                |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class | <p><a href="classfloo_1_1_b_m_x_chat_service.md#enum-thumbnailstrategy"><strong>ThumbnailStrategy</strong></a> { ThirdpartyServerCreate = 1, LocalServerCreate}<br>Thumbnail generation policy,</p> |

## Public Functions

|                             | Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual                     | [**\~BMXChatService**](classfloo\_1\_1\_b\_m\_x\_chat\_service.md#function-\~bmxchatservice)()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-sendmessage"><strong>sendMessage</strong></a>(BMXMessagePtr msg) =0<br>Send a message, and the message status change is notified via listener</p>                                                                                                                                                                                                                                                                                                                                                                       |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-resendmessage"><strong>resendMessage</strong></a>(BMXMessagePtr msg) =0<br>Resend this message, and the message status change is notified via listener</p>                                                                                                                                                                                                                                                                                                                                                              |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-recallmessage"><strong>recallMessage</strong></a>(BMXMessagePtr msg) =0<br>Recall a message, and the message status change is notified via listener</p>                                                                                                                                                                                                                                                                                                                                                                 |
| virtual BMXErrorCode        | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-forwardmessage"><strong>forwardMessage</strong></a>(const BMXMessageList &#x26; list, BMXConversationPtr to, BMXMessagePtr &#x26; newMsg) =0<br>Merge and forward messages</p>                                                                                                                                                                                                                                                                                                                                          |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-forwardmessage"><strong>forwardMessage</strong></a>(BMXMessagePtr msg) =0<br>Simple forwarding messages, users should create forwarding messages first through BMXMessage:: createForwardMessage ()</p>                                                                                                                                                                                                                                                                                                                 |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-ackmessage"><strong>ackMessage</strong></a>(BMXMessagePtr msg) =0<br>Send read acknowledgement</p>                                                                                                                                                                                                                                                                                                                                                                                                                      |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-ackmessagedelivered"><strong>ackMessageDelivered</strong></a>(BMXMessagePtr msg) =0<br>Send delivery acknowledgement</p>                                                                                                                                                                                                                                                                                                                                                                                                |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-ackplaymessage"><strong>ackPlayMessage</strong></a>(BMXMessagePtr msg) =0<br>Send an audio/video message playback acknowledgement</p>                                                                                                                                                                                                                                                                                                                                                                                   |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-readcancel"><strong>readCancel</strong></a>(BMXMessagePtr msg) =0<br>Mark this message as unread and synchronize to all devices of the current user</p>                                                                                                                                                                                                                                                                                                                                                                 |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-readallmessage"><strong>readAllMessage</strong></a>(BMXMessagePtr msg) =0<br>Mark this message and all previous messages as read, and synchronize to all current users' devices</p>                                                                                                                                                                                                                                                                                                                                     |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-removemessage"><strong>removeMessage</strong></a>(BMXMessagePtr msg, bool synchronize =true) =0<br>Delete this message, which synchronizes to other devices of the current user</p>                                                                                                                                                                                                                                                                                                                                     |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-downloadthumbnail"><strong>downloadThumbnail</strong></a>(BMXMessagePtr msg, <a href="classfloo_1_1_b_m_x_chat_service.md#enum-thumbnailstrategy">ThumbnailStrategy</a> strategy =<a href="classfloo_1_1_b_m_x_chat_service.md#enumvalue-thirdpartyservercreate">ThumbnailStrategy::ThirdpartyServerCreate</a>) =0<br>Download thumbnail, downloading state changes and progress notified via listener. Thumbnail generation policy: 1 - generated by third-party server, 2 - generated by local server, default 1.</p> |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-downloadattachment"><strong>downloadAttachment</strong></a>(BMXMessagePtr msg) =0<br>Downloaded attachments, and download state changes and progress are notified via listener</p>                                                                                                                                                                                                                                                                                                                                      |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-downloadattachmentbyurl"><strong>downloadAttachmentByUrl</strong></a>(int64_t msgId, const std::string &#x26; url, const std::string &#x26; path) =0<br>Downloaded attachments, and download state changes and progress are notified via listener</p>                                                                                                                                                                                                                                                                   |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-canceluploadattachment"><strong>cancelUploadAttachment</strong></a>(BMXMessagePtr msg) =0<br>Cancel uploading attachment</p>                                                                                                                                                                                                                                                                                                                                                                                            |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-canceldownloadattachment"><strong>cancelDownloadAttachment</strong></a>(BMXMessagePtr msg) =0<br>Cancel attachment downloading</p>                                                                                                                                                                                                                                                                                                                                                                                      |
| virtual int                 | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-transferingnum"><strong>transferingNum</strong></a>() =0<br>Number of uploading/downloading files</p>                                                                                                                                                                                                                                                                                                                                                                                                                   |
| virtual BMXErrorCode        | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-insertmessages"><strong>insertMessages</strong></a>(const BMXMessageList &#x26; list) =0<br>Insert a message</p>                                                                                                                                                                                                                                                                                                                                                                                                        |
| virtual BMXMessagePtr       | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-getmessage"><strong>getMessage</strong></a>(int64_t msgId) =0<br>Read a message</p>                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-deleteconversation"><strong>deleteConversation</strong></a>(int64_t conversationId, bool synchronize =false) =0<br>Delete a conversation</p>                                                                                                                                                                                                                                                                                                                                                                            |
| virtual BMXConversationPtr  | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-openconversation"><strong>openConversation</strong></a>(int64_t conversationId, <a href="classfloo_1_1_b_m_x_conversation.md#enum-type">BMXConversation::Type</a> type, bool createIfNotExist =true) =0<br>Launch a conversation</p>                                                                                                                                                                                                                                                                                    |
| virtual std::string         | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-attachmentdir"><strong>attachmentDir</strong></a>() =0<br>Get attachment saving path</p>                                                                                                                                                                                                                                                                                                                                                                                                                                |
| virtual std::string         | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-attachmentdirforconversation"><strong>attachmentDirForConversation</strong></a>(int64_t conversationId) =0<br>Get attachment saving path for a conversation</p>                                                                                                                                                                                                                                                                                                                                                         |
| virtual BMXConversationList | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-getallconversations"><strong>getAllConversations</strong></a>() =0<br>Get all conversations</p>                                                                                                                                                                                                                                                                                                                                                                                                                         |
| virtual int                 | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-getallconversationsunreadcount"><strong>getAllConversationsUnreadCount</strong></a>() =0<br>Get number of unread messages for all conversations (unreads for individuals and groups marked as blocked is not counted)</p>                                                                                                                                                                                                                                                                                               |
| virtual BMXErrorCode        | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-retrievehistorymessages"><strong>retrieveHistoryMessages</strong></a>(BMXConversationPtr conversation, int64_t refMsgId, size_t size, BMXMessageList &#x26; result) =0<br>Pull message history</p>                                                                                                                                                                                                                                                                                                                      |
| virtual BMXErrorCode        | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-searchmessagesbykeywords"><strong>searchMessagesByKeyWords</strong></a>(const std::string &#x26; keywords, int64_t refTime, size_t size, std::vector&#x3C; BMXMessageList > &#x26; result, <a href="classfloo_1_1_b_m_x_conversation.md#enum-direction">BMXConversation::Direction</a> =<a href="classfloo_1_1_b_m_x_conversation.md#enumvalue-up">BMXConversation::Direction::Up</a>) =0<br>Search for messages by keyword</p>                                                                                         |
| virtual BMXErrorCode        | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-searchmessages"><strong>searchMessages</strong></a>(const std::string &#x26; keywords, int64_t refTime, size_t size, std::vector&#x3C; BMXMessageList > &#x26; result, <a href="classfloo_1_1_b_m_x_conversation.md#enum-direction">BMXConversation::Direction</a> =<a href="classfloo_1_1_b_m_x_conversation.md#enumvalue-up">BMXConversation::Direction::Up</a>) =0<br>Deprecated.</p>                                                                                                                                |
| virtual BMXErrorCode        | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-getgroupackmessageuseridlist"><strong>getGroupAckMessageUserIdList</strong></a>(BMXMessagePtr msg, std::vector&#x3C; int64_t > &#x26; groupMemberIdList) =0<br>Get the list of user-ids that have read group messages</p>                                                                                                                                                                                                                                                                                               |
| virtual BMXErrorCode        | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-getgroupackmessageunreaduseridlist"><strong>getGroupAckMessageUnreadUserIdList</strong></a>(BMXMessagePtr msg, std::vector&#x3C; int64_t > &#x26; groupMemberIdList) =0<br>Get a list of unread user ids for the sent group message</p>                                                                                                                                                                                                                                                                                 |
| virtual BMXErrorCode        | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-getgroupplayackmessageuseridlist"><strong>getGroupPlayAckMessageUserIdList</strong></a>(BMXMessagePtr msg, std::vector&#x3C; int64_t > &#x26; groupMemberIdList) =0<br>Get the user id list for sent group audio/video messages played (for audio/video messages only)</p>                                                                                                                                                                                                                                              |
| virtual BMXErrorCode        | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-getgroupunplayackmessageuseridlist"><strong>getGroupUnPlayAckMessageUserIdList</strong></a>(BMXMessagePtr msg, std::vector&#x3C; int64_t > &#x26; groupMemberIdList) =0<br>Get the user id list for sent group audio/video messages unplayed (for audio/video messages only)</p>                                                                                                                                                                                                                                        |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-addchatlistener"><strong>addChatListener</strong></a>(<a href="classfloo_1_1_b_m_x_chat_service_listener.md">BMXChatServiceListener</a> * listener) =0<br>Add chat listener</p>                                                                                                                                                                                                                                                                                                                                         |
| virtual void                | <p><a href="classfloo_1_1_b_m_x_chat_service.md#function-removechatlistener"><strong>removeChatListener</strong></a>(<a href="classfloo_1_1_b_m_x_chat_service_listener.md">BMXChatServiceListener</a> * listener) =0<br>Remove chat listener</p>                                                                                                                                                                                                                                                                                                                                |

## Protected Functions

|      | Name                                                                                                                          |
| ---- | ----------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXChatService**](classfloo\_1\_1\_b\_m\_x\_chat\_service.md#function-bmxchatservice)()                                    |
| void | [**updateMessageId**](classfloo\_1\_1\_b\_m\_x\_chat\_service.md#function-updatemessageid)(BMXMessagePtr msg, int64\_t newId) |

## Public Types Documentation

### enum ThumbnailStrategy

| Enumerator             | Value | Description                     |
| ---------------------- | ----- | ------------------------------- |
| ThirdpartyServerCreate | 1     | Generated by third-party server |
| LocalServerCreate      |       | Generated by local server       |

Thumbnail generation policy,

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

Send a message, and the message status change is notified via listener

**Parameters**:

* **msg** Message to be sent

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

Resend this message, and the message status change is notified via listener

**Parameters**:

* **msg** Resent message

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

Recall a message, and the message status change is notified via listener

**Parameters**:

* **msg** Recalled message

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

Merge and forward messages

**Parameters**:

* **list** List of messages to be forwarded
* **to** The conversation to which message is forwarded
* **newMsg** The newly generated single forwarded message from the merging list of messages to be forwarded

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

Simple forwarding messages, users should create forwarding messages first through BMXMessage:: createForwardMessage ()

**Parameters**:

* **msg** Messages to be forwarded

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

Send read acknowledgement

**Parameters**:

* **msg** Message requiring a read acknowledgement to be sent

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

Send delivery acknowledgement

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

Send an audio/video message playback acknowledgement

**Parameters**:

* **msg** Message requiring a read acknowledgement to be sent

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

Mark this message as unread and synchronize to all devices of the current user

**Parameters**:

* **msg** The message needs to send “read recalled”

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

Mark this message and all previous messages as read, and synchronize to all current users' devices

**Parameters**:

* **msg** The message for which all earlier messages need to be marked as read

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

Delete this message, which synchronizes to other devices of the current user

**Parameters**:

* **msg** Message to be deleted
* **synchronize** Whether to synchronize to other devices, otherwise only the locally stored message will be deleted

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

Download thumbnail, downloading state changes and progress notified via listener. Thumbnail generation policy: 1 - generated by third-party server, 2 - generated by local server, default 1.

**Parameters**:

* **msg** Message requiring to download thumbnail
* **strategy** Thumbnail generation policy, 1 - generated by third-party server, 2 - Generated by local server, default 1.

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

Downloaded attachments, and download state changes and progress are notified via listener

**Parameters**:

* **msg** Message requiring to download attachment

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

Downloaded attachments, and download state changes and progress are notified via listener

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

Cancel uploading attachment

**Parameters**:

* **msg** Message requiring to cancel attachment uploading

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

Cancel attachment downloading

**Parameters**:

* **msg** Message requiring to cancel attachment downloading

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function transferingNum

```cpp
virtual int transferingNum() =0
```

Number of uploading/downloading files

**Return**: Number of files

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

Insert a message

**Parameters**:

* **list** Insert message list

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

Read a message

**Parameters**:

* **msgId** id of the message which needs to be fetched

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

Delete a conversation

**Parameters**:

* **conversationId** Conversation id requiring to delete conversation
* **synchronize** Whether to delete the conversation on other devices synchronously, default false, means only delete the conversation on the current device

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

Launch a conversation

**Parameters**:

* **conversationId** id of the conversation which needs to be opened
* **type** Conversation type, single/group chat.
* **createIfNotExist** Whether to create a local conversation if no conversation existing, default to create

**Return**: BMXConversationPtr

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function attachmentDir

```cpp
virtual std::string attachmentDir() =0
```

Get attachment saving path

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

Get attachment saving path for a conversation

**Parameters**:

* **conversationId** Conversation id requiring a conversation attachment path

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function getAllConversations

```cpp
virtual BMXConversationList getAllConversations() =0
```

Get all conversations

**Return**: BMXConversationList

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatService'></div>
```

### function getAllConversationsUnreadCount

```cpp
virtual int getAllConversationsUnreadCount() =0
```

Get number of unread messages for all conversations (unreads for individuals and groups marked as blocked is not counted)

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

Pull message history

**Parameters**:

* **conversation** Conversation for which message history needs to pull
* **refMsgId** Start message Id for pulling conversation messages
* **size** Maximum number of messages to pull
* **result** List of messages fetched by pull operation, externally initializing an incoming empty list.

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

Search for messages by keyword

**Parameters**:

* **keywords** Keyword for search
* **refTime** Start time of message search
* **size** Maximum number of messages to search
* **result** List of searched message results, externally initializing an incoming empty list.
* **Direction** Message search direction, default (Direction::Up)means search from earlier messages.

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

* **keywords** Keyword for search
* **refTime** Start time of message search
* **size** Maximum number of messages to search
* **result** List of searched message results, externally initializing an incoming empty list.
* **Direction** Message search direction, default (Direction::Up)means search from earlier messages.

**Return**: BMXErrorCode

use searchMessagesByKeyWords instead.

Search for messages

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

Get the list of user-ids that have read group messages

**Parameters**:

* **msg** Message requiring to get list of read user ids
* **groupMemberIdList** List of read user ids for this message, initially passed in as an empty list

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

Get a list of unread user ids for the sent group message

**Parameters**:

* **msg** Message requiring to get list of unread user ids
* **groupMemberIdList** List of unread user ids for this message, initially passed in as an empty list

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

Get the user id list for sent group audio/video messages played (for audio/video messages only)

**Parameters**:

* **msg** Message requiring to get list of played user ids
* **groupMemberIdList** List of played user ids for this message, initially passed in as an empty list

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

Get the user id list for sent group audio/video messages unplayed (for audio/video messages only)

**Parameters**:

* **msg** Message requiring to get list of unplayed user ids
* **groupMemberIdList** List of unplayed user ids for this message, initially passed in as an empty list

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

Add chat listener

**Parameters**:

* **listener** Chat listener

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

Remove chat listener

**Parameters**:

* **listener** Chat listener

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
