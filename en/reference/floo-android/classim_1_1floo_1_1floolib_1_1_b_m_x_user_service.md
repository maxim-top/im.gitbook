---
title: im::floo::floolib::BMXUserService
summary: User Service
---

# im::floo::floolib::BMXUserService

User Service

## Public Functions

|                   | Name                                                                                                                                                                                                                                                                                                                             |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_user\_service.md#function-delete)()                                                                                                                                                                                                                                  |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-binddevice"><strong>bindDevice</strong></a>(String token)<br>Binding device push token</p>                                                                                                                                                             |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-getdevicelist"><strong>getDeviceList</strong></a>(BMXDeviceList deviceList)<br>Get device list</p>                                                                                                                                                     |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-getprofile"><strong>getProfile</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md">BMXUserProfile</a> profile, boolean forceRefresh)<br>Get user details, force pull from server if forceRefresh == true</p>                   |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-deletedevice"><strong>deleteDevice</strong></a>(int device_sn)<br>Delete device</p>                                                                                                                                                                    |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setnickname"><strong>setNickname</strong></a>(String nickname)<br>Set nickname</p>                                                                                                                                                                     |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-uploadavatar"><strong>uploadAvatar</strong></a>(String avatarPath, FileProgressListener callback)<br>Upload avatar</p>                                                                                                                                 |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-downloadavatar"><strong>downloadAvatar</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md">BMXUserProfile</a> profile, boolean thumbnail, FileProgressListener callback)<br>Download avatar, default to download thumbnail</p> |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setpublicinfo"><strong>setPublicInfo</strong></a>(String publicInfo)<br>Set public extension information</p>                                                                                                                                           |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setprivateinfo"><strong>setPrivateInfo</strong></a>(String privateInfo)<br>Set private extension information</p>                                                                                                                                       |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setaddfriendauthmode"><strong>setAddFriendAuthMode</strong></a>(BMXUserProfile.AddFriendAuthMode mode)<br>Set method to validate when adding friend</p>                                                                                                |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setauthquestion"><strong>setAuthQuestion</strong></a>(BMXUserProfile.AuthQuestion authQuestion)<br>Set friend authentication questions</p>                                                                                                             |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setenablepush"><strong>setEnablePush</strong></a>(boolean enable)<br>Set whether push is allowed</p>                                                                                                                                                   |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setenablepushdetaile"><strong>setEnablePushDetaile</strong></a>(boolean enable)<br>Set whether to push details</p>                                                                                                                                     |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setpushnickname"><strong>setPushNickname</strong></a>(String nickname)<br>Set push nickname</p>                                                                                                                                                        |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setpushalias"><strong>setPushAlias</strong></a>(String alias, String bmxPushToken)<br>Set push alias</p>                                                                                                                                               |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setnotificationsound"><strong>setNotificationSound</strong></a>(boolean enable)<br>Set whether a new message is audibly alerted</p>                                                                                                                    |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setnotificationvibrate"><strong>setNotificationVibrate</strong></a>(boolean enable)<br>Set whether a new message is alerted in vibration</p>                                                                                                           |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setautodownloadattachment"><strong>setAutoDownloadAttachment</strong></a>(boolean enable)<br>Set whether to automatically download thumbnail and voice attachment</p>                                                                                  |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setautoacceptgroupinvite"><strong>setAutoAcceptGroupInvite</strong></a>(boolean enable)<br>Set whether to automatically accept group invitations</p>                                                                                                   |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-adduserlistener"><strong>addUserListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md">BMXUserServiceListener</a> listener)<br>Add user state listener</p>                                                      |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-removeuserlistener"><strong>removeUserListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md">BMXUserServiceListener</a> listener)<br>Remove user state listener</p>                                             |

## Protected Functions

