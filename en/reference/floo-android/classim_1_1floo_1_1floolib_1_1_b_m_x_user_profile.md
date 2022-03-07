---
title: im::floo::floolib::BMXUserProfile
summary: User Profile 

---

# im::floo::floolib::BMXUserProfile



User Profile 

Inherits from BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-bmxuserprofile)**() |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-delete)**() |
| long | **[userId](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-userid)**()<br>User ID (unique)  |
| BMXUserProfile.UserCategory | **[category](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-category)**()<br>User policy  |
| String | **[username](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-username)**()<br>Username (unique)  |
| String | **[nickname](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-nickname)**()<br>User nickname  |
| String | **[avatarRatelUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-avatarratelurl)**()<br>Ratel server address of user avatar  |
| String | **[avatarUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-avatarurl)**()<br>User avatar  |
| String | **[avatarPath](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-avatarpath)**()<br>Local storage path of user avatar  |
| String | **[avatarThumbnailPath](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-avatarthumbnailpath)**()<br>Local storage path of user avatar thumbnail  |
| String | **[mobilePhone](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-mobilephone)**()<br>User mobile phone  |
| String | **[email](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-email)**()<br>User email  |
| String | **[publicInfo](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-publicinfo)**()<br>User public extension information, visible to friends  |
| String | **[privateInfo](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-privateinfo)**()<br>User private extension information, not visible to friends  |
| BMXUserProfile.AddFriendAuthMode | **[addFriendAuthMode](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-addfriendauthmode)**()<br>How to validate when adding friend  |
| BMXUserProfile.AuthQuestion | **[authQuestion](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-authquestion)**()<br>Authentication questions when adding friend  |
| BMXUserProfile.MessageSetting | **[messageSetting](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-messagesetting)**()<br>User message settings  |
| boolean | **[isAutoAcceptGroupInvite](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-isautoacceptgroupinvite)**()<br>Whether to automatically agree to join group when a group invitation is received  |

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

User ID (unique) 

**Return**: int64_t 

### function category

```java
inline BMXUserProfile.UserCategory category()
```

User policy 

**Return**: [UserCategory]

### function username

```java
inline String username()
```

Username (unique) 

**Return**: std::string 

### function nickname

```java
inline String nickname()
```

User nickname 

**Return**: std::string 

### function avatarRatelUrl

```java
inline String avatarRatelUrl()
```

Ratel server address of user avatar 

**Return**: std::string 

### function avatarUrl

```java
inline String avatarUrl()
```

User avatar 

**Return**: std::string 

### function avatarPath

```java
inline String avatarPath()
```

Local storage path of user avatar 

**Return**: std::string 

### function avatarThumbnailPath

```java
inline String avatarThumbnailPath()
```

Local storage path of user avatar thumbnail 

**Return**: std::string 

### function mobilePhone

```java
inline String mobilePhone()
```

User mobile phone 

**Return**: std::string 

### function email

```java
inline String email()
```

User email 

**Return**: std::string 

### function publicInfo

```java
inline String publicInfo()
```

User public extension information, visible to friends 

**Return**: JSON(std::string) 

### function privateInfo

```java
inline String privateInfo()
```

User private extension information, not visible to friends 

**Return**: JSON(std::string) 

### function addFriendAuthMode

```java
inline BMXUserProfile.AddFriendAuthMode addFriendAuthMode()
```

How to validate when adding friend 

**Return**: [AddFriendAuthMode]

### function authQuestion

```java
inline BMXUserProfile.AuthQuestion authQuestion()
```

Authentication questions when adding friend 

**Return**: AuthQuestion 

### function messageSetting

```java
inline BMXUserProfile.MessageSetting messageSetting()
```

User message settings 

**Return**: MessageSetting 

### function isAutoAcceptGroupInvite

```java
inline boolean isAutoAcceptGroupInvite()
```

Whether to automatically agree to join group when a group invitation is received 

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