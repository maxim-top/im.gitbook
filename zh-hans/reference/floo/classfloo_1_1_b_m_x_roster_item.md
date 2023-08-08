---
title: floo::BMXRosterItem
summary: 联系人
---

# floo::BMXRosterItem

联系人

`#include <bmx_roster_item.h>`

Inherits from BMXBaseObject

## Public Types

|            | Name                                                                                                                                                                                      |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class | <p><a href="classfloo_1_1_b_m_x_roster_item.md#enum-rosterrelation"><strong>RosterRelation</strong></a> { Friend, Deleted, Stranger, Blocked}<br>好友关系</p>                                 |
| enum class | <p><a href="classfloo_1_1_b_m_x_roster_item.md#enum-addfriendauthmode"><strong>AddFriendAuthMode</strong></a> { Open, NeedApproval, AnswerQuestion, RejectAll}<br>roster 被申请加好友时的验证方式</p> |

## Public Functions

|                                                                                               | Name                                                                                                                                            |
| --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual                                                                                       | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-~bmxrosteritem"><strong>~BMXRosterItem</strong></a>()<br>析构函数</p>                       |
| virtual int64\_t                                                                              | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-rosterid"><strong>rosterId</strong></a>() =0<br>好友Id</p>                                |
| virtual const std::string &                                                                   | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-username"><strong>username</strong></a>() =0<br>好友名</p>                                 |
| virtual const std::string &                                                                   | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-nickname"><strong>nickname</strong></a>() =0<br>好友昵称</p>                                |
| virtual std::string                                                                           | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-avatarratelurl"><strong>avatarRatelUrl</strong></a>() =0<br>好友头像Ratel服务器地址</p>          |
| virtual std::string                                                                           | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-avatarurl"><strong>avatarUrl</strong></a>() =0<br>好友头像服务器地址</p>                         |
| virtual std::string                                                                           | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-avatarpath"><strong>avatarPath</strong></a>() =0<br>好友头像本地存储路径</p>                      |
| virtual std::string                                                                           | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-avatarthumbnailurl"><strong>avatarThumbnailUrl</strong></a>() =0<br>好友头像缩略图服务器地址</p>    |
| virtual std::string                                                                           | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-avatarthumbnailpath"><strong>avatarThumbnailPath</strong></a>() =0<br>好友头像缩略图本地存储路径</p> |
| virtual const JSON &                                                                          | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-publicinfo"><strong>publicInfo</strong></a>() =0<br>扩展信息，用户设置的好友可以看到的信息，比如地址，个性签名等</p>  |
| virtual const JSON &                                                                          | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-alias"><strong>alias</strong></a>() =0<br>用户对好友添加的备注等信息</p>                             |
| virtual const JSON &                                                                          | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-ext"><strong>ext</strong></a>() =0<br>用户的服务器扩展信息</p>                                    |
| virtual const JSON &                                                                          | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-localext"><strong>localExt</strong></a>() =0<br>用户的本地扩展信息</p>                           |
| virtual [RosterRelation](classfloo\_1\_1\_b\_m\_x\_roster\_item.md#enum-rosterrelation)       | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-relation"><strong>relation</strong></a>() =0<br>联系人关系</p>                               |
| virtual bool                                                                                  | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-ismutenotification"><strong>isMuteNotification</strong></a>() =0<br>是否提醒用户消息</p>        |
| virtual [AddFriendAuthMode](classfloo\_1\_1\_b\_m\_x\_roster\_item.md#enum-addfriendauthmode) | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-addfriendauthmode"><strong>addFriendAuthMode</strong></a>() =0<br>roster的好友添加验证方式。</p>  |
| virtual const std::string &                                                                   | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-authquestion"><strong>authQuestion</strong></a>() =0<br>roster的好友验证问题。</p>              |

## Protected Functions

|   | Name                                                                                    |
| - | --------------------------------------------------------------------------------------- |
|   | [**BMXRosterItem**](classfloo\_1\_1\_b\_m\_x\_roster\_item.md#function-bmxrosteritem)() |

## Public Types Documentation

### enum RosterRelation

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Friend     |       | 好友          |
| Deleted    |       | 被删除         |
| Stranger   |       | 陌生人         |
| Blocked    |       | 被加入黑名单      |

好友关系

### enum AddFriendAuthMode

| Enumerator     | Value | Description    |
| -------------- | ----- | -------------- |
| Open           |       | 无需验证，任何人可以加为好友 |
| NeedApproval   |       | 需要同意方可加为好友     |
| AnswerQuestion |       | 需要回答问题正确方可加为好友 |
| RejectAll      |       | 拒绝所有加好友申请      |

roster 被申请加好友时的验证方式

## Public Functions Documentation

### function \~BMXRosterItem

```cpp
inline virtual ~BMXRosterItem()
```

析构函数

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```

### function rosterId

```cpp
virtual int64_t rosterId() =0
```

好友Id

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```

### function username

```cpp
virtual const std::string & username() =0
```

好友名

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```

### function nickname

```cpp
virtual const std::string & nickname() =0
```

好友昵称

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```

### function avatarRatelUrl

```cpp
virtual std::string avatarRatelUrl() =0
```

好友头像Ratel服务器地址

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```

### function avatarUrl

```cpp
virtual std::string avatarUrl() =0
```

好友头像服务器地址

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```

### function avatarPath

```cpp
virtual std::string avatarPath() =0
```

好友头像本地存储路径

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```

### function avatarThumbnailUrl

```cpp
virtual std::string avatarThumbnailUrl() =0
```

好友头像缩略图服务器地址

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```

### function avatarThumbnailPath

```cpp
virtual std::string avatarThumbnailPath() =0
```

好友头像缩略图本地存储路径

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```

### function publicInfo

```cpp
virtual const JSON & publicInfo() =0
```

扩展信息，用户设置的好友可以看到的信息，比如地址，个性签名等

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```

### function alias

```cpp
virtual const JSON & alias() =0
```

用户对好友添加的备注等信息

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```

### function ext

```cpp
virtual const JSON & ext() =0
```

用户的服务器扩展信息

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```

### function localExt

```cpp
virtual const JSON & localExt() =0
```

用户的本地扩展信息

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```

### function relation

```cpp
virtual RosterRelation relation() =0
```

联系人关系

**Return**: RosterRelation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```

### function isMuteNotification

```cpp
virtual bool isMuteNotification() =0
```

是否提醒用户消息

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```

### function addFriendAuthMode

```cpp
virtual AddFriendAuthMode addFriendAuthMode() =0
```

roster的好友添加验证方式。

**Return**: AddFriendAuthMode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```

### function authQuestion

```cpp
virtual const std::string & authQuestion() =0
```

roster的好友验证问题。

**Return**: std::string

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```

### function BMXRosterItem

```cpp
inline BMXRosterItem()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
