---
title: im::floo::floolib::BMXPushManager
summary: 推送管理器 

---

# im::floo::floolib::BMXPushManager



推送管理器 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXPushManager](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-bmxpushmanager)**([BMXPushService](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md) service) |
| void | **[start](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-start)**(final String alias, final String bmxToken, final BMXCallBack callBack)<br>初始化推送sdk。在仅使用推送的情况下使用该接口初始化推送sdk。在同时使用IM功能的时候直接在BMXClient调用登陆功能即可。config对象初始化的时候需要传入平台类型和设备id。  |
| void | **[start](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-start)**(final String alias, final BMXCallBack callBack) |
| void | **[start](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-start)**(final BMXCallBack callBack) |
| void | **[stop](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-stop)**(final BMXCallBack callBack)<br>停止推送功能接口。  |
| void | **[resume](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-resume)**(final BMXCallBack callBack)<br>恢复推送功能接口。  |
| void | **[unbindAlias](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-unbindalias)**(final String alias, final BMXCallBack callBack)<br>解除用户别名绑定。  |
| String | **[getToken](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-gettoken)**()<br>获取登陆后使用的用户token。  |
| String | **[getCert](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-getcert)**()<br>获取登陆后服务器返回的推送证书。  |
| BMXPushService.PushSdkStatus | **[status](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-status)**()<br>推送sdk当前的状态。  |
| void | **[bindDeviceToken](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-binddevicetoken)**(final String token, final BMXCallBack callBack)<br>推送绑定设备token。  |
| void | **[bindVoipToken](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-bindvoiptoken)**(final String token, final BMXCallBack callBack)<br>绑定推送设备的voiptoken。  |
| void | **[getPushProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-getpushprofile)**(final boolean forceRefresh, final BMXDataCallBack< [BMXPushUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_push_user_profile.md) > callBack)<br>获取推送用户详情，如果forceRefresh == true，则强制从服务端拉取  |
| void | **[setTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-settags)**(final TagList tags, final String operationId, final BMXCallBack callBack)<br>设置推送用户的标签。  |
| void | **[getTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-gettags)**(final TagList tags, final String operationId, final BMXCallBack callBack)<br>获取推送用户的标签。  |
| void | **[deleteTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-deletetags)**(final TagList tags, final String operationId, final BMXCallBack callBack)<br>删除推送用户的标签。  |
| void | **[clearTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-cleartags)**(final String operationId, final BMXCallBack callBack)<br>清空推送用户的标签。  |
| void | **[setBadge](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setbadge)**(final int count, final BMXCallBack callBack)<br>设置推送用户的未读角标。  |
| void | **[setPushMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setpushmode)**(final boolean enable, final BMXCallBack callBack)<br>设置推送启用状态。默认为使用推送。  |
| void | **[setPushMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setpushmode)**(final BMXCallBack callBack) |
| void | **[setPushTime](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setpushtime)**(final int startHour, final int endHour, final BMXCallBack callBack)<br>设置允许推送时间。  |
| void | **[setSilenceTime](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setsilencetime)**(final int startHour, final int endHour, final BMXCallBack callBack)<br>设置推送静默的起始结束时间。  |
| void | **[setRunBackgroundMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setrunbackgroundmode)**(final boolean enable, final BMXCallBack callBack)<br>设置推送是否可以后台运行。默认是false。  |
| void | **[setRunBackgroundMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setrunbackgroundmode)**(final BMXCallBack callBack) |
| void | **[setGeoFenceMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setgeofencemode)**(final boolean enable, final boolean isAllow, final BMXCallBack callBack)<br>设置推送的地理围栏功能是否运行。  |
| void | **[setGeoFenceMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setgeofencemode)**(final boolean enable, final BMXCallBack callBack) |
| void | **[setGeoFenceMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setgeofencemode)**(final BMXCallBack callBack) |
| void | **[clearNotification](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-clearnotification)**(final long notificationId)<br>清除指定id的通知。  |
| void | **[clearAllNotifications](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-clearallnotifications)**() |
| void | **[sendMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-sendmessage)**(final String content)<br>发送推送上行消息，消息状态变化会通过listener通知  |
| void | **[loadLocalPushMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-loadlocalpushmessages)**(final long refMsgId, final long size, final BMXMessageList result, final BMXPushService.PushDirection arg3, final BMXCallBack callBack)<br>加载数据库本地存储的推送消息。如果不指定则从最新消息开始  |
| void | **[loadLocalPushMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-loadlocalpushmessages)**(final long refMsgId, final long size, final BMXMessageList result, final BMXCallBack callBack) |
| void | **[addPushListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-addpushlistener)**([BMXPushServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md) listener)<br>添加推送监听者  |
| void | **[removePushListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-removepushlistener)**([BMXPushServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md) listener)<br>移除推送监听者  |

