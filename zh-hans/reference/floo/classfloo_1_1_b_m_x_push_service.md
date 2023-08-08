---
title: floo::BMXPushService
---

# floo::BMXPushService

## Public Types

|            | Name                                                                                                                                                               |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| enum class | <p><a href="classfloo_1_1_b_m_x_push_service.md#enum-pushsdkstatus"><strong>PushSdkStatus</strong></a> { Starting = 1, Started, Stoped, Offline}<br>push sdk状态</p> |
| enum class | <p><a href="classfloo_1_1_b_m_x_push_service.md#enum-pushdirection"><strong>PushDirection</strong></a> { Up, Down}<br>本地推送消息搜索方向</p>                               |

## Public Functions

|                                                                                        | Name                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual                                                                                | [**\~BMXPushService**](classfloo\_1\_1\_b\_m\_x\_push\_service.md#function-\~bmxpushservice)()                                                                                                                                                                                                                                                                                                       |
| virtual BMXErrorCode                                                                   | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-start"><strong>start</strong></a>(const std::string &#x26; alias ="", const std::string &#x26; bmxToken ="") =0<br>初始化推送sdk。在仅使用推送的情况下使用该接口初始化推送sdk。在同时使用IM功能的时候直接在BMXClient调用登陆功能即可。config对象初始化的时候需要传入平台类型和设备id。</p>                                                                                                                       |
| virtual BMXErrorCode                                                                   | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-stop"><strong>stop</strong></a>() =0<br>停止推送功能接口。</p>                                                                                                                                                                                                                                                                                       |
| virtual BMXErrorCode                                                                   | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-resume"><strong>resume</strong></a>() =0<br>恢复推送功能接口。</p>                                                                                                                                                                                                                                                                                   |
| virtual BMXErrorCode                                                                   | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-unbindalias"><strong>unbindAlias</strong></a>(const std::string &#x26; alias) =0<br>解除用户别名绑定。</p>                                                                                                                                                                                                                                           |
| virtual const std::string &                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-gettoken"><strong>getToken</strong></a>() =0<br>获取登陆后使用的用户token。</p>                                                                                                                                                                                                                                                                        |
| virtual const std::string &                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-getcert"><strong>getCert</strong></a>() =0<br>获取登陆后服务器返回的推送证书。</p>                                                                                                                                                                                                                                                                          |
| virtual [PushSdkStatus](classfloo\_1\_1\_b\_m\_x\_push\_service.md#enum-pushsdkstatus) | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-status"><strong>status</strong></a>() =0<br>推送sdk当前的状态。</p>                                                                                                                                                                                                                                                                                 |
| virtual BMXErrorCode                                                                   | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-binddevicetoken"><strong>bindDeviceToken</strong></a>(const std::string &#x26; token) =0<br>推送绑定设备token。</p>                                                                                                                                                                                                                                |
| virtual BMXErrorCode                                                                   | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-bindvoiptoken"><strong>bindVoipToken</strong></a>(const std::string &#x26; token) =0<br>绑定推送设备的voiptoken。</p>                                                                                                                                                                                                                               |
| virtual BMXErrorCode                                                                   | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-getpushprofile"><strong>getPushProfile</strong></a>(BMXPushUserProfilePtr &#x26; pushProfile, bool forceRefresh) =0<br>获取推送用户详情，如果forceRefresh == true，则强制从服务端拉取</p>                                                                                                                                                                        |
| virtual BMXErrorCode                                                                   | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-settags"><strong>setTags</strong></a>(const std::vector&#x3C; std::string > &#x26; tags, const std::string &#x26; operationId) =0<br>设置推送用户的标签。</p>                                                                                                                                                                                         |
| virtual BMXErrorCode                                                                   | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-gettags"><strong>getTags</strong></a>(std::vector&#x3C; std::string > &#x26; tags, const std::string &#x26; operationId) =0<br>获取推送用户的标签。</p>                                                                                                                                                                                               |
| virtual BMXErrorCode                                                                   | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-deletetags"><strong>deleteTags</strong></a>(const std::vector&#x3C; std::string > &#x26; tags, const std::string &#x26; operationId) =0<br>删除推送用户的标签。</p>                                                                                                                                                                                   |
| virtual BMXErrorCode                                                                   | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-cleartags"><strong>clearTags</strong></a>(const std::string &#x26; operationId) =0<br>清空推送用户的标签。</p>                                                                                                                                                                                                                                        |
| virtual BMXErrorCode                                                                   | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-setbadge"><strong>setBadge</strong></a>(int count) =0<br>设置推送用户的未读角标。</p>                                                                                                                                                                                                                                                                   |
| virtual BMXErrorCode                                                                   | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-setpushmode"><strong>setPushMode</strong></a>(bool enable =true) =0<br>设置推送启用状态。默认为使用推送。</p>                                                                                                                                                                                                                                                |
| virtual BMXErrorCode                                                                   | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-setpushtime"><strong>setPushTime</strong></a>(int startHour, int endHour) =0<br>设置允许推送时间。</p>                                                                                                                                                                                                                                               |
| virtual BMXErrorCode                                                                   | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-setsilencetime"><strong>setSilenceTime</strong></a>(int startHour, int endHour) =0<br>设置推送静默的起始结束时间。</p>                                                                                                                                                                                                                                    |
| virtual BMXErrorCode                                                                   | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-setrunbackgroundmode"><strong>setRunBackgroundMode</strong></a>(bool enable =false) =0<br>设置推送是否可以后台运行。默认是false。</p>                                                                                                                                                                                                                        |
| virtual BMXErrorCode                                                                   | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-setgeofencemode"><strong>setGeoFenceMode</strong></a>(bool enable =false, bool isAllow =false) =0<br>设置推送的地理围栏功能是否运行。</p>                                                                                                                                                                                                                   |
| virtual void                                                                           | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-clearnotification"><strong>clearNotification</strong></a>(int64_t notificationId) =0<br>清除指定id的通知。</p>                                                                                                                                                                                                                                      |
| virtual void                                                                           | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-clearallnotifications"><strong>clearAllNotifications</strong></a>() =0<br>清空下拉通知栏全部通知。</p>                                                                                                                                                                                                                                                  |
| virtual void                                                                           | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-sendmessage"><strong>sendMessage</strong></a>(const std::string &#x26; content) =0<br>发送推送上行消息，消息状态变化会通过listener通知</p>                                                                                                                                                                                                                      |
| virtual BMXErrorCode                                                                   | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-loadlocalpushmessages"><strong>loadLocalPushMessages</strong></a>(int64_t refMsgId, size_t size, BMXMessageList &#x26; result, <a href="classfloo_1_1_b_m_x_push_service.md#enum-pushdirection">PushDirection</a> =<a href="classfloo_1_1_b_m_x_push_service.md#enumvalue-up">PushDirection::Up</a>) =0<br>加载数据库本地存储的推送消息。如果不指定则从最新消息开始</p> |
| virtual void                                                                           | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-addpushlistener"><strong>addPushListener</strong></a>(<a href="classfloo_1_1_b_m_x_push_service_listener.md">BMXPushServiceListener</a> * listener) =0<br>添加推送监听者</p>                                                                                                                                                                       |
| virtual void                                                                           | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-removepushlistener"><strong>removePushListener</strong></a>(<a href="classfloo_1_1_b_m_x_push_service_listener.md">BMXPushServiceListener</a> * listener) =0<br>移除推送监听者</p>                                                                                                                                                                 |

## Public Types Documentation

### enum PushSdkStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Starting   | 1     | 正在启动        |
| Started    |       | 启动，在线       |
| Stoped     |       | 停止          |
| Offline    |       | 离线          |

push sdk状态

### enum PushDirection

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Up         |       | 取更旧消息       |
| Down       |       | 取更新消息       |

本地推送消息搜索方向

## Public Functions Documentation

### function \~BMXPushService

```cpp
inline virtual ~BMXPushService()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function start

```cpp
virtual BMXErrorCode start(
    const std::string & alias ="",
    const std::string & bmxToken =""
) =0
```

初始化推送sdk。在仅使用推送的情况下使用该接口初始化推送sdk。在同时使用IM功能的时候直接在BMXClient调用登陆功能即可。config对象初始化的时候需要传入平台类型和设备id。

**Parameters**:

* **alias** 推送初始化使用的当前用户别名
* **bmxToken** 推送初始化的时候App传入的使用的用户的token，无用户的状态下不传入即可。

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function stop

```cpp
virtual BMXErrorCode stop() =0
```

停止推送功能接口。

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function resume

```cpp
virtual BMXErrorCode resume() =0
```

恢复推送功能接口。

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function unbindAlias

```cpp
virtual BMXErrorCode unbindAlias(
    const std::string & alias
) =0
```

解除用户别名绑定。

**Parameters**:

* **alias** 需要解除绑定的用户别名。

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function getToken

```cpp
virtual const std::string & getToken() =0
```

获取登陆后使用的用户token。

**Return**: std::stirng

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function getCert

```cpp
virtual const std::string & getCert() =0
```

获取登陆后服务器返回的推送证书。

**Return**: std::stirng

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function status

```cpp
virtual PushSdkStatus status() =0
```

推送sdk当前的状态。

**Return**: PushSdkStatus

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function bindDeviceToken

```cpp
virtual BMXErrorCode bindDeviceToken(
    const std::string & token
) =0
```

推送绑定设备token。

**Parameters**:

* **token** 设备的推送token

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function bindVoipToken

```cpp
virtual BMXErrorCode bindVoipToken(
    const std::string & token
) =0
```

绑定推送设备的voiptoken。

**Parameters**:

* **token** 设备的voip推送token

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function getPushProfile

```cpp
virtual BMXErrorCode getPushProfile(
    BMXPushUserProfilePtr & pushProfile,
    bool forceRefresh
) =0
```

获取推送用户详情，如果forceRefresh == true，则强制从服务端拉取

**Parameters**:

* **profile** 推送用户profile信息，初始传入指向为空的shared\_ptr对象，函数返回后从此处获取用户profile信息。
* **forceRefresh** 是否强制从服务器拉取，本地获取失败的情况下会自动从服务器拉取

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function setTags

```cpp
virtual BMXErrorCode setTags(
    const std::vector< std::string > & tags,
    const std::string & operationId
) =0
```

设置推送用户的标签。

**Parameters**:

* **tags** 用户标签
* **operationId** 操作id。在回调通知中对应通知提醒。

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function getTags

```cpp
virtual BMXErrorCode getTags(
    std::vector< std::string > & tags,
    const std::string & operationId
) =0
```

获取推送用户的标签。

**Parameters**:

* **tags** 用户标签
* **operationId** 操作id。在回调通知中对应通知提醒。

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function deleteTags

```cpp
virtual BMXErrorCode deleteTags(
    const std::vector< std::string > & tags,
    const std::string & operationId
) =0
```

删除推送用户的标签。

**Parameters**:

* **tags** 要删除用户标签
* **operationId** 操作id。在回调通知中对应通知提醒。

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function clearTags

```cpp
virtual BMXErrorCode clearTags(
    const std::string & operationId
) =0
```

清空推送用户的标签。

**Parameters**:

* **operationId** 操作id。在回调通知中对应通知提醒。

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function setBadge

```cpp
virtual BMXErrorCode setBadge(
    int count
) =0
```

设置推送用户的未读角标。

**Parameters**:

* **count** 用户未读角标数

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function setPushMode

```cpp
virtual BMXErrorCode setPushMode(
    bool enable =true
) =0
```

设置推送启用状态。默认为使用推送。

**Parameters**:

* **enable** 推送的启用状态

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function setPushTime

```cpp
virtual BMXErrorCode setPushTime(
    int startHour,
    int endHour
) =0
```

设置允许推送时间。

**Parameters**:

* **startHour** 静默允许推送的起始时间小时
* **endHour** 静默允许推送的结束时间小时

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function setSilenceTime

```cpp
virtual BMXErrorCode setSilenceTime(
    int startHour,
    int endHour
) =0
```

设置推送静默的起始结束时间。

**Parameters**:

* **startHour** 静默推送的起始时间小时
* **endHour** 静默推送的结束时间小时

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function setRunBackgroundMode

```cpp
virtual BMXErrorCode setRunBackgroundMode(
    bool enable =false
) =0
```

设置推送是否可以后台运行。默认是false。

**Parameters**:

* **enable** 推送后台运行状态。

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function setGeoFenceMode

```cpp
virtual BMXErrorCode setGeoFenceMode(
    bool enable =false,
    bool isAllow =false
) =0
```

设置推送的地理围栏功能是否运行。

**Parameters**:

* **enable** 地理围栏功能是否运行。
* **isAllow** 用户是否主动弹出用户定位请求。

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function clearNotification

```cpp
virtual void clearNotification(
    int64_t notificationId
) =0
```

清除指定id的通知。

**Parameters**:

* **notificationId** 通知id

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function clearAllNotifications

```cpp
virtual void clearAllNotifications() =0
```

清空下拉通知栏全部通知。

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function sendMessage

```cpp
virtual void sendMessage(
    const std::string & content
) =0
```

发送推送上行消息，消息状态变化会通过listener通知

**Parameters**:

* **content** 发送的上行推送消息内容

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function loadLocalPushMessages

```cpp
virtual BMXErrorCode loadLocalPushMessages(
    int64_t refMsgId,
    size_t size,
    BMXMessageList & result,
    PushDirection  =PushDirection::Up
) =0
```

加载数据库本地存储的推送消息。如果不指定则从最新消息开始

**Parameters**:

* **refMsgId** 加载推送消息的起始id
* **size** 最大加载消息条数
* **result** 数据库返回的加载本地推送消息列表
* **Direction** 加载推送消息的方向，默认是加载更早的消息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function addPushListener

```cpp
virtual void addPushListener(
    BMXPushServiceListener * listener
) =0
```

添加推送监听者

**Parameters**:

* **listener** 推送监听者

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

### function removePushListener

```cpp
virtual void removePushListener(
    BMXPushServiceListener * listener
) =0
```

移除推送监听者

**Parameters**:

* **listener** 推送监听者

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
