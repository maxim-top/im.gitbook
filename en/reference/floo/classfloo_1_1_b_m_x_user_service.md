---
title: floo::BMXUserService
summary: User Service 

---

# floo::BMXUserService



User Service 


`#include <bmx_user_service.h>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void(int percent)> | **[Callback](classfloo_1_1_b_m_x_user_service.md#typedef-callback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXUserService](classfloo_1_1_b_m_x_user_service.md#function-~bmxuserservice)**() |
| virtual BMXErrorCode | **[bindDevice](classfloo_1_1_b_m_x_user_service.md#function-binddevice)**(const std::string & token) =0<br>Binding device push token  |
| virtual BMXErrorCode | **[getDeviceList](classfloo_1_1_b_m_x_user_service.md#function-getdevicelist)**(BMXDeviceList & deviceList) =0<br>Get device list  |
| virtual BMXErrorCode | **[deleteDevice](classfloo_1_1_b_m_x_user_service.md#function-deletedevice)**(int32_t device_sn) =0<br>Delete device  |
| virtual BMXErrorCode | **[getProfile](classfloo_1_1_b_m_x_user_service.md#function-getprofile)**(BMXUserProfilePtr & profile, bool forceRefresh) =0<br>Get user details, force pull from server if forceRefresh == true  |
| virtual BMXErrorCode | **[setNickname](classfloo_1_1_b_m_x_user_service.md#function-setnickname)**(const std::string & nickname) =0<br>Set nickname  |
| virtual BMXErrorCode | **[uploadAvatar](classfloo_1_1_b_m_x_user_service.md#function-uploadavatar)**(const std::string & avatarPath, Callback callback) =0<br>Upload avatar  |
| virtual BMXErrorCode | **[downloadAvatar](classfloo_1_1_b_m_x_user_service.md#function-downloadavatar)**(BMXUserProfilePtr profile, bool thumbnail, Callback callback) =0<br>Download avatar, default to download thumbnail  |
| virtual BMXErrorCode | **[setPublicInfo](classfloo_1_1_b_m_x_user_service.md#function-setpublicinfo)**(const std::string & publicInfo) =0<br>Set public extension information  |
| virtual BMXErrorCode | **[setPrivateInfo](classfloo_1_1_b_m_x_user_service.md#function-setprivateinfo)**(const std::string & privateInfo) =0<br>Set private extension information  |
| virtual BMXErrorCode | **[setAddFriendAuthMode](classfloo_1_1_b_m_x_user_service.md#function-setaddfriendauthmode)**([BMXUserProfile::AddFriendAuthMode](classfloo_1_1_b_m_x_user_profile.md#enum-addfriendauthmode) mode) =0<br>Set method to validate when adding friend  |
| virtual BMXErrorCode | **[setAuthQuestion](classfloo_1_1_b_m_x_user_service.md#function-setauthquestion)**(const [BMXUserProfile::AuthQuestion] & authQuestion) =0<br>Set friend authentication questions  |
| virtual BMXErrorCode | **[setEnablePush](classfloo_1_1_b_m_x_user_service.md#function-setenablepush)**(bool enable) =0<br>Set whether push is allowed  |
| virtual BMXErrorCode | **[setEnablePushDetaile](classfloo_1_1_b_m_x_user_service.md#function-setenablepushdetaile)**(bool enable) =0<br>Set whether to push details  |
| virtual BMXErrorCode | **[setPushNickname](classfloo_1_1_b_m_x_user_service.md#function-setpushnickname)**(const std::string & nickname) =0<br>Set push nickname  |
| virtual BMXErrorCode | **[setPushAlias](classfloo_1_1_b_m_x_user_service.md#function-setpushalias)**(const std::string & alias, const std::string & bmxPushToken) =0 |
| virtual BMXErrorCode | **[setNotificationSound](classfloo_1_1_b_m_x_user_service.md#function-setnotificationsound)**(bool enable) =0<br>Set whether a new message is audibly alerted  |
| virtual BMXErrorCode | **[setNotificationVibrate](classfloo_1_1_b_m_x_user_service.md#function-setnotificationvibrate)**(bool enable) =0<br>Set whether a new message is alerted in vibration  |
| virtual BMXErrorCode | **[setAutoDownloadAttachment](classfloo_1_1_b_m_x_user_service.md#function-setautodownloadattachment)**(bool enable) =0<br>Set whether to automatically download thumbnail and voice attachment  |
| virtual BMXErrorCode | **[setAutoAcceptGroupInvite](classfloo_1_1_b_m_x_user_service.md#function-setautoacceptgroupinvite)**(bool enable) =0<br>Set whether to automatically accept group invitations  |
| virtual void | **[addUserListener](classfloo_1_1_b_m_x_user_service.md#function-adduserlistener)**([BMXUserServiceListener](classfloo_1_1_b_m_x_user_service_listener.md) * listener) =0<br>Add user state listener  |
| virtual void | **[removeUserListener](classfloo_1_1_b_m_x_user_service.md#function-removeuserlistener)**([BMXUserServiceListener](classfloo_1_1_b_m_x_user_service_listener.md) * listener) =0<br>Remove user state listener  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXUserService](classfloo_1_1_b_m_x_user_service.md#function-bmxuserservice)**() |

## Public Types Documentation

### typedef Callback

```cpp
typedef std::function<void(int percent)> floo::BMXUserService::Callback;
```


## Public Functions Documentation

### function ~BMXUserService

```cpp
inline virtual ~BMXUserService()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="~BMXUserService" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="bindDevice" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="getDeviceList" %}{% endlanying_code_snippet %}
```
### function deleteDevice

```cpp
virtual BMXErrorCode deleteDevice(
    int32_t device_sn
) =0
```

Delete device 

**Parameters**: 

  * **device_sn** Device serial number 


**Return**: BMXErrorCode 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="deleteDevice" %}{% endlanying_code_snippet %}
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

  * **profile** User profile, initially passed in a pointing-to-empty shared_ptr object, and fetch user profile here after the function returned. 
  * **forceRefresh** Whether to force pull from server, automatically if local fetch failed 


**Return**: BMXErrorCode 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="getProfile" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="setNickname" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="uploadAvatar" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="downloadAvatar" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="setPublicInfo" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="setPrivateInfo" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="setAddFriendAuthMode" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="setAuthQuestion" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="setEnablePush" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="setEnablePushDetaile" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="setPushNickname" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="setPushAlias" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="setNotificationSound" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="setNotificationVibrate" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="setAutoDownloadAttachment" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="setAutoAcceptGroupInvite" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="addUserListener" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="removeUserListener" %}{% endlanying_code_snippet %}
```
### function BMXUserService

```cpp
inline BMXUserService()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXUserService",function="BMXUserService" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800