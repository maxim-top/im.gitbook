---
title: im::floo::floolib::BMXPushManager
summary: Push manager
---

# im::floo::floolib::BMXPushManager

Push manager

## Public Functions

|                              | Name                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                              | [**BMXPushManager**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_manager.md#function-bmxpushmanager)([BMXPushService](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_service.md) service)                                                                                                                                                                                                                                                      |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-start"><strong>start</strong></a>(final String alias, final String bmxToken, final BMXCallBack callBack)<br>Initialize push sdk. Use this interface to initialize the push sdk in the case of using push only. When using IM features at the same time, call login function directly in BMXClient. The config object initializes by passing in the platform type and device id.</p> |
| void                         | [**start**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_manager.md#function-start)(final String alias, final BMXCallBack callBack)                                                                                                                                                                                                                                                                                                                   |
| void                         | [**start**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_manager.md#function-start)(final BMXCallBack callBack)                                                                                                                                                                                                                                                                                                                                       |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-stop"><strong>stop</strong></a>(final BMXCallBack callBack)<br>Shut push feature interface.</p>                                                                                                                                                                                                                                                                                     |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-resume"><strong>resume</strong></a>(final BMXCallBack callBack)<br>Resume push function.</p>                                                                                                                                                                                                                                                                                        |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-unbindalias"><strong>unbindAlias</strong></a>(final String alias, final BMXCallBack callBack)<br>Unbind user alias.</p>                                                                                                                                                                                                                                                             |
| String                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-gettoken"><strong>getToken</strong></a>()<br>Get user token to use after login.</p>                                                                                                                                                                                                                                                                                                 |
| String                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-getcert"><strong>getCert</strong></a>()<br>Get push certificate returned by server after login.</p>                                                                                                                                                                                                                                                                                 |
| BMXPushService.PushSdkStatus | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-status"><strong>status</strong></a>()<br>Push the current state of sdk.</p>                                                                                                                                                                                                                                                                                                         |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-binddevicetoken"><strong>bindDeviceToken</strong></a>(final String token, final BMXCallBack callBack)<br>Push binding device token.</p>                                                                                                                                                                                                                                             |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-bindvoiptoken"><strong>bindVoipToken</strong></a>(final String token, final BMXCallBack callBack)<br>Bind voiptoken of push device</p>                                                                                                                                                                                                                                              |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-getpushprofile"><strong>getPushProfile</strong></a>(final boolean forceRefresh, final BMXDataCallBack&#x3C; <a href="../../../zh-hans/reference/floo-android/classim_1_1floo_1_1floolib_1_1_b_m_x_push_user_profile.md">BMXPushUserProfile</a> > callBack)<br>Get push user details, force pull from server-side if forceRefresh == true</p>                                        |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-settags"><strong>setTags</strong></a>(final TagList tags, final String operationId, final BMXCallBack callBack)<br>Set tags of push user.</p>                                                                                                                                                                                                                                       |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-gettags"><strong>getTags</strong></a>(final TagList tags, final String operationId, final BMXCallBack callBack)<br>Get tags of the push user.</p>                                                                                                                                                                                                                                   |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-deletetags"><strong>deleteTags</strong></a>(final TagList tags, final String operationId, final BMXCallBack callBack)<br>Delete tags of the push user.</p>                                                                                                                                                                                                                          |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-cleartags"><strong>clearTags</strong></a>(final String operationId, final BMXCallBack callBack)<br>Clear tags of the push user.</p>                                                                                                                                                                                                                                                 |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setbadge"><strong>setBadge</strong></a>(final int count, final BMXCallBack callBack)<br>Set unread badge for push user.</p>                                                                                                                                                                                                                                                         |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setpushmode"><strong>setPushMode</strong></a>(final boolean enable, final BMXCallBack callBack)<br>Set push enabled state. Default enabled.</p>                                                                                                                                                                                                                                     |
| void                         | [**setPushMode**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_manager.md#function-setpushmode)(final BMXCallBack callBack)                                                                                                                                                                                                                                                                                                                           |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setpushtime"><strong>setPushTime</strong></a>(final int startHour, final int endHour, final BMXCallBack callBack)<br>Set allowed push time.</p>                                                                                                                                                                                                                                     |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setsilencetime"><strong>setSilenceTime</strong></a>(final int startHour, final int endHour, final BMXCallBack callBack)<br>Set the start and end time of silent push.</p>                                                                                                                                                                                                           |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setrunbackgroundmode"><strong>setRunBackgroundMode</strong></a>(final boolean enable, final BMXCallBack callBack)<br>Set whether to run push in background, default false.</p>                                                                                                                                                                                                      |
| void                         | [**setRunBackgroundMode**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_manager.md#function-setrunbackgroundmode)(final BMXCallBack callBack)                                                                                                                                                                                                                                                                                                         |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-setgeofencemode"><strong>setGeoFenceMode</strong></a>(final boolean enable, final boolean isAllow, final BMXCallBack callBack)<br>Set whether to run push geo-fencing feature.</p>                                                                                                                                                                                                  |
| void                         | [**setGeoFenceMode**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_manager.md#function-setgeofencemode)(final boolean enable, final BMXCallBack callBack)                                                                                                                                                                                                                                                                                             |
| void                         | [**setGeoFenceMode**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_manager.md#function-setgeofencemode)(final BMXCallBack callBack)                                                                                                                                                                                                                                                                                                                   |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-clearnotification"><strong>clearNotification</strong></a>(final long notificationId)<br>Clear notifications for the specified id.</p>                                                                                                                                                                                                                                               |
| void                         | [**clearAllNotifications**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_manager.md#function-clearallnotifications)()                                                                                                                                                                                                                                                                                                                                 |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-sendmessage"><strong>sendMessage</strong></a>(final String content)<br>Send a push uplink message and notify the listener of a change in message status</p>                                                                                                                                                                                                                         |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-loadlocalpushmessages"><strong>loadLocalPushMessages</strong></a>(final long refMsgId, final long size, final BMXMessageList result, final BMXPushService.PushDirection arg3, final BMXCallBack callBack)<br>Load push message stored in local database. Start with latest message if not specified</p>                                                                             |
| void                         | [**loadLocalPushMessages**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_push\_manager.md#function-loadlocalpushmessages)(final long refMsgId, final long size, final BMXMessageList result, final BMXCallBack callBack)                                                                                                                                                                                                                                    |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-addpushlistener"><strong>addPushListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md">BMXPushServiceListener</a> listener)<br>Add push listener</p>                                                                                                                                                                                         |
| void                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_manager.md#function-removepushlistener"><strong>removePushListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_push_service_listener.md">BMXPushServiceListener</a> listener)<br>Remove push listener</p>                                                                                                                                                                                |

## Public Functions Documentation

### function BMXPushManager

```java
inline BMXPushManager(
    BMXPushService service
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
```

### function start

```java
inline void start(
    final BMXCallBack callBack
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
```

### function stop

```java
inline void stop(
    final BMXCallBack callBack
)
```

Shut push feature interface.

**Parameters**:

* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
```

### function resume

```java
inline void resume(
    final BMXCallBack callBack
)
```

Resume push function.

**Parameters**:

* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
```

### function getToken

```java
inline String getToken()
```

Get user token to use after login.

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
```

### function getCert

```java
inline String getCert()
```

Get push certificate returned by server after login.

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
```

### function status

```java
inline BMXPushService.PushSdkStatus status()
```

Push the current state of sdk.

**Return**: PushSdkStatus

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
* **callBack** Profile of push user, initially passing in to a pointing-to-empty shared\_ptr object, from which to retrieve the user profile after function returns

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
```

### function setPushMode

```java
inline void setPushMode(
    final BMXCallBack callBack
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
```

### function setRunBackgroundMode

```java
inline void setRunBackgroundMode(
    final BMXCallBack callBack
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
```

### function setGeoFenceMode

```java
inline void setGeoFenceMode(
    final BMXCallBack callBack
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
```

### function clearAllNotifications

```java
inline void clearAllNotifications()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXPushManager'></div>
```



Updated on 2022-01-26 at 17:18:31 +0800
