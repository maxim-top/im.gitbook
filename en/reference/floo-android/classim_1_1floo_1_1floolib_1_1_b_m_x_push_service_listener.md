---
title: im::floo::floolib::BMXPushServiceListener
---

# im::floo::floolib::BMXPushServiceListener

## Public Functions

|                   | Name                                                                                                                                                                                                                                                                                                        |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-delete)()                                                                                                                                                                                                               |
| void              | [**swigReleaseOwnership**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-swigreleaseownership)()                                                                                                                                                                                   |
| void              | [**swigTakeOwnership**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-swigtakeownership)()                                                                                                                                                                                         |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onpushstart"><strong>onPushStart</strong></a>(String bmxToken)<br>Notification of push initialization complete.</p>                                                                                                      |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onpushstop"><strong>onPushStop</strong></a>()<br>Notification of push feature stop.</p>                                                                                                                                  |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-oncertretrieved"><strong>onCertRetrieved</strong></a>(String cert)<br>Get push certificate after push initialization.</p>                                                                                                |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onsettags"><strong>onSetTags</strong></a>(String operationId)<br>Set callback of user push success.</p>                                                                                                                  |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-ongettags"><strong>onGetTags</strong></a>(String operationId)<br>Get callback of user push success.</p>                                                                                                                  |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-ondeletetags"><strong>onDeleteTags</strong></a>(String operationId)<br>Delete callback of user push success.</p>                                                                                                         |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-oncleartags"><strong>onClearTags</strong></a>(String operationId)<br>Clear callback of user push success.</p>                                                                                                            |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onreceivepush"><strong>onReceivePush</strong></a>(BMXMessageList list)<br>New push notification received.</p>                                                                                                            |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onstatuschanged"><strong>onStatusChanged</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, [BMXErrorCode] error)<br>Send notification of push uplink message status change.</p> |
|                   | [**BMXPushServiceListener**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-bmxpushservicelistener)()                                                                                                                                                                               |
| void              | [**registerPushService**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-registerpushservice)([BMXPushService](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md) service)                                                                                                       |

## Protected Functions

|      | Name                                                                                                                                                                                       |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|      | [**BMXPushServiceListener**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-bmxpushservicelistener)(long cPtr, boolean cMemoryOwn)                                 |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-finalize)()                                                                                          |
| void | [**swigDirectorDisconnect**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-swigdirectordisconnect)()                                                              |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-getcptr)([BMXPushServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md) obj) |

## Protected Attributes

|                   | Name                                                                                                  |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| transient boolean | [**swigCMemOwn**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#variable-swigcmemown) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>

```

### function swigReleaseOwnership

```java
inline void swigReleaseOwnership()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>

```

### function swigTakeOwnership

```java
inline void swigTakeOwnership()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>

```

### function onPushStop

```java
inline void onPushStop()
```

Notification of push feature stop.

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>

```

### function BMXPushServiceListener

```java
inline BMXPushServiceListener()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>

```

### function finalize

```java
inline void finalize()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>

```

### function swigDirectorDisconnect

```java
inline void swigDirectorDisconnect()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>
```

***

Updated on 2022-01-26 at 17:18:31 +0800
