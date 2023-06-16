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


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushServiceListener",function="delete" %}{% endlanying_code_snippet %}
```
### function swigReleaseOwnership

```java
inline void swigReleaseOwnership()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushServiceListener",function="swigReleaseOwnership" %}{% endlanying_code_snippet %}
```
### function swigTakeOwnership

```java
inline void swigTakeOwnership()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushServiceListener",function="swigTakeOwnership" %}{% endlanying_code_snippet %}
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


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushServiceListener",function="onPushStart" %}{% endlanying_code_snippet %}
```
### function onPushStop

```java
inline void onPushStop()
```

Notification of push feature stop. 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushServiceListener",function="onPushStop" %}{% endlanying_code_snippet %}
```
### function onCertRetrieved

```java
inline void onCertRetrieved(
    String cert
)
```

Get push certificate after push initialization. 

**Parameters**: 

  * **cert** Push certificate obtained from server 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushServiceListener",function="onCertRetrieved" %}{% endlanying_code_snippet %}
```
### function onSetTags

```java
inline void onSetTags(
    String operationId
)
```

Set callback of user push success. 

**Parameters**: 

  * **operationId** Operation id 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushServiceListener",function="onSetTags" %}{% endlanying_code_snippet %}
```
### function onGetTags

```java
inline void onGetTags(
    String operationId
)
```

Get callback of user push success. 

**Parameters**: 

  * **operationId** Operation id 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushServiceListener",function="onGetTags" %}{% endlanying_code_snippet %}
```
### function onDeleteTags

```java
inline void onDeleteTags(
    String operationId
)
```

Delete callback of user push success. 

**Parameters**: 

  * **operationId** Operation id 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushServiceListener",function="onDeleteTags" %}{% endlanying_code_snippet %}
```
### function onClearTags

```java
inline void onClearTags(
    String operationId
)
```

Clear callback of user push success. 

**Parameters**: 

  * **operationId** Operation id 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushServiceListener",function="onClearTags" %}{% endlanying_code_snippet %}
```
### function onReceivePush

```java
inline void onReceivePush(
    BMXMessageList list
)
```

New push notification received. 

**Parameters**: 

  * **list** Push notification list 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushServiceListener",function="onReceivePush" %}{% endlanying_code_snippet %}
```
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


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushServiceListener",function="onStatusChanged" %}{% endlanying_code_snippet %}
```
### function BMXPushServiceListener

```java
inline BMXPushServiceListener()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushServiceListener",function="BMXPushServiceListener" %}{% endlanying_code_snippet %}
```
### function registerPushService

```java
inline void registerPushService(
    BMXPushService service
)
```


## Protected Functions Documentation

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushServiceListener",function="registerPushService" %}{% endlanying_code_snippet %}
```
### function BMXPushServiceListener

```java
inline BMXPushServiceListener(
    long cPtr,
    boolean cMemoryOwn
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushServiceListener",function="BMXPushServiceListener" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushServiceListener",function="finalize" %}{% endlanying_code_snippet %}
```
### function swigDirectorDisconnect

```java
inline void swigDirectorDisconnect()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushServiceListener",function="swigDirectorDisconnect" %}{% endlanying_code_snippet %}
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


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushServiceListener",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800