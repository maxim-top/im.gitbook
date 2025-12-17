---
title: im::floo::floolib::BMXUserManager
summary: User manager
---

# im::floo::floolib::BMXUserManager

User manager

## Public Functions

|                     | Name                                                                                                                                                                                                                                                                                                                   |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                     | [**BMXUserManager**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-bmxusermanager)([BMXUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md) service, [BMXClient](classim_1_1floo_1_1floolib_1_1_b_m_x_client.md) bmxClient)                                                              |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signupnewuser"><strong>signUpNewUser</strong></a>(final String username, final String password, final BMXDataCallBack&#x3C; <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md">BMXUserProfile</a> > callBack)<br>Register</p>    |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signinbyname"><strong>signInByName</strong></a>(final String name, final String password, final BMXCallBack callBack)<br>Username login</p>                                                                                                  |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signinbyid"><strong>signInById</strong></a>(final long id, final String password, final BMXCallBack callBack)<br>id login</p>                                                                                                                |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-autosigninbyname"><strong>autoSignInByName</strong></a>(final String name, final String password, final BMXCallBack callBack)<br>Auto login, by username</p>                                                                                 |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-autosigninbyid"><strong>autoSignInById</strong></a>(final long uid, final String password, final BMXCallBack callBack)<br>Auto login, by id</p>                                                                                              |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signout"><strong>signOut</strong></a>(final BMXCallBack callBack)<br>Log out</p>                                                                                                                                                             |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signout"><strong>signOut</strong></a>(final long userId, final BMXCallBack callBack)<br>Log out</p>                                                                                                                                          |
| \[BMXConnectStatus] | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-connectstatus"><strong>connectStatus</strong></a>()<br>Get the current connection state with server</p>                                                                                                                                      |
| \[BMXSignInStatus]  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-signinstatus"><strong>signInStatus</strong></a>()<br>Get the current login state</p>                                                                                                                                                         |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-binddevice"><strong>bindDevice</strong></a>(final String token, final BMXCallBack callBack)<br>Binding device push token</p>                                                                                                                 |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-getdevicelist"><strong>getDeviceList</strong></a>(final BMXDataCallBack&#x3C; BMXDeviceList > callBack)<br>Get list of logged-in devices</p>                                                                                                 |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-deletedevice"><strong>deleteDevice</strong></a>(final int device_sn, final BMXCallBack callBack)<br>Delete device</p>                                                                                                                        |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-getprofile"><strong>getProfile</strong></a>(final boolean forceRefresh, final BMXDataCallBack&#x3C; <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md">BMXUserProfile</a> > callBack)<br>Get user details</p>                    |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setnickname"><strong>setNickname</strong></a>(final String nickname, final BMXCallBack callBack)<br>Set nickname</p>                                                                                                                         |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-uploadavatar"><strong>uploadAvatar</strong></a>(final String avatarPath, final FileProgressListener listener, final BMXCallBack callBack)<br>Upload avatar</p>                                                                               |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-downloadavatar"><strong>downloadAvatar</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md">BMXUserProfile</a> profile, final FileProgressListener listener, final BMXCallBack callBack)<br>Download avatar</p> |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setpublicinfo"><strong>setPublicInfo</strong></a>(final String publicInfo, final BMXCallBack callBack)<br>Set public extension information</p>                                                                                               |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setprivateinfo"><strong>setPrivateInfo</strong></a>(final String privateInfo, final BMXCallBack callBack)<br>Set private extension information</p>                                                                                           |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setaddfriendauthmode"><strong>setAddFriendAuthMode</strong></a>(final BMXUserProfile.AddFriendAuthMode mode, final BMXCallBack callBack)<br>Set method to validate when adding friend</p>                                                    |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setauthquestion"><strong>setAuthQuestion</strong></a>(final BMXUserProfile.AuthQuestion authQuestion, final BMXCallBack callBack)<br>Set friend authentication questions</p>                                                                 |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setenablepush"><strong>setEnablePush</strong></a>(final boolean enable, final BMXCallBack callBack)<br>Set whether push is allowed</p>                                                                                                       |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setenablepushdetaile"><strong>setEnablePushDetaile</strong></a>(final boolean enable, final BMXCallBack callBack)<br>Set whether to push details</p>                                                                                         |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setpushnickname"><strong>setPushNickname</strong></a>(final String nickname, final BMXCallBack callBack)<br>Set push nickname</p>                                                                                                            |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setpushalias"><strong>setPushAlias</strong></a>(final String alias, final String bmxPushToken, final BMXCallBack callBack)<br>Set push alias</p>                                                                                             |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setnotificationsound"><strong>setNotificationSound</strong></a>(final boolean enable, final BMXCallBack callBack)<br>Set whether a new message is audibly alerted</p>                                                                        |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setnotificationvibrate"><strong>setNotificationVibrate</strong></a>(final boolean enable, final BMXCallBack callBack)<br>Set whether a new message is alerted in vibration</p>                                                               |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setautodownloadattachment"><strong>setAutoDownloadAttachment</strong></a>(final boolean enable, final BMXCallBack callBack)<br>Set whether to automatically download thumbnail and voice attachment</p>                                      |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-setautoacceptgroupinvite"><strong>setAutoAcceptGroupInvite</strong></a>(final boolean enable, final BMXCallBack callBack)<br>Set whether to automatically accept group invitations</p>                                                       |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-adduserlistener"><strong>addUserListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md">BMXUserServiceListener</a> listener)<br>Add user state listener</p>                                            |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-removeuserlistener"><strong>removeUserListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md">BMXUserServiceListener</a> listener)<br>Remove user state listener</p>                                   |
| void                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_manager.md#function-changeappid"><strong>changeAppId</strong></a>(final String appId, final BMXCallBack callBack)<br>Switch appId</p>                                                                                                                            |

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

