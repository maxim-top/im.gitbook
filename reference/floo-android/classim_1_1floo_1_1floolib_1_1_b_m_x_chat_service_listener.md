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
| void | **[onStatusChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onstatuschanged)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, [BMXErrorCode] error)<br>Messaging state changed  |
| void | **[onAttachmentUploadProgressChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onattachmentuploadprogresschanged)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, int percent)<br>Attachment upload state changed  |
| void | **[onRecallStatusChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onrecallstatuschanged)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, [BMXErrorCode] error)<br>Message recall state changed  |
| void | **[onReceive](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceive)**(BMXMessageList list)<br>Message received  |
| void | **[onReceiveCommandMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivecommandmessages)**(BMXMessageList list)<br>Command received  |
| void | **[onReceiveSystemMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivesystemmessages)**(BMXMessageList list)<br>System notification message received  |
| void | **[onReceiveReadAcks](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivereadacks)**(BMXMessageList list)<br>Receipt of message read received  |
| void | **[onReceiveDeliverAcks](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivedeliveracks)**(BMXMessageList list)<br>Receipt of message delivered received  |
| void | **[onReceiveRecallMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceiverecallmessages)**(BMXMessageList list)<br>Canceled message received  |
| void | **[onReceiveReadCancels](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivereadcancels)**(BMXMessageList list)<br>Message re-unread received (cross-device synchronization for changing message status into unread)  |
| void | **[onReceiveReadAllMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivereadallmessages)**(BMXMessageList list)<br>All received messages are read (all messages are set to read before cross-device synchronization)  |
| void | **[onReceiveDeleteMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceivedeletemessages)**(BMXMessageList list)<br>Deletion received (delete messages cross devices synchronously)  |
| void | **[onReceivePlayAcks](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onreceiveplayacks)**(BMXMessageList list)<br>Receipt of message played received  |
| void | **[onAttachmentStatusChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onattachmentstatuschanged)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, [BMXErrorCode] error, int percent)<br>Attachment download state changed  |
| void | **[onAttachmentDownloadByUrlStatusChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onattachmentdownloadbyurlstatuschanged)**(long msgId, [BMXErrorCode] error, int percent)<br>Attachment download state changed  |
| void | **[onRetrieveHistoryMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onretrievehistorymessages)**([BMXConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md) conversation)<br>Pull message history  |
| void | **[onLoadAllConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onloadallconversation)**()<br>List of unread conversations has been loaded  |
| void | **[onConversationCreate](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onconversationcreate)**([BMXConversation](classim_1_1floo_1_1floolib_1_1_b_m_x_conversation.md) conversation, [BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg)<br>Create a new conversation locally  |
| void | **[onConversationDelete](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-onconversationdelete)**(long conversationId, [BMXErrorCode] error)<br>Delete conversation  |
| void | **[onTotalUnreadCountChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_chat_service_listener.md#function-ontotalunreadcountchanged)**(int unreadCount)<br>Update total unread-number  |
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


### function swigReleaseOwnership

```java
inline void swigReleaseOwnership()
```


### function swigTakeOwnership

```java
inline void swigTakeOwnership()
```


### function onStatusChanged

```java
inline void onStatusChanged(
    BMXMessage msg,
    BMXErrorCode error
)
```

Messaging state changed 

**Parameters**: 

  * **msg** Message with state changed 
  * **error** State error code 


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


### function onReceive

```java
inline void onReceive(
    BMXMessageList list
)
```

Message received 

**Parameters**: 

  * **list** List of received messages 


### function onReceiveCommandMessages

```java
inline void onReceiveCommandMessages(
    BMXMessageList list
)
```

Command received 

**Parameters**: 

  * **list** List of received messages 


### function onReceiveSystemMessages

```java
inline void onReceiveSystemMessages(
    BMXMessageList list
)
```

System notification message received 

**Parameters**: 

  * **list** List of received system messages 


### function onReceiveReadAcks

```java
inline void onReceiveReadAcks(
    BMXMessageList list
)
```

Receipt of message read received 

**Parameters**: 

  * **list** List of received messages with read receipt 


### function onReceiveDeliverAcks

```java
inline void onReceiveDeliverAcks(
    BMXMessageList list
)
```

Receipt of message delivered received 

**Parameters**: 

  * **list** List of received messages with delivered receipt 


### function onReceiveRecallMessages

```java
inline void onReceiveRecallMessages(
    BMXMessageList list
)
```

Canceled message received 

**Parameters**: 

  * **list** List of canceled messages received 


### function onReceiveReadCancels

```java
inline void onReceiveReadCancels(
    BMXMessageList list
)
```

Message re-unread received (cross-device synchronization for changing message status into unread) 

**Parameters**: 

  * **list** List of received messages with re-unread receipt 


### function onReceiveReadAllMessages

```java
inline void onReceiveReadAllMessages(
    BMXMessageList list
)
```

All received messages are read (all messages are set to read before cross-device synchronization) 

**Parameters**: 

  * **list** List of received messages with all-read receipt 


### function onReceiveDeleteMessages

```java
inline void onReceiveDeleteMessages(
    BMXMessageList list
)
```

Deletion received (delete messages cross devices synchronously) 

**Parameters**: 

  * **list** List of deleted messages received 


### function onReceivePlayAcks

```java
inline void onReceivePlayAcks(
    BMXMessageList list
)
```

Receipt of message played received 

**Parameters**: 

  * **list** List of received messages with read receipt 


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


### function onRetrieveHistoryMessages

```java
inline void onRetrieveHistoryMessages(
    BMXConversation conversation
)
```

Pull message history 

**Parameters**: 

  * **conversation** Conversation for which a specific message history was pulled 


### function onLoadAllConversation

```java
inline void onLoadAllConversation()
```

List of unread conversations has been loaded 

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


### function onConversationDelete

```java
inline void onConversationDelete(
    long conversationId,
    BMXErrorCode error
)
```

Delete conversation 

**Parameters**: 

  * **conversationId** Deleted local conversation id 
  * **error** State error code 


### function onTotalUnreadCountChanged

```java
inline void onTotalUnreadCountChanged(
    int unreadCount
)
```

Update total unread-number 

**Parameters**: 

  * **unreadCount** Total number of local unread conversations 


### function BMXChatServiceListener

```java
inline BMXChatServiceListener()
```


### function registerChatService

```java
inline void registerChatService(
    BMXChatService service
)
```


## Protected Functions Documentation

### function BMXChatServiceListener

```java
inline BMXChatServiceListener(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
```


### function swigDirectorDisconnect

```java
inline void swigDirectorDisconnect()
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


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800