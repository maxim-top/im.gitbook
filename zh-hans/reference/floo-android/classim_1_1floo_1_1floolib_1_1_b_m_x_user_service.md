---
title: im::floo::floolib::BMXUserService
summary: 用户Service
---

# im::floo::floolib::BMXUserService

用户Service

## Public Functions

|                   | Name                                                                                                                                                                                                                                                                                           |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_user\_service.md#function-delete)()                                                                                                                                                                                                |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-binddevice"><strong>bindDevice</strong></a>(String token)<br>绑定设备推送token</p>                                                                                                                                         |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-getdevicelist"><strong>getDeviceList</strong></a>(BMXDeviceList deviceList)<br>获取设备列表</p>                                                                                                                            |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-getprofile"><strong>getProfile</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md">BMXUserProfile</a> profile, boolean forceRefresh)<br>获取用户详情，如果forceRefresh == true，则强制从服务端拉取</p>          |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-deletedevice"><strong>deleteDevice</strong></a>(int device_sn)<br>删除设备</p>                                                                                                                                           |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setnickname"><strong>setNickname</strong></a>(String nickname)<br>设置昵称</p>                                                                                                                                           |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-uploadavatar"><strong>uploadAvatar</strong></a>(String avatarPath, FileProgressListener callback)<br>上传头像</p>                                                                                                        |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-downloadavatar"><strong>downloadAvatar</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md">BMXUserProfile</a> profile, boolean thumbnail, FileProgressListener callback)<br>下载头像，默认下载缩略图</p> |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setpublicinfo"><strong>setPublicInfo</strong></a>(String publicInfo)<br>设置公开扩展信息</p>                                                                                                                                 |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setprivateinfo"><strong>setPrivateInfo</strong></a>(String privateInfo)<br>设置私有扩展信息</p>                                                                                                                              |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setaddfriendauthmode"><strong>setAddFriendAuthMode</strong></a>(BMXUserProfile.AddFriendAuthMode mode)<br>设置加好友验证方式</p>                                                                                              |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setauthquestion"><strong>setAuthQuestion</strong></a>(BMXUserProfile.AuthQuestion authQuestion)<br>设置加好友验证问题</p>                                                                                                     |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setenablepush"><strong>setEnablePush</strong></a>(boolean enable)<br>设置是否允许推送</p>                                                                                                                                    |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setenablepushdetaile"><strong>setEnablePushDetaile</strong></a>(boolean enable)<br>设置是否推送详情</p>                                                                                                                      |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setpushnickname"><strong>setPushNickname</strong></a>(String nickname)<br>设置推送昵称</p>                                                                                                                                 |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setpushalias"><strong>setPushAlias</strong></a>(String alias, String bmxPushToken)<br>设置推送别名</p>                                                                                                                     |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setnotificationsound"><strong>setNotificationSound</strong></a>(boolean enable)<br>设置收到新消息是否声音提醒</p>                                                                                                                 |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setnotificationvibrate"><strong>setNotificationVibrate</strong></a>(boolean enable)<br>设置收到新消息是否震动</p>                                                                                                               |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setautodownloadattachment"><strong>setAutoDownloadAttachment</strong></a>(boolean enable)<br>设置是否自动缩略图和语音附件</p>                                                                                                      |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setautoacceptgroupinvite"><strong>setAutoAcceptGroupInvite</strong></a>(boolean enable)<br>设置是否自动同意入群邀请</p>                                                                                                          |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-adduserlistener"><strong>addUserListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md">BMXUserServiceListener</a> listener)<br>添加用户状态监听者</p>                                  |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-removeuserlistener"><strong>removeUserListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md">BMXUserServiceListener</a> listener)<br>移除用户状态监听者</p>                            |

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

绑定设备推送token

**Parameters**:

* **token** 设备token

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

获取设备列表

**Parameters**:

* **deviceList** 设备列表，传入空列表函数返回后从此处获取返回的设备列表

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

获取用户详情，如果forceRefresh == true，则强制从服务端拉取

**Parameters**:

* **profile** 用户profile信息，初始传入指向为空的shared\_ptr对象，函数返回后从此处获取用户profile信息。
* **forceRefresh** 是否强制从服务器拉取，本地获取失败的情况下会自动从服务器拉取

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

删除设备

**Parameters**:

* **device\_sn** 设备序列号

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

设置昵称

**Parameters**:

* **nickname** 用户昵称

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

上传头像

**Parameters**:

* **avatarPath** 上传头像的本地地址
* **callback** 上传回调函数

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

下载头像，默认下载缩略图

**Parameters**:

* **profile** 用户profile
* **thumbnail** 是否下载缩略图，true下载缩略图，false下载原图
* **callback** 下载回调函数

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

设置公开扩展信息

**Parameters**:

* **publicInfo** 公开扩展信息

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

设置私有扩展信息

**Parameters**:

* **privateInfo** 私有扩展信息

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

设置加好友验证方式

**Parameters**:

* **mode** 加好友验证方式

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

设置加好友验证问题

**Parameters**:

* **authQuestion** 加好友验证问题

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

设置是否允许推送

**Parameters**:

* **enable** 是否允许推送，true推送，false不推送

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

设置是否推送详情

**Parameters**:

* **enable** 是否推送详情，true推送，false不推送

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

设置推送昵称

**Parameters**:

* **nickname** 推送昵称

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

设置推送别名

**Parameters**:

* **alias** 别名
* **bmxPushToken** 推送token

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

设置收到新消息是否声音提醒

**Parameters**:

* **enable** 收到新消息是否声音提醒，true提醒，false不提醒

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

设置收到新消息是否震动

**Parameters**:

* **enable** 收到新消息是否震动，true震动，false不震动

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

设置是否自动缩略图和语音附件

**Parameters**:

* **enable** 是否自动缩略图和语音附件，true自动下载，false不会自动下载

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

设置是否自动同意入群邀请

**Parameters**:

* **enable** 是否自动同意入群邀请，true同意，false不同意

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

添加用户状态监听者

**Parameters**:

* **listener** 用户状态监听者

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

移除用户状态监听者

**Parameters**:

* **listener** 用户状态监听者

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
