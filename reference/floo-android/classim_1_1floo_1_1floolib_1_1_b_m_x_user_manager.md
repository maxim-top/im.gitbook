---
title: im::floo::floolib::BMXUserManager
summary: 用户管理器 

---

# im::floo::floolib::BMXUserManager



用户管理器 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXUserManager](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-bmxusermanager)**([BMXUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md) service, [BMXClient](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md) bmxClient) |
| void | **[signUpNewUser](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signupnewuser)**(final String username, final String password, final BMXDataCallBack< [BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md) > callBack)<br>注册  |
| void | **[signInByName](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signinbyname)**(final String name, final String password, final BMXCallBack callBack)<br>用户名登陆  |
| void | **[signInById](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signinbyid)**(final long id, final String password, final BMXCallBack callBack)<br>id 登陆  |
| void | **[autoSignInByName](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-autosigninbyname)**(final String name, final String password, final BMXCallBack callBack)<br>自动登陆 根据用户名  |
| void | **[autoSignInById](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-autosigninbyid)**(final long uid, final String password, final BMXCallBack callBack)<br>自动登陆 根据id  |
| void | **[signOut](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signout)**(final BMXCallBack callBack)<br>退出登录  |
| void | **[signOut](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signout)**(final long userId, final BMXCallBack callBack)<br>退出登录  |
| [BMXConnectStatus] | **[connectStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-connectstatus)**()<br>获取当前和服务器的连接状态  |
| [BMXSignInStatus] | **[signInStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signinstatus)**()<br>获取当前的登录状态  |
| void | **[bindDevice](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-binddevice)**(final String token, final BMXCallBack callBack)<br>绑定设备推送token  |
| void | **[getDeviceList](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-getdevicelist)**(final BMXDataCallBack< BMXDeviceList > callBack)<br>获取登录的设备列表  |
| void | **[deleteDevice](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-deletedevice)**(final int device_sn, final BMXCallBack callBack)<br>删除设备  |
| void | **[getProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-getprofile)**(final boolean forceRefresh, final BMXDataCallBack< [BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md) > callBack)<br>获取用户详情  |
| void | **[setNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setnickname)**(final String nickname, final BMXCallBack callBack)<br>设置昵称  |
| void | **[uploadAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-uploadavatar)**(final String avatarPath, final FileProgressListener listener, final BMXCallBack callBack)<br>上传头像  |
| void | **[downloadAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-downloadavatar)**(final [BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md) profile, final FileProgressListener listener, final BMXCallBack callBack)<br>下载头像  |
| void | **[setPublicInfo](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setpublicinfo)**(final String publicInfo, final BMXCallBack callBack)<br>设置公开扩展信息  |
| void | **[setPrivateInfo](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setprivateinfo)**(final String privateInfo, final BMXCallBack callBack)<br>设置私有扩展信息  |
| void | **[setAddFriendAuthMode](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setaddfriendauthmode)**(final BMXUserProfile.AddFriendAuthMode mode, final BMXCallBack callBack)<br>设置加好友验证方式  |
| void | **[setAuthQuestion](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setauthquestion)**(final BMXUserProfile.AuthQuestion authQuestion, final BMXCallBack callBack)<br>设置加好友验证问题  |
| void | **[setEnablePush](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setenablepush)**(final boolean enable, final BMXCallBack callBack)<br>设置是否允许推送  |
| void | **[setEnablePushDetaile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setenablepushdetaile)**(final boolean enable, final BMXCallBack callBack)<br>设置是否推送详情  |
| void | **[setPushNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setpushnickname)**(final String nickname, final BMXCallBack callBack)<br>设置推送昵称  |
| void | **[setPushAlias](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setpushalias)**(final String alias, final String bmxPushToken, final BMXCallBack callBack)<br>设置推送别名  |
| void | **[setNotificationSound](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setnotificationsound)**(final boolean enable, final BMXCallBack callBack)<br>设置收到新消息是否声音提醒  |
| void | **[setNotificationVibrate](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setnotificationvibrate)**(final boolean enable, final BMXCallBack callBack)<br>设置收到新消息是否震动  |
| void | **[setAutoDownloadAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setautodownloadattachment)**(final boolean enable, final BMXCallBack callBack)<br>设置是否自动缩略图和语音附件  |
| void | **[setAutoAcceptGroupInvite](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setautoacceptgroupinvite)**(final boolean enable, final BMXCallBack callBack)<br>设置是否自动同意入群邀请  |
| void | **[addUserListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-adduserlistener)**([BMXUserServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md) listener)<br>添加用户状态监听者  |
| void | **[removeUserListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-removeuserlistener)**([BMXUserServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md) listener)<br>移除用户状态监听者  |
| void | **[changeAppId](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-changeappid)**(final String appId, final BMXCallBack callBack)<br>切换appId  |

