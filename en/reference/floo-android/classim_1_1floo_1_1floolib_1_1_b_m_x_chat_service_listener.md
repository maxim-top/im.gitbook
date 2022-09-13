---
title: im::floo::floolib::BMXChatServiceListener
summary: Chat listener 

---

# im::floo::floolib::BMXChatServiceListener



Chat listener 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-delete)**() |
| void | **[swigReleaseOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-swigreleaseownership)**() |
| void | **[swigTakeOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-swigtakeownership)**() |
| void | **[onStatusChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onstatuschanged)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, [BMXErrorCode] error)<br>Message state changed  |
| void | **[onAttachmentUploadProgressChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onattachmentuploadprogresschanged)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, int percent)<br>Attachment upload state changed  |
| void | **[onRecallStatusChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onrecallstatuschanged)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, [BMXErrorCode] error)<br>Message recall state changed  |
| void | **[onReceive](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceive)**(BMXMessageList list)<br>Messages received  |
| void | **[onReceiveCommandMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivecommandmessages)**(BMXMessageList list)<br>Command received  |
| void | **[onReceiveSystemMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivesystemmessages)**(BMXMessageList list)<br>System notification messages received  |
| void | **[onReceiveReadAcks](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivereadacks)**(BMXMessageList list)<br>Read acknowledgement of messages received  |
| void | **[onReceiveDeliverAcks](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivedeliveracks)**(BMXMessageList list)<br>Acknowledgement of message delivered received  |
| void | **[onReceiveRecallMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceiverecallmessages)**(BMXMessageList list)<br>Canceled messages received  |
| void | **[onReceiveReadCancels](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivereadcancels)**(BMXMessageList list)<br>Message re-unread received (cross-device synchronization for changing message status into unread)  |
| void | **[onReceiveReadAllMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivereadallmessages)**(BMXMessageList list)<br>All received messages are read (all messages are set to read before cross-device synchronization)  |
| void | **[onReceiveDeleteMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivedeletemessages)**(BMXMessageList list)<br> Message deletions received (delete messages cross devices synchronously)  |
| void | **[onReceivePlayAcks](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceiveplayacks)**(BMXMessageList list)<br>Acknowledgement of message played received  |
| void | **[onAttachmentStatusChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onattachmentstatuschanged)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, [BMXErrorCode] error, int percent)<br>Attachment download state changed  |
| void | **[onAttachmentDownloadByUrlStatusChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onattachmentdownloadbyurlstatuschanged)**(long msgId, [BMXErrorCode] error, int percent)<br>Attachment download state changed  |
| void | **[onRetrieveHistoryMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onretrievehistorymessages)**([BMXConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md) conversation)<br>Pull message history  |
| void | **[onLoadAllConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onloadallconversation)**()<br>List of unread conversations has been loaded  |
| void | **[onConversationCreate](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onconversationcreate)**([BMXConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md) conversation, [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>Create a new conversation locally  |
| void | **[onConversationDelete](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onconversationdelete)**(long conversationId, [BMXErrorCode] error)<br> Delete a conversation  |
| void | **[onTotalUnreadCountChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-ontotalunreadcountchanged)**(int unreadCount)<br>Update total number of unread messages  |
| | **[BMXChatServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-bmxchatservicelistener)**() |
| void | **[registerChatService](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-registerchatservice)**([BMXChatService](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service.md) service) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXChatServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-bmxchatservicelistener)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-finalize)**() |
| void | **[swigDirectorDisconnect](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-swigdirectordisconnect)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-getcptr)**([BMXChatServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md) obj) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| transient boolean | **[swigCMemOwn](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#variable-swigcmemown)**  |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="delete" %}{% endlanying_code_snippet %}
```
### function swigReleaseOwnership

```java
inline void swigReleaseOwnership()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="swigReleaseOwnership" %}{% endlanying_code_snippet %}
```
### function swigTakeOwnership

```java
inline void swigTakeOwnership()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="swigTakeOwnership" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onStatusChanged" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onAttachmentUploadProgressChanged" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onRecallStatusChanged" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceive" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceiveCommandMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceiveSystemMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceiveReadAcks" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceiveDeliverAcks" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceiveRecallMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceiveReadCancels" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceiveReadAllMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceiveDeleteMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onReceivePlayAcks" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onAttachmentStatusChanged" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onAttachmentDownloadByUrlStatusChanged" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onRetrieveHistoryMessages" %}{% endlanying_code_snippet %}
```
### function onLoadAllConversation

```java
inline void onLoadAllConversation()
```

List of unread conversations has been loaded 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onLoadAllConversation" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onConversationCreate" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onConversationDelete" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="onTotalUnreadCountChanged" %}{% endlanying_code_snippet %}
```
### function BMXChatServiceListener

```java
inline BMXChatServiceListener()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="BMXChatServiceListener" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="registerChatService" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="BMXChatServiceListener" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="finalize" %}{% endlanying_code_snippet %}
```
### function swigDirectorDisconnect

```java
inline void swigDirectorDisconnect()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="swigDirectorDisconnect" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXChatServiceListener",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800