---
title: im::floo::floolib::BMXPushService

---

# im::floo::floolib::BMXPushService





## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-delete)**() |
| [BMXErrorCode] | **[start](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-start)**(String alias, String bmxToken)<br>初始化推送sdk。在仅使用推送的情况下使用该接口初始化推送sdk。在同时使用IM功能的时候直接在BMXClient调用登陆功能即可。config对象初始化的时候需要传入平台类型和设备id。  |
| [BMXErrorCode] | **[start](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-start)**(String alias) |
| [BMXErrorCode] | **[start](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-start)**() |
| [BMXErrorCode] | **[stop](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-stop)**()<br>停止推送功能接口。  |
| [BMXErrorCode] | **[resume](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-resume)**()<br>恢复推送功能接口。  |
| [BMXErrorCode] | **[unbindAlias](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-unbindalias)**(String alias)<br>解除用户别名绑定。  |
| String | **[getToken](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-gettoken)**()<br>获取登陆后使用的用户token。  |
| String | **[getCert](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-getcert)**()<br>获取登陆后服务器返回的推送证书。  |
| BMXPushService.PushSdkStatus | **[status](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-status)**()<br>推送sdk当前的状态。  |
| [BMXErrorCode] | **[bindDeviceToken](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-binddevicetoken)**(String token)<br>推送绑定设备token。  |
| [BMXErrorCode] | **[bindVoipToken](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-bindvoiptoken)**(String token)<br>绑定推送设备的voiptoken。  |
| [BMXErrorCode] | **[getPushProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-getpushprofile)**([BMXPushUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_push_user_profile.md) pushProfile, boolean forceRefresh)<br>获取推送用户详情，如果forceRefresh == true，则强制从服务端拉取  |
| [BMXErrorCode] | **[setTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-settags)**(TagList tags, String operationId)<br>设置推送用户的标签。  |
| [BMXErrorCode] | **[getTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-gettags)**(TagList tags, String operationId)<br>获取推送用户的标签。  |
| [BMXErrorCode] | **[deleteTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-deletetags)**(TagList tags, String operationId)<br>删除推送用户的标签。  |
| [BMXErrorCode] | **[clearTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-cleartags)**(String operationId)<br>清空推送用户的标签。  |
| [BMXErrorCode] | **[setBadge](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setbadge)**(int count)<br>设置推送用户的未读角标。  |
| [BMXErrorCode] | **[setPushMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setpushmode)**(boolean enable)<br>设置推送启用状态。默认为使用推送。  |
| [BMXErrorCode] | **[setPushMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setpushmode)**() |
| [BMXErrorCode] | **[setPushTime](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setpushtime)**(int startHour, int endHour)<br>设置允许推送时间。  |
| [BMXErrorCode] | **[setSilenceTime](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setsilencetime)**(int startHour, int endHour)<br>设置推送静默的起始结束时间。  |
| [BMXErrorCode] | **[setRunBackgroundMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setrunbackgroundmode)**(boolean enable)<br>设置推送是否可以后台运行。默认是false。  |
| [BMXErrorCode] | **[setRunBackgroundMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setrunbackgroundmode)**() |
| [BMXErrorCode] | **[setGeoFenceMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setgeofencemode)**(boolean enable, boolean isAllow)<br>设置推送的地理围栏功能是否运行。  |
| [BMXErrorCode] | **[setGeoFenceMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setgeofencemode)**(boolean enable) |
| [BMXErrorCode] | **[setGeoFenceMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setgeofencemode)**() |
| void | **[clearNotification](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-clearnotification)**(long notificationId)<br>清除指定id的通知。  |
| void | **[clearAllNotifications](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-clearallnotifications)**() |
| void | **[sendMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-sendmessage)**(String content)<br>发送推送上行消息，消息状态变化会通过listener通知  |
| [BMXErrorCode] | **[loadLocalPushMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-loadlocalpushmessages)**(long refMsgId, long size, BMXMessageList result, BMXPushService.PushDirection arg3)<br>加载数据库本地存储的推送消息。如果不指定则从最新消息开始  |
| [BMXErrorCode] | **[loadLocalPushMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-loadlocalpushmessages)**(long refMsgId, long size, BMXMessageList result) |
| void | **[addPushListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-addpushlistener)**([BMXPushServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md) listener)<br>添加推送监听者  |
| void | **[removePushListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-removepushlistener)**([BMXPushServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md) listener)<br>移除推送监听者  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXPushService](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-bmxpushservice)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-getcptr)**([BMXPushService](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md) obj) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| transient boolean | **[swigCMemOwn](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#variable-swigcmemown)**  |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
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


**Return**: [BMXErrorCode]

### function start

```java
inline BMXErrorCode start(
    String alias
)
```


### function start

```java
inline BMXErrorCode start()
```


### function stop

```java
inline BMXErrorCode stop()
```

停止推送功能接口。 

**Return**: [BMXErrorCode]

### function resume

```java
inline BMXErrorCode resume()
```

恢复推送功能接口。 

**Return**: [BMXErrorCode]

### function unbindAlias

```java
inline BMXErrorCode unbindAlias(
    String alias
)
```

解除用户别名绑定。 

**Parameters**: 

  * **alias** 需要解除绑定的用户别名。 


**Return**: [BMXErrorCode]

### function getToken

```java
inline String getToken()
```

获取登陆后使用的用户token。 

### function getCert

```java
inline String getCert()
```

获取登陆后服务器返回的推送证书。 

### function status

```java
inline BMXPushService.PushSdkStatus status()
```

推送sdk当前的状态。 

**Return**: [PushSdkStatus]

### function bindDeviceToken

```java
inline BMXErrorCode bindDeviceToken(
    String token
)
```

推送绑定设备token。 

**Parameters**: 

  * **token** 设备的推送token 


**Return**: [BMXErrorCode]

### function bindVoipToken

```java
inline BMXErrorCode bindVoipToken(
    String token
)
```

绑定推送设备的voiptoken。 

**Parameters**: 

  * **token** 设备的voip推送token 


**Return**: [BMXErrorCode]

### function getPushProfile

```java
inline BMXErrorCode getPushProfile(
    BMXPushUserProfile pushProfile,
    boolean forceRefresh
)
```

获取推送用户详情，如果forceRefresh == true，则强制从服务端拉取 

**Parameters**: 

  * **pushProfile** 推送用户profile信息，初始传入指向为空的shared_ptr对象，函数返回后从此处获取用户profile信息。 
  * **forceRefresh** 是否强制从服务器拉取，本地获取失败的情况下会自动从服务器拉取 


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

### function clearTags

```java
inline BMXErrorCode clearTags(
    String operationId
)
```

清空推送用户的标签。 

**Parameters**: 

  * **operationId** 操作id。在回调通知中对应通知提醒。 


**Return**: [BMXErrorCode]

### function setBadge

```java
inline BMXErrorCode setBadge(
    int count
)
```

设置推送用户的未读角标。 

**Parameters**: 

  * **count** 用户未读角标数 


**Return**: [BMXErrorCode]

### function setPushMode

```java
inline BMXErrorCode setPushMode(
    boolean enable
)
```

设置推送启用状态。默认为使用推送。 

**Parameters**: 

  * **enable** 推送的启用状态 


**Return**: [BMXErrorCode]

### function setPushMode

```java
inline BMXErrorCode setPushMode()
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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

### function setRunBackgroundMode

```java
inline BMXErrorCode setRunBackgroundMode(
    boolean enable
)
```

设置推送是否可以后台运行。默认是false。 

**Parameters**: 

  * **enable** 推送后台运行状态。 


**Return**: [BMXErrorCode]

### function setRunBackgroundMode

```java
inline BMXErrorCode setRunBackgroundMode()
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


**Return**: [BMXErrorCode]

### function setGeoFenceMode

```java
inline BMXErrorCode setGeoFenceMode(
    boolean enable
)
```


### function setGeoFenceMode

```java
inline BMXErrorCode setGeoFenceMode()
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


### function clearAllNotifications

```java
inline void clearAllNotifications()
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


### function loadLocalPushMessages

```java
inline BMXErrorCode loadLocalPushMessages(
    long refMsgId,
    long size,
    BMXMessageList result
)
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

### function BMXPushService

```java
inline BMXPushService(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
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


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800