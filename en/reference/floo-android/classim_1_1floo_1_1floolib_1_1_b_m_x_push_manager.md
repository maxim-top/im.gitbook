---
title: im::floo::floolib::BMXPushManager
summary: Push manager 

---

# im::floo::floolib::BMXPushManager



Push manager 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXPushManager](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-bmxpushmanager)**([BMXPushService](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md) service) |
| void | **[start](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-start)**(final String alias, final String bmxToken, final BMXCallBack callBack)<br>Initialize push sdk. Use this interface to initialize the push sdk in the case of using push only. When using IM features at the same time, call login function directly in BMXClient. The config object initializes by passing in the platform type and device id.  |
| void | **[start](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-start)**(final String alias, final BMXCallBack callBack) |
| void | **[start](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-start)**(final BMXCallBack callBack) |
| void | **[stop](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-stop)**(final BMXCallBack callBack)<br>Shut push feature interface.  |
| void | **[resume](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-resume)**(final BMXCallBack callBack)<br>Resume push function.  |
| void | **[unbindAlias](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-unbindalias)**(final String alias, final BMXCallBack callBack)<br>Unbind user alias.  |
| String | **[getToken](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-gettoken)**()<br>Get user token to use after login.  |
| String | **[getCert](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-getcert)**()<br>Get push certificate returned by server after login.  |
| BMXPushService.PushSdkStatus | **[status](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-status)**()<br>Push the current state of sdk.  |
| void | **[bindDeviceToken](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-binddevicetoken)**(final String token, final BMXCallBack callBack)<br>Push binding device token.  |
| void | **[bindVoipToken](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-bindvoiptoken)**(final String token, final BMXCallBack callBack)<br>Bind voiptoken of push device  |
| void | **[getPushProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-getpushprofile)**(final boolean forceRefresh, final BMXDataCallBack< [BMXPushUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_push_user_profile.md) > callBack)<br>Get push user details, force pull from server-side if forceRefresh == true  |
| void | **[setTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-settags)**(final TagList tags, final String operationId, final BMXCallBack callBack)<br>Set tags of push user.  |
| void | **[getTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-gettags)**(final TagList tags, final String operationId, final BMXCallBack callBack)<br>Get tags of the push user.  |
| void | **[deleteTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-deletetags)**(final TagList tags, final String operationId, final BMXCallBack callBack)<br>Delete tags of the push user.  |
| void | **[clearTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-cleartags)**(final String operationId, final BMXCallBack callBack)<br>Clear tags of the push user.  |
| void | **[setBadge](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setbadge)**(final int count, final BMXCallBack callBack)<br>Set unread badge for push user.  |
| void | **[setPushMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setpushmode)**(final boolean enable, final BMXCallBack callBack)<br>Set push enabled state. Default enabled.  |
| void | **[setPushMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setpushmode)**(final BMXCallBack callBack) |
| void | **[setPushTime](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setpushtime)**(final int startHour, final int endHour, final BMXCallBack callBack)<br>Set allowed push time.  |
| void | **[setSilenceTime](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setsilencetime)**(final int startHour, final int endHour, final BMXCallBack callBack)<br>Set the start and end time of silent push.  |
| void | **[setRunBackgroundMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setrunbackgroundmode)**(final boolean enable, final BMXCallBack callBack)<br>Set whether to run push in background, default false.  |
| void | **[setRunBackgroundMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setrunbackgroundmode)**(final BMXCallBack callBack) |
| void | **[setGeoFenceMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setgeofencemode)**(final boolean enable, final boolean isAllow, final BMXCallBack callBack)<br>Set whether to run push geo-fencing feature.  |
| void | **[setGeoFenceMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setgeofencemode)**(final boolean enable, final BMXCallBack callBack) |
| void | **[setGeoFenceMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setgeofencemode)**(final BMXCallBack callBack) |
| void | **[clearNotification](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-clearnotification)**(final long notificationId)<br>Clear notifications for the specified id.  |
| void | **[clearAllNotifications](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-clearallnotifications)**() |
| void | **[sendMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-sendmessage)**(final String content)<br>Send a push uplink message and notify the listener of a change in message status  |
| void | **[loadLocalPushMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-loadlocalpushmessages)**(final long refMsgId, final long size, final BMXMessageList result, final BMXPushService.PushDirection arg3, final BMXCallBack callBack)<br>Load push message stored in local database. Start with latest message if not specified  |
| void | **[loadLocalPushMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-loadlocalpushmessages)**(final long refMsgId, final long size, final BMXMessageList result, final BMXCallBack callBack) |
| void | **[addPushListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-addpushlistener)**([BMXPushServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md) listener)<br>Add push listener  |
| void | **[removePushListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-removepushlistener)**([BMXPushServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md) listener)<br>Remove push listener  |

