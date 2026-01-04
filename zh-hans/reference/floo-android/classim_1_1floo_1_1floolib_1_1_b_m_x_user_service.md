---
title: im::floo::floolib::BMXUserService
summary: 用户Service 

---

# im::floo::floolib::BMXUserService



用户Service 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-delete)**() |
| [BMXErrorCode] | **[bindDevice](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-binddevice)**(String token)<br>绑定设备推送token  |
| [BMXErrorCode] | **[getDeviceList](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-getdevicelist)**(BMXDeviceList deviceList)<br>获取设备列表  |
| [BMXErrorCode] | **[getProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-getprofile)**([BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md) profile, boolean forceRefresh)<br>获取用户详情，如果forceRefresh == true，则强制从服务端拉取  |
| [BMXErrorCode] | **[deleteDevice](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-deletedevice)**(int device_sn)<br>删除设备  |
| [BMXErrorCode] | **[setNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setnickname)**(String nickname)<br>设置昵称  |
| [BMXErrorCode] | **[uploadAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-uploadavatar)**(String avatarPath, FileProgressListener callback)<br>上传头像  |
| [BMXErrorCode] | **[downloadAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-downloadavatar)**([BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md) profile, boolean thumbnail, FileProgressListener callback)<br>下载头像，默认下载缩略图  |
| [BMXErrorCode] | **[setPublicInfo](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setpublicinfo)**(String publicInfo)<br>设置公开扩展信息  |
| [BMXErrorCode] | **[setPrivateInfo](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setprivateinfo)**(String privateInfo)<br>设置私有扩展信息  |
| [BMXErrorCode] | **[setAddFriendAuthMode](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setaddfriendauthmode)**(BMXUserProfile.AddFriendAuthMode mode)<br>设置加好友验证方式  |
| [BMXErrorCode] | **[setAuthQuestion](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setauthquestion)**(BMXUserProfile.AuthQuestion authQuestion)<br>设置加好友验证问题  |
| [BMXErrorCode] | **[setEnablePush](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setenablepush)**(boolean enable)<br>设置是否允许推送  |
| [BMXErrorCode] | **[setEnablePushDetaile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setenablepushdetaile)**(boolean enable)<br>设置是否推送详情  |
| [BMXErrorCode] | **[setPushNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setpushnickname)**(String nickname)<br>设置推送昵称  |
| [BMXErrorCode] | **[setPushAlias](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setpushalias)**(String alias, String bmxPushToken)<br>设置推送别名  |
| [BMXErrorCode] | **[setNotificationSound](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setnotificationsound)**(boolean enable)<br>设置收到新消息是否声音提醒  |
| [BMXErrorCode] | **[setNotificationVibrate](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setnotificationvibrate)**(boolean enable)<br>设置收到新消息是否震动  |
| [BMXErrorCode] | **[setAutoDownloadAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setautodownloadattachment)**(boolean enable)<br>设置是否自动缩略图和语音附件  |
| [BMXErrorCode] | **[setAutoAcceptGroupInvite](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setautoacceptgroupinvite)**(boolean enable)<br>设置是否自动同意入群邀请  |
| void | **[addUserListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-adduserlistener)**([BMXUserServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md) listener)<br>添加用户状态监听者  |
| void | **[removeUserListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-removeuserlistener)**([BMXUserServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md) listener)<br>移除用户状态监听者  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-bmxuserservice)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-getcptr)**([BMXUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md) obj) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| transient boolean | **[swigCMemOwn](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#variable-swigcmemown)**  |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="delete" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="bindDevice" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="getDeviceList" %}{% endlanying_code_snippet %}
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

  * **profile** 用户profile信息，初始传入指向为空的shared_ptr对象，函数返回后从此处获取用户profile信息。 
  * **forceRefresh** 是否强制从服务器拉取，本地获取失败的情况下会自动从服务器拉取 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="getProfile" %}{% endlanying_code_snippet %}
```
### function deleteDevice

```java
inline BMXErrorCode deleteDevice(
    int device_sn
)
```

删除设备 

**Parameters**: 

  * **device_sn** 设备序列号 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="deleteDevice" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="setNickname" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="uploadAvatar" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="downloadAvatar" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="setPublicInfo" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="setPrivateInfo" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="setAddFriendAuthMode" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="setAuthQuestion" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="setEnablePush" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="setEnablePushDetaile" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="setPushNickname" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="setPushAlias" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="setNotificationSound" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="setNotificationVibrate" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="setAutoDownloadAttachment" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="setAutoAcceptGroupInvite" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="addUserListener" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="removeUserListener" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="BMXUserService" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="finalize" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserService",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800