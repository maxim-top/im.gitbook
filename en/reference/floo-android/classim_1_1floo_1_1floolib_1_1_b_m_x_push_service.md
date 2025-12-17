---
title: im::floo::floolib::BMXPushService
---

# im::floo::floolib::BMXPushService

## Public Functions

|                              | Name                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void            | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-delete)()                                                                                                                                                                                                                                                                                                                                  |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-start"><strong>start</strong></a>(String alias, String bmxToken)<br>Initialize push sdk. Use this interface to initialize the push sdk in the case of using push only. When using IM features at the same time, call login function directly in BMXClient. The config object initializes by passing in the platform type and device id.</p> |
| \[BMXErrorCode]              | [**start**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-start)(String alias)                                                                                                                                                                                                                                                                                                                        |
| \[BMXErrorCode]              | [**start**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-start)()                                                                                                                                                                                                                                                                                                                                    |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-stop"><strong>stop</strong></a>()<br>Shut push feature interface.</p>                                                                                                                                                                                                                                                                       |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-resume"><strong>resume</strong></a>()<br>Resume push function.</p>                                                                                                                                                                                                                                                                          |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-unbindalias"><strong>unbindAlias</strong></a>(String alias)<br>Unbind user alias.</p>                                                                                                                                                                                                                                                       |
| String                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-gettoken"><strong>getToken</strong></a>()<br>Get user token to use after login.</p>                                                                                                                                                                                                                                                         |
| String                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-getcert"><strong>getCert</strong></a>()<br>Get push certificate returned by server after login.</p>                                                                                                                                                                                                                                         |
| BMXPushService.PushSdkStatus | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-status"><strong>status</strong></a>()<br>Push the current state of sdk.</p>                                                                                                                                                                                                                                                                 |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-binddevicetoken"><strong>bindDeviceToken</strong></a>(String token)<br>Push binding device token.</p>                                                                                                                                                                                                                                       |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-bindvoiptoken"><strong>bindVoipToken</strong></a>(String token)<br>Bind voiptoken of push device</p>                                                                                                                                                                                                                                        |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-getpushprofile"><strong>getPushProfile</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_user_profile.md">BMXPushUserProfile</a> pushProfile, boolean forceRefresh)<br>Get push user details, force pull from server-side if forceRefresh == true</p>                                                                         |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-settags"><strong>setTags</strong></a>(TagList tags, String operationId)<br>Set tags of push user.</p>                                                                                                                                                                                                                                       |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-gettags"><strong>getTags</strong></a>(TagList tags, String operationId)<br>Get tags of the push user.</p>                                                                                                                                                                                                                                   |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-deletetags"><strong>deleteTags</strong></a>(TagList tags, String operationId)<br>Delete tags of the push user.</p>                                                                                                                                                                                                                          |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-cleartags"><strong>clearTags</strong></a>(String operationId)<br>Clear tags of the push user.</p>                                                                                                                                                                                                                                           |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setbadge"><strong>setBadge</strong></a>(int count)<br>Set unread badge for push user.</p>                                                                                                                                                                                                                                                   |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setpushmode"><strong>setPushMode</strong></a>(boolean enable)<br>Set push enabled state. Default enabled.</p>                                                                                                                                                                                                                               |
| \[BMXErrorCode]              | [**setPushMode**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setpushmode)()                                                                                                                                                                                                                                                                                                                        |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setpushtime"><strong>setPushTime</strong></a>(int startHour, int endHour)<br>Set allowed push time.</p>                                                                                                                                                                                                                                     |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setsilencetime"><strong>setSilenceTime</strong></a>(int startHour, int endHour)<br>Set the start and end time of silent push.</p>                                                                                                                                                                                                           |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setrunbackgroundmode"><strong>setRunBackgroundMode</strong></a>(boolean enable)<br>Set whether to run push in background, default false.</p>                                                                                                                                                                                                |
| \[BMXErrorCode]              | [**setRunBackgroundMode**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setrunbackgroundmode)()                                                                                                                                                                                                                                                                                                      |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setgeofencemode"><strong>setGeoFenceMode</strong></a>(boolean enable, boolean isAllow)<br>Set whether to run push geo-fencing feature.</p>                                                                                                                                                                                                  |
| \[BMXErrorCode]              | [**setGeoFenceMode**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setgeofencemode)(boolean enable)                                                                                                                                                                                                                                                                                                  |
| \[BMXErrorCode]              | [**setGeoFenceMode**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-setgeofencemode)()                                                                                                                                                                                                                                                                                                                |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-clearnotification"><strong>clearNotification</strong></a>(long notificationId)<br>Clear notifications for the specified id.</p>                                                                                                                                                                                                             |
| void                         | [**clearAllNotifications**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-clearallnotifications)()                                                                                                                                                                                                                                                                                                    |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-sendmessage"><strong>sendMessage</strong></a>(String content)<br>Send a push uplink message and notify the listener of a change in message status</p>                                                                                                                                                                                       |
| \[BMXErrorCode]              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-loadlocalpushmessages"><strong>loadLocalPushMessages</strong></a>(long refMsgId, long size, BMXMessageList result, BMXPushService.PushDirection arg3)<br>Load push message stored in local database. Start with latest message if not specified</p>                                                                                         |
| \[BMXErrorCode]              | [**loadLocalPushMessages**](classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-loadlocalpushmessages)(long refMsgId, long size, BMXMessageList result)                                                                                                                                                                                                                                                     |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-addpushlistener"><strong>addPushListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md">BMXPushServiceListener</a> listener)<br>Add push listener</p>                                                                                                                                                 |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service.md#function-removepushlistener"><strong>removePushListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md">BMXPushServiceListener</a> listener)<br>Remove push listener</p>                                                                                                                                        |

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