## Public Functions Documentation

### function BMXPushManager

```java
inline BMXPushManager(
    BMXPushService service
)
```


### function start

```java
inline void start(
    final String alias,
    final String bmxToken,
    final BMXCallBack callBack
)
```

初始化推送sdk。在仅使用推送的情况下使用该接口初始化推送sdk。在同时使用IM功能的时候直接在BMXClient调用登陆功能即可。config对象初始化的时候需要传入平台类型和设备id。 

**Parameters**: 

  * **alias** 推送初始化使用的当前用户别名 
  * **bmxToken** 推送初始化的时候App传入的使用的用户的token，无用户的状态下不传入即可。 
  * **callBack** [BMXErrorCode]


### function start

```java
inline void start(
    final String alias,
    final BMXCallBack callBack
)
```


### function start

```java
inline void start(
    final BMXCallBack callBack
)
```


### function stop

```java
inline void stop(
    final BMXCallBack callBack
)
```

停止推送功能接口。 

**Parameters**: 

  * **callBack** [BMXErrorCode]


### function resume

```java
inline void resume(
    final BMXCallBack callBack
)
```

恢复推送功能接口。 

**Parameters**: 

  * **callBack** [BMXErrorCode]


### function unbindAlias

```java
inline void unbindAlias(
    final String alias,
    final BMXCallBack callBack
)
```

解除用户别名绑定。 

**Parameters**: 

  * **alias** 需要解除绑定的用户别名。 
  * **callBack** [BMXErrorCode]


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

**Return**: PushSdkStatus 

### function bindDeviceToken

```java
inline void bindDeviceToken(
    final String token,
    final BMXCallBack callBack
)
```

推送绑定设备token。 

**Parameters**: 

  * **token** 设备的推送token 
  * **callBack** [BMXErrorCode]


### function bindVoipToken

```java
inline void bindVoipToken(
    final String token,
    final BMXCallBack callBack
)
```

绑定推送设备的voiptoken。 

**Parameters**: 

  * **token** 设备的voip推送token 
  * **callBack** [BMXErrorCode]


### function getPushProfile

```java
inline void getPushProfile(
    final boolean forceRefresh,
    final BMXDataCallBack< BMXPushUserProfile > callBack
)
```

获取推送用户详情，如果forceRefresh == true，则强制从服务端拉取 

**Parameters**: 

  * **forceRefresh** 是否强制从服务器拉取，本地获取失败的情况下会自动从服务器拉取 
  * **callBack** 推送用户profile信息，初始传入指向为空的shared_ptr对象，函数返回后从此处获取用户profile信息 


### function setTags

```java
inline void setTags(
    final TagList tags,
    final String operationId,
    final BMXCallBack callBack
)
```

设置推送用户的标签。 

**Parameters**: 

  * **tags** 用户标签 
  * **operationId** 操作id。在回调通知中对应通知提醒。 
  * **callBack** [BMXErrorCode]


### function getTags

```java
inline void getTags(
    final TagList tags,
    final String operationId,
    final BMXCallBack callBack
)
```

