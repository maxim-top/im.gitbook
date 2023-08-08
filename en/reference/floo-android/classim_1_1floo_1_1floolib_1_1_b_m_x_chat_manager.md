---
title: im::floo::floolib::BMXChatManager
summary: Chat manager
---

# im::floo::floolib::BMXChatManager

Chat manager

## Public Functions

|      | Name                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXChatManager**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_manager.md#function-bmxchatmanager)([BMXChatService](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_service.md) service)                                                                                                                                                                                                                     |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-sendmessage"><strong>sendMessage</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Send a message, and the message status change is notified via listener</p>                                                                                                                                    |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-resendmessage"><strong>resendMessage</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Resend this message, and the message status change is notified via listener</p>                                                                                                                           |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-recallmessage"><strong>recallMessage</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Recall a message, and the message status change is notified via listener</p>                                                                                                                              |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-forwardmessage"><strong>forwardMessage</strong></a>(final BMXMessageList list, final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md">BMXConversation</a> to, final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> newMsg, final BMXCallBack callBack)<br>Merge and forward messages</p>                   |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-forwardmessage"><strong>forwardMessage</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Simple forwarding messages, users should create forwarding messages first through BMXMessage:: createForwardMessage ()</p>                                                                              |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-readallmessage"><strong>readAllMessage</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Mark this message and all previous messages as read, and synchronize to all current users' devices</p>                                                                                                  |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-removemessage"><strong>removeMessage</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, final boolean synchronize)<br>Delete this message, which synchronizes to other devices of the current user</p>                                                                                               |
| void | [**removeMessage**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_manager.md#function-removemessage)(final [BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md) msg)                                                                                                                                                                                                                               |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-ackmessage"><strong>ackMessage</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Send read acknowledgement</p>                                                                                                                                                                                   |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-readcancel"><strong>readCancel</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Set unread</p>                                                                                                                                                                                                  |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-downloadthumbnail"><strong>downloadThumbnail</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Download thumbnail, downloading state changes and progress notified via listener. Thumbnail generation policy: 1 - generated by third-party server, 2 - generated by local server, default 1.</p> |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-downloadattachment"><strong>downloadAttachment</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Downloaded attachments, and download state changes and progress are notified via listener</p>                                                                                                   |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-canceldownloadattachment"><strong>cancelDownloadAttachment</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Cancel attachment downloading</p>                                                                                                                                                   |
| int  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-transferingnum"><strong>transferingNum</strong></a>()<br>Number of uploading/downloading files</p>                                                                                                                                                                                                                                                 |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-insertmessages"><strong>insertMessages</strong></a>(final BMXMessageList list, final BMXCallBack callBack)<br>Insert a message</p>                                                                                                                                                                                                                 |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-getmessage"><strong>getMessage</strong></a>(final long msgId, final BMXDataCallBack&#x3C; <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> > callBack)<br>Read a message</p>                                                                                                                                               |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-deleteconversation"><strong>deleteConversation</strong></a>(final long conversationId, final Boolean sync)<br>Delete a conversation</p>                                                                                                                                                                                                            |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-openconversation"><strong>openConversation</strong></a>(final long conversationId, final BMXConversation.Type type, final boolean createIfNotExist, final BMXDataCallBack&#x3C; <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md">BMXConversation</a> > callBack)<br>Launch a conversation</p>                                        |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-getallconversations"><strong>getAllConversations</strong></a>(final BMXDataCallBack&#x3C; BMXConversationList > callBack)<br>Get all conversations</p>                                                                                                                                                                                             |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-getallconversationsunreadcount"><strong>getAllConversationsUnreadCount</strong></a>(final BMXDataCallBack&#x3C; Integer > callBack)<br>Get number of unread messages for all conversations (unreads for individuals and groups marked as blocked is not counted)</p>                                                                               |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-retrievehistorymessages"><strong>retrieveHistoryMessages</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md">BMXConversation</a> conversation, final long refMsgId, final long size, final BMXDataCallBack&#x3C; BMXMessageList > callBack)<br>Pull message history</p>                                              |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-searchmessages"><strong>searchMessages</strong></a>(final String keywords, final long refTime, final long size, final BMXConversation.Direction arg4, final BMXDataCallBack&#x3C; BMXMessageListList > callBack)<br>Search for messages</p>                                                                                                        |
| void | [**searchMessages**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_chat\_manager.md#function-searchmessages)(final String keywords, final long refTime, final long size, final BMXDataCallBack< BMXMessageListList > callBack)                                                                                                                                                                                              |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-getgroupackmessageuseridlist"><strong>getGroupAckMessageUserIdList</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, final BMXDataCallBack&#x3C; ListOfLongLong > callBack)<br>Get the list of user-ids that have read group messages</p>                                                           |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-addchatlistener"><strong>addChatListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md">BMXChatServiceListener</a> listener)<br>Add chat listener</p>                                                                                                                                                        |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_manager.md#function-removechatlistener"><strong>removeChatListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md">BMXChatServiceListener</a> listener)<br>Remove chat listener</p>                                                                                                                                               |

## Public Functions Documentation

### function BMXChatManager

```java
inline BMXChatManager(
    BMXChatService service
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function sendMessage

```java
inline void sendMessage(
    final BMXMessage msg
)
```

Send a message, and the message status change is notified via listener

**Parameters**:

* **msg** Message to be sent

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function resendMessage

```java
inline void resendMessage(
    final BMXMessage msg
)
```

Resend this message, and the message status change is notified via listener

**Parameters**:

* **msg** Resent message

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function recallMessage

```java
inline void recallMessage(
    final BMXMessage msg
)
```

Recall a message, and the message status change is notified via listener

**Parameters**:

* **msg** Recalled message

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function forwardMessage

```java
inline void forwardMessage(
    final BMXMessageList list,
    final BMXConversation to,
    final BMXMessage newMsg,
    final BMXCallBack callBack
)
```

Merge and forward messages

**Parameters**:

* **list** List of messages to be forwarded
* **to** The conversation to which message is forwarded
* **newMsg** The newly generated single forwarded message from the merging list of messages to be forwarded
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function forwardMessage

```java
inline void forwardMessage(
    final BMXMessage msg
)
```

Simple forwarding messages, users should create forwarding messages first through BMXMessage:: createForwardMessage ()

**Parameters**:

* **msg** Messages to be forwarded

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function readAllMessage

```java
inline void readAllMessage(
    final BMXMessage msg
)
```

Mark this message and all previous messages as read, and synchronize to all current users' devices

**Parameters**:

* **msg** The message for which all earlier messages need to be marked as read

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function removeMessage

```java
inline void removeMessage(
    final BMXMessage msg,
    final boolean synchronize
)
```

Delete this message, which synchronizes to other devices of the current user

**Parameters**:

* **msg** Message to be deleted
* **synchronize** Whether to synchronize to other devices, otherwise only the locally stored message will be deleted

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function removeMessage

```java
inline void removeMessage(
    final BMXMessage msg
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function ackMessage

```java
inline void ackMessage(
    final BMXMessage msg
)
```

Send read acknowledgement

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function readCancel

```java
inline void readCancel(
    final BMXMessage msg
)
```

Set unread

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function downloadThumbnail

```java
inline void downloadThumbnail(
    final BMXMessage msg
)
```

Download thumbnail, downloading state changes and progress notified via listener. Thumbnail generation policy: 1 - generated by third-party server, 2 - generated by local server, default 1.

**Parameters**:

* **msg** Message requiring to download thumbnail

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function downloadAttachment

```java
inline void downloadAttachment(
    final BMXMessage msg
)
```

Downloaded attachments, and download state changes and progress are notified via listener

**Parameters**:

* **msg** Message requiring to download attachment

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function cancelDownloadAttachment

```java
inline void cancelDownloadAttachment(
    final BMXMessage msg
)
```

Cancel attachment downloading

**Parameters**:

* **msg** Message requiring to download attachment

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function transferingNum

```java
inline int transferingNum()
```

Number of uploading/downloading files

**Return**: Number of files in transfer

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function insertMessages

```java
inline void insertMessages(
    final BMXMessageList list,
    final BMXCallBack callBack
)
```

Insert a message

**Parameters**:

* **list** Insert message list
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function getMessage

```java
inline void getMessage(
    final long msgId,
    final BMXDataCallBack< BMXMessage > callBack
)
```

Read a message

**Parameters**:

* **msgId** id of the message which needs to be fetched
* **callBack** [BMXMessage](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message.md)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function deleteConversation

```java
inline void deleteConversation(
    final long conversationId,
    final Boolean sync
)
```

Delete a conversation

**Parameters**:

* **conversationId** Conversation id requiring to delete conversation
* **sync** Whether to delete the conversation on other devices synchronously, default false, means only delete the conversation on the current device

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function openConversation

```java
inline void openConversation(
    final long conversationId,
    final BMXConversation.Type type,
    final boolean createIfNotExist,
    final BMXDataCallBack< BMXConversation > callBack
)
```

Launch a conversation

**Parameters**:

* **conversationId** id of the conversation which needs to be opened
* **type** Conversation type, single/group chat.
* **createIfNotExist** Whether to create a local conversation if no conversation existing, default to create
* **callBack** [BMXConversation](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_conversation.md)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function getAllConversations

```java
inline void getAllConversations(
    final BMXDataCallBack< BMXConversationList > callBack
)
```

Get all conversations

**Parameters**:

* **callBack** BMXConversationList

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function getAllConversationsUnreadCount

```java
inline void getAllConversationsUnreadCount(
    final BMXDataCallBack< Integer > callBack
)
```

Get number of unread messages for all conversations (unreads for individuals and groups marked as blocked is not counted)

**Parameters**:

* **callBack** Number of unreads

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function retrieveHistoryMessages

```java
inline void retrieveHistoryMessages(
    final BMXConversation conversation,
    final long refMsgId,
    final long size,
    final BMXDataCallBack< BMXMessageList > callBack
)
```

Pull message history

**Parameters**:

* **conversation** Conversation for which message history needs to pull
* **refMsgId** Start message Id for pulling conversation messages
* **size** Maximum number of messages to pull
* **callBack** BMXErrorCode,Message list obtained by pull

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

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

Search for messages

**Parameters**:

* **keywords** Keyword for search
* **refTime** Start time of message search
* **size** Maximum number of messages to search
* **arg4** Message search direction, default (Direction::Up)means search from earlier messages.
* **callBack** BMXErrorCode,List of searched message results

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function searchMessages

```java
inline void searchMessages(
    final String keywords,
    final long refTime,
    final long size,
    final BMXDataCallBack< BMXMessageListList > callBack
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```

### function getGroupAckMessageUserIdList

```java
inline void getGroupAckMessageUserIdList(
    final BMXMessage msg,
    final BMXDataCallBack< ListOfLongLong > callBack
)
```

Get the list of user-ids that have read group messages

**Parameters**:

* **msg** Message requiring to get list of read user ids
* **callBack** \[BMXErrorCode], list of user ids that have read this message

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatManager'></div>
```



Updated on 2022-01-26 at 17:18:31 +0800
