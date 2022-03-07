---
title: floo::BMXUserProfile
summary: User Profile 

---

# floo::BMXUserProfile



User Profile 


`#include <bmx_user_profile.h>`

Inherits from BMXBaseObject

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[AddFriendAuthMode](classfloo_1_1_b_m_x_user_profile.md#enum-addfriendauthmode)** { Open, NeedApproval, AnswerQuestion, RejectAll}<br>How to validate when adding friend  |
| enum class| **[UserCategory](classfloo_1_1_b_m_x_user_profile.md#enum-usercategory)** { Normal, Advanced}<br>User type  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXUserProfile](classfloo_1_1_b_m_x_user_profile.md#function-~bmxuserprofile)**()<br>Destructor  |
| virtual int64_t | **[userId](classfloo_1_1_b_m_x_user_profile.md#function-userid)**() =0<br>User ID (unique)  |
| virtual [UserCategory](classfloo_1_1_b_m_x_user_profile.md#enum-usercategory) | **[category](classfloo_1_1_b_m_x_user_profile.md#function-category)**() =0<br>User policy  |
| virtual const std::string & | **[username](classfloo_1_1_b_m_x_user_profile.md#function-username)**() =0<br>Username (unique)  |
| virtual const std::string & | **[nickname](classfloo_1_1_b_m_x_user_profile.md#function-nickname)**() =0<br>User nickname  |
| virtual std::string | **[avatarRatelUrl](classfloo_1_1_b_m_x_user_profile.md#function-avatarratelurl)**() =0<br>User ratel server avatar url  |
| virtual std::string | **[avatarUrl](classfloo_1_1_b_m_x_user_profile.md#function-avatarurl)**() =0<br>User avatar url  |
| virtual std::string | **[avatarPath](classfloo_1_1_b_m_x_user_profile.md#function-avatarpath)**() =0<br>Local storage path of user avatar  |
| virtual std::string | **[avatarThumbnailPath](classfloo_1_1_b_m_x_user_profile.md#function-avatarthumbnailpath)**() =0<br>Local storage path of user avatar thumbnail  |
| virtual const std::string & | **[mobilePhone](classfloo_1_1_b_m_x_user_profile.md#function-mobilephone)**() =0<br>User mobile phone  |
| virtual const std::string & | **[email](classfloo_1_1_b_m_x_user_profile.md#function-email)**() =0<br>User email  |
| virtual const JSON & | **[publicInfo](classfloo_1_1_b_m_x_user_profile.md#function-publicinfo)**() =0<br>User public extension information, visible to friends  |
| virtual const JSON & | **[privateInfo](classfloo_1_1_b_m_x_user_profile.md#function-privateinfo)**() =0<br>User private extension information, not visible to friends  |
| virtual [AddFriendAuthMode](classfloo_1_1_b_m_x_user_profile.md#enum-addfriendauthmode) | **[addFriendAuthMode](classfloo_1_1_b_m_x_user_profile.md#function-addfriendauthmode)**() =0<br>How to validate when adding friend  |
| virtual const [AuthQuestion] & | **[authQuestion](classfloo_1_1_b_m_x_user_profile.md#function-authquestion)**() =0<br>Authentication questions when adding friend  |
| virtual const [MessageSetting] & | **[messageSetting](classfloo_1_1_b_m_x_user_profile.md#function-messagesetting)**() =0<br>User message settings  |
| virtual bool | **[isAutoAcceptGroupInvite](classfloo_1_1_b_m_x_user_profile.md#function-isautoacceptgroupinvite)**() =0<br>Whether to automatically agree to join group when a group invitation is received  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXUserProfile](classfloo_1_1_b_m_x_user_profile.md#function-bmxuserprofile)**() |

## Public Types Documentation

### enum AddFriendAuthMode

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Open | | No authentication required, anyone can be added as a friend   |
| NeedApproval | | Consent is required to be added as a friend   |
| AnswerQuestion | | Need to answer authentication question correctly to be added as a friend   |
| RejectAll | | Reject all adding friend requests   |



How to validate when adding friend 

### enum UserCategory

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Normal | | Normal user   |
| Advanced | | Power user   |



User type 

## Public Functions Documentation

### function ~BMXUserProfile

```cpp
inline virtual ~BMXUserProfile()
```

Destructor 

### function userId

```cpp
virtual int64_t userId() =0
```

User ID (unique) 

**Return**: int64_t 

### function category

```cpp
virtual UserCategory category() =0
```

User policy 

**Return**: UserCategory 

### function username

```cpp
virtual const std::string & username() =0
```

Username (unique) 

**Return**: std::string 

### function nickname

```cpp
virtual const std::string & nickname() =0
```

User nickname 

**Return**: std::string 

### function avatarRatelUrl

```cpp
virtual std::string avatarRatelUrl() =0
```

User ratel server avatar url 

**Return**: std::string 

### function avatarUrl

```cpp
virtual std::string avatarUrl() =0
```

User avatar url 

**Return**: std::string 

### function avatarPath

```cpp
virtual std::string avatarPath() =0
```

Local storage path of user avatar 

**Return**: std::string 

### function avatarThumbnailPath

```cpp
virtual std::string avatarThumbnailPath() =0
```

Local storage path of user avatar thumbnail 

**Return**: std::string 

### function mobilePhone

```cpp
virtual const std::string & mobilePhone() =0
```

User mobile phone 

**Return**: std::string 

### function email

```cpp
virtual const std::string & email() =0
```

User email 

**Return**: std::string 

### function publicInfo

```cpp
virtual const JSON & publicInfo() =0
```

User public extension information, visible to friends 

**Return**: JSON(std::string) 

### function privateInfo

```cpp
virtual const JSON & privateInfo() =0
```

User private extension information, not visible to friends 

**Return**: JSON(std::string) 

### function addFriendAuthMode

```cpp
virtual AddFriendAuthMode addFriendAuthMode() =0
```

How to validate when adding friend 

**Return**: AddFriendAuthMode 

### function authQuestion

```cpp
virtual const AuthQuestion & authQuestion() =0
```

Authentication questions when adding friend 

**Return**: [AuthQuestion]

### function messageSetting

```cpp
virtual const MessageSetting & messageSetting() =0
```

User message settings 

**Return**: [MessageSetting]

### function isAutoAcceptGroupInvite

```cpp
virtual bool isAutoAcceptGroupInvite() =0
```

Whether to automatically agree to join group when a group invitation is received 

**Return**: bool 

## Protected Functions Documentation

### function BMXUserProfile

```cpp
inline BMXUserProfile()
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800