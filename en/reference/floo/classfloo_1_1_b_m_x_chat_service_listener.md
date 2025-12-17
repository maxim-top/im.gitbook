---
title: floo::BMXChatServiceListener
summary: Chat listener
---

# floo::BMXChatServiceListener

Chat listener

`#include <bmx_chat_service_listener.h>`

## Public Functions

|              | Name                                                                                                                                                                                                                                                                                                                |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-bmxchatservicelistener"><strong>BMXChatServiceListener</strong></a>()<br>Constructor</p>                                                                                                                                                          |
| virtual      | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-~bmxchatservicelistener"><strong>~BMXChatServiceListener</strong></a>()<br>Destructor</p>                                                                                                                                                         |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onstatuschanged"><strong>onStatusChanged</strong></a>(BMXMessagePtr msg, BMXErrorCode error)<br>Message state changed</p>                                                                                                                         |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onattachmentuploadprogresschanged"><strong>onAttachmentUploadProgressChanged</strong></a>(BMXMessagePtr msg, int percent)<br>Attachment upload state changed</p>                                                                                  |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onrecallstatuschanged"><strong>onRecallStatusChanged</strong></a>(BMXMessagePtr msg, BMXErrorCode error)<br>Message recall state changed</p>                                                                                                      |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceive"><strong>onReceive</strong></a>(const BMXMessageList &#x26; list)<br>Messages received</p>                                                                                                                                              |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivecommandmessages"><strong>onReceiveCommandMessages</strong></a>(const BMXMessageList &#x26; list)<br>Command received</p>                                                                                                                 |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivesystemmessages"><strong>onReceiveSystemMessages</strong></a>(const BMXMessageList &#x26; list)<br>System notification messages received</p>                                                                                              |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivereadacks"><strong>onReceiveReadAcks</strong></a>(const BMXMessageList &#x26; list)<br>Read acknowledgement of messages received</p>                                                                                                      |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivedeliveracks"><strong>onReceiveDeliverAcks</strong></a>(const BMXMessageList &#x26; list)<br>Acknowledgement of message delivered received</p>                                                                                            |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceiverecallmessages"><strong>onReceiveRecallMessages</strong></a>(const BMXMessageList &#x26; list)<br>Canceled messages received</p>                                                                                                         |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivereadcancels"><strong>onReceiveReadCancels</strong></a>(const BMXMessageList &#x26; list)<br>Message re-unread received (cross-device synchronization for changing message status into unread)</p>                                        |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivereadallmessages"><strong>onReceiveReadAllMessages</strong></a>(const BMXMessageList &#x26; list)<br>All received messages are read (all messages are set to read before cross-device synchronization)</p>                                |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivedeletemessages"><strong>onReceiveDeleteMessages</strong></a>(const BMXMessageList &#x26; list)<br>Message deletions received (delete messages cross devices synchronously)</p>                                                           |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceiveplayacks"><strong>onReceivePlayAcks</strong></a>(const BMXMessageList &#x26; list)<br>Received acknowledgement of audio/video message playback</p>                                                                                       |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onattachmentstatuschanged"><strong>onAttachmentStatusChanged</strong></a>(BMXMessagePtr msg, BMXErrorCode error, int percent)<br>Attachment download state changed</p>                                                                            |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onattachmentdownloadbyurlstatuschanged"><strong>onAttachmentDownloadByUrlStatusChanged</strong></a>(int64_t msgId, BMXErrorCode error, int percent)<br>Attachment download state changed</p>                                                      |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onretrievehistorymessages"><strong>onRetrieveHistoryMessages</strong></a>(BMXConversationPtr conversation)<br>Pull message history</p>                                                                                                            |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onloadallconversation"><strong>onLoadAllConversation</strong></a>()<br>List of unread conversations has been loaded</p>                                                                                                                           |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onconversationcreate"><strong>onConversationCreate</strong></a>(BMXConversationPtr conversation, BMXMessagePtr msg)<br>Create a new conversation locally</p>                                                                                      |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onconversationdelete"><strong>onConversationDelete</strong></a>(int64_t conversationId, BMXErrorCode error)<br>Delete a conversation</p>                                                                                                          |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-ontotalunreadcountchanged"><strong>onTotalUnreadCountChanged</strong></a>(int unreadCount)<br>Update total number of unread messages</p>                                                                                                          |
| void         | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-registerchatservice"><strong>registerChatService</strong></a>(<a href="classfloo_1_1_b_m_x_chat_service.md">BMXChatService</a> * service)<br>Register BMXChatService to which BMXChatServiceListener is bound (automatic registration in SDK)</p> |

## Protected Attributes

|                                                          | Name                                                                           |
| -------------------------------------------------------- | ------------------------------------------------------------------------------ |
| [BMXChatService](classfloo_1_1_b_m_x_chat_service.md) \* | [**mService**](classfloo_1_1_b_m_x_chat_service_listener.md#variable-mservice) |

## Public Functions Documentation

### function BMXChatServiceListener

```cpp
inline BMXChatServiceListener()
```

Constructor

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function \~BMXChatServiceListener

```cpp
inline virtual ~BMXChatServiceListener()
```

Destructor

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onStatusChanged

```cpp
inline virtual void onStatusChanged(
    BMXMessagePtr msg,
    BMXErrorCode error
)
```

Message state changed

**Parameters**:

* **msg** Message with state changed
* **error** State error code

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onAttachmentUploadProgressChanged

```cpp
inline virtual void onAttachmentUploadProgressChanged(
    BMXMessagePtr msg,
    int percent
)
```

Attachment upload state changed

**Parameters**:

* **msg** Message for uploading attachment
* **percent** Progress of attachment uploading

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onRecallStatusChanged

```cpp
inline virtual void onRecallStatusChanged(
    BMXMessagePtr msg,
    BMXErrorCode error
)
```

Message recall state changed

**Parameters**:

* **msg** Message with state change canceled
* **error** State error code

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onReceive

```cpp
inline virtual void onReceive(
    const BMXMessageList & list
)
```

Messages received

**Parameters**:

* **list** List of received messages

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onReceiveCommandMessages

```cpp
inline virtual void onReceiveCommandMessages(
    const BMXMessageList & list
)
```

Command received

**Parameters**:

* **list** List of received messages

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onReceiveSystemMessages

```cpp
inline virtual void onReceiveSystemMessages(
    const BMXMessageList & list
)
```

System notification messages received

**Parameters**:

* **list** List of received system messages

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onReceiveReadAcks

```cpp
inline virtual void onReceiveReadAcks(
    const BMXMessageList & list
)
```

Read acknowledgement of messages received

**Parameters**:

* **list** List of received messages with read acknowledgement

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onReceiveDeliverAcks

```cpp
inline virtual void onReceiveDeliverAcks(
    const BMXMessageList & list
)
```

Acknowledgement of message delivered received

**Parameters**:

* **list** List of received messages with delivered acknowledgement

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onReceiveRecallMessages

```cpp
inline virtual void onReceiveRecallMessages(
    const BMXMessageList & list
)
```

Canceled messages received

**Parameters**:

* **list** List of canceled messages received

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onReceiveReadCancels

```cpp
inline virtual void onReceiveReadCancels(
    const BMXMessageList & list
)
```

Message re-unread received (cross-device synchronization for changing message status into unread)

**Parameters**:

* **list** List of received messages with re-unread acknowledgement

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onReceiveReadAllMessages

```cpp
inline virtual void onReceiveReadAllMessages(
    const BMXMessageList & list
)
```

All received messages are read (all messages are set to read before cross-device synchronization)

**Parameters**:

* **list** List of received messages with all-read acknowledgement

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onReceiveDeleteMessages

```cpp
inline virtual void onReceiveDeleteMessages(
    const BMXMessageList & list
)
```

Message deletions received (delete messages cross devices synchronously)

**Parameters**:

* **list** List of deleted messages received

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onReceivePlayAcks

```cpp
inline virtual void onReceivePlayAcks(
    const BMXMessageList & list
)
```

Received acknowledgement of audio/video message playback

**Parameters**:

* **list** List of received audio/video messages with playback acknowledgement

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onAttachmentStatusChanged

```cpp
inline virtual void onAttachmentStatusChanged(
    BMXMessagePtr msg,
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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onAttachmentDownloadByUrlStatusChanged

```cpp
inline virtual void onAttachmentDownloadByUrlStatusChanged(
    int64_t msgId,
    BMXErrorCode error,
    int percent
)
```

Attachment download state changed

**Parameters**:

* **msgId** Message ID with downloading state changed
* **error** State error code
* **percent** Progress of attachment downloading

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onRetrieveHistoryMessages

```cpp
inline virtual void onRetrieveHistoryMessages(
    BMXConversationPtr conversation
)
```

Pull message history

**Parameters**:

* **conversation** Conversation for which a specific message history was pulled

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onLoadAllConversation

```cpp
inline virtual void onLoadAllConversation()
```

List of unread conversations has been loaded

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onConversationCreate

```cpp
inline virtual void onConversationCreate(
    BMXConversationPtr conversation,
    BMXMessagePtr msg
)
```

Create a new conversation locally

**Parameters**:

* **conversation** Newly created local conversation
* **msg** Latest message for conversation, return for existing, empty for no existing

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onConversationDelete

```cpp
inline virtual void onConversationDelete(
    int64_t conversationId,
    BMXErrorCode error
)
```

Delete a conversation

**Parameters**:

* **conversationId** Deleted local conversation id
* **error** State error code

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function onTotalUnreadCountChanged

```cpp
inline virtual void onTotalUnreadCountChanged(
    int unreadCount
)
```

Update total number of unread messages

**Parameters**:

* **unreadCount** Total number of local unread conversations

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>

```

### function registerChatService

```cpp
inline void registerChatService(
    BMXChatService * service
)
```

Register BMXChatService to which BMXChatServiceListener is bound (automatic registration in SDK)

**Parameters**:

* **service** [BMXChatService](classfloo_1_1_b_m_x_chat_service.md)

## Protected Attributes Documentation

### variable mService

```cpp
BMXChatService * mService;
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
