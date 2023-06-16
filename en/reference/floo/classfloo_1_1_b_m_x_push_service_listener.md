---
title: floo::BMXPushServiceListener

---

# floo::BMXPushServiceListener





## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXPushServiceListener](classfloo_1_1_b_m_x_push_service_listener.md#function-bmxpushservicelistener)**()<br>Constructor  |
| virtual | **[~BMXPushServiceListener](classfloo_1_1_b_m_x_push_service_listener.md#function-~bmxpushservicelistener)**()<br>Destructor  |
| virtual void | **[onPushStart](classfloo_1_1_b_m_x_push_service_listener.md#function-onpushstart)**(const std::string bmxToken)<br>Notification of push initialization complete.  |
| virtual void | **[onPushStop](classfloo_1_1_b_m_x_push_service_listener.md#function-onpushstop)**()<br>Notification of push feature stop.  |
| virtual void | **[onCertRetrieved](classfloo_1_1_b_m_x_push_service_listener.md#function-oncertretrieved)**(const std::string cert)<br>Get push certificate after push initialization.  |
| virtual void | **[onSetTags](classfloo_1_1_b_m_x_push_service_listener.md#function-onsettags)**(const std::string & operationId)<br>Set callback of user push success.  |
| virtual void | **[onGetTags](classfloo_1_1_b_m_x_push_service_listener.md#function-ongettags)**(const std::string & operationId)<br>Get callback of user push success.  |
| virtual void | **[onDeleteTags](classfloo_1_1_b_m_x_push_service_listener.md#function-ondeletetags)**(const std::string & operationId)<br>Delete callback of user push success.  |
| virtual void | **[onClearTags](classfloo_1_1_b_m_x_push_service_listener.md#function-oncleartags)**(const std::string & operationId)<br>Clear callback of user push success.  |
| virtual void | **[onReceivePush](classfloo_1_1_b_m_x_push_service_listener.md#function-onreceivepush)**(const BMXMessageList & list)<br>New push notification received.  |
| virtual void | **[onStatusChanged](classfloo_1_1_b_m_x_push_service_listener.md#function-onstatuschanged)**(BMXMessagePtr msg, BMXErrorCode error)<br>Send notification of push uplink message status change.  |
| void | **[registerPushService](classfloo_1_1_b_m_x_push_service_listener.md#function-registerpushservice)**([BMXPushService](classfloo_1_1_b_m_x_push_service.md) * service)<br>Register BMXPushService to which BMXPushServiceListener is bound (automatic registration in SDK)  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [BMXPushService](classfloo_1_1_b_m_x_push_service.md) * | **[mService](classfloo_1_1_b_m_x_push_service_listener.md#variable-mservice)**  |

## Public Functions Documentation

### function BMXPushServiceListener

```cpp
inline BMXPushServiceListener()
```

Constructor 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXPushServiceListener",function="BMXPushServiceListener" %}{% endlanying_code_snippet %}
```
### function ~BMXPushServiceListener

```cpp
inline virtual ~BMXPushServiceListener()
```

Destructor 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXPushServiceListener",function="~BMXPushServiceListener" %}{% endlanying_code_snippet %}
```
### function onPushStart

```cpp
inline virtual void onPushStart(
    const std::string bmxToken
)
```

Notification of push initialization complete. 

**Parameters**: 

  * **bmxToken** bmxToken used in current push 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXPushServiceListener",function="onPushStart" %}{% endlanying_code_snippet %}
```
### function onPushStop

```cpp
inline virtual void onPushStop()
```

Notification of push feature stop. 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXPushServiceListener",function="onPushStop" %}{% endlanying_code_snippet %}
```
### function onCertRetrieved

```cpp
inline virtual void onCertRetrieved(
    const std::string cert
)
```

Get push certificate after push initialization. 

**Parameters**: 

  * **cert** Push certificate obtained from server 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXPushServiceListener",function="onCertRetrieved" %}{% endlanying_code_snippet %}
```
### function onSetTags

```cpp
inline virtual void onSetTags(
    const std::string & operationId
)
```

Set callback of user push success. 

**Parameters**: 

  * **operationId** Operation id 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXPushServiceListener",function="onSetTags" %}{% endlanying_code_snippet %}
```
### function onGetTags

```cpp
inline virtual void onGetTags(
    const std::string & operationId
)
```

Get callback of user push success. 

**Parameters**: 

  * **operationId** Operation id 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXPushServiceListener",function="onGetTags" %}{% endlanying_code_snippet %}
```
### function onDeleteTags

```cpp
inline virtual void onDeleteTags(
    const std::string & operationId
)
```

Delete callback of user push success. 

**Parameters**: 

  * **operationId** Operation id 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXPushServiceListener",function="onDeleteTags" %}{% endlanying_code_snippet %}
```
### function onClearTags

```cpp
inline virtual void onClearTags(
    const std::string & operationId
)
```

Clear callback of user push success. 

**Parameters**: 

  * **operationId** Operation id 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXPushServiceListener",function="onClearTags" %}{% endlanying_code_snippet %}
```
### function onReceivePush

```cpp
inline virtual void onReceivePush(
    const BMXMessageList & list
)
```

New push notification received. 

**Parameters**: 

  * **list** Push notification list 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXPushServiceListener",function="onReceivePush" %}{% endlanying_code_snippet %}
```
### function onStatusChanged

```cpp
inline virtual void onStatusChanged(
    BMXMessagePtr msg,
    BMXErrorCode error
)
```

Send notification of push uplink message status change. 

**Parameters**: 

  * **msg** Uplink message with state change 
  * **error** State error code 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXPushServiceListener",function="onStatusChanged" %}{% endlanying_code_snippet %}
```
### function registerPushService

```cpp
inline void registerPushService(
    BMXPushService * service
)
```

Register BMXPushService to which BMXPushServiceListener is bound (automatic registration in SDK) 

**Parameters**: 

  * **service** [BMXPushService](classfloo_1_1_b_m_x_push_service.md)


## Protected Attributes Documentation

### variable mService

```cpp
BMXPushService * mService;
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXPushServiceListener",function="registerPushService" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800