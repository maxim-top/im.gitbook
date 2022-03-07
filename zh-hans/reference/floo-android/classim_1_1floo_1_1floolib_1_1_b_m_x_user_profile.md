---
title: im::floo::floolib::BMXUserProfile
summary: 用户Profile 

---

# im::floo::floolib::BMXUserProfile



用户Profile 

Inherits from BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-bmxuserprofile)**() |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-delete)**() |
| long | **[userId](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-userid)**()<br>用户ID（唯一）  |
| BMXUserProfile.UserCategory | **[category](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-category)**()<br>用户策略  |
| String | **[username](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-username)**()<br>用户名（唯一）  |
| String | **[nickname](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-nickname)**()<br>用户昵称  |
| String | **[avatarRatelUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-avatarratelurl)**()<br>用户头像ratel服务器地址  |
| String | **[avatarUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-avatarurl)**()<br>用户头像  |
| String | **[avatarPath](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-avatarpath)**()<br>用户头像本地存储路径  |
| String | **[avatarThumbnailPath](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-avatarthumbnailpath)**()<br>用户头像缩略图本地存储路径  |
| String | **[mobilePhone](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-mobilephone)**()<br>用户手机  |
| String | **[email](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-email)**()<br>用户邮箱  |
| String | **[publicInfo](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-publicinfo)**()<br>用户公开扩展信息，好友可见  |
| String | **[privateInfo](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-privateinfo)**()<br>用户私有扩展信息，好友不可见  |
| BMXUserProfile.AddFriendAuthMode | **[addFriendAuthMode](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-addfriendauthmode)**()<br>加好友校验方式  |
| BMXUserProfile.AuthQuestion | **[authQuestion](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-authquestion)**()<br>添加好友时的验证问题  |
| BMXUserProfile.MessageSetting | **[messageSetting](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-messagesetting)**()<br>用户消息设定  |
| boolean | **[isAutoAcceptGroupInvite](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-isautoacceptgroupinvite)**()<br>收到群组邀请进群时是否自动同意进群  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-bmxuserprofile)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-getcptr)**([BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md) obj) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| transient long | **[swigCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#variable-swigcptr)**  |

## Public Functions Documentation

### function BMXUserProfile

```java
inline BMXUserProfile()
```


### function delete

```java
inline synchronized void delete()
```


### function userId

```java
inline long userId()
```

用户ID（唯一） 

**Return**: int64_t 

### function category

```java
inline BMXUserProfile.UserCategory category()
```

用户策略 

**Return**: [UserCategory]

### function username

```java
inline String username()
```

用户名（唯一） 

**Return**: std::string 

### function nickname

```java
inline String nickname()
```

用户昵称 

**Return**: std::string 

### function avatarRatelUrl

```java
inline String avatarRatelUrl()
```

用户头像ratel服务器地址 

**Return**: std::string 

### function avatarUrl

```java
inline String avatarUrl()
```

用户头像 

**Return**: std::string 

### function avatarPath

```java
inline String avatarPath()
```

用户头像本地存储路径 

**Return**: std::string 

### function avatarThumbnailPath

```java
inline String avatarThumbnailPath()
```

用户头像缩略图本地存储路径 

**Return**: std::string 

### function mobilePhone

```java
inline String mobilePhone()
```

用户手机 

**Return**: std::string 

### function email

```java
inline String email()
```

用户邮箱 

**Return**: std::string 

### function publicInfo

```java
inline String publicInfo()
```

用户公开扩展信息，好友可见 

**Return**: JSON(std::string) 

### function privateInfo

```java
inline String privateInfo()
```

用户私有扩展信息，好友不可见 

**Return**: JSON(std::string) 

### function addFriendAuthMode

```java
inline BMXUserProfile.AddFriendAuthMode addFriendAuthMode()
```

加好友校验方式 

**Return**: [AddFriendAuthMode]

### function authQuestion

```java
inline BMXUserProfile.AuthQuestion authQuestion()
```

添加好友时的验证问题 

**Return**: AuthQuestion 

### function messageSetting

```java
inline BMXUserProfile.MessageSetting messageSetting()
```

用户消息设定 

**Return**: MessageSetting 

### function isAutoAcceptGroupInvite

```java
inline boolean isAutoAcceptGroupInvite()
```

收到群组邀请进群时是否自动同意进群 

**Return**: bool 

## Protected Functions Documentation

### function BMXUserProfile

```java
inline BMXUserProfile(
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
    BMXUserProfile obj
)
```


## Public Attributes Documentation

### variable swigCPtr

```java
transient long swigCPtr;
```


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800