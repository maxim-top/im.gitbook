---
title: floo::BMXRosterItem
summary: 联系人 

---

# floo::BMXRosterItem



联系人 


`#include <bmx_roster_item.h>`

Inherits from BMXBaseObject

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[RosterRelation](classfloo_1_1_b_m_x_roster_item.md#enum-rosterrelation)** { Friend, Deleted, Stranger, Blocked}<br>好友关系  |
| enum class| **[AddFriendAuthMode](classfloo_1_1_b_m_x_roster_item.md#enum-addfriendauthmode)** { Open, NeedApproval, AnswerQuestion, RejectAll}<br>roster 被申请加好友时的验证方式  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXRosterItem](classfloo_1_1_b_m_x_roster_item.md#function-~bmxrosteritem)**()<br>析构函数  |
| virtual int64_t | **[rosterId](classfloo_1_1_b_m_x_roster_item.md#function-rosterid)**() =0<br>好友Id  |
| virtual const std::string & | **[username](classfloo_1_1_b_m_x_roster_item.md#function-username)**() =0<br>好友名  |
| virtual const std::string & | **[nickname](classfloo_1_1_b_m_x_roster_item.md#function-nickname)**() =0<br>好友昵称  |
| virtual std::string | **[avatarRatelUrl](classfloo_1_1_b_m_x_roster_item.md#function-avatarratelurl)**() =0<br>好友头像Ratel服务器地址  |
| virtual std::string | **[avatarUrl](classfloo_1_1_b_m_x_roster_item.md#function-avatarurl)**() =0<br>好友头像服务器地址  |
| virtual std::string | **[avatarPath](classfloo_1_1_b_m_x_roster_item.md#function-avatarpath)**() =0<br>好友头像本地存储路径  |
| virtual std::string | **[avatarThumbnailUrl](classfloo_1_1_b_m_x_roster_item.md#function-avatarthumbnailurl)**() =0<br>好友头像缩略图服务器地址  |
| virtual std::string | **[avatarThumbnailPath](classfloo_1_1_b_m_x_roster_item.md#function-avatarthumbnailpath)**() =0<br>好友头像缩略图本地存储路径  |
| virtual const JSON & | **[publicInfo](classfloo_1_1_b_m_x_roster_item.md#function-publicinfo)**() =0<br>扩展信息，用户设置的好友可以看到的信息，比如地址，个性签名等  |
| virtual const JSON & | **[alias](classfloo_1_1_b_m_x_roster_item.md#function-alias)**() =0<br>用户对好友添加的备注等信息  |
| virtual const JSON & | **[ext](classfloo_1_1_b_m_x_roster_item.md#function-ext)**() =0<br>用户的服务器扩展信息  |
| virtual const JSON & | **[localExt](classfloo_1_1_b_m_x_roster_item.md#function-localext)**() =0<br>用户的本地扩展信息  |
| virtual [RosterRelation](classfloo_1_1_b_m_x_roster_item.md#enum-rosterrelation) | **[relation](classfloo_1_1_b_m_x_roster_item.md#function-relation)**() =0<br>联系人关系  |
| virtual bool | **[isMuteNotification](classfloo_1_1_b_m_x_roster_item.md#function-ismutenotification)**() =0<br>是否提醒用户消息  |
| virtual [AddFriendAuthMode](classfloo_1_1_b_m_x_roster_item.md#enum-addfriendauthmode) | **[addFriendAuthMode](classfloo_1_1_b_m_x_roster_item.md#function-addfriendauthmode)**() =0<br>roster的好友添加验证方式。  |
| virtual const std::string & | **[authQuestion](classfloo_1_1_b_m_x_roster_item.md#function-authquestion)**() =0<br>roster的好友验证问题。  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXRosterItem](classfloo_1_1_b_m_x_roster_item.md#function-bmxrosteritem)**() |

## Public Types Documentation

### enum RosterRelation

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Friend | | 好友   |
| Deleted | | 被删除   |
| Stranger | | 陌生人   |
| Blocked | | 被加入黑名单   |



好友关系 

### enum AddFriendAuthMode

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Open | | 无需验证，任何人可以加为好友   |
| NeedApproval | | 需要同意方可加为好友   |
| AnswerQuestion | | 需要回答问题正确方可加为好友   |
| RejectAll | | 拒绝所有加好友申请   |



roster 被申请加好友时的验证方式 

## Public Functions Documentation

### function ~BMXRosterItem

```cpp
inline virtual ~BMXRosterItem()
```

析构函数 

### function rosterId

```cpp
virtual int64_t rosterId() =0
```

好友Id 

**Return**: int64_t 

### function username

```cpp
virtual const std::string & username() =0
```

好友名 

**Return**: std::string 

### function nickname

```cpp
virtual const std::string & nickname() =0
```

好友昵称 

**Return**: std::string 

### function avatarRatelUrl

```cpp
virtual std::string avatarRatelUrl() =0
```

好友头像Ratel服务器地址 

**Return**: std::string 

### function avatarUrl

```cpp
virtual std::string avatarUrl() =0
```

好友头像服务器地址 

**Return**: std::string 

### function avatarPath

```cpp
virtual std::string avatarPath() =0
```

好友头像本地存储路径 

**Return**: std::string 

### function avatarThumbnailUrl

```cpp
virtual std::string avatarThumbnailUrl() =0
```

好友头像缩略图服务器地址 

**Return**: std::string 

### function avatarThumbnailPath

```cpp
virtual std::string avatarThumbnailPath() =0
```

好友头像缩略图本地存储路径 

**Return**: std::string 

### function publicInfo

```cpp
virtual const JSON & publicInfo() =0
```

扩展信息，用户设置的好友可以看到的信息，比如地址，个性签名等 

**Return**: JSON(std::string) 

### function alias

```cpp
virtual const JSON & alias() =0
```

用户对好友添加的备注等信息 

**Return**: JSON(std::string) 

### function ext

```cpp
virtual const JSON & ext() =0
```

用户的服务器扩展信息 

**Return**: JSON(std::string) 

### function localExt

```cpp
virtual const JSON & localExt() =0
```

用户的本地扩展信息 

**Return**: JSON(std::string) 

### function relation

```cpp
virtual RosterRelation relation() =0
```

联系人关系 

**Return**: RosterRelation 

### function isMuteNotification

```cpp
virtual bool isMuteNotification() =0
```

是否提醒用户消息 

**Return**: bool 

### function addFriendAuthMode

```cpp
virtual AddFriendAuthMode addFriendAuthMode() =0
```

roster的好友添加验证方式。 

**Return**: AddFriendAuthMode 

### function authQuestion

```cpp
virtual const std::string & authQuestion() =0
```

roster的好友验证问题。 

**Return**: std::string 

## Protected Functions Documentation

### function BMXRosterItem

```cpp
inline BMXRosterItem()
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800