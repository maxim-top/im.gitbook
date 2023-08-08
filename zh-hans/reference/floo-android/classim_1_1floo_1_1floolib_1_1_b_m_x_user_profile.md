---
title: im::floo::floolib::BMXUserProfile
summary: 用户Profile
---

# im::floo::floolib::BMXUserProfile

用户Profile

Inherits from BMXBaseObject

## Public Functions

|                                  | Name                                                                                                                                                                       |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                  | [**BMXUserProfile**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_user\_profile.md#function-bmxuserprofile)()                                                            |
| synchronized void                | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_user\_profile.md#function-delete)()                                                                            |
| long                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-userid"><strong>userId</strong></a>()<br>用户ID（唯一）</p>                                            |
| BMXUserProfile.UserCategory      | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-category"><strong>category</strong></a>()<br>用户策略</p>                                            |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-username"><strong>username</strong></a>()<br>用户名（唯一）</p>                                         |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-nickname"><strong>nickname</strong></a>()<br>用户昵称</p>                                            |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-avatarratelurl"><strong>avatarRatelUrl</strong></a>()<br>用户头像ratel服务器地址</p>                      |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-avatarurl"><strong>avatarUrl</strong></a>()<br>用户头像</p>                                          |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-avatarpath"><strong>avatarPath</strong></a>()<br>用户头像本地存储路径</p>                                  |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-avatarthumbnailpath"><strong>avatarThumbnailPath</strong></a>()<br>用户头像缩略图本地存储路径</p>             |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-mobilephone"><strong>mobilePhone</strong></a>()<br>用户手机</p>                                      |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-email"><strong>email</strong></a>()<br>用户邮箱</p>                                                  |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-publicinfo"><strong>publicInfo</strong></a>()<br>用户公开扩展信息，好友可见</p>                               |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-privateinfo"><strong>privateInfo</strong></a>()<br>用户私有扩展信息，好友不可见</p>                            |
| BMXUserProfile.AddFriendAuthMode | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-addfriendauthmode"><strong>addFriendAuthMode</strong></a>()<br>加好友校验方式</p>                       |
| BMXUserProfile.AuthQuestion      | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-authquestion"><strong>authQuestion</strong></a>()<br>添加好友时的验证问题</p>                              |
| BMXUserProfile.MessageSetting    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-messagesetting"><strong>messageSetting</strong></a>()<br>用户消息设定</p>                              |
| boolean                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-isautoacceptgroupinvite"><strong>isAutoAcceptGroupInvite</strong></a>()<br>收到群组邀请进群时是否自动同意进群</p> |

## Protected Functions

|      | Name                                                                                                                                                                                   |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXUserProfile**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_user\_profile.md#function-bmxuserprofile)(long cPtr, boolean cMemoryOwn)                                           |
| void | [**finalize**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_user\_profile.md#function-finalize)()                                                                                    |
| long | [**getCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_user\_profile.md#function-getcptr)([BMXUserProfile](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_user\_profile.md) obj) |

## Public Attributes

|                | Name                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------- |
| transient long | [**swigCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_user\_profile.md#variable-swigcptr) |

## Public Functions Documentation

### function BMXUserProfile

```java
inline BMXUserProfile()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function delete

```java
inline synchronized void delete()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function userId

```java
inline long userId()
```

用户ID（唯一）

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function category

```java
inline BMXUserProfile.UserCategory category()
```

用户策略

**Return**: \[UserCategory]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function username

```java
inline String username()
```

用户名（唯一）

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function nickname

```java
inline String nickname()
```

用户昵称

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function avatarRatelUrl

```java
inline String avatarRatelUrl()
```

用户头像ratel服务器地址

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function avatarUrl

```java
inline String avatarUrl()
```

用户头像

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function avatarPath

```java
inline String avatarPath()
```

用户头像本地存储路径

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function avatarThumbnailPath

```java
inline String avatarThumbnailPath()
```

用户头像缩略图本地存储路径

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function mobilePhone

```java
inline String mobilePhone()
```

用户手机

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function email

```java
inline String email()
```

用户邮箱

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function publicInfo

```java
inline String publicInfo()
```

用户公开扩展信息，好友可见

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function privateInfo

```java
inline String privateInfo()
```

用户私有扩展信息，好友不可见

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function addFriendAuthMode

```java
inline BMXUserProfile.AddFriendAuthMode addFriendAuthMode()
```

加好友校验方式

**Return**: \[AddFriendAuthMode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function authQuestion

```java
inline BMXUserProfile.AuthQuestion authQuestion()
```

添加好友时的验证问题

**Return**: AuthQuestion

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function messageSetting

```java
inline BMXUserProfile.MessageSetting messageSetting()
```

用户消息设定

**Return**: MessageSetting

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function isAutoAcceptGroupInvite

```java
inline boolean isAutoAcceptGroupInvite()
```

收到群组邀请进群时是否自动同意进群

**Return**: bool

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function BMXUserProfile

```java
inline BMXUserProfile(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```

### function finalize

```java
inline void finalize()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>
```



Updated on 2022-01-26 at 17:18:31 +0800
