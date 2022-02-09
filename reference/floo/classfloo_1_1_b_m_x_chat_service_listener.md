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
| virtual void | **[onStatusChanged](classfloo_1_1_b_m_x_chat_service_listener.md#function-onstatuschanged)**(BMXMessagePtr msg, BMXErrorCode error)<br>Messaging state changed  |
| virtual void | **[onAttachmentUploadProgressChanged](classfloo_1_1_b_m_x_chat_service_listener.md#function-onattachmentuploadprogresschanged)**(BMXMessagePtr msg, int percent)<br>Attachment upload state changed  |
| virtual void | **[onRecallStatusChanged](classfloo_1_1_b_m_x_chat_service_listener.md#function-onrecallstatuschanged)**(BMXMessagePtr msg, BMXErrorCode error)<br>Message recall state changed  |
| virtual void | **[onReceive](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceive)**(const BMXMessageList & list)<br>Message received  |
| virtual void | **[onReceiveCommandMessages](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivecommandmessages)**(const BMXMessageList & list)<br>Command received  |
| virtual void | **[onReceiveSystemMessages](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivesystemmessages)**(const BMXMessageList & list)<br>System notification message received  |
| virtual void | **[onReceiveReadAcks](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivereadacks)**(const BMXMessageList & list)<br>Receipt of message read received  |
| virtual void | **[onReceiveDeliverAcks](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivedeliveracks)**(const BMXMessageList & list)<br>Receipt of message delivered received  |
| virtual void | **[onReceiveRecallMessages](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceiverecallmessages)**(const BMXMessageList & list)<br>Canceled message received  |
| virtual void | **[onReceiveReadCancels](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivereadcancels)**(const BMXMessageList & list)<br>Message re-unread received (cross-device synchronization for changing message status into unread)  |
| virtual void | **[onReceiveReadAllMessages](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivereadallmessages)**(const BMXMessageList & list)<br>All received messages are read (all messages are set to read before cross-device synchronization)  |
| virtual void | **[onReceiveDeleteMessages](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivedeletemessages)**(const BMXMessageList & list)<br>Deletion received (delete messages cross devices synchronously)  |
| virtual void | **[onReceivePlayAcks](classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceiveplayacks)**(const BMXMessageList & list)<br>Received receipt of audio/video message playback  |
| virtual void | **[onAttachmentStatusChanged](classfloo_1_1_b_m_x_chat_service_listener.md#function-onattachmentstatuschanged)**(BMXMessagePtr msg, BMXErrorCode error, int percent)<br>Attachment download state changed  |
| virtual void | **[onAttachmentDownloadByUrlStatusChanged](classfloo_1_1_b_m_x_chat_service_listener.md#function-onattachmentdownloadbyurlstatuschanged)**(int64_t msgId, BMXErrorCode error, int percent)<br>Attachment download state changed  |
| virtual void | **[onRetrieveHistoryMessages](classfloo_1_1_b_m_x_chat_service_listener.md#function-onretrievehistorymessages)**(BMXConversationPtr conversation)<br>Pull message history  |
| virtual void | **[onLoadAllConversation](classfloo_1_1_b_m_x_chat_service_listener.md#function-onloadallconversation)**()<br>List of unread conversations has been loaded  |
| virtual void | **[onConversationCreate](classfloo_1_1_b_m_x_chat_service_listener.md#function-onconversationcreate)**(BMXConversationPtr conversation, BMXMessagePtr msg)<br>Create a new conversation locally  |
| virtual void | **[onConversationDelete](classfloo_1_1_b_m_x_chat_service_listener.md#function-onconversationdelete)**(int64_t conversationId, BMXErrorCode error)<br>Delete conversation  |
| virtual void | **[onTotalUnreadCountChanged](classfloo_1_1_b_m_x_chat_service_listener.md#function-ontotalunreadcountchanged)**(int unreadCount)<br>Update total unread-number  |
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

### function ~BMXChatServiceListener

```cpp
inline virtual ~BMXChatServiceListener()
```

Destructor 

### function onStatusChanged

```cpp
inline virtual void onStatusChanged(
    BMXMessagePtr msg,
    BMXErrorCode error
)
```

Messaging state changed 

**Parameters**: 

  * **msg** Message with state changed 
  * **error** State error code 


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


### function onReceive

```cpp
inline virtual void onReceive(
    const BMXMessageList & list
)
```

Message received 

**Parameters**: 

  * **list** List of received messages 


### function onReceiveCommandMessages

```cpp
inline virtual void onReceiveCommandMessages(
    const BMXMessageList & list
)
```

Command received 

**Parameters**: 

  * **list** List of received messages 


### function onReceiveSystemMessages

```cpp
inline virtual void onReceiveSystemMessages(
    const BMXMessageList & list
)
```

System notification message received 

**Parameters**: 

  * **list** List of received system messages 


### function onReceiveReadAcks

```cpp
inline virtual void onReceiveReadAcks(
    const BMXMessageList & list
)
```

Receipt of message read received 

**Parameters**: 

  * **list** List of received messages with read receipt 


### function onReceiveDeliverAcks

```cpp
inline virtual void onReceiveDeliverAcks(
    const BMXMessageList & list
)
```

Receipt of message delivered received 

**Parameters**: 

  * **list** List of received messages with delivered receipt 


### function onReceiveRecallMessages

```cpp
inline virtual void onReceiveRecallMessages(
    const BMXMessageList & list
)
```

Canceled message received 

**Parameters**: 

  * **list** List of canceled messages received 


### function onReceiveReadCancels

```cpp
inline virtual void onReceiveReadCancels(
    const BMXMessageList & list
)
```

Message re-unread received (cross-device synchronization for changing message status into unread) 

**Parameters**: 

  * **list** List of received messages with re-unread receipt 


### function onReceiveReadAllMessages

```cpp
inline virtual void onReceiveReadAllMessages(
    const BMXMessageList & list
)
```

All received messages are read (all messages are set to read before cross-device synchronization) 

**Parameters**: 

  * **list** List of received messages with all-read receipt 


### function onReceiveDeleteMessages

```cpp
inline virtual void onReceiveDeleteMessages(
    const BMXMessageList & list
)
```

Deletion received (delete messages cross devices synchronously) 

**Parameters**: 

  * **list** List of deleted messages received 


### function onReceivePlayAcks

```cpp
inline virtual void onReceivePlayAcks(
    const BMXMessageList & list
)
```

Received receipt of audio/video message playback 

**Parameters**: 

  * **list** List of received audio/video messages with playback receipt 


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


### function onRetrieveHistoryMessages

```cpp
inline virtual void onRetrieveHistoryMessages(
    BMXConversationPtr conversation
)
```

Pull message history 

**Parameters**: 

  * **conversation** Conversation for which a specific message history was pulled 


### function onLoadAllConversation

```cpp
inline virtual void onLoadAllConversation()
```

List of unread conversations has been loaded 

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


### function onConversationDelete

```cpp
inline virtual void onConversationDelete(
    int64_t conversationId,
    BMXErrorCode error
)
```

Delete conversation 

**Parameters**: 

  * **conversationId** Deleted local conversation id 
  * **error** State error code 


### function onTotalUnreadCountChanged

```cpp
inline virtual void onTotalUnreadCountChanged(
    int unreadCount
)
```

Update total unread-number 

**Parameters**: 

  * **unreadCount** Total number of local unread conversations 


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


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800