Register

**Parameters**:

* **password** Password
* **username** Username
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

Username login

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

id login

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

Auto login, by username

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

Auto login, by id

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

Log out

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

Log out

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

Get the current connection state with server

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>

```

### function signInStatus

```java
inline BMXSignInStatus signInStatus()
```

Get the current login state

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

Binding device push token

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

Get list of logged-in devices

**Parameters**:

* **callBack** \[BMXErrorCode] list of logged-in devices

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

Delete device

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

Get user details

**Parameters**:

* **forceRefresh** Force pull latest results from server
* **callBack** \[BMXErrorCode], user details

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

Set nickname

**Parameters**:

* **nickname** Nickname
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

Upload avatar

**Parameters**:

* **avatarPath** Local file path of avatar
* **listener** Uploading progress listener
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

Download avatar

**Parameters**:

* **profile** User details
* **listener** Downloading progress listener
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

Set public extension information

**Parameters**:

* **publicInfo** User public information
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

Set private extension information

**Parameters**:

* **privateInfo** User private information (self-visibe only)
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

Set method to validate when adding friend

**Parameters**:

* **mode** How to validate when adding friend
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

Set friend authentication questions

**Parameters**:

* **authQuestion** Verification question
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

Set whether push is allowed

**Parameters**:

* **enable** Whether to allow push, true to push, false not to
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

Set whether to push details

**Parameters**:

* **enable** Whether to push details, true to push, false not to
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

Set push nickname

**Parameters**:

* **nickname** Push nickname
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

Set push alias

**Parameters**:

* **alias** Alias
* **bmxPushToken** Push token
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

Set whether a new message is audibly alerted

**Parameters**:

* **enable** Whether to sound alert when new message received, true to alert, false not to
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

Set whether a new message is alerted in vibration

**Parameters**:

* **enable** Whether to vibrate alert when new message received, true to alert, false not to
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

Set whether to automatically download thumbnail and voice attachment

**Parameters**:

* **enable** Whether to automatically download thumbnail and voice attachment, true to download, false not to
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

Set whether to automatically accept group invitations

**Parameters**:

* **enable** Whether to automatically agree to group invitation, true to agree, false not to
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

Add user state listener

**Parameters**:

* **listener** User state listener

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

Remove user state listener

**Parameters**:

* **listener** User state listener

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

Switch appId

**Parameters**:

* **appId** appId

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserManager'></div>
```

***

Updated on 2022-01-26 at 17:18:31 +0800
