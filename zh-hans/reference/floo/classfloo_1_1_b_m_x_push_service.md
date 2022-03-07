---
title: floo::BMXPushService

---

# floo::BMXPushService





## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[PushSdkStatus](classfloo_1_1_b_m_x_push_service.md#enum-pushsdkstatus)** { Starting = 1, Started, Stoped, Offline}<br>push sdk状态  |
| enum class| **[PushDirection](classfloo_1_1_b_m_x_push_service.md#enum-pushdirection)** { Up, Down}<br>本地推送消息搜索方向  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXPushService](classfloo_1_1_b_m_x_push_service.md#function-~bmxpushservice)**() |
| virtual BMXErrorCode | **[start](classfloo_1_1_b_m_x_push_service.md#function-start)**(const std::string & alias ="", const std::string & bmxToken ="") =0<br>初始化推送sdk。在仅使用推送的情况下使用该接口初始化推送sdk。在同时使用IM功能的时候直接在BMXClient调用登陆功能即可。config对象初始化的时候需要传入平台类型和设备id。  |
| virtual BMXErrorCode | **[stop](classfloo_1_1_b_m_x_push_service.md#function-stop)**() =0<br>停止推送功能接口。  |
| virtual BMXErrorCode | **[resume](classfloo_1_1_b_m_x_push_service.md#function-resume)**() =0<br>恢复推送功能接口。  |
| virtual BMXErrorCode | **[unbindAlias](classfloo_1_1_b_m_x_push_service.md#function-unbindalias)**(const std::string & alias) =0<br>解除用户别名绑定。  |
| virtual const std::string & | **[getToken](classfloo_1_1_b_m_x_push_service.md#function-gettoken)**() =0<br>获取登陆后使用的用户token。  |
| virtual const std::string & | **[getCert](classfloo_1_1_b_m_x_push_service.md#function-getcert)**() =0<br>获取登陆后服务器返回的推送证书。  |
| virtual [PushSdkStatus](classfloo_1_1_b_m_x_push_service.md#enum-pushsdkstatus) | **[status](classfloo_1_1_b_m_x_push_service.md#function-status)**() =0<br>推送sdk当前的状态。  |
| virtual BMXErrorCode | **[bindDeviceToken](classfloo_1_1_b_m_x_push_service.md#function-binddevicetoken)**(const std::string & token) =0<br>推送绑定设备token。  |
| virtual BMXErrorCode | **[bindVoipToken](classfloo_1_1_b_m_x_push_service.md#function-bindvoiptoken)**(const std::string & token) =0<br>绑定推送设备的voiptoken。  |
| virtual BMXErrorCode | **[getPushProfile](classfloo_1_1_b_m_x_push_service.md#function-getpushprofile)**(BMXPushUserProfilePtr & pushProfile, bool forceRefresh) =0<br>获取推送用户详情，如果forceRefresh == true，则强制从服务端拉取  |
| virtual BMXErrorCode | **[setTags](classfloo_1_1_b_m_x_push_service.md#function-settags)**(const std::vector< std::string > & tags, const std::string & operationId) =0<br>设置推送用户的标签。  |
| virtual BMXErrorCode | **[getTags](classfloo_1_1_b_m_x_push_service.md#function-gettags)**(std::vector< std::string > & tags, const std::string & operationId) =0<br>获取推送用户的标签。  |
| virtual BMXErrorCode | **[deleteTags](classfloo_1_1_b_m_x_push_service.md#function-deletetags)**(const std::vector< std::string > & tags, const std::string & operationId) =0<br>删除推送用户的标签。  |
| virtual BMXErrorCode | **[clearTags](classfloo_1_1_b_m_x_push_service.md#function-cleartags)**(const std::string & operationId) =0<br>清空推送用户的标签。  |
| virtual BMXErrorCode | **[setBadge](classfloo_1_1_b_m_x_push_service.md#function-setbadge)**(int count) =0<br>设置推送用户的未读角标。  |
| virtual BMXErrorCode | **[setPushMode](classfloo_1_1_b_m_x_push_service.md#function-setpushmode)**(bool enable =true) =0<br>设置推送启用状态。默认为使用推送。  |
| virtual BMXErrorCode | **[setPushTime](classfloo_1_1_b_m_x_push_service.md#function-setpushtime)**(int startHour, int endHour) =0<br>设置允许推送时间。  |
| virtual BMXErrorCode | **[setSilenceTime](classfloo_1_1_b_m_x_push_service.md#function-setsilencetime)**(int startHour, int endHour) =0<br>设置推送静默的起始结束时间。  |
| virtual BMXErrorCode | **[setRunBackgroundMode](classfloo_1_1_b_m_x_push_service.md#function-setrunbackgroundmode)**(bool enable =false) =0<br>设置推送是否可以后台运行。默认是false。  |
| virtual BMXErrorCode | **[setGeoFenceMode](classfloo_1_1_b_m_x_push_service.md#function-setgeofencemode)**(bool enable =false, bool isAllow =false) =0<br>设置推送的地理围栏功能是否运行。  |
| virtual void | **[clearNotification](classfloo_1_1_b_m_x_push_service.md#function-clearnotification)**(int64_t notificationId) =0<br>清除指定id的通知。  |
| virtual void | **[clearAllNotifications](classfloo_1_1_b_m_x_push_service.md#function-clearallnotifications)**() =0<br>清空下拉通知栏全部通知。  |
| virtual void | **[sendMessage](classfloo_1_1_b_m_x_push_service.md#function-sendmessage)**(const std::string & content) =0<br>发送推送上行消息，消息状态变化会通过listener通知  |
| virtual BMXErrorCode | **[loadLocalPushMessages](classfloo_1_1_b_m_x_push_service.md#function-loadlocalpushmessages)**(int64_t refMsgId, size_t size, BMXMessageList & result, [PushDirection](classfloo_1_1_b_m_x_push_service.md#enum-pushdirection)  =[PushDirection::Up](classfloo_1_1_b_m_x_push_service.md#enumvalue-up)) =0<br>加载数据库本地存储的推送消息。如果不指定则从最新消息开始  |
| virtual void | **[addPushListener](classfloo_1_1_b_m_x_push_service.md#function-addpushlistener)**([BMXPushServiceListener](classfloo_1_1_b_m_x_push_service_listener.md) * listener) =0<br>添加推送监听者  |
| virtual void | **[removePushListener](classfloo_1_1_b_m_x_push_service.md#function-removepushlistener)**([BMXPushServiceListener](classfloo_1_1_b_m_x_push_service_listener.md) * listener) =0<br>移除推送监听者  |

## Public Types Documentation

### enum PushSdkStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Starting | 1| 正在启动   |
| Started | | 启动，在线   |
| Stoped | | 停止   |
| Offline | | 离线   |



push sdk状态 

### enum PushDirection

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Up | | 取更旧消息   |
| Down | | 取更新消息   |



本地推送消息搜索方向 

## Public Functions Documentation

### function ~BMXPushService

```cpp
inline virtual ~BMXPushService()
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

### function stop

```cpp
virtual BMXErrorCode stop() =0
```

停止推送功能接口。 

**Return**: BMXErrorCode 

### function resume

```cpp
virtual BMXErrorCode resume() =0
```

恢复推送功能接口。 

**Return**: BMXErrorCode 

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

### function getToken

```cpp
virtual const std::string & getToken() =0
```

获取登陆后使用的用户token。 

**Return**: std::stirng 

### function getCert

```cpp
virtual const std::string & getCert() =0
```

获取登陆后服务器返回的推送证书。 

**Return**: std::stirng 

### function status

```cpp
virtual PushSdkStatus status() =0
```

推送sdk当前的状态。 

**Return**: PushSdkStatus 

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

### function getPushProfile

```cpp
virtual BMXErrorCode getPushProfile(
    BMXPushUserProfilePtr & pushProfile,
    bool forceRefresh
) =0
```

获取推送用户详情，如果forceRefresh == true，则强制从服务端拉取 

**Parameters**: 

  * **profile** 推送用户profile信息，初始传入指向为空的shared_ptr对象，函数返回后从此处获取用户profile信息。 
  * **forceRefresh** 是否强制从服务器拉取，本地获取失败的情况下会自动从服务器拉取 


**Return**: BMXErrorCode 

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

### function clearNotification

```cpp
virtual void clearNotification(
    int64_t notificationId
) =0
```

清除指定id的通知。 

**Parameters**: 

  * **notificationId** 通知id 


### function clearAllNotifications

```cpp
virtual void clearAllNotifications() =0
```

清空下拉通知栏全部通知。 

### function sendMessage

```cpp
virtual void sendMessage(
    const std::string & content
) =0
```

发送推送上行消息，消息状态变化会通过listener通知 

**Parameters**: 

  * **content** 发送的上行推送消息内容 


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


### function addPushListener

```cpp
virtual void addPushListener(
    BMXPushServiceListener * listener
) =0
```

添加推送监听者 

**Parameters**: 

  * **listener** 推送监听者 


### function removePushListener

```cpp
virtual void removePushListener(
    BMXPushServiceListener * listener
) =0
```

移除推送监听者 

**Parameters**: 

  * **listener** 推送监听者 


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800