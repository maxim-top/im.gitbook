---
title: im::floo::floolib::BMXPushService

---

# im::floo::floolib::BMXPushService





## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-delete)**() |
| [BMXErrorCode] | **[start](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-start)**(String alias, String bmxToken)<br>Initialize push sdk. Use this interface to initialize the push sdk in the case of using push only. When using IM features at the same time, call login function directly in BMXClient. The config object initializes by passing in the platform type and device id.  |
| [BMXErrorCode] | **[start](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-start)**(String alias) |
| [BMXErrorCode] | **[start](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-start)**() |
| [BMXErrorCode] | **[stop](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-stop)**()<br>Shut push feature interface.  |
| [BMXErrorCode] | **[resume](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-resume)**()<br>Resume push function.  |
| [BMXErrorCode] | **[unbindAlias](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-unbindalias)**(String alias)<br>Unbind user alias.  |
| String | **[getToken](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-gettoken)**()<br>Get user token to use after login.  |
| String | **[getCert](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-getcert)**()<br>Get push certificate returned by server after login.  |
| BMXPushService.PushSdkStatus | **[status](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-status)**()<br>Push the current state of sdk.  |
| [BMXErrorCode] | **[bindDeviceToken](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-binddevicetoken)**(String token)<br>Push binding device token.  |
| [BMXErrorCode] | **[bindVoipToken](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-bindvoiptoken)**(String token)<br>Bind voiptoken of push device  |
| [BMXErrorCode] | **[getPushProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-getpushprofile)**([BMXPushUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_push_user_profile.md) pushProfile, boolean forceRefresh)<br>Get push user details, force pull from server-side if forceRefresh == true  |
| [BMXErrorCode] | **[setTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-settags)**(TagList tags, String operationId)<br>Set tags of push user.  |
| [BMXErrorCode] | **[getTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-gettags)**(TagList tags, String operationId)<br>Get tags of the push user.  |
| [BMXErrorCode] | **[deleteTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-deletetags)**(TagList tags, String operationId)<br>Delete tags of the push user.  |
| [BMXErrorCode] | **[clearTags](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-cleartags)**(String operationId)<br>Clear tags of the push user.  |
| [BMXErrorCode] | **[setBadge](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setbadge)**(int count)<br>Set unread badge for push user.  |
| [BMXErrorCode] | **[setPushMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setpushmode)**(boolean enable)<br>Set push enabled state. Default enabled.  |
| [BMXErrorCode] | **[setPushMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setpushmode)**() |
| [BMXErrorCode] | **[setPushTime](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setpushtime)**(int startHour, int endHour)<br>Set allowed push time.  |
| [BMXErrorCode] | **[setSilenceTime](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setsilencetime)**(int startHour, int endHour)<br>Set the start and end time of silent push.  |
| [BMXErrorCode] | **[setRunBackgroundMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setrunbackgroundmode)**(boolean enable)<br>Set whether to run push in background, default false.  |
| [BMXErrorCode] | **[setRunBackgroundMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setrunbackgroundmode)**() |
| [BMXErrorCode] | **[setGeoFenceMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setgeofencemode)**(boolean enable, boolean isAllow)<br>Set whether to run push geo-fencing feature.  |
| [BMXErrorCode] | **[setGeoFenceMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setgeofencemode)**(boolean enable) |
| [BMXErrorCode] | **[setGeoFenceMode](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setgeofencemode)**() |
| void | **[clearNotification](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-clearnotification)**(long notificationId)<br>Clear notifications for the specified id.  |
| void | **[clearAllNotifications](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-clearallnotifications)**() |
| void | **[sendMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-sendmessage)**(String content)<br>Send a push uplink message and notify the listener of a change in message status  |
| [BMXErrorCode] | **[loadLocalPushMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-loadlocalpushmessages)**(long refMsgId, long size, BMXMessageList result, BMXPushService.PushDirection arg3)<br>Load push message stored in local database. Start with latest message if not specified  |
| [BMXErrorCode] | **[loadLocalPushMessages](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-loadlocalpushmessages)**(long refMsgId, long size, BMXMessageList result) |
| void | **[addPushListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-addpushlistener)**([BMXPushServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md) listener)<br>Add push listener  |
| void | **[removePushListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-removepushlistener)**([BMXPushServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md) listener)<br>Remove push listener  |

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


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="delete" %}{% endlanying_code_snippet %}
```
### function start

```java
inline BMXErrorCode start(
    String alias,
    String bmxToken
)
```

Initialize push sdk. Use this interface to initialize the push sdk in the case of using push only. When using IM features at the same time, call login function directly in BMXClient. The config object initializes by passing in the platform type and device id. 

**Parameters**: 

  * **alias** Current user alias used for push initialization 
  * **bmxToken** User token to use that passed in by App when push initialization, and no passing in is OK without users. 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="start" %}{% endlanying_code_snippet %}
```
### function start

