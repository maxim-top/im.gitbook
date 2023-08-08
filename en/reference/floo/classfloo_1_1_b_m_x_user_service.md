---
title: floo::BMXUserService
summary: User Service
---

# floo::BMXUserService

User Service

`#include <bmx_user_service.h>`

## Public Types

|                                           | Name                                                                        |
| ----------------------------------------- | --------------------------------------------------------------------------- |
| typedef std::function< void(int percent)> | [**Callback**](classfloo\_1\_1\_b\_m\_x\_user\_service.md#typedef-callback) |

## Public Functions

|                      | Name                                                                                                                                                                                                                                                                                          |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual              | [**\~BMXUserService**](classfloo\_1\_1\_b\_m\_x\_user\_service.md#function-\~bmxuserservice)()                                                                                                                                                                                                |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-binddevice"><strong>bindDevice</strong></a>(const std::string &#x26; token) =0<br>Binding device push token</p>                                                                                                                      |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-getdevicelist"><strong>getDeviceList</strong></a>(BMXDeviceList &#x26; deviceList) =0<br>Get device list</p>                                                                                                                         |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-deletedevice"><strong>deleteDevice</strong></a>(int32_t device_sn) =0<br>Delete device</p>                                                                                                                                           |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-getprofile"><strong>getProfile</strong></a>(BMXUserProfilePtr &#x26; profile, bool forceRefresh) =0<br>Get user details, force pull from server if forceRefresh == true</p>                                                          |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setnickname"><strong>setNickname</strong></a>(const std::string &#x26; nickname) =0<br>Set nickname</p>                                                                                                                              |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-uploadavatar"><strong>uploadAvatar</strong></a>(const std::string &#x26; avatarPath, Callback callback) =0<br>Upload avatar</p>                                                                                                      |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-downloadavatar"><strong>downloadAvatar</strong></a>(BMXUserProfilePtr profile, bool thumbnail, Callback callback) =0<br>Download avatar, default to download thumbnail</p>                                                           |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setpublicinfo"><strong>setPublicInfo</strong></a>(const std::string &#x26; publicInfo) =0<br>Set public extension information</p>                                                                                                    |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setprivateinfo"><strong>setPrivateInfo</strong></a>(const std::string &#x26; privateInfo) =0<br>Set private extension information</p>                                                                                                |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setaddfriendauthmode"><strong>setAddFriendAuthMode</strong></a>(<a href="classfloo_1_1_b_m_x_user_profile.md#enum-addfriendauthmode">BMXUserProfile::AddFriendAuthMode</a> mode) =0<br>Set method to validate when adding friend</p> |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setauthquestion"><strong>setAuthQuestion</strong></a>(const [BMXUserProfile::AuthQuestion] &#x26; authQuestion) =0<br>Set friend authentication questions</p>                                                                        |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setenablepush"><strong>setEnablePush</strong></a>(bool enable) =0<br>Set whether push is allowed</p>                                                                                                                                 |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setenablepushdetaile"><strong>setEnablePushDetaile</strong></a>(bool enable) =0<br>Set whether to push details</p>                                                                                                                   |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setpushnickname"><strong>setPushNickname</strong></a>(const std::string &#x26; nickname) =0<br>Set push nickname</p>                                                                                                                 |
| virtual BMXErrorCode | [**setPushAlias**](classfloo\_1\_1\_b\_m\_x\_user\_service.md#function-setpushalias)(const std::string & alias, const std::string & bmxPushToken) =0                                                                                                                                          |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setnotificationsound"><strong>setNotificationSound</strong></a>(bool enable) =0<br>Set whether a new message is audibly alerted</p>                                                                                                  |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setnotificationvibrate"><strong>setNotificationVibrate</strong></a>(bool enable) =0<br>Set whether a new message is alerted in vibration</p>                                                                                         |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setautodownloadattachment"><strong>setAutoDownloadAttachment</strong></a>(bool enable) =0<br>Set whether to automatically download thumbnail and voice attachment</p>                                                                |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setautoacceptgroupinvite"><strong>setAutoAcceptGroupInvite</strong></a>(bool enable) =0<br>Set whether to automatically accept group invitations</p>                                                                                 |
| virtual void         | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-adduserlistener"><strong>addUserListener</strong></a>(<a href="classfloo_1_1_b_m_x_user_service_listener.md">BMXUserServiceListener</a> * listener) =0<br>Add user state listener</p>                                                |
| virtual void         | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-removeuserlistener"><strong>removeUserListener</strong></a>(<a href="classfloo_1_1_b_m_x_user_service_listener.md">BMXUserServiceListener</a> * listener) =0<br>Remove user state listener</p>                                       |

## Protected Functions

|   | Name                                                                                       |
| - | ------------------------------------------------------------------------------------------ |
|   | [**BMXUserService**](classfloo\_1\_1\_b\_m\_x\_user\_service.md#function-bmxuserservice)() |

## Public Types Documentation

### typedef Callback

```cpp
typedef std::function<void(int percent)> floo::BMXUserService::Callback;
```

## Public Functions Documentation

### function \~BMXUserService

```cpp
inline virtual ~BMXUserService()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function bindDevice

```cpp
virtual BMXErrorCode bindDevice(
    const std::string & token
) =0
```

Binding device push token

**Parameters**:

* **token** Device token

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function getDeviceList

```cpp
virtual BMXErrorCode getDeviceList(
    BMXDeviceList & deviceList
) =0
```

Get device list

**Parameters**:

* **deviceList** Device list, pass in an empty list function and fetch the returned device list here

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function deleteDevice

```cpp
virtual BMXErrorCode deleteDevice(
    int32_t device_sn
) =0
```

Delete device

**Parameters**:

* **device\_sn** Device serial number

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function getProfile

```cpp
virtual BMXErrorCode getProfile(
    BMXUserProfilePtr & profile,
    bool forceRefresh
) =0
```

Get user details, force pull from server if forceRefresh == true

**Parameters**:

* **profile** User profile, initially passed in a pointing-to-empty shared\_ptr object, and fetch user profile here after the function returned.
* **forceRefresh** Whether to force pull from server, automatically if local fetch failed

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function setNickname

```cpp
virtual BMXErrorCode setNickname(
    const std::string & nickname
) =0
```

Set nickname

**Parameters**:

* **nickname** User nickname

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function uploadAvatar

```cpp
virtual BMXErrorCode uploadAvatar(
    const std::string & avatarPath,
    Callback callback
) =0
```

Upload avatar

**Parameters**:

* **avatarPath** Local address to upload avatar
* **callback** Upload callback function

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function downloadAvatar

```cpp
virtual BMXErrorCode downloadAvatar(
    BMXUserProfilePtr profile,
    bool thumbnail,
    Callback callback
) =0
```

Download avatar, default to download thumbnail

**Parameters**:

* **profile** User profile
* **thumbnail** Whether to download thumbnail, true for thumbnail, false for original
* **callback** Download callback function

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function setPublicInfo

```cpp
virtual BMXErrorCode setPublicInfo(
    const std::string & publicInfo
) =0
```

Set public extension information

**Parameters**:

* **publicInfo** Public extension information

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function setPrivateInfo

```cpp
virtual BMXErrorCode setPrivateInfo(
    const std::string & privateInfo
) =0
```

Set private extension information

**Parameters**:

* **privateInfo** Private extension information

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function setAddFriendAuthMode

```cpp
virtual BMXErrorCode setAddFriendAuthMode(
    BMXUserProfile::AddFriendAuthMode mode
) =0
```

Set method to validate when adding friend

**Parameters**:

* **mode** Add friend authentication

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function setAuthQuestion

```cpp
virtual BMXErrorCode setAuthQuestion(
    const BMXUserProfile::AuthQuestion & authQuestion
) =0
```

Set friend authentication questions

**Parameters**:

* **authQuestion** Add friend authentication question

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function setEnablePush

```cpp
virtual BMXErrorCode setEnablePush(
    bool enable
) =0
```

Set whether push is allowed

**Parameters**:

* **enable** Whether to allow push, true to push, false not to

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function setEnablePushDetaile

```cpp
virtual BMXErrorCode setEnablePushDetaile(
    bool enable
) =0
```

Set whether to push details

**Parameters**:

* **enable** Whether to push details, true to push, false not to

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function setPushNickname

```cpp
virtual BMXErrorCode setPushNickname(
    const std::string & nickname
) =0
```

Set push nickname

**Parameters**:

* **nickname** Push nickname

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function setPushAlias

```cpp
virtual BMXErrorCode setPushAlias(
    const std::string & alias,
    const std::string & bmxPushToken
) =0
```

**Parameters**:

* **nickname** Push nickname

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function setNotificationSound

```cpp
virtual BMXErrorCode setNotificationSound(
    bool enable
) =0
```

Set whether a new message is audibly alerted

**Parameters**:

* **enable** Whether to sound alert when new message received, true to alert, false not to

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function setNotificationVibrate

```cpp
virtual BMXErrorCode setNotificationVibrate(
    bool enable
) =0
```

Set whether a new message is alerted in vibration

**Parameters**:

* **enable** Whether to vibrate alert when new message received, true to alert, false not to

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function setAutoDownloadAttachment

```cpp
virtual BMXErrorCode setAutoDownloadAttachment(
    bool enable
) =0
```

Set whether to automatically download thumbnail and voice attachment

**Parameters**:

* **enable** Whether to automatically download thumbnail and voice attachment, true to download, false not to

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function setAutoAcceptGroupInvite

```cpp
virtual BMXErrorCode setAutoAcceptGroupInvite(
    bool enable
) =0
```

Set whether to automatically accept group invitations

**Parameters**:

* **enable** Whether to automatically agree to group invitation, true to agree, false not to

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function addUserListener

```cpp
virtual void addUserListener(
    BMXUserServiceListener * listener
) =0
```

Add user state listener

**Parameters**:

* **listener** User state listener

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function removeUserListener

```cpp
virtual void removeUserListener(
    BMXUserServiceListener * listener
) =0
```

Remove user state listener

**Parameters**:

* **listener** User state listener

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```

### function BMXUserService

```cpp
inline BMXUserService()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserService'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
