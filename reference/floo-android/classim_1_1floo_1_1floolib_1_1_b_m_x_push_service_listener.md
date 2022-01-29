---
title: im::floo::floolib::BMXPushServiceListener

---

# im::floo::floolib::BMXPushServiceListener





## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-delete)**() |
| void | **[swigReleaseOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-swigreleaseownership)**() |
| void | **[swigTakeOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-swigtakeownership)**() |
| void | **[onPushStart](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onpushstart)**(String bmxToken)<br>Notification of push initialization complete.  |
| void | **[onPushStop](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onpushstop)**()<br>Notification of push feature stop.  |
| void | **[onCertRetrieved](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-oncertretrieved)**(String cert)<br>Get push certificate after push initialization.  |
| void | **[onSetTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onsettags)**(String operationId)<br>Set callback of user push success.  |
| void | **[onGetTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-ongettags)**(String operationId)<br>Get callback of user push success.  |
| void | **[onDeleteTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-ondeletetags)**(String operationId)<br>Delete callback of user push success.  |
| void | **[onClearTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-oncleartags)**(String operationId)<br>Clear callback of user push success.  |
| void | **[onReceivePush](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onreceivepush)**(BMXMessageList list)<br>New push notification received.  |
| void | **[onStatusChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onstatuschanged)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, [BMXErrorCode] error)<br>Send notification of push uplink message status change.  |
| | **[BMXPushServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-bmxpushservicelistener)**() |
| void | **[registerPushService](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-registerpushservice)**([BMXPushService](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md) service) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXPushServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-bmxpushservicelistener)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-finalize)**() |
| void | **[swigDirectorDisconnect](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-swigdirectordisconnect)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-getcptr)**([BMXPushServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md) obj) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| transient boolean | **[swigCMemOwn](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#variable-swigcmemown)**  |

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


### function onPushStart

```java
inline void onPushStart(
    String bmxToken
)
```

Notification of push initialization complete. 

**Parameters**: 

  * **bmxToken** bmxToken used in current push 


### function onPushStop

```java
inline void onPushStop()
```

Notification of push feature stop. 

### function onCertRetrieved

```java
inline void onCertRetrieved(
    String cert
)
```

Get push certificate after push initialization. 

**Parameters**: 

  * **cert** Push certificate obtained from server 


### function onSetTags

```java
inline void onSetTags(
    String operationId
)
```

Set callback of user push success. 

**Parameters**: 

  * **operationId** Operation id 


### function onGetTags

```java
inline void onGetTags(
    String operationId
)
```

Get callback of user push success. 

**Parameters**: 

  * **operationId** Operation id 


### function onDeleteTags

```java
inline void onDeleteTags(
    String operationId
)
```

Delete callback of user push success. 

**Parameters**: 

  * **operationId** Operation id 


### function onClearTags

```java
inline void onClearTags(
    String operationId
)
```

Clear callback of user push success. 

**Parameters**: 

  * **operationId** Operation id 


### function onReceivePush

```java
inline void onReceivePush(
    BMXMessageList list
)
```

New push notification received. 

**Parameters**: 

  * **list** Push notification list 


### function onStatusChanged

```java
inline void onStatusChanged(
    BMXMessage msg,
    BMXErrorCode error
)
```

Send notification of push uplink message status change. 

**Parameters**: 

  * **msg** Uplink message with state change 
  * **error** State error code 


### function BMXPushServiceListener

```java
inline BMXPushServiceListener()
```


### function registerPushService

```java
inline void registerPushService(
    BMXPushService service
)
```


## Protected Functions Documentation

### function BMXPushServiceListener

```java
inline BMXPushServiceListener(
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
    BMXPushServiceListener obj
)
```


## Protected Attributes Documentation

### variable swigCMemOwn

```java
transient boolean swigCMemOwn;
```


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800