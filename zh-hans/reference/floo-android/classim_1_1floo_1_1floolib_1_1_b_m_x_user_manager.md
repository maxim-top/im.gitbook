---
title: im::floo::floolib::BMXUserManager
summary: 用户管理器
---

# im::floo::floolib::BMXUserManager

用户管理器

## Public Functions

|                     | Name                                                                                                                                                                                                                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                     | [**BMXUserManager**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-bmxusermanager)([BMXUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md) service, [BMXClient](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md) bmxClient)                                                     |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signupnewuser"><strong>signUpNewUser</strong></a>(final String username, final String password, final BMXDataCallBack&#x3C; <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md">BMXUserProfile</a> > callBack)<br>注册</p> |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signinbyname"><strong>signInByName</strong></a>(final String name, final String password, final BMXCallBack callBack)<br>用户名登陆</p>                                                                                                  |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signinbyid"><strong>signInById</strong></a>(final long id, final String password, final BMXCallBack callBack)<br>id 登陆</p>                                                                                                          |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-autosigninbyname"><strong>autoSignInByName</strong></a>(final String name, final String password, final BMXCallBack callBack)<br>自动登陆 根据用户名</p>                                                                                     |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-autosigninbyid"><strong>autoSignInById</strong></a>(final long uid, final String password, final BMXCallBack callBack)<br>自动登陆 根据id</p>                                                                                             |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signout"><strong>signOut</strong></a>(final BMXCallBack callBack)<br>退出登录</p>                                                                                                                                                       |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signout"><strong>signOut</strong></a>(final long userId, final BMXCallBack callBack)<br>退出登录</p>                                                                                                                                    |
| \[BMXConnectStatus] | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-connectstatus"><strong>connectStatus</strong></a>()<br>获取当前和服务器的连接状态</p>                                                                                                                                                            |
| \[BMXSignInStatus]  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signinstatus"><strong>signInStatus</strong></a>()<br>获取当前的登录状态</p>                                                                                                                                                                  |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-binddevice"><strong>bindDevice</strong></a>(final String token, final BMXCallBack callBack)<br>绑定设备推送token</p>                                                                                                                      |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-getdevicelist"><strong>getDeviceList</strong></a>(final BMXDataCallBack&#x3C; BMXDeviceList > callBack)<br>获取登录的设备列表</p>                                                                                                            |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-deletedevice"><strong>deleteDevice</strong></a>(final int device_sn, final BMXCallBack callBack)<br>删除设备</p>                                                                                                                        |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-getprofile"><strong>getProfile</strong></a>(final boolean forceRefresh, final BMXDataCallBack&#x3C; <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md">BMXUserProfile</a> > callBack)<br>获取用户详情</p>                     |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setnickname"><strong>setNickname</strong></a>(final String nickname, final BMXCallBack callBack)<br>设置昵称</p>                                                                                                                        |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-uploadavatar"><strong>uploadAvatar</strong></a>(final String avatarPath, final FileProgressListener listener, final BMXCallBack callBack)<br>上传头像</p>                                                                               |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-downloadavatar"><strong>downloadAvatar</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md">BMXUserProfile</a> profile, final FileProgressListener listener, final BMXCallBack callBack)<br>下载头像</p>   |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setpublicinfo"><strong>setPublicInfo</strong></a>(final String publicInfo, final BMXCallBack callBack)<br>设置公开扩展信息</p>                                                                                                              |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setprivateinfo"><strong>setPrivateInfo</strong></a>(final String privateInfo, final BMXCallBack callBack)<br>设置私有扩展信息</p>                                                                                                           |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setaddfriendauthmode"><strong>setAddFriendAuthMode</strong></a>(final BMXUserProfile.AddFriendAuthMode mode, final BMXCallBack callBack)<br>设置加好友验证方式</p>                                                                           |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setauthquestion"><strong>setAuthQuestion</strong></a>(final BMXUserProfile.AuthQuestion authQuestion, final BMXCallBack callBack)<br>设置加好友验证问题</p>                                                                                  |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setenablepush"><strong>setEnablePush</strong></a>(final boolean enable, final BMXCallBack callBack)<br>设置是否允许推送</p>                                                                                                                 |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setenablepushdetaile"><strong>setEnablePushDetaile</strong></a>(final boolean enable, final BMXCallBack callBack)<br>设置是否推送详情</p>                                                                                                   |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setpushnickname"><strong>setPushNickname</strong></a>(final String nickname, final BMXCallBack callBack)<br>设置推送昵称</p>                                                                                                              |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setpushalias"><strong>setPushAlias</strong></a>(final String alias, final String bmxPushToken, final BMXCallBack callBack)<br>设置推送别名</p>                                                                                            |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setnotificationsound"><strong>setNotificationSound</strong></a>(final boolean enable, final BMXCallBack callBack)<br>设置收到新消息是否声音提醒</p>                                                                                              |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setnotificationvibrate"><strong>setNotificationVibrate</strong></a>(final boolean enable, final BMXCallBack callBack)<br>设置收到新消息是否震动</p>                                                                                            |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setautodownloadattachment"><strong>setAutoDownloadAttachment</strong></a>(final boolean enable, final BMXCallBack callBack)<br>设置是否自动缩略图和语音附件</p>                                                                                   |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setautoacceptgroupinvite"><strong>setAutoAcceptGroupInvite</strong></a>(final boolean enable, final BMXCallBack callBack)<br>设置是否自动同意入群邀请</p>                                                                                       |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-adduserlistener"><strong>addUserListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md">BMXUserServiceListener</a> listener)<br>添加用户状态监听者</p>                                                 |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-removeuserlistener"><strong>removeUserListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md">BMXUserServiceListener</a> listener)<br>移除用户状态监听者</p>                                           |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-changeappid"><strong>changeAppId</strong></a>(final String appId, final BMXCallBack callBack)<br>切换appId</p>                                                                                                                        |

## Public Functions Documentation

### function BMXUserManager

```java
inline BMXUserManager(
    BMXUserService service,
    BMXClient bmxClient
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

### function signOut

```java
inline void signOut(
    final BMXCallBack callBack
)
```

退出登录

**Parameters**:

* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

### function signOut

```java
inline void signOut(
    final long userId,
    final BMXCallBack callBack
)
```

退出登录

**Parameters**:

* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

### function connectStatus

```java
inline BMXConnectStatus connectStatus()
```

获取当前和服务器的连接状态

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

### function signInStatus

```java
inline BMXSignInStatus signInStatus()
```

获取当前的登录状态

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

### function getDeviceList

```java
inline void getDeviceList(
    final BMXDataCallBack< BMXDeviceList > callBack
)
```

获取登录的设备列表

**Parameters**:

* **callBack** \[BMXErrorCode] 登录的设备列表

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

### function deleteDevice

```java
inline void deleteDevice(
    final int device_sn,
    final BMXCallBack callBack
)
```

删除设备

**Parameters**:

* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode],用户详情

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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
* **callBack** \[BMXErrorCode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>
```

***

Updated on 2022-01-26 at 17:18:31 +0800
