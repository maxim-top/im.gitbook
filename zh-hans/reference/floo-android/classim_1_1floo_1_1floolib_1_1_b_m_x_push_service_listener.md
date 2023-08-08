---
title: im::floo::floolib::BMXPushServiceListener
---

# im::floo::floolib::BMXPushServiceListener

## Public Functions

|                   | Name                                                                                                                                                                                                                                                                  |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_service\_listener.md#function-delete)()                                                                                                                                                             |
| void              | [**swigReleaseOwnership**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_service\_listener.md#function-swigreleaseownership)()                                                                                                                                 |
| void              | [**swigTakeOwnership**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_service\_listener.md#function-swigtakeownership)()                                                                                                                                       |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onpushstart"><strong>onPushStart</strong></a>(String bmxToken)<br>Push初始化完成通知。</p>                                                                                                 |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onpushstop"><strong>onPushStop</strong></a>()<br>Push功能停止通知。</p>                                                                                                                   |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-oncertretrieved"><strong>onCertRetrieved</strong></a>(String cert)<br>Push初始化完成后获取推送证书。</p>                                                                                        |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onsettags"><strong>onSetTags</strong></a>(String operationId)<br>设置用户推送成功回调。</p>                                                                                                   |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-ongettags"><strong>onGetTags</strong></a>(String operationId)<br>获取用户推送成功回调。</p>                                                                                                   |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-ondeletetags"><strong>onDeleteTags</strong></a>(String operationId)<br>删除用户推送成功回调。</p>                                                                                             |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-oncleartags"><strong>onClearTags</strong></a>(String operationId)<br>清空用户推送成功回调。</p>                                                                                               |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onreceivepush"><strong>onReceivePush</strong></a>(BMXMessageList list)<br>接收到新的Push通知。</p>                                                                                         |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md#function-onstatuschanged"><strong>onStatusChanged</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message.md">BMXMessage</a> msg, [BMXErrorCode] error)<br>发送Push上行消息状态变化通知。</p> |
|                   | [**BMXPushServiceListener**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_service\_listener.md#function-bmxpushservicelistener)()                                                                                                                             |
| void              | [**registerPushService**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_service\_listener.md#function-registerpushservice)([BMXPushService](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_service.md) service)                                          |

## Protected Functions

|      | Name                                                                                                                                                                                                               |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|      | [**BMXPushServiceListener**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_service\_listener.md#function-bmxpushservicelistener)(long cPtr, boolean cMemoryOwn)                                             |
| void | [**finalize**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_service\_listener.md#function-finalize)()                                                                                                      |
| void | [**swigDirectorDisconnect**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_service\_listener.md#function-swigdirectordisconnect)()                                                                          |
| long | [**getCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_service\_listener.md#function-getcptr)([BMXPushServiceListener](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_service\_listener.md) obj) |

## Protected Attributes

|                   | Name                                                                                                              |
| ----------------- | ----------------------------------------------------------------------------------------------------------------- |
| transient boolean | [**swigCMemOwn**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_service\_listener.md#variable-swigcmemown) |

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

Push初始化完成通知。

**Parameters**:

* **bmxToken** 当前push使用bmxToken

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushServiceListener'></div>
```

### function onPushStop

```java
inline void onPushStop()
```

Push功能停止通知。

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

Push初始化完成后获取推送证书。

**Parameters**:

* **cert** 从服务器获取的推送证书

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

设置用户推送成功回调。

**Parameters**:

* **operationId** 操作id

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

获取用户推送成功回调。

**Parameters**:

* **operationId** 操作id

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

删除用户推送成功回调。

**Parameters**:

* **operationId** 操作id

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

清空用户推送成功回调。

**Parameters**:

* **operationId** 操作id

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

接收到新的Push通知。

**Parameters**:

* **list** Push通知列表

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

发送Push上行消息状态变化通知。

**Parameters**:

* **msg** 发生状态变化的上行消息
* **error** 状态错误码

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



Updated on 2022-01-26 at 17:18:31 +0800
