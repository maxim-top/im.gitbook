---
title: floo::BMXUserService
summary: 用户Service 

---

# floo::BMXUserService



用户Service 


`#include <bmx_user_service.h>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void(int percent)> | **[Callback](classfloo_1_1_b_m_x_user_service.md#typedef-callback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXUserService](classfloo_1_1_b_m_x_user_service.md#function-~bmxuserservice)**() |
| virtual BMXErrorCode | **[bindDevice](classfloo_1_1_b_m_x_user_service.md#function-binddevice)**(const std::string & token) =0<br>绑定设备推送token  |
| virtual BMXErrorCode | **[getDeviceList](classfloo_1_1_b_m_x_user_service.md#function-getdevicelist)**(BMXDeviceList & deviceList) =0<br>获取设备列表  |
| virtual BMXErrorCode | **[deleteDevice](classfloo_1_1_b_m_x_user_service.md#function-deletedevice)**(int32_t device_sn) =0<br>删除设备  |
| virtual BMXErrorCode | **[getProfile](classfloo_1_1_b_m_x_user_service.md#function-getprofile)**(BMXUserProfilePtr & profile, bool forceRefresh) =0<br>获取用户详情，如果forceRefresh == true，则强制从服务端拉取  |
| virtual BMXErrorCode | **[setNickname](classfloo_1_1_b_m_x_user_service.md#function-setnickname)**(const std::string & nickname) =0<br>设置昵称  |
| virtual BMXErrorCode | **[uploadAvatar](classfloo_1_1_b_m_x_user_service.md#function-uploadavatar)**(const std::string & avatarPath, Callback callback) =0<br>上传头像  |
| virtual BMXErrorCode | **[downloadAvatar](classfloo_1_1_b_m_x_user_service.md#function-downloadavatar)**(BMXUserProfilePtr profile, bool thumbnail, Callback callback) =0<br>下载头像，默认下载缩略图  |
| virtual BMXErrorCode | **[setPublicInfo](classfloo_1_1_b_m_x_user_service.md#function-setpublicinfo)**(const std::string & publicInfo) =0<br>设置公开扩展信息  |
| virtual BMXErrorCode | **[setPrivateInfo](classfloo_1_1_b_m_x_user_service.md#function-setprivateinfo)**(const std::string & privateInfo) =0<br>设置私有扩展信息  |
| virtual BMXErrorCode | **[setAddFriendAuthMode](classfloo_1_1_b_m_x_user_service.md#function-setaddfriendauthmode)**([BMXUserProfile::AddFriendAuthMode](classfloo_1_1_b_m_x_user_profile.md#enum-addfriendauthmode) mode) =0<br>设置加好友验证方式  |
| virtual BMXErrorCode | **[setAuthQuestion](classfloo_1_1_b_m_x_user_service.md#function-setauthquestion)**(const [BMXUserProfile::AuthQuestion] & authQuestion) =0<br>设置加好友验证问题  |
| virtual BMXErrorCode | **[setEnablePush](classfloo_1_1_b_m_x_user_service.md#function-setenablepush)**(bool enable) =0<br>设置是否允许推送  |
| virtual BMXErrorCode | **[setEnablePushDetaile](classfloo_1_1_b_m_x_user_service.md#function-setenablepushdetaile)**(bool enable) =0<br>设置是否推送详情  |
| virtual BMXErrorCode | **[setPushNickname](classfloo_1_1_b_m_x_user_service.md#function-setpushnickname)**(const std::string & nickname) =0<br>设置推送昵称  |
| virtual BMXErrorCode | **[setPushAlias](classfloo_1_1_b_m_x_user_service.md#function-setpushalias)**(const std::string & alias, const std::string & bmxPushToken) =0 |
| virtual BMXErrorCode | **[setNotificationSound](classfloo_1_1_b_m_x_user_service.md#function-setnotificationsound)**(bool enable) =0<br>设置收到新消息是否声音提醒  |
| virtual BMXErrorCode | **[setNotificationVibrate](classfloo_1_1_b_m_x_user_service.md#function-setnotificationvibrate)**(bool enable) =0<br>设置收到新消息是否震动  |
| virtual BMXErrorCode | **[setAutoDownloadAttachment](classfloo_1_1_b_m_x_user_service.md#function-setautodownloadattachment)**(bool enable) =0<br>设置是否自动缩略图和语音附件  |
| virtual BMXErrorCode | **[setAutoAcceptGroupInvite](classfloo_1_1_b_m_x_user_service.md#function-setautoacceptgroupinvite)**(bool enable) =0<br>设置是否自动同意入群邀请  |
| virtual void | **[addUserListener](classfloo_1_1_b_m_x_user_service.md#function-adduserlistener)**([BMXUserServiceListener](classfloo_1_1_b_m_x_user_service_listener.md) * listener) =0<br>添加用户状态监听者  |
| virtual void | **[removeUserListener](classfloo_1_1_b_m_x_user_service.md#function-removeuserlistener)**([BMXUserServiceListener](classfloo_1_1_b_m_x_user_service_listener.md) * listener) =0<br>移除用户状态监听者  |

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


### function bindDevice

```cpp
virtual BMXErrorCode bindDevice(
    const std::string & token
) =0
```

绑定设备推送token 

**Parameters**: 

  * **token** 设备token 


**Return**: BMXErrorCode 

### function getDeviceList

```cpp
virtual BMXErrorCode getDeviceList(
    BMXDeviceList & deviceList
) =0
```

获取设备列表 

**Parameters**: 

  * **deviceList** 设备列表，传入空列表函数返回后从此处获取返回的设备列表 


**Return**: BMXErrorCode 

### function deleteDevice

```cpp
virtual BMXErrorCode deleteDevice(
    int32_t device_sn
) =0
```

删除设备 

**Parameters**: 

  * **device_sn** 设备序列号 


**Return**: BMXErrorCode 

### function getProfile

```cpp
virtual BMXErrorCode getProfile(
    BMXUserProfilePtr & profile,
    bool forceRefresh
) =0
```

获取用户详情，如果forceRefresh == true，则强制从服务端拉取 

**Parameters**: 

  * **profile** 用户profile信息，初始传入指向为空的shared_ptr对象，函数返回后从此处获取用户profile信息。 
  * **forceRefresh** 是否强制从服务器拉取，本地获取失败的情况下会自动从服务器拉取 


**Return**: BMXErrorCode 

### function setNickname

```cpp
virtual BMXErrorCode setNickname(
    const std::string & nickname
) =0
```

设置昵称 

**Parameters**: 

  * **nickname** 用户昵称 


**Return**: BMXErrorCode 

### function uploadAvatar

```cpp
virtual BMXErrorCode uploadAvatar(
    const std::string & avatarPath,
    Callback callback
) =0
```

上传头像 

**Parameters**: 

  * **avatarPath** 上传头像的本地地址 
  * **callback** 上传回调函数 


**Return**: BMXErrorCode 

### function downloadAvatar

```cpp
virtual BMXErrorCode downloadAvatar(
    BMXUserProfilePtr profile,
    bool thumbnail,
    Callback callback
) =0
```

下载头像，默认下载缩略图 

**Parameters**: 

  * **profile** 用户profile 
  * **thumbnail** 是否下载缩略图，true下载缩略图，false下载原图 
  * **callback** 下载回调函数 


**Return**: BMXErrorCode 

### function setPublicInfo

```cpp
virtual BMXErrorCode setPublicInfo(
    const std::string & publicInfo
) =0
```

设置公开扩展信息 

**Parameters**: 

  * **publicInfo** 公开扩展信息 


**Return**: BMXErrorCode 

### function setPrivateInfo

```cpp
virtual BMXErrorCode setPrivateInfo(
    const std::string & privateInfo
) =0
```

设置私有扩展信息 

**Parameters**: 

  * **privateInfo** 私有扩展信息 


**Return**: BMXErrorCode 

### function setAddFriendAuthMode

```cpp
virtual BMXErrorCode setAddFriendAuthMode(
    BMXUserProfile::AddFriendAuthMode mode
) =0
```

设置加好友验证方式 

**Parameters**: 

  * **mode** 加好友验证方式 


**Return**: BMXErrorCode 

### function setAuthQuestion

```cpp
virtual BMXErrorCode setAuthQuestion(
    const BMXUserProfile::AuthQuestion & authQuestion
) =0
```

设置加好友验证问题 

**Parameters**: 

  * **authQuestion** 加好友验证问题 


**Return**: BMXErrorCode 

### function setEnablePush

```cpp
virtual BMXErrorCode setEnablePush(
    bool enable
) =0
```

设置是否允许推送 

**Parameters**: 

  * **enable** 是否允许推送，true推送，false不推送 


**Return**: BMXErrorCode 

### function setEnablePushDetaile

```cpp
virtual BMXErrorCode setEnablePushDetaile(
    bool enable
) =0
```

设置是否推送详情 

**Parameters**: 

  * **enable** 是否推送详情，true推送，false不推送 


**Return**: BMXErrorCode 

### function setPushNickname

```cpp
virtual BMXErrorCode setPushNickname(
    const std::string & nickname
) =0
```

设置推送昵称 

**Parameters**: 

  * **nickname** 推送昵称 


**Return**: BMXErrorCode 

### function setPushAlias

```cpp
virtual BMXErrorCode setPushAlias(
    const std::string & alias,
    const std::string & bmxPushToken
) =0
```


**Parameters**: 

  * **nickname** 推送昵称 


**Return**: BMXErrorCode 

### function setNotificationSound

```cpp
virtual BMXErrorCode setNotificationSound(
    bool enable
) =0
```

设置收到新消息是否声音提醒 

**Parameters**: 

  * **enable** 收到新消息是否声音提醒，true提醒，false不提醒 


**Return**: BMXErrorCode 

### function setNotificationVibrate

```cpp
virtual BMXErrorCode setNotificationVibrate(
    bool enable
) =0
```

设置收到新消息是否震动 

**Parameters**: 

  * **enable** 收到新消息是否震动，true震动，false不震动 


**Return**: BMXErrorCode 

### function setAutoDownloadAttachment

```cpp
virtual BMXErrorCode setAutoDownloadAttachment(
    bool enable
) =0
```

设置是否自动缩略图和语音附件 

**Parameters**: 

  * **enable** 是否自动缩略图和语音附件，true自动下载，false不会自动下载 


**Return**: BMXErrorCode 

### function setAutoAcceptGroupInvite

```cpp
virtual BMXErrorCode setAutoAcceptGroupInvite(
    bool enable
) =0
```

设置是否自动同意入群邀请 

**Parameters**: 

  * **enable** 是否自动同意入群邀请，true同意，false不同意 


**Return**: BMXErrorCode 

### function addUserListener

```cpp
virtual void addUserListener(
    BMXUserServiceListener * listener
) =0
```

添加用户状态监听者 

**Parameters**: 

  * **listener** 用户状态监听者 


### function removeUserListener

```cpp
virtual void removeUserListener(
    BMXUserServiceListener * listener
) =0
```

移除用户状态监听者 

**Parameters**: 

  * **listener** 用户状态监听者 


## Protected Functions Documentation

### function BMXUserService

```cpp
inline BMXUserService()
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800