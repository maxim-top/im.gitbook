---
title: floo::BMXChatServiceListener
summary: Chat listener 

---

# floo::BMXChatServiceListener



Chat listener 


`#include <bmx_chat_service_listener.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXChatServiceListener](classfloo_1_1_b_m_x_chat_service_listener.md#function-bmxchatservicelistener)**()<br>Constructor  |
| virtual | **[~BMXChatServiceListener](classfloo_1_1_b_m_x_chat_service_listener.md#function-~bmxchatservicelistener)**()<br>Destructor  |
| virtual void | **[onStatusChanged](classfloo_1_1_b_m_x_chat_service_listener.md#function-onstatuschanged)**(BMXMessagePtr msg, BMXErrorCode error)<br>Message state changed  |
| virtual void | **[onAttachmentUploadProgressChanged](classfloo_1_1_b_m_x_chat_service_listener.md#function-onattachmentuploadprogresschanged)**(BMXMessagePtr msg, int percent)<br>Attachment upload state changed  |
| virtual void | **[onRecallStatusChanged](classfloo_1_1_b_m_x_chat_service_listener.md#function-onrecallstatuschanged)**(BMXMessagePtr msg, BMXErrorCode error)<br>Message recall state changed  |
| virtual void | **[onReceive](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceive)**(const BMXMessageList & list)<br>Messages received  |
| virtual void | **[onReceiveCommandMessages](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivecommandmessages)**(const BMXMessageList & list)<br>Command received  |
| virtual void | **[onReceiveSystemMessages](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivesystemmessages)**(const BMXMessageList & list)<br>System notification messages received  |
| virtual void | **[onReceiveReadAcks](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivereadacks)**(const BMXMessageList & list)<br>Read acknowledgement of messages received  |
| virtual void | **[onReceiveDeliverAcks](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivedeliveracks)**(const BMXMessageList & list)<br>Acknowledgement of message delivered received  |
| virtual void | **[onReceiveRecallMessages](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceiverecallmessages)**(const BMXMessageList & list)<br>Canceled messages received  |
| virtual void | **[onReceiveReadCancels](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivereadcancels)**(const BMXMessageList & list)<br>Message re-unread received (cross-device synchronization for changing message status into unread)  |
| virtual void | **[onReceiveReadAllMessages](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivereadallmessages)**(const BMXMessageList & list)<br>All received messages are read (all messages are set to read before cross-device synchronization)  |
| virtual void | **[onReceiveDeleteMessages](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivedeletemessages)**(const BMXMessageList & list)<br> Message deletions received (delete messages cross devices synchronously)  |
| virtual void | **[onReceivePlayAcks](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceiveplayacks)**(const BMXMessageList & list)<br>Received acknowledgement of audio/video message playback  |
| virtual void | **[onAttachmentStatusChanged](classfloo_1_1_b_m_x_chat_service_listener.md#function-onattachmentstatuschanged)**(BMXMessagePtr msg, BMXErrorCode error, int percent)<br>Attachment download state changed  |
| virtual void | **[onAttachmentDownloadByUrlStatusChanged](classfloo_1_1_b_m_x_chat_service_listener.md#function-onattachmentdownloadbyurlstatuschanged)**(int64_t msgId, BMXErrorCode error, int percent)<br>Attachment download state changed  |
| virtual void | **[onRetrieveHistoryMessages](classfloo_1_1_b_m_x_chat_service_listener.md#function-onretrievehistorymessages)**(BMXConversationPtr conversation)<br>Pull message history  |
| virtual void | **[onLoadAllConversation](classfloo_1_1_b_m_x_chat_service_listener.md#function-onloadallconversation)**()<br>List of unread conversations has been loaded  |
| virtual void | **[onConversationCreate](classfloo_1_1_b_m_x_chat_service_listener.md#function-onconversationcreate)**(BMXConversationPtr conversation, BMXMessagePtr msg)<br>Create a new conversation locally  |
| virtual void | **[onConversationDelete](classfloo_1_1_b_m_x_chat_service_listener.md#function-onconversationdelete)**(int64_t conversationId, BMXErrorCode error)<br> Delete a conversation  |
| virtual void | **[onTotalUnreadCountChanged](classfloo_1_1_b_m_x_chat_service_listener.md#function-ontotalunreadcountchanged)**(int unreadCount)<br>Update total number of unread messages  |
| void | **[registerChatService](classfloo_1_1_b_m_x_chat_service_listener.md#function-registerchatservice)**([BMXChatService](classfloo_1_1_b_m_x_chat_service.md) * service)<br>Register BMXChatService to which BMXChatServiceListener is bound (automatic registration in SDK)  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [BMXChatService](classfloo_1_1_b_m_x_chat_service.md) * | **[mService](classfloo_1_1_b_m_x_chat_service_listener.md#variable-mservice)**  |

## Public Functions Documentation

### function BMXChatServiceListener

```cpp
inline BMXChatServiceListener()
```

Constructor 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="BMXChatServiceListener" %}{% endlanying_code_snippet %}
```
### function ~BMXChatServiceListener

```cpp
inline virtual ~BMXChatServiceListener()
```

Destructor 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="~BMXChatServiceListener" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onStatusChanged" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onAttachmentUploadProgressChanged" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onRecallStatusChanged" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onReceive" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onReceiveCommandMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onReceiveSystemMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onReceiveReadAcks" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onReceiveDeliverAcks" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onReceiveRecallMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onReceiveReadCancels" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onReceiveReadAllMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onReceiveDeleteMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onReceivePlayAcks" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onAttachmentStatusChanged" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onAttachmentDownloadByUrlStatusChanged" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onRetrieveHistoryMessages" %}{% endlanying_code_snippet %}
```
### function onLoadAllConversation

```cpp
inline virtual void onLoadAllConversation()
```

List of unread conversations has been loaded 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onLoadAllConversation" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onConversationCreate" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onConversationDelete" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="onTotalUnreadCountChanged" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXChatServiceListener",function="registerChatService" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800