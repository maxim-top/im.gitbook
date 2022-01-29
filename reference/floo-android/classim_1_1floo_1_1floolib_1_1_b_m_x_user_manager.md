---
title: im::floo::floolib::BMXUserManager
summary: User manager 

---

# im::floo::floolib::BMXUserManager



User manager 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXUserManager](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-bmxusermanager)**([BMXUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md) service, [BMXClient](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md) bmxClient) |
| void | **[signUpNewUser](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signupnewuser)**(final String username, final String password, final BMXDataCallBack< [BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md) > callBack)<br>Register  |
| void | **[signInByName](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signinbyname)**(final String name, final String password, final BMXCallBack callBack)<br>Username login  |
| void | **[signInById](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signinbyid)**(final long id, final String password, final BMXCallBack callBack)<br>id login  |
| void | **[autoSignInByName](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-autosigninbyname)**(final String name, final String password, final BMXCallBack callBack)<br>Auto login, by username  |
| void | **[autoSignInById](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-autosigninbyid)**(final long uid, final String password, final BMXCallBack callBack)<br>Auto login, by id  |
| void | **[signOut](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signout)**(final BMXCallBack callBack)<br>Log out  |
| void | **[signOut](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signout)**(final long userId, final BMXCallBack callBack)<br>Log out  |
| [BMXConnectStatus] | **[connectStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-connectstatus)**()<br>Get the current connection state with server  |
| [BMXSignInStatus] | **[signInStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signinstatus)**()<br>Get the current login state  |
| void | **[bindDevice](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-binddevice)**(final String token, final BMXCallBack callBack)<br>Binding device push token  |
| void | **[getDeviceList](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-getdevicelist)**(final BMXDataCallBack< BMXDeviceList > callBack)<br>Get list of logged-in devices  |
| void | **[deleteDevice](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-deletedevice)**(final int device_sn, final BMXCallBack callBack)<br>Delete device  |
| void | **[getProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-getprofile)**(final boolean forceRefresh, final BMXDataCallBack< [BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md) > callBack)<br>Get user details  |
| void | **[setNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setnickname)**(final String nickname, final BMXCallBack callBack)<br>Set nickname  |
| void | **[uploadAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-uploadavatar)**(final String avatarPath, final FileProgressListener listener, final BMXCallBack callBack)<br>Upload avatar  |
| void | **[downloadAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-downloadavatar)**(final [BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md) profile, final FileProgressListener listener, final BMXCallBack callBack)<br>Download avatar  |
| void | **[setPublicInfo](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setpublicinfo)**(final String publicInfo, final BMXCallBack callBack)<br>Set public extension information  |
| void | **[setPrivateInfo](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setprivateinfo)**(final String privateInfo, final BMXCallBack callBack)<br>Set private extension information  |
| void | **[setAddFriendAuthMode](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setaddfriendauthmode)**(final BMXUserProfile.AddFriendAuthMode mode, final BMXCallBack callBack)<br>Set how to validate when adding friend  |
| void | **[setAuthQuestion](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setauthquestion)**(final BMXUserProfile.AuthQuestion authQuestion, final BMXCallBack callBack)<br>Set friend authentication questions  |
| void | **[setEnablePush](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setenablepush)**(final boolean enable, final BMXCallBack callBack)<br>Set whether push is allowed  |
| void | **[setEnablePushDetaile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setenablepushdetaile)**(final boolean enable, final BMXCallBack callBack)<br>Set whether to push details  |
| void | **[setPushNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setpushnickname)**(final String nickname, final BMXCallBack callBack)<br>Set push nickname  |
| void | **[setPushAlias](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setpushalias)**(final String alias, final String bmxPushToken, final BMXCallBack callBack)<br>Set push alias  |
| void | **[setNotificationSound](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setnotificationsound)**(final boolean enable, final BMXCallBack callBack)<br>Set whether a new message is audibly alerted  |
| void | **[setNotificationVibrate](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setnotificationvibrate)**(final boolean enable, final BMXCallBack callBack)<br>Set whether a new message is alerted in vibration  |
| void | **[setAutoDownloadAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setautodownloadattachment)**(final boolean enable, final BMXCallBack callBack)<br>Set whether to automatically download thumbnail and voice attachment  |
| void | **[setAutoAcceptGroupInvite](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setautoacceptgroupinvite)**(final boolean enable, final BMXCallBack callBack)<br>Set whether to automatically accept group invitations  |
| void | **[addUserListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-adduserlistener)**([BMXUserServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md) listener)<br>Add user state listener  |
| void | **[removeUserListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-removeuserlistener)**([BMXUserServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md) listener)<br>Remove user state listener  |
| void | **[changeAppId](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-changeappid)**(final String appId, final BMXCallBack callBack)<br>Switch appId  |

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

