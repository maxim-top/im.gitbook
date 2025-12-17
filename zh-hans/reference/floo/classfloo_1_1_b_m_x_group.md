---
title: floo::BMXGroup
summary: 群组
---

# floo::BMXGroup

群组

`#include <bmx_group.h>`

Inherits from BMXBaseObject

## Public Types

|                                             | Name                                                                                                                                                                                                                                                                                          |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class                                  | <p><a href="classfloo_1_1_b_m_x_group.md#enum-invitationstatus"><strong>InvitationStatus</strong></a> { Pending, Accepted, Declined}<br>群邀请状态</p>                                                                                                                                             |
| enum class                                  | <p><a href="classfloo_1_1_b_m_x_group.md#enum-applicationstatus"><strong>ApplicationStatus</strong></a> { Pending, Accepted, Declined}<br>群申请状态</p>                                                                                                                                           |
| enum class                                  | <p><a href="classfloo_1_1_b_m_x_group.md#enum-msgpushmode"><strong>MsgPushMode</strong></a> { All, None, AdminOrAt, Admin, At}<br>消息通知类型</p>                                                                                                                                                  |
| enum class                                  | <p><a href="classfloo_1_1_b_m_x_group.md#enum-modifymode"><strong>ModifyMode</strong></a> { AdminOnly, Open}<br>群信息修改模式</p>                                                                                                                                                                   |
| enum class                                  | <p><a href="classfloo_1_1_b_m_x_group.md#enum-joinauthmode"><strong>JoinAuthMode</strong></a> { Open, NeedApproval, RejectAll}<br>进群验证方式</p>                                                                                                                                                  |
| enum class                                  | <p><a href="classfloo_1_1_b_m_x_group.md#enum-invitemode"><strong>InviteMode</strong></a> { AdminOnly, Open}<br>邀请入群模式</p>                                                                                                                                                                    |
| enum class                                  | <p><a href="classfloo_1_1_b_m_x_group.md#enum-updateinfotype"><strong>UpdateInfoType</strong></a> { UnKnown, Name, Description, Avatar, Owner, Ext, NickName, ModifyMode, JoinAuthMode, InviteMode, MsgPushMode, MsgMuteMode, ReadAckMode, HistoryVisibleMode, BanExpireTime}<br>群组信息更新类型</p> |
| enum class                                  | <p><a href="classfloo_1_1_b_m_x_group.md#enum-groupstatus"><strong>GroupStatus</strong></a> { Normal, Destroyed}<br>群组状态</p>                                                                                                                                                                  |
| enum class                                  | <p><a href="classfloo_1_1_b_m_x_group.md#enum-msgmutemode"><strong>MsgMuteMode</strong></a> { None, MuteNotification, MuteChat}<br>群组消息屏蔽模式</p>                                                                                                                                               |
| enum class                                  | [**MemberRoleType**](classfloo_1_1_b_m_x_group.md#enum-memberroletype) { GroupMember, GroupAdmin, GroupOwner, NotGroupMember}                                                                                                                                                                 |
| enum class                                  | [**GroupType**](classfloo_1_1_b_m_x_group.md#enum-grouptype) { Private, Public, Chatroom}                                                                                                                                                                                                     |
| typedef std::shared\_ptr< \[Member] >       | [**MemberPtr**](classfloo_1_1_b_m_x_group.md#typedef-memberptr)                                                                                                                                                                                                                               |
| typedef std::vector< MemberPtr >            | [**MemberList**](classfloo_1_1_b_m_x_group.md#typedef-memberlist)                                                                                                                                                                                                                             |
| typedef std::shared\_ptr< \[BannedMember] > | [**BannedMemberPtr**](classfloo_1_1_b_m_x_group.md#typedef-bannedmemberptr)                                                                                                                                                                                                                   |
| typedef std::vector< BannedMemberPtr >      | [**BannedMemberList**](classfloo_1_1_b_m_x_group.md#typedef-bannedmemberlist)                                                                                                                                                                                                                 |
| typedef std::shared\_ptr< \[SharedFile] >   | [**SharedFilePtr**](classfloo_1_1_b_m_x_group.md#typedef-sharedfileptr)                                                                                                                                                                                                                       |
| typedef std::vector< SharedFilePtr >        | [**SharedFileList**](classfloo_1_1_b_m_x_group.md#typedef-sharedfilelist)                                                                                                                                                                                                                     |
| typedef std::shared\_ptr< \[Announcement] > | [**AnnouncementPtr**](classfloo_1_1_b_m_x_group.md#typedef-announcementptr)                                                                                                                                                                                                                   |
| typedef std::vector< AnnouncementPtr >      | [**AnnouncementList**](classfloo_1_1_b_m_x_group.md#typedef-announcementlist)                                                                                                                                                                                                                 |
| typedef std::shared\_ptr< \[Invitation] >   | [**InvitationPtr**](classfloo_1_1_b_m_x_group.md#typedef-invitationptr)                                                                                                                                                                                                                       |
| typedef std::vector< InvitationPtr >        | [**InvitationList**](classfloo_1_1_b_m_x_group.md#typedef-invitationlist)                                                                                                                                                                                                                     |
| typedef std::shared\_ptr< \[Application] >  | [**ApplicationPtr**](classfloo_1_1_b_m_x_group.md#typedef-applicationptr)                                                                                                                                                                                                                     |
| typedef std::vector< ApplicationPtr >       | [**ApplicationList**](classfloo_1_1_b_m_x_group.md#typedef-applicationlist)                                                                                                                                                                                                                   |

## Public Functions

|                                                                            | Name                                                                                                                                                     |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual                                                                    | <p><a href="classfloo_1_1_b_m_x_group.md#function-~bmxgroup"><strong>~BMXGroup</strong></a>()<br>析构函数</p>                                                |
| virtual int64\_t                                                           | <p><a href="classfloo_1_1_b_m_x_group.md#function-groupid"><strong>groupId</strong></a>() =0<br>群Id</p>                                                  |
| virtual [GroupType](classfloo_1_1_b_m_x_group.md#enum-grouptype)           | <p><a href="classfloo_1_1_b_m_x_group.md#function-grouptype"><strong>groupType</strong></a>() =0<br>当前群组的群组类型（Private 私有群组，Public 公开群组，Chatroom 聊天室）</p> |
| virtual const std::string &                                                | <p><a href="classfloo_1_1_b_m_x_group.md#function-mynickname"><strong>myNickname</strong></a>() =0<br>在群里的昵称</p>                                         |
| virtual const std::string &                                                | <p><a href="classfloo_1_1_b_m_x_group.md#function-name"><strong>name</strong></a>() =0<br>群名称</p>                                                        |
| virtual const std::string &                                                | <p><a href="classfloo_1_1_b_m_x_group.md#function-description"><strong>description</strong></a>() =0<br>群描述</p>                                          |
| virtual std::string                                                        | <p><a href="classfloo_1_1_b_m_x_group.md#function-avatarratelurl"><strong>avatarRatelUrl</strong></a>() =0<br>群头像Ratel服务器Url</p>                         |
| virtual std::string                                                        | <p><a href="classfloo_1_1_b_m_x_group.md#function-avatarurl"><strong>avatarUrl</strong></a>() =0<br>群头像服务器Url</p>                                        |
| virtual std::string                                                        | <p><a href="classfloo_1_1_b_m_x_group.md#function-avatarpath"><strong>avatarPath</strong></a>() =0<br>群头像下载后的本地路径</p>                                    |
| virtual std::string                                                        | <p><a href="classfloo_1_1_b_m_x_group.md#function-avatarthumbnailurl"><strong>avatarThumbnailUrl</strong></a>() =0<br>群头像缩略图服务器Url</p>                   |
| virtual std::string                                                        | <p><a href="classfloo_1_1_b_m_x_group.md#function-avatarthumbnailpath"><strong>avatarThumbnailPath</strong></a>() =0<br>群头像缩略图下载后的本地路径</p>               |
| virtual int64\_t                                                           | <p><a href="classfloo_1_1_b_m_x_group.md#function-createtime"><strong>createTime</strong></a>() =0<br>群创建时间</p>                                          |
| virtual const JSON &                                                       | <p><a href="classfloo_1_1_b_m_x_group.md#function-extension"><strong>extension</strong></a>() =0<br>群扩展信息</p>                                            |
| virtual int64\_t                                                           | <p><a href="classfloo_1_1_b_m_x_group.md#function-ownerid"><strong>ownerId</strong></a>() =0<br>群Owner</p>                                               |
| virtual int                                                                | <p><a href="classfloo_1_1_b_m_x_group.md#function-capacity"><strong>capacity</strong></a>() =0<br>最大人数</p>                                               |
| virtual int                                                                | <p><a href="classfloo_1_1_b_m_x_group.md#function-memberscount"><strong>membersCount</strong></a>() =0<br>群成员数量，包含Owner，admins 和members</p>              |
| virtual int                                                                | <p><a href="classfloo_1_1_b_m_x_group.md#function-adminscount"><strong>adminsCount</strong></a>() =0<br>群管理员数量</p>                                       |
| virtual int                                                                | <p><a href="classfloo_1_1_b_m_x_group.md#function-blocklistsize"><strong>blockListSize</strong></a>() =0<br>黑名单数量</p>                                    |
| virtual int                                                                | <p><a href="classfloo_1_1_b_m_x_group.md#function-bannedlistsize"><strong>bannedListSize</strong></a>() =0<br>禁言数量</p>                                   |
| virtual int                                                                | <p><a href="classfloo_1_1_b_m_x_group.md#function-sharedfilescount"><strong>sharedFilesCount</strong></a>() =0<br>群共享文件数量</p>                            |
| virtual int64\_t                                                           | <p><a href="classfloo_1_1_b_m_x_group.md#function-latestannouncementid"><strong>latestAnnouncementId</strong></a>() =0<br>最新群公告id</p>                    |
| virtual [MsgPushMode](classfloo_1_1_b_m_x_group.md#enum-msgpushmode)       | <p><a href="classfloo_1_1_b_m_x_group.md#function-msgpushmode"><strong>msgPushMode</strong></a>() =0<br>群消息通知类型</p>                                      |
| virtual [ModifyMode](classfloo_1_1_b_m_x_group.md#enum-modifymode)         | <p><a href="classfloo_1_1_b_m_x_group.md#function-modifymode"><strong>modifyMode</strong></a>() =0<br>群信息修改模式</p>                                        |
| virtual [JoinAuthMode](classfloo_1_1_b_m_x_group.md#enum-joinauthmode)     | <p><a href="classfloo_1_1_b_m_x_group.md#function-joinauthmode"><strong>joinAuthMode</strong></a>() =0<br>入群审批模式</p>                                     |
| virtual [InviteMode](classfloo_1_1_b_m_x_group.md#enum-invitemode)         | <p><a href="classfloo_1_1_b_m_x_group.md#function-invitemode"><strong>inviteMode</strong></a>() =0<br>入群邀请模式</p>                                         |
| virtual [MsgMuteMode](classfloo_1_1_b_m_x_group.md#enum-msgmutemode)       | <p><a href="classfloo_1_1_b_m_x_group.md#function-msgmutemode"><strong>msgMuteMode</strong></a>() =0<br>群消息屏蔽模式</p>                                      |
| virtual [GroupStatus](classfloo_1_1_b_m_x_group.md#enum-groupstatus)       | <p><a href="classfloo_1_1_b_m_x_group.md#function-groupstatus"><strong>groupStatus</strong></a>() =0<br>当前群组的状态。（Normal 正常， Destroyed 以销毁）</p>           |
| virtual bool                                                               | <p><a href="classfloo_1_1_b_m_x_group.md#function-ismember"><strong>isMember</strong></a>() =0<br>Deprecated use roleType instead.</p>                   |
| virtual bool                                                               | <p><a href="classfloo_1_1_b_m_x_group.md#function-enablereadack"><strong>enableReadAck</strong></a>() =0<br>是否开启群消息已读功能</p>                              |
| virtual bool                                                               | <p><a href="classfloo_1_1_b_m_x_group.md#function-historyvisible"><strong>historyVisible</strong></a>() =0<br>是否可以加载显示历史聊天记录</p>                         |
| virtual [MemberRoleType](classfloo_1_1_b_m_x_group.md#enum-memberroletype) | <p><a href="classfloo_1_1_b_m_x_group.md#function-roletype"><strong>roleType</strong></a>() =0<br>成员在群组内的角色类型</p>                                        |
| virtual int64\_t                                                           | <p><a href="classfloo_1_1_b_m_x_group.md#function-banexpiretime"><strong>banExpireTime</strong></a>() =0<br>群组全员禁言到期时间</p>                               |

## Protected Functions

|   | Name                                                             |
| - | ---------------------------------------------------------------- |
|   | [**BMXGroup**](classfloo_1_1_b_m_x_group.md#function-bmxgroup)() |

## Public Types Documentation

### enum InvitationStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Pending    |       | 请求待处理       |
| Accepted   |       | 请求已接受       |
| Declined   |       | 请求已拒绝       |

群邀请状态

### enum ApplicationStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Pending    |       | 请求待处理       |
| Accepted   |       | 请求已接受       |
| Declined   |       | 请求已拒绝       |

群申请状态

### enum MsgPushMode

| Enumerator | Value | Description  |
| ---------- | ----- | ------------ |
| All        |       | 通知所有群消息      |
| None       |       | 所有消息都不通知     |
| AdminOrAt  |       | 只通知管理员或者被@消息 |
| Admin      |       | 只通知知管理员消息    |
| At         |       | 只通知被@消息      |

消息通知类型

### enum ModifyMode

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| AdminOnly  |       | 只有管理员可以     |
| Open       |       | 所有群成员都可以修改  |

群信息修改模式

### enum JoinAuthMode

| Enumerator   | Value | Description |
| ------------ | ----- | ----------- |
| Open         |       | 无需验证        |
| NeedApproval |       | 需要管理员批准     |
| RejectAll    |       | 拒绝所有申请      |

进群验证方式

### enum InviteMode

| Enumerator | Value | Description   |
| ---------- | ----- | ------------- |
| AdminOnly  |       | 只有管理员可以邀请他人进群 |
| Open       |       | 所有人都可以邀请他人进群  |

邀请入群模式

### enum UpdateInfoType

| Enumerator         | Value | Description     |
| ------------------ | ----- | --------------- |
| UnKnown            |       | 默认初始化值          |
| Name               |       | 修改群名称           |
| Description        |       | 修改群描述           |
| Avatar             |       | 修改群头像           |
| Owner              |       | 修改群主            |
| Ext                |       | 修改群扩展           |
| NickName           |       | 群成员修改昵称         |
| ModifyMode         |       | 修改群信息模式         |
| JoinAuthMode       |       | 修改进群验证方式        |
| InviteMode         |       | 修改邀请入群模式        |
| MsgPushMode        |       | 修改群消息推送类型       |
| MsgMuteMode        |       | 修改是否提醒消息        |
| ReadAckMode        |       | 是否开启群消息已读功能     |
| HistoryVisibleMode |       | 新群成员是否可见群历史聊天记录 |
| BanExpireTime      |       | 群组全员禁言到期时间      |

群组信息更新类型

### enum GroupStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Normal     |       | 群组状态正常      |
| Destroyed  |       | 群组已销毁       |

群组状态

### enum MsgMuteMode

| Enumerator       | Value | Description |
| ---------------- | ----- | ----------- |
| None             |       | 不屏蔽         |
| MuteNotification |       | 屏蔽本地消息通知    |
| MuteChat         |       | 屏蔽消息，不接收消息  |

群组消息屏蔽模式

### enum MemberRoleType

| Enumerator     | Value | Description |
| -------------- | ----- | ----------- |
| GroupMember    |       | 群成员         |
| GroupAdmin     |       | 群管理员        |
| GroupOwner     |       | 群主          |
| NotGroupMember |       | 非群成员        |

### enum GroupType

| Enumerator | Value | Description         |
| ---------- | ----- | ------------------- |
| Private    |       | 私有群组                |
| Public     |       | 公开群组(现在暂时没有开放次类型群组) |
| Chatroom   |       | 聊天室                 |

### typedef MemberPtr

```cpp
typedef std::shared_ptr<Member> floo::BMXGroup::MemberPtr;
```

### typedef MemberList

```cpp
typedef std::vector<MemberPtr> floo::BMXGroup::MemberList;
```

### typedef BannedMemberPtr

```cpp
typedef std::shared_ptr<BannedMember> floo::BMXGroup::BannedMemberPtr;
```

### typedef BannedMemberList

```cpp
typedef std::vector<BannedMemberPtr> floo::BMXGroup::BannedMemberList;
```

### typedef SharedFilePtr

```cpp
typedef std::shared_ptr<SharedFile> floo::BMXGroup::SharedFilePtr;
```

### typedef SharedFileList

```cpp
typedef std::vector<SharedFilePtr> floo::BMXGroup::SharedFileList;
```

### typedef AnnouncementPtr

```cpp
typedef std::shared_ptr<Announcement> floo::BMXGroup::AnnouncementPtr;
```

### typedef AnnouncementList

```cpp
typedef std::vector<AnnouncementPtr> floo::BMXGroup::AnnouncementList;
```

### typedef InvitationPtr

```cpp
typedef std::shared_ptr<Invitation> floo::BMXGroup::InvitationPtr;
```

### typedef InvitationList

```cpp
typedef std::vector<InvitationPtr> floo::BMXGroup::InvitationList;
```

### typedef ApplicationPtr

```cpp
typedef std::shared_ptr<Application> floo::BMXGroup::ApplicationPtr;
```

### typedef ApplicationList

```cpp
typedef std::vector<ApplicationPtr> floo::BMXGroup::ApplicationList;
```

## Public Functions Documentation

### function \~BMXGroup

```cpp
inline virtual ~BMXGroup()
```

析构函数

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function groupId

```cpp
virtual int64_t groupId() =0
```

群Id

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function groupType

```cpp
virtual GroupType groupType() =0
```

当前群组的群组类型（Private 私有群组，Public 公开群组，Chatroom 聊天室）

**Return**: GroupType

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function myNickname

```cpp
virtual const std::string & myNickname() =0
```

在群里的昵称

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function name

```cpp
virtual const std::string & name() =0
```

群名称

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function description

```cpp
virtual const std::string & description() =0
```

群描述

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function avatarRatelUrl

```cpp
virtual std::string avatarRatelUrl() =0
```

群头像Ratel服务器Url

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function avatarUrl

```cpp
virtual std::string avatarUrl() =0
```

群头像服务器Url

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function avatarPath

```cpp
virtual std::string avatarPath() =0
```

群头像下载后的本地路径

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function avatarThumbnailUrl

```cpp
virtual std::string avatarThumbnailUrl() =0
```

群头像缩略图服务器Url

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function avatarThumbnailPath

```cpp
virtual std::string avatarThumbnailPath() =0
```

群头像缩略图下载后的本地路径

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function createTime

```cpp
virtual int64_t createTime() =0
```

群创建时间

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function extension

```cpp
virtual const JSON & extension() =0
```

群扩展信息

**Return**: JSON(std::string)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function ownerId

```cpp
virtual int64_t ownerId() =0
```

群Owner

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function capacity

```cpp
virtual int capacity() =0
```

最大人数

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function membersCount

```cpp
virtual int membersCount() =0
```

群成员数量，包含Owner，admins 和members

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function adminsCount

```cpp
virtual int adminsCount() =0
```

群管理员数量

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function blockListSize

```cpp
virtual int blockListSize() =0
```

黑名单数量

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function bannedListSize

```cpp
virtual int bannedListSize() =0
```

禁言数量

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function sharedFilesCount

```cpp
virtual int sharedFilesCount() =0
```

群共享文件数量

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function latestAnnouncementId

```cpp
virtual int64_t latestAnnouncementId() =0
```

最新群公告id

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function msgPushMode

```cpp
virtual MsgPushMode msgPushMode() =0
```

群消息通知类型

**Return**: MsgPushMode

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function modifyMode

```cpp
virtual ModifyMode modifyMode() =0
```

群信息修改模式

**Return**: ModifyMode

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function joinAuthMode

```cpp
virtual JoinAuthMode joinAuthMode() =0
```

入群审批模式

**Return**: JoinAuthMode

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function inviteMode

```cpp
virtual InviteMode inviteMode() =0
```

入群邀请模式

**Return**: InviteMode

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function msgMuteMode

```cpp
virtual MsgMuteMode msgMuteMode() =0
```

群消息屏蔽模式

**Return**: MsgMuteMode

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function groupStatus

```cpp
virtual GroupStatus groupStatus() =0
```

当前群组的状态。（Normal 正常， Destroyed 以销毁）

**Return**: GroupStatus

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function isMember

```cpp
virtual bool isMember() =0
```

Deprecated use roleType instead.

**Return**: bool

当前用户是否是群成员

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function enableReadAck

```cpp
virtual bool enableReadAck() =0
```

是否开启群消息已读功能

**Return**: bool

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function historyVisible

```cpp
virtual bool historyVisible() =0
```

是否可以加载显示历史聊天记录

**Return**: bool

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function roleType

```cpp
virtual MemberRoleType roleType() =0
```

成员在群组内的角色类型

**Return**: MemberRoleType

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function banExpireTime

```cpp
virtual int64_t banExpireTime() =0
```

群组全员禁言到期时间

**Return**: int64\_t

## Protected Functions Documentation

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>

```

### function BMXGroup

```cpp
inline BMXGroup()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroup'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
