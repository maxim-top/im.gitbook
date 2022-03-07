---
title: floo::BMXPushService

---

# floo::BMXPushService





## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[PushSdkStatus](classfloo_1_1_b_m_x_push_service.md#enum-pushsdkstatus)** { Starting = 1, Started, Stoped, Offline}<br>push sdk state  |
| enum class| **[PushDirection](classfloo_1_1_b_m_x_push_service.md#enum-pushdirection)** { Up, Down}<br>Search direction of local push message  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXPushService](classfloo_1_1_b_m_x_push_service.md#function-~bmxpushservice)**() |
| virtual BMXErrorCode | **[start](classfloo_1_1_b_m_x_push_service.md#function-start)**(const std::string & alias ="", const std::string & bmxToken ="") =0<br>Initialize push sdk. Use this interface to initialize the push sdk in the case of using push only. When using IM features at the same time, call login function directly in BMXClient. The config object initializes by passing in the platform type and device id.  |
| virtual BMXErrorCode | **[stop](classfloo_1_1_b_m_x_push_service.md#function-stop)**() =0<br>Shut push feature interface.  |
| virtual BMXErrorCode | **[resume](classfloo_1_1_b_m_x_push_service.md#function-resume)**() =0<br>Resume push function.  |
| virtual BMXErrorCode | **[unbindAlias](classfloo_1_1_b_m_x_push_service.md#function-unbindalias)**(const std::string & alias) =0<br>Unbind user alias.  |
| virtual const std::string & | **[getToken](classfloo_1_1_b_m_x_push_service.md#function-gettoken)**() =0<br>Get user token to use after login.  |
| virtual const std::string & | **[getCert](classfloo_1_1_b_m_x_push_service.md#function-getcert)**() =0<br>Get push certificate returned by server after login.  |
| virtual [PushSdkStatus](classfloo_1_1_b_m_x_push_service.md#enum-pushsdkstatus) | **[status](classfloo_1_1_b_m_x_push_service.md#function-status)**() =0<br>Push the current state of sdk.  |
| virtual BMXErrorCode | **[bindDeviceToken](classfloo_1_1_b_m_x_push_service.md#function-binddevicetoken)**(const std::string & token) =0<br>Push binding device token.  |
| virtual BMXErrorCode | **[bindVoipToken](classfloo_1_1_b_m_x_push_service.md#function-bindvoiptoken)**(const std::string & token) =0<br>Bind voiptoken of push device  |
| virtual BMXErrorCode | **[getPushProfile](classfloo_1_1_b_m_x_push_service.md#function-getpushprofile)**(BMXPushUserProfilePtr & pushProfile, bool forceRefresh) =0<br>Get push user details, force pull from server-side if forceRefresh == true  |
| virtual BMXErrorCode | **[setTags](classfloo_1_1_b_m_x_push_service.md#function-settags)**(const std::vector< std::string > & tags, const std::string & operationId) =0<br>Set tags of push user.  |
| virtual BMXErrorCode | **[getTags](classfloo_1_1_b_m_x_push_service.md#function-gettags)**(std::vector< std::string > & tags, const std::string & operationId) =0<br>Get tags of the push user.  |
| virtual BMXErrorCode | **[deleteTags](classfloo_1_1_b_m_x_push_service.md#function-deletetags)**(const std::vector< std::string > & tags, const std::string & operationId) =0<br>Delete tags of the push user.  |
| virtual BMXErrorCode | **[clearTags](classfloo_1_1_b_m_x_push_service.md#function-cleartags)**(const std::string & operationId) =0<br>Clear tags of the push user.  |
| virtual BMXErrorCode | **[setBadge](classfloo_1_1_b_m_x_push_service.md#function-setbadge)**(int count) =0<br>Set unread badge for push user.  |
| virtual BMXErrorCode | **[setPushMode](classfloo_1_1_b_m_x_push_service.md#function-setpushmode)**(bool enable =true) =0<br>Set push enabled state. Default enabled.  |
| virtual BMXErrorCode | **[setPushTime](classfloo_1_1_b_m_x_push_service.md#function-setpushtime)**(int startHour, int endHour) =0<br>Set allowed push time.  |
| virtual BMXErrorCode | **[setSilenceTime](classfloo_1_1_b_m_x_push_service.md#function-setsilencetime)**(int startHour, int endHour) =0<br>Set the start and end time of silent push.  |
| virtual BMXErrorCode | **[setRunBackgroundMode](classfloo_1_1_b_m_x_push_service.md#function-setrunbackgroundmode)**(bool enable =false) =0<br>Set whether to run push in background, default false.  |
| virtual BMXErrorCode | **[setGeoFenceMode](classfloo_1_1_b_m_x_push_service.md#function-setgeofencemode)**(bool enable =false, bool isAllow =false) =0<br>Set whether to run push geo-fencing feature.  |
| virtual void | **[clearNotification](classfloo_1_1_b_m_x_push_service.md#function-clearnotification)**(int64_t notificationId) =0<br>Clear notifications for the specified id.  |
| virtual void | **[clearAllNotifications](classfloo_1_1_b_m_x_push_service.md#function-clearallnotifications)**() =0<br>Empty the drop-down notification bar for all notifications.  |
| virtual void | **[sendMessage](classfloo_1_1_b_m_x_push_service.md#function-sendmessage)**(const std::string & content) =0<br>Send a push uplink message and notify the listener of a change in message status  |
| virtual BMXErrorCode | **[loadLocalPushMessages](classfloo_1_1_b_m_x_push_service.md#function-loadlocalpushmessages)**(int64_t refMsgId, size_t size, BMXMessageList & result, [PushDirection](classfloo_1_1_b_m_x_push_service.md#enum-pushdirection)  =[PushDirection::Up](classfloo_1_1_b_m_x_push_service.md#enumvalue-up)) =0<br>Load push message stored in local database. Start with latest message if not specified  |
| virtual void | **[addPushListener](classfloo_1_1_b_m_x_push_service.md#function-addpushlistener)**([BMXPushServiceListener](classfloo_1_1_b_m_x_push_service_listener.md) * listener) =0<br>Add push listener  |
| virtual void | **[removePushListener](classfloo_1_1_b_m_x_push_service.md#function-removepushlistener)**([BMXPushServiceListener](classfloo_1_1_b_m_x_push_service_listener.md) * listener) =0<br>Remove push listener  |

## Public Types Documentation

### enum PushSdkStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Starting | 1| Starting   |
| Started | | Started, online   |
| Stoped | | Stop   |
| Offline | | Offline   |



push sdk state 

### enum PushDirection

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Up | | Fetch older message   |
| Down | | Fetch newer message   |



Search direction of local push message 

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

Initialize push sdk. Use this interface to initialize the push sdk in the case of using push only. When using IM features at the same time, call login function directly in BMXClient. The config object initializes by passing in the platform type and device id. 

**Parameters**: 

  * **alias** Current user alias used for push initialization 
  * **bmxToken** User token to use that passed in by App when push initialization, and no passing in is OK without users. 


**Return**: BMXErrorCode 

### function stop

```cpp
virtual BMXErrorCode stop() =0
```

Shut push feature interface. 

**Return**: BMXErrorCode 

### function resume

```cpp
virtual BMXErrorCode resume() =0
```

Resume push function. 

**Return**: BMXErrorCode 

### function unbindAlias

```cpp
virtual BMXErrorCode unbindAlias(
    const std::string & alias
) =0
```

Unbind user alias. 

**Parameters**: 

  * **alias** The user alias that needs to be unbound. 


**Return**: BMXErrorCode 

### function getToken

```cpp
virtual const std::string & getToken() =0
```

Get user token to use after login. 

**Return**: std::stirng 

### function getCert

```cpp
virtual const std::string & getCert() =0
```

Get push certificate returned by server after login. 

**Return**: std::stirng 

### function status

```cpp
virtual PushSdkStatus status() =0
```

Push the current state of sdk. 

**Return**: PushSdkStatus 

### function bindDeviceToken

```cpp
virtual BMXErrorCode bindDeviceToken(
    const std::string & token
) =0
```

Push binding device token. 

**Parameters**: 

  * **token** Device push token 


**Return**: BMXErrorCode 

### function bindVoipToken

```cpp
virtual BMXErrorCode bindVoipToken(
    const std::string & token
) =0
```

Bind voiptoken of push device 

**Parameters**: 

  * **token** Device voip push token 


**Return**: BMXErrorCode 

### function getPushProfile

```cpp
virtual BMXErrorCode getPushProfile(
    BMXPushUserProfilePtr & pushProfile,
    bool forceRefresh
) =0
```

Get push user details, force pull from server-side if forceRefresh == true 

**Parameters**: 

  * **profile** Push user profile information, initially passing in a pointing-to-empty shared_ptr object, fetch the user profile information here after function returned. 
  * **forceRefresh** Whether to force pull from server, automatically if local fetch failed 


**Return**: BMXErrorCode 

### function setTags

```cpp
virtual BMXErrorCode setTags(
    const std::vector< std::string > & tags,
    const std::string & operationId
) =0
```

Set tags of push user. 

**Parameters**: 

  * **tags** User tag 
  * **operationId** Operation id. Corresponding notification reminder in callback notification. 


**Return**: BMXErrorCode 

### function getTags

```cpp
virtual BMXErrorCode getTags(
    std::vector< std::string > & tags,
    const std::string & operationId
) =0
```

Get tags of the push user. 

**Parameters**: 

  * **tags** User tag 
  * **operationId** Operation id. Corresponding notification reminder in callback notification. 


**Return**: BMXErrorCode 

### function deleteTags

```cpp
virtual BMXErrorCode deleteTags(
    const std::vector< std::string > & tags,
    const std::string & operationId
) =0
```

Delete tags of the push user. 

**Parameters**: 

  * **tags** User tag to delete 
  * **operationId** Operation id. Corresponding notification reminder in callback notification. 


**Return**: BMXErrorCode 

### function clearTags

```cpp
virtual BMXErrorCode clearTags(
    const std::string & operationId
) =0
```

Clear tags of the push user. 

**Parameters**: 

  * **operationId** Operation id. Corresponding notification reminder in callback notification. 


**Return**: BMXErrorCode 

### function setBadge

```cpp
virtual BMXErrorCode setBadge(
    int count
) =0
```

Set unread badge for push user. 

**Parameters**: 

  * **count** Unread badge count of user 


**Return**: BMXErrorCode 

### function setPushMode

```cpp
virtual BMXErrorCode setPushMode(
    bool enable =true
) =0
```

Set push enabled state. Default enabled. 

**Parameters**: 

  * **enable** Enabled state of push 


**Return**: BMXErrorCode 

### function setPushTime

```cpp
virtual BMXErrorCode setPushTime(
    int startHour,
    int endHour
) =0
```

Set allowed push time. 

**Parameters**: 

  * **startHour** Start time for allowed silent push (hour) 
  * **endHour** End time for allowed silent push (hour) 


**Return**: BMXErrorCode 

### function setSilenceTime

```cpp
virtual BMXErrorCode setSilenceTime(
    int startHour,
    int endHour
) =0
```

Set the start and end time of silent push. 

**Parameters**: 

  * **startHour** Start time for silent push (hour) 
  * **endHour** End time for silent push (hour) 


**Return**: BMXErrorCode 

### function setRunBackgroundMode

```cpp
virtual BMXErrorCode setRunBackgroundMode(
    bool enable =false
) =0
```

Set whether to run push in background, default false. 

**Parameters**: 

  * **enable** Running state of push background 


**Return**: BMXErrorCode 

### function setGeoFenceMode

```cpp
virtual BMXErrorCode setGeoFenceMode(
    bool enable =false,
    bool isAllow =false
) =0
```

Set whether to run push geo-fencing feature. 

**Parameters**: 

  * **enable** Whether the geo-fencing function is running. 
  * **isAllow** Whether the user actively pops up a user location request. 


**Return**: BMXErrorCode 

### function clearNotification

```cpp
virtual void clearNotification(
    int64_t notificationId
) =0
```

Clear notifications for the specified id. 

**Parameters**: 

  * **notificationId** Notification id 


### function clearAllNotifications

```cpp
virtual void clearAllNotifications() =0
```

Empty the drop-down notification bar for all notifications. 

### function sendMessage

```cpp
virtual void sendMessage(
    const std::string & content
) =0
```

Send a push uplink message and notify the listener of a change in message status 

**Parameters**: 

  * **content** Sent uplink push content 


### function loadLocalPushMessages

```cpp
virtual BMXErrorCode loadLocalPushMessages(
    int64_t refMsgId,
    size_t size,
    BMXMessageList & result,
    PushDirection  =PushDirection::Up
) =0
```

Load push message stored in local database. Start with latest message if not specified 

**Parameters**: 

  * **refMsgId** Start id for loading pushes 
  * **size** Maximum number of searched messages 
  * **result** List of loaded local pushes returned by database 
  * **Direction** Direction of loading pushes, default to load earlier messages 


### function addPushListener

```cpp
virtual void addPushListener(
    BMXPushServiceListener * listener
) =0
```

Add push listener 

**Parameters**: 

  * **listener** Push listener 


### function removePushListener

```cpp
virtual void removePushListener(
    BMXPushServiceListener * listener
) =0
```

Remove push listener 

**Parameters**: 

  * **listener** Push listener 


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800