## Public Functions Documentation

### function BMXPushManager

```java
inline BMXPushManager(
    BMXPushService service
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="BMXPushManager" %}{% endlanying_code_snippet %}
```
### function start

```java
inline void start(
    final String alias,
    final String bmxToken,
    final BMXCallBack callBack
)
```

Initialize push sdk. Use this interface to initialize the push sdk in the case of using push only. When using IM features at the same time, call login function directly in BMXClient. The config object initializes by passing in the platform type and device id. 

**Parameters**: 

  * **alias** Current user alias used for push initialization 
  * **bmxToken** User token to use that passed in by App when push initialization, and no passing in is OK without users. 
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="start" %}{% endlanying_code_snippet %}
```
### function start

```java
inline void start(
    final String alias,
    final BMXCallBack callBack
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="start" %}{% endlanying_code_snippet %}
```
### function start

```java
inline void start(
    final BMXCallBack callBack
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="start" %}{% endlanying_code_snippet %}
```
### function stop

```java
inline void stop(
    final BMXCallBack callBack
)
```

Shut push feature interface. 

**Parameters**: 

  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="stop" %}{% endlanying_code_snippet %}
```
### function resume

```java
inline void resume(
    final BMXCallBack callBack
)
```

Resume push function. 

**Parameters**: 

  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="resume" %}{% endlanying_code_snippet %}
```
### function unbindAlias

```java
inline void unbindAlias(
    final String alias,
    final BMXCallBack callBack
)
```

Unbind user alias. 

**Parameters**: 

  * **alias** The user alias that needs to be unbound. 
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="unbindAlias" %}{% endlanying_code_snippet %}
```
### function getToken

```java
inline String getToken()
```

Get user token to use after login. 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="getToken" %}{% endlanying_code_snippet %}
```
### function getCert

```java
inline String getCert()
```

Get push certificate returned by server after login. 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="getCert" %}{% endlanying_code_snippet %}
```
### function status

```java
inline BMXPushService.PushSdkStatus status()
```

Push the current state of sdk. 

**Return**: PushSdkStatus 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="status" %}{% endlanying_code_snippet %}
```
### function bindDeviceToken

```java
inline void bindDeviceToken(
    final String token,
    final BMXCallBack callBack
)
```

Push binding device token. 

**Parameters**: 

  * **token** Device push token 
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="bindDeviceToken" %}{% endlanying_code_snippet %}
```
### function bindVoipToken

```java
inline void bindVoipToken(
    final String token,
    final BMXCallBack callBack
)
```

Bind voiptoken of push device 

**Parameters**: 

  * **token** Device voip push token 
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="bindVoipToken" %}{% endlanying_code_snippet %}
```
### function getPushProfile

```java
inline void getPushProfile(
    final boolean forceRefresh,
    final BMXDataCallBack< BMXPushUserProfile > callBack
)
```

Get push user details, force pull from server-side if forceRefresh == true 

**Parameters**: 

  * **forceRefresh** Whether to force pull from server, automatically if local fetch failed 
  * **callBack** Profile of push user, initially passing in to a pointing-to-empty shared_ptr object, from which to retrieve the user profile after function returns 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="getPushProfile" %}{% endlanying_code_snippet %}
```
### function setTags

```java
inline void setTags(
    final TagList tags,
    final String operationId,
    final BMXCallBack callBack
)
```

Set tags of push user. 

**Parameters**: 

  * **tags** User tag 
  * **operationId** Operation id. Corresponding notification reminder in callback notification. 
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="setTags" %}{% endlanying_code_snippet %}
```
### function getTags

```java
inline void getTags(
    final TagList tags,
    final String operationId,
    final BMXCallBack callBack
)
```

Get tags of the push user. 

**Parameters**: 

  * **tags** User tag 
  * **operationId** Operation id. Corresponding notification reminder in callback notification. 
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="getTags" %}{% endlanying_code_snippet %}
```
### function deleteTags

```java
inline void deleteTags(
    final TagList tags,
    final String operationId,
    final BMXCallBack callBack
)
```

Delete tags of the push user. 

**Parameters**: 

  * **tags** User tag to delete 
  * **operationId** Operation id. Corresponding notification reminder in callback notification. 
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="deleteTags" %}{% endlanying_code_snippet %}
```
### function clearTags

```java
inline void clearTags(
    final String operationId,
    final BMXCallBack callBack
)
```

Clear tags of the push user. 

**Parameters**: 

  * **operationId** Operation id. Corresponding notification reminder in callback notification. 
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="clearTags" %}{% endlanying_code_snippet %}
```
### function setBadge