## Public Functions Documentation

### function BMXUserManager

```java
inline BMXUserManager(
    BMXUserService service,
    BMXClient bmxClient
)
```


### function signUpNewUser

```java
inline void signUpNewUser(
    final String username,
    final String password,
    final BMXDataCallBack< BMXUserProfile > callBack
)
```

注册 

**Parameters**: 

  * **password** 密码 
  * **username** 用户名 
  * **callBack** [BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md)


### function signInByName

```java
inline void signInByName(
    final String name,
    final String password,
    final BMXCallBack callBack
)
```

用户名登陆 

**Parameters**: 

  * **name** 
  * **password** 
  * **callBack** [BMXErrorCode]


### function signInById

```java
inline void signInById(
    final long id,
    final String password,
    final BMXCallBack callBack
)
```

id 登陆 

**Parameters**: 

  * **id** 
  * **password** 
  * **callBack** [BMXErrorCode]


### function autoSignInByName

```java
inline void autoSignInByName(
    final String name,
    final String password,
    final BMXCallBack callBack
)
```

自动登陆 根据用户名 

**Parameters**: 

  * **name** 
  * **password** 
  * **callBack** [BMXErrorCode]


### function autoSignInById

```java
inline void autoSignInById(
    final long uid,
    final String password,
    final BMXCallBack callBack
)
```

自动登陆 根据id 

**Parameters**: 

  * **uid** 
  * **password** 
  * **callBack** [BMXErrorCode]


### function signOut

```java
inline void signOut(
    final BMXCallBack callBack
)
```

退出登录 

**Parameters**: 

  * **callBack** [BMXErrorCode]


### function signOut

```java
inline void signOut(
    final long userId,
    final BMXCallBack callBack
)
```

退出登录 

**Parameters**: 

  * **callBack** [BMXErrorCode]


### function connectStatus

```java
inline BMXConnectStatus connectStatus()
```

获取当前和服务器的连接状态 

### function signInStatus

```java
inline BMXSignInStatus signInStatus()
```

获取当前的登录状态 

### function bindDevice

```java
inline void bindDevice(
    final String token,
    final BMXCallBack callBack
)
```

绑定设备推送token 

**Parameters**: 

  * **token** device token 
  * **callBack** [BMXErrorCode]


### function getDeviceList

```java
inline void getDeviceList(
    final BMXDataCallBack< BMXDeviceList > callBack
)
```

获取登录的设备列表 

**Parameters**: 

  * **callBack** [BMXErrorCode] 登录的设备列表 


### function deleteDevice

```java
inline void deleteDevice(
    final int device_sn,
    final BMXCallBack callBack
)
```

删除设备 

**Parameters**: 

  * **callBack** [BMXErrorCode]


### function getProfile

```java
inline void getProfile(
    final boolean forceRefresh,
    final BMXDataCallBack< BMXUserProfile > callBack
)
```

获取用户详情 

**Parameters**: 

  * **forceRefresh** 强制从服务器拉取最新结果 
  * **callBack** [BMXErrorCode],用户详情 


### function setNickname

```java
inline void setNickname(
    final String nickname,
    final BMXCallBack callBack
)
```

设置昵称 

**Parameters**: 

  * **nickname** 昵称 
  * **callBack** [BMXErrorCode]


### function uploadAvatar

```java
inline void uploadAvatar(
    final String avatarPath,
    final FileProgressListener listener,
    final BMXCallBack callBack
)
```

上传头像 

**Parameters**: 

  * **avatarPath** 头像本地文件路径 
  * **listener** 上传进度监听器 
  * **callBack** [BMXErrorCode]


### function downloadAvatar

```java
inline void downloadAvatar(
    final BMXUserProfile profile,
    final FileProgressListener listener,
    final BMXCallBack callBack
)
```

下载头像 

