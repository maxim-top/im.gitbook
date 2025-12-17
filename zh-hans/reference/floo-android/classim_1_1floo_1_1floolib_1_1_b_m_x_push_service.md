---
title: im::floo::floolib::BMXPushService
---

# im::floo::floolib::BMXPushService

## Public Functions

|                              | Name                                                                                                                                                                                                                                                                                                         |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| synchronized void            | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-delete)()                                                                                                                                                                                                                         |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-start"><strong>start</strong></a>(String alias, String bmxToken)<br>初始化推送sdk。在仅使用推送的情况下使用该接口初始化推送sdk。在同时使用IM功能的时候直接在BMXClient调用登陆功能即可。config对象初始化的时候需要传入平台类型和设备id。</p>                                                             |
| \[BMXErrorCode]              | [**start**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-start)(String alias)                                                                                                                                                                                                               |
| \[BMXErrorCode]              | [**start**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-start)()                                                                                                                                                                                                                           |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-stop"><strong>stop</strong></a>()<br>停止推送功能接口。</p>                                                                                                                                                                                 |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-resume"><strong>resume</strong></a>()<br>恢复推送功能接口。</p>                                                                                                                                                                             |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-unbindalias"><strong>unbindAlias</strong></a>(String alias)<br>解除用户别名绑定。</p>                                                                                                                                                       |
| String                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-gettoken"><strong>getToken</strong></a>()<br>获取登陆后使用的用户token。</p>                                                                                                                                                                  |
| String                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-getcert"><strong>getCert</strong></a>()<br>获取登陆后服务器返回的推送证书。</p>                                                                                                                                                                    |
| BMXPushService.PushSdkStatus | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-status"><strong>status</strong></a>()<br>推送sdk当前的状态。</p>                                                                                                                                                                           |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-binddevicetoken"><strong>bindDeviceToken</strong></a>(String token)<br>推送绑定设备token。</p>                                                                                                                                            |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-bindvoiptoken"><strong>bindVoipToken</strong></a>(String token)<br>绑定推送设备的voiptoken。</p>                                                                                                                                           |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-getpushprofile"><strong>getPushProfile</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_user_profile.md">BMXPushUserProfile</a> pushProfile, boolean forceRefresh)<br>获取推送用户详情，如果forceRefresh == true，则强制从服务端拉取</p> |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-settags"><strong>setTags</strong></a>(TagList tags, String operationId)<br>设置推送用户的标签。</p>                                                                                                                                          |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-gettags"><strong>getTags</strong></a>(TagList tags, String operationId)<br>获取推送用户的标签。</p>                                                                                                                                          |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-deletetags"><strong>deleteTags</strong></a>(TagList tags, String operationId)<br>删除推送用户的标签。</p>                                                                                                                                    |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-cleartags"><strong>clearTags</strong></a>(String operationId)<br>清空推送用户的标签。</p>                                                                                                                                                    |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setbadge"><strong>setBadge</strong></a>(int count)<br>设置推送用户的未读角标。</p>                                                                                                                                                             |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setpushmode"><strong>setPushMode</strong></a>(boolean enable)<br>设置推送启用状态。默认为使用推送。</p>                                                                                                                                             |
| \[BMXErrorCode]              | [**setPushMode**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setpushmode)()                                                                                                                                                                                                               |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setpushtime"><strong>setPushTime</strong></a>(int startHour, int endHour)<br>设置允许推送时间。</p>                                                                                                                                         |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setsilencetime"><strong>setSilenceTime</strong></a>(int startHour, int endHour)<br>设置推送静默的起始结束时间。</p>                                                                                                                              |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setrunbackgroundmode"><strong>setRunBackgroundMode</strong></a>(boolean enable)<br>设置推送是否可以后台运行。默认是false。</p>                                                                                                                      |
| \[BMXErrorCode]              | [**setRunBackgroundMode**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setrunbackgroundmode)()                                                                                                                                                                                             |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setgeofencemode"><strong>setGeoFenceMode</strong></a>(boolean enable, boolean isAllow)<br>设置推送的地理围栏功能是否运行。</p>                                                                                                                     |
| \[BMXErrorCode]              | [**setGeoFenceMode**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setgeofencemode)(boolean enable)                                                                                                                                                                                         |
| \[BMXErrorCode]              | [**setGeoFenceMode**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setgeofencemode)()                                                                                                                                                                                                       |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-clearnotification"><strong>clearNotification</strong></a>(long notificationId)<br>清除指定id的通知。</p>                                                                                                                                   |
| void                         | [**clearAllNotifications**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-clearallnotifications)()                                                                                                                                                                                           |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-sendmessage"><strong>sendMessage</strong></a>(String content)<br>发送推送上行消息，消息状态变化会通过listener通知</p>                                                                                                                                  |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-loadlocalpushmessages"><strong>loadLocalPushMessages</strong></a>(long refMsgId, long size, BMXMessageList result, BMXPushService.PushDirection arg3)<br>加载数据库本地存储的推送消息。如果不指定则从最新消息开始</p>                                          |
| \[BMXErrorCode]              | [**loadLocalPushMessages**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-loadlocalpushmessages)(long refMsgId, long size, BMXMessageList result)                                                                                                                                            |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-addpushlistener"><strong>addPushListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md">BMXPushServiceListener</a> listener)<br>添加推送监听者</p>                                                  |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-removepushlistener"><strong>removePushListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md">BMXPushServiceListener</a> listener)<br>移除推送监听者</p>                                            |

