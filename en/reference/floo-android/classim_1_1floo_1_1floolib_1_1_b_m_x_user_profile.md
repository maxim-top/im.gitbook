---
title: im::floo::floolib::BMXUserProfile
summary: User Profile
---

# im::floo::floolib::BMXUserProfile

User Profile

Inherits from BMXBaseObject

## Public Functions

|                                  | Name                                                                                                                                                                                                                                      |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                  | [**BMXUserProfile**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-bmxuserprofile)()                                                                                                                                      |
| synchronized void                | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-delete)()                                                                                                                                                      |
| long                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-userid"><strong>userId</strong></a>()<br>User ID (unique)</p>                                                                                                   |
| BMXUserProfile.UserCategory      | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-category"><strong>category</strong></a>()<br>User policy</p>                                                                                                    |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-username"><strong>username</strong></a>()<br>Username (unique)</p>                                                                                              |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-nickname"><strong>nickname</strong></a>()<br>User nickname</p>                                                                                                  |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-avatarratelurl"><strong>avatarRatelUrl</strong></a>()<br>Ratel server address of user avatar</p>                                                                |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-avatarurl"><strong>avatarUrl</strong></a>()<br>User avatar</p>                                                                                                  |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-avatarpath"><strong>avatarPath</strong></a>()<br>Local storage path of user avatar</p>                                                                          |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-avatarthumbnailpath"><strong>avatarThumbnailPath</strong></a>()<br>Local storage path of user avatar thumbnail</p>                                              |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-mobilephone"><strong>mobilePhone</strong></a>()<br>User mobile phone</p>                                                                                        |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-email"><strong>email</strong></a>()<br>User email</p>                                                                                                           |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-publicinfo"><strong>publicInfo</strong></a>()<br>User public extension information, visible to friends</p>                                                      |
| String                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-privateinfo"><strong>privateInfo</strong></a>()<br>User private extension information, not visible to friends</p>                                               |
| BMXUserProfile.AddFriendAuthMode | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-addfriendauthmode"><strong>addFriendAuthMode</strong></a>()<br>How to validate when adding friend</p>                                                           |
| BMXUserProfile.AuthQuestion      | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-authquestion"><strong>authQuestion</strong></a>()<br>Authentication questions when adding friend</p>                                                            |
| BMXUserProfile.MessageSetting    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-messagesetting"><strong>messageSetting</strong></a>()<br>User message settings</p>                                                                              |
| boolean                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-isautoacceptgroupinvite"><strong>isAutoAcceptGroupInvite</strong></a>()<br>Whether to automatically agree to join group when a group invitation is received</p> |

## Protected Functions

|      | Name                                                                                                                                                             |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXUserProfile**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-bmxuserprofile)(long cPtr, boolean cMemoryOwn)                                |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-finalize)()                                                                         |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#function-getcptr)([BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md) obj) |

## Public Attributes

|                | Name                                                                                   |
| -------------- | -------------------------------------------------------------------------------------- |
| transient long | [**swigCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md#variable-swigcptr) |

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

User ID (unique)

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>

```

### function category

```java
inline BMXUserProfile.UserCategory category()
```

User policy

**Return**: \[UserCategory]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>

```

### function username

```java
inline String username()
```

Username (unique)

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>

```

### function nickname

```java
inline String nickname()
```

User nickname

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>

```

### function avatarRatelUrl

```java
inline String avatarRatelUrl()
```

Ratel server address of user avatar

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>

```

### function avatarUrl

```java
inline String avatarUrl()
```

User avatar

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>

```

### function avatarPath

```java
inline String avatarPath()
```

Local storage path of user avatar

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>

```

### function avatarThumbnailPath

```java
inline String avatarThumbnailPath()
```

Local storage path of user avatar thumbnail

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>

```

### function mobilePhone

```java
inline String mobilePhone()
```

User mobile phone

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>

```

### function email

```java
inline String email()
```

User email

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>

```

### function publicInfo

```java
inline String publicInfo()
```

User public extension information, visible to friends

**Return**: JSON(std::string)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>

```

### function privateInfo

```java
inline String privateInfo()
```

User private extension information, not visible to friends

**Return**: JSON(std::string)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>

```

### function addFriendAuthMode

```java
inline BMXUserProfile.AddFriendAuthMode addFriendAuthMode()
```

How to validate when adding friend

**Return**: \[AddFriendAuthMode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>

```

### function authQuestion

```java
inline BMXUserProfile.AuthQuestion authQuestion()
```

Authentication questions when adding friend

**Return**: AuthQuestion

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>

```

### function messageSetting

```java
inline BMXUserProfile.MessageSetting messageSetting()
```

User message settings

**Return**: MessageSetting

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserProfile'></div>

```

### function isAutoAcceptGroupInvite

```java
inline boolean isAutoAcceptGroupInvite()
```

Whether to automatically agree to join group when a group invitation is received

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

***

Updated on 2022-01-26 at 17:18:31 +0800
