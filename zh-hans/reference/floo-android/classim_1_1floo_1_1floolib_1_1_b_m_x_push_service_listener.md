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
| void | **[onPushStart](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onpushstart)**(String bmxToken)<br>Push初始化完成通知。  |
| void | **[onPushStop](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onpushstop)**()<br>Push功能停止通知。  |
| void | **[onCertRetrieved](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-oncertretrieved)**(String cert)<br>Push初始化完成后获取推送证书。  |
| void | **[onSetTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onsettags)**(String operationId)<br>设置用户推送成功回调。  |
| void | **[onGetTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-ongettags)**(String operationId)<br>获取用户推送成功回调。  |
| void | **[onDeleteTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-ondeletetags)**(String operationId)<br>删除用户推送成功回调。  |
| void | **[onClearTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-oncleartags)**(String operationId)<br>清空用户推送成功回调。  |
| void | **[onReceivePush](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onreceivepush)**(BMXMessageList list)<br>接收到新的Push通知。  |
| void | **[onStatusChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onstatuschanged)**([BMXMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message.md) msg, [BMXErrorCode] error)<br>发送Push上行消息状态变化通知。  |
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

Push初始化完成通知。 

**Parameters**: 

  * **bmxToken** 当前push使用bmxToken 


### function onPushStop

```java
inline void onPushStop()
```

Push功能停止通知。 

### function onCertRetrieved

```java
inline void onCertRetrieved(
    String cert
)
```

Push初始化完成后获取推送证书。 

**Parameters**: 

  * **cert** 从服务器获取的推送证书 


### function onSetTags

```java
inline void onSetTags(
    String operationId
)
```

设置用户推送成功回调。 

**Parameters**: 

  * **operationId** 操作id 


### function onGetTags

```java
inline void onGetTags(
    String operationId
)
```

获取用户推送成功回调。 

**Parameters**: 

  * **operationId** 操作id 


### function onDeleteTags

```java
inline void onDeleteTags(
    String operationId
)
```

删除用户推送成功回调。 

**Parameters**: 

  * **operationId** 操作id 


### function onClearTags

```java
inline void onClearTags(
    String operationId
)
```

清空用户推送成功回调。 

**Parameters**: 

  * **operationId** 操作id 


### function onReceivePush

```java
inline void onReceivePush(
    BMXMessageList list
)
```

接收到新的Push通知。 

**Parameters**: 

  * **list** Push通知列表 


### function onStatusChanged

```java
inline void onStatusChanged(
    BMXMessage msg,
    BMXErrorCode error
)
```

发送Push上行消息状态变化通知。 

**Parameters**: 

  * **msg** 发生状态变化的上行消息 
  * **error** 状态错误码 


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