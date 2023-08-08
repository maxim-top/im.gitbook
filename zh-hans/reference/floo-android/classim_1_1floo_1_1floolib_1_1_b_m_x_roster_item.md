---
title: im::floo::floolib::BMXRosterItem
summary: 联系人
---

# im::floo::floolib::BMXRosterItem

联系人

Inherits from BMXBaseObject

## Public Functions

|                                 | Name                                                                                                                                                          |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                 | [**BMXRosterItem**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_roster\_item.md#function-bmxrosteritem)()                                                  |
| synchronized void               | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_roster\_item.md#function-delete)()                                                                |
| long                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-rosterid"><strong>rosterId</strong></a>()<br>好友Id</p>                                |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-username"><strong>username</strong></a>()<br>好友名</p>                                 |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-nickname"><strong>nickname</strong></a>()<br>好友昵称</p>                                |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarratelurl"><strong>avatarRatelUrl</strong></a>()<br>好友头像ratel服务器地址</p>          |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarurl"><strong>avatarUrl</strong></a>()<br>好友头像服务器地址</p>                         |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarpath"><strong>avatarPath</strong></a>()<br>好友头像本地存储路径</p>                      |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarthumbnailurl"><strong>avatarThumbnailUrl</strong></a>()<br>好友头像缩略图地址</p>       |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarthumbnailpath"><strong>avatarThumbnailPath</strong></a>()<br>好友头像缩略图本地存储路径</p> |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-publicinfo"><strong>publicInfo</strong></a>()<br>扩展信息，用户设置的好友可以看到的信息，比如地址，个性签名等</p>  |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-alias"><strong>alias</strong></a>()<br>用户对好友添加的备注等信息</p>                             |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-ext"><strong>ext</strong></a>()<br>用户的服务器扩展信息</p>                                    |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-localext"><strong>localExt</strong></a>()<br>用户的本地扩展信息</p>                           |
| BMXRosterItem.RosterRelation    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-relation"><strong>relation</strong></a>()<br>联系人关系</p>                               |
| boolean                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-ismutenotification"><strong>isMuteNotification</strong></a>()<br>是否提醒用户消息</p>        |
| BMXRosterItem.AddFriendAuthMode | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-addfriendauthmode"><strong>addFriendAuthMode</strong></a>()<br>roster的好友添加验证方式。</p>  |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-authquestion"><strong>authQuestion</strong></a>()<br>roster的好友验证问题。</p>              |

## Protected Functions

|      | Name                                                                                                                                                                                |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXRosterItem**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_roster\_item.md#function-bmxrosteritem)(long cPtr, boolean cMemoryOwn)                                           |
| void | [**finalize**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_roster\_item.md#function-finalize)()                                                                                  |
| long | [**getCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_roster\_item.md#function-getcptr)([BMXRosterItem](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_roster\_item.md) obj) |

## Public Attributes

|                | Name                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------ |
| transient long | [**swigCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_roster\_item.md#variable-swigcptr) |

## Public Functions Documentation

### function BMXRosterItem

```java
inline BMXRosterItem()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function delete

```java
inline synchronized void delete()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function rosterId

```java
inline long rosterId()
```

好友Id

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function username

```java
inline String username()
```

好友名

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function nickname

```java
inline String nickname()
```

好友昵称

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function avatarRatelUrl

```java
inline String avatarRatelUrl()
```

好友头像ratel服务器地址

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function avatarUrl

```java
inline String avatarUrl()
```

好友头像服务器地址

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function avatarPath

```java
inline String avatarPath()
```

好友头像本地存储路径

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function avatarThumbnailUrl

```java
inline String avatarThumbnailUrl()
```

好友头像缩略图地址

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function avatarThumbnailPath

```java
inline String avatarThumbnailPath()
```

好友头像缩略图本地存储路径

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function publicInfo

```java
inline String publicInfo()
```

扩展信息，用户设置的好友可以看到的信息，比如地址，个性签名等

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function alias

```java
inline String alias()
```

用户对好友添加的备注等信息

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function ext

```java
inline String ext()
```

用户的服务器扩展信息

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function localExt

```java
inline String localExt()
```

用户的本地扩展信息

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function relation

```java
inline BMXRosterItem.RosterRelation relation()
```

联系人关系

**Return**: \[RosterRelation]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function isMuteNotification

```java
inline boolean isMuteNotification()
```

是否提醒用户消息

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function addFriendAuthMode

```java
inline BMXRosterItem.AddFriendAuthMode addFriendAuthMode()
```

roster的好友添加验证方式。

**Return**: \[AddFriendAuthMode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function authQuestion

```java
inline String authQuestion()
```

roster的好友验证问题。

**Return**: std::string

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function BMXRosterItem

```java
inline BMXRosterItem(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function finalize

```java
inline void finalize()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

### function getCPtr

```java
static inline long getCPtr(
    BMXRosterItem obj
)
```

## Public Attributes Documentation

### variable swigCPtr

```java
transient long swigCPtr;
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```



Updated on 2022-01-26 at 17:18:31 +0800