```java
inline BMXErrorCode start(
    String alias
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="start" %}{% endlanying_code_snippet %}
```
### function start

```java
inline BMXErrorCode start()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="start" %}{% endlanying_code_snippet %}
```
### function stop

```java
inline BMXErrorCode stop()
```

Shut push feature interface. 

**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="stop" %}{% endlanying_code_snippet %}
```
### function resume

```java
inline BMXErrorCode resume()
```

Resume push function. 

**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="resume" %}{% endlanying_code_snippet %}
```
### function unbindAlias

```java
inline BMXErrorCode unbindAlias(
    String alias
)
```

Unbind user alias. 

**Parameters**: 

  * **alias** The user alias that needs to be unbound. 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="unbindAlias" %}{% endlanying_code_snippet %}
```
### function getToken

```java
inline String getToken()
```

Get user token to use after login. 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="getToken" %}{% endlanying_code_snippet %}
```
### function getCert

```java
inline String getCert()
```

Get push certificate returned by server after login. 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="getCert" %}{% endlanying_code_snippet %}
```
### function status

```java
inline BMXPushService.PushSdkStatus status()
```

Push the current state of sdk. 

**Return**: [PushSdkStatus]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="status" %}{% endlanying_code_snippet %}
```
### function bindDeviceToken

```java
inline BMXErrorCode bindDeviceToken(
    String token
)
```

Push binding device token. 

**Parameters**: 

  * **token** Device push token 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="bindDeviceToken" %}{% endlanying_code_snippet %}
```
### function bindVoipToken

```java
inline BMXErrorCode bindVoipToken(
    String token
)
```

Bind voiptoken of push device 

**Parameters**: 

  * **token** Device voip push token 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="bindVoipToken" %}{% endlanying_code_snippet %}
```
### function getPushProfile

```java
inline BMXErrorCode getPushProfile(
    BMXPushUserProfile pushProfile,
    boolean forceRefresh
)
```

Get push user details, force pull from server-side if forceRefresh == true 

**Parameters**: 

  * **pushProfile** Push user profile information, initially passing in a pointing-to-empty shared_ptr object, fetch the user profile information here after function returned. 
  * **forceRefresh** Whether to force pull from server, automatically if local fetch failed 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="getPushProfile" %}{% endlanying_code_snippet %}
```
### function setTags

```java
inline BMXErrorCode setTags(
    TagList tags,
    String operationId
)
```

Set tags of push user. 

**Parameters**: 

  * **tags** User tag 
  * **operationId** Operation id. Corresponding notification reminder in callback notification. 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="setTags" %}{% endlanying_code_snippet %}
```
### function getTags

```java
inline BMXErrorCode getTags(
    TagList tags,
    String operationId
)
```

Get tags of the push user. 

**Parameters**: 

  * **tags** User tag 
  * **operationId** Operation id. Corresponding notification reminder in callback notification. 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="getTags" %}{% endlanying_code_snippet %}
```
### function deleteTags

```java
inline BMXErrorCode deleteTags(
    TagList tags,
    String operationId
)
```

Delete tags of the push user. 

**Parameters**: 

  * **tags** User tag to delete 
  * **operationId** Operation id. Corresponding notification reminder in callback notification. 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="deleteTags" %}{% endlanying_code_snippet %}
```
### function clearTags

