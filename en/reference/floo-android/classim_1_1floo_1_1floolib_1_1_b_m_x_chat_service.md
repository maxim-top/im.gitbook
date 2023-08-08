---
title: im::floo::floolib::BMXChatService
summary: Chat Service
---

# im::floo::floolib::BMXChatService

Chat Service

## Public Functions

|                                                                                   | Name                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void                                                                 | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md#function-delete)()                                                                                                                                                                                                                                                                                                                                                                   |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-sendmessage"><strong>sendMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Send a message, and the message status change is notified via listener</p>                                                                                                                                                                               |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-resendmessage"><strong>resendMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Resend this message, and the message status change is notified via listener</p>                                                                                                                                                                      |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-recallmessage"><strong>recallMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Recall a message, and the message status change is notified via listener</p>                                                                                                                                                                         |
| \[BMXErrorCode]                                                                   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-forwardmessage"><strong>forwardMessage</strong></a>(BMXMessageList list, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md">BMXConversation</a> to, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> newMsg)<br>Merge and forward messages</p>                                                                                                      |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-forwardmessage"><strong>forwardMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Simple forwarding messages, users should create forwarding messages first through BMXMessage:: createForwardMessage ()</p>                                                                                                                         |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-ackmessage"><strong>ackMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Send read acknowledgement</p>                                                                                                                                                                                                                              |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-ackmessagedelivered"><strong>ackMessageDelivered</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Send delivery acknowledgement</p>                                                                                                                                                                                                        |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-ackplaymessage"><strong>ackPlayMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Send a playback acknowledgement</p>                                                                                                                                                                                                                |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-readcancel"><strong>readCancel</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Mark this message as unread and synchronize to all devices of the current user</p>                                                                                                                                                                         |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-readallmessage"><strong>readAllMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Mark this message and all previous messages as read, and synchronize to all current users' devices</p>                                                                                                                                             |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-removemessage"><strong>removeMessage</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, boolean synchronize)<br>Delete this message, which synchronizes to other devices of the current user</p>                                                                                                                                                |
| void                                                                              | [**removeMessage**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md#function-removemessage)([BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md) msg)                                                                                                                                                                                                                                                                          |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-downloadthumbnail"><strong>downloadThumbnail</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, BMXChatService.ThumbnailStrategy strategy)<br>Download thumbnail, downloading state changes and progress notified via listener. Thumbnail generation policy: 1 - generated by third-party server, 2 - generated by local server, default 1.</p> |
| void                                                                              | [**downloadThumbnail**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md#function-downloadthumbnail)([BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md) msg)                                                                                                                                                                                                                                                                  |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-downloadattachment"><strong>downloadAttachment</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Downloaded attachments, and download state changes and progress are notified via listener</p>                                                                                                                                              |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-downloadattachmentbyurl"><strong>downloadAttachmentByUrl</strong></a>(long msgId, String url, String path)<br>Downloaded attachments, and download state changes and progress are notified via listener</p>                                                                                                                                                                             |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-canceluploadattachment"><strong>cancelUploadAttachment</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Cancel uploading attachment</p>                                                                                                                                                                                                    |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-canceldownloadattachment"><strong>cancelDownloadAttachment</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Cancel uploading attachment</p>                                                                                                                                                                                                |
| int                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-transferingnum"><strong>transferingNum</strong></a>()<br>Number of uploading/downloading files</p>                                                                                                                                                                                                                                                                                      |
| \[BMXErrorCode]                                                                   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-insertmessages"><strong>insertMessages</strong></a>(BMXMessageList list)<br>Insert a message</p>                                                                                                                                                                                                                                                                                        |
| [BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md)           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getmessage"><strong>getMessage</strong></a>(long msgId)<br>Read a message</p>                                                                                                                                                                                                                                                                                                           |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-deleteconversation"><strong>deleteConversation</strong></a>(long conversationId, boolean synchronize)<br>Delete a conversation</p>                                                                                                                                                                                                                                                      |
| void                                                                              | [**deleteConversation**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md#function-deleteconversation)(long conversationId)                                                                                                                                                                                                                                                                                                                        |
| [BMXConversation](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md) | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-openconversation"><strong>openConversation</strong></a>(long conversationId, BMXConversation.Type type, boolean createIfNotExist)<br>Launch a conversation</p>                                                                                                                                                                                                                          |
| [BMXConversation](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md) | [**openConversation**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md#function-openconversation)(long conversationId, BMXConversation.Type type)                                                                                                                                                                                                                                                                                                 |
| String                                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-attachmentdir"><strong>attachmentDir</strong></a>()<br>Get attachment saving path</p>                                                                                                                                                                                                                                                                                                   |
| String                                                                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-attachmentdirforconversation"><strong>attachmentDirForConversation</strong></a>(long conversationId)<br>Get attachment saving path for a conversation</p>                                                                                                                                                                                                                               |
| BMXConversationList                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getallconversations"><strong>getAllConversations</strong></a>()<br>Get all conversations</p>                                                                                                                                                                                                                                                                                            |
| int                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getallconversationsunreadcount"><strong>getAllConversationsUnreadCount</strong></a>()<br>Get number of unread messages for all conversations (unreads for individuals and groups marked as blocked is not counted)</p>                                                                                                                                                                  |
| \[BMXErrorCode]                                                                   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-retrievehistorymessages"><strong>retrieveHistoryMessages</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md">BMXConversation</a> conversation, long refMsgId, long size, BMXMessageList result)<br>Pull message history</p>                                                                                                                                     |
| \[BMXErrorCode]                                                                   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-searchmessagesbykeywords"><strong>searchMessagesByKeyWords</strong></a>(String keywords, long refTime, long size, BMXMessageListList result, BMXConversation.Direction arg4)<br>Search for messages</p>                                                                                                                                                                                 |
| \[BMXErrorCode]                                                                   | [**searchMessagesByKeyWords**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md#function-searchmessagesbykeywords)(String keywords, long refTime, long size, BMXMessageListList result)                                                                                                                                                                                                                                                            |
| \[BMXErrorCode]                                                                   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-searchmessages"><strong>searchMessages</strong></a>(String keywords, long refTime, long size, BMXMessageListList result, BMXConversation.Direction arg4)<br>Search for messages</p>                                                                                                                                                                                                     |
| \[BMXErrorCode]                                                                   | [**searchMessages**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md#function-searchmessages)(String keywords, long refTime, long size, BMXMessageListList result)                                                                                                                                                                                                                                                                                |
| \[BMXErrorCode]                                                                   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getgroupackmessageuseridlist"><strong>getGroupAckMessageUserIdList</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, ListOfLongLong groupMemberIdList)<br>Get the list of user-ids that have read group messages</p>                                                                                                                           |
| \[BMXErrorCode]                                                                   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getgroupackmessageunreaduseridlist"><strong>getGroupAckMessageUnreadUserIdList</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, ListOfLongLong groupMemberIdList)<br>Get a list of unread user ids for the sent group message</p>                                                                                                             |
| \[BMXErrorCode]                                                                   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getgroupplayackmessageuseridlist"><strong>getGroupPlayAckMessageUserIdList</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, ListOfLongLong groupMemberIdList)<br>Get a list of playback user ids for the sent group message</p>                                                                                                               |
| \[BMXErrorCode]                                                                   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-getgroupunplayackmessageuseridlist"><strong>getGroupUnPlayAckMessageUserIdList</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, ListOfLongLong groupMemberIdList)<br>Get a list of unplayed user ids for the sent group message</p>                                                                                                           |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-addchatlistener"><strong>addChatListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md">BMXChatServiceListener</a> listener)<br>Add chat listener</p>                                                                                                                                                                                             |
| void                                                                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md#function-removechatlistener"><strong>removeChatListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md">BMXChatServiceListener</a> listener)<br>Remove chat listener</p>                                                                                                                                                                                    |

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

Send a message, and the message status change is notified via listener

**Parameters**:

* **msg** Message to be sent

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

Resend this message, and the message status change is notified via listener

**Parameters**:

* **msg** Resent message

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

Recall a message, and the message status change is notified via listener

**Parameters**:

* **msg** Recalled message

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

Merge and forward messages

**Parameters**:

* **list** List of messages to be forwarded
* **to** The conversation to which message is forwarded
* **newMsg** The newly generated single forwarded message from the merging list of messages to be forwarded

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

Simple forwarding messages, users should create forwarding messages first through BMXMessage:: createForwardMessage ()

**Parameters**:

* **msg** Messages to be forwarded

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

Send read acknowledgement

**Parameters**:

* **msg** Message requiring a read acknowledgement to be sent

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

Send delivery acknowledgement

**Parameters**:

* **msg** Message that need to send a delivery acknowledgement

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

Send a playback acknowledgement

**Parameters**:

* **msg** Messages that require to send a playback acknowledgement

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

Mark this message as unread and synchronize to all devices of the current user

**Parameters**:

* **msg** The message needs to send “read recalled”

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

Mark this message and all previous messages as read, and synchronize to all current users' devices

**Parameters**:

* **msg** The message for which all earlier messages need to be marked as read

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

Delete this message, which synchronizes to other devices of the current user

**Parameters**:

* **msg** Message to be deleted
* **synchronize** Whether to synchronize to other devices, otherwise only the locally stored message will be deleted

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

Download thumbnail, downloading state changes and progress notified via listener. Thumbnail generation policy: 1 - generated by third-party server, 2 - generated by local server, default 1.

**Parameters**:

* **msg** Message requiring to download thumbnail
* **strategy** Thumbnail generation policy, 1 - generated by third-party server, 2 - Generated by local server, default 1.

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

Downloaded attachments, and download state changes and progress are notified via listener

**Parameters**:

* **msg** Message requiring to download attachment

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

Downloaded attachments, and download state changes and progress are notified via listener

**Parameters**:

* **msgId** Message requiring to download attachment
* **url** File remote address
* **path** File local address

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

Cancel uploading attachment

**Parameters**:

* **msg** Message requiring to cancel attachment uploading

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

Cancel uploading attachment

**Parameters**:

* **msg** Message requiring to cancel attachment uploading

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function transferingNum

```java
inline int transferingNum()
```

Number of uploading/downloading files

**Return**: Number of files

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

Insert a message

**Parameters**:

* **list** Insert message list

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

Read a message

**Parameters**:

* **msgId** id of the message which needs to be fetched

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

Delete a conversation

**Parameters**:

* **conversationId** Conversation id requiring to delete conversation
* **synchronize** Whether to delete the conversation on other devices synchronously, default false, means only delete the conversation on the current device

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

Launch a conversation

**Parameters**:

* **conversationId** id of the conversation which needs to be opened
* **type** Conversation type, single/group chat.
* **createIfNotExist** Whether to create a local conversation if no conversation existing, default to create

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

Get attachment saving path

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

Get attachment saving path for a conversation

**Parameters**:

* **conversationId** Conversation id requiring a conversation attachment path

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function getAllConversations

```java
inline BMXConversationList getAllConversations()
```

Get all conversations

**Return**: BMXConversationList

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatService'></div>
```

### function getAllConversationsUnreadCount

```java
inline int getAllConversationsUnreadCount()
```

Get number of unread messages for all conversations (unreads for individuals and groups marked as blocked is not counted)

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

Pull message history

**Parameters**:

* **conversation** Conversation for which message history needs to pull
* **refMsgId** Start message Id for pulling conversation messages
* **size** Maximum number of messages to pull
* **result** List of messages fetched by pull operation, externally initializing an incoming empty list.

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

Search for messages

**Parameters**:

* **keywords** Keyword for search
* **refTime** Start time of message search
* **size** Maximum number of messages to search
* **result** List of searched message results, externally initializing an incoming empty list.
* **arg4** Message search direction, default (Direction::Up)means search from earlier messages.

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

Search for messages

**Parameters**:

* **keywords** Keyword for search
* **refTime** Start time of message search
* **size** Maximum number of messages to search
* **result** List of searched message results, externally initializing an incoming empty list.
* **arg4** Message search direction, default (Direction::Up)means search from earlier messages.

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

Get the list of user-ids that have read group messages

**Parameters**:

* **msg** Message requiring to get list of read user ids
* **groupMemberIdList** List of read user ids for this message, initially passed in as an empty list

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

Get a list of unread user ids for the sent group message

**Parameters**:

* **msg** Message requiring to get list of unread user ids
* **groupMemberIdList** List of unread user ids for this message, initially passed in as an empty list

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

Get a list of playback user ids for the sent group message

**Parameters**:

* **msg** Message requiring to get list of played user ids
* **groupMemberIdList** List of played user ids for this message, initially passed in as an empty list

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

Get a list of unplayed user ids for the sent group message

**Parameters**:

* **msg** Message requiring to get list of unplayed user ids
* **groupMemberIdList** List of unplayed user ids for this message, initially passed in as an empty list

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

Add chat listener

**Parameters**:

* **listener** Chat listener

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

Remove chat listener

**Parameters**:

* **listener** Chat listener

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