**Parameters**: 

  * **profile** 用户详情 
  * **listener** 下载进度监听器 
  * **callBack** [BMXErrorCode]


### function setPublicInfo

```java
inline void setPublicInfo(
    final String publicInfo,
    final BMXCallBack callBack
)
```

设置公开扩展信息 

**Parameters**: 

  * **publicInfo** 用户公开信息 
  * **callBack** [BMXErrorCode]


### function setPrivateInfo

```java
inline void setPrivateInfo(
    final String privateInfo,
    final BMXCallBack callBack
)
```

设置私有扩展信息 

**Parameters**: 

  * **privateInfo** 用户私有信息（只对自己可见） 
  * **callBack** [BMXErrorCode]


### function setAddFriendAuthMode

```java
inline void setAddFriendAuthMode(
    final BMXUserProfile.AddFriendAuthMode mode,
    final BMXCallBack callBack
)
```

设置加好友验证方式 

**Parameters**: 

  * **mode** 添加好友时的验证方式 
  * **callBack** [BMXErrorCode]


### function setAuthQuestion

```java
inline void setAuthQuestion(
    final BMXUserProfile.AuthQuestion authQuestion,
    final BMXCallBack callBack
)
```

设置加好友验证问题 

**Parameters**: 

  * **authQuestion** 验证问题 
  * **callBack** [BMXErrorCode]


### function setEnablePush

```java
inline void setEnablePush(
    final boolean enable,
    final BMXCallBack callBack
)
```

设置是否允许推送 

**Parameters**: 

  * **enable** 是否允许推送，true推送，false不推送 
  * **callBack** [BMXErrorCode]


### function setEnablePushDetaile

```java
inline void setEnablePushDetaile(
    final boolean enable,
    final BMXCallBack callBack
)
```

设置是否推送详情 

**Parameters**: 

  * **enable** 是否推送详情，true推送，false不推送 
  * **callBack** [BMXErrorCode]


### function setPushNickname

```java
inline void setPushNickname(
    final String nickname,
    final BMXCallBack callBack
)
```

设置推送昵称 

**Parameters**: 

  * **nickname** 推送昵称 
  * **callBack** [BMXErrorCode]


### function setPushAlias

```java
inline void setPushAlias(
    final String alias,
    final String bmxPushToken,
    final BMXCallBack callBack
)
```

设置推送别名 

**Parameters**: 

  * **alias** 别名 
  * **bmxPushToken** 推送token 
  * **callBack** [BMXErrorCode]


### function setNotificationSound

```java
inline void setNotificationSound(
    final boolean enable,
    final BMXCallBack callBack
)
```

设置收到新消息是否声音提醒 

**Parameters**: 

  * **enable** 收到新消息是否声音提醒，true提醒，false不提醒 
  * **callBack** [BMXErrorCode]


### function setNotificationVibrate

```java
inline void setNotificationVibrate(
    final boolean enable,
    final BMXCallBack callBack
)
```

设置收到新消息是否震动 

**Parameters**: 

  * **enable** 收到新消息是否震动，true震动，false不震动 
  * **callBack** [BMXErrorCode]


### function setAutoDownloadAttachment

```java
inline void setAutoDownloadAttachment(
    final boolean enable,
    final BMXCallBack callBack
)
```

设置是否自动缩略图和语音附件 

**Parameters**: 

  * **enable** 是否自动缩略图和语音附件，true自动下载，false不会自动下载 
  * **callBack** [BMXErrorCode]


### function setAutoAcceptGroupInvite

```java
inline void setAutoAcceptGroupInvite(
    final boolean enable,
    final BMXCallBack callBack
)
```

设置是否自动同意入群邀请 

**Parameters**: 

  * **enable** 是否自动同意入群邀请，true同意，false不同意 
  * **callBack** [BMXErrorCode]


### function addUserListener

```java
inline void addUserListener(
    BMXUserServiceListener listener
)
```

添加用户状态监听者 

**Parameters**: 

  * **listener** 用户状态监听者 


### function removeUserListener

```java
inline void removeUserListener(
    BMXUserServiceListener listener
)
```

移除用户状态监听者 

**Parameters**: 

  * **listener** 用户状态监听者 


### function changeAppId

```java
inline void changeAppId(
    final String appId,
    final BMXCallBack callBack
)
```

切换appId 

**Parameters**: 

  * **appId** appId 


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800