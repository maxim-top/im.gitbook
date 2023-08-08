---
title: floo::BMXUserService
summary: 用户Service
---

# floo::BMXUserService

用户Service

`#include <bmx_user_service.h>`

## Public Types

|                                           | Name                                                                        |
| ----------------------------------------- | --------------------------------------------------------------------------- |
| typedef std::function< void(int percent)> | [**Callback**](classfloo\_1\_1\_b\_m\_x\_user\_service.md#typedef-callback) |

## Public Functions

|                      | Name                                                                                                                                                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual              | [**\~BMXUserService**](classfloo\_1\_1\_b\_m\_x\_user\_service.md#function-\~bmxuserservice)()                                                                                                                                                                |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-binddevice"><strong>bindDevice</strong></a>(const std::string &#x26; token) =0<br>绑定设备推送token</p>                                                                                                    |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-getdevicelist"><strong>getDeviceList</strong></a>(BMXDeviceList &#x26; deviceList) =0<br>获取设备列表</p>                                                                                                  |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-deletedevice"><strong>deleteDevice</strong></a>(int32_t device_sn) =0<br>删除设备</p>                                                                                                                    |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-getprofile"><strong>getProfile</strong></a>(BMXUserProfilePtr &#x26; profile, bool forceRefresh) =0<br>获取用户详情，如果forceRefresh == true，则强制从服务端拉取</p>                                                   |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setnickname"><strong>setNickname</strong></a>(const std::string &#x26; nickname) =0<br>设置昵称</p>                                                                                                      |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-uploadavatar"><strong>uploadAvatar</strong></a>(const std::string &#x26; avatarPath, Callback callback) =0<br>上传头像</p>                                                                               |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-downloadavatar"><strong>downloadAvatar</strong></a>(BMXUserProfilePtr profile, bool thumbnail, Callback callback) =0<br>下载头像，默认下载缩略图</p>                                                             |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setpublicinfo"><strong>setPublicInfo</strong></a>(const std::string &#x26; publicInfo) =0<br>设置公开扩展信息</p>                                                                                            |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setprivateinfo"><strong>setPrivateInfo</strong></a>(const std::string &#x26; privateInfo) =0<br>设置私有扩展信息</p>                                                                                         |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setaddfriendauthmode"><strong>setAddFriendAuthMode</strong></a>(<a href="classfloo_1_1_b_m_x_user_profile.md#enum-addfriendauthmode">BMXUserProfile::AddFriendAuthMode</a> mode) =0<br>设置加好友验证方式</p> |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setauthquestion"><strong>setAuthQuestion</strong></a>(const [BMXUserProfile::AuthQuestion] &#x26; authQuestion) =0<br>设置加好友验证问题</p>                                                                  |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setenablepush"><strong>setEnablePush</strong></a>(bool enable) =0<br>设置是否允许推送</p>                                                                                                                    |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setenablepushdetaile"><strong>setEnablePushDetaile</strong></a>(bool enable) =0<br>设置是否推送详情</p>                                                                                                      |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setpushnickname"><strong>setPushNickname</strong></a>(const std::string &#x26; nickname) =0<br>设置推送昵称</p>                                                                                            |
| virtual BMXErrorCode | [**setPushAlias**](classfloo\_1\_1\_b\_m\_x\_user\_service.md#function-setpushalias)(const std::string & alias, const std::string & bmxPushToken) =0                                                                                                          |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setnotificationsound"><strong>setNotificationSound</strong></a>(bool enable) =0<br>设置收到新消息是否声音提醒</p>                                                                                                 |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setnotificationvibrate"><strong>setNotificationVibrate</strong></a>(bool enable) =0<br>设置收到新消息是否震动</p>                                                                                               |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setautodownloadattachment"><strong>setAutoDownloadAttachment</strong></a>(bool enable) =0<br>设置是否自动缩略图和语音附件</p>                                                                                      |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-setautoacceptgroupinvite"><strong>setAutoAcceptGroupInvite</strong></a>(bool enable) =0<br>设置是否自动同意入群邀请</p>                                                                                          |
| virtual void         | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-adduserlistener"><strong>addUserListener</strong></a>(<a href="classfloo_1_1_b_m_x_user_service_listener.md">BMXUserServiceListener</a> * listener) =0<br>添加用户状态监听者</p>                              |
| virtual void         | <p><a href="classfloo_1_1_b_m_x_user_service.md#function-removeuserlistener"><strong>removeUserListener</strong></a>(<a href="classfloo_1_1_b_m_x_user_service_listener.md">BMXUserServiceListener</a> * listener) =0<br>移除用户状态监听者</p>                        |

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

绑定设备推送token

**Parameters**:

* **token** 设备token

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

获取设备列表

**Parameters**:

* **deviceList** 设备列表，传入空列表函数返回后从此处获取返回的设备列表

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

删除设备

**Parameters**:

* **device\_sn** 设备序列号

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

获取用户详情，如果forceRefresh == true，则强制从服务端拉取

**Parameters**:

* **profile** 用户profile信息，初始传入指向为空的shared\_ptr对象，函数返回后从此处获取用户profile信息。
* **forceRefresh** 是否强制从服务器拉取，本地获取失败的情况下会自动从服务器拉取

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

设置昵称

**Parameters**:

* **nickname** 用户昵称

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

上传头像

**Parameters**:

* **avatarPath** 上传头像的本地地址
* **callback** 上传回调函数

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

下载头像，默认下载缩略图

**Parameters**:

* **profile** 用户profile
* **thumbnail** 是否下载缩略图，true下载缩略图，false下载原图
* **callback** 下载回调函数

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

设置公开扩展信息

**Parameters**:

* **publicInfo** 公开扩展信息

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

设置私有扩展信息

**Parameters**:

* **privateInfo** 私有扩展信息

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

设置加好友验证方式

**Parameters**:

* **mode** 加好友验证方式

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

设置加好友验证问题

**Parameters**:

* **authQuestion** 加好友验证问题

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

设置是否允许推送

**Parameters**:

* **enable** 是否允许推送，true推送，false不推送

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

设置是否推送详情

**Parameters**:

* **enable** 是否推送详情，true推送，false不推送

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

设置推送昵称

**Parameters**:

* **nickname** 推送昵称

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

* **nickname** 推送昵称

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

设置收到新消息是否声音提醒

**Parameters**:

* **enable** 收到新消息是否声音提醒，true提醒，false不提醒

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

设置收到新消息是否震动

**Parameters**:

* **enable** 收到新消息是否震动，true震动，false不震动

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

设置是否自动缩略图和语音附件

**Parameters**:

* **enable** 是否自动缩略图和语音附件，true自动下载，false不会自动下载

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

设置是否自动同意入群邀请

**Parameters**:

* **enable** 是否自动同意入群邀请，true同意，false不同意

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

添加用户状态监听者

**Parameters**:

* **listener** 用户状态监听者

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

移除用户状态监听者

**Parameters**:

* **listener** 用户状态监听者

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
