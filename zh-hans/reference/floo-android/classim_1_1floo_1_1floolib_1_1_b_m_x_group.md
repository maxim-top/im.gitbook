---
title: im::floo::floolib::BMXGroup
summary: 群组
---

# im::floo::floolib::BMXGroup

群组

Inherits from BMXBaseObject

## Public Classes

|       | Name                                                                                                                     |
| ----- | ------------------------------------------------------------------------------------------------------------------------ |
| class | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_1_1_announcement.md"><strong>Announcement</strong></a><br>群公告</p> |
| class | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group_1_1_application.md"><strong>Application</strong></a><br>群申请</p>   |

## Public Functions

|                         | Name                                                                                                                                                                   |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                         | [**BMXGroup**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group.md#function-bmxgroup)()                                                                            |
| synchronized void       | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group.md#function-delete)()                                                                                |
| long                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-groupid"><strong>groupId</strong></a>()<br>群Id</p>                                                  |
| BMXGroup.GroupType      | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-grouptype"><strong>groupType</strong></a>()<br>当前群组的群组类型（Private 私有群组，Public 公开群组，Chatroom 聊天室）</p> |
| String                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-mynickname"><strong>myNickname</strong></a>()<br>在群里的昵称</p>                                         |
| String                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-name"><strong>name</strong></a>()<br>群名称</p>                                                        |
| String                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-description"><strong>description</strong></a>()<br>群描述</p>                                          |
| String                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarratelurl"><strong>avatarRatelUrl</strong></a>()<br>群头像ratel地址</p>                             |
| String                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarurl"><strong>avatarUrl</strong></a>()<br>群头像</p>                                              |
| String                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarpath"><strong>avatarPath</strong></a>()<br>群头像下载后的本地路径</p>                                    |
| String                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarthumbnailurl"><strong>avatarThumbnailUrl</strong></a>()<br>群头像缩略图地址</p>                       |
| String                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-avatarthumbnailpath"><strong>avatarThumbnailPath</strong></a>()<br>群头像缩略图下载后的本地路径</p>               |
| long                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-createtime"><strong>createTime</strong></a>()<br>群创建时间</p>                                          |
| String                  | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-extension"><strong>extension</strong></a>()<br>群扩展信息</p>                                            |
| long                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-ownerid"><strong>ownerId</strong></a>()<br>群Owner</p>                                               |
| int                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-capacity"><strong>capacity</strong></a>()<br>最大人数</p>                                               |
| int                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-memberscount"><strong>membersCount</strong></a>()<br>群成员数量，包含Owner，admins 和members</p>              |
| int                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-adminscount"><strong>adminsCount</strong></a>()<br>群管理员数量</p>                                       |
| int                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-blocklistsize"><strong>blockListSize</strong></a>()<br>黑名单数量</p>                                    |
| int                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-bannedlistsize"><strong>bannedListSize</strong></a>()<br>禁言数量</p>                                   |
| int                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-sharedfilescount"><strong>sharedFilesCount</strong></a>()<br>群共享文件数量</p>                            |
| long                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-latestannouncementid"><strong>latestAnnouncementId</strong></a>()<br>最新群公告id</p>                    |
| BMXGroup.MsgPushMode    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-msgpushmode"><strong>msgPushMode</strong></a>()<br>群消息通知类型</p>                                      |
| BMXGroup.ModifyMode     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-modifymode"><strong>modifyMode</strong></a>()<br>群信息修改模式</p>                                        |
| BMXGroup.JoinAuthMode   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-joinauthmode"><strong>joinAuthMode</strong></a>()<br>入群审批模式</p>                                     |
| BMXGroup.InviteMode     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-invitemode"><strong>inviteMode</strong></a>()<br>入群邀请模式</p>                                         |
| BMXGroup.MsgMuteMode    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-msgmutemode"><strong>msgMuteMode</strong></a>()<br>群消息屏蔽模式</p>                                      |
| BMXGroup.GroupStatus    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-groupstatus"><strong>groupStatus</strong></a>()<br>当前群组的状态。（Normal 正常， Destroyed 以销毁）</p>           |
| boolean                 | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-ismember"><strong>isMember</strong></a>()<br>Deprecated use roleType instead.</p>                   |
| boolean                 | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-enablereadack"><strong>enableReadAck</strong></a>()<br>是否开启群消息已读功能</p>                              |
| boolean                 | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-historyvisible"><strong>historyVisible</strong></a>()<br>是否可以加载显示历史聊天记录</p>                         |
| BMXGroup.MemberRoleType | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-roletype"><strong>roleType</strong></a>()<br>成员在群组内的角色类型</p>                                        |
| long                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_group.md#function-banexpiretime"><strong>banExpireTime</strong></a>()<br>群组全员禁言到期时间</p>                               |

## Protected Functions

|      | Name                                                                                                                                                             |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXGroup**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group.md#function-bmxgroup)(long cPtr, boolean cMemoryOwn)                                         |
| void | [**finalize**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group.md#function-finalize)()                                                                      |
| long | [**getCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group.md#function-getcptr)([BMXGroup](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group.md) obj) |

## Public Attributes

|                | Name                                                                                      |
| -------------- | ----------------------------------------------------------------------------------------- |
| transient long | [**swigCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_group.md#variable-swigcptr) |

## Public Functions Documentation

### function BMXGroup

```java
inline BMXGroup()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function delete

```java
inline synchronized void delete()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function groupId

```java
inline long groupId()
```

群Id

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function groupType

```java
inline BMXGroup.GroupType groupType()
```

当前群组的群组类型（Private 私有群组，Public 公开群组，Chatroom 聊天室）

**Return**: \[GroupType]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function myNickname

```java
inline String myNickname()
```

在群里的昵称

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function name

```java
inline String name()
```

群名称

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function description

```java
inline String description()
```

群描述

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function avatarRatelUrl

```java
inline String avatarRatelUrl()
```

群头像ratel地址

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function avatarUrl

```java
inline String avatarUrl()
```

群头像

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function avatarPath

```java
inline String avatarPath()
```

群头像下载后的本地路径

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function avatarThumbnailUrl

```java
inline String avatarThumbnailUrl()
```

群头像缩略图地址

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function avatarThumbnailPath

```java
inline String avatarThumbnailPath()
```

群头像缩略图下载后的本地路径

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function createTime

```java
inline long createTime()
```

群创建时间

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function extension

```java
inline String extension()
```

群扩展信息

**Return**: JSON(std::string)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function ownerId

```java
inline long ownerId()
```

群Owner

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function capacity

```java
inline int capacity()
```

最大人数

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function membersCount

```java
inline int membersCount()
```

群成员数量，包含Owner，admins 和members

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function adminsCount

```java
inline int adminsCount()
```

群管理员数量

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function blockListSize

```java
inline int blockListSize()
```

黑名单数量

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function bannedListSize

```java
inline int bannedListSize()
```

禁言数量

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function sharedFilesCount

```java
inline int sharedFilesCount()
```

群共享文件数量

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function latestAnnouncementId

```java
inline long latestAnnouncementId()
```

最新群公告id

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function msgPushMode

```java
inline BMXGroup.MsgPushMode msgPushMode()
```

群消息通知类型

**Return**: \[MsgPushMode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function modifyMode

```java
inline BMXGroup.ModifyMode modifyMode()
```

群信息修改模式

**Return**: \[ModifyMode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function joinAuthMode

```java
inline BMXGroup.JoinAuthMode joinAuthMode()
```

入群审批模式

**Return**: \[JoinAuthMode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function inviteMode

```java
inline BMXGroup.InviteMode inviteMode()
```

入群邀请模式

**Return**: \[InviteMode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function msgMuteMode

```java
inline BMXGroup.MsgMuteMode msgMuteMode()
```

群消息屏蔽模式

**Return**: \[MsgMuteMode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function groupStatus

```java
inline BMXGroup.GroupStatus groupStatus()
```

当前群组的状态。（Normal 正常， Destroyed 以销毁）

**Return**: \[GroupStatus]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function isMember

```java
inline boolean isMember()
```

Deprecated use roleType instead.

**Return**: bool

当前用户是否是群成员

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function enableReadAck

```java
inline boolean enableReadAck()
```

是否开启群消息已读功能

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function historyVisible

```java
inline boolean historyVisible()
```

是否可以加载显示历史聊天记录

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function roleType

```java
inline BMXGroup.MemberRoleType roleType()
```

成员在群组内的角色类型

**Return**: \[MemberRoleType]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function banExpireTime

```java
inline long banExpireTime()
```

群组全员禁言到期时间

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function BMXGroup

```java
inline BMXGroup(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function finalize

```java
inline void finalize()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```

### function getCPtr

```java
static inline long getCPtr(
    BMXGroup obj
)
```

## Public Attributes Documentation

### variable swigCPtr

```java
transient long swigCPtr;
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXGroup'></div>
```



Updated on 2022-01-26 at 17:18:31 +0800