```java
inline BMXErrorCode clearTags(
    String operationId
)
```

Clear tags of the push user. 

**Parameters**: 

  * **operationId** Operation id. Corresponding notification reminder in callback notification. 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="clearTags" %}{% endlanying_code_snippet %}
```
### function setBadge

```java
inline BMXErrorCode setBadge(
    int count
)
```

Set unread badge for push user. 

**Parameters**: 

  * **count** Unread badge count of user 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="setBadge" %}{% endlanying_code_snippet %}
```
### function setPushMode

```java
inline BMXErrorCode setPushMode(
    boolean enable
)
```

Set push enabled state. Default enabled. 

**Parameters**: 

  * **enable** Enabled state of push 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="setPushMode" %}{% endlanying_code_snippet %}
```
### function setPushMode

```java
inline BMXErrorCode setPushMode()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="setPushMode" %}{% endlanying_code_snippet %}
```
### function setPushTime

```java
inline BMXErrorCode setPushTime(
    int startHour,
    int endHour
)
```

Set allowed push time. 

**Parameters**: 

  * **startHour** Start time for allowed silent push (hour) 
  * **endHour** End time for allowed silent push (hour) 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="setPushTime" %}{% endlanying_code_snippet %}
```
### function setSilenceTime

```java
inline BMXErrorCode setSilenceTime(
    int startHour,
    int endHour
)
```

Set the start and end time of silent push. 

**Parameters**: 

  * **startHour** Start time for silent push (hour) 
  * **endHour** End time for silent push (hour) 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="setSilenceTime" %}{% endlanying_code_snippet %}
```
### function setRunBackgroundMode

```java
inline BMXErrorCode setRunBackgroundMode(
    boolean enable
)
```

Set whether to run push in background, default false. 

**Parameters**: 

  * **enable** Running state of push background 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="setRunBackgroundMode" %}{% endlanying_code_snippet %}
```
### function setRunBackgroundMode

```java
inline BMXErrorCode setRunBackgroundMode()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="setRunBackgroundMode" %}{% endlanying_code_snippet %}
```
### function setGeoFenceMode

```java
inline BMXErrorCode setGeoFenceMode(
    boolean enable,
    boolean isAllow
)
```

Set whether to run push geo-fencing feature. 

**Parameters**: 

  * **enable** Whether the geo-fencing function is running. 
  * **isAllow** Whether the user actively pops up a user location request. 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="setGeoFenceMode" %}{% endlanying_code_snippet %}
```
### function setGeoFenceMode

```java
inline BMXErrorCode setGeoFenceMode(
    boolean enable
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="setGeoFenceMode" %}{% endlanying_code_snippet %}
```
### function setGeoFenceMode

```java
inline BMXErrorCode setGeoFenceMode()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="setGeoFenceMode" %}{% endlanying_code_snippet %}
```
### function clearNotification

```java
inline void clearNotification(
    long notificationId
)
```

Clear notifications for the specified id. 

**Parameters**: 

  * **notificationId** Notification id 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="clearNotification" %}{% endlanying_code_snippet %}
```
### function clearAllNotifications

```java
inline void clearAllNotifications()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="clearAllNotifications" %}{% endlanying_code_snippet %}
```
### function sendMessage

```java
inline void sendMessage(
    String content
)
```

Send a push uplink message and notify the listener of a change in message status 

**Parameters**: 

  * **content** Sent uplink push content 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="sendMessage" %}{% endlanying_code_snippet %}
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

Load push message stored in local database. Start with latest message if not specified 

**Parameters**: 

  * **refMsgId** Start id for loading pushes 
  * **size** Maximum number of searched messages 
  * **result** List of loaded local pushes returned by database 
  * **arg3** Direction of loading pushes, default to load earlier messages 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="loadLocalPushMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="loadLocalPushMessages" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="addPushListener" %}{% endlanying_code_snippet %}
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


## Protected Functions Documentation

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="removePushListener" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="BMXPushService" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="finalize" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXPushService",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800