获取推送用户的标签。 

**Parameters**: 

  * **tags** 用户标签 
  * **operationId** 操作id。在回调通知中对应通知提醒。 
  * **callBack** [BMXErrorCode]


### function deleteTags

```java
inline void deleteTags(
    final TagList tags,
    final String operationId,
    final BMXCallBack callBack
)
```

删除推送用户的标签。 

**Parameters**: 

  * **tags** 要删除用户标签 
  * **operationId** 操作id。在回调通知中对应通知提醒。 
  * **callBack** [BMXErrorCode]


### function clearTags

```java
inline void clearTags(
    final String operationId,
    final BMXCallBack callBack
)
```

清空推送用户的标签。 

**Parameters**: 

  * **operationId** 操作id。在回调通知中对应通知提醒。 
  * **callBack** [BMXErrorCode]


### function setBadge

```java
inline void setBadge(
    final int count,
    final BMXCallBack callBack
)
```

设置推送用户的未读角标。 

**Parameters**: 

  * **count** 用户未读角标数 
  * **callBack** [BMXErrorCode]


### function setPushMode

```java
inline void setPushMode(
    final boolean enable,
    final BMXCallBack callBack
)
```

设置推送启用状态。默认为使用推送。 

**Parameters**: 

  * **enable** 推送的启用状态 
  * **callBack** [BMXErrorCode]


### function setPushMode

```java
inline void setPushMode(
    final BMXCallBack callBack
)
```


### function setPushTime

```java
inline void setPushTime(
    final int startHour,
    final int endHour,
    final BMXCallBack callBack
)
```

设置允许推送时间。 

**Parameters**: 

  * **startHour** 静默允许推送的起始时间小时 
  * **endHour** 静默允许推送的结束时间小时 
  * **callBack** [BMXErrorCode]


### function setSilenceTime

```java
inline void setSilenceTime(
    final int startHour,
    final int endHour,
    final BMXCallBack callBack
)
```

设置推送静默的起始结束时间。 

**Parameters**: 

  * **startHour** 静默推送的起始时间小时 
  * **endHour** 静默推送的结束时间小时 
  * **callBack** [BMXErrorCode]


### function setRunBackgroundMode

```java
inline void setRunBackgroundMode(
    final boolean enable,
    final BMXCallBack callBack
)
```

设置推送是否可以后台运行。默认是false。 

**Parameters**: 

  * **enable** 推送后台运行状态。 
  * **callBack** [BMXErrorCode]


### function setRunBackgroundMode

```java
inline void setRunBackgroundMode(
    final BMXCallBack callBack
)
```


### function setGeoFenceMode

```java
inline void setGeoFenceMode(
    final boolean enable,
    final boolean isAllow,
    final BMXCallBack callBack
)
```

设置推送的地理围栏功能是否运行。 

**Parameters**: 

  * **enable** 地理围栏功能是否运行。 
  * **isAllow** 用户是否主动弹出用户定位请求。 
  * **callBack** [BMXErrorCode]


### function setGeoFenceMode

```java
inline void setGeoFenceMode(
    final boolean enable,
    final BMXCallBack callBack
)
```


### function setGeoFenceMode

```java
inline void setGeoFenceMode(
    final BMXCallBack callBack
)
```


### function clearNotification

```java
inline void clearNotification(
    final long notificationId
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
    final String content
)
```

发送推送上行消息，消息状态变化会通过listener通知 

**Parameters**: 

  * **content** 发送的上行推送消息内容 


### function loadLocalPushMessages

```java
inline void loadLocalPushMessages(
    final long refMsgId,
    final long size,
    final BMXMessageList result,
    final BMXPushService.PushDirection arg3,
    final BMXCallBack callBack
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
inline void loadLocalPushMessages(
    final long refMsgId,
    final long size,
    final BMXMessageList result,
    final BMXCallBack callBack
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


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800