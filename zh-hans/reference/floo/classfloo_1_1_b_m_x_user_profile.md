---
title: floo::BMXUserProfile
summary: 用户Profile
---

# floo::BMXUserProfile

用户Profile

`#include <bmx_user_profile.h>`

Inherits from BMXBaseObject

## Public Types

|            | Name                                                                                                                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| enum class | <p><a href="classfloo_1_1_b_m_x_user_profile.md#enum-addfriendauthmode"><strong>AddFriendAuthMode</strong></a> { Open, NeedApproval, AnswerQuestion, RejectAll}<br>对方申请加好友时的验证方式</p> |
| enum class | <p><a href="classfloo_1_1_b_m_x_user_profile.md#enum-usercategory"><strong>UserCategory</strong></a> { Normal, Advanced}<br>用户类型</p>                                                 |

## Public Functions

|                                                                                                | Name                                                                                                                                                         |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| virtual                                                                                        | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-~bmxuserprofile"><strong>~BMXUserProfile</strong></a>()<br>析构函数</p>                                 |
| virtual int64\_t                                                                               | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-userid"><strong>userId</strong></a>() =0<br>用户ID（唯一）</p>                                            |
| virtual [UserCategory](classfloo\_1\_1\_b\_m\_x\_user\_profile.md#enum-usercategory)           | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-category"><strong>category</strong></a>() =0<br>用户策略</p>                                            |
| virtual const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-username"><strong>username</strong></a>() =0<br>用户名（唯一）</p>                                         |
| virtual const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-nickname"><strong>nickname</strong></a>() =0<br>用户昵称</p>                                            |
| virtual std::string                                                                            | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-avatarratelurl"><strong>avatarRatelUrl</strong></a>() =0<br>用户ratel服务器头像url</p>                     |
| virtual std::string                                                                            | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-avatarurl"><strong>avatarUrl</strong></a>() =0<br>用户头像url</p>                                       |
| virtual std::string                                                                            | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-avatarpath"><strong>avatarPath</strong></a>() =0<br>用户头像本地存储路径</p>                                  |
| virtual std::string                                                                            | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-avatarthumbnailpath"><strong>avatarThumbnailPath</strong></a>() =0<br>用户头像缩略图本地存储路径</p>             |
| virtual const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-mobilephone"><strong>mobilePhone</strong></a>() =0<br>用户手机</p>                                      |
| virtual const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-email"><strong>email</strong></a>() =0<br>用户邮箱</p>                                                  |
| virtual const JSON &                                                                           | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-publicinfo"><strong>publicInfo</strong></a>() =0<br>用户公开扩展信息，好友可见</p>                               |
| virtual const JSON &                                                                           | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-privateinfo"><strong>privateInfo</strong></a>() =0<br>用户私有扩展信息，好友不可见</p>                            |
| virtual [AddFriendAuthMode](classfloo\_1\_1\_b\_m\_x\_user\_profile.md#enum-addfriendauthmode) | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-addfriendauthmode"><strong>addFriendAuthMode</strong></a>() =0<br>加好友校验方式</p>                       |
| virtual const \[AuthQuestion] &                                                                | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-authquestion"><strong>authQuestion</strong></a>() =0<br>添加好友时的验证问题</p>                              |
| virtual const \[MessageSetting] &                                                              | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-messagesetting"><strong>messageSetting</strong></a>() =0<br>用户消息设定</p>                              |
| virtual bool                                                                                   | <p><a href="classfloo_1_1_b_m_x_user_profile.md#function-isautoacceptgroupinvite"><strong>isAutoAcceptGroupInvite</strong></a>() =0<br>收到群组邀请进群时是否自动同意进群</p> |

## Protected Functions

|   | Name                                                                                       |
| - | ------------------------------------------------------------------------------------------ |
|   | [**BMXUserProfile**](classfloo\_1\_1\_b\_m\_x\_user\_profile.md#function-bmxuserprofile)() |

## Public Types Documentation

### enum AddFriendAuthMode

| Enumerator     | Value | Description    |
| -------------- | ----- | -------------- |
| Open           |       | 无需验证，任何人可以加为好友 |
| NeedApproval   |       | 需要同意方可加为好友     |
| AnswerQuestion |       | 需要回答问题正确方可加为好友 |
| RejectAll      |       | 拒绝所有加好友申请      |

对方申请加好友时的验证方式

### enum UserCategory

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Normal     |       | 普通用户        |
| Advanced   |       | 高级用户        |

用户类型

## Public Functions Documentation

### function \~BMXUserProfile

```cpp
inline virtual ~BMXUserProfile()
```

析构函数

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function userId

```cpp
virtual int64_t userId() =0
```

用户ID（唯一）

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function category

```cpp
virtual UserCategory category() =0
```

用户策略

**Return**: UserCategory

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function username

```cpp
virtual const std::string & username() =0
```

用户名（唯一）

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function nickname

```cpp
virtual const std::string & nickname() =0
```

用户昵称

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function avatarRatelUrl

```cpp
virtual std::string avatarRatelUrl() =0
```

用户ratel服务器头像url

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function avatarUrl

```cpp
virtual std::string avatarUrl() =0
```

用户头像url

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function avatarPath

```cpp
virtual std::string avatarPath() =0
```

用户头像本地存储路径

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function avatarThumbnailPath

```cpp
virtual std::string avatarThumbnailPath() =0
```

用户头像缩略图本地存储路径

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function mobilePhone

```cpp
virtual const std::string & mobilePhone() =0
```

用户手机

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function email

```cpp
virtual const std::string & email() =0
```

用户邮箱

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function publicInfo

```cpp
virtual const JSON & publicInfo() =0
```

用户公开扩展信息，好友可见

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function privateInfo

```cpp
virtual const JSON & privateInfo() =0
```

用户私有扩展信息，好友不可见

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function addFriendAuthMode

```cpp
virtual AddFriendAuthMode addFriendAuthMode() =0
```

加好友校验方式

**Return**: AddFriendAuthMode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function authQuestion

```cpp
virtual const AuthQuestion & authQuestion() =0
```

添加好友时的验证问题

**Return**: \[AuthQuestion]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function messageSetting

```cpp
virtual const MessageSetting & messageSetting() =0
```

用户消息设定

**Return**: \[MessageSetting]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserProfile'></div>
```

### function isAutoAcceptGroupInvite

```cpp
virtual bool isAutoAcceptGroupInvite() =0
```

收到群组邀请进群时是否自动同意进群

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
