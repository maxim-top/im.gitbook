---
title: im::floo::floolib::BMXUserService
summary: User Service 

---

# im::floo::floolib::BMXUserService



User Service 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-delete)**() |
| [BMXErrorCode] | **[bindDevice](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-binddevice)**(String token)<br>Binding device push token  |
| [BMXErrorCode] | **[getDeviceList](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-getdevicelist)**(BMXDeviceList deviceList)<br>Get device list  |
| [BMXErrorCode] | **[getProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-getprofile)**([BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md) profile, boolean forceRefresh)<br>Get user details, force pull from server if forceRefresh == true  |
| [BMXErrorCode] | **[deleteDevice](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-deletedevice)**(int device_sn)<br>Delete device  |
| [BMXErrorCode] | **[setNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setnickname)**(String nickname)<br>Set nickname  |
| [BMXErrorCode] | **[uploadAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-uploadavatar)**(String avatarPath, FileProgressListener callback)<br>Upload avatar  |
| [BMXErrorCode] | **[downloadAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-downloadavatar)**([BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md) profile, boolean thumbnail, FileProgressListener callback)<br>Download avatar, default to download thumbnail  |
| [BMXErrorCode] | **[setPublicInfo](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setpublicinfo)**(String publicInfo)<br>Set public extension information  |
| [BMXErrorCode] | **[setPrivateInfo](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setprivateinfo)**(String privateInfo)<br>Set private extension information  |
| [BMXErrorCode] | **[setAddFriendAuthMode](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setaddfriendauthmode)**(BMXUserProfile.AddFriendAuthMode mode)<br>Set method to validate when adding friend  |
| [BMXErrorCode] | **[setAuthQuestion](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setauthquestion)**(BMXUserProfile.AuthQuestion authQuestion)<br>Set friend authentication questions  |
| [BMXErrorCode] | **[setEnablePush](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setenablepush)**(boolean enable)<br>Set whether push is allowed  |
| [BMXErrorCode] | **[setEnablePushDetaile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setenablepushdetaile)**(boolean enable)<br>Set whether to push details  |
| [BMXErrorCode] | **[setPushNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setpushnickname)**(String nickname)<br>Set push nickname  |
| [BMXErrorCode] | **[setPushAlias](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setpushalias)**(String alias, String bmxPushToken)<br>Set push alias  |
| [BMXErrorCode] | **[setNotificationSound](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setnotificationsound)**(boolean enable)<br>Set whether a new message is audibly alerted  |
| [BMXErrorCode] | **[setNotificationVibrate](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setnotificationvibrate)**(boolean enable)<br>Set whether a new message is alerted in vibration  |
| [BMXErrorCode] | **[setAutoDownloadAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setautodownloadattachment)**(boolean enable)<br>Set whether to automatically download thumbnail and voice attachment  |
| [BMXErrorCode] | **[setAutoAcceptGroupInvite](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-setautoacceptgroupinvite)**(boolean enable)<br>Set whether to automatically accept group invitations  |
| void | **[addUserListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-adduserlistener)**([BMXUserServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md) listener)<br>Add user state listener  |
| void | **[removeUserListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md#function-removeuserlistener)**([BMXUserServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md) listener)<br>Remove user state listener  |

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


### function bindDevice

```java
inline BMXErrorCode bindDevice(
    String token
)
```

Binding device push token 

**Parameters**: 

  * **token** Device token 


**Return**: [BMXErrorCode]

### function getDeviceList

```java
inline BMXErrorCode getDeviceList(
    BMXDeviceList deviceList
)
```

Get device list 

**Parameters**: 

  * **deviceList** Device list, pass in an empty list function and fetch the returned device list here 


**Return**: [BMXErrorCode]

### function getProfile

```java
inline BMXErrorCode getProfile(
    BMXUserProfile profile,
    boolean forceRefresh
)
```

Get user details, force pull from server if forceRefresh == true 

**Parameters**: 

  * **profile** User profile, initially passed in a pointing-to-empty shared_ptr object, and fetch user profile here after the function returned. 
  * **forceRefresh** Whether to force pull from server, automatically if local fetch failed 


**Return**: [BMXErrorCode]

### function deleteDevice

```java
inline BMXErrorCode deleteDevice(
    int device_sn
)
```

Delete device 

**Parameters**: 

  * **device_sn** Device serial number 


**Return**: [BMXErrorCode]

### function setNickname

```java
inline BMXErrorCode setNickname(
    String nickname
)
```

Set nickname 

**Parameters**: 

  * **nickname** User nickname 


**Return**: [BMXErrorCode]

### function uploadAvatar

```java
inline BMXErrorCode uploadAvatar(
    String avatarPath,
    FileProgressListener callback
)
```

Upload avatar 

**Parameters**: 

  * **avatarPath** Local address to upload avatar 
  * **callback** Upload callback function 


**Return**: [BMXErrorCode]

### function downloadAvatar

```java
inline BMXErrorCode downloadAvatar(
    BMXUserProfile profile,
    boolean thumbnail,
    FileProgressListener callback
)
```

Download avatar, default to download thumbnail 

**Parameters**: 

  * **profile** User profile 
  * **thumbnail** Whether to download thumbnail, true for thumbnail, false for original 
  * **callback** Download callback function 


**Return**: [BMXErrorCode]

### function setPublicInfo

```java
inline BMXErrorCode setPublicInfo(
    String publicInfo
)
```

Set public extension information 

**Parameters**: 

  * **publicInfo** Public extension information 


**Return**: [BMXErrorCode]

### function setPrivateInfo

```java
inline BMXErrorCode setPrivateInfo(
    String privateInfo
)
```

Set private extension information 

**Parameters**: 

  * **privateInfo** Private extension information 


**Return**: [BMXErrorCode]

### function setAddFriendAuthMode

```java
inline BMXErrorCode setAddFriendAuthMode(
    BMXUserProfile.AddFriendAuthMode mode
)
```

Set method to validate when adding friend 

**Parameters**: 

  * **mode** Add friend authentication 


**Return**: [BMXErrorCode]

### function setAuthQuestion

```java
inline BMXErrorCode setAuthQuestion(
    BMXUserProfile.AuthQuestion authQuestion
)
```

Set friend authentication questions 

**Parameters**: 

  * **authQuestion** Add friend authentication question 


**Return**: [BMXErrorCode]

### function setEnablePush

```java
inline BMXErrorCode setEnablePush(
    boolean enable
)
```

Set whether push is allowed 

**Parameters**: 

  * **enable** Whether to allow push, true to push, false not to 


**Return**: [BMXErrorCode]

### function setEnablePushDetaile

```java
inline BMXErrorCode setEnablePushDetaile(
    boolean enable
)
```

Set whether to push details 

**Parameters**: 

  * **enable** Whether to push details, true to push, false not to 


**Return**: [BMXErrorCode]

### function setPushNickname

```java
inline BMXErrorCode setPushNickname(
    String nickname
)
```

Set push nickname 

**Parameters**: 

  * **nickname** Push nickname 


**Return**: [BMXErrorCode]

### function setPushAlias

```java
inline BMXErrorCode setPushAlias(
    String alias,
    String bmxPushToken
)
```

Set push alias 

**Parameters**: 

  * **alias** Alias 
  * **bmxPushToken** Push token 


**Return**: [BMXErrorCode]

### function setNotificationSound

```java
inline BMXErrorCode setNotificationSound(
    boolean enable
)
```

Set whether a new message is audibly alerted 

**Parameters**: 

  * **enable** Whether to sound alert when new message received, true to alert, false not to 


**Return**: [BMXErrorCode]

### function setNotificationVibrate

```java
inline BMXErrorCode setNotificationVibrate(
    boolean enable
)
```

Set whether a new message is alerted in vibration 

**Parameters**: 

  * **enable** Whether to vibrate alert when new message received, true to alert, false not to 


**Return**: [BMXErrorCode]

### function setAutoDownloadAttachment

```java
inline BMXErrorCode setAutoDownloadAttachment(
    boolean enable
)
```

Set whether to automatically download thumbnail and voice attachment 

**Parameters**: 

  * **enable** Whether to automatically download thumbnail and voice attachment, true to download, false not to 


**Return**: [BMXErrorCode]

### function setAutoAcceptGroupInvite

```java
inline BMXErrorCode setAutoAcceptGroupInvite(
    boolean enable
)
```

Set whether to automatically accept group invitations 

**Parameters**: 

  * **enable** Whether to automatically agree to group invitation, true to agree, false not to 


**Return**: [BMXErrorCode]

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


## Protected Functions Documentation

### function BMXUserService

```java
inline BMXUserService(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
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


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800