Initialize push sdk. Use this interface to initialize the push sdk in the case of using push only. When using IM features at the same time, call login function directly in BMXClient. The config object initializes by passing in the platform type and device id.

**Parameters**:

* **alias** Current user alias used for push initialization
* **bmxToken** User token to use that passed in by App when push initialization, and no passing in is OK without users.

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

Shut push feature interface.

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function resume

```java
inline BMXErrorCode resume()
```

Resume push function.

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

Unbind user alias.

**Parameters**:

* **alias** The user alias that needs to be unbound.

**Return**: \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function getToken

```java
inline String getToken()
```

Get user token to use after login.

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function getCert

```java
inline String getCert()
```

Get push certificate returned by server after login.

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushService'></div>

```

### function status

```java
inline BMXPushService.PushSdkStatus status()
```

Push the current state of sdk.

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

Push binding device token.

**Parameters**:

* **token** Device push token

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

Bind voiptoken of push device

**Parameters**:

* **token** Device voip push token

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

Get push user details, force pull from server-side if forceRefresh == true

**Parameters**:

* **pushProfile** Push user profile information, initially passing in a pointing-to-empty shared\_ptr object, fetch the user profile information here after function returned.
* **forceRefresh** Whether to force pull from server, automatically if local fetch failed

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

Set tags of push user.

**Parameters**:

* **tags** User tag
* **operationId** Operation id. Corresponding notification reminder in callback notification.

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

Get tags of the push user.

**Parameters**:

* **tags** User tag
* **operationId** Operation id. Corresponding notification reminder in callback notification.

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

Delete tags of the push user.

**Parameters**:

* **tags** User tag to delete
* **operationId** Operation id. Corresponding notification reminder in callback notification.

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

Clear tags of the push user.

**Parameters**:

* **operationId** Operation id. Corresponding notification reminder in callback notification.

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

Set unread badge for push user.

**Parameters**:

* **count** Unread badge count of user

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

Set push enabled state. Default enabled.

**Parameters**:

* **enable** Enabled state of push

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

Set allowed push time.

**Parameters**:

* **startHour** Start time for allowed silent push (hour)
* **endHour** End time for allowed silent push (hour)

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

Set the start and end time of silent push.

**Parameters**:

* **startHour** Start time for silent push (hour)
* **endHour** End time for silent push (hour)

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

Set whether to run push in background, default false.

**Parameters**:

* **enable** Running state of push background

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

Set whether to run push geo-fencing feature.

**Parameters**:

* **enable** Whether the geo-fencing function is running.
* **isAllow** Whether the user actively pops up a user location request.

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

Clear notifications for the specified id.

**Parameters**:

* **notificationId** Notification id

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

Send a push uplink message and notify the listener of a change in message status

**Parameters**:

* **content** Sent uplink push content

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

Load push message stored in local database. Start with latest message if not specified

**Parameters**:

* **refMsgId** Start id for loading pushes
* **size** Maximum number of searched messages
* **result** List of loaded local pushes returned by database
* **arg3** Direction of loading pushes, default to load earlier messages

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

Add push listener

**Parameters**:

* **listener** Push listener

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

Remove push listener

**Parameters**:

* **listener** Push listener

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
