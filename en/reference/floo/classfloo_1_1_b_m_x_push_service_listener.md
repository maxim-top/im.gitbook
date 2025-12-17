---
title: floo::BMXPushServiceListener
---

# floo::BMXPushServiceListener

## Public Functions

|              | Name                                                                                                                                                                                                                                                                                                                |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-bmxpushservicelistener"><strong>BMXPushServiceListener</strong></a>()<br>Constructor</p>                                                                                                                                                          |
| virtual      | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-~bmxpushservicelistener"><strong>~BMXPushServiceListener</strong></a>()<br>Destructor</p>                                                                                                                                                         |
| virtual void | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-onpushstart"><strong>onPushStart</strong></a>(const std::string bmxToken)<br>Notification of push initialization complete.</p>                                                                                                                    |
| virtual void | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-onpushstop"><strong>onPushStop</strong></a>()<br>Notification of push feature stop.</p>                                                                                                                                                           |
| virtual void | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-oncertretrieved"><strong>onCertRetrieved</strong></a>(const std::string cert)<br>Get push certificate after push initialization.</p>                                                                                                              |
| virtual void | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-onsettags"><strong>onSetTags</strong></a>(const std::string &#x26; operationId)<br>Set callback of user push success.</p>                                                                                                                         |
| virtual void | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-ongettags"><strong>onGetTags</strong></a>(const std::string &#x26; operationId)<br>Get callback of user push success.</p>                                                                                                                         |
| virtual void | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-ondeletetags"><strong>onDeleteTags</strong></a>(const std::string &#x26; operationId)<br>Delete callback of user push success.</p>                                                                                                                |
| virtual void | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-oncleartags"><strong>onClearTags</strong></a>(const std::string &#x26; operationId)<br>Clear callback of user push success.</p>                                                                                                                   |
| virtual void | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-onreceivepush"><strong>onReceivePush</strong></a>(const BMXMessageList &#x26; list)<br>New push notification received.</p>                                                                                                                        |
| virtual void | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-onstatuschanged"><strong>onStatusChanged</strong></a>(BMXMessagePtr msg, BMXErrorCode error)<br>Send notification of push uplink message status change.</p>                                                                                       |
| void         | <p><a href="classfloo_1_1_b_m_x_push_service_listener.md#function-registerpushservice"><strong>registerPushService</strong></a>(<a href="classfloo_1_1_b_m_x_push_service.md">BMXPushService</a> * service)<br>Register BMXPushService to which BMXPushServiceListener is bound (automatic registration in SDK)</p> |

## Protected Attributes

|                                                          | Name                                                                           |
| -------------------------------------------------------- | ------------------------------------------------------------------------------ |
| [BMXPushService](classfloo_1_1_b_m_x_push_service.md) \* | [**mService**](classfloo_1_1_b_m_x_push_service_listener.md#variable-mservice) |

## Public Functions Documentation

### function BMXPushServiceListener

```cpp
inline BMXPushServiceListener()
```

Constructor

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

```

### function \~BMXPushServiceListener

```cpp
inline virtual ~BMXPushServiceListener()
```

Destructor

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

```

### function onPushStop

```cpp
inline virtual void onPushStop()
```

Notification of push feature stop.

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushServiceListener'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