```java
inline void setBadge(
    final int count,
    final BMXCallBack callBack
)
```

Set unread badge for push user. 

**Parameters**: 

  * **count** Unread badge count of user 
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="setBadge" %}{% endlanying_code_snippet %}
```
### function setPushMode

```java
inline void setPushMode(
    final boolean enable,
    final BMXCallBack callBack
)
```

Set push enabled state. Default enabled. 

**Parameters**: 

  * **enable** Enabled state of push 
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="setPushMode" %}{% endlanying_code_snippet %}
```
### function setPushMode

```java
inline void setPushMode(
    final BMXCallBack callBack
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="setPushMode" %}{% endlanying_code_snippet %}
```
### function setPushTime

```java
inline void setPushTime(
    final int startHour,
    final int endHour,
    final BMXCallBack callBack
)
```

Set allowed push time. 

**Parameters**: 

  * **startHour** Start time for allowed silent push (hour) 
  * **endHour** End time for allowed silent push (hour) 
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="setPushTime" %}{% endlanying_code_snippet %}
```
### function setSilenceTime

```java
inline void setSilenceTime(
    final int startHour,
    final int endHour,
    final BMXCallBack callBack
)
```

Set the start and end time of silent push. 

**Parameters**: 

  * **startHour** Start time for silent push (hour) 
  * **endHour** End time for silent push (hour) 
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="setSilenceTime" %}{% endlanying_code_snippet %}
```
### function setRunBackgroundMode

```java
inline void setRunBackgroundMode(
    final boolean enable,
    final BMXCallBack callBack
)
```

Set whether to run push in background, default false. 

**Parameters**: 

  * **enable** Running state of push background 
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="setRunBackgroundMode" %}{% endlanying_code_snippet %}
```
### function setRunBackgroundMode

```java
inline void setRunBackgroundMode(
    final BMXCallBack callBack
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="setRunBackgroundMode" %}{% endlanying_code_snippet %}
```
### function setGeoFenceMode

```java
inline void setGeoFenceMode(
    final boolean enable,
    final boolean isAllow,
    final BMXCallBack callBack
)
```

Set whether to run push geo-fencing feature. 

**Parameters**: 

  * **enable** Whether the geo-fencing function is running. 
  * **isAllow** Whether the user actively pops up a user location request. 
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="setGeoFenceMode" %}{% endlanying_code_snippet %}
```
### function setGeoFenceMode

```java
inline void setGeoFenceMode(
    final boolean enable,
    final BMXCallBack callBack
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="setGeoFenceMode" %}{% endlanying_code_snippet %}
```
### function setGeoFenceMode

```java
inline void setGeoFenceMode(
    final BMXCallBack callBack
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="setGeoFenceMode" %}{% endlanying_code_snippet %}
```
### function clearNotification

```java
inline void clearNotification(
    final long notificationId
)
```

Clear notifications for the specified id. 

**Parameters**: 

  * **notificationId** Notification id 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="clearNotification" %}{% endlanying_code_snippet %}
```
### function clearAllNotifications

```java
inline void clearAllNotifications()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="clearAllNotifications" %}{% endlanying_code_snippet %}
```
### function sendMessage

```java
inline void sendMessage(
    final String content
)
```

Send a push uplink message and notify the listener of a change in message status 

**Parameters**: 

  * **content** Sent uplink push content 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="sendMessage" %}{% endlanying_code_snippet %}
```
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

Load push message stored in local database. Start with latest message if not specified 

**Parameters**: 

  * **refMsgId** Start id for loading pushes 
  * **size** Maximum number of searched messages 
  * **result** List of loaded local pushes returned by database 
  * **arg3** Direction of loading pushes, default to load earlier messages 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="loadLocalPushMessages" %}{% endlanying_code_snippet %}
```
### function loadLocalPushMessages

```java
inline void loadLocalPushMessages(
    final long refMsgId,
    final long size,
    final BMXMessageList result,
    final BMXCallBack callBack
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="loadLocalPushMessages" %}{% endlanying_code_snippet %}
```
### function addPushListener

```java
inline void addPushListener(
    BMXPushServiceListener listener
)
```

Add push listener 

**Parameters**: 

  * **listener** Push listener 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="addPushListener" %}{% endlanying_code_snippet %}
```
### function removePushListener

```java
inline void removePushListener(
    BMXPushServiceListener listener
)
```

Remove push listener 

**Parameters**: 

  * **listener** Push listener 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushManager",function="removePushListener" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800