Register 

**Parameters**: 

  * **password** Password 
  * **username** Username 
  * **callBack** [BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md)


### function signInByName

```java
inline void signInByName(
    final String name,
    final String password,
    final BMXCallBack callBack
)
```

Username login 

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

id login 

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

Auto login, by username 

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

Auto login, by id 

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

Log out 

**Parameters**: 

  * **callBack** [BMXErrorCode]


### function signOut

```java
inline void signOut(
    final long userId,
    final BMXCallBack callBack
)
```

Log out 

**Parameters**: 

  * **callBack** [BMXErrorCode]


### function connectStatus

```java
inline BMXConnectStatus connectStatus()
```

Get the current connection state with server 

### function signInStatus

```java
inline BMXSignInStatus signInStatus()
```

Get the current login state 

### function bindDevice

```java
inline void bindDevice(
    final String token,
    final BMXCallBack callBack
)
```

Binding device push token 

**Parameters**: 

  * **token** device token 
  * **callBack** [BMXErrorCode]


### function getDeviceList

```java
inline void getDeviceList(
    final BMXDataCallBack< BMXDeviceList > callBack
)
```

Get list of logged-in devices 

**Parameters**: 

  * **callBack** [BMXErrorCode] list of logged-in devices 


### function deleteDevice

```java
inline void deleteDevice(
    final int device_sn,
    final BMXCallBack callBack
)
```

Delete device 

**Parameters**: 

  * **callBack** [BMXErrorCode]


### function getProfile

```java
inline void getProfile(
    final boolean forceRefresh,
    final BMXDataCallBack< BMXUserProfile > callBack
)
```

Get user details 

**Parameters**: 

  * **forceRefresh** Force pull latest results from server 
  * **callBack** [BMXErrorCode], user details 


### function setNickname

```java
inline void setNickname(
    final String nickname,
    final BMXCallBack callBack
)
```

Set nickname 

**Parameters**: 

  * **nickname** Nickname 
  * **callBack** [BMXErrorCode]


### function uploadAvatar

```java
inline void uploadAvatar(
    final String avatarPath,
    final FileProgressListener listener,
    final BMXCallBack callBack
)
```

Upload avatar 

**Parameters**: 

  * **avatarPath** Local file path of avatar 
  * **listener** Uploading progress listener 
  * **callBack** [BMXErrorCode]


### function downloadAvatar

```java
inline void downloadAvatar(
    final BMXUserProfile profile,
    final FileProgressListener listener,
    final BMXCallBack callBack
)
```

Download avatar 

**Parameters**: 

  * **profile** User details 
  * **listener** Downloading progress listener 
  * **callBack** [BMXErrorCode]


### function setPublicInfo

```java
inline void setPublicInfo(
    final String publicInfo,
    final BMXCallBack callBack
)
```

Set public extension information 

**Parameters**: 

  * **publicInfo** User public information 
  * **callBack** [BMXErrorCode]


### function setPrivateInfo

