---
title: floo::BMXPushService
---

# floo::BMXPushService

## Public Types

|            | Name                                                                                                                                                                   |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class | <p><a href="classfloo_1_1_b_m_x_push_service.md#enum-pushsdkstatus"><strong>PushSdkStatus</strong></a> { Starting = 1, Started, Stoped, Offline}<br>push sdk state</p> |
| enum class | <p><a href="classfloo_1_1_b_m_x_push_service.md#enum-pushdirection"><strong>PushDirection</strong></a> { Up, Down}<br>Search direction of local push message</p>       |

## Public Functions

|                                                                                 | Name                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual                                                                         | [**\~BMXPushService**](classfloo_1_1_b_m_x_push_service.md#function-~bmxpushservice)()                                                                                                                                                                                                                                                                                                                                                                         |
| virtual BMXErrorCode                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-start"><strong>start</strong></a>(const std::string &#x26; alias ="", const std::string &#x26; bmxToken ="") =0<br>Initialize push sdk. Use this interface to initialize the push sdk in the case of using push only. When using IM features at the same time, call login function directly in BMXClient. The config object initializes by passing in the platform type and device id.</p>            |
| virtual BMXErrorCode                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-stop"><strong>stop</strong></a>() =0<br>Shut push feature interface.</p>                                                                                                                                                                                                                                                                                                                              |
| virtual BMXErrorCode                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-resume"><strong>resume</strong></a>() =0<br>Resume push function.</p>                                                                                                                                                                                                                                                                                                                                 |
| virtual BMXErrorCode                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-unbindalias"><strong>unbindAlias</strong></a>(const std::string &#x26; alias) =0<br>Unbind user alias.</p>                                                                                                                                                                                                                                                                                            |
| virtual const std::string &                                                     | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-gettoken"><strong>getToken</strong></a>() =0<br>Get user token to use after login.</p>                                                                                                                                                                                                                                                                                                                |
| virtual const std::string &                                                     | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-getcert"><strong>getCert</strong></a>() =0<br>Get push certificate returned by server after login.</p>                                                                                                                                                                                                                                                                                                |
| virtual [PushSdkStatus](classfloo_1_1_b_m_x_push_service.md#enum-pushsdkstatus) | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-status"><strong>status</strong></a>() =0<br>Push the current state of sdk.</p>                                                                                                                                                                                                                                                                                                                        |
| virtual BMXErrorCode                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-binddevicetoken"><strong>bindDeviceToken</strong></a>(const std::string &#x26; token) =0<br>Push binding device token.</p>                                                                                                                                                                                                                                                                            |
| virtual BMXErrorCode                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-bindvoiptoken"><strong>bindVoipToken</strong></a>(const std::string &#x26; token) =0<br>Bind voiptoken of push device</p>                                                                                                                                                                                                                                                                             |
| virtual BMXErrorCode                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-getpushprofile"><strong>getPushProfile</strong></a>(BMXPushUserProfilePtr &#x26; pushProfile, bool forceRefresh) =0<br>Get push user details, force pull from server-side if forceRefresh == true</p>                                                                                                                                                                                                 |
| virtual BMXErrorCode                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-settags"><strong>setTags</strong></a>(const std::vector&#x3C; std::string > &#x26; tags, const std::string &#x26; operationId) =0<br>Set tags of push user.</p>                                                                                                                                                                                                                                       |
| virtual BMXErrorCode                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-gettags"><strong>getTags</strong></a>(std::vector&#x3C; std::string > &#x26; tags, const std::string &#x26; operationId) =0<br>Get tags of the push user.</p>                                                                                                                                                                                                                                         |
| virtual BMXErrorCode                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-deletetags"><strong>deleteTags</strong></a>(const std::vector&#x3C; std::string > &#x26; tags, const std::string &#x26; operationId) =0<br>Delete tags of the push user.</p>                                                                                                                                                                                                                          |
| virtual BMXErrorCode                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-cleartags"><strong>clearTags</strong></a>(const std::string &#x26; operationId) =0<br>Clear tags of the push user.</p>                                                                                                                                                                                                                                                                                |
| virtual BMXErrorCode                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-setbadge"><strong>setBadge</strong></a>(int count) =0<br>Set unread badge for push user.</p>                                                                                                                                                                                                                                                                                                          |
| virtual BMXErrorCode                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-setpushmode"><strong>setPushMode</strong></a>(bool enable =true) =0<br>Set push enabled state. Default enabled.</p>                                                                                                                                                                                                                                                                                   |
| virtual BMXErrorCode                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-setpushtime"><strong>setPushTime</strong></a>(int startHour, int endHour) =0<br>Set allowed push time.</p>                                                                                                                                                                                                                                                                                            |
| virtual BMXErrorCode                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-setsilencetime"><strong>setSilenceTime</strong></a>(int startHour, int endHour) =0<br>Set the start and end time of silent push.</p>                                                                                                                                                                                                                                                                  |
| virtual BMXErrorCode                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-setrunbackgroundmode"><strong>setRunBackgroundMode</strong></a>(bool enable =false) =0<br>Set whether to run push in background, default false.</p>                                                                                                                                                                                                                                                   |
| virtual BMXErrorCode                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-setgeofencemode"><strong>setGeoFenceMode</strong></a>(bool enable =false, bool isAllow =false) =0<br>Set whether to run push geo-fencing feature.</p>                                                                                                                                                                                                                                                 |
| virtual void                                                                    | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-clearnotification"><strong>clearNotification</strong></a>(int64_t notificationId) =0<br>Clear notifications for the specified id.</p>                                                                                                                                                                                                                                                                 |
| virtual void                                                                    | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-clearallnotifications"><strong>clearAllNotifications</strong></a>() =0<br>Empty the drop-down notification bar for all notifications.</p>                                                                                                                                                                                                                                                             |
| virtual void                                                                    | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-sendmessage"><strong>sendMessage</strong></a>(const std::string &#x26; content) =0<br>Send a push uplink message and notify the listener of a change in message status</p>                                                                                                                                                                                                                            |
| virtual BMXErrorCode                                                            | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-loadlocalpushmessages"><strong>loadLocalPushMessages</strong></a>(int64_t refMsgId, size_t size, BMXMessageList &#x26; result, <a href="classfloo_1_1_b_m_x_push_service.md#enum-pushdirection">PushDirection</a> =<a href="classfloo_1_1_b_m_x_push_service.md#enumvalue-up">PushDirection::Up</a>) =0<br>Load push message stored in local database. Start with latest message if not specified</p> |
| virtual void                                                                    | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-addpushlistener"><strong>addPushListener</strong></a>(<a href="classfloo_1_1_b_m_x_push_service_listener.md">BMXPushServiceListener</a> * listener) =0<br>Add push listener</p>                                                                                                                                                                                                                       |
| virtual void                                                                    | <p><a href="classfloo_1_1_b_m_x_push_service.md#function-removepushlistener"><strong>removePushListener</strong></a>(<a href="classfloo_1_1_b_m_x_push_service_listener.md">BMXPushServiceListener</a> * listener) =0<br>Remove push listener</p>                                                                                                                                                                                                              |

## Public Types Documentation

### enum PushSdkStatus

| Enumerator | Value | Description     |
| ---------- | ----- | --------------- |
| Starting   | 1     | Starting        |
| Started    |       | Started, online |
| Stoped     |       | Stop            |
| Offline    |       | Offline         |

push sdk state

### enum PushDirection

| Enumerator | Value | Description         |
| ---------- | ----- | ------------------- |
| Up         |       | Fetch older message |
| Down       |       | Fetch newer message |

Search direction of local push message

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

Initialize push sdk. Use this interface to initialize the push sdk in the case of using push only. When using IM features at the same time, call login function directly in BMXClient. The config object initializes by passing in the platform type and device id.

**Parameters**:

* **alias** Current user alias used for push initialization
* **bmxToken** User token to use that passed in by App when push initialization, and no passing in is OK without users.

**Return**: BMXErrorCode

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>

```

### function stop

```cpp
virtual BMXErrorCode stop() =0
```

Shut push feature interface.

**Return**: BMXErrorCode

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>

```

### function resume

```cpp
virtual BMXErrorCode resume() =0
```

Resume push function.

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

Unbind user alias.

**Parameters**:

* **alias** The user alias that needs to be unbound.

**Return**: BMXErrorCode

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>

```

### function getToken

```cpp
virtual const std::string & getToken() =0
```

Get user token to use after login.

**Return**: std::stirng

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>

```

### function getCert

```cpp
virtual const std::string & getCert() =0
```

Get push certificate returned by server after login.

**Return**: std::stirng

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>

```

### function status

```cpp
virtual PushSdkStatus status() =0
```

Push the current state of sdk.

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

Push binding device token.

**Parameters**:

* **token** Device push token

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

Bind voiptoken of push device

**Parameters**:

* **token** Device voip push token

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

Get push user details, force pull from server-side if forceRefresh == true

**Parameters**:

* **profile** Push user profile information, initially passing in a pointing-to-empty shared\_ptr object, fetch the user profile information here after function returned.
* **forceRefresh** Whether to force pull from server, automatically if local fetch failed

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

Set tags of push user.

**Parameters**:

* **tags** User tag
* **operationId** Operation id. Corresponding notification reminder in callback notification.

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

Get tags of the push user.

**Parameters**:

* **tags** User tag
* **operationId** Operation id. Corresponding notification reminder in callback notification.

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

Delete tags of the push user.

**Parameters**:

* **tags** User tag to delete
* **operationId** Operation id. Corresponding notification reminder in callback notification.

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

Clear tags of the push user.

**Parameters**:

* **operationId** Operation id. Corresponding notification reminder in callback notification.

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

Set unread badge for push user.

**Parameters**:

* **count** Unread badge count of user

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

Set push enabled state. Default enabled.

**Parameters**:

* **enable** Enabled state of push

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

Set allowed push time.

**Parameters**:

* **startHour** Start time for allowed silent push (hour)
* **endHour** End time for allowed silent push (hour)

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

Set the start and end time of silent push.

**Parameters**:

* **startHour** Start time for silent push (hour)
* **endHour** End time for silent push (hour)

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

Set whether to run push in background, default false.

**Parameters**:

* **enable** Running state of push background

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

Set whether to run push geo-fencing feature.

**Parameters**:

* **enable** Whether the geo-fencing function is running.
* **isAllow** Whether the user actively pops up a user location request.

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

Clear notifications for the specified id.

**Parameters**:

* **notificationId** Notification id

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>

```

### function clearAllNotifications

```cpp
virtual void clearAllNotifications() =0
```

Empty the drop-down notification bar for all notifications.

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

Send a push uplink message and notify the listener of a change in message status

**Parameters**:

* **content** Sent uplink push content

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

Load push message stored in local database. Start with latest message if not specified

**Parameters**:

* **refMsgId** Start id for loading pushes
* **size** Maximum number of searched messages
* **result** List of loaded local pushes returned by database
* **Direction** Direction of loading pushes, default to load earlier messages

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

Add push listener

**Parameters**:

* **listener** Push listener

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

Remove push listener

**Parameters**:

* **listener** Push listener

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushService'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