|      | Name                                                                                                                                                                                   |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXUserService**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_user\_service.md#function-bmxuserservice)(long cPtr, boolean cMemoryOwn)                                           |
| void | [**finalize**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_user\_service.md#function-finalize)()                                                                                    |
| long | [**getCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_user\_service.md#function-getcptr)([BMXUserService](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_user\_service.md) obj) |

## Protected Attributes

|                   | Name                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------- |
| transient boolean | [**swigCMemOwn**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_user\_service.md#variable-swigcmemown) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function bindDevice

```java
inline BMXErrorCode bindDevice(
    String token
)
```

Binding device push token

**Parameters**:

* **token** Device token

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function getDeviceList

```java
inline BMXErrorCode getDeviceList(
    BMXDeviceList deviceList
)
```

Get device list

**Parameters**:

* **deviceList** Device list, pass in an empty list function and fetch the returned device list here

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function getProfile

```java
inline BMXErrorCode getProfile(
    BMXUserProfile profile,
    boolean forceRefresh
)
```

Get user details, force pull from server if forceRefresh == true

**Parameters**:

* **profile** User profile, initially passed in a pointing-to-empty shared\_ptr object, and fetch user profile here after the function returned.
* **forceRefresh** Whether to force pull from server, automatically if local fetch failed

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function deleteDevice

```java
inline BMXErrorCode deleteDevice(
    int device_sn
)
```

Delete device

**Parameters**:

* **device\_sn** Device serial number

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function setNickname

```java
inline BMXErrorCode setNickname(
    String nickname
)
```

Set nickname

**Parameters**:

* **nickname** User nickname

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function uploadAvatar

```java
inline BMXErrorCode uploadAvatar(
    String avatarPath,
    FileProgressListener callback
)
```

Upload avatar

**Parameters**:

* **avatarPath** Local address to upload avatar
* **callback** Upload callback function

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function downloadAvatar

```java
inline BMXErrorCode downloadAvatar(
    BMXUserProfile profile,
    boolean thumbnail,
    FileProgressListener callback
)
```

Download avatar, default to download thumbnail

**Parameters**:

* **profile** User profile
* **thumbnail** Whether to download thumbnail, true for thumbnail, false for original
* **callback** Download callback function

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function setPublicInfo

```java
inline BMXErrorCode setPublicInfo(
    String publicInfo
)
```

Set public extension information

**Parameters**:

* **publicInfo** Public extension information

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function setPrivateInfo

```java
inline BMXErrorCode setPrivateInfo(
    String privateInfo
)
```

Set private extension information

**Parameters**:

* **privateInfo** Private extension information

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function setAddFriendAuthMode

```java
inline BMXErrorCode setAddFriendAuthMode(
    BMXUserProfile.AddFriendAuthMode mode
)
```

Set method to validate when adding friend

**Parameters**:

* **mode** Add friend authentication

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function setAuthQuestion

```java
inline BMXErrorCode setAuthQuestion(
    BMXUserProfile.AuthQuestion authQuestion
)
```

Set friend authentication questions

**Parameters**:

* **authQuestion** Add friend authentication question

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function setEnablePush

```java
inline BMXErrorCode setEnablePush(
    boolean enable
)
```

Set whether push is allowed

**Parameters**:

* **enable** Whether to allow push, true to push, false not to

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function setEnablePushDetaile

```java
inline BMXErrorCode setEnablePushDetaile(
    boolean enable
)
```

Set whether to push details

**Parameters**:

* **enable** Whether to push details, true to push, false not to

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function setPushNickname

```java
inline BMXErrorCode setPushNickname(
    String nickname
)
```

Set push nickname

**Parameters**:

* **nickname** Push nickname

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function setPushAlias

```java
inline BMXErrorCode setPushAlias(
    String alias,
    String bmxPushToken
)
```

Set push alias

**Parameters**:

* **alias** Alias
* **bmxPushToken** Push token

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function setNotificationSound

```java
inline BMXErrorCode setNotificationSound(
    boolean enable
)
```

Set whether a new message is audibly alerted

**Parameters**:

* **enable** Whether to sound alert when new message received, true to alert, false not to

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function setNotificationVibrate

```java
inline BMXErrorCode setNotificationVibrate(
    boolean enable
)
```

Set whether a new message is alerted in vibration

**Parameters**:

* **enable** Whether to vibrate alert when new message received, true to alert, false not to

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function setAutoDownloadAttachment

```java
inline BMXErrorCode setAutoDownloadAttachment(
    boolean enable
)
```

Set whether to automatically download thumbnail and voice attachment

**Parameters**:

* **enable** Whether to automatically download thumbnail and voice attachment, true to download, false not to

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function setAutoAcceptGroupInvite

```java
inline BMXErrorCode setAutoAcceptGroupInvite(
    boolean enable
)
```

Set whether to automatically accept group invitations

**Parameters**:

* **enable** Whether to automatically agree to group invitation, true to agree, false not to

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function addUserListener

```java
inline void addUserListener(
    BMXUserServiceListener listener
)
```

Add user state listener

**Parameters**:

* **listener** User state listener

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function removeUserListener

```java
inline void removeUserListener(
    BMXUserServiceListener listener
)
```

Remove user state listener

**Parameters**:

* **listener** User state listener

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function BMXUserService

```java
inline BMXUserService(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function finalize

```java
inline void finalize()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```

### function getCPtr

```java
static inline long getCPtr(
    BMXUserService obj
)
```

## Protected Attributes Documentation

### variable swigCMemOwn

```java
transient boolean swigCMemOwn;
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserService'></div>
```



Updated on 2022-01-26 at 17:18:31 +0800