```java
inline void setPrivateInfo(
    final String privateInfo,
    final BMXCallBack callBack
)
```

Set private extension information 

**Parameters**: 

  * **privateInfo** User private information (self-visibe only) 
  * **callBack** [BMXErrorCode]


### function setAddFriendAuthMode

```java
inline void setAddFriendAuthMode(
    final BMXUserProfile.AddFriendAuthMode mode,
    final BMXCallBack callBack
)
```

Set how to validate when adding friend 

**Parameters**: 

  * **mode** How to validate when adding friend 
  * **callBack** [BMXErrorCode]


### function setAuthQuestion

```java
inline void setAuthQuestion(
    final BMXUserProfile.AuthQuestion authQuestion,
    final BMXCallBack callBack
)
```

Set friend authentication questions 

**Parameters**: 

  * **authQuestion** Verification question 
  * **callBack** [BMXErrorCode]


### function setEnablePush

```java
inline void setEnablePush(
    final boolean enable,
    final BMXCallBack callBack
)
```

Set whether push is allowed 

**Parameters**: 

  * **enable** Whether to allow push, true to push, false not to 
  * **callBack** [BMXErrorCode]


### function setEnablePushDetaile

```java
inline void setEnablePushDetaile(
    final boolean enable,
    final BMXCallBack callBack
)
```

Set whether to push details 

**Parameters**: 

  * **enable** Whether to push details, true to push, false not to 
  * **callBack** [BMXErrorCode]


### function setPushNickname

```java
inline void setPushNickname(
    final String nickname,
    final BMXCallBack callBack
)
```

Set push nickname 

**Parameters**: 

  * **nickname** Push nickname 
  * **callBack** [BMXErrorCode]


### function setPushAlias

```java
inline void setPushAlias(
    final String alias,
    final String bmxPushToken,
    final BMXCallBack callBack
)
```

Set push alias 

**Parameters**: 

  * **alias** Alias 
  * **bmxPushToken** Push token 
  * **callBack** [BMXErrorCode]


### function setNotificationSound

```java
inline void setNotificationSound(
    final boolean enable,
    final BMXCallBack callBack
)
```

Set whether a new message is audibly alerted 

**Parameters**: 

  * **enable** Whether to sound alert when new message received, true to alert, false not to 
  * **callBack** [BMXErrorCode]


### function setNotificationVibrate

```java
inline void setNotificationVibrate(
    final boolean enable,
    final BMXCallBack callBack
)
```

Set whether a new message is alerted in vibration 

**Parameters**: 

  * **enable** Whether to vibrate alert when new message received, true to alert, false not to 
  * **callBack** [BMXErrorCode]


### function setAutoDownloadAttachment

```java
inline void setAutoDownloadAttachment(
    final boolean enable,
    final BMXCallBack callBack
)
```

Set whether to automatically download thumbnail and voice attachment 

**Parameters**: 

  * **enable** Whether to automatically download thumbnail and voice attachment, true to download, false not to 
  * **callBack** [BMXErrorCode]


### function setAutoAcceptGroupInvite

```java
inline void setAutoAcceptGroupInvite(
    final boolean enable,
    final BMXCallBack callBack
)
```

Set whether to automatically accept group invitations 

**Parameters**: 

  * **enable** Whether to automatically agree to group invitation, true to agree, false not to 
  * **callBack** [BMXErrorCode]


### function addUserListener

```java
inline void addUserListener(
    BMXUserServiceListener listener
)
```

Add user state listener 

**Parameters**: 

  * **listener** User state listener 


### function removeUserListener

```java
inline void removeUserListener(
    BMXUserServiceListener listener
)
```

Remove user state listener 

**Parameters**: 

  * **listener** User state listener 


### function changeAppId

```java
inline void changeAppId(
    final String appId,
    final BMXCallBack callBack
)
```

Switch appId 

**Parameters**: 

  * **appId** appId 


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800