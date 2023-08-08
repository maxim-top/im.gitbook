---
title: floo::BMXUserProfile
summary: User Profile
---

# floo::BMXUserProfile

User Profile

`#include <bmx_user_profile.h>`

Inherits from BMXBaseObject

## Public Types

|            | Name                                                                                                                                                                                                      |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class | <p><a href="classfloo_1_1_b_m_x_user_profile.md#enum-addfriendauthmode"><strong>AddFriendAuthMode</strong></a> { Open, NeedApproval, AnswerQuestion, RejectAll}<br>How to validate when adding friend</p> |
| enum class | <p><a href="classfloo_1_1_b_m_x_user_profile.md#enum-usercategory"><strong>UserCategory</strong></a> { Normal, Advanced}<br>User type</p>                                                                 |

## Public Functions

|                                                                                                | Name                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual                                                                                        | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-~bmxuserprofile"><strong>~BMXUserProfile</strong></a>()<br>Destructor</p>                                                                                          |
| virtual int64\_t                                                                               | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-userid"><strong>userId</strong></a>() =0<br>User ID (unique)</p>                                                                                                   |
| virtual [UserCategory](classfloo\_1\_1\_b\_m\_x\_user\_profile.md#enum-usercategory)           | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-category"><strong>category</strong></a>() =0<br>User policy</p>                                                                                                    |
| virtual const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-username"><strong>username</strong></a>() =0<br>Username (unique)</p>                                                                                              |
| virtual const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-nickname"><strong>nickname</strong></a>() =0<br>User nickname</p>                                                                                                  |
| virtual std::string                                                                            | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-avatarratelurl"><strong>avatarRatelUrl</strong></a>() =0<br>User ratel server avatar url</p>                                                                       |
| virtual std::string                                                                            | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-avatarurl"><strong>avatarUrl</strong></a>() =0<br>User avatar url</p>                                                                                              |
| virtual std::string                                                                            | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-avatarpath"><strong>avatarPath</strong></a>() =0<br>Local storage path of user avatar</p>                                                                          |
| virtual std::string                                                                            | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-avatarthumbnailpath"><strong>avatarThumbnailPath</strong></a>() =0<br>Local storage path of user avatar thumbnail</p>                                              |
| virtual const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-mobilephone"><strong>mobilePhone</strong></a>() =0<br>User mobile phone</p>                                                                                        |
| virtual const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-email"><strong>email</strong></a>() =0<br>User email</p>                                                                                                           |
| virtual const JSON &                                                                           | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-publicinfo"><strong>publicInfo</strong></a>() =0<br>User public extension information, visible to friends</p>                                                      |
| virtual const JSON &                                                                           | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-privateinfo"><strong>privateInfo</strong></a>() =0<br>User private extension information, not visible to friends</p>                                               |
| virtual [AddFriendAuthMode](classfloo\_1\_1\_b\_m\_x\_user\_profile.md#enum-addfriendauthmode) | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-addfriendauthmode"><strong>addFriendAuthMode</strong></a>() =0<br>How to validate when adding friend</p>                                                           |
| virtual const \[AuthQuestion] &                                                                | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-authquestion"><strong>authQuestion</strong></a>() =0<br>Authentication questions when adding friend</p>                                                            |
| virtual const \[MessageSetting] &                                                              | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-messagesetting"><strong>messageSetting</strong></a>() =0<br>User message settings</p>                                                                              |
| virtual bool                                                                                   | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-isautoacceptgroupinvite"><strong>isAutoAcceptGroupInvite</strong></a>() =0<br>Whether to automatically agree to join group when a group invitation is received</p> |

## Protected Functions

|   | Name                                                                                       |
| - | ------------------------------------------------------------------------------------------ |
|   | [**BMXUserProfile**](classfloo\_1\_1\_b\_m\_x\_user\_profile.md#function-bmxuserprofile)() |

## Public Types Documentation

### enum AddFriendAuthMode

| Enumerator     | Value | Description                                                              |
| -------------- | ----- | ------------------------------------------------------------------------ |
| Open           |       | No authentication required, anyone can be added as a friend              |
| NeedApproval   |       | Consent is required to be added as a friend                              |
| AnswerQuestion |       | Need to answer authentication question correctly to be added as a friend |
| RejectAll      |       | Reject all adding friend requests                                        |

How to validate when adding friend

### enum UserCategory

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Normal     |       | Normal user |
| Advanced   |       | Power user  |

User type

## Public Functions Documentation

### function \~BMXUserProfile

```cpp
inline virtual ~BMXUserProfile()
```

Destructor

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function userId

```cpp
virtual int64_t userId() =0
```

User ID (unique)

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function category

```cpp
virtual UserCategory category() =0
```

User policy

**Return**: UserCategory

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function username

```cpp
virtual const std::string & username() =0
```

Username (unique)

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function nickname

```cpp
virtual const std::string & nickname() =0
```

User nickname

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function avatarRatelUrl

```cpp
virtual std::string avatarRatelUrl() =0
```

User ratel server avatar url

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function avatarUrl

```cpp
virtual std::string avatarUrl() =0
```

User avatar url

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function avatarPath

```cpp
virtual std::string avatarPath() =0
```

Local storage path of user avatar

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function avatarThumbnailPath

```cpp
virtual std::string avatarThumbnailPath() =0
```

Local storage path of user avatar thumbnail

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function mobilePhone

```cpp
virtual const std::string & mobilePhone() =0
```

User mobile phone

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function email

```cpp
virtual const std::string & email() =0
```

User email

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function publicInfo

```cpp
virtual const JSON & publicInfo() =0
```

User public extension information, visible to friends

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function privateInfo

```cpp
virtual const JSON & privateInfo() =0
```

User private extension information, not visible to friends

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function addFriendAuthMode

```cpp
virtual AddFriendAuthMode addFriendAuthMode() =0
```

How to validate when adding friend

**Return**: AddFriendAuthMode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function authQuestion

```cpp
virtual const AuthQuestion & authQuestion() =0
```

Authentication questions when adding friend

**Return**: \[AuthQuestion]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function messageSetting

```cpp
virtual const MessageSetting & messageSetting() =0
```

User message settings

**Return**: \[MessageSetting]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function isAutoAcceptGroupInvite

```cpp
virtual bool isAutoAcceptGroupInvite() =0
```

Whether to automatically agree to join group when a group invitation is received

**Return**: bool

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function BMXUserProfile

```cpp
inline BMXUserProfile()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