## Protected Functions

|      | Name                                                                                                                                                             |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXPushService**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-bmxpushservice)(long cPtr, boolean cMemoryOwn)                                |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-finalize)()                                                                         |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-getcptr)([BMXPushService](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md) obj) |

## Protected Attributes

|                   | Name                                                                                         |
| ----------------- | -------------------------------------------------------------------------------------------- |
| transient boolean | [**swigCMemOwn**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#variable-swigcmemown) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function start

```java
inline BMXErrorCode start(
    String alias,
    String bmxToken
)
```

初始化推送sdk。在仅使用推送的情况下使用该接口初始化推送sdk。在同时使用IM功能的时候直接在BMXClient调用登陆功能即可。config对象初始化的时候需要传入平台类型和设备id。

**Parameters**:

* **alias** 推送初始化使用的当前用户别名
* **bmxToken** 推送初始化的时候App传入的使用的用户的token，无用户的状态下不传入即可。

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function start

```java
inline BMXErrorCode start(
    String alias
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function start

```java
inline BMXErrorCode start()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function stop

```java
inline BMXErrorCode stop()
```

停止推送功能接口。

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function resume

```java
inline BMXErrorCode resume()
```

恢复推送功能接口。

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function unbindAlias

```java
inline BMXErrorCode unbindAlias(
    String alias
)
```

解除用户别名绑定。

**Parameters**:

* **alias** 需要解除绑定的用户别名。

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function getToken

```java
inline String getToken()
```

获取登陆后使用的用户token。

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function getCert

```java
inline String getCert()
```

获取登陆后服务器返回的推送证书。

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function status

```java
inline BMXPushService.PushSdkStatus status()
```

推送sdk当前的状态。

**Return**: \[PushSdkStatus]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function bindDeviceToken

```java
inline BMXErrorCode bindDeviceToken(
    String token
)
```

推送绑定设备token。

**Parameters**:

* **token** 设备的推送token

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function bindVoipToken

```java
inline BMXErrorCode bindVoipToken(
    String token
)
```

绑定推送设备的voiptoken。

**Parameters**:

* **token** 设备的voip推送token

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function getPushProfile

```java
inline BMXErrorCode getPushProfile(
    BMXPushUserProfile pushProfile,
    boolean forceRefresh
)
```

获取推送用户详情，如果forceRefresh == true，则强制从服务端拉取

**Parameters**:

* **pushProfile** 推送用户profile信息，初始传入指向为空的shared\_ptr对象，函数返回后从此处获取用户profile信息。
* **forceRefresh** 是否强制从服务器拉取，本地获取失败的情况下会自动从服务器拉取

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function setTags

```java
inline BMXErrorCode setTags(
    TagList tags,
    String operationId
)
```

设置推送用户的标签。

**Parameters**:

* **tags** 用户标签
* **operationId** 操作id。在回调通知中对应通知提醒。

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function getTags

```java
inline BMXErrorCode getTags(
    TagList tags,
    String operationId
)
```

获取推送用户的标签。

**Parameters**:

* **tags** 用户标签
* **operationId** 操作id。在回调通知中对应通知提醒。

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function deleteTags

```java
inline BMXErrorCode deleteTags(
    TagList tags,
    String operationId
)
```

删除推送用户的标签。

**Parameters**:

* **tags** 要删除用户标签
* **operationId** 操作id。在回调通知中对应通知提醒。

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function clearTags

```java
inline BMXErrorCode clearTags(
    String operationId
)
```

清空推送用户的标签。

**Parameters**:

* **operationId** 操作id。在回调通知中对应通知提醒。

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function setBadge

```java
inline BMXErrorCode setBadge(
    int count
)
```

设置推送用户的未读角标。

**Parameters**:

* **count** 用户未读角标数

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function setPushMode

```java
inline BMXErrorCode setPushMode(
    boolean enable
)
```

设置推送启用状态。默认为使用推送。

**Parameters**:

* **enable** 推送的启用状态

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function setPushMode

```java
inline BMXErrorCode setPushMode()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function setPushTime

```java
inline BMXErrorCode setPushTime(
    int startHour,
    int endHour
)
```

设置允许推送时间。

**Parameters**:

* **startHour** 静默允许推送的起始时间小时
* **endHour** 静默允许推送的结束时间小时

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function setSilenceTime

```java
inline BMXErrorCode setSilenceTime(
    int startHour,
    int endHour
)
```

设置推送静默的起始结束时间。

**Parameters**:

* **startHour** 静默推送的起始时间小时
* **endHour** 静默推送的结束时间小时

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function setRunBackgroundMode

```java
inline BMXErrorCode setRunBackgroundMode(
    boolean enable
)
```

设置推送是否可以后台运行。默认是false。

**Parameters**:

* **enable** 推送后台运行状态。

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function setRunBackgroundMode

```java
inline BMXErrorCode setRunBackgroundMode()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function setGeoFenceMode

```java
inline BMXErrorCode setGeoFenceMode(
    boolean enable,
    boolean isAllow
)
```

设置推送的地理围栏功能是否运行。

**Parameters**:

* **enable** 地理围栏功能是否运行。
* **isAllow** 用户是否主动弹出用户定位请求。

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function setGeoFenceMode

```java
inline BMXErrorCode setGeoFenceMode(
    boolean enable
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function setGeoFenceMode

```java
inline BMXErrorCode setGeoFenceMode()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function clearNotification

```java
inline void clearNotification(
    long notificationId
)
```

清除指定id的通知。

**Parameters**:

* **notificationId** 通知id

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function clearAllNotifications

```java
inline void clearAllNotifications()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function sendMessage

```java
inline void sendMessage(
    String content
)
```

发送推送上行消息，消息状态变化会通过listener通知

**Parameters**:

* **content** 发送的上行推送消息内容

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function loadLocalPushMessages

```java
inline BMXErrorCode loadLocalPushMessages(
    long refMsgId,
    long size,
    BMXMessageList result,
    BMXPushService.PushDirection arg3
)
```

加载数据库本地存储的推送消息。如果不指定则从最新消息开始

**Parameters**:

* **refMsgId** 加载推送消息的起始id
* **size** 最大加载消息条数
* **result** 数据库返回的加载本地推送消息列表
* **arg3** 加载推送消息的方向，默认是加载更早的消息

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function loadLocalPushMessages

```java
inline BMXErrorCode loadLocalPushMessages(
    long refMsgId,
    long size,
    BMXMessageList result
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function addPushListener

```java
inline void addPushListener(
    BMXPushServiceListener listener
)
```

添加推送监听者

**Parameters**:

* **listener** 推送监听者

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function removePushListener

```java
inline void removePushListener(
    BMXPushServiceListener listener
)
```

移除推送监听者

**Parameters**:

* **listener** 推送监听者

## Protected Functions Documentation

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function BMXPushService

```java
inline BMXPushService(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function finalize

```java
inline void finalize()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function getCPtr

```java
static inline long getCPtr(
    BMXPushService obj
)
```

## Protected Attributes Documentation

### variable swigCMemOwn

```java
transient boolean swigCMemOwn;
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>
```

***

Updated on 2022-01-26 at 17:18:31 +0800
