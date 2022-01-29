---
title: floo::BMXUserProfile
summary: 用户Profile 

---

# floo::BMXUserProfile



用户Profile 


`#include <bmx_user_profile.h>`

Inherits from BMXBaseObject

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[AddFriendAuthMode](classfloo_1_1_b_m_x_user_profile.md#enum-addfriendauthmode)** { Open, NeedApproval, AnswerQuestion, RejectAll}<br>对方申请加好友时的验证方式  |
| enum class| **[UserCategory](classfloo_1_1_b_m_x_user_profile.md#enum-usercategory)** { Normal, Advanced}<br>用户类型  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXUserProfile](classfloo_1_1_b_m_x_user_profile.md#function-~bmxuserprofile)**()<br>析构函数  |
| virtual int64_t | **[userId](classfloo_1_1_b_m_x_user_profile.md#function-userid)**() =0<br>用户ID（唯一）  |
| virtual [UserCategory](classfloo_1_1_b_m_x_user_profile.md#enum-usercategory) | **[category](classfloo_1_1_b_m_x_user_profile.md#function-category)**() =0<br>用户策略  |
| virtual const std::string & | **[username](classfloo_1_1_b_m_x_user_profile.md#function-username)**() =0<br>用户名（唯一）  |
| virtual const std::string & | **[nickname](classfloo_1_1_b_m_x_user_profile.md#function-nickname)**() =0<br>用户昵称  |
| virtual std::string | **[avatarRatelUrl](classfloo_1_1_b_m_x_user_profile.md#function-avatarratelurl)**() =0<br>用户ratel服务器头像url  |
| virtual std::string | **[avatarUrl](classfloo_1_1_b_m_x_user_profile.md#function-avatarurl)**() =0<br>用户头像url  |
| virtual std::string | **[avatarPath](classfloo_1_1_b_m_x_user_profile.md#function-avatarpath)**() =0<br>用户头像本地存储路径  |
| virtual std::string | **[avatarThumbnailPath](classfloo_1_1_b_m_x_user_profile.md#function-avatarthumbnailpath)**() =0<br>用户头像缩略图本地存储路径  |
| virtual const std::string & | **[mobilePhone](classfloo_1_1_b_m_x_user_profile.md#function-mobilephone)**() =0<br>用户手机  |
| virtual const std::string & | **[email](classfloo_1_1_b_m_x_user_profile.md#function-email)**() =0<br>用户邮箱  |
| virtual const JSON & | **[publicInfo](classfloo_1_1_b_m_x_user_profile.md#function-publicinfo)**() =0<br>用户公开扩展信息，好友可见  |
| virtual const JSON & | **[privateInfo](classfloo_1_1_b_m_x_user_profile.md#function-privateinfo)**() =0<br>用户私有扩展信息，好友不可见  |
| virtual [AddFriendAuthMode](classfloo_1_1_b_m_x_user_profile.md#enum-addfriendauthmode) | **[addFriendAuthMode](classfloo_1_1_b_m_x_user_profile.md#function-addfriendauthmode)**() =0<br>加好友校验方式  |
| virtual const [AuthQuestion] & | **[authQuestion](classfloo_1_1_b_m_x_user_profile.md#function-authquestion)**() =0<br>添加好友时的验证问题  |
| virtual const [MessageSetting] & | **[messageSetting](classfloo_1_1_b_m_x_user_profile.md#function-messagesetting)**() =0<br>用户消息设定  |
| virtual bool | **[isAutoAcceptGroupInvite](classfloo_1_1_b_m_x_user_profile.md#function-isautoacceptgroupinvite)**() =0<br>收到群组邀请进群时是否自动同意进群  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXUserProfile](classfloo_1_1_b_m_x_user_profile.md#function-bmxuserprofile)**() |

## Public Types Documentation

### enum AddFriendAuthMode

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Open | | 无需验证，任何人可以加为好友   |
| NeedApproval | | 需要同意方可加为好友   |
| AnswerQuestion | | 需要回答问题正确方可加为好友   |
| RejectAll | | 拒绝所有加好友申请   |



对方申请加好友时的验证方式 

### enum UserCategory

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Normal | | 普通用户   |
| Advanced | | 高级用户   |



用户类型 

## Public Functions Documentation

### function ~BMXUserProfile

```cpp
inline virtual ~BMXUserProfile()
```

析构函数 

### function userId

```cpp
virtual int64_t userId() =0
```

用户ID（唯一） 

**Return**: int64_t 

### function category

```cpp
virtual UserCategory category() =0
```

用户策略 

**Return**: UserCategory 

### function username

```cpp
virtual const std::string & username() =0
```

用户名（唯一） 

**Return**: std::string 

### function nickname

```cpp
virtual const std::string & nickname() =0
```

用户昵称 

**Return**: std::string 

### function avatarRatelUrl

```cpp
virtual std::string avatarRatelUrl() =0
```

用户ratel服务器头像url 

**Return**: std::string 

### function avatarUrl

```cpp
virtual std::string avatarUrl() =0
```

用户头像url 

**Return**: std::string 

### function avatarPath

```cpp
virtual std::string avatarPath() =0
```

用户头像本地存储路径 

**Return**: std::string 

### function avatarThumbnailPath

```cpp
virtual std::string avatarThumbnailPath() =0
```

用户头像缩略图本地存储路径 

**Return**: std::string 

### function mobilePhone

```cpp
virtual const std::string & mobilePhone() =0
```

用户手机 

**Return**: std::string 

### function email

```cpp
virtual const std::string & email() =0
```

用户邮箱 

**Return**: std::string 

### function publicInfo

```cpp
virtual const JSON & publicInfo() =0
```

用户公开扩展信息，好友可见 

**Return**: JSON(std::string) 

### function privateInfo

```cpp
virtual const JSON & privateInfo() =0
```

用户私有扩展信息，好友不可见 

**Return**: JSON(std::string) 

### function addFriendAuthMode

```cpp
virtual AddFriendAuthMode addFriendAuthMode() =0
```

加好友校验方式 

**Return**: AddFriendAuthMode 

### function authQuestion

```cpp
virtual const AuthQuestion & authQuestion() =0
```

添加好友时的验证问题 

**Return**: [AuthQuestion]

### function messageSetting

```cpp
virtual const MessageSetting & messageSetting() =0
```

用户消息设定 

**Return**: [MessageSetting]

### function isAutoAcceptGroupInvite

```cpp
virtual bool isAutoAcceptGroupInvite() =0
```

收到群组邀请进群时是否自动同意进群 

**Return**: bool 

## Protected Functions Documentation

### function BMXUserProfile

```cpp
inline BMXUserProfile()
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800