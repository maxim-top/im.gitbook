---
title: im::floo::floolib::BMXChatServiceListener
summary: Chat listener
---

# im::floo::floolib::BMXChatServiceListener

Chat listener

## Public Functions

|                   | Name                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-delete)()                                                                                                                                                                                                                                                                              |
| void              | [**swigReleaseOwnership**](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-swigreleaseownership)()                                                                                                                                                                                                                                                  |
| void              | [**swigTakeOwnership**](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-swigtakeownership)()                                                                                                                                                                                                                                                        |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onstatuschanged"><strong>onStatusChanged</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, [BMXErrorCode] error)<br>Message state changed</p>                                                                                                  |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onattachmentuploadprogresschanged"><strong>onAttachmentUploadProgressChanged</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, int percent)<br>Attachment upload state changed</p>                                                             |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onrecallstatuschanged"><strong>onRecallStatusChanged</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, [BMXErrorCode] error)<br>Message recall state changed</p>                                                                               |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceive"><strong>onReceive</strong></a>(BMXMessageList list)<br>Messages received</p>                                                                                                                                                                                                 |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivecommandmessages"><strong>onReceiveCommandMessages</strong></a>(BMXMessageList list)<br>Command received</p>                                                                                                                                                                    |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivesystemmessages"><strong>onReceiveSystemMessages</strong></a>(BMXMessageList list)<br>System notification messages received</p>                                                                                                                                                 |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivereadacks"><strong>onReceiveReadAcks</strong></a>(BMXMessageList list)<br>Read acknowledgement of messages received</p>                                                                                                                                                         |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivedeliveracks"><strong>onReceiveDeliverAcks</strong></a>(BMXMessageList list)<br>Acknowledgement of message delivered received</p>                                                                                                                                               |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceiverecallmessages"><strong>onReceiveRecallMessages</strong></a>(BMXMessageList list)<br>Canceled messages received</p>                                                                                                                                                            |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivereadcancels"><strong>onReceiveReadCancels</strong></a>(BMXMessageList list)<br>Message re-unread received (cross-device synchronization for changing message status into unread)</p>                                                                                           |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivereadallmessages"><strong>onReceiveReadAllMessages</strong></a>(BMXMessageList list)<br>All received messages are read (all messages are set to read before cross-device synchronization)</p>                                                                                   |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivedeletemessages"><strong>onReceiveDeleteMessages</strong></a>(BMXMessageList list)<br>Message deletions received (delete messages cross devices synchronously)</p>                                                                                                              |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceiveplayacks"><strong>onReceivePlayAcks</strong></a>(BMXMessageList list)<br>Acknowledgement of message played received</p>                                                                                                                                                        |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onattachmentstatuschanged"><strong>onAttachmentStatusChanged</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, [BMXErrorCode] error, int percent)<br>Attachment download state changed</p>                                                     |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onattachmentdownloadbyurlstatuschanged"><strong>onAttachmentDownloadByUrlStatusChanged</strong></a>(long msgId, [BMXErrorCode] error, int percent)<br>Attachment download state changed</p>                                                                                             |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onretrievehistorymessages"><strong>onRetrieveHistoryMessages</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md">BMXConversation</a> conversation)<br>Pull message history</p>                                                                                  |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onloadallconversation"><strong>onLoadAllConversation</strong></a>()<br>List of unread conversations has been loaded</p>                                                                                                                                                                 |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onconversationcreate"><strong>onConversationCreate</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md">BMXConversation</a> conversation, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg)<br>Create a new conversation locally</p> |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onconversationdelete"><strong>onConversationDelete</strong></a>(long conversationId, [BMXErrorCode] error)<br>Delete a conversation</p>                                                                                                                                                 |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-ontotalunreadcountchanged"><strong>onTotalUnreadCountChanged</strong></a>(int unreadCount)<br>Update total number of unread messages</p>                                                                                                                                                |
|                   | [**BMXChatServiceListener**](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-bmxchatservicelistener)()                                                                                                                                                                                                                                              |
| void              | [**registerChatService**](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-registerchatservice)([BMXChatService](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md) service)                                                                                                                                                                      |

## Protected Functions

|      | Name                                                                                                                                                                                       |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|      | [**BMXChatServiceListener**](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-bmxchatservicelistener)(long cPtr, boolean cMemoryOwn)                                 |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-finalize)()                                                                                          |
| void | [**swigDirectorDisconnect**](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-swigdirectordisconnect)()                                                              |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-getcptr)([BMXChatServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md) obj) |

## Protected Attributes

|                   | Name                                                                                                  |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| transient boolean | [**swigCMemOwn**](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#variable-swigcmemown) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function swigReleaseOwnership

```java
inline void swigReleaseOwnership()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function swigTakeOwnership

```java
inline void swigTakeOwnership()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onStatusChanged

```java
inline void onStatusChanged(
    BMXMessage msg,
    BMXErrorCode error
)
```

Message state changed

**Parameters**:

* **msg** Message with state changed
* **error** State error code

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onAttachmentUploadProgressChanged

```java
inline void onAttachmentUploadProgressChanged(
    BMXMessage msg,
    int percent
)
```

Attachment upload state changed

**Parameters**:

* **msg** Message for uploading attachment
* **percent** Progress of attachment uploading

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onRecallStatusChanged

```java
inline void onRecallStatusChanged(
    BMXMessage msg,
    BMXErrorCode error
)
```

Message recall state changed

**Parameters**:

* **msg** Message with state change canceled
* **error** State error code

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onReceive

```java
inline void onReceive(
    BMXMessageList list
)
```

Messages received

**Parameters**:

* **list** List of received messages

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onReceiveCommandMessages

```java
inline void onReceiveCommandMessages(
    BMXMessageList list
)
```

Command received

**Parameters**:

* **list** List of received messages

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onReceiveSystemMessages

```java
inline void onReceiveSystemMessages(
    BMXMessageList list
)
```

System notification messages received

**Parameters**:

* **list** List of received system messages

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onReceiveReadAcks

```java
inline void onReceiveReadAcks(
    BMXMessageList list
)
```

Read acknowledgement of messages received

**Parameters**:

* **list** List of received messages with read acknowledgement

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onReceiveDeliverAcks

```java
inline void onReceiveDeliverAcks(
    BMXMessageList list
)
```

Acknowledgement of message delivered received

**Parameters**:

* **list** List of received messages with delivered acknowledgement

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onReceiveRecallMessages

```java
inline void onReceiveRecallMessages(
    BMXMessageList list
)
```

Canceled messages received

**Parameters**:

* **list** List of canceled messages received

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onReceiveReadCancels

```java
inline void onReceiveReadCancels(
    BMXMessageList list
)
```

Message re-unread received (cross-device synchronization for changing message status into unread)

**Parameters**:

* **list** List of received messages with re-unread acknowledgement

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onReceiveReadAllMessages

```java
inline void onReceiveReadAllMessages(
    BMXMessageList list
)
```

All received messages are read (all messages are set to read before cross-device synchronization)

**Parameters**:

* **list** List of received messages with all-read acknowledgement

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onReceiveDeleteMessages

```java
inline void onReceiveDeleteMessages(
    BMXMessageList list
)
```

Message deletions received (delete messages cross devices synchronously)

**Parameters**:

* **list** List of deleted messages received

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onReceivePlayAcks

```java
inline void onReceivePlayAcks(
    BMXMessageList list
)
```

Acknowledgement of message played received

**Parameters**:

* **list** List of received messages with read acknowledgement

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onAttachmentStatusChanged

```java
inline void onAttachmentStatusChanged(
    BMXMessage msg,
    BMXErrorCode error,
    int percent
)
```

Attachment download state changed

**Parameters**:

* **msg** Message with downloading state changed
* **error** State error code
* **percent** Progress of attachment downloading

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onAttachmentDownloadByUrlStatusChanged

```java
inline void onAttachmentDownloadByUrlStatusChanged(
    long msgId,
    BMXErrorCode error,
    int percent
)
```

Attachment download state changed

**Parameters**:

* **msgId** Message ID with download state changed
* **error** State error code
* **percent** Progress of attachment downloading

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onRetrieveHistoryMessages

```java
inline void onRetrieveHistoryMessages(
    BMXConversation conversation
)
```

Pull message history

**Parameters**:

* **conversation** Conversation for which a specific message history was pulled

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onLoadAllConversation

```java
inline void onLoadAllConversation()
```

List of unread conversations has been loaded

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onConversationCreate

```java
inline void onConversationCreate(
    BMXConversation conversation,
    BMXMessage msg
)
```

Create a new conversation locally

**Parameters**:

* **conversation** Newly created local conversation
* **msg** Latest message for conversation, return for existing, empty for no existing

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onConversationDelete

```java
inline void onConversationDelete(
    long conversationId,
    BMXErrorCode error
)
```

Delete a conversation

**Parameters**:

* **conversationId** Deleted local conversation id
* **error** State error code

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function onTotalUnreadCountChanged

```java
inline void onTotalUnreadCountChanged(
    int unreadCount
)
```

Update total number of unread messages

**Parameters**:

* **unreadCount** Total number of local unread conversations

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function BMXChatServiceListener

```java
inline BMXChatServiceListener()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function finalize

```java
inline void finalize()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

```

### function swigDirectorDisconnect

```java
inline void swigDirectorDisconnect()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXChatServiceListener'></div>
```

***

Updated on 2022-01-26 at 17:18:31